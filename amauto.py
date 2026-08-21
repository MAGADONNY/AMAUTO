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
css_stilovi = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.block-container {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}

html {
    scroll-behavior: smooth;
}

/* Fiksirani beli header na vrhu ekrana */
.custom-header {
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
}

.logo-container img {
    height: 65px;
    width: auto;
    display: block;
    object-fit: contain;
}

.header-phone a {
    color: #111111;
    text-decoration: none;
    font-weight: bold;
    font-size: 16px;
}
.header-phone a:hover {
    color: #E53E3E;
}

.main-content {
    margin-top: 85px;
}

.hero-container {
    position: relative;
    width: 100%;
    min-height: 580px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

@keyframes advancedZoomBlur {
    0% {
        transform: scale(1.25);
        filter: blur(6px) brightness(0.3);
    }
    100% {
        transform: scale(1.0);
        filter: blur(0px) brightness(1.0);
    }
}

.hero-background-animated {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    z-index: 1;
    animation: advancedZoomBlur 3.2s cubic-bezier(0.1, 0.8, 0.2, 1) forwards;
}

.hero-content {
    position: relative;
    z-index: 99;
    text-align: center;
    color: white !important;
    padding: 40px;
    width: 100%;
}

@keyframes elementsFadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.hero-content h1 {
    font-size: 46px;
    font-weight: 300;
    letter-spacing: 2px;
    margin-bottom: 20px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    color: white !important;
    animation: elementsFadeIn 1.4s ease-out forwards;
}

.hero-content p {
    font-size: 19px;
    color: #e0e0e0 !important;
    max-width: 600px;
    margin: 0 auto 40px auto;
    line-height: 1.6;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    animation: elementsFadeIn 1.8s ease-out forwards;
}

.hero-btn {
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
}
.hero-btn:hover {
    background-color: #C53030;
    transform: translateY(-2px);
}

/* DIZAJN KARTICA */
.service-box {
    background-color: #f9f9f9;
    padding: 20px 15px;
    border-radius: 6px;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.02);
}
.box-black { border-top: 4px solid #111111; }
.box-red { border-top: 4px solid #E53E3E; }

/* RAZMACI NA PC VERZIJI */
.usluge-sekcija {
    margin-top: 20px !important;
}
.contact-footer {
    background-color: #111111;
    color: white;
    padding: 50px 40px;
    text-align: center;
    margin-top: 60px !important;
}

/* STIL ZA ZBIJANJE REDOVA U KONTAKTU */
.contact-item {
    font-size: 17px;
    color: #dddddd;
    margin: 6px 0 !important;
    padding: 0 !important;
    line-height: 1.4;
}

/* SPECIJALNA PODEŠAVANJA ZA MOBILNE TELEFONE */
@media (max-width: 768px) {
    .usluge-sekcija {
        transform: translateY(-45px);
    }
    div[data-testid="column"] {
        margin-bottom: -15px !important; 
    }
    .contact-footer {
        padding: 40px 20px;
        margin-top: 40px !important;
    }
}

.powered-by {
    font-size: 13px;
    color: #2ECC71 !important;
    margin-top: 15px;
    letter-spacing: 1px;
    font-weight: normal !important;
}
</style>
"""

css_sa_pozadinom = css_stilovi.replace(".hero-background-animated {", f".hero-background-animated {{ background-image: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.75)), {stil_pozadine}")
st.markdown(css_sa_pozadinom, unsafe_allow_html=True)

# 4. IZGRADNJA SAJTA

zaglavlje_html = f"""
<div class="custom-header">
    <div class="logo-container">
        <img src="{izvor_logotipa}" alt="AM AUTO Logo">
    </div>
    <div class="header-phone">
        <a href="tel:+381616065018">📞 061 / 60-65-018</a>
    </div>
</div>
"""
st.markdown(zaglavlje_html, unsafe_allow_html=True)

st.markdown('<div class="main-content">', unsafe_allow_html=True)

hero_html = """
<div class="hero-container">
    <div class="hero-background-animated"></div>
    <div class="hero-content">
        <h1><b style="font-weight: 900;">AM AUTO</b> agencija</h1>
        <p>Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.</p>
        <a href="#kontakt" class="hero-btn">KONTAKTIRAJTE NAS</a>
    </div>
</div>
"""
st.markdown(hero_html, unsafe_allow_html=True)

# SEKCIJA "NAŠE USLUGE"
st.markdown('<div class="usluge-sekcija">', unsafe_allow_html=True)
st.markdown('<br><h2 style="text-align: center; font-weight: 700; color: #111111; font-family: sans-serif; margin-bottom: 0px;">NAŠE USLUGE</h2>', unsafe_allow_html=True)
st.markdown('<div style="width: 50px; height: 3px; background-color: #E53E3E; margin: 10px auto 30px auto;"></div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-box box-black" style="font-family: sans-serif;">
            <div style="font-size: 35px; margin-bottom: 5px;">📝</div>
            <h3 style="font-weight: 700; margin-bottom: 8px; color: #111111; font-size: 18px;">Registracija vozila</h3>
            <p style="color: #666666; line-height: 1.5; font-size: 14px; margin-bottom: 0px;">Kompletna usluga tehničkog pregleda, osiguranja i izdavanja nalepnica bez odlaska u MUP.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-box box-red" style="font-family: sans-serif;">
            <div style="font-size: 35px; margin-bottom: 5px;">🚗</div>
            <h3 style="font-weight: 700; margin-bottom: 8px; color: #111111; font-size: 18px;">Uvoz vozila</h3>
            <p style="color: #666666; line-height: 1.5; font-size: 14px; margin-bottom: 0px;">Pomoć pri odabiru, organizacija transporta, carinjenje i kompletna dokumentacija za uvoz automobila.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-box box-black" style="font-family: sans-serif;">
            <div style="font-size: 35px; margin-bottom: 5px;">💳</div>
            <h3 style="font-weight: 700; margin-bottom: 8px; color: #111111; font-size: 18px;">Platni promet</h3>
            <p style="color: #666666; line-height: 1.5; font-size: 14px; margin-bottom: 0px;">Brzo i sigurno plaćanje svih vrsta računa, taksi i uplatnica direktno na našem šalteru.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# INTERAKTIVNI ORJENTACIONI KALKULATOR
st.write("---")
st.markdown('<p style="text-align: center; font-size: 22px; font-weight: normal; color: #111111; font-family: sans-serif; margin-bottom: 0px; letter-spacing: 1px;">ORJENTACIONI KALKULATOR TROŠKOVA</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666666; font-family: sans-serif; font-size: 14px; margin-top: 5px; margin-bottom: 25px;">za tačan iznos molimo da nas kontaktirate</p>', unsafe_allow_html=True)

# Odnos kolona [1.5, 7, 1.5] za savršeno sužene i centrirane unose
glavni_kalk_levo, glavni_kalk_sadrzaj, glavni_kalk_desno = st.columns([1.5, 7, 1.5])

with glavni_kalk_sadrzaj:
    k_col1, k_col2, k_col3 = st.columns(3)
    
    with k_col1:
        kubikaza = st.number_input("Zapremina (ccm):", min_value=500, max_value=6000, value=1998, step=50, key="calc_ccm")
        
    with k_col2:
        snaga = st.number_input("Snaga motora (kW):", min_value=10, max_value=500, value=85, step=5, key="calc_kw")
        
    with k_col3:
        godiste = st.number_input("Godište vozila:", min_value=1980, max_value=2026, value=2015, step=1, key="calc_year")

    osnovica = 15000
    if kubikaza > 2000:
        osnovica += 25000
    elif kubikaza > 1600:
        osnovica += 10000

    if snaga > 100:
        osnovica += 7000

    starost = 2026 - godiste
    if starost > 20:
        osnovica = osnovica * 0.2
    elif starost > 10:
        osnovica = osnovica * 0.6
    elif starost > 5:
        osnovica = osnovica * 0.8

    procenjena_cena = int(osnovica + 6000)
    st.write("")
st.info(f"Procena troškova registracije: oko {procenjena_cena:,} RSD")


# VRAĆENA ČISTA I FINO PODEŠENA KONTAKT SEKCIJA
st.write("---")

kontakt_tekst = """
<div style="font-family: sans-serif; text-align: center; max-width: 600px; margin: 0 auto; padding: 10px 20px;">
    <p style="font-size: 22px; font-weight: normal; color: #111111; margin-bottom: 25px; letter-spacing: 1px;">KONTAKT INFORMACIJE</p>
    
    <div style="font-size: 16px; color: #111111; line-height: 1.6; text-align: left; display: inline-block;">
        <p style="margin: 5px 0;">📍 Adresa: <strong>1. Novembar 250, LAĆARAK</strong></p>
        <p style="margin: 5px 0;">📞 Telefon: <strong>061 / 60-65-018</strong></p>
        <p style="margin: 5px 0;">📧 Email: <strong>am.auto@gmail.com</strong></p>
    </div>
    
    <div style="margin-top: 30px; font-size: 13px; color: #777777; line-height: 1.5;">
        <p style="margin: 0;">© 2026 AM AUTO. Sva prava zadržana.</p>
        <p style="margin: 5px 0 0 0;">Powered by MAGICOMP</p>
    </div>
</div>
"""
st.markdown(kontakt_tekst, unsafe_allow_html=True)
