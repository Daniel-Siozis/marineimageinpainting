import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Input, Conv2DTranspose
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.optimizers import Adamax
from tensorflow.keras.callbacks import EarlyStopping
import os
from PIL import Image

# Definiere dein vortrainiertes Modell, z.B. ein einfaches CNN
def create_model():
    model = Sequential()
    model.add(Input(shape=(64, 64, 3)))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(Conv2DTranspose(3, (3, 3), activation='relu', padding='same'))
    return model

# Lade deine Bilder und ihre beschädigten Versionen
def load_data(train_path, noisy_path):
    # Hier lädst du deine Bilder und ihre beschädigten Versionen
    valid_images_paths = []  # Liste mit den Bildern
    broken_images_paths = []   # Liste mit den beschädigten Versionen der Bilder

    counter = 0
    for filename in os.listdir(train_path):
        counter = counter + 1
        img_path = os.path.join(train_path, filename).replace("\\","/")
        valid_images_paths.append(img_path)
        if counter == 12000:
            break
    
    counter = 0

    for filename in os.listdir(noisy_path):
        counter = counter + 1
        img_path = os.path.join(noisy_path, filename).replace("\\","/")
        broken_images_paths.append(img_path)
        if counter == 12000:
            break

    valid_images = []
    for path in valid_images_paths:
        image = Image.open(path)
        valid_images.append(np.array(image) / 255.0)

    broken_images = []
    for path in broken_images_paths:
        noisy_image = Image.open(path)
        broken_images.append(np.array(noisy_image) / 255.0)

    # Konvertiere die Listen in NumPy-Arrays und füge die Batch-Dimension hinzu
    valid_train_images = np.array(valid_images)
    broken_train_images = np.array(broken_images)

    print(valid_train_images.shape)
    print(broken_train_images.shape)
    return valid_train_images, broken_train_images

# Definiere den Modelltrainingsprozess
def train_model(model, train_images, train_images_noisy):
    # Auswahl zwischen den Optimizer Adam, Nadam und Adamax & Anpassung der learning_rate
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')

    # Anpassung der patience (5: nach 5 Epochen ohne Fortschritt beim 'loss' wird frühzeitig gestoppt)
    early_stopping = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)

    # Anpassung der epochs und batch_size
    model.fit(train_images_noisy, train_images, epochs=30, batch_size=1, callbacks=[early_stopping])

# Hauptfunktion zum Trainieren und Speichern des Modells
def main():
    # Lade Daten
    train_path = 'Dataset\lid'
    noisy_path = 'Dataset\oken'
    train_images, train_images_noisy = load_data(train_path, noisy_path)

    # Erstelle das Modell
    model = create_model()

    # Trainiere das Modell
    train_model(model, train_images, train_images_noisy)

    # Speichere das trainierte Modell
    model.save('inpainting_64x64_model.h5')

if __name__ == "__main__":
    main()
