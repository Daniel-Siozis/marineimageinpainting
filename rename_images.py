import os
import shutil
from PIL import Image

def rescale_images(source_dir, dest_dir):
    newSize = (64,64)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    counter = 1
    # Gehe durch jede Datei im Quellverzeichnis
    for filename in os.listdir(source_dir):
        # Überprüfe, ob die Datei eine Bilddatei ist (du kannst die Bedingung anpassen, je nach den Dateitypen, die du verschieben möchtest)
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Erzeuge den neuen Dateinamen (hier können auch andere Methoden zur Umbenennung verwendet werden)
            new_filename = str(counter) + "-valid.jpg"
            # Konstruiere den Pfad zur aktuellen Datei und zur Ziel-Datei
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, new_filename)
            # Kopiere die Datei in das Zielverzeichnis und benenne sie dabei um
            shutil.copy(source_file, dest_file)
            with Image.open(dest_file) as img:
                resized_img = img.resize(newSize, Image.Resampling.LANCZOS)
                resized_img.save(dest_file)
            counter = counter +1

# Beispielaufruf der Funktion
source_directory = "Dataset\original"
destination_directory = "Dataset\lid"
rescale_images(source_directory, destination_directory)
