# HR_Analytics

problem statement of my project:I have a data of company named abc.in that company every year around 15% of its employees leave the company.
so I have to analyze why its happening what is the reason behind it.

So for this project I got 4 csv files containing different data of employees.
the challenging part is to understand the data and cleaning the data because data needs so much cleaning.so I imported all the files and done EDA and concatenate all files.
After this the next step is to do VDA and analyze the distribution of data checking multicollinearity between independed features and we dont need unnecessary features so we selected best features.
Our data has categorical values but we cannot pass categorical values to our model so i done one hot encoding then for training and testing we split data with test size of 25%.
then we standardize the features that needed to be standardize so for model building we choose the classification model that gives highest accuracy so decision tree gives me the highest accuracy so i choosed decision tree.
Decision Trees use Gini Index or Entropy to find out how pure a node is(purity). so i Define a function to calculate gini index then i done cross validation to avoid overfitting.
after this I perform some hyperparameter tuning like grid search to improve the accuracy we get accuracy of 80% which is good enough. then plotted roc curve.
Then i loaded the model and made web application using streamlit and deployed it on heroku.

application link : https://sahil1932001-hr-analytics-app-wuabge.streamlit.app/

