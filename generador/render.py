# -*- coding: utf-8 -*-
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__))
CAL = os.environ.get("CAL") or sys.exit("export CAL=<carpeta del calendario, ej. 2026-11-23>")
CALDIR = os.path.join(HERE, "..", "calendarios", CAL)
sys.path.insert(0, CALDIR)
from content import POSTS, P, CTA_URL

B = os.path.join(HERE, "brand") + "/"
OUT = os.path.join(CALDIR, "build") + "/"
W, H = 1080, 1350
CH = (27, 27, 27); CR = (240, 240, 240); WH = (255, 255, 255); GR = (107, 107, 107); LG = (170, 170, 170); OR = WH; BODY = (68, 68, 68)
SH_DARK = (181, 101, 46); SH_LIGHT = (201, 201, 201)
F = lambda w, s: ImageFont.truetype(f"{B}OSO-{w}.ttf", s)
LOGO_W = Image.open(B + "logo-white.png").convert("RGBA")
LOGO_D = Image.open(B + "logo-dark.png").convert("RGBA")
M = 72  # margen
SEDES = {"Pol": "POLANCO", "Int": "INTERLOMAS", "Bos": "BOSQUES", "Ins": "INSURGENTES SUR", "SRa": "SAN RAFAEL"}
def sede_tag(d, img, x, y):
    s = SEDES.get(img[:3]);
    if s: tag(d, x, y, s, bg=WH, fg=CH, size=20)

def logo(im, dark_bg, x, y, w=170):
    L = (LOGO_W if dark_bg else LOGO_D).copy()
    L = L.resize((w, int(L.height * w / L.width)), Image.LANCZOS)
    im.paste(L, (x, y), L)

def fit(path, w, h, cy=0.5):
    im = Image.open(P + path).convert("RGB")
    return ImageOps.fit(im, (w, h), Image.LANCZOS, centering=(0.5, cy))

def wrap(d, text, font, maxw):
    out = []
    for para in text.split("\n"):
        line = ""
        for wd in para.split(" "):
            t = (line + " " + wd).strip()
            if d.textlength(t, font=font) <= maxw: line = t
            else:
                if line: out.append(line)
                line = wd
        out.append(line)
    return out

def text_block(d, x, y, text, font, fill, maxw, lh=1.12, shadow=None):
    for ln in wrap(d, text, font, maxw):
        if shadow: d.text((x + 6, y + 6), ln, font=font, fill=shadow)
        d.text((x, y), ln, font=font, fill=fill)
        y += int(font.size * lh)
    return y

def tag(d, x, y, text, bg=CH, fg=CR, size=24):
    f = F(700, size); tw = d.textlength(text, font=f)
    d.rectangle([x, y, x + tw + 32, y + size + 22], fill=bg)
    d.text((x + 16, y + 9), text, font=f, fill=fg)
    return y + size + 22

def counter(d, i, n, dark):
    f = F(700, 22); s = f"{i}/{n}"
    d.text((W - M - d.textlength(s, font=f), M + 8), s, font=f, fill=CR if dark else CH)

def squares(d, x, y, n=12, s=14, g=6, col=OR):
    for k in range(n): d.rectangle([x + k*(s+g), y, x + k*(s+g) + s, y + s], fill=col)

def s_cover(sl, i, n):
    band = 520
    im = Image.new("RGB", (W, H), CH)
    im.paste(fit(sl["img"], W, H - band, sl.get("crop", 0.5)), (0, 0))
    d = ImageDraw.Draw(im)
    sede_tag(d, sl["img"], M, H - band - 66)
    logo(im, True, M, H - band + 56, 150)
    y = H - band + 56
    tag(d, W - M - int(d.textlength(sl["eyebrow"], font=F(700, 22))) - 32, y + 4, sl["eyebrow"], bg=WH, fg=CH, size=22)
    y = text_block(d, M, H - band + 150, sl["title"], F(900, 74), WH, W - 2*M, 1.04)
    fs=F(700, 28); d.text((M, H - 92), sl["sub"], font=fs, fill=LG); ax=M+d.textlength(sl["sub"], font=fs)+18; d.polygon([(ax,H-86),(ax,H-62),(ax+18,H-74)], fill=LG)
    counter(d, i, n, True)
    return im

def s_photo(sl, i, n):
    band = 400
    im = Image.new("RGB", (W, H), CR)
    im.paste(fit(sl["img"], W, H - band, sl.get("crop", 0.5)), (0, 0))
    d = ImageDraw.Draw(im)
    y = H - band
    tag(d, M, y - 36, sl["kicker"], size=24)
    y = text_block(d, M, y + 52, sl["title"], F(900, 60), CH, W - 2*M, 1.06)
    y = text_block(d, M, y + 14, sl["body"], F(600, 32), BODY, W - 2*M - 40, 1.3)
    squares(d, M, H - 60, 6, 12, 6, CH)
    logo(im, False, W - M - 110, H - 70, 110)
    counter(d, i, n, False) if False else None
    return im

def s_list(sl, i, n):
    im = Image.new("RGB", (W, H), CR); d = ImageDraw.Draw(im)
    logo(im, False, M, M, 140)
    counter(d, i, n, False)
    y = tag(d, M, 300, sl["eyebrow"], size=26) + 44
    y = text_block(d, M, y, sl["title"], F(900, 92), CH, W - 2*M, 1.04) + 50
    fb = F(700, 44)
    for it in sl["items"]:
        d.rectangle([M, y + 14, M + 26, y + 40], fill=CH)
        y = text_block(d, M + 50, y, it, fb, CH, W - 2*M - 60, 1.25) + 34
    if sl.get("note"):
        d.text((M, H - 100), sl["note"], font=F(600, 24), fill=BODY)
    d.rectangle([0, H - 40, W, H], fill=CH)
    return im

def s_price(sl, i, n):
    im = Image.new("RGB", (W, H), CR)
    ph = 560
    im.paste(fit(sl["img"], W, ph), (0, 0))
    d = ImageDraw.Draw(im)
    d.rectangle([0, ph, W, H], fill=CR)
    sede_tag(d, sl["img"], M, ph - 62)
    y = tag(d, M, ph + 60, sl["eyebrow"], size=26) + 30
    fp = F(900, 130)
    d.text((M, y), sl["price"], font=fp, fill=CH)
    pw = d.textlength(sl["price"], font=fp)
    d.text((M + pw + 20, y + 86), sl["unit"], font=F(800, 30), fill=GR)
    y += 170
    text_block(d, M, y, sl["body"], F(600, 34), BODY, W - 2*M - 40, 1.3)
    d.rectangle([0, H - 40, W, H], fill=CH)
    return im

def s_cta(sl, i, n):
    im = Image.new("RGB", (W, H), CH); d = ImageDraw.Draw(im)
    logo(im, True, M, M, 200)
    y = text_block(d, M, 420, sl["title"], F(900, 92), WH, W - 2*M, 1.04) + 40
    text_block(d, M, y, sl["body"], F(600, 36), LG, W - 2*M - 60, 1.3)
    f = F(800, 30); bh = 110
    d.rectangle([M, H - 250, W - M, H - 250 + bh], fill=WH)
    tw = d.textlength(CTA_URL, font=f)
    d.text(((W - tw) / 2, H - 250 + 38), CTA_URL, font=f, fill=CH)
    squares(d, M, H - 90, 30, 14, 6, GR)
    return im

R = dict(cover=s_cover, photo=s_photo, list=s_list, price=s_price, cta=s_cta)

def render_post(p):
    od = OUT + f"{p['id']}_{p['fecha']}_carrusel/"; os.makedirs(od, exist_ok=True)
    files = []
    for i, sl in enumerate(p["slides"], 1):
        im = R[sl["t"]](sl, i, len(p["slides"]))
        f = od + f"{i:02d}.jpg"; im.save(f, quality=92); files.append(f)
    # PDF para LinkedIn (documento)
    ims = [Image.open(f).convert("RGB") for f in files]
    ims[0].save(od + f"ThePool_{p['id']}_linkedin.pdf", save_all=True, append_images=ims[1:], resolution=150)
    open(od + "caption_ig_fb.txt", "w").write(p["ig"]); open(od + "caption_linkedin.txt", "w").write(p["li"])
    return files

if __name__ == "__main__":
    ids = sys.argv[1:]
    for p in POSTS:
        if p["tipo"] == "carrusel" and (not ids or p["id"] in ids):
            print(p["id"], len(render_post(p)))
