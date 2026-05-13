import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title='Apendicity FC', layout='wide', page_icon='⚽')

# --- ESTILOS CSS (Dorado y Colores del Logo) ---
st.markdown("""
    <style>
    .player-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        border: 2px solid #D4AF37; /* Dorado metálico */
        border-radius: 12px;
        padding: 12px;
        text-align: center;
        margin-bottom: 15px;
        min-height: 130px;
        box-shadow: 0px 4px 10px rgba(212, 175, 55, 0.2);
        transition: all 0.3s ease;
    }
    .player-card:hover {
        transform: translateY(-8px);
        box-shadow: 0px 8px 20px rgba(212, 175, 55, 0.4);
        border-color: #f1d592;
    }
    .number-style {
        background: linear-gradient(to bottom, #f1d592, #D4AF37);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        font-size: 32px;
        font-weight: 900;
        line-height: 1;
    }
    .name-style {
        color: #ffffff;
        margin: 5px 0;
        font-size: 16px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .pos-style {
        color: #D4AF37;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .section-header {
        color: #D4AF37;
        font-family: 'Arial Black', sans-serif;
        border-left: 5px solid #D4AF37;
        padding-left: 15px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

def mostrar_img(archivo, texto):
    if os.path.exists(archivo):
        st.image(archivo, caption=texto)
    else:
        st.info(f"Subiendo archivo: {archivo}")

# --- SIDEBAR ---
with st.sidebar:
    st.title("📍 Menú")
    st.markdown("[⚽ Equipo](#nuestro-equipo)")
    st.markdown("[👕 Tienda](#merch-y-suplementos)")
    st.markdown("[📞 Contacto](#contáctanos)")

# --- CABECERA ---
st.title('⚽ Apendicity FC')
st.write('### queremosunagalletadelnata')

# --- SECCIÓN: NUESTRO EQUIPO ---
st.header('Nuestro Equipo', anchor='nuestro-equipo')
mostrar_img('equipo.jpg', 'Plantel Oficial Apendicity FC')

# --- CATEGORÍAS ACTUALIZADAS ---
categorias = {
    "🧤 ARQUERAS": [
        {"n": "Frías", "num": "19", "p": "Arquero/Defensa"},
        {"n": "Urra", "num": "88", "p": "Universal"} # Movida aquí
    ],
    "🛡️ LÍNEA DEFENSIVA": [
        {"n": "Poblete", "num": "8", "p": "Defensa Central"},
        {"n": "Rosenfeld", "num": "18", "p": "Defensa"},
        {"n": "Cerpa", "num": "4", "p": "Defensa"},
        {"n": "Inés", "num": "24", "p": "Defensa/Medio"},
        {"n": "Samacoitz", "num": "6", "p": "Defensa/Medio Def."}
    ],
    "🎯 MEDIOCAMPO": [
        {"n": "Acevedo", "num": "22", "p": "Medio Ofensivo"},
        {"n": "Paredes", "num": "10", "p": "Medio Ofensivo"},
        {"n": "Anto Lagos", "num": "12", "p": "Defensa/Medio Of."},
        {"n": "Coya", "num": "??", "p": "Medio Ofensivo"},
        {"n": "Maguire", "num": "3", "p": "Defensa/Medio Of."},
        {"n": "Cami", "num": "??", "p": "Medio Defensivo"}
    ],
    "⚡ ATAQUE Y UNIVERSALES": [
        {"n": "Nina", "num": "11", "p": "Delantera"},
        {"n": "Agus", "num": "16", "p": "Delantera/Medio"},
        {"n": "Guti", "num": "7", "p": "Universal"},
        {"n": "Elisol", "num": "5", "p": "Universal"},
        {"n": "Rafa", "num": "2", "p": "Universal"},
        {"n": "Pía", "num": "9", "p": "Universal"}
    ]
}

# Mostrar cartas
for cat, lista in categorias.items():
    st.markdown(f"<h3 class='section-header'>{cat}</h3>", unsafe_allow_html=True)
    cols = st.columns(5)
    for i, j in enumerate(lista):
        with cols[i % 5]:
            st.markdown(f"""
            <div class="player-card">
                <div class="number-style">{j['num']}</div>
                <div class="name-style">{j['n']}</div>
                <div class="pos-style">{j['p']}</div>
            </div>
            """, unsafe_allow_html=True)

st.divider()

# --- RESULTADOS ---
st.subheader('🏆 Calendario y Resultados')
res = {
    'Fecha': ['14/05', '07/05', '09/04', '27/03'],
    'Rival': ['Real Parir FC', 'Dopaminitas', 'Melatominas', 'Staphylogol'],
    'Marcador': ['POR JUGAR', '0 - 1', '0 - 4', '1 - 2']
}
st.table(res)

st.divider()

# --- MERCH ---
st.header('Merch y Suplementos', anchor='merch-y-suplementos')
m1, m2, m3 = st.columns(3)
with m1:
    mostrar_img('polera.png', 'Polera Oficial')
    mostrar_img('proteina.png', 'Proteína')
with m2:
    mostrar_img('jockey.png', 'Jockey')
    mostrar_img('botellas.png', 'Botella')
with m3:
    st.info('🚚 Envíos a todo Chile.')
    st.success('✅ Stock disponible.')

st.divider()

# --- NEWSLETTER ---
st.subheader('📩 Mantente al día')
col_news1, col_news2 = st.columns([2, 1])
with col_news1:
    email_usuario = st.text_input('Déjanos tu contacto para noticias:', placeholder='tu@correo.com')
with col_news2:
    st.write("##")
    if st.button('Suscribirme'):
        if email_usuario: st.toast(f'¡Registrado {email_usuario}!')
        else: st.warning('Ingresa un correo.')

st.divider()

# --- CONTACTO ---
st.header('Contáctanos!!', anchor='contáctanos')
c1, c2, c3 = st.columns(3)
with c1:
    st.write("### 📸 Instagram")
    st.link_button("@apendicity._fc", "https://www.instagram.com/apendicity._fc")
with c2:
    st.write("### 📧 Email")
    st.write("Apendicity_fc@gmail.com")
with c3:
    st.write("### 📞 Teléfono")
    st.write("+569 4733 2124")

st.caption('© 2026 queremosunagalletadelnata')
