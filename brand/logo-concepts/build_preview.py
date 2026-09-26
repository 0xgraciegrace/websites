"""Builds preview.html with every concept SVG inlined, so it opens standalone."""
from pathlib import Path

here = Path(__file__).parent
svg = {p.stem: p.read_text() for p in here.glob("*.svg")}

concepts = [
    ("a-mascota", "A · Mascota", "Pingüino de frente sosteniendo un cubito. El más expresivo y amigable; ideal como personaje para redes, bolsas y rótulos."),
    ("b-asomado", "B · Asomado", "Pingüino asomándose desde un cubo de hielo. Funciona como ícono de app, avatar de WhatsApp y favicon: se lee bien en tamaños pequeños."),
    ("c-tubo", "C · Tubo", "Pingüino de perfil construido con la forma del hielo en tubo. El más moderno y geométrico; conecta directamente con el producto estrella."),
]

def lockup(key, dark=False):
    fg = "#F4FBFC" if dark else "#0B1F3A"
    return f"""
    <div class="lockup {'dark' if dark else ''}">
      <div class="lk-icon">{svg[key]}</div>
      <div class="lk-text">
        <span class="lk-hielo">HIELO</span>
        <span class="lk-name" style="color:{fg}">PINGÜINO</span>
        <span class="lk-tag">Del Oriente</span>
      </div>
    </div>"""

cards = ""
for key, title, desc in concepts:
    cards += f"""
  <section class="concept">
    <header><h2>{title}</h2><p>{desc}</p></header>
    <div class="row">
      <div class="tile light">{svg[key]}</div>
      <div class="tile navy">{svg[key]}</div>
      <div class="tile teal">{svg[key]}</div>
    </div>
    <div class="row lockups">{lockup(key)}{lockup(key, dark=True)}</div>
    <div class="sizes"><span>Tamaños pequeños:</span>
      <div style="width:64px">{svg[key]}</div><div style="width:32px">{svg[key]}</div><div style="width:16px">{svg[key]}</div>
    </div>
  </section>"""

html = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hielo Pingüino · Conceptos de logo</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;700;900&display=swap" rel="stylesheet">
<style>
  :root {{ --navy:#0B1F3A; --teal:#2EC4C9; --orange:#FF7A1A; --ice:#F4FBFC; --sun:#FFC933; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; font-family:Rubik, system-ui, sans-serif; background:#E9F3F5; color:var(--navy); }}
  main {{ max-width:1040px; margin:0 auto; padding:40px 16px 80px; }}
  h1 {{ font-weight:900; font-size:clamp(28px,5vw,44px); margin:0 0 6px; }}
  .lead {{ margin:0 0 28px; color:#35506F; max-width:680px; }}
  .palette {{ display:flex; flex-wrap:wrap; gap:10px; margin-bottom:36px; }}
  .sw {{ flex:1 1 150px; border-radius:14px; padding:44px 12px 10px; font-size:13px; font-weight:500; }}
  .concept, .badge-sec {{ background:#fff; border-radius:22px; padding:24px; margin-bottom:28px; box-shadow:0 1px 0 rgba(11,31,58,.06); }}
  .concept h2, .badge-sec h2 {{ margin:0 0 4px; font-weight:900; }}
  .concept header p, .badge-sec p {{ margin:0 0 18px; color:#35506F; }}
  .row {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(200px,1fr)); gap:14px; margin-bottom:14px; }}
  .tile {{ border-radius:16px; padding:28px; display:grid; place-items:center; aspect-ratio:1; }}
  .tile svg {{ width:100%; max-width:170px; }}
  .light {{ background:var(--ice); }} .navy {{ background:var(--navy); }} .teal {{ background:var(--teal); }}
  .lockups {{ grid-template-columns:repeat(auto-fit,minmax(300px,1fr)); }}
  .lockup {{ display:flex; align-items:center; gap:16px; padding:22px; border-radius:16px; background:var(--ice); }}
  .lockup.dark {{ background:var(--navy); }}
  .lk-icon svg {{ width:84px; display:block; }}
  .lk-text {{ display:flex; flex-direction:column; line-height:1; }}
  .lk-hielo {{ font-weight:700; letter-spacing:.42em; font-size:14px; color:var(--teal); }}
  .lk-name {{ font-weight:900; font-size:40px; letter-spacing:-.01em; margin:4px 0 6px; }}
  .lk-tag {{ align-self:flex-start; background:var(--orange); color:#fff; font-weight:700; font-size:12px; padding:4px 10px; border-radius:99px; letter-spacing:.06em; text-transform:uppercase; }}
  .sizes {{ display:flex; align-items:end; gap:18px; color:#35506F; font-size:14px; flex-wrap:wrap; }}
  .sizes svg {{ width:100%; display:block; }}
  .badge-row {{ display:flex; flex-wrap:wrap; gap:20px; align-items:center; }}
  .badge-row > svg {{ width:200px; }} .badge-row div svg {{ width:100%; display:block; }}
  /* sticker outline so navy shapes stay visible on navy backgrounds */
  .navy svg, .lockup.dark .lk-icon svg {{ filter:drop-shadow(3px 0 0 var(--ice)) drop-shadow(-3px 0 0 var(--ice)) drop-shadow(0 3px 0 var(--ice)) drop-shadow(0 -3px 0 var(--ice)); }}
  .note {{ font-size:13px; color:#5B708A; }}
  @media (max-width:480px) {{ .lk-name {{ font-size:30px; }} .lk-icon svg {{ width:64px; }} }}
</style>
</head>
<body>
<main>
  <h1>Hielo Pingüino · Conceptos de logo</h1>
  <p class="lead">Tres direcciones para el ícono principal, más el sello regional <strong>Del Oriente</strong>. Todas usan la misma paleta: moderna, de alto contraste y deliberadamente distinta al azul y blanco clásico de la competencia.</p>

  <div class="palette">
    <div class="sw" style="background:var(--navy);color:#fff">Navy Profundo<br>#0B1F3A</div>
    <div class="sw" style="background:var(--teal)">Hielo Teal<br>#2EC4C9</div>
    <div class="sw" style="background:var(--orange);color:#fff">Naranja Eléctrico<br>#FF7A1A</div>
    <div class="sw" style="background:var(--ice);border:1px solid #d4e4e8">Blanco Hielo<br>#F4FBFC</div>
    <div class="sw" style="background:var(--sun)">Amarillo Sol<br>#FFC933</div>
  </div>
{cards}
  <section class="badge-sec">
    <h2>Sello regional · Del Oriente</h2>
    <p>Emblema secundario para bolsas y rótulos en el mercado oriental. Si la marca se expande a San Salvador u Occidente, el sello se cambia o se quita y el logo principal queda intacto.</p>
    <div class="badge-row">{svg['badge-del-oriente']}<div style="width:72px">{svg['badge-del-oriente']}</div></div>
  </section>
  <p class="note">Borradores de concepto. Una vez elegida la dirección, se refinan las formas, se convierte la tipografía a contornos y se entregan los archivos finales (SVG, PNG, favicon, versión a una tinta para impresión de bolsas).</p>
</main>
</body>
</html>
"""
(here / "preview.html").write_text(html)
print("wrote preview.html")
