import http.server
import socketserver
import os

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Ako se traži osnovna ruta, serviraj naš HTML kod direktno iz memorije
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            html_code = """<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AM AUTO | Agencija za registraciju i uvoz vozila</title>
    <!-- Tailwind CSS for modern and simple styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Intro Fade In Effect */
        .fade-in-init {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 1.2s ease-out, transform 1.2s ease-out;
        }
        .fade-in-visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body class="bg-gray-50 text-black font-sans m-0 p-0">

    <!-- HEADER: Beo sa velikim logom -->
    <header class="bg-white shadow-md sticky top-0 z-50 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <!-- LOGO: Sa crvenim detaljem prema smernicama -->
            <div class="text-3xl font-extrabold tracking-wider">
                <span class="text-black">AM</span> <span class="text-red-600">AUTO</span>
            </div>
            <!-- Navigacija -->
            <nav class="hidden md:flex space-x-8 font-medium">
                <a href="#usluge" class="text-gray-700 hover:text-red-600 transition">Usluge</a>
                <a href="#o-nama" class="text-gray-700 hover:text-red-600 transition">O nama</a>
                <a href="#kontakt" class="text-gray-700 hover:text-red-600 transition">Kontakt</a>
            </nav>
            <!-- CTA dugme -->
            <a href="#kontakt" class="bg-black text-white px-5 py-2.5 rounded-md font-semibold hover:bg-red-600 transition duration-300">
                Pozovite nas
            </a>
        </div>
    </header>

    <!-- INTRO/HERO SEKCIJA: Sa fade-in efektom -->
    <section class="relative bg-black text-white py-32 px-6 overflow-hidden flex items-center justify-center min-h-[75vh]">
        <!-- Pozadinski overlay -->
        <div class="absolute inset-0 bg-cover bg-center opacity-30" style="background-image: url('https://images.unsplash.com/photo-1549399542-7e3f8b79c341?q=80&w=1920');"></div>
        
        <div class="relative max-w-4xl mx-auto text-center fade-in-init z-10" id="hero-content">
            <h1 class="text-4xl md:text-6xl font-black mb-6 uppercase tracking-tight">
                Brza registracija i <span class="text-red-600">pouzdan uvoz</span> vozila
            </h1>
            <p class="text-lg md:text-xl text-gray-300 mb-10 max-w-2xl mx-auto">
                Agencija AM AUTO vam pruža kompletnu uslugu registracije, uvoza motornih vozila i bezbednog platnog prometa na jednom mestu.
            </p>
            <div class="flex flex-col sm:flex-row justify-center gap-4">
                <a href="#usluge" class="bg-red-600 hover:bg-red-700 text-white font-bold px-8 py-3.5 rounded-md transition duration-300 text-center">
                    Naše usluge
                </a>
                <a href="#kontakt" class="border-2 border-white hover:bg-white hover:text-black text-white font-bold px-8 py-3.5 rounded-md transition duration-300 text-center">
                    Kontaktirajte nas
                </a>
            </div>
        </div>
    </section>

    <!-- USLUGE SEKCIJA -->
    <section id="usluge" class="py-24 px-6 max-w-7xl mx-auto">
        <div class="text-center mb-16">
            <h2 class="text-3xl md:text-4xl font-black uppercase tracking-tight">Šta radimo za vas</h2>
            <div class="w-16 h-1 bg-red-600 mx-auto mt-4"></div>
        </div>
        
        <div class="grid md:grid-cols-3 gap-8">
            <!-- Kartica 1: Registracija -->
            <div class="bg-white p-8 rounded-lg shadow-sm border border-gray-100 hover:border-red-600 transition-all duration-300 group">
                <div class="w-12 h-12 bg-gray-100 text-red-600 flex items-center justify-center rounded-md font-bold text-xl mb-6 group-hover:bg-red-600 group-hover:text-white transition-all">
                    01
                </div>
                <h3 class="text-xl font-bold mb-3">Registracija vozila</h3>
                <p class="text-gray-600 leading-relaxed">
                    Kompletna priprema dokumentacije, tehnički pregled i izdavanje registracionih nalepnica bez odlaska u SUP.
                </p>
            </div>
            
            <!-- Kartica 2: Uvoz -->
            <div class="bg-white p-8 rounded-lg shadow-sm border border-gray-100 hover:border-red-600 transition-all duration-300 group">
                <div class="w-12 h-12 bg-gray-100 text-red-600 flex items-center justify-center rounded-md font-bold text-xl mb-6 group-hover:bg-red-600 group-hover:text-white transition-all">
                    02
                </div>
                <h3 class="text-xl font-bold mb-3">Uvoz motornih vozila</h3>
                <p class="text-gray-600 leading-relaxed">
                    Posredovanje pri kupovini, organizacija transporta, carinjenje i kompletna špediterska dokumentacija za vaš automobil.
                </p>
            </div>
            
            <!-- Kartica 3: Platni promet -->
            <div class="bg-white p-8 rounded-lg shadow-sm border border-gray-100 hover:border-red-600 transition-all duration-300 group">
                <div class="w-12 h-12 bg-gray-100 text-red-600 flex items-center justify-center rounded-md font-bold text-xl mb-6 group-hover:bg-red-600 group-hover:text-white transition-all">
                    03
                </div>
                <h3 class="text-xl font-bold mb-3">Platni promet</h3>
                <p class="text-gray-600 leading-relaxed">
                    Sve vrste uplata taksi, poreza i uplatnica brzo, sigurno i jednostavno na našem šalteru.
                </p>
            </div>
        </div>
    </section>

    <!-- KONTAKT SEKCIJA -->
    <section id="kontakt" class="bg-black text-white py-24 px-6">
        <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-12">
            <div>
                <h2 class="text-3xl md:text-4xl font-black uppercase tracking-tight mb-6">Budimo u kontaktu</h2>
                <p class="text-gray-400 mb-8 max-w-md">
                    Imate pitanja u vezi sa cenom registracije ili carinjenja? Posetite nas ili nas pozovite direktno.
                </p>
                <div class="space-y-4">
                    <p class="flex items-center text-gray-300"><span class="text-red-600 font-bold mr-3">A:</span> Prvi Novembar 250, LACARAK</p>
                    <p class="flex items-center text-gray-300"><span class="text-red-600 font-bold mr-3">T:</span> +381616065018</p>
                    <p class="flex items-center text-gray-300"><span class="text-red-600 font-bold mr-3">E:</span> amauto@gmail.com</p>
                </div>
            </div>
            <div class="bg-white text-black p-8 rounded-lg shadow-lg">
                <form class="space-y-4" onsubmit="event.preventDefault(); alert('Poruka je poslata!');">
                    <div>
                        <label class="block text-sm font-semibold mb-1 text-gray-700">Ime i prezime</label>
                        <input type="text" class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:border-red-600" required>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold mb-1 text-gray-700">Telefon</label>
                        <input type="tel" class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:border-red-600" required>
                    </div>
                    <div>
                        <label class="block text-sm font-semibold mb-1 text-gray-700">Poruka</label>
                        <textarea rows="4" class="w-full p-3 border border-gray-300 rounded focus:outline-none focus:border-red-600" required></textarea>
                    </div>
                    <button type="submit" class="w-full bg-red-600 hover:bg-red-700 text-white font-bold py-3 rounded transition duration-300">
                        Pošalji upit
                    </button>
                </form>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="bg-gray-900 text-gray-500 text-center py-6 border-t border-gray-800 text-sm">
        <p>&copy; 2026 AM AUTO. Sva prava zadržana.</p>
    </footer>

    <!-- JavaScript za Fade-In efekat na učitavanju -->
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const heroContent = document.getElementById("hero-content");
            if (heroContent) {
                // Mali timeout da bi efekat bio primetan nakon što browser renderuje osnovu
                setTimeout(() => {
                    heroContent.classList.add("fade-in-visible");
                }, 150);
            }
        });
    </script>
</body>
</html>
"""
            self.wfile.write(html_code.encode('utf-8'))
        else:
            super().do_GET()

if __name__ == "__main__":
    print(f"Pokretanje AM AUTO servera na portu {PORT}...")
    print(f"Otvorite brauzer i idite na: http://localhost:{PORT}")
    print("Za zaustavljanje servera pritisnite CTRL+C u terminalu.")
    
    # Dozvoljava ponovno zauzimanje porta bez čekanja operativnog sistema
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer uspešno zaustavljen.")
