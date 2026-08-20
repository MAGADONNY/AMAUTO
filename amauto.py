import streamlit as st
import streamlit.components.v1 as components
import base64
import os

# Podešavanje stranice
st.set_page_config(
    page_title="AM AUTO - Agencija za registraciju i uvoz vozila - Laćarak",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Funkcija za bezbedno pretvaranje lokalne slike u Base64 format
def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return "data:image/jpeg;base64," + base64.b64encode(img_file.read()).decode()
    return ""

# Učitavanje slika sa servera
logo_base64 = get_base64_image("LOGO.JPG")
bg_base64 = get_base64_image("AMBck.JPG")

# Rezervne varijante ako slika nema
logo_src = logo_base64 if logo_base64 else "https://placeholder.com"

# ČIST HTML I CSS BEZ ZAGLAVLJENIH ZAGRADA
html_sadrzaj = """
<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AM AUTO - Laćarak</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        html {
            scroll-behavior: smooth;
        }
        body {
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background-color: #ffffff;
            color: #111111;
            overflow-x: hidden;
        }
        
        /* Glavna uvodna animacija */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        .animated-content {
            animation: fadeInUp 1.2s ease-out forwards;
        }
        
        /* Fiksirani beli header */
        .custom-header {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background-color: #ffffff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            z-index: 9999;
            padding: 5px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            height: 80px;
        }
        .logo-container {
            display: flex;
            align-items: center;
            height: 100%;
        }
        .logo-container img {
            height: 60px;
            width: auto;
            object-fit: contain;
        }
        .header-phone a {
            color: #111111;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            transition: 0.3s;
        }
        .header-phone a:hover {
            color: #E53E3E;
        }
        
        /* Sadržaj ispod headera */
        .main-body {
            margin-top: 80px;
        }
        
        /* Hero sekcija sa Audijem */
        .hero-section {
            background-size: cover;
            background-position: center center;
            background-repeat: no-repeat !important;
            width: 100%;
            padding: 120px 5%;
            min-height: 600px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
        }
        .hero-section h1 {
            font-size: 46px;
            font-weight: 800;
            letter-spacing: 2px;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        }
        .hero-section p {
            font-size: 19px;
            color: #e0e0e0;
            max-width: 600px;
            margin: 0 auto 40px auto;
            line-height: 1.6;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
        }
        .hero-btn {
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
        }
        .hero-btn:hover {
            background-color: #C53030;
            transform: translateY(-2px);
        }
        
        /* Sekcija usluga */
        .services-section {
            padding: 80px 5%;
            background-color: #ffffff;
            text-align: center;
        }
        .services-section h2 {
            font-size: 30px;
            font-weight: 700;
            color: #111111;
            margin-bottom: 10px;
        }
        .title-divider {
            width: 50px;
            height: 3px;
            background-color: #E53E3E;
            margin: 0 auto 50px auto;
        }
        .services-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 30px;
        }
        .service-card {
            flex: 1;
            min-width: 280px;
            max-width: 350px;
            padding: 40px 25px;
            background: #f9f9f9;
            border-radius: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        }
        .card-black { border-top: 4px solid #111111; }
        .card-red { border-top: 4px solid #E53E3E; }
        
        .card-icon { font-size: 40px; margin-bottom: 15px; }
        .service-card h3 { font-size: 20px; font-weight: 700; color: #111111; margin-bottom: 15px; }
        .service-card p { color: #666666; font-size: 15px; line-height: 1.6; }
        
        /* Kontakt sekcija */
        .footer-section {
            background-color: #111111;
            color: white;
            padding: 70px 5%;
            text-align: center;
        }
        .footer-section h2 { 
            font-size: 28px; 
            font-weight: 700; 
            margin-bottom: 10px; 
            letter-spacing: 1px;
        }
        .footer-divider {
            width: 35px;
            height: 2px;
            background-color: #E53E3E;
            margin: 0 auto 40px auto;
        }
        .contact-item {
            font-size: 17px;
            color: #dddddd;
            margin-bottom: 15px;
        }
        .contact-item a {
            color: #ffffff;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }
        .contact-item a:hover {
            color: #E53E3E;
        }
        .copyright { 
            font-size: 14px; 
            color: #555555; 
            margin-top: 40px; 
        }
        .powered-by {
            font-size: 13px;
            color: #E53E3E;
            margin-top: 10px;
            letter-spacing: 2px;
        }
        
        /* Responzivnost za mobilne telefone */
        @media (max-width: 768px) {
            .hero-section {
                min-height: 480px;
            }
            .hero-section h1 { font-size: 32px; }
            .hero-section p { font-size: 16px; }
        }
    </style>
</head>
<body>

    <!-- HEADER SA LOGOOM I PODACIMA -->
    <div class="custom-header">
        <div class="logo-container">
            <img src="##LOGO_PLACEHOLDER##" alt="AM AUTO Logo">
        </div>
        <div class="header-phone">
            <a href="tel:+381616065018">📞 061 / 60-65-018</a>
        </div>
    </div>

    <!-- GLAVNI SADRŽAJ -->
    <div class="main-body animated-content">
        <div class="hero-section" style="##BG_PLACEHOLDER##">
            <h1>AM AUTO AGENCIJA</h1>
            <p>Sve na jednom mestu za Vaše vozilo. Brza registracija, siguran uvoz motornih vozila i pouzdan platni promet.</p>
            <a href="#kontakt" class="hero-btn">KONTAKTIRAJTE NAS</a>
        </div>
        
        <!-- NAŠE USLUGE -->
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
        
        <!-- KONTAKT SEKCIJA -->
        <div id="kontakt" class="footer-section">
            <h2>KONTAKT INFORMACIJE</h2>
            <div class="footer-divider"></div>
            
            <div class="contact-item">
                📍 Adresa: <strong>1. Novembar 250, LAĆARAK</strong>
            </div>
            <div class="contact-item">
                📞 Telefon: <a href="tel:+381616065018"><strong>061 / 60-65-018</strong></a>
            </div>
            <div class="contact-item">
                📧 Email: <a href="mailto:amauto@gmail.com"><strong>amauto@gmail.com</strong></a>
            </div>
            
            <p class="copyright">&copy; 2026 AM AUTO. Sva prava zadržana.</p>
            <div class="powered-by">Powered by MAGICOMP</div>
        </div>
    </div>

</body>
</html>
"""

# Bezbedno ubacivanje slika na samom kraju
bg_style_string = f"background-image: linear-gradient(rgba(0, 0, 0, 0.50), rgba(0, 0, 0, 0.70)), url('{bg_base64}');" if bg_base64 else "background: linear-gradient(135deg, #111111 0%, #222222 100%);"

html_sadrzaj = html_sadrzaj.replace("##LOGO_PLACEHOLDER##", logo_src)
