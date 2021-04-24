### 0. Abstract



### 1. Introduction (answer what is the real world problem and why it is important)
#### 1.1 Why we choose insurance area - from the company aspect
Four important implement directions of data mining in insurance area are:Determine rates, get new customers, retain old customers, and detect fraud claims. [<sup>1</sup>](#refer-anchor-1)
##### 1.1.1 Determine the rate:  
The premium rate is the ratio of the premium to the insured amount. If the premium is fixed and the compensation amount is too large, the premium rate will be very low, which will bring a certain economic burden to the company, and the insurance company will be in an unstable state, which is not conducive to steady development; If the premium rate is too high, for the insured, the insurance premium they bear is not equal to the protection they get, which will cause the loss of customers. The goal of the insurance company is to reduce the risk and cost to the maximum extent, so as to obtain the maximum income. Insurance industry is a typical knowledge intensive industry, which is more suitable for the implementation of knowledge management and data mining technology [<sup>2</sup>](#refer-anchor-2)

For insurance companies, how to give consideration to the efficiency of claim settlement and risk supervision, and how to mine the data stored by insurance companies to establish a prediction model can help insurance companies to choose insurance types and determine premium rates. [<sup>2</sup>](#refer-anchor-2)

##### 1.1.2 Detect fraud claim:
Understand the personal insurance data and diagnosis and treatment materials related to customers, select characteristic variables, establish decision-making data model, help insurance companies to carry out customer risk level analysis, customers with risk level within the normal range can get compensation quickly, and the applicants with suspected data should be traced. Through the analysis of the historical data of medical insurance claims cases, we can establish an effective automatic identification mode of fraud cases, improve the operating performance of insurance companies, and promote the healthy, stable and harmonious development of the insurance industry.[<sup>2</sup>](#refer-anchor-2)

##### 1.1.3 Reaching new customers: 
Data mining can help insurance companies fully explore the value of customers and the potential value that customers may bring in each stage of their life cycle. 
1. In terms of customer identification, provide general characteristics of customer data and identify potential customers by subdividing customer characteristics.
2. Clustering to classify potential customers in order to convert them into real customers 
3. Analyze customer demand through the pattern of customers' past purchase behavior, to facilitate the company to provide products that are more suitable for customers. 

##### 1.1.4 Retain old customers：
In terms of customer retention, data mining can be applied to customer loyalty analysis and customer churn waring analysis. Through the historical transaction behavior of customers, the abnormal behavior of customers or warned, and the purchase change is predicted.
#### 1.2 Why we choose to mine medical data and the importance of medical data collected from insurance - from the government aspects
1. With the deepening of population aging in China, the payment pressure of endowment insurance fund is becoming more and more obvious. How to maintain the balance of income and expenditure of endowment insurance fund is an important issue in the development of social security in China. The sustained growth of insurance companies' profits can effectively drive the stable development of the insurance industry in China, thus reducing the burden of social insurance.
2. Improving the social security system. Identify people who are not willing to be insured by insurance companies and ensure that their medical health can be guaranteed by the national finance. 
3. The government's partial grasp of this part of data can promote the improvement of malicious competition in the insurance industry. In all kinds of insurance, only life insurance, trauma insurance and disability insurance can carry out risk rating, while health insurance companies cannot offer different prices according to age, gender, health status or family size. The price of insurance products depends on the possibility of individual claims. Due to the lack of laws regulating data mining, the problem of customer privacy becomes more complex. Herman argues that the current privacy law does not provide any protection for individuals as to how information subsequently obtained through data mining will be used. It is particularly problematic to decide who can become a customer according to the categories found by data mining. [<sup>3</sup>](#refer-anchor-3) In order to prevent insurance companies from obtaining people's personal information through improper means to compete for the market, the government can control and use it within the scope of its permission, so as to avoid the immoral use of data mining as far as possible. And protecting the public's personal information from secondary use or abuse.
4. Mining medical insurance data is an effective way to observe the long-term treatment and recovery of diseases. Raedel Michael Through the digital database of a large national insurance company in Germany, this paper tracks the experimental effect of re intervention of restorative treatment of permanent teeth. He also put forward improvement measures from the perspective of public health and the need of optimized strategies. [<sup>4</sup>](#refer-anchor-4) Shen Chengche used association rule arm to study the complex clinical manifestations of BPD with borderline personality disorder through the data of patients in the National Health Insurance Research Database of Taiwan[<sup>5</sup>](#refer-anchor-5) It can be seen that data mining also has great application prospects in disease research and nursing, which should be taken into consideration by the government.

In conclusion, our optimism about the prospects of data mining applications in the insurance industry, 
coupled with the importance of medical data obtained from insurance policies, 
constitute the reasons why we chose this direction as our subject.



### 2. Dataset selection(collection) and Data pre-processing

#### 2.1 Where you find your data (or how do you collect the data and create your dataset)?
#### 2.2 How do you analyze your data?
#### 2.3 how to pre-process your data to fit your solution?
#### 2.4 Any challenges with your dataset?
![children](children.png)
![bmi](bmi.png)
![age](age.png)


### 3. Methodologies 
> Any machine learning algorithm can be used (not limited to the algorithm we have learned).
Creativity is encouraged.
Be careful, a sophisticated approach with little description and explanation will receive little credit.

### 4. Evaluation
> Elaborate your experiment, such as splitting dataset, K-fold; Compare your solution with benchmarks in literature; Evaluation metrics for your task;
Analysing your results etc.

### References
<div id="refer-anchor-1"></div>
- [1] https://wenku.baidu.com/view/07faf62d915f804d2b16c13b.html
<div id="refer-anchor-2"></div>
- [2] https://d.wanfangdata.com.cn/thesis/Y2415220
<div id="refer-anchor-3"></div>
- [3] AL-SAGGAF, Y. (2015). The Use of Data Mining by Private Health Insurance Companies and Customers’ Privacy: An Ethical Analysis. Cambridge Quarterly of Healthcare Ethics, 24(3), 281-292. doi:10.1017/S0963180114000607
<div id="refer-anchor-4"></div>
- [4] Raedel, M., Hartmann, A., Priess, H., Bohm, S., Samietz, S., Konstantinidis, I. & Walter, M.H. 2017, "Re-interventions after restoring teeth--Mining an insurance database", Journal of dentistry, vol. 57, pp. 14-19.
<div id="refer-anchor-5"></div>
- [5] Cheng-Che, S., Li-Yu, H. & Ya-Han, H. 2017, "Comorbidity study of borderline personality disorder: applying association rule mining to the Taiwan national health insurance research database", BMC Medical Informatics and Decision Making, vol. 17.

