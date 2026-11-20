# -*- coding: utf-8 -*-
# Calendario The Pool: 23-nov a 18-dic 2026. Lun carrusel, Mié reel, Vie carrusel.
import os
P = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "generador", "fotos") + "/"

TAGS = "#ThePoolMX #CoworkingCDMX #OficinasCDMX #OficinaDeBarrio"
CTA_URL = "AGENDA TU RECORRIDO · THEPOOL.MX"

POSTS = [
# ---------------- SEMANA 1 ----------------
dict(id="01", fecha="2026-11-23", dia="Lun", tipo="carrusel", pilar="Sedes",
 slides=[
  dict(t="cover", img="Pol_portada.jpg", eyebrow="CDMX Y EDO. MEX", title="CINCO BARRIOS.\nUNA MISMA\nCOMUNIDAD.", sub="Desliza y encuentra el tuyo"),
  dict(t="photo", img="Pol_of13_cap3_3.jpg", kicker="POLANCO · GOLDSMITH 40", title="Junto al Parque Lincoln", body="Para los que cierran tratos en la comida y regresan caminando."),
  dict(t="photo", img="Int_portada.jpg", kicker="INTERLOMAS · VÍA MAGNA 19", title="La oficina cerca de casa", body="Equipos de 2 a +35 personas sin cruzar la ciudad."),
  dict(t="photo", img="Bos_portada.jpg", kicker="BOSQUES · BOSQUE DE ALISOS 29", title="Trabajar con terraza", body="Áreas verdes, oficinas con terraza privada y mucha calma."),
  dict(t="photo", img="Ins_portada.jpg", kicker="INSURGENTES SUR · FRENTE A GALERÍAS", title="Bajas del Metrobús y llegaste", body="Lista de espera abierta."),
  dict(t="photo", img="SRa_portada.jpg", kicker="SAN RAFAEL · NUEVA SEDE", title="De 4 a 73 personas", body="Oficinas listas para usar y terraza de 245 metros."),
  dict(t="cta", title="¿CUÁL ES\nTU BARRIO?", body="Cuéntanos en comentarios. O mejor: ven a conocerlo en persona."),
 ],
 ig="""Cinco sedes, cinco barrios, una sola comunidad.

Nunca nos convenció la torre corporativa a una hora de tu casa. Lo nuestro es la oficina que queda cerca de donde haces tu vida: tu café, tu gym, la comida con tu mamá.

📍 Polanco · Interlomas · Bosques · Insurgentes Sur · San Rafael

¿Cuál te queda más cerca? Te leemos 👇
Agenda tu recorrido en thepool.mx

""" + TAGS,
 li="""Cinco sedes, cinco barrios, una misma comunidad.

En The Pool creemos que la oficina debe estar cerca de donde vive tu equipo, no a una hora de tráfico. Por eso estamos en Polanco, Interlomas, Bosques de las Lomas, Insurgentes Sur y San Rafael.

Oficinas privadas desde 2 personas, coworking y salas de juntas. ¿Cuál le queda mejor a tu equipo?

Agenda un recorrido: thepool.mx

#Coworking #OficinasPrivadas #CDMX"""),

dict(id="02", fecha="2026-11-25", dia="Mié", tipo="reel", pilar="Comunidad · Polanco",
 voz=[
  ("Llegas a Goldsmith 40, saludas en recepción y agarras tu café.", ["Pol_portada.jpg"]),
  ("Tu equipo ya está instalado. Cuatro, ocho, los que sean.", ["Pol_of3_cap4_1.jpg","Pol_of19_cap8_1.jpg"]),
  ("Junta a las once, en la sala.", ["Pol_of8_cap9_0.jpg"]),
  ("Comes a unos pasos del Parque Lincoln.", ["Pol_of5_cap8_0.jpg"]),
  ("Y en la tarde, alguien de la comunidad te presenta a tu próximo cliente.", ["Pol_of5_cap8_1.jpg","Pol_portada.jpg"]),
  ("Eso es trabajar en tu barrio. The Pool Polanco. Agenda tu recorrido.", ["END"]),
 ],
 hook="UN DÍA EN THE POOL POLANCO",
 ig="""Un día normal en Polanco 👇

Café en recepción, tu equipo en su oficina, junta a las 11, comida cerca del Parque Lincoln y, si tienes suerte, un nuevo cliente que conociste en el pasillo.

Eso es tener oficina en tu barrio.

📍 Goldsmith 40, Polanco
Agenda tu recorrido en thepool.mx

""" + TAGS + " #Polanco",
 li="""Así se ve un día en The Pool Polanco.

Recepción, oficinas privadas para equipos de 2 a 9 personas, salas de juntas y una comunidad donde los contactos pasan solos.

Goldsmith 40, Polanco. Agenda un recorrido: thepool.mx

#Coworking #Polanco #OficinasPrivadas"""),

dict(id="03", fecha="2026-11-27", dia="Vie", tipo="carrusel", pilar="Promo Buen Fin",
 slides=[
  dict(t="cover", img="Pol_of19_cap8_0.jpg", eyebrow="BUEN FIN · SOLO NOVIEMBRE", title="10% MENOS\nEN TU OFICINA\nPRIVADA.", sub="Quedan pocos días"),
  dict(t="list", eyebrow="ASÍ DE FÁCIL", title="Dos formas de\naprovecharlo", items=["Contratas tu oficina en noviembre: 10% de descuento.","O te vas al plan anual: 10% de descuento.","Te ayudamos a elegir sede y tamaño."], note="Precios + IVA. Sujeto a disponibilidad."),
  dict(t="photo", img="Pol_of3_cap4_0.jpg", kicker="POLANCO · OFICINA 3", title="Para 4 personas", body="Amueblada y lista para entrar."),
  dict(t="photo", img="Bos_of9_cap6_1.jpg", kicker="BOSQUES · OFICINA 9", title="Para 6 personas", body="Luz natural y mucho verde alrededor."),
  dict(t="photo", img="Int_of211_cap12_0.jpg", kicker="INTERLOMAS · OFICINA 211", title="Para 12 personas", body="Para el equipo que ya no cabe en tu sala."),
  dict(t="cta", title="TERMINA EL\n30 DE NOVIEMBRE", body="Escríbenos por DM o agenda tu recorrido esta semana."),
 ],
 ig="""Buen Fin, pero para tu equipo 🏊

Todo noviembre tienes 10% de descuento si contratas tu oficina privada, o 10% si te vas al plan anual.

Polanco, Interlomas, Bosques, Insurgentes Sur y San Rafael. Oficinas listas para entrar, desde 2 personas.

Se acaba el 30 de noviembre. Mándanos DM y te decimos qué hay disponible.

Precios + IVA. Sujeto a disponibilidad.

""" + TAGS + " #BuenFin",
 li="""Buen Fin en The Pool: 10% de descuento al contratar una oficina privada en noviembre, o 10% al contratar el plan anual.

Oficinas amuebladas y listas para operar en Polanco, Interlomas, Bosques, Insurgentes Sur y San Rafael.

Válido hasta el 30 de noviembre. Precios + IVA, sujeto a disponibilidad.
thepool.mx

#BuenFin #OficinasPrivadas #CDMX"""),

# ---------------- SEMANA 2 ----------------
dict(id="04", fecha="2026-11-30", dia="Lun", tipo="carrusel", pilar="Opciones",
 slides=[
  dict(t="cover", img="Pol_of5_cap8_1.jpg", eyebrow="OPCIONES", title="NO TODOS\nTRABAJAMOS\nIGUAL.", sub="Encuentra tu plan"),
  dict(t="price", img="Pol_portada.jpg", eyebrow="DAY PASS", price="$450", unit="+ IVA", body="Un día de coworking. Para probar, o para cuando ya no aguantas trabajar desde casa."),
  dict(t="price", img="Int_portada.jpg", eyebrow="LITE PASS", price="$2,000", unit="+ IVA", body="10 accesos al coworking. Vienes cuando quieras."),
  dict(t="price", img="Bos_portada.jpg", eyebrow="NACIONAL", price="$3,900", unit="+ IVA / MES", body="Coworking 24/7, acceso a todas las sedes y 8 horas de sala de juntas."),
  dict(t="price", img="Pol_of13_cap3_0.jpg", eyebrow="OFICINA PRIVADA", price="Desde 2", unit="PERSONAS", body="Amueblada, con internet y recepción. Tu equipo, tu puerta."),
  dict(t="price", img="Pol_of9_cap5_0.jpg", eyebrow="DOMICILIO FISCAL", price="$24,000", unit="+ IVA / AÑO", body="Tu dirección comercial en un barrio que suena bien."),
  dict(t="cta", title="¿NO SABES\nCUÁL ES EL TUYO?", body="Mándanos DM con cuántas personas son y cómo trabajan. Te recomendamos uno."),
 ],
 ig="""Hay quien viene un día a la semana y hay equipos de 12 que ya viven aquí. Por eso no tenemos un solo plan.

☕ Day Pass · $450 + IVA
🎟️ Lite Pass · 10 accesos · $2,000 + IVA
🌎 Nacional · $3,900 + IVA/mes, acceso 24/7 a todas las sedes
🚪 Oficina privada · desde 2 personas
📬 Domicilio fiscal · $24,000 + IVA/año

¿Cuál eres tú? Si no sabes, mándanos DM y te ayudamos.

""" + TAGS,
 li="""No todos los equipos trabajan igual, por eso en The Pool hay varias formas de entrar:

• Day Pass: $450 + IVA
• Lite Pass (10 accesos): $2,000 + IVA
• Plan Nacional: $3,900 + IVA/mes, coworking 24/7 en todas las sedes y 8 h de sala de juntas
• Oficina privada: desde 2 personas
• Domicilio fiscal: $24,000 + IVA/año

thepool.mx

#Coworking #FlexibleWorkspace #CDMX"""),

dict(id="05", fecha="2026-12-02", dia="Mié", tipo="reel", pilar="Sedes · Bosques",
 voz=[
  ("¿Y si tu oficina tuviera terraza?", ["Bos_portada.jpg"]),
  ("En Bosques de las Lomas trabajas rodeado de verde.", ["Bos_of24_cap3_2.jpg"]),
  ("Oficinas para tres, para seis, con luz natural todo el día.", ["Bos_of9_cap6_1.jpg","Bos_of24_cap3_0.jpg"]),
  ("Y cuando la junta se pone pesada, sales a tomar aire.", ["Bos_portada.jpg"]),
  ("The Pool Bosques. Agenda tu recorrido.", ["END"]),
 ],
 hook="¿Y SI TU OFICINA TUVIERA TERRAZA?",
 ig="""Spoiler: sí la tiene 🌿

En Bosques de las Lomas trabajas rodeado de verde, con oficinas para 3 o 6 personas, luz natural y terraza para cuando necesitas aire.

📍 Bosque de Alisos 29, Bosques de las Lomas
Agenda tu recorrido en thepool.mx

""" + TAGS + " #BosquesDeLasLomas",
 li="""Una oficina con terraza en Bosques de las Lomas.

The Pool Bosques: oficinas privadas con luz natural, áreas verdes y un ambiente tranquilo para trabajar con foco.

Bosque de Alisos 29. Agenda un recorrido: thepool.mx

#OficinasPrivadas #Coworking #CDMX"""),

dict(id="06", fecha="2026-12-04", dia="Vie", tipo="carrusel", pilar="Sedes · Interlomas",
 slides=[
  dict(t="cover", img="Int_portada.jpg", eyebrow="INTERLOMAS", title="TU EQUIPO\nSIN CRUZAR\nLA CIUDAD.", sub="De 2 a +35 personas"),
  dict(t="photo", img="Int_of207_cap11_0.jpg", kicker="OFICINA 207", title="Hasta 11 personas", body="Vista abierta y luz todo el día."),
  dict(t="photo", img="Int_of211_cap12_1.jpg", kicker="OFICINA 211", title="Hasta 12 personas", body="Para cuando el equipo creció más rápido que el plan."),
  dict(t="photo", img="Int_of211_cap12_3.jpg", kicker="ESPACIOS PARA JUNTAS", title="Café, plática y decisiones", body="Sin salir del edificio."),
  dict(t="list", eyebrow="INCLUYE", title="Llegas y\nya trabajas", items=["Wi-fi de alta velocidad","Recepción","Cafetería y área lounge","Acceso 24/7","Pet friendly"]),
  dict(t="cta", title="VEN A\nCONOCERLA", body="Vía Magna 19, Interlomas. Agenda tu recorrido."),
 ],
 ig="""Si tu equipo vive en la zona poniente, ¿para qué cruzar la ciudad todos los días?

En Interlomas tenemos oficinas privadas desde 2 personas hasta equipos de +35, listas para usarse desde el día uno. Wi-fi, recepción, cafetería, lounge y acceso 24/7.

📍 Vía Magna 19, Interlomas
Agenda tu recorrido en thepool.mx

""" + TAGS + " #Interlomas",
 li="""Para equipos de la zona poniente: oficinas privadas en Interlomas para 2 a +35 personas, listas para operar.

Wi-fi de alta velocidad, recepción, cafetería, lounge y acceso 24/7. Menos tráfico, más tiempo para lo importante.

Vía Magna 19. Agenda un recorrido: thepool.mx

#Interlomas #OficinasPrivadas #Coworking"""),

# ---------------- SEMANA 3 ----------------
dict(id="07", fecha="2026-12-07", dia="Lun", tipo="carrusel", pilar="Comunidad",
 slides=[
  dict(t="cover", img="Pol_of5_cap8_0.jpg", eyebrow="COMUNIDAD", title="LO QUE NO\nVIENE EN EL\nCONTRATO.", sub="Desliza"),
  dict(t="photo", img="Pol_portada.jpg", kicker="01 · POLANCO", title="El vecino de escritorio", body="Que te presenta a tu próximo cliente."),
  dict(t="photo", img="Int_portada.jpg", kicker="02 · INTERLOMAS", title="El café de las 9", body="Con gente que no es de tu equipo (y eso se agradece)."),
  dict(t="photo", img="Bos_portada.jpg", kicker="03 · BOSQUES", title="La junta que se mudó a la terraza", body="Porque hay ideas que salen mejor al aire libre."),
  dict(t="list", eyebrow="Y TAMBIÉN", title="Lo que sí está\nen el contrato", items=["Eventos de networking","Promovemos tu marca en la comunidad","Pet friendly","Parking de bicis","Precios preferenciales en servicios"]),
  dict(t="cta", title="¿YA ERES\nPOOLER?", body="Etiqueta a tu compañero de escritorio favorito."),
 ],
 ig="""Lo mejor de The Pool no viene en el contrato 🤝

El vecino de escritorio que te pasa un cliente. El café de las 9 con gente de otras industrias. La junta que terminó en la terraza.

Eso es la comunidad. El wi-fi y la recepción también están, pero esto es lo que hace que la gente se quede.

Etiqueta a tu pooler favorito 👇

""" + TAGS + " #Comunidad",
 li="""Lo que más valoran los equipos en The Pool no viene en el contrato: los contactos que surgen en el pasillo, el café con gente de otras industrias, los eventos de networking.

Oficinas y coworking en 5 barrios de CDMX y Edo. Mex.
thepool.mx

#Comunidad #Coworking #Networking"""),

dict(id="08", fecha="2026-12-09", dia="Mié", tipo="reel", pilar="Sedes · Todas",
 voz=[
  ("Polanco, para cerrar tratos y comer bien.", ["Pol_portada.jpg"]),
  ("Interlomas, para no cruzar la ciudad.", ["Int_portada.jpg"]),
  ("Bosques, para trabajar con terraza.", ["Bos_portada.jpg"]),
  ("Insurgentes Sur, para bajarte del Metrobús y llegar.", ["Ins_portada.jpg"]),
  ("Y San Rafael, nuestra casa nueva.", ["SRa_portada.jpg"]),
  ("Cinco barrios, una comunidad. ¿Cuál es el tuyo?", ["END"]),
 ],
 hook="ELIGE TU BARRIO",
 ig="""Cinco barrios, una comunidad. ¿Cuál es el tuyo? 👇

📍 Polanco
📍 Interlomas
📍 Bosques de las Lomas
📍 Insurgentes Sur
📍 San Rafael

Agenda tu recorrido en thepool.mx

""" + TAGS,
 li="""Polanco, Interlomas, Bosques de las Lomas, Insurgentes Sur y San Rafael.

Cinco sedes de The Pool para que tu equipo trabaje cerca de donde vive. Oficinas privadas, coworking y salas de juntas.

thepool.mx

#Coworking #OficinasPrivadas #CDMX"""),

dict(id="09", fecha="2026-12-11", dia="Vie", tipo="carrusel", pilar="Promo Navidad",
 slides=[
  dict(t="cover", img="Int_of207_cap11_1.jpg", eyebrow="PROMO DE DICIEMBRE", title="EMPIEZA EL\nAÑO CON OFICINA\nPROPIA.", sub="10% de descuento"),
  dict(t="list", eyebrow="ASÍ FUNCIONA", title="Tu regalo de\nfin de año", items=["Contratas tu oficina en diciembre: 10% de descuento.","O te vas al plan anual: 10% de descuento.","En enero llegas y ya trabajas."], note="Precios + IVA. Sujeto a disponibilidad."),
  dict(t="photo", img="Pol_of9_cap5_0.jpg", kicker="POLANCO · OFICINA 9", title="Sin armar nada", body="Muebles, internet y recepción incluidos."),
  dict(t="photo", img="Bos_of24_cap3_2.jpg", kicker="BOSQUES · OFICINA 24", title="Cinco barrios para elegir", body="Polanco, Interlomas, Bosques, Insurgentes Sur y San Rafael."),
  dict(t="cta", title="VÁLIDO TODO\nDICIEMBRE", body="Agenda tu recorrido antes de las vacaciones."),
 ],
 ig="""El mejor propósito de año nuevo: dejar de trabajar desde el comedor 🎄

Todo diciembre tienes 10% de descuento si contratas tu oficina privada, o 10% en el plan anual.

Oficinas amuebladas, con internet y recepción. Llegas en enero y ya estás trabajando.

Agenda tu recorrido en thepool.mx antes de las vacaciones.

Precios + IVA. Sujeto a disponibilidad.

""" + TAGS,
 li="""Promo de diciembre en The Pool: 10% de descuento al contratar tu oficina privada este mes, o 10% en el plan anual.

Oficinas amuebladas y listas para operar en enero, en Polanco, Interlomas, Bosques, Insurgentes Sur y San Rafael.

Precios + IVA, sujeto a disponibilidad. thepool.mx

#OficinasPrivadas #CDMX #Coworking"""),

# ---------------- SEMANA 4 ----------------
dict(id="10", fecha="2026-12-14", dia="Lun", tipo="carrusel", pilar="Opciones",
 slides=[
  dict(t="cover", img="Pol_of19_cap8_2.jpg", eyebrow="OFICINAS PRIVADAS", title="¿CUÁNTOS\nSON EN TU\nEQUIPO?", sub="Desliza"),
  dict(t="photo", img="Pol_of12_cap3_0.jpg", kicker="POLANCO · OFICINA 12", title="3 personas", body="Para arrancar."),
  dict(t="photo", img="Pol_of3_cap4_1.jpg", kicker="POLANCO · OFICINA 3", title="4 personas", body="El equipo chico que ya va en serio."),
  dict(t="photo", img="Bos_of9_cap6_0.jpg", kicker="BOSQUES · OFICINA 9", title="6 personas", body="Con verde por la ventana."),
  dict(t="photo", img="Pol_of19_cap8_1.jpg", kicker="POLANCO · OFICINA 19", title="8 personas", body="Para el área completa."),
  dict(t="photo", img="Int_of211_cap12_2.jpg", kicker="INTERLOMAS · OFICINA 211", title="12 personas", body="Y su propio espacio de juntas."),
  dict(t="list", eyebrow="¿MÁS DE 12?", title="También\ntenemos", items=["Interlomas: equipos de +35 personas","San Rafael: de 4 a 73 personas","Insurgentes Sur: lista de espera abierta"], note="Disponibilidad sujeta a cambios."),
  dict(t="cta", title="DINOS CUÁNTOS\nSON", body="Y te mandamos opciones por DM."),
 ],
 ig="""¿Cuántos son en tu equipo? Comenta el número 👇

3, 4, 6, 8, 12... o más de 35. Tenemos oficinas privadas para cada etapa, amuebladas y listas para entrar.

Te mandamos opciones por DM según tu tamaño y tu barrio.

Disponibilidad sujeta a cambios.

""" + TAGS,
 li="""¿Tu equipo creció? En The Pool hay oficinas privadas para 3, 4, 6, 8, 12 personas y espacios para equipos de +35 en Interlomas o hasta 73 en San Rafael.

Amuebladas y listas para operar. Agenda un recorrido: thepool.mx

#OficinasPrivadas #Startups #CDMX"""),

dict(id="11", fecha="2026-12-16", dia="Mié", tipo="reel", pilar="Promo Navidad",
 voz=[
  ("Enero siempre llega con los mismos propósitos.", ["Pol_of13_cap3_1.jpg"]),
  ("Ordenar al equipo. Dejar de trabajar desde el comedor. Verte más profesional con tus clientes.", ["Pol_of19_cap8_0.jpg","Int_of207_cap11_0.jpg"]),
  ("Si contratas tu oficina en diciembre, tienes 10% de descuento.", ["Bos_of9_cap6_1.jpg"]),
  ("Cinco sedes, oficinas listas para entrar.", ["Int_portada.jpg","Pol_portada.jpg"]),
  ("Agenda tu recorrido antes de que acabe el año.", ["END"]),
 ],
 hook="TU PROPÓSITO 2027: OFICINA PROPIA",
 ig="""Propósito 2027: que tu equipo deje de trabajar en el comedor 😅

Contrata tu oficina en diciembre y llévate 10% de descuento (o 10% en plan anual). Cinco sedes, oficinas listas para entrar en enero.

Agenda tu recorrido en thepool.mx

Precios + IVA. Sujeto a disponibilidad.

""" + TAGS,
 li="""Cierra el año con la oficina resuelta.

Contratando en diciembre tienes 10% de descuento en tu oficina privada o en el plan anual de The Pool. Cinco sedes en CDMX y Edo. Mex., listas para operar en enero.

Precios + IVA, sujeto a disponibilidad. thepool.mx

#OficinasPrivadas #CDMX"""),

dict(id="12", fecha="2026-12-18", dia="Vie", tipo="carrusel", pilar="Sedes nuevas",
 slides=[
  dict(t="cover", img="SRa_portada.jpg", eyebrow="NUEVA SEDE", title="LLEGAMOS A\nSAN RAFAEL.", sub="Nueva sede"),
  dict(t="list", eyebrow="SAN RAFAEL", title="Lo que vas a\nencontrar", items=["Oficinas para equipos de 4 a 73 personas","Terraza de 245 metros cuadrados","Coworking","Listas para usar"]),
  dict(t="photo", img="SRa_portada.jpg", crop=0.3, kicker="SAN RAFAEL · COWORKING", title="Tu nuevo lugar para trabajar", body="Oficinas privadas y coworking en la colonia San Rafael."),
  dict(t="cta", title="CONOCE\nSAN RAFAEL", body="Agenda tu recorrido y conoce la sede antes que nadie."),
 ],
 ig="""Nueva casa: San Rafael 🏡

Oficinas para equipos de 4 a 73 personas, coworking y una terraza de 245 m² que ya queremos estrenar con ustedes.

Agenda tu recorrido en thepool.mx

""" + TAGS + " #SanRafael",
 li="""The Pool llega a San Rafael: oficinas privadas para equipos de 4 a 73 personas, coworking y terraza de 245 m².

thepool.mx

#Coworking #OficinasPrivadas #CDMX"""),
]
