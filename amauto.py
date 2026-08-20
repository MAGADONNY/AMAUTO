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

# Učitavanje tvog logotipa i pozadine sa Audijem iz tvog repozitorijuma
logo_b64 = ucitaj_sliku_base64("LOGO.JPG")
pozadina_b64 = ucitaj_sliku_base64("AMBck.JPG")

# Rezervni plan ako slike ne postoje na serveru
izvor_logotipa = logo_b64 if logo_b64 else "https://placeholder.com"
stil_pozadine = f"background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.80)), url('{pozadina_b64}');" if pozadina_b64 else "background: linear-gradient(135deg, #111111 0%, #222222 100%);"

# PROVEREN I SIGURAN GOOGLE MAPS LINK (Otvara direktnu lokaciju i navigaciju u Laćarku)
MAPS_URL = "https://google.com"

# 3. Globalni CSS stilovi za stabilan i čist grafički prikaz
st.markdown(f"""
    <style>
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    .block-container {{
        padding-top: 0px !important;
        padding-bottom: 0px !important;
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
    
    /* Pomak celog sadržaja nadole zbog fiksiranog menija */
    .main-content {{
        margin-top: 85px;
    }}
    
    /* Tamna Hero sekcija sa Audijem u pozadini */
    .hero-section {{
        {stil_pozadine}
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat !important;
        width: 100%;
        padding: 120px 40px;
        text-align: center;
        color: white !important;
        min-height: 580px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }}
    
    /* Glavni naslov - Podrazumevano postavljen na tanak font */
    .hero-section h1 {{
        font-size: 46px;
        font-weight: 300;
        letter-spacing: 2px;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        color: white !important;
    }}
    
    .hero-section p {{
        font-size: 19px;
        color: #e0e0e0 !important;
        max-width: 600px;
        margin: 0 auto 40px auto;
        line-height: 1.6;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }}
    
    /* Dugme Kontaktirajte nas */
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
    }}
    .hero-btn:hover {{
        background-color: #C53030;
        transform: translateY(-2px);
    }}
    
    /* Stilizacija kartica sa uslugama */
    .service-box {{
        background-color: #f9f9f9;
        padding: 40px 25px;
        border-radius: 6px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
    }}
    .box-black {{ border-top: 4px solid #111111; }}
    .box-red {{ border-top: 4px solid #E53E3E; }}
    
    /* Kontakt sekcija na dnu (Footer) */
    .contact-footer {{
        background-color: #111111;
        color: white;
        padding: 60px 40px;
        text-align: center;
        margin-top: 60px;
    }}
    
    /* Powered by zelen, normalan i bez podebljanja */
    .powered-by {{
        font-size: 13px;
        color: #2ECC71 !important;
        margin-top: 15px;
        letter-spacing: 1px;
        font-weight: normal !important;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. IZGRADNJA SAJTA

# Prikaz belog headera sa logoom i telefonom
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

# Otvaranje glavnog dela stranice ispod menija
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# HERO SEKCIJA (Dugme otvara fabričku Google Maps navigaciju)
st.markdown(f"""
    <div class="hero-section">
        <h1><b style="font-weight: 900;">AM AUTO</b> agencija</h1>
        <p>Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.</p>
        <a href="{MAPS_URL}" target="_blank" class="hero-btn">PRONAĐITE NAS</a>
    </div>
""", unsafe_allow_html=True)

st.markdown('<br><br>', unsafe_allow_html=True)

# NASLOV USLUGA
st.markdown('<h2 style="text-align: center; font-weight: 700; color: #111111; font-family: sans-serif;">NAŠE USLUGE</h2>', unsafe_allow_html=True)
st.markdown('<div style="width: 50px; height: 3px; background-color: #E53E3E; margin: 15px auto 50px auto;"></div>', unsafe_allow_html=True)

# TRI KARTICE SA USLUGAMA
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-box box-black" style="font-family: sans-serif;">
            <div style="font-size: 40px; margin-bottom: 15px;">📝</div>
            <h3 style="font-weight: 700; margin-bottom: 15px; color: #111111;">Registracija vozila</h3>
            <p style="color: #666666; line-height: 1.6; font-size: 15px;">Kompletna usluga tehničkog pregleda, osiguranja i izdavanja registracionih nalepnica bez odlaska u MUP.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-box box-red" style="font-family: sans-serif;">
            <div style="font-size: 40px; margin-bottom: 15px;">🚢</div>
            <h3 style="font-weight: 700; margin-bottom: 15px; color: #111111;">Uvoz vozila</h3>
            <p style="color: #666666; line-height: 1.6; font-size: 15px;">Pomoć pri odabiru, organizacija transporta, carinjenje i kompletna dokumentacija za uvoz automobila.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-box box-black" style="font-family: sans-serif;">
            <div style="font-size: 40px; margin-bottom: 15px;">💳</div>
            <h3 style="font-weight: 700; margin-bottom: 15px; color: #111111;">Platni promet</h3>
            <p style="color: #666666; line-height: 1.6; font-size: 15px;">Brzo i sigurno plaćanje svih vrsta računa, taksi i uplatnica direktno na našem šalteru.</p>
        </div>
    """, unsafe_allow_html=True)

# TAMNA KONTAKT SEKCIJA (Ispravljen email u am.auto@gmail.com)
st.markdown(f"""
    <div id="kontakt" class="contact-footer" style="font-family: sans-serif;">
        <h2 style="font-weight: 700; margin-bottom: 10px;">KONTAKT INFORMACIJE</h2>
        <div style="width: 35px; height: 2px; background-color: #E53E3E; margin: 0 auto 40px auto;"></div>
        <p style="font-size: 17px; color: #dddddd; margin-bottom: 15px;">
            📍 Adresa: <a href="{MAPS_URL}" target="_blank" style="color: white; text-decoration: underline;"><strong>1. Novembar 250, LAĆARAK</strong></a>
        </p>
        <p style="font-size: 17px; color: #dddddd; margin-bottom: 15px;">📞 Telefon: <a href="tel:+381616065018" style="color: white; text-decoration: none;"><strong>061 / 60-65-018</strong></a></p>
        <p style="font-size: 17px; color: #dddddd; margin-bottom: 30px;">📧 Email: <a href="mailto:am.auto@gmail.com" style="color: white; text-decoration: none;"><strong>am.auto@gmail.com</strong></a></p>
        <p style="font-size: 14px; color: #555555; margin-top: 40px;">&copy; 2026 AM AUTO. Sva prava zadržana.</p>
        <div class="powered-by">Powered by MAGICOMP</div>
    </div>
""", unsafe_allow_html=True)

# Zatvaranje glavnog dela stranice
st.markdown('</div>', unsafe_allow_html=True)
