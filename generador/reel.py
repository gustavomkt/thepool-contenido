# -*- coding: utf-8 -*-
# Reel 1080x1920: fotos con zoom lento por beat, subtítulos en marca, cierre con logo. Audio = voz ElevenLabs.
import os, sys, subprocess, json
from PIL import Image, ImageDraw, ImageOps
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from render import OUT, POSTS, P, CTA_URL, F, CH, CR, OR, WH, GR, LG, SH_DARK, wrap, logo, squares

W, H, FPS = 1080, 1920, 30

def run(c): subprocess.run(c, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def dur(f):
    return float(subprocess.check_output(f'ffprobe -v error -show_entries format=duration -of csv=p=0 "{f}"', shell=True))

def silences(f):
    o = subprocess.run(f'ffmpeg -i "{f}" -af silencedetect=n=-35dB:d=0.22 -f null -', shell=True, capture_output=True, text=True).stderr
    st = [float(l.split("silence_start: ")[1]) for l in o.splitlines() if "silence_start" in l]
    en = [float(l.split("silence_end: ")[1].split(" ")[0]) for l in o.splitlines() if "silence_end" in l]
    return list(zip(st, en))

def beat_bounds(audio, texts):
    """Corta en los silencios más cercanos a la proporción de caracteres de cada beat."""
    D = dur(audio); sil = [(a + b) / 2 for a, b in silences(audio) if 0.3 < a < D - 0.3]
    tot = sum(len(t) for t in texts); acc = 0; cuts = []
    for t in texts[:-1]:
        acc += len(t); target = D * acc / tot
        c = min(sil, key=lambda s: abs(s - target)) if sil else target
        if cuts and c <= cuts[-1] + 0.5: c = target
        cuts.append(c)
    b = [0.0] + cuts + [D]
    return [(b[i], b[i + 1]) for i in range(len(texts))], D

def sub_png(text, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = F(800, 54); lines = wrap(d, text, f, W - 220)
    lh = 70; y = int(H * 0.70)
    for ln in lines:
        tw = d.textlength(ln, font=f); x = (W - tw) / 2
        d.rectangle([x - 22, y - 10, x + tw + 22, y + lh - 6], fill=CH + (235,))
        d.text((x, y), ln, font=f, fill=WH); y += lh + 4
    im.save(path)

def hook_png(text, path):
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    f = F(900, 66); y = 260
    for ln in wrap(d, text, f, W - 160):
        tw = d.textlength(ln, font=f); x = (W - tw) / 2
        d.rectangle([x - 24, y - 12, x + tw + 24, y + 78], fill=WH + (255,))
        d.text((x, y), ln, font=f, fill=CH); y += 96
    logo(im, True, (W - 200) // 2, 110, 200)
    im.save(path)

def end_png(path):
    im = Image.new("RGB", (W, H), CH); d = ImageDraw.Draw(im)
    logo(im, True, (W - 520) // 2, 560, 520)
    f = F(800, 40); tw = d.textlength(CTA_URL, font=f)
    d.rectangle([90, 1080, W - 90, 1200], fill=WH); d.text(((W - tw) / 2, 1118), CTA_URL, font=f, fill=CH)
    squares(d, (W - 39 * 20) // 2, 1560, 39, 14, 6, GR)
    im.save(path)

def clip(img, seconds, out, zoom_in=True):
    src = Image.open(P + img).convert("RGB")
    big = ImageOps.fit(src, (int(W * 1.25), int(H * 1.25)), Image.LANCZOS)
    tmp = out + ".png"; big.save(tmp)
    n = max(1, int(seconds * FPS))
    z = f"min(1+0.12*on/{n},1.12)" if zoom_in else f"max(1.12-0.12*on/{n},1)"
    run(f'ffmpeg -y -loop 1 -i "{tmp}" -vf "zoompan=z=\'{z}\':x=\'iw/2-(iw/zoom/2)\':y=\'ih/2-(ih/zoom/2)\':d={n}:s={W}x{H}:fps={FPS},format=yuv420p" -frames:v {n} -c:v libx264 -preset veryfast -crf 20 "{out}"')

def build(p, audio):
    wd = OUT + f"{p['id']}_{p['fecha']}_reel/"; tmpd = wd + "tmp/"; os.makedirs(tmpd, exist_ok=True)
    texts = [t for t, _ in p["voz"]]
    bounds, D = beat_bounds(audio, texts)
    total = D + 0.8
    clips = []; k = 0; inputs = []; filt = []; overlays = []
    for bi, ((t, imgs), (a, b)) in enumerate(zip(p["voz"], bounds)):
        if bi == len(bounds) - 1: b = total
        seg = b - a
        if imgs == ["END"]:
            ep = tmpd + "end.png"; end_png(ep); c = tmpd + f"c{k:02d}.mp4"
            run(f'ffmpeg -y -loop 1 -i "{ep}" -t {seg:.3f} -r {FPS} -vf format=yuv420p -c:v libx264 -preset veryfast -crf 20 "{c}"')
            clips.append(c); k += 1
        else:
            per = seg / len(imgs)
            for j, im in enumerate(imgs):
                c = tmpd + f"c{k:02d}.mp4"; clip(im, per, c, zoom_in=(k % 2 == 0)); clips.append(c); k += 1
        sp = tmpd + f"s{bi:02d}.png"; sub_png(t.replace("diez por ciento","10%").replace("Goldsmith cuarenta","Goldsmith 40"), sp); overlays.append((sp, a, b))
    lst = tmpd + "list.txt"; open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
    run(f'ffmpeg -y -f concat -safe 0 -i "{lst}" -c copy "{tmpd}base.mp4"')
    hp = tmpd + "hook.png"; hook_png(p["hook"], hp)
    ins = f'-i "{tmpd}base.mp4" -i "{audio}" -i "{hp}" ' + " ".join(f'-i "{o[0]}"' for o in overlays)
    fc = "[0:v][2:v]overlay=0:0:enable='lt(t,2.6)'[v0]"; last = "v0"
    for i, (_, a, b) in enumerate(overlays):
        fc += f";[{last}][{i+3}:v]overlay=0:0:enable='between(t,{a:.2f},{b:.2f})'[v{i+1}]"; last = f"v{i+1}"
    out = wd + f"ThePool_reel_{p['id']}.mp4"
    run(f'ffmpeg -y {ins} -filter_complex "{fc};[1:a]apad=pad_dur=0.8[a]" -map "[{last}]" -map "[a]" -t {total:.2f} -c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart "{out}"')
    open(wd + "caption_ig_fb.txt", "w").write(p["ig"]); open(wd + "caption_linkedin.txt", "w").write(p["li"])
    # portada (cover) para el feed
    cov = Image.open(P + next(i for _, ims in p["voz"] for i in ims if i != "END")).convert("RGB")
    cov = ImageOps.fit(cov, (W, H), Image.LANCZOS); cov.paste(Image.open(hp), (0, 0), Image.open(hp)); cov.save(wd + "portada.jpg", quality=92)
    return out, total, bounds

if __name__ == "__main__":
    pid, audio = sys.argv[1], sys.argv[2]
    p = next(x for x in POSTS if x["id"] == pid)
    print(build(p, audio))
