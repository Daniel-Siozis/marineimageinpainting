import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
 
# CSS für den animierten Hintergrund und spezifische Stile
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://www.bing.com/th/id/OGC.081f8cd08585e1040a8393c25b274126?pid=1.7&rurl=https%3a%2f%2fgiffiles.alphacoders.com%2f195%2f19516.gif&ehk=prgnSylokkfl0aH%2bDLaEqgHzeySBwEUCF8DG8yQCes8%3d");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
 
[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}
 
h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF;
}
 
.st-markdown {
    color: #FFFFFF;
}
 
[data-testid="stText"] {
    color: #FFFFFF;
}
 
.head {
    font-family: 'Lato', sans-serif;
    color: #000;
    padding: 10px;
    border: none;  /* Kein Rahmen */
    margin: 0;     /* Kein äußerer Abstand */
    border-radius: 5px;
    position: fixed;  /* Fixiere das Element */
    top: 0;           /* Abstand vom oberen Rand */
    left: 0;          /* Abstand vom linken Rand */
    width: 100%;      /* Volle Breite */
    z-index: 1000;    /* Über anderen Elementen */
}
 
.info-box {
    background-color: #FA0707;
    color: #FFFFFF;
    border-radius: 5px;
    padding: 10px;
}
 
.fische {
    background-color: #912424;
    color: #FFFFFF;
    padding: 10px;
    border-radius: 5px;
}
</style>
"""
 
# Einfügen des CSS in die Streamlit-App
st.markdown(page_bg_img, unsafe_allow_html=True)
 
# Streamlit-Anwendung
st.markdown('<div class="head"><h4>Sehen Sie zu wie sich ihr Bild eigenständig reparieren lässt!</h4></div>', unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.markdown('<div class="info-box">Information! Es dürfen nur Bilder verwendet werden, die unter Wasser aufgenommen wurden</div>', unsafe_allow_html=True)
st.write("")
# Datei hochladen
uploaded_file = st.file_uploader("Laden Sie hier Ihre Fischbilder hoch!", type=["png", "jpg", "jpeg"])

# Lade das trainierte Modell
model = load_model('trained_model.h5')

# Funktion zur Reparatur des Bildes
def repair_image(image):
    # Vorverarbeitung des Bildes
    image = np.array(image)
    image = image / 255.0 # Normalisierung auf den Bereich [0, 1]
    
    # Vorhersage mit dem Modell
    predicted_image = model.predict(np.expand_dims(image, axis=0))

    # Nachverarbeitung des reparierten Bildes
    predicted_image = np.squeeze(predicted_image, axis=0)
    predicted_image = (predicted_image * 255).astype(np.uint8) # Rückkehr zum urpsrünglichen Bereich [0, 255]
    
    return predicted_image
 
# Wenn eine Datei hochgeladen wurde
if uploaded_file is not None:
    # Zeige das hochgeladene Bild an
    st.image(uploaded_file, caption='Hochgeladenes Bild', use_column_width=True)
 
    # Repariere das Bild, wenn der Benutzer auf die Schaltfläche klickt
    if st.button('Reparieren'):
        # Öffne das hochgeladene Bild
        image = Image.open(uploaded_file)
 
        # Repariere das Bild
        repaired_image = repair_image(image)
 
        # Zeige das reparierte Bild an
        st.image(repaired_image, caption='Repariertes Bild', use_column_width=True)
