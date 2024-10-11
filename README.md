# SkySentinel-X
Micro-Doppler Target Classification system for the Smart India Hackathon (SIH). Using spectrograms generated from STFT on FMCW radar data, the system employs deep learning models to classify drones and birds by their micro-Doppler signatures. A web interface will display real-time monitoring and detection for enhanced airspace security.

-------------- Development Log -------------------------

# Skysentinel-X Development Log

## Project Overview

- Start Date: [23 Sep]

- Team Members:

> Aditya Pratap Singh
> Mohd Arham
> Aman Sigroha
> Pranay Vohra
> Eish Chandeal
> Diya Virmani 

- Project Goals:

The goal is to create a software for the identification of Flying Objects based on their micro doppler signatures , and determining whether it is actually an UAV (Unmanned Aerial vehicle) or a bird.

The software will be in the form of a web application where information regarding the flying object will be displayed, which will include its binary classification and additional features such as Velocity, Co-ordinates and visually showcasing their movement patterns in 2d and 3d formats.

We will need to include a combination of CNN and RNN models in our application which will be its core thing. Through these models we will be really able to analyze those micro signatures, see shifts in its characteristics and get output as a result of it.

## Weekly Log

### Week 1: [26 Aug - 1 Sep]

#### Objectives:

- 1: [Understanding the Problem statement properly. Studying various research papers regarding how micro doppler signatures are analyzed and objects identified through their use, the principles radar system's work on.]

- 2: [Figuring out how will implementation of such a system will look like, What sort of machine learning models would be required for providing most accurate classificaton of the flying object.]

- 3: [Understanding the tech stacks that would be necessary for the project, and how will those technologies interact with each other for our software application to function properly and work with data received in real time through radar systems]

- 4: [Designing a good looking UI which we will require during our presentation]

- 5: Creating a proper synopsis that will need to be submitted in its due time, synopsis will include the basic information regarding the project and tech stack that will be required for its implementation

#### Progress:

- [Objective 1]:

  [completed, Went through multiple research papers on the subject and maintained a google doc where each members research work was being stored]

- [Objective 2]:

  [completed, through extensive research and found out will need CNN's and RNN's ]

- [Objectve 3]:

  [completed, concluded that we will create a web based product , and web technologies will work together with Machine learning and deep learning models]

- [Objectve 4]:

  [completed, The design was created through the use of a tool called FIGMA]

- [Objectve 5]:

  [completed, Synopsis was created and submitted with concise info]

#### Challenges & Solutions:

1.  Challenge:

[Overall application, what sort of technologies will need to be integrated , and how will the signals will even get processed? ]

    Solution:

[The signal will be processed into STFT spectrograms to analyze subtle changes in the micro-Doppler signatures of flying targets.

In our project, CNNs will be used for object identification and classification, while RNNs will handle object tracking, determining its precise location, and visually representing its movement in 2D and 3D on our web application.

These technologies will work in tandem through integrated pipelines and API endpoints to ensure seamless functionality.]

#### Key Decisions:

- [Not using hardware]: [Minimizing expenses and sticking to our theme of software]
- [STFT spectrograms datasets]: [What will essentially be used for train CNN's and RNN's]

#### Next Steps:

- 1. [Creation of design, because that's what will be shown as a prototype of basically the UI of our final product, the way it would look like. The way information related to the object will get displayed]

- 2. [3d model which is kind of the USP of our product for object tracking, we need a basic prototype for that as well]

- 3. [Creation of ppt that we will need on our day 2 of intra college hackathon]

#### Notes:

Essential learnings from the week:

> Focus on the technical details more rather than the physics part itself. Because we are not like physicists rather developers, we focus more on how implementation would look rather than theory.

> When digging through research papers, make sure to have clarity on the specificity of topics you are looking for and essential things you must learn.

> When found a research paper or resource make sure to look into it properly and don’t just juggle around multiple things. Note down the essential points somewhere in a document.

> If you are short on time , or have not figured out some important things. It's better to keep the meetings short and to the point. Allocate tasks clearly to each member. So that people aren’t working unproductively on the same things as eachother

> When working on your project try to look for similar projects that may have been worked on by others. My come across a gitHub repository.

---

### Week 2: [2 SEP - 8 SEP]

#### Objectives:

- 1: [Creation of power point presentation for intra college hackathon rounds]

- 2: [Finalising the design for our web application's UI ]

- 3: [Creating prototype of our 3d model which will update in real time and will be displayed on our web interface.]

- 4: [Gaining clarity and understanding the entire technical process properly. How data is being given to the deep learning model(CNN's and RNN's), and how than information from that analysis is transferred and interpreted by our webapplication. How the data is stored and displayed.]

#### Progress:

- [Objective 1]: [Completed, through the Use of Canva]
- [Objective 2]: [Completed, through the use of figma]
- [Objective 3]: [Completed, through reactJs and its respective libraries]

#### Challenges & Solutions:

1.  Challenge:

[Finding already existing 3d models of Drone present online and rendering that 3d model with its proper environment onto the interface]

    Solution:

[3d models were found online and for rendering it a few react libraries were used and node packages were installed]

2.  Challenge:

[Following the presentations format, and following it also making the presentation more visually appealing. Including necessary statistics based on the usage of drones and accidents, mishaps that took place through the use of such UAV's]

    Solution:

[Found the required statistics through a webpage referencing several research papers. Made the presentation more visually appealing by creating flow chart of the entire technical process and including various images.]

#### Key Decisions:

- [Creation_of_flowChart]: [for representing information visually in concise manner]
- [Showcasing the 3D model]: [Essential as it was an important feature our web app]

#### Next Steps:

- 1. [Finding dataset of STFT spectrograms for different kinds of UAV's and flying objects in order to train our DL model from a vast pool of data. For accurate analysis and prediction]

- 2. [Figuring out ways to develop our own custom model or find pretrained deep learning CNN models online for analysis and accurate insights as results]

#### Notes:

> Prepare for the screening beforehand, make sure to keep it short , directly tell what's the problem and the possible solutions to it. Jump into the technical stuff rather than spending more time explaining the theoretical portion

> Make sure that your teammates have clarity regarding the segment they are supposed to present in front of the judges. Do mock presentations beforehand, ask each other questions and test everyone’s understanding.

> Like for example , for this project how the application will be connected to the hardware, how will the data be transferred from the radar to the ML model and from there onto the web interface. Be thorough with the technical details and technologies that will be involved.

> Prepare things before the end moment arrives, so that you have time left to review what you have created.

---

### Week 3: [9 SEP - 15 SEP]

#### Objective:

- 1: [Finding data of STFT spectrograms for Various kinds of UAV's for training our model]

- 2: [Understanding how CNN models will be able to analyze this image data in the form of STFT spectrograms ]

#### Progress:

- [Objective 1]: [Completed, Found a github repo with dataset from verified sources]
- [Objective 2]: [Completed, Through extensive research on this topic]

#### Challenges & Solutions:

1.  Challenge:

[All the datasets seem to present behind one paywall or the other, will require proper dataset containing imagery in the form of STFT spectrograms]

    Solution:

[Solved through a lot of searching and digging through multiple sources online and finally found it.]

#### Next Steps:

- 1. [Figuring out how to train our DL and ML model on this vast dataset of STFT spectrograms imagery, and where to even find such pretrained models to begin with ]

#### Notes:

[Any additional observations, learnings, or comments]

> Don't download any random app that your teammate tells you to.

---

### Week 4: [16 SEP - 22 SEP]

#### Objectives:

- 1: [ Figuring out and creating machine learning and deep learning part, using pretrained existing models]

- 2: [ Training those models on the dataset of STFT spectrograms, and getting accurate results.]

- 3: [Augmentation of already existing data, to feed the DL model data in higher amounts for it to give more accurate predictions.]

#### Progress:

- [Objective 1]: [Completed, Use of VGG models for image recognition and analysis.]
- [Objective 2]: [Completed, Through the use of numerous python libraries
  (tensorflow, pytorch etc.)]
- [Objective 3]: [Completed, data augmentation is applied using many trasformations on the STFT imagery(Resize, flip, rotation, color jitter)]

#### Challenges & Solutions:

1.  Challenge:

[Creating a deep learning architecture by ourselves is way too big of task, better find some already existing models for analysis of our STFT datasets]

    Solution:

[Found models such as VGG 16 and VGG 19 models which are trained on a large dataset of images from the ImageNet database, will be used for tasks related to analysis and identifying essential features from images ]

2. Challenge:

[How do you render and use such CNN models. How would passing such images through these models even work]

    Solution:

[This was solved by use various libraries provided by python for fetching images from a particular location, and rendering + training of such Deep learning models.]

#### Key Decisions:

- [use of VGG16 and 19]:

  [pretrained and highly accurate image recogniton models, trained over a vast dataset]

#### Next Steps:

- 1. [ Uploading the code and keeping it on cloud. ]

- 2. [ Understanding and debugging the code whilst reducing inefficiencies]

- 3. [ Missing data on micro doppler signatures of real birds online, need to find it.]

#### Notes:

[Any additional observations, learnings, or comments]

---

### Week 5: [23 SEP - 29 SEP]

#### Objectives:

- 1: [ Getting data on real bird’s micro doppler signatures or generating it synthetically using MatLab or other python libraries such as SciPy]

- 2: [ Understanding the overall codebase and ways to make it more efficient]

#### Progress:

- [Objective 1]:

  [In Search of, Still looking online for synthetically generated data ]

- [Objective 2]:

  [In progress, understanding the code base and reducing its execution time]

#### Challenges & Solutions:

1.  Challenge:

[the Code's execution is pretty slow on google COLAB, the model training part where the algorithm goes through the dataset and model receives training and gives out its results related to accuracy and validation]

    Solution:

[Yet to resolved]

2. Challenge:

[The real bird data seems to be pretty confidential, datasets aren't really availiable out there for them. So the next option seems to be look for synthetically generated data of real bird's micro doppler signatures OR creating them ourselve's which will take quite some time to say the least]

    Solution:

[yet to be resolved.]

#### Key Decisions:

- [Moving to google COLAB]:

  [To utilize cloud resources instead of running everything on local machine, enabling easy sharing of codebase]

- [Search for synthetic data or its creation]:

  [Real data is pretty scarce or just confidential. Creating our own using Matlab and python libraries Or can look for it online]

#### Next Steps:

- 1. [ Feeding data to the CNN model in real time in form of STFT spectrograms and getting an output. Including its binary classification and characteristics ]

- 2. [ LSTM (RNN) models, where to get already existing ones, how to use them and integrate them to our application (In order to tell the UAV’s co-ordinates, velocity and overall, just movement patterns)]

- 3. [ Real-time processing: Implement a sliding window approach on your incoming radar data , Process each new window through your CNN for classification , Update your LSTM with new data to predict movement and location ,Use multi-threading or asynchronous processing to handle real-time data flow ]

- 4. [ Real time changes in 3D and 2D models present on web interface based off of information gained from these RNN’s and CNN’s. Will have to look into creation of piplines in the form API end points or whatever is necessary to transfer result data after analysis from the model to the web interface.]

- 5. [Signal Processing setup using Python libraries, for signals received in real time through the radar and their conversion to STFT spectrograms that will then be FED to our deep learning models]

#### Notes:

[Any additional observations, learnings, or comments]

---

### Week 6: [30 Sep - 6 Oct]

#### Challenges - objectives - plans

- 1.  The model was being suspiciously accurate. Maybe it's overfit with the data we currently have, or the attributes Resnet50 is considering for classification may not be the most accurate in case of STFT spectrograms.

- 2. An STFT spectrogram of a helicopter drone was fed to the model which it named as bionic bird

- 3. Possibly our dataset’s size can be increased through the generation of synthetic dataset using MATLAB or something. Bigger dataset for our model to be trained on.

- 4. Synthetic data generation for STFT spectrograms of birds will be done in the future.

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

DL : Deep learning
ML : Machine learning
STFT : Short time fourier transform
CNN : convolutional neural networks
RNN : recurrent neural network
LSTM : low short term memory
UAV : Unmanned aerial vehicle
VGG : visual geometry groups
REPO : repository
UI : User interface
API : application programming interface
USP : unique selling point
