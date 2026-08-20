import streamlit as st
import streamlit.components.v1 as components

# Podešavanje stranice (mora biti prva Streamlit komanda)
st.set_page_config(
    page_title="AM AUTO - Agencija za registraciju i uvoz vozila",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Tačne putanje do slika na tvom GitHub nalogu
LOGO_URL = "https://githubusercontent.com"
BACKGROUND_URL = "https://githubusercontent.com"

# Kompletan HTML, CSS i JS spakovan u jednu bezbednu celinu
html_sadrzaj = f"""
<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AM AUTO</title>
    <style>
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}
        body {{
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: #ffffff;
            color: #111111;
            overflow-x: hidden;
        }}
        
        /* Uvodna animacija */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        .animated-content {{
            animation: fadeInUp 1.4s ease-out forwards;
        }}
        
        /* Fiksirani beli header */
        .custom-header {{
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
        }}
        .logo-container img {{
            height: 65px;
            width: auto;
        }}
        .header-phone a {{
            color: #111111;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
        }}
        
        /* Glavni sadržaj ispod headera */
        .main-body {{
            margin-top: 85px;
        }}
        
        /* Hero sekcija sa Audijem u pozadini */
        .hero-section {{
            background-color: #1a1a1a;
            background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.75)), url('{BACKGROUND_URL}');
            background-size: cover;
            background-position: center;
            padding: 140px 5%;
            text-align: center;
            color: white;
            min-height: 550px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        .hero-section h1 {{
            font-size: 46px;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }}
        .hero-section p {{
            font-size: 19px;
            color: #e0e0e0;
            max-width: 600px;
            margin: 0 auto 40px auto;
            line-height: 1.6;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        }}
        .hero-btn {{
            background-color: #E53E3E;
            color: white;
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
        }}
        
        /* Sekcija usluga */
        .services-section {{
            padding: 80px 5%;
            background-color: #ffffff;
            text-align: center;
        }}
        .services-section h2 {{
            font-size: 30px;
            font-weight: 700;
            color: #111111;
            margin-bottom: 10px;
        }}
        .title-divider {{
            width: 50px;
            height: 3px;
            background-color: #E53E3E;
            margin: 0 auto 50px auto;
        }}
        .services-grid {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }}
        .service-card {{
            flex: 1;
            min-width: 280px;
            max-width: 350px;
            padding: 40px 25px;
            background: #f9f9f9;
            border-radius: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            transition: 0.3s;
        }}
        .card-black {{ border-top: 4px solid #111111; }}
        .card-red {{ border-top: 4px solid #E53E3E; }}
        
        .card-icon {{
            font-size: 40px;
            margin-bottom: 15px;
        }}
        .service-card h3 {{
            font-size: 20px;
            font-weight: 700;
            color: #111111;
            margin-bottom: 15px;
        }}
        .service-card p {{
            color: #666666;
            font-size: 15px;
            line-height: 1.6;
        }}
        
        /* Kontakt sekcija */
        .footer-section {{
            background-color: #111111;
            color: white;
            padding: 60px 5%;
            text-align: center;
        }}
        .footer-section h2 {{
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 30px;
        }}
        .footer-section p {{
            font-size: 16px;
            color: #aaaaaa;
            margin-bottom: 10px;
        }}
        .copyright {{
            font-size: 14px;
            color: #555555;
            margin-top: 40px;
        }}
    </style>
</head>
<body>

    <div class="custom-header">
        <div class="logo-container">
            <img src="{LOGO_URL}" alt="AM AUTO Logo" onerror="this.onerror=null; this.src='https://placeholder.com';">
        </div>
        <div class="header-phone">
            <a href="tel:+381601234567">📞 060 / 123-4567</a>
        </div>
    </div>

    <div class="main-body animated-content">
        <div class="hero-section">
            <h1>AM AUTO AGENCIJA</h1>
            <p>Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.</p>
            <a href="tel:+381601234567" class="hero-btn">POZOVITE ODMAH</a>
        </div>
        
        <div class="services-section">
            <h2>NAŠE USLUGE</h2>
            <div class="title-divider"></div>
            
            <div class="services-grid">
                <div class="service-card card-black">
                    <div class="card-icon">📝</div>
                    <h3>Registracija vozila</h3>
                    <p>Kompletna usluga tehničkog pregleda, osiguranja i izdavanja registracionih nalepnica bez odlaska u MUP.</p>
                </div>
                <div class="service-card card-red">
                    <div class="card-icon">🚢</div>
                    <h3>Uvoz vozila</h3>
                    <p>Pomoć pri odabiru, organizacija transporta, carinjenje i kompletna dokumentacija za uvoz automobila.</p>
                </div>
                <div class="service-card card-black">
                    <div class="card-icon">💳</div>
                    <h3>Platni promet</h3>
                    <p>Brzo i sigurno plaćanje svih vrsta računa, taksi i uplatnica direktno na našem šalteru.</p>
                </div>
            </div>
        </div>
        
        <div class="footer-section">
            <h2>KONTAKT INFORMACIJE</h2>
            <p>📍 Adresa: [Unesi tvoju adresu ovde]</p>
            <p>📧 Email: info@amauto.rs</p>
            <p class="copyright">&copy; 2026 AM AUTO. Sva prava zadržana.</p>
        </div>
    </div>

</body>
</html>
"""

# Uklanjanje podrazumevanih Streamlit margina da bi sajt išao od ivice do ivice ekrana
st.markdown("""
    <style>
    .block-container { padding: 0px !important; }
    iframe { border: none !important; }
    </style>
""", unsafe_allow_html=True)

# Prikazivanje kompletnog sajta preko celog ekrana (visina 1000px obezbeđuje prostor za skrolovanje)
components.html(html_sadrzaj, height=1000, scrolling=True)
