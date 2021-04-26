### 0. Abstract



### 1. Introduction (answer what is the real world problem and why it is important)
The purpose of linear regression is to predict the trend, find the law, or find a suitable expression for the data to express a certain trend. In this experiment, we used linear regression to analyze the relationship between the individual insurance costs and the individual's own conditions. We believe that our forecast has a certain impact on policyholders, insurance companies, and social development. 

**For policyholders**: When choosing insurance, this data result helps policyholders to choose the optimal insurance that suits them based on their personal conditions. At the same time, the causality shown by this prediction will also invisibly prompt individuals to pay attention to physical health issues. The results of our forecasts will also help people buy insurance against unpredictable risks in advance and share the risk for the unpredictable future. 

**For insurance companies**: Insurance companies need to receive feedback from society from time to time. By analyzing this information, the insurance companies can keep a balance between the risk and the cost, so as to achieve the maximum benefit; The establishment of decision data model is helpful for enterprises to analyze customer risk level and avoid fraud claim; Data mining can help insurance companies fully explore the value of customers. To be more specific, potential customers may convert them into real customers by using clustering; what’s more, data mining can be applied to customer churn waring analysis for retaining those existing customers. [1]

**For society**: The results of this prediction can be used as a basis for people to purchase insurance to a certain extent. When choosing insurance, this forecast can be used as a reference for policyholders to a certain extent. This forecast can effectively avoid the unhealthy trend of blindly setting insurance premiums in the insurance market. In addition, our research will also increase people's attention to insurance. 

Mining medical insurance data is an effective way to observe the long-term treatment and recovery of diseases. Raedel Michael Through the digital database of a large national insurance company in Germany, this paper tracks the experimental effect of re intervention of restorative treatment of permanent teeth. He also put forward improvement measures from the perspective of public health and the need of optimized strategies [2]. It can be seen that data mining also has great application prospects in disease research and nursing, which should be taken into consideration by the government.

In conclusion, our optimism about the prospects of data mining applications in the insurance industry, coupled with the importance of medical data obtained from insurance policies, constitute the reasons why we chose this direction as our subject.

### 2. Dataset selection(collection) and Data pre-processing

#### 2.1 Where you find your data (or how do you collect the data and create your dataset)?
Since we want to practice some linear regression algorithms, we found the data set at [kaggle](https://www.kaggle.com/mirichoi0218/insurance) by searching linear regression related topics. 
#### 2.2 How do you analyze your data?
Our data set has seven columns:
- age: age of primary beneficiary
- sex: insurance contractor gender, female, male
- bmi: Body mass index, providing an understanding of body, weights that are relatively high or low relative to height,
objective index of body weight (kg / m ^ 2) using the ratio of height to weight, ideally 18.5 to 24.9
- children: Number of children covered by health insurance / Number of dependents
- smoker: Smoking
- region: the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.
- charges: Individual medical costs billed by health insurance

According to common sense it is easy to know that:
- age: 
  - With age, the possibility of getting sick also increases. 
  - The incidence of different diseases varies at different ages.  
  - Therefore, even if people of different ages insured the same product, the premiums payable are different.  
  - **Forecast: within a certain range, the younger you are, the cheaper your insurance premium will be.**    
- sex: Men and women face different risks.
  - The life span of men is generally lower than that of women.
  - Men are more likely to get cancer than women, and the mortality rate is higher than that of women.   
  - There are differences in lifestyles between men and women: Generally speaking, men have more bad habits than women, such as smoking and drinking. Moreover, Men were also less aware of their own health and less likely to go to hospital.
  - Men’s social pressure is greater: in China's family economy at present, there are still more male-dominated families. Men face greater economic pressure and more intense social competition.  
  - **Prediction: In the case of critical illness insurance and life insurance, in most cases men pay more than women; In the case of accident and medical insurance, there is generally no gender difference in premiums.**
- bmi: 
  - The health condition of the insured will affect the premium paid.
  - The insurance company will assess the risk based on the insured’s physical condition. If there is a relevant medical history or the physical condition is poor, the health notification may not be available, and additional fees are required for underwriting, and the premium will be higher, of course.  
**Prediction: We guess that the premium paid by Bmi between 18-24 will be cheaper, because the calculated value within this range is recognized as healthy and normal.**    
- smoker: 
  - Smoking can cause lung cancer, and 90% of the total mortality is caused by smoking. Smoking can also cause blood clots, and it can trigger all kinds of heart disease. Therefore, the mortality rate of these smokers will also increase, and additional premiums are usually required.
  - **Forecast: For people who smoke, their premiums will be higher**
- region:
  - Various environmental factors such as different living habits, behavioral habits, and different climates in the place can affect the individual's physical condition. For example, high salt and cold can lead to high blood pressure, and there are more people with high blood pressure in colder regions; in addition, the difference in diet between North and South is relatively large, and fine grains and large meat will bring obesity, so there are more obese patients in some areas.
- children:
  - The cost of raising multiple children is relatively high. The pressure on parents is greater，when there are more children. Compared to parents with fewer children, parents with many children are more anxious and will have some physical problems. In addition, families with more children put their parents' retirement at greater risk. Therefore, for policyholders with more children, their insurance premiums will increase accordingly.
  - **Prediction: For policyholders, when they have more children, their insurance premiums will be higher when other factors are the same.**  

Therefore, it is reasonable to infer that the charges for an insurance is calculated based on the health condition and the lifestyle of the insured person, 
in other words, the first six columns namely age, sex, bmi, number of children, smoke or not, and region should be the independent variable, 
while the charges should be the dependent variable. 
Thus, we come up with the idea that a multivariate function could be used to fit their relationship, 
so that we can predict the insurance cost based on the six main feature of a person. 
#### 2.3 how to pre-process your data to fit your solution?
##### 2.3.0 Data
The following is the head of our raw data
```
   age     sex     bmi  children smoker     region      charges
0   19  female  27.900         0    yes  southwest  16884.92400
1   18    male  33.770         1     no  southeast   1725.55230
2   28    male  33.000         3     no  southeast   4449.46200
3   33    male  22.705         0     no  northwest  21984.47061
4   32    male  28.880         0     no  northwest   3866.85520
```

##### 2.3.1 Data Cleaning
Firstly we need to see how many invalid entries are there in each column. 
[pandas.DataFrame.isnull](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.isnull.html) is helpful for this calculation. 
The result is shown like this:
```
age         0
sex         0
bmi         0
children    0
smoker      0
region      0
charges     0
dtype: int64
```
There is no invalid entry in this data set so this stage could be omitted. 

##### 2.3.2 Encoding
The following is information of the data frame
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64
dtypes: float64(2), int64(2), object(3)
memory usage: 73.3+ KB
```
From this table we can see that age, children, and charge are numerical features, 
while sex, smoker, and region are categorical features. 
In order to analyse them and fit them into a linear regression model,
it is necessary to preform some kind of encoding to convert the categorical features to numeric features. 
For smoker and sex, since they are binary attribute, we directly encode yes/no or male/female to 1/0. 
For region, since it has four different categories, we implement one-hot-encoding to convert it to four binary attributes, 
namely southwest, southeast, northwest, northeast. 

After the encoding, the head of the dataframe is shown as this:
```
   age     bmi  children      charges  is_smoker  is_male  southwest  \
0   19  27.900         0  16884.92400          1        0          1   
1   18  33.770         1   1725.55230          0        1          0   
2   28  33.000         3   4449.46200          0        1          0   
3   33  22.705         0  21984.47061          0        1          0   
4   32  28.880         0   3866.85520          0        1          0   

   southeast  northwest  northeast  
0          0          0          0  
1          1          0          0  
2          1          0          0  
3          0          1          0  
4          0          1          0  
```
And the information of the data set is shown as following:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 10 columns):
 #   Column     Non-Null Count  Dtype  
---  ------     --------------  -----  
 0   age        1338 non-null   int64  
 1   bmi        1338 non-null   float64
 2   children   1338 non-null   int64  
 3   charges    1338 non-null   float64
 4   is_smoker  1338 non-null   int64  
 5   is_male    1338 non-null   int64  
 6   southwest  1338 non-null   int64  
 7   southeast  1338 non-null   int64  
 8   northwest  1338 non-null   int64  
 9   northeast  1338 non-null   int64  
dtypes: float64(2), int64(8)
memory usage: 104.7 KB
```
Since all the features are numeric now, we can go on to the next stage. 

##### 2.3.3 Data Observation
###### 2.3.3.1 Distribution
In order to get an overview of the dataset, 
we plot the distributions of the variables firstly. 

![variable distribution overview](images/variables_distribution_overview.png)

It is shown that 
- age is almost uniformly distributed except the range before 20, 
- bim obeys normal distribution, 
- the number of children and the charge seems to be in exponential distributions, 
- male and female take up nearly half of the sample respectively, 
- about one out of four are smoker, 
- the portion of people leaving in southwest, southeast, northwest, and northeast have no significant difference, almost evenly distributed. 

###### 2.3.3.2 Correlations
There are 10 independent variables in our data set after the one hot encoding. 
Some of them may have a strong relationship with the insurance cost, while some of them may not. 
To figure out which variables have the most significant contribution, we could use [pandas.DataFrame.corr](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html)
to calculate correlation between the independent variables and the dependant variable. The result is shown as following: 
```
age          0.299008
bmi          0.198341
children     0.067998
charges      1.000000
is_smoker    0.787251
is_male      0.057292
southwest   -0.043210
southeast    0.073982
northwest   -0.039905
northeast    0.006349
Name: charges, dtype: float64
```
It is shown that is_smoker, age and bmi are the most significant terms. 
Let's plot some figures to show visualize their relationship with charge. 

![charge versus is_smoker](images/charge_versus_smoke.png)

![charge versus age](images/charge_versus_age.png)

![charge versus bmi](images/charge_versus_bmi.png)

And we could also plot the scatter matrix to visualize the relationship between every pair of variables. 

![scatter matrix](images/scatter_matrix.png)

##### 2.3.4 Feature Scaling
Since we have seen that in the previous plot there are no outliers in this data set, 
so we choose the min-max scaling method for feature scaling.

$$
scaled = \frac{unscaled - min}{max-min}
$$


After scaling, the head of the data set is shown as following:
```
   is_smoker  is_male  southwest  southeast  northwest  northeast       age  \
0          1        0          1          0          0          0  0.021739   
1          0        1          0          1          0          0  0.000000   
2          0        1          0          1          0          0  0.217391   
3          0        1          0          0          1          0  0.326087   
4          0        1          0          0          1          0  0.304348   

        bmi  children   charges  
0  0.321227       0.0  0.251611  
1  0.479150       0.2  0.009636  
2  0.458434       0.6  0.053115  
3  0.181464       0.0  0.333010  
4  0.347592       0.0  0.043816  
```
We can see that now all the attributes are ranged from 0-1, 
which makes it easy for the linear regression algorithm to converge. 


Since we also record the minimum and maximum value for the original data set, 
it is easy to reverse this process or test new data
```
{'age': {'min': 18, 'max': 64},
 'bmi': {'min': 15.96, 'max': 53.13},
 'children': {'min': 0, 'max': 5},
 'charges': {'min': 1121.8739, 'max': 63770.42801}}
```

#### 2.4 Any challenges with your dataset?
Nothing challenging currently


### 3. Methodologies 
> Any machine learning algorithm can be used (not limited to the algorithm we have learned).
Creativity is encouraged.
Be careful, a sophisticated approach with little description and explanation will receive little credit.

#### 3.1 One-Degree Multiple Variables Batch Gradient Descent (GD)
We select the column charges as Y, and the remaining columns joined with a column of 1s as X. 
```
X.shape: (1338, 10)
Y.shape: (1338, 1)
```
We refer the gradient decent algorithm introduced in lab2 to finish the linear regression, and the formulas to calculate the gradient is shown as follow: 
$$
h(\theta)\text{ is the multiple variable function}
$$

$$
h_{\theta_0, \theta_1, \cdots, \theta_j} = \theta_0 x_0+\theta_1 x_1+\theta_2 x_2+\cdots+\theta_j x_j
$$

$$
\theta = 
\begin{bmatrix}
\theta_0\\\theta_1\\\vdots\\\theta_j
\end{bmatrix},
x = 
\begin{bmatrix}
x_0\\x_1\\\vdots\\x_j
\end{bmatrix}
$$

$$
h_\theta = \theta^{T}x
$$

$$
J(\theta)\text{ is the cost function}
$$

$$
J(\theta) = \frac{1}{m}\sum_{i=1}^{m}(\theta^Tx^{(i)}-y^{(i)})^2
$$

$$
\text{let } t = \theta_0 x_0^{(i)}+\theta_1 x_1^{(i)}+\cdots+\theta_j x_j^{(i)}-y^{(i)}
$$

$$
\text{then, }J(\theta) = \frac{1}{m}\sum_{i=1}^{m}t^2,
$$

$$
\frac{\partial J}{\partial \theta_j} = \frac{\partial J}{\partial t}\frac{\partial t}{\partial\theta_j} = \frac{1}{m}\sum_{i=1}^{m}2tx_j^{(i)}
$$





The initial theta vectors are set to all zeros since we assume that we have no knowledge about 
the contribution of each attribute at the very beginning. 

To get the most suitable argument for learning rate and number of iteration, 
we come up with an idea that we plot the loss against the number of iteration. 

Here is the figure when the learning rate is set to 0.02 and number of iteration is set to 500. 

![](images/degree_1_lr_002_ni_500.png)

It is shown that the loss descended swiftly at the beginning since the gradient was large, 
and converged slowly afterwards since the gradient became small. 

If the learning rate or number of iteration are too small, it may not be totally converged after the training, 
like this figure shows when the learning rate is set to 0.01 and the number of iteration is set to 100:

![](images/degree_1_lr_001_ni_100.png)

However, if the learning rate is too high, the regression may never converge, 
like this figure shows when the learning rate is set to 0.5 and the number of iteration is set to 20:

![](images/degree_1_lr_05_20.png)

The final result of the one-degree gradient descent model is that 
the minimum loss is about 0.0093, 
and the corresponding theta vector is
```python
[[-0.04155146] 
 [ 0.38043647] # is_smoker
 [-0.00207574] # is_male
 [-0.01633501] # southwest
 [-0.01636002] # southeast
 [-0.00723836] # northwest
 [-0.00161808] # northeast
 [ 0.18908899] # age
 [ 0.18676482] # bmi
 [ 0.03755355]]# children
```
We can compare it with the correlation coefficient calculated previously 

attribute | correlation coefficient | final theta vector
----------|-------------------------|-------------------
ones      |                         |-0.04155146
is_smoker | 0.787251                | 0.38043647
is_male   | 0.057292                | 0.00207574
southwest |-0.043210                |-0.01633501
southeast | 0.073982                |-0.01636002
northwest |-0.039905                |-0.00723836
northeast | 0.006349                |-0.00161808
age       | 0.299008                | 0.18908899
bmi       | 0.198341                | 0.18676482
children  | 0.067998                | 0.03755355

#### 3.2 Higher Degree Multiple Variables Linear Regression



### 4. Evaluation
> Elaborate your experiment, such as splitting dataset, K-fold; Compare your solution with benchmarks in literature; Evaluation metrics for your task;
Analysing your results etc.



### References
1. https://d.wanfangdata.com.cn/thesis/Y2415220
2. Raedel, M., Hartmann, A., Priess, H., Bohm, S., Samietz, S., Konstantinidis, I. & Walter, M.H. 2017, "Re-interventions after restoring teeth--Mining an insurance database", Journal of dentistry, vol. 57, pp. 14-19.