import streamlit as st
import base64
import os

# 1. Podešavanje stranice
st.set_page_config(
    page_title="AM AUTO - Agencija za registraciju i uvoz vozila - Laćarak",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Funkcija za pretvaranje lokalnih fajlova sa GitHub-a u bezbedan Base64 format
def ucitaj_sliku_base64(putanja_slike):
    if os.path.exists(putanja_slike):
        with open(putanja_slike, "rb") as fajl:
            podaci = fajl.read()
            return "data:image/jpeg;base64," + base64.b64encode(podaci).decode()
    return ""

logo_b64 = ucitaj_sliku_base64("LOGO.JPG")
pozadina_b64 = ucitaj_sliku_base64("AMBck.JPG")

izvor_logotipa = logo_b64 if logo_b64 else "https://placeholder.com"
stil_pozadine = f"url('{pozadina_b64}');" if pozadina_b64 else "linear-gradient(135deg, #111111 0%, #222222 100%);"

# 3. Globalni CSS stilovi
css_stilovi = f"""
<style>
#MainMenu {{visibility: hidden;}}
footer {{visibility: hidden;}}
header {{visibility: hidden;}}

.block-container {{
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}}

html {{
    scroll-behavior: smooth;
}}

/* Fiksirani beli header na vrhu ekrana */
.custom-header {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #ffffff;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    z-index: 99999;
    padding: 10px 5%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 85px;
}}

.logo-container img {{
    height: 65px;
    width: auto;
    display: block;
    object-fit: contain;
}}

.header-phone a {{
    color: #111111;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
}}
.header-phone a:hover {{
    color: #E53E3E;
}}

.main-content {{
    margin-top: 85px;
}}

.hero-container {{
    position: relative;
    width: 100%;
    min-height: 580px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}}

@keyframes advancedZoomBlur {{
    0% {{
        transform: scale(1.25);
        filter: blur(6px) brightness(0.3);
    }}
    100% {{
        transform: scale(1.0);
        filter: blur(0px) brightness(1.0);
    }}
}}

.hero-background-animated {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.75)), {stil_pozadine}
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    z-index: 1;
    animation: advancedZoomBlur 3.2s cubic-bezier(0.1, 0.8, 0.2, 1) forwards;
}}

.hero-content {{
    position: relative;
    z-index: 99;
    text-align: center;
    color: white !important;
    padding: 40px;
    width: 100%;
}}

@keyframes elementsFadeIn {{
    from {{ opacity: 0; transform: translateY(20px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.hero-content h1 {{
    font-size: 46px;
    font-weight: 300;
    letter-spacing: 2px;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    color: white !important;
    animation: elementsFadeIn 1.4s ease-out forwards;
}}

.hero-content p {{
    font-size: 19px;
    color: #e0e0e0 !important;
    max-width: 600px;
    margin: 0 auto 40px auto;
    line-height: 1.6;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    animation: elementsFadeIn 1.8s ease-out forwards;
}}

.hero-btn {{
    background-color: #E53E3E;
    color: white !important;
    padding: 16px 40px;
    font-weight: bold;
    text-decoration: none;
    border-radius: 4px;
    letter-spacing: 1px;
    display: inline-block;
    box-shadow: 0 4px 15px rgba(229, 62, 62, 0.4);
    transition: 0.3s;
    animation: elementsFadeIn 2.2s ease-out forwards;
}}
.hero-btn:hover {{
    background-color: #C53030;
    transform: translateY(-2px);
}}

/* REORGANIZOVANI CSS ZA KARTICE */
.service-box-custom {{
    background-color: #f9f9f9;
    padding: 20px 15px;
    border-radius: 6px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    width: 100%;
}}
.border-black {{ border-top: 4px solid #111111; }}
.border-red {{ border-top: 4px solid #E53E3E; }}

/* Kontrola spoljnih razmaka */
.usluge-omotac {{
    margin-top: 30px !important;
}}

.kontakt-omotac {{
    margin-top: 30px !important;
}}

@media (max-width: 768px) {{
    .usluge-omotac {{
        margin-top: -40px !important; /* Povlačenje sekcije usluga bliže slici na telefonu */
    }}
    .kontakt-omotac {{
        margin-top: -15px !important; /* Jače privlačenje kontakta na dnu ekrana telefona */
    }}
    /* Smanjenje fabričkog Streamlit razmaka između kolona na telefonu */
    div[data-testid="column"] {{
        margin-bottom: 12px !important;
    }}
}}

.contact-footer-custom {{
    background-color: #111111;
    color: white;
    padding: 50px 40px;
    text-align: center;
}}

@media (max-width: 768px) {{
    .contact-footer-custom {{
        padding: 40px 20px;
    }}
}}

.powered-by {{
    font-size: 13px;
    color: #2ECC71 !important;
    margin-top: 15px;
    letter-spacing: 1px;
    font-weight: normal !important;
}}
</style>
"""
st.markdown(css_stilovi, unsafe_allow_html=True)

# 4. IZGRADNJA SAJTA

st.markdown(f"""
<div class="custom-header">
    <div class="logo-container">
        <img src="{izvor_logotipa}" alt="AM AUTO Logo">
    </div>
    <div class="header-phone">
        <a href="tel:+381616065018">📞 061 / 60-65-018</a>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

st.markdown(f"""
<div class="hero-container">
    <div class="hero-background-animated"></div>
    <div class="hero-content">
        <h1><b style="font-weight: 900;">AM AUTO</b> agencija</h1>
        <p>Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.</p>
        <a href="#kontakt" class="hero-btn">KONTAKTIRAJTE NAS</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ODVOJENI POZIVI DA BI STREAMLIT ISPRAVNO RENDERISAO HTML
st.markdown('<div class="usluge-omotac">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; font-weight: 700; color: #111111; font-family: sans-serif; margin-bottom: 0px;">NAŠE USLUGE</h2>', unsafe_allow_html=True)
st.markdown('<div style="width: 50px; height: 3px; background-color: #E53E3E; margin: 10px auto 30px auto;"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="service-box-custom border-black" style="font-family: sans-serif;">
        <div style="font-size: 35px; margin-bottom: 5px;">📝</div>
        <h3 style="font-weight: 700; margin-bottom: 8px; color: #111111; font-size: 18px;">Registracija vozila</h3>
        <p style="color: #666666; line-height: 1.5; font-size: 14px; margin-bottom: 0px;">Kompletna usluga tehničkog pregleda, osiguranja i izdavanja nalepnica bez odlaska u MUP.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="service-box-custom border-red" style="font-family: sans-serif;">
        <div style="font-size: 35px; margin-bottom: 5px;">🚗</div>
        <h3 style="font-weight: 700; margin-bottom: 8px; color: #111111; font-size: 18px;">Uvoz vozila</h3>
        <p style="color: #666666; line-height: 1.5; font-size: 14px; margin-bottom: 0px;">Pomoć pri odabiru, organizacija transporta, carinjenje i kompletna dokumentacija za uvoz automobila.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="service-box-custom border-black" style="font-family: sans-serif;">
        <div style="font-size: 35px; margin-bottom: 5px;">💳</div>
        <h3 style="font-weight: 700; margin-bottom: 8px; color: #111111; font-size: 18px;">Platni promet</h3>
        <p style="color: #666666; line-height: 1.5; font-size: 14px; margin-bottom: 0px;">Brzo i sigurno plaćanje svih vrsta računa, taksi i uplatnica direktno na našem šalteru.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ODVOJENA KONTAKT SEKCIJA
st.markdown('<div class="kontakt-omotac">', unsafe_allow_html=True)
st.markdown("""
<div id="kontakt" class="contact-footer-custom" style="font-family: sans-serif;">
    <h2 style="font-weight: 700; margin-bottom: 10px;">KONTAKT INFORMACIJE</h2>
    <div style="width: 35px; height: 2px; background-color: #E53E3E; margin: 0 auto 40px auto;"></div>
    <p style="font-size: 17px; color: #dddddd; margin-bottom: 15px;">📍 Adresa: <strong>1. Novembar 250, LAĆARAK</strong></p>
    <p style="font-size: 17px; color: #dddddd; margin-bottom: 15px;">📞 Telefon: <a href="tel:+381616065018" style="color: white; text-decoration: none;"><strong>061 / 60-65-018</strong></a></p>
    <p style="font-size: 17px; color: #dddddd; margin-bottom: 30px;">📧 Email: <a href="mailto:am.auto@gmail.com" style="color: white; text-decoration: none;"><strong>am.auto@gmail.com</strong></a></p>
    <p style="font-size: 14px; color: #555555; margin-top: 40px;">&copy; 2026 AM AUTO. Sva prava zadržana.</p>
    <div class="powered-by">Powered by MAGICOMP</div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
