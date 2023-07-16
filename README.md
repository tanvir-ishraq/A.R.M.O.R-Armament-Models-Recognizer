
# Project A.R.M.O.R Introduction
<p align="center"> A.R.M.O.R - <strong>Ar<strong>mament **Mo**dels **R**ecognizer for civilian security. </p> <br/> 
A comprehensive image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model was developed as a security measure that can classify comprehensive 22 different types of most common military armaments posing threat for civilians on land. Civilian security. <br/>
The armament types are following: <br/>
1.  2S19 Msta artillery
2.  BM-21 Grad artillery
3.  G6 Rhino artillery
4.  M109 artillery
5.  M270 MLRS artillery
6.  Smerch artillery
7.  BMP-2 vehicle
8.  BTR-80 vehicle
9.  Humvee vehicle
10. LAV-25 vehicle
11. M113 vehicle
12. MRAP vehicle
13. Leopard 2 tank
14. M1 Abrams tank
15. T-72 tank
16. Type 99 tank
17. Bayraktar TB2 UCAV drone
18. CH-5 Rainbow UCAV drone
19. Hermes 900 drone
20. Heron TP drone
21. MQ-9 Reaper UCAV drone
22. RQ-4 Global Hawk UCAV drone

# Dataset Preparation
**Research:** Existing military datasets are insufficient for civilian security. We aim to update them for our modern goals. I did research on which categories poses most threat to civilians being on land. Did deep research on most common armaments on each categories. researched most produced available armaments in modern times. researched most used in military operation and wars in modern times. researched most used armaments. <br/><br/>
**Data Collection:** Downloaded from DuckDuckGo using term name. A grand total of ~5500 images finally consisted our dataset after deeply cleaning dataset. (with more data and categories to be added more later project version) <br/><br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. Proper dataset split percentage was followed. Proper batch_size was set to utilize power of GPU. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `data augmentation` section in `notebooks/ARMOR_classfier_full_process.ipynb`

# Training and Data Cleaning
**Training overview:** The powerful resnet152 model was chosen as starting point. Fine-tuned a resnet152 model for 20 epochs and achieved upto ~96% accuracy. During this 20 epochs period, I obeserved train loss and validation loss with attention to ensure overfit doesn't occur. <br/> <br/>
**Data Cleaning:** This was the most time-consuming part. I dealt with a lot of noisy data/miscategorization from the browser fetched images. There were also images that interfered. And some images were contaminated. First I did an universal cleaning manually. Then I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment
I deployed the model to HuggingFace Spaces Gradio App. The implementation can be found in `hf_deployment` folder and [online here](https://huggingface.co/spaces/tanvir-ishraq/ARMOR-Armament-Models-Recognizer). <br/>
<img src = "hf_deployment/ARMOR_gradio_app.png" width="780" height="350">

# API integration with GitHub Pages
The deployed model API is integrated [here](https://tanvir-ishraq.github.io/A.R.M.O.R-Armament-Models-Recognizer/) in GitHub Pages Website. Deployement implementation and other details can be found in `docs` folder.
