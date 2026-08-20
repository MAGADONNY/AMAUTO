import streamlit as st

# Podešavanje stranice
st.set_page_config(
    page_title="AM AUTO - Agencija za registraciju i uvoz vozila",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Sakrivanje standardnih Streamlit elemenata i definisanje CSS stilova
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
    }
    
    /* Glavna uvodna animacija (Fade In + Slide Up) */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animated-content {
        animation: fadeInUp 1.4s ease-out forwards;
    }
    
    /* CSS za fiksirani beli header */
    .custom-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #ffffff;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        z-index: 9999;
        padding: 10px 5%;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo-container img {
        height: 65px;
        width: auto;
    }
    
    .main-body {
        margin-top: 85px;
    }
    </style>
""", unsafe_allow_html=True)

# --- TAČNE PUTANJE SA TVOG GITHUB-A ---
LOGO_URL = "https://githubusercontent.com"
BACKGROUND_URL = "https://githubusercontent.com"

# Prikaz belog headera sa tvog GitHub-a
st.markdown(f"""
    <div class="custom-header">
        <div class="logo-container">
            <img src="{LOGO_URL}" alt="AM AUTO Logo" onerror="this.onerror=null; this.src='https://placeholder.com';">
        </div>
        <div style="font-family: sans-serif; font-weight: bold; color: #111111;">
            <a href="tel:+381601234567" style="color: #111111; text-decoration: none; font-size: 16px;">📞 060 / 123-4567</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# Glavni sadržaj stranice sa uvodnom animacijom i Audijem u pozadini
st.markdown(f"""
    <div class="main-body animated-content" style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;">
        
        <!-- HERO SEKCIJA SA TVOJOM SLIKOM AMBck.JPG -->
        <div style="background-color: #1a1a1a; background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.75)), url('{BACKGROUND_URL}'); background-size: cover; background-position: center; padding: 140px 5%; text-align: center; color: white; min-height: 550px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h1 style="font-size: 46px; font-weight: 800; letter-spacing: 2px; margin-bottom: 20px; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
                AM AUTO AGENCIJA
            </h1>
            <p style="font-size: 19px; color: #e0e0e0; max-width: 600px; margin: 0 auto 40px auto; line-height: 1.6; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
                Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.
            </p>
            <a href="tel:+381601234567" style="background-color: #E53E3E; color: white; padding: 16px 40px; font-weight: bold; text-decoration: none; border-radius: 4px; letter-spacing: 1px; display: inline-block; box-shadow: 0 4px 15px rgba(229, 62, 62, 0.4);">
                POZOVITE ODMAH
            </a>
        </div>
        
        <!-- SEKCIJA USLUGE -->
        <div style="padding: 80px 5%; background-color: #ffffff; text-align: center;">
            <h2 style="font-size: 30px; font-weight: 700; color: #111111; margin-bottom: 10px;">NAŠE USLUGE</h2>
            <div style="width: 50px; height: 3px; background-color: #E53E3E; margin: 0 auto 50px auto;"></div>
            
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 30px;">
                <!-- Kartica 1 -->
                <div style="flex: 1; min-width: 280px; max-width: 350px; padding: 40px 25px; background: #f9f9f9; border-top: 4px solid #111111; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <div style="font-size: 40px; margin-bottom: 15px;">📝</div>
                    <h3 style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 15px;">Registracija vozila</h3>
                    <p style="color: #666666; font-size: 15px; line-height: 1.6;">Kompletna usluga tehničkog pregleda, osiguranja i izdavanja registracionih nalepnica bez odlaska u MUP.</p>
                </div>
                <!-- Kartica 2 -->
                <div style="flex: 1; min-width: 280px; max-width: 350px; padding: 40px 25px; background: #f9f9f9; border-top: 4px solid #E53E3E; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <div style="font-size: 40px; margin-bottom: 15px;">🚢</div>
                    <h3 style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 15px;">Uvoz vozila</h3>
                    <p style="color: #666666; font-size: 15px; line-height: 1.6;">Pomoć pri odabiru, organizacija transporta, carinjenje i kompletna dokumentacija za uvoz automobila.</p>
                </div>
                <!-- Kartica 3 -->
                <div style="flex: 1; min-width: 280px; max-width: 350px; padding: 40px 25px; background: #f9f9f9; border-top: 4px solid #111111; border-radius: 4px; box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
                    <div style="font-size: 40px; margin-bottom: 15px;">💳</div>
                    <h3 style="font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 15px;">Platni promet</h3>
                    <p style="color: #666666; font-size: 15px; line-height: 1.6;">Brzo i sigurno plaćanje svih vrsta računa, taksi i uplatnica direktno na našem šalteru.</p>
                </div>
            </div>
        </div>
        
        <!-- KONTAKT SEKCIJA -->
        <div style="background-color: #111111; color: white; padding: 60px 5%; text-align: center;">
            <h2 style="font-size: 26px; font-weight: 700; margin-bottom: 30px;">KONTAKT INFORMACIJE</h2>
            <p style="font-size: 16px; color: #aaaaaa; margin-bottom: 10px;">📍 Adresa: [1.NOVEMBAR 250]</p>
            <p style="font-size: 16px; color: #aaaaaa; margin-bottom: 30px;">📧 Email: amauto@gmail.com</p>
            <p style="font-size: 14px; color: #555555; margin-top: 40px;">&copy; 2026 AM AUTO. Sva prava zadržana.</p>
        </div>
        
    </div>
""", unsafe_allow_html=True)
