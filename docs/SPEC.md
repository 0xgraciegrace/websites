# Pingüino del Oriente: Website Specification (draft v0.3)

Status: **Draft, in review.** Build starts only after the open questions in section 9 are answered.

---

## 1. Product summary

| | |
|---|---|
| **Brand name** | **Pingüino del Oriente** (spoken form: *"un Pingüino"*) |
| **Tagline options** | *Hecho para el calor del Oriente* / *El Hielo del Oriente* |
| **Company** | Locally owned ice plant in San Miguel, El Salvador |
| **Launch products** | Clear **tube ice** (hielo en tubo) and **ice cubes** (cubitos) |
| **Market** | Eastern El Salvador: San Miguel, La Unión, Usulután, Morazán |
| **Main competitor** | Hielo Polar (national incumbent, polar-bear mascot, blue/white arctic look) |

**Positioning in one line:** *Hecho para el calor del Oriente.* Ice made locally, delivered faster and colder than ice shipped in from San Salvador.

### Naming decision (recorded)
- ✅ **Pingüino del Oriente** is the brand name. Regional identity in Oriente is a deliberate defensive position against Hielo Polar.
- ✅ In the logo, **PINGÜINO** is the dominant word and **DEL ORIENTE** sits beneath it, so the short spoken form (*"dame un Pingüino"*) comes naturally.
- ❌ "Pingüino Oriental" is rejected because *oriental* reads as "Asian food" in local B2C usage.
- ⚠️ Accepted trade-off: the regional name may need a sub-brand or adjustment if the company later expands to San Salvador or Occidente.

---

## 2. Website goals

1. **B2B lead generation (primary conversion):** restaurants, marisquerías, fisheries, hotels and event organizers ask for a quote or open an account.
2. **B2C / retail awareness:** shoppers learn the brand and where to buy it. Tienditas and gas stations ask to become points of sale.
3. **Local trust:** show that the plant is real, local and reliable (address, photos, jobs, delivery zones).

**Primary call to action:** a WhatsApp chat with a pre-filled message (the default channel for businesses in El Salvador).
**Secondary call to action:** a phone call, then a simple quote form.

---

## 3. Audiences

| Segment | Who | What they care about | Message |
|---|---|---|---|
| **B2B** | Restaurants, marisquerías, fisheries, hotels, bars, event organizers | Reliability, delivery speed, melt rate, price per kg | *Reabastecimiento en menos de 2 horas en zona urbana.* Local plant, so no melt loss in transit. |
| **Retail partners** | Tienditas, gas stations, beach vendors (El Cuco, Las Flores) | Steady supply, margin, freezer visibility | *We don't run out on Semana Santa or at the fiestas de noviembre.* |
| **Consumers** | Families, parties, beach trips | Cold, clean, lasts in the heat | *El hielo que aguanta el calor del Oriente.* / *Frío de Verdad.* |

---

## 4. Sitemap

Single-page site in **Spanish** (es-SV), with anchor navigation. It can grow into several pages later.

1. **Header:** logo, nav (Productos · Negocios · Dónde comprar · Contacto), WhatsApp button
2. **Hero:** big headline, mascot, two CTAs (*Pedir para mi negocio* / *¿Dónde comprar?*)
3. **Productos:** Hielo en Tubo and Cubitos, with bag sizes and best uses
4. **¿Por qué Pingüino?:** 3–4 proof points (hecho en San Miguel, cristalino y purificado, dura más, entrega rápida)
5. **Para Negocios (B2B):** delivery SLA, volume and recurring orders, zones served, quote CTA
6. **Dónde comprar:** list or map of points of sale, plus a *"¿Querés vender Pingüino?"* CTA
7. **Nuestra planta / Nosotros:** local story, plant photos, water purification process, local jobs
8. **Preguntas frecuentes:** delivery hours, minimum order, payment methods, water quality
9. **Contacto:** WhatsApp, phone, address and map, hours
10. **Footer:** logo, *Del Oriente* badge, social links, legal

---

## 5. Draft copy (Spanish, to refine)

- **Hero headline:** *Hecho para el calor del Oriente.*
- **Hero sub:** *Hielo cristalino, purificado y producido aquí en San Miguel. Más frío, más rápido, más cerca.*
- **Tube ice:** *Hielo en Tubo: cristalino y de alta densidad. Ideal para bebidas, bares y eventos.*
- **Cubes:** *Cubitos: perfectos para la casa, la playa y el negocio.*
- **B2B:** *¿Tenés restaurante, marisquería o evento? Te abastecemos en menos de 2 horas en la zona urbana de San Miguel.*
- **Local pride:** *De migueleños, para el Oriente.*

---

## 6. Visual identity (summary; details in `/brand`)

- **Look:** bold, stylized and modern, with a playful mascot. Deliberately the opposite of Polar's corporate, realistic arctic style.
- **Palette:**

| Token | Hex | Use |
|---|---|---|
| Navy Profundo | `#0B1F3A` | Primary text, mascot body, dark backgrounds |
| Hielo Teal | `#2EC4C9` | Brand accent, ice, highlights |
| Naranja Eléctrico | `#FF7A1A` | Beak, feet, CTAs, "pop" in freezer chests |
| Blanco Hielo | `#F4FBFC` | Backgrounds, mascot belly |
| Amarillo Sol | `#FFC933` | Straw hat (shade `#E3A51A`), heat, promo badges |
| Azul Bufanda | `#1F5FC4` | Scarf and eyes |

- **Type:** a heavy rounded or geometric sans for headings (candidate: *Rubik* 800–900) and a clean sans for body text.
- **Logo system:** penguin icon + **PINGÜINO / DEL ORIENTE** wordmark + optional *Hecho en San Miguel* seal. See `brand/logo-concepts/`.
- **Chosen mascot (concept F), approved:** a modern, friendly flat-vector penguin that wears a *sombrero de palma* and a blue-white scarf (the scarf also says "cold"). It has an open smile, blue eyes and one flipper raised in greeting. It sits between the client's classic 3D reference and the earlier flat concepts.
  - `brand/logo-concepts/f-moderno.svg`: full body, for bags, signs, social media and the website hero
  - `brand/logo-concepts/f-moderno-icono.svg`: head only, for the app icon, WhatsApp avatar and favicon
  - `brand/logo-concepts/f-moderno-1tinta.svg`: one-color navy icon, for clear bags, stamps and embroidery
- **National symbols:** the blue-white scarf only hints at the flag. It does not reproduce the flag or use the coat of arms. Confirm with a lawyer or the CNR (Registro de la Propiedad Intelectual) before registering the trademark.

---

## 7. Technical requirements

- Static site: plain HTML, CSS and a little JS. No framework and no backend.
- Mobile-first. Most visitors arrive on a phone over mobile data, so pages should load fast (target under 1 MB total, images in WebP).
- WhatsApp deep links: `https://wa.me/503XXXXXXXX?text=...`
- Quote form: a hosted form service (Formspree or Google Forms) or WhatsApp only. **To decide.**
- Embedded Google Maps for the plant location.
- SEO: Spanish meta tags, Open Graph image, LocalBusiness schema.org markup (address, hours, phone).
- Hosting: GitHub Pages (free) with a custom domain. **To decide.**
- Accessibility: WCAG AA contrast and alt text on all images.

---

## 8. Out of scope for v1

Online ordering and payments, customer accounts, blog, English version.

---

## 9. Open questions

1. **Launch priority:** B2B volume first, retail first, or both equally? This decides the hero CTA.
2. **Bag sizes and formats** for tube ice and cubes (e.g. 5 lb / 10 lb / 20 lb / quintal?).
3. **Delivery zones and SLA:** is *< 2 h in urban San Miguel* something you can actually commit to? Which other municipalities are covered?
4. **Contact details:** WhatsApp number, phone, plant address, opening hours.
5. **Proof points:** water treatment (ósmosis inversa? UV?), health registration or permits, founding date.
6. **Photos:** do you have plant, product and team photos, or should we plan a photo shoot?
7. **Domain:** e.g. `pinguinodeloriente.com.sv` / `pinguinodeloriente.com`?
8. **Social media:** Facebook, Instagram and TikTok handles.
9. ~~**Logo direction**~~: concept F approved.
10. **Bag printing:** how many ink colors can the bag supplier print? This decides whether the bag uses the full-color mascot or the one-color version.
