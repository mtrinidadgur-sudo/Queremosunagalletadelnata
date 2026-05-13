import streamlit as st
import os

# Configuración de la página
st.set_page_config(page_title='Apendicity FC', layout='wide', page_icon='⚽')

# --- ÍNDICE DESPLEGABLE (SIDEBAR) ---
with st.sidebar:
    st.title("📍 Navegación")
    st.markdown("[⚽ Nuestro Equipo](#nuestro-equipo)")
    st.markdown("[👕 Merch y Suplementos](#merch-y-suplementos)")
    st.markdown("[📞 Contáctanos!!](#contáctanos)")
    st.divider()
    st.write("Próximo partido: **14 de Mayo**")

# --- SECCIÓN: NUESTRO EQUIPO ---
st.header('Nuestro Equipo', anchor='nuestro-equipo')
st.write('### Plantel Oficial Apendicity FC')

# Lista de jugadoras
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

# Diseño de "Cartas" en cuadrícula (4 por fila)
cols = st.columns(4)
for i, j in enumerate(jugadoras):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="border: 2px solid #FFD700; border-radius: 10px; padding: 15px; text-align: center; background-color: #1e1e1e; margin-bottom: 20px; min-height: 150px;">
            <h1 style="color: #FFD700; margin: 0; font-size: 40px;">{j['num']}</h1>
            <h3 style="color: white; margin: 5px 0;">{j['n']}</h3>
            <p style="color: #cccccc; font-size: 14px; font-style: italic;">{j['p']}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# --- SECCIÓN: MERCH ---
st.header('Merch y Suplementos', anchor='merch-y-suplementos')
c1, c2, c3 = st.columns(3)
with c1:
    mostrar_img('polera.png', 'Polera - $25')
    mostrar_img('proteina.png', 'Proteina - $40')
with c2:
    mostrar_img('jockey.png', 'Jockey - $15')
    mostrar_img('botellas.png', 'Botella - $10')
with c3:
    st.info('🚚 Envíos a todo el país')
    st.success('✅ Stock disponible')

st.divider()

# --- SECCIÓN: NEWSLETTER ---
st.subheader('📩 Mantente al día')
col_news1, col_news2 = st.columns([2, 1])
with col_news1:
    email_usuario = st.text_input('Si quieres recibir noticias de nuestro equipo, déjanos tu contacto:', placeholder='tu@email.com')
with col_news2:
    if st.button('Suscribirme'):
        if email_usuario:
            st.toast(f'¡Gracias! Registramos a {email_usuario}')
        else:
            st.error('Ingresa un correo')

st.divider()

# --- SECCIÓN: CONTACTO ---
st.header('Contáctanos!!', anchor='contáctanos')
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 📸 Instagram")
    st.write("[@apendicity._fc](https://www.instagram.com/apendicity._fc)")

with col2:
    st.markdown("### 📧 Email")
    st.write("Apendicity_fc@gmail.com")

with col3:
    st.markdown("### 📞 Teléfono")
    st.write("+569 4733 2124")

st.markdown('---')
st.caption('© 2026 queremosunagalletadelnata | Todos los derechos reservados')
