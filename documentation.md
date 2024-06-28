# Marine Image Inpainting

Muriz Ganic (it78iwat/23215741), Daniel Siozis (ha04giji/23171488), Berkan Türkel (yb57ogox/22833043), Samuel Arapoglu (os78odaz/23198175) 

## 1 Introduction

Welcome to our project on Marine Image Inpainting! This repository contains the code and resources for our AI model designed to repair and enhance images captured by underwater cameras. The primary objective of this project is to address the common issues faced in underwater photography, such as image degradation and data loss, by using deep learning techniques.

### Motivation
The underwater world presents a host of challenges for capturing high-quality images. Factors such as murky water, low light conditions, and physical obstructions often result in images that are damaged or incomplete. (These imperfections can impede the progress of marine research, conservation efforts, and various industrial activities.) Our project aims to tackle these issues by leveraging advanced AI techniques to repair and restore underwater images, thereby enhancing their clarity and utility.

### Research question
How can deep learning techniques be optimized to effectively repair and enhance underwater images captured by underwater cameras, despite the challenges posed by poor visibility, low light, and physical obstructions?

#### How is this document structured
This document is organized in the following sections:
1.	Introduction
2.	Related Work
3.	Methodology
4.	Results
5.	Discussion
6.	Conclusion

## 2 Related Work

#### Underwater Image Enhancement
Enhancing underwater images is critical for improving visibility and color accuracy, which are often degraded due to water absorption and scattering. Effective enhancement techniques are essential for applications in marine biology, underwater exploration, and environmental monitoring.
#### "Underwater Image Restoration Based on Convolutional Neural Networks"
•	Wang et al. (2019) explore using convolutional neural networks (CNNs) for restoring underwater images, focusing on improving visibility and color accuracy through deep learning techniques.
#### "GAN-Based Underwater Image Enhancement"

•	Chang et al. (2023) utilizes generative adversarial networks (GANs) to enhance underwater images, focusing on improving image quality by addressing color distortion and low visibility.


#### Image Inpainting
Image inpainting is vital for reconstructing damaged or missing parts of images, which is particularly challenging in underwater environments due to complex textures and lighting conditions. Advanced inpainting techniques ensure the integrity and usability of underwater imagery for scientific analysis and documentation.

#### „Efficient Computational Techniques for Real-Time Underwater Image Inpainting"
•	Yu et al. (2022) present efficient computational techniques designed for real-time inpainting of underwater images, emphasizing the importance of speed and resource optimization in practical underwater applications.


By integrating insights from these studies, our project in marine image inpainting draws inspiration and methodologies from these research papers to enhance the restoration and quality of underwater images, contributing to the field with AI-driven solutions.

## 3 Methodology
### 3.1 General Methodology
1.	Data Acquisition: We began by acquiring the DeepFish dataset, which offered a comprehensive collection of underwater images essential for training our model.
2.	Data Preparation: We then developed a program to artificially create damaged images by adding black boxes to the originals, simulating real-world degradation. Generating a set of damaged images alongside the original ones.
3.	Model Development: We designed a Convolutional Neural Network (CNN) model specifically for image inpainting.
4.	Model Training: We trained our model using supervised learning techniques. This involved feeding the model both the damaged and the corresponding original images.
5.	Deployment: Finally, we deployed the trained model via a Streamlit app, allowing users to upload damaged images and view the inpainted results.

### 3.2 Data Understanding and Preparation

We used the JCU DeepFish dataset for our project. The dataset originally consists of approximately 40 thousand images collected underwater from 20 habitats in the marine-environments of tropical Australia. Videos for DeepFish were collected for 20 habitats from remote coastal marine environments of tropical Australia. 
To simulate damaged images, we developed a program that artificially created damaged versions by adding black boxes to some of the original images. This process generated a set of both valid and damaged images, which we used to train our model. We also had downscale the images to 64x64 pixels due to hardware constraints.
### 3.3 Modeling and Evaluation
#### 3.3.1 Model 
We used a simple convolutional neural network (CNN) model for our marine image inpainting project. The model consists of several convolutional layers for feature extraction and a transposed convolutional layer for reconstructing the repaired images.

#### 3.3.2 Parameters 
For our marine image inpainting project, we configured several key training parameters to optimize model performance:
-	Learning rate = 0.001 with Adam Optimizer 
-	Epochs = 30
-	Batch_size = 1
-	Patience (Early Stopping) = 5

#### 3.3.3 Training
We trained our model using supervised learning with TensorFlow on our own hardware, specifically an RTX 3090 Ti GPU, utilizing CUDA to reduce training time. To manage hardware limitations, we downscaled the images to 64x64 resolution. The training dataset included both valid and damaged images. Training durations varied between 20 to 60 minutes per session. Additionally, we implemented an early stopping mechanism that halted training if the model ceased making useful progress, ensuring efficient use of resources.

## 4 Results

### 4.1 Artifacts 
Model Architecture
-	Convolutional Neural Network (CNN): We designed and implemented a CNN specifically tailored for image inpainting tasks.

Dataset
-	Training and Testing Datasets: We compiled a dataset of underwater images, including both clean images and their artificially damaged counterparts.

Trained model
-	Saved Model File: After training, we saved the trained model as ‘trained_model.h5‘.

Documentation
-	Readme

### 4.2  Libraries and Tools

-	NumPy: for handling and processing image data
-	TensorFlow: for constructing and training our convolutional neural network (CNN) model. We leveraged its high-level Keras API to define the model architecture and perform training tasks.
-	PIL (Python Imaging Library): to load and preprocess the images in our dataset
-	os: to navigate directories and handle file paths for loading the dataset of underwater images and their damaged versions
-	Streamlit: for application deployment

### 4.3 Concept of the Streamlit App
We built an intuitive Streamlit app for marine image inpainting. Users can easily upload damaged or incomplete underwater images, which the app processes using our AI model to repair and restore them. The app displays the original and inpainted images side by side for comparison, allowing users to visually assess the improvements. The app also provides information about the AI model, its training process, and potential applications, ensuring transparency and understanding of the technology.

### 4.4 Results on unseen data
Our marine image inpainting model demonstrates promising performance when evaluated on unseen underwater images. The results indicate that the model can restore damaged areas. While there is always room for further refinement, the current performance is encouraging.

## 5 Discussion

### 5.1 Results/ Artifacts/ App

Our project resulted in a trained AI model capable of repairing underwater images, which we deployed via a Streamlit app. The app allows users to upload damaged images and view the repaired outputs.

### 5.2 Limitations

One significant limitation we encountered was hardware constraints, particularly with GPU memory (VRAM) and RAM. This limitation restricted our ability to process high-resolution images, necessitating the downscaling of our underwater images to 64x64 pixels.

### 5.3 Ethics Perspective

Dangers of the Application
The application of our marine image inpainting model could potentially be misused to generate misleading or manipulated images, which underscores the need for careful monitoring and ethical usage guidelines.

Transparency
We prioritize transparency by thoroughly documenting our methods, datasets, and model limitations, which helps users understand the capabilities and potential biases of our model, fostering trust and accountability.

Effects on Climate Change
Training machine learning models can have a notable carbon footprint.

### 5.4 Further research 
Further research could include expanding the dataset to encompass a wider variety of underwater scenes and damage types, enhancing the model's robustness. Additionally, exploring new evaluation metrics to better assess inpainting quality and realism would be beneficial. Lastly, efforts to enhance model efficiency, such as optimizing for reduced processing time and resource usage, would make the technology more practical for real-time applications.
-	Expanding the dataset to enhance the model’s robustness by having a wider variety of underwater scenes and damage types
-	Enhance model efficiency by reducing processing time and resource usage without sacrificing performance
-	Advanced features like optimizing for Real-Time Use. Allowing the model to process and repair underwater images in real-time, such as live video feeds from underwater robots.
## 6 Conclusion

In this project, we developed and tested an AI model for marine image inpainting, aimed at repairing damaged underwater images. Our findings indicate that the model performs reasonably well on unseen data, producing visually coherent and realistic inpainted images. However, the limitations due to hardware constraints led us to downscale images, which may affect the finer details of the restorations
By addressing the areas mentioned in ‘Further research’, future researchers can build on our work to further advance the field of marine image inpainting and its practical applications.



