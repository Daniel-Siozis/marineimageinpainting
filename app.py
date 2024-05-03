import streamlit as st 

st.write('hello world test5')

st.title('Bild Hochladen')

# Datei hochladen
uploaded_file = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg"])

# Wenn eine Datei hochgeladen wurde
if uploaded_file is not None:
    # Zeige das hochgeladene Bild an
    st.image(uploaded_file, caption='Hochgeladenes Bild', use_column_width=True)