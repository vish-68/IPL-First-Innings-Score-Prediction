
# IPL First Innings Score Prediction

Now a days as we know that Data Science plays an important role in 
every field. Sports is one of them we use data science for predicting 
the winner or score. In this project I have build Machine Learning 
model for predicting first innings score of Indian Premier League.
I got this dataset from kaggle and data set contains information 
from 2008 to 2017 and information of every delivery is save.
This data is time series data set means we have to split data into
train and test using date column not but "train_test_split".
## Data Analysis

In IPL First Innings Score Prediction dataset we have 15 features(including target 
variable) and 76014 records.

* mid : match id
* date : date of all the matches
* venue : all the statidums where matches were played
* bat_team : batting teams
* bowl_team : bowling teams
* batsman : the one who came to bat
* bowler : the one who come to bowl
* runs : runs in every delivery
* wickets : wickets
* overs : ball by ball 
* runs_last_5 : runs in last 5 overs
* wickets_last_5 : wickets in last 5 overs
* striker : player who is batting
* non-striker : player who is standing on non-striker end
* total : total runs.
## Approach

Our Main goal is to know that whether which check the First Innings Score

* Data Exploration : Exploring dataset using pandas, numpy, matplotlib and seaborn.
* Data visualization :Ploted graphs to get insights about dependend and independed variables.
* Model Selection I : Tested all base models to check the base accuracy. Also ploted and calculate Performance Metrics to check whether a model is a good fit or not.
* Model Selection II : After testing all base if some of them are not working properly then we have to do model tunning. 
* Pickle File : Selected model as per best accuracy and created pickle file using pickle library.
* Webpage & deployment : Created a webform that takes all the necessary inputs from user and shows output. After that I have deployed project on Herokuapp. 

## Technologies Used

* Jupyter notebook, Spyder, VScode Is Used For IDE.
* For Visualization Of The Plots Matplotlib , Seaborn Are Used.
* Herokuapp is Used For Model Deployment.
* Front End Deployment Is Done Using HTML, CSS, Bootstrap.
* Flask is for creating the application server and pages.
* Git Hub Is Used As A Version Control System.
* os is used for creating and deleting folders.
* csv is used for creating .csv format file.
* numpy is for arrays computations and mathematical operations
* pandas is for Manipulation and wrangling structured data
* scikit-learn is used for machine learning tool kit
* pickle is used for saving model
* Linear is used for LinearRegression Implementation.
* Ridge is used for RidgeRegression Implementation.
* Lasso is used for LassoRegression Implementation.
* SGD is used for SGDRegressor Implementation.
* K-Nearest Neighbors is used for KNNRegressor Implementation.
* SVM is used for SVR Implementation.
* Decision Tree is used for KNeighborsRegressor Implementation.
* Extra Trees is used for ExtraTreesRegressor Implementation.
* Random forest is used for RandomForestRegressor Implementation.
* Ada boost is used for AdaBoostRegressor Implementation.
* Gradient is used for GradientBoostingRegressor Implementation.
* XGboost is used for XGBRegressor Implementation
* Ensemble is used for VotingRegressor Implementation.
## Deployment

**Herokuapp Link:** https://ipl-1st-innings-score-predict.herokuapp.com/
  
## Deployment

To Clone this project run

```bash
git clone https://github.com/vish-68/IPL-First-Innings-Score-Prediction
```
Go to Project directory
```bash
cd IPL-First-Innings-Score-Prediction
```
Install dependencies
``` bash
pip install -r requirements.txt
```  
Run the app.py
```bash
python app.py
```
## Conclusion

We developed IPL First Innings score model which is capable to predict
the score of first innings. In this dataset 15 features(including 
target variable). 
* Our 1st step is to import dataset and check all
  the details like shape, info(), describe() for getting better knowledge
  about data or each variable.
* 2nd step is to checking missing value and datatype of missing variable
  by looking at info(). after that we have to delete those 
  variable whose missing value is more than 50% of data. Other 
  variable should be treat as repect to their datatype. Here we deleted those
  rows who has less than 5 overs and kept those batting and bowling teams who 
  played for all the seasons
* 3rd step After handling all this we have to do data 
  visualization for getting some insight for eg. we have to check 
  for ouliers, imbalanced variable or imbalanced data so we have to 
  remove ouliers or do upsampling for those.
* 4th step we have group all the same kinds of cloud condition in one groups
* 5th step converting all categorical variable into numerical eg venue, bat_team, bowl_team.
* 6th step Splitting data into training and validation data and building 
  different ML model like LinearRegression, Ridge, Lasso, statsmodels, SGDRegressor, 
  KNeighborsRegressor, SVR, DecisionTreeRegressor, ExtraTreesRegressor, 
  RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor, 
  VotingRegressor, XGBRegressor. Out of all VotingRegressor is working 
  properly.
* Last step is model Deployment using Flask Framework.
  For model deployment we have to dump our model using pickle library
  and can save our model in .pkl or .sav extension.
