from PIL import Image, ImageDraw
import os
import random

def add_black_box_to_images(input_dir, output_dir):
    # Überprüfe, ob der Ausgabeordner existiert, andernfalls erstelle ihn
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Gehe durch jede Datei im Eingabeordner
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Überprüfe, ob es sich um eine Bilddatei handelt
            input_path = os.path.join(input_dir, filename)

            # Umbenennen des Bildes
            new_filename = "broken" + filename
            output_path = os.path.join(output_dir, new_filename)

            # Öffne das Bild
            image = Image.open(input_path)
            
            # Bestimme die Größe des Bildes
            image_width, image_height = image.size
            
            # Generiere zufällige Größe für den schwarzen Kasten
            box_width = random.randint(10, image_width // 2)
            box_height = random.randint(10, image_height // 2)
            
            # Generiere zufällige Position für den schwarzen Kasten
            box_left = random.randint(0, image_width - box_width)
            box_top = random.randint(0, image_height - box_height)
            box_right = box_left + box_width
            box_bottom = box_top + box_height
            
            # Erstelle ein Draw-Objekt, um auf das Bild zu zeichnen
            draw = ImageDraw.Draw(image)
            
            # Zeichne den schwarzen Kasten
            draw.rectangle([box_left, box_top, box_right, box_bottom], fill="black")
            
            # Speichere das bearbeitete Bild im Ausgabeordner
            image.save(output_path)
            print(f"Ein schwarzer Kasten wurde erfolgreich in der Mitte des Bildes platziert und unter {output_path} gespeichert.")

# Beispielaufruf der Funktion
source_directory = "Dataset\lid"
destination_directory = "Dataset\oken"
add_black_box_to_images(source_directory, destination_directory)