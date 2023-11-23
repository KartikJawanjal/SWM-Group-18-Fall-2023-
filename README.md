# SWM-Group-18-Fall-2023-Directional Stock Prediction using Viral Tweets & News

### This is a project built as a requirement for the course CSE 573 Semantic Web Mining at Arizona State University.

### This project focuses on harnessing the power of viral tweets and news data to accurately predict stock prices for two prominent technology companies, Amazon and Apple. We employ natural language processing (NLP) techniques and machine learning algorithms to extract valuable insights from social media and news sources. The project presents the methodology and techniques used to achieve this goal and evaluate the predictive performance of our models.

### CODE
1. ``` trainer.py ``` contains the train helper function for the BERT.
2. ``` summary.py ``` contains the code to summarize the text.
3. ``` plot.py ``` contains code to get plots for BERT (updated plots)
4. ``` model.py ``` contains the code for defining the model architecture
5. ``` inference.py ``` contains the code for running the inference engine for BERT
6. ``` main.py ``` contains the base code for BERT
7. ``` helper.py ``` contains the code to perform data pre-processing and tokenization for logistic regression
8. ``` daily_data_preprocess.ipynb ``` contains code to get the daily data after performing data cleaning
9. ``` bert_preprocess.py ``` contains code to pre-process the text for BERT
10. ``` SVM-Final.ipynb ``` contains code to apply SVM on the dataset
11. ``` Preprocess_Amazon.py ``` contains code to get labels for Amazon data based on stock charts
12. ``` Preprocess_Apple.py ``` contains code to get labels for Apple data based on stock charts
13. ``` Logistic Regression(**).ipynb ``` contains code to perform Logistic regression for various data: Amazon daily, Amazon hourly, Apple Daily , Apple hourly
14. ``` Data Extraction and Preprocess.ipynb ``` 

Steps to run BERT: 
1. Head to the CODE directory and open the file main.py
2. To run the main.py file use the command ``` python main.py --data_dir <dataset-dir> --model <model_name> --token_len <token_length> --folds <K_fold>```
   
### DATA

This folder contains the "dataset.txt" file. The file includes the link to the dataset on Google Drive, and access is restricted. To obtain permission to access the dataset, please request it, and the owner will grant it as soon as possible.

### EVALUATION
This folder contains the results after performing K-fold cross-validation on BERT and other classical methods. The graphs in this folder are for the best-performing fold and the image with a tabular column for classical methods is the averaged values of the respective metric over all folds.  


