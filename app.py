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
st.title('⚽ Apendicity FC')
st.write('### queremosunagalletadelnata')

st.header('Nuestro Equipo', anchor='nuestro-equipo')
# Función para mostrar imágenes con seguridad
def mostrar_img(archivo, texto):
    if os.path.exists(archivo):
        st.image(archivo, caption=texto)
    else:
        st.info(f"Subiendo foto: {archivo}")

mostrar_img('equipo.jpg', 'Plantel Oficial Apendicity FC')

st.subheader('Calendario y Resultados')
res = {
    'Fecha': ['14/05', '07/05', '09/04', '27/03'],
    'Rival': ['Real Parir FC', 'Dopaminitas', 'Melatominas', 'Staphylogol'],
    'Marcador': ['POR JUGAR', '0 - 1', '0 - 4', '1 - 2']
}
st.table(res)

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
