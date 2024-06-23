import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Conv2DTranspose, Input, BatchNormalization, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.optimizers import Adamax
from tensorflow.keras.callbacks import EarlyStopping
import os
from PIL import Image

# Definiere dein Modell als Fully Convolutional Network
def create_model(input_shape=(None, None, 3)):
    model = Sequential()
    model.add(Input(shape=input_shape))
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(BatchNormalization())
    model.add(Conv2DTranspose(3, (3, 3), activation='sigmoid', padding='same'))  # Ändere die Aktivierung zu sigmoid
    return model

# Lade die Daten und stelle sicher, dass die Bilder die gleiche Größe haben
def load_data(train_path, noisy_path, target_size=(64, 64)):
    valid_images_paths = []
    broken_images_paths = []

    for filename in os.listdir(train_path)[:13953]:
        img_path = os.path.join(train_path, filename).replace("\\", "/")
        valid_images_paths.append(img_path)

    for filename in os.listdir(noisy_path)[:13953]:
        img_path = os.path.join(noisy_path, filename).replace("\\", "/")
        broken_images_paths.append(img_path)

    valid_images = []
    for path in valid_images_paths:
        image = Image.open(path)
        image = image.resize(target_size)
        valid_images.append(np.array(image) / 255.0)

    broken_images = []
    for path in broken_images_paths:
        noisy_image = Image.open(path)
        noisy_image = noisy_image.resize(target_size)
        broken_images.append(np.array(noisy_image) / 255.0)

    valid_train_images = np.array(valid_images)
    broken_train_images = np.array(broken_images)

    print(f'Valid images shape: {valid_train_images.shape}')
    print(f'Broken images shape: {broken_train_images.shape}')
    return valid_train_images, broken_train_images

# Trainiere das Modell mit den Bildern
def train_model(model, train_images, train_images_noisy):
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    
    early_stopping = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)
    
    model.fit(train_images_noisy, train_images, epochs=30, batch_size=1, callbacks=[early_stopping])

# Hauptfunktion zum Trainieren und Speichern des Modells
def main():
    train_path = 'Dataset/lid'
    noisy_path = 'Dataset/oken'
    train_images, train_images_noisy = load_data(train_path, noisy_path)

    model = create_model()

    train_model(model, train_images, train_images_noisy)

    model.save('trained_model.h5')

if __name__ == "__main__":
    main()
