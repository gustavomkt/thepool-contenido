# -*- coding: utf-8 -*-
"""Construye las piezas de un calendario y publica media + calendar.json para la página de aprobación.

Uso:
  CAL=2026-11-23 python3 generador/build.py            # todas las piezas
  CAL=2026-11-23 python3 generador/build.py 03 05      # solo esas piezas

Reels: necesita calendarios/<CAL>/audio/<id>.mp3 (voz ElevenLabs). Si cambia el guion,
regenera la voz primero y guarda el mp3 con ese nombre.
"""
import os, sys, glob, json, shutil, subprocess
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render
from render import POSTS, OUT, CALDIR, render_post
from PIL import Image

MEDIA = os.path.join(CALDIR, "media")
ids = sys.argv[1:]

def sh(c): subprocess.run(c, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def build_one(p):
    pid = p["id"]
    dst = os.path.join(MEDIA, pid); shutil.rmtree(dst, ignore_errors=True); os.makedirs(dst)
    if p["tipo"] == "carrusel":
        shutil.rmtree(glob.glob(OUT + f"{pid}_*")[0], ignore_errors=True) if glob.glob(OUT + f"{pid}_*") else None
        files = render_post(p)
        for f in files:
            Image.open(f).save(os.path.join(dst, os.path.basename(f)), quality=86)
        shutil.copy(glob.glob(os.path.dirname(files[0]) + "/*.pdf")[0], os.path.join(dst, f"ThePool_{pid}_linkedin.pdf"))
    else:
        import reel
        audio = os.path.join(CALDIR, "audio", f"{pid}.mp3")
        out, _, _ = reel.build(p, audio)
        sh(f'ffmpeg -y -i "{out}" -c:v libx264 -preset veryfast -b:v 1100k -maxrate 1300k -bufsize 2600k '
           f'-pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart "{dst}/reel.mp4"')
        shutil.copy(os.path.join(os.path.dirname(out), "portada.jpg"), os.path.join(dst, "portada.jpg"))
        shutil.rmtree(os.path.join(os.path.dirname(out), "tmp"), ignore_errors=True)
    print("ok", pid)

def write_calendar_json():
    vfile = os.path.join(CALDIR, "versiones.json")
    vers = json.load(open(vfile)) if os.path.exists(vfile) else {}
    items = []
    for p in POSTS:
        d = os.path.join(MEDIA, p["id"])
        media = sorted(os.listdir(d)) if os.path.isdir(d) else []
        hook = (p["slides"][0]["title"] if p["tipo"] == "carrusel" else p["hook"]).replace("\n", " ")
        items.append(dict(id=p["id"], fecha=p["fecha"], dia=p["dia"], tipo=p["tipo"], pilar=p["pilar"],
                          gancho=hook, version=vers.get(p["id"], 1), media=media,
                          copy_ig_fb=p["ig"], copy_linkedin=p["li"],
                          guion=[t for t, _ in p.get("voz", [])]))
    json.dump(dict(calendario=os.environ["CAL"], posts=items), open(os.path.join(CALDIR, "calendar.json"), "w"),
              ensure_ascii=False, indent=1)

if __name__ == "__main__":
    for p in POSTS:
        if not ids or p["id"] in ids:
            build_one(p)
    write_calendar_json()
    shutil.rmtree(OUT, ignore_errors=True)
