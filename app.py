import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://media.giphy.com/media/zvCG9M91fwjCgsdB70/giphy.gif?cid=790b7611i6a6xemzy77p4375hnvxo0r6g56z8s7raz8phfc6&ep=v1_gifs_search&rid=giphy.gif&ct=g");
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
    border: none;
    margin: 0;
    border-radius: 5px;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
}

.info-box {
    background-color: #FFDE59;
    color: #FFFFFF;
    border-radius: 5px;
    padding: 10px;
}
.example {
  color: #FFFFFF;
}

.fische {
    background-color: #912424;
    color: #FFFFFF;
    padding: 10px;
    border-radius: 5px;
}

/* Sidebar-Styling */
[data-testid="stSidebar"] {
    background-color: #262527;
    width: 10% !important;
}


[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] h4, [data-testid="stSidebar"] h5, [data-testid="stSidebar"] h6 {
    color: #FFFFFF;
}

[data-testid="stSidebar"] .css-1d391kg {
    color: #FF0000;
}
[data-testid="stSidebar"] .st-emotion-cache-1nm2qww {
    color: #FFFFFF;
}
[data-testid="stSidebar"] .st-emotion-cache-j6qv4b p {
    color: #FFFFFF;
}
[data-testid="stSidebar"] .st-emotion-cache-ue6h4q{
 color: #262527;
}

[data-testid="stSidebar"] .css-1l0t84s {
    color: #FF0000;
}

[data-testid="stSidebar"] .st-ay {
    background-color: #000080;
    color: #FF0000;
    }

[data-testid="stSidebar"] .css-1cpxqw2 {
    color: #FF0000;
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)
st.sidebar.title("Menü")
page = st.sidebar.radio("Selection-Screen", ["Hauptmenü", "Dokumentation", "Examples", "Über uns"])


# Leere Sidebar, um sicherzustellen, dass die Sidebar sichtbar ist
st.sidebar.empty()
# Dann fügen wir den eigentlichen Inhalt hinzu
if page != "Über uns":
    st.markdown('<div class="head"><h4>Sehen Sie zu wie sich ihr Bild eigenständig reparieren lässt!</h4></div>', unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown('<div class="info-box">Information! Es dürfen nur Bilder verwendet werden, die unter Wasser aufgenommen wurden.</div>', unsafe_allow_html=True)
    st.write("")
    uploaded_file = st.file_uploader("Laden Sie hier Ihre Fischbilder hoch!", type=["png", "jpg", "jpeg"])

model = load_model('trained_model.h5')
def repair_image(image, target_size=(64, 64)):
    # Originalbildgröße speichern
    original_size = image.size
    
    # Vorverarbeitung des Bildes
    image = image.resize(target_size)  # Bild auf Modellgröße skalieren
    image_array = np.array(image) / 255.0  # Normalisierung auf den Bereich [0, 1]
    
    # Vorhersage mit dem Modell
    predicted_image = model.predict(np.expand_dims(image_array, axis=0))
    
    # Nachverarbeitung des reparierten Bildes
    predicted_image = np.squeeze(predicted_image, axis=0)
    predicted_image = (predicted_image * 255).astype(np.uint8)  # Rückkehr zum ursprünglichen Bereich [0, 255]
    predicted_image = Image.fromarray(predicted_image)
    
    # Bild auf ursprüngliche Größe zurückskalieren
    predicted_image = predicted_image.resize(original_size)
    
    return predicted_image

# Wenn eine Datei hochgeladen wurde
if page!="Über uns" and uploaded_file is not None:
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


if page == "Bild reparieren":
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Hochgeladenes Bild', use_column_width=True)
        if st.button('Reparieren'):
            image = Image.open(uploaded_file)
            repaired_image = repair_image(image)
            st.image(repaired_image, caption='Repariertes Bild', use_column_width=True)

elif page == "Dokumentation":
    st.write("Hier können weitere Unterpunkte hinzugefügt werden.")

elif page == "Examples":
    
    
    # Beispielbilder laden (entweder lokal oder von einer URL)
    example_images = [
        ("Beispielbild 1", "MarineInpaint/Bilder/oken/1-broken.jpg", "MarineInpaint/Bilder/original/7393_F1_f000000.jpg"),
        
    ]
    
    for title, original, repaired in example_images:
        st.markdown('<div class="example">Hier sehen Sie wie es funktionieren kann</div>', unsafe_allow_html=True)
        st.write(title)
        st.image(original, caption='Originalbild', use_column_width=True)
        st.image(repaired, caption='Repariertes Bild', use_column_width=True)
        st.write("")

elif page == "Über uns":
    st.title("Über uns")
    st.subheader("Unser Team")
    box_style = """
    <style>
    .box {
        background-color: #f9f9f9;
        border: solid #ddd;
        padding: 10px;
        border-radius: 1px;
        margin-bottom: 10px;
    }
    .box h3{
    color: #000000; }
    </style>
    """
    st.markdown(box_style, unsafe_allow_html=True)

    st.markdown("""
    <div class="box">
        <h3>Daniel Siozis</h3>
        <p>Modell-Entwicklung</p>
        <p><strong>Persona:</strong> Durch die Automatisierung komplexer Aufgaben kann KI die Effizienz und Produktivität in verschiedensten Branchen, von der Medizin bis zur Automobilindustrie, enorm steigern.
                Durch die Automatisierung komplexer Aufgaben kann KI die Effizienz und Produktivität in verschiedensten Branchen, von der Medizin bis zur Automobilindustrie, enorm steigern.
            Durch die enorme und schnelle Datenverarbeitung werden auch schnell neue Erkenntnisse gewonnen, die überall neue Erfolge erzielen könnten.
 
</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="box">
        <h3>Samuel Arapoglu</h3>
        <p>Webentwicklung</p>
        <p><strong>Persona:</strong> Durch meine Position als Werkstudent in der Energiewirtschaft habe ich neben der Tätigkeit als SAP ABAP Entwickler die Möglichekit bei der Implementierung eines internen GPT Modells 
            mitzuwirken. KI kann dadurch wichtige Daten vor Dritten schützen.
   </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
     <div class="box">
        <h3>Berkan Türkel</h3>
        <p>Hardwarebereitstellung & Modelltraining</p>
        <p><strong>Persona:</strong> Künstliche Intelligenz ermöglicht die effiziente Analyse großer Datenmengen und die Lösung komplexer Probleme. In Bereichen wie Medizin und Umwelt eröffnet sie neue Perspektiven und optimiert Prozesse. Dadurch trägt sie maßgeblich zu einer intelligenteren und nachhaltigeren Zukunft bei.</p>
    </div>
        """, unsafe_allow_html=True)
    st.markdown("""
     <div class="box">
        <h3>Muriz Ganic</h3>
        <p>Modelltraining</p>
        <p><strong>Persona:</strong> Künstliche Intelligenz ist nicht nur Technologie, sondern der Schlüssel, um die komplexesten Herausforderungen unserer Zeit zu lösen. Durch ihre Fähigkeit, immense Datenmengen in kürzester Zeit zu verarbeiten, eröffnet sie neue Möglichkeiten in Medizin, Umweltwissenschaften und vielen anderen Bereichen. 
                KI hilft uns, effizientere Lösungen zu finden, die unseren Alltag nachhaltiger und intelligenter gestalten.</p>
    </div>
        """, unsafe_allow_html=True)
    
    
  
    # Optional: Hinzufügen von Abständen für eine bessere Lesbarkeit
    st.markdown("---")
    
