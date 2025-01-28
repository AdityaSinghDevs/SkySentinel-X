# SkySentinel-X

Micro-Doppler Target Classification system for the Smart India Hackathon (SIH). Using spectrograms generated from STFT on FMCW radar data, the system employs deep learning models to classify drones and birds by their micro-Doppler signatures. A web interface will display real-time monitoring and detection for enhanced airspace security.

---
## Reference  

If you use this work, data, or any part of this project document, please provide appropriate credit by mentioning the repository as a reference:  

**SkySentinel-X** - Project Log Repository  
GitHub: [AdityaSinghDevs/SkySentinel-X](https://github.com/AdityaSinghDevs/SkySentinel-X)  

Your acknowledgment helps in maintaining transparency and credits the effort behind this work. Thank you!

---
+ ## Upcoming Updates  

+ The repository will soon be updated with organized datasets and additional gsource code.  
+ These updates will include refined data, improved documentation, and structured implementations.  
---

## Development Log

### Project Overview

- **Start Date:** 23 Sep
- **Team Members:**
  - Aditya Pratap Singh
  - Mohd Arham
  - Aman Sigroha
  - Pranay Vohra
  - Eish Chandeal

- **Project Goals:**
  
  The goal is to create software for the identification of flying objects based on their micro-Doppler signatures, determining whether it is a UAV (Unmanned Aerial Vehicle) or a bird.  
  The software will be in the form of a web application that displays information about the flying object, including its classification and additional features such as velocity,     
  coordinates, and visual movement patterns in 2D and 3D formats. The core models will be CNN and RNN, used to analyze micro-Doppler signatures and provide accurate classification 
  results.

---

### Week 1: [26 Aug - 1 Sep]

#### Objectives:
1. Understand the problem statement, study research papers on micro-Doppler signature analysis and object identification, and learn radar system principles.
2. Figure out the system's implementation and identify necessary machine learning models for accurate classification.
3. Determine the required tech stack and how these technologies will interact for real-time data processing through radar systems.
4. Design a UI for the presentation.
5. Create and submit a project synopsis outlining basic information and the required tech stack.

#### Progress:
- Objective 1: Completed – Research papers were studied and stored in a shared document.
- Objective 2: Completed – Concluded CNNs and RNNs will be required.
- Objective 3: Completed – Decided on a web-based product integrating ML models.
- Objective 4: Completed – UI design created using Figma.
- Objective 5: Completed – Synopsis submitted.

#### Challenges & Solutions:
1. **Challenge:** Understanding the integration of technologies and signal processing.
   
   - **Solution:** Signals will be processed into STFT spectrograms, with CNNs for object classification and RNNs for object tracking and visualizing movement in 2D/3D.

#### Key Decisions:
- Not using hardware to minimize costs.
- Using STFT spectrogram datasets to train CNN and RNN models.

#### Next Steps:
1. Create the UI design prototype.
2. Develop a 3D object-tracking model.
3. Prepare a presentation for the intra-college hackathon.

---

### Week 2: [2 Sep - 8 Sep]

#### Objectives:
1. Create a PowerPoint presentation for the hackathon.
2. Finalize the web app UI design.
3. Create a 3D model prototype for real-time object tracking.
4. Gain clarity on data flow from radar to deep learning models and the web application.

#### Progress:
- Objective 1: Completed – Presentation created using Canva.
- Objective 2: Completed – UI finalized using Figma.
- Objective 3: Completed – 3D model created using ReactJS.

#### Challenges & Solutions:

1. **Challenge:** Finding existing 3D models and rendering them on the web interface.
   
   - **Solution:** Found models online and used React libraries for rendering.

2. **Challenge:** Making the presentation visually appealing while adhering to format.
   
   - **Solution:** Used statistics and a flowchart to enhance the presentation.

#### Key Decisions:
- Created a flowchart to visually represent technical information.
- Showcased the 3D model as an important feature.

#### Next Steps:
1. Find an STFT spectrogram dataset for training.
2. Explore pre-trained deep learning models for accurate classification.

---

### Week 3: [9 Sep - 15 Sep]

#### Objectives:
1. Find datasets of STFT spectrograms for UAV classification.
2. Understand how CNNs analyze STFT spectrogram images.

#### Progress:
- Objective 1: Completed – Found a dataset on GitHub.
- Objective 2: Completed – Researched CNN applications in spectrogram analysis.

#### Challenges & Solutions:

1. **Challenge:** Most datasets were behind paywalls or the other, will require proper dataset containing imagery in the form of STFT spectrograms.
   
   - **Solution:** Found a verified free dataset after extensive searching.

#### Next Steps:
1. Train deep learning models using the dataset.

---

### Week 4: [16 Sep - 22 Sep]

#### Objectives:
1. Implement deep learning using pre-trained models.
2. Train models on the STFT spectrogram dataset.
3. Augment existing data for improved prediction accuracy.

#### Progress:
- Objective 1: Completed – Used VGG models for image recognition.
- Objective 2: Completed – Training done using Python libraries.
- Objective 3: Completed – Applied data augmentation techniques like resizing, flipping, and rotation.

#### Challenges & Solutions:
1. **Challenge:** Building a custom deep learning model from scratch.
   - **Solution:** Used VGG16 and VGG19 models for spectrogram analysis.

2. **Challenge:** Understanding how to pass spectrogram images through CNNs.
   - **Solution:** Used Python libraries to fetch images and train models.

#### Key Decisions:
- Used pre-trained VGG models for high-accuracy image recognition.

#### Next Steps:
1. Upload code to the cloud.
2. Debug and optimize code efficiency.

---

### Week 5: [23 Sep - 29 Sep]

#### Objectives:
1. Obtain real bird micro-Doppler data or generate it synthetically.
2. Optimize the codebase for better performance.

#### Progress:
- Objective 1: In progress – Still searching for datasets.
- Objective 2: In progress – Working on optimizing execution time.

#### Challenges & Solutions:
1. **Challenge:** Slow execution on Google Colab during model training.
   - **Solution:** Yet to be resolved.

2. **Challenge:** Lack of publicly available real bird data.
   - **Solution:** Considering synthetic data generation.

3. **Challenge:** generating synthetic data based on bird flight characteristics, Doppler shifts, and trajectory patterns.]
   - **Solution:** Considering using MATLAB or SciPy to create simulated data for birds’ micro-Doppler signatures based on known characteristics and movement behaviors.

#### Key Decisions:

- Generate synthetic bird data : Since actual bird micro-Doppler data is unavailable, the team will simulate the required data.
- Optimize the code : Prioritize reducing inefficiencies to speed up the execution time during model training.
  
#### Next Steps:

- 1. Complete the synthetic bird data generation using tools like MATLAB or SciPy.
- 2. Optimize model training and execution on platforms like Google Colab.
- 3. Prepare for further testing and integrate the data into the web interface for real-time classification.

#### Notes:

> When working with data that's hard to find, don’t hesitate to generate synthetic datasets based on known patterns and characteristics.
> Always allocate time for optimizing your code, as inefficiencies can significantly slow down processes when working with large datasets.

### Week 6: [30 Sep - 6 Oct]

#### Challenges - objectives - plans

- 1.  The model was being suspiciously accurate. Maybe it's overfit with the data we currently have, or the attributes Resnet50 is considering for classification may not be the most accurate in case of STFT spectrograms.

- 2. An STFT spectrogram of a helicopter drone was fed to the model which it named as bionic bird

- 3. Possibly our dataset’s size can be increased through the generation of synthetic dataset using MATLAB or something. Bigger dataset for our model to be trained on.

- 4. Synthetic data generation for STFT spectrograms of birds will be done in the future.
     
---

## Conclusion:

SkySentinel-X has made significant strides in using deep learning models to classify micro-Doppler signatures from drones and birds. By leveraging CNNs, RNNs, and STFT spectrograms, and integrating them into a responsive web interface, the project aims to enhance airspace security. The focus now is on refining synthetic data, optimizing model performance, and preparing for real-time radar data testing.

## Important Links

- [Link to project repository]
- [Link to design documents]
- [Link to team communication channel]

## Team Member Contributions

[Management_And_Lead]:

    > Aditya Pratap Singh

[Research_And_Development]:

    > Pranay Vohra
    > Aditya Pratap Singh
    > Eish Chandeal

[Design_of_User_interface]:

    > Mohd Arham
    > Aman Sigroha

[DL_and_Ml_work]:

    > Aditya Pratap Singh

[STFT_Data_collection]:

    > Pranay Vohra
    > Aditya Pratap Singh

[Development_of_3d_model]:

    > Aman Sigroha (Our esteemed web developer)

[Creation_of_Presentation]:

    > Aditya Pratap Singh
    > Mohd Arham
    > Eish Chandeal

[Creation_of_synopsis]:

    > Aditya Pratap Singh
    > Pranay Vohra
    > Aman Sigroha
    > Eish Chandeal
    > Mohd Arham

[MVP_behind_the_scenes]

    > Shiven Kashyap

[Inital_Team_Formation]:

    > Aditya Pratap Singh
    > Diya Virmani

## Glossary

- DL : Deep learning
- ML : Machine learning
- STFT : Short time fourier transform
- CNN : convolutional neural networks
- RNN : recurrent neural network
- LSTM : low short term memory
- UAV : Unmanned aerial vehicle
- VGG : visual geometry groups
- REPO : repository
- UI : User interface
- API : application programming interface
- USP : unique selling point
