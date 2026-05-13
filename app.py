import streamlit as st
import os
st.set_page_config(page_title='Apendicity FC', layout='wide')
st.title('Apendicity FC')
st.write('### queremosunagalletadelnata')
if os.path.exists('equipo.jpg'): st.image('equipo.jpg', caption='Plantel Oficial')
st.header('Resultados')
res = {'Fecha': ['14/05', '07/05', '09/04', '27/03'], 'Rival': ['Real Parir FC', 'Dopaminitas', 'Melatominas', 'Staphylogol'], 'Marcador': ['POR JUGAR', '0-1', '0-4', '1-2']}
st.table(res)
st.header('Merch y Suplementos')
c1, c2, c3 = st.columns(3)
with c1:
    if os.path.exists('polera.png'): st.image('polera.png', caption='Polera')
    if os.path.exists('proteina.png'): st.image('proteina.png', caption='Proteina')
with c2:
    if os.path.exists('jockey.png'): st.image('jockey.png', caption='Jockey')
    if os.path.exists('botellas.png'): st.image('botellas.png', caption='Botella')
with c3: st.info('Proximo partido: 14 de Mayo')
st.write('(c) 2026 queremosunagalletadelnata')