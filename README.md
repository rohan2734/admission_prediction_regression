# admission_prediction_regression

## Dataset and its Analysis 
1. This project predicts the chances of your admission by taking the following inputs : GRE , TOEFL score , University Rating , SOP  score  , LOR Score , Research - Yes/ No  
2. I found this [dataset](https://www.kaggle.com/datasets/gurbanovafatima/admission-prediction) on Kaggle. 
3. I used the following Regression Algorithms : Linear Regression , Lasso , Ridge , Elastic Net
4. The accuracy of the model is 80%

## Building model 
5. I have followed the steps of 
  1. preprocessing (removing null values)
  2. Feature selection (dropped Serial numbers)
  3. Analysed the dataset using EDA and profile Reports from pandas 
  4. I found that there are large variances in dataset ,and this is a problem, since it would be hard to build a relationship between Features and Labels 
  5. So using Standard Scaler , I have solved the problem.
  6. I split the features and labels
  7. I have used fit_transform on X_train,y_train and fitted on the model and calculated the score of it
  8. for prediction I used transform on X_test. and calculated the score using X_test,y_test
  9. I have followed the same steps with Lasso,Ridge,Elastic Net
 
## Building API
6. Linear Regression , Lasso , Ridge , Elastic were giving the same accuracy of 80% 
7. After chosing the perfect model  , I have converted the model to pickle file using pickle library
8. I built Flask API , wrote html files using css and connected the html and API for getting the inputs and predicting the outputs respectively
9. I also saved the scaler object as a pickle file, so that I can transform the input from the user and pass it to the model and get the predictions in the right way.

## Deployment on Azure 
10. I have deployed the [Admission prediciton regression](https://admission-prediction-regression-rohandevaki.azurewebsites.net) , (my second ML project ) on Azure  successfully, 
11. I have faced issues in selecting the regions, figured out that default region is best
12. I have facied issues in building the model, forgot to build requirements.txt , added it, and solved the issues of migrating the workflow file from node12 to node16.
13. After the build process, Deployment was successful.
14. Tada!! now you can also use my [Admission prediciton regression](https://admission-prediction-regression-rohandevaki.azurewebsites.net) and predict your chances of getting admitted to your college by giving the required inputs
15. If you have any suggestions , please let me know . 

16. If you have any opportunities for me, please check my github read me page [rohan2734](https://github.com/rohan2734) .
17. you can reach out to me via mail or [Linkedin](https://www.linkedin.com/in/rohandevaki/)

## Demonstration of the Project 

