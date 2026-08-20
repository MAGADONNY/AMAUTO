import streamlit as st

# 1. Podešavanje stranice (Garantuje čist mobile-friendly izgled)
st.set_page_config(
    page_title="AM AUTO - Agencija za registraciju i uvoz vozila - Laćarak",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Linkovi ka tvom logotipu i pozadini sa Audijem na GitHub-u
LOGO_URL = "https://githubusercontent.com"
BACKGROUND_URL = "https://githubusercontent.com"

# 3. CSS za fiksirani beli header i moderan dizajn elemenata
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
        height: 80px;
    }}
    
    /* Pomak sadržaja nadole zbog headera */
    .main-content {{
        margin-top: 100px;
    }}
    
    /* Tamna Hero sekcija sa Audijem u pozadini */
    .hero-bg {{
        background-image: linear-gradient(rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.75)), url('{BACKGROUND_URL}');
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        padding: 120px 40px;
        border-radius: 8px;
        text-align: center;
        color: white;
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
    
    /* Kontakt sekcija na dnu */
    .contact-footer {{
        background-color: #111111;
        color: white;
        padding: 60px 40px;
        border-radius: 8px;
        text-align: center;
        margin-top: 60px;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. PRIKAZIVANJE SAJTA PREKO FABRIČKIH STREAMLIT FUNKCIJA (Nema grešaka)

# Beli header sa logotipom i telefonom
st.markdown(f"""
    <div class="custom-header">
        <div>
            <img src="{LOGO_URL}" style="height: 60px; width: auto;" onerror="this.onerror=null; this.src='https://placeholder.com';">
        </div>
        <div style="font-family: sans-serif; font-weight: bold;">
            <a href="tel:+381616065018" style="color: #111111; text-decoration: none; font-size: 16px;">📞 061 / 60-65-018</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Otvaranje glavnog kontejnera ispod headera
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# HERO SEKCIJA (Audi i Glavni Tekst)
st.markdown('<div class="hero-bg">', unsafe_allow_html=True)
st.title("AM AUTO AGENCIJA")
st.write("Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<br><br>', unsafe_allow_html=True)

# NASLOV USLUGA
st.markdown('<h2 style="text-align: center; font-weight: 700; color: #111111;">NAŠE USLUGE</h2>', unsafe_allow_html=True)
st.markdown('<div style="width: 50px; height: 3px; background-color: #E53E3E; margin: 15px auto 50px auto;"></div>', unsafe_allow_html=True)

# TRI KARTICE SA USLUGAMA (Koristimo Streamlit kolone)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="service-box box-black">
            <div style="font-size: 40px; margin-bottom: 15px;">📝</div>
            <h3 style="font-weight: 700; margin-bottom: 15px;">Registracija vozila</h3>
            <p style="color: #666666; line-height: 1.6;">Kompletna usluga tehničkog pregleda, osiguranja i izdavanja registracionih nalepnica bez odlaska u MUP.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-box box-red">
            <div style="font-size: 40px; margin-bottom: 15px;">🚢</div>
            <h3 style="font-weight: 700; margin-bottom: 15px;">Uvoz vozila</h3>
            <p style="color: #666666; line-height: 1.6;">Pomoć pri odabiru, organizacija transporta, carinjenje i kompletna dokumentacija za uvoz automobila.</p>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-box box-black">
            <div style="font-size: 40px; margin-bottom: 15px;">💳</div>
            <h3 style="font-weight: 700; margin-bottom: 15px;">Platni promet</h3>
            <p style="color: #666666; line-height: 1.6;">Brzo i sigurno plaćanje svih vrsta računa, taksi i uplatnica direktno na našem šalteru.</p>
        </div>
    """, unsafe_allow_html=True)

# KONTAKT SEKCIJA NA DMU (Footer)
st.markdown("""
    <div class="contact-footer">
        <h2 style="font-weight: 700; margin-bottom: 10px;">KONTAKT INFORMACIJE</h2>
        <div style="width: 35px; height: 2px; background-color: #E53E3E; margin: 0 auto 40px auto;"></div>
        <p style="font-size: 17px; color: #dddddd; margin-bottom: 15px;">📍 Adresa: <strong>1. Novembar 250, LAĆARAK</strong></p>
        <p style="font-size: 17px; color: #dddddd; margin-bottom: 15px;">📞 Telefon: <a href="tel:+381616065018" style="color: white; text-decoration: none;"><strong>061 / 60-65-018</strong></a></p>
        <p style="font-size: 17px; color: #dddddd; margin-bottom: 30px;">📧 Email: <a href="mailto:amauto@gmail.com" style="color: white; text-decoration: none;"><strong>amauto@gmail.com</strong></a></p>
        <p style="font-size: 14px; color: #555555; margin-top: 40px;">&copy; 2026 AM AUTO. Sva prava zadržana.</p>
        <p style="font-size: 13px; color: #E53E3E; margin-top: 10px; font-weight: bold; letter-spacing: 2px;">Powered by MAGICOMP</p>
    </div>
""", unsafe_allow_html=True)

# Zatvaranje glavnog kontejnera
st.markdown('</div>', unsafe_allow_html=True)
