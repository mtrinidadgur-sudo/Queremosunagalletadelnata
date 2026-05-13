import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title='Apendicity FC', layout='wide', page_icon='⚽')

# --- ESTILOS CSS PARA LAS CARTAS ---
st.markdown("""
    <style>
    .player-card {
        border: 2px solid #FFD700;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        background-color: #1e1e1e;
        margin-bottom: 20px;
        min-height: 180px;
        transition: transform 0.3s;
    }
    .player-card:hover {
        transform: scale(1.05);
        border-color: #ffffff;
    }
    .number-style {
        color: #FFD700;
        margin: 0;
        font-size: 45px;
        font-weight: bold;
    }
    .name-style {
        color: white;
        margin: 5px 0;
        font-size: 20px;
    }
    .pos-style {
        color: #cccccc;
        font-size: 14px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ÍNDICE DESPLEGABLE (SIDEBAR) ---
with st.sidebar:
    st.title("📍 Navegación")
    st.markdown("[⚽ Nuestro Equipo](#nuestro-equipo)")
    st.markdown("[👕 Merch y Suplementos](#merch-y-suplementos)")
    st.markdown("[📞 Contáctanos!!](#contáctanos)")
    st.divider()
    st.write("Próximo partido: **14 de Mayo**")
    st.write("⚽ Rival: **Real Parir FC**")

# --- CABECERA ---
st.title('⚽ Apendicity FC')
st.write('### queremosunagalletadelnata')

# --- SECCIÓN: NUESTRO EQUIPO (ESTILO CARTAS FIFA) ---
st.header('Nuestro Equipo', anchor='nuestro-equipo')

jugadoras = [
    {"n": "Nina", "num": "11", "p": "Delantera"},
    {"n": "Guti", "num": "7", "p": "Universal"},
    {"n": "Maguire", "num": "3", "p": "Defensa/Medio Of."},
    {"n": "Elisol", "num": "5", "p": "Universal"},
    {"n": "Acevedo", "num": "22", "p": "Medio Ofensivo"},
    {"n": "Paredes", "num": "10", "p": "Medio Ofensivo"},
    {"n": "Samacoitz", "num": "6", "p": "Defensa/Medio Def."},
    {"n": "Frías", "num": "19", "p": "Arquero/Defensa"},
    {"n": "Rafa", "num": "2", "p": "Universal"},
    {"n": "Rosenfeld", "num": "18", "p": "Defensa"},
    {"n": "Anto Lagos", "num": "12", "p": "Defensa/Medio Of."},
    {"n": "Pía", "num": "9", "p": "Universal"},
    {"n": "Urra", "num": "88", "p": "Universal"},
    {"n": "Poblete", "num": "8", "p": "Defensa Central"},
    {"n": "Inés", "num": "24", "p": "Defensa/Medio"},
    {"n": "Agus", "num": "16", "p": "Delantera/Medio"},
    {"n": "Coya", "num": "??", "p": "Medio Ofensivo"},
    {"n": "Cami", "num": "??", "p": "Medio Defensivo"},
    {"n": "Cerpa", "num": "4", "p": "Defensa"}
]

# Mostrar jugadoras en cuadrícula de 4
cols = st.columns(4)
for i, j in enumerate(jugadoras):
    with cols[i % 4]:
        st.markdown(f"""
        <div class="player-card">
            <div class="number-style">{j['num']}</div>
            <div class="name-style">{j['n']}</div>
            <div class="pos-style">{j['p']}</div>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- TABLA DE RESULTADOS ---
st.subheader('🏆 Calendario y Resultados')
res = {
    'Fecha': ['14/05', '07/05', '09/04', '27/03'],
    'Rival': ['Real Parir FC', 'Dopaminitas', 'Melatominas', 'Staphylogol'],
    'Marcador': ['POR JUGAR', '0 - 1', '0 - 4', '1 - 2']
}
st.table(res)

st.divider()

# --- SECCIÓN: MERCH ---
st.header('Merch y Suplementos', anchor='merch-y-suplementos')

def mostrar_img(archivo, texto):
    if os.path.exists(archivo):
        st.image(archivo, caption=texto)
    else:
        st.info(f"Foto pendiente: {archivo}")

c1, c2, c3 = st.columns(3)
with c1:
    mostrar_img('polera.png', 'Polera Oficial - $25')
    mostrar_img('proteina.png', 'Proteína Gold - $40')
with c2:
    mostrar_img('jockey.png', 'Jockey Club - $15')
    mostrar_img('botellas.png', 'Botella Hidratación - $10')
with c3:
    st.info('🚚 Realizamos envíos a todo Chile.')
    st.success('💳 Pago seguro con transferencia o Flow.')

st.divider()

# --- SECCIÓN: NEWSLETTER ---
st.subheader('📩 Noticias de Apendicity FC')
col_news1, col_news2 = st.columns([2, 1])
with col_news1:
    email_usuario = st.text_input('Si quieres recibir noticias de nuestro equipo, déjanos tu contacto:', placeholder='ejemplo@correo.com')
with col_news2:
    st.write("##") # Espaciador
    if st.button('Suscribirme'):
        if email_usuario:
            st.toast(f'¡Perfecto! {email_usuario} ha sido registrado.')
        else:
            st.warning('Por favor, ingresa un correo válido.')

st.divider()

# --- SECCIÓN: CONTACTO ---
st.header('Contáctanos!!', anchor='contáctanos')
cont1, cont2, cont3 = st.columns(3)

with cont1:
    st.write("### 📸 Instagram")
    st.link_button("Ir a @apendicity._fc", "https://www.instagram.com/apendicity._fc")

with cont2:
    st.write("### 📧 Email")
    st.write("Apendicity_fc@gmail.com")

with cont3:
    st.write("### 📞 Teléfono")
    st.write("+569 4733 2124")

st.markdown('---')
st.caption('© 2026 queremosunagalletadelnata | Apendicity FC Official Website')
