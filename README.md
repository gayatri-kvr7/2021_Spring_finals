# **Drug-Related Fatalities After Providing Medical Treatment**

Team Members: 
a) Gayatri Kallakuri (gayatri7), GitHub: gayatri-kvr7
b) Shreya Girdhar (girdhar4), GitHub: girdhar4

Our aim for this project is to study and understand the data from two datasets coming from the state of Connecticut. The data has information about Drug related deaths for different deaths and how these deaths are influenced by Addiction Treatment. The project is based on below two data sources:

1. Accidental Drug Related Deaths 2012-2018
https://catalog.data.gov/dataset/accidental-drug-related-deaths-2012-2018 This is Accidental Drug Related Deaths for years 2012-2018 for the state of connecticut. This data contains a listing of each accidental death associated with drug overdose in Connecticut from 2012 to 2018. Data is derived from an investigation by the Office of the Chief Medical Examiner which includes the toxicity report, death certificate, as well as a scene investigation.

2. Admissions to DMHAS Addiction Treatment by Town, Year, Month, and Primary Drug
https://catalog.data.gov/dataset/admissions-to-dmhas-addiction-treatment-by-town-year-month-and-primary-drug This data here is Addiction Treatment data by Town-Year-Month and primary drug for the state of connecticut This dataset includes monthly admission counts- by primary drug of choice- to DMHAS funded/operated treatment, organized by clients town of residence.

After doing an initial exploratory data analysis we realised the time frame for both the data sources is different. The Accidental Drug Related Deaths are captured for the years 2012 to 2018 and for the Addiction Treatment the data captured is for years 2014-2016. Since only data from 2014-2016 was available in both the files we have taken the data fr 2014-2016 to validate the Hypothesis.

# <ins>Overview of Data in Files</ins>

**1. Accidental Drug Related Deaths 2012-2018**
There are a total of 15 drugs for which we have some fatility data. With all the data present in the file the fatility rate for men is observed to be more than for women.![download1](https://user-images.githubusercontent.com/77979984/116886114-4ac62d80-abee-11eb-8e42-7ab5c57e005a.png)

The Deaths are spread across the age group of 20-70, but most of teh deaths have occurred for the age group 25-55
![newplot2](https://user-images.githubusercontent.com/77979984/116886484-c031fe00-abee-11eb-9f32-0f63e95a1fc0.png)

**2. Admissions to DMHAS Addiction Treatment by Town, Year, Month, and Primary Drug**
There are 19 different drugs for which we have some data for people who have received treatment.
![download3](https://user-images.githubusercontent.com/77979984/116886631-ec4d7f00-abee-11eb-9dc2-4312feb70b2f.png)

# <ins>Hypothesis</ins>
## Hypothesis I - People are more likely to die due to accidental death because of Ethanol consumption than drug use due to the consumption of Morphine_NotHeroin.
  I) 
The causes of death can either be an accidental death or death due to natural causes. The accidental death rate bacause of consumption of ethanol is greater than thean due to consumption of Morphine_NotHeroin.
The comparison is done on a per year basis and based on Gender. The data has been studied over a period of 3 years(2014-2016). 
The total number of deaths due to consumption of Ethanol has been increasing over years for both males and females.
![newplot4](https://user-images.githubusercontent.com/77979984/116888598-45b6ad80-abf1-11eb-9272-f6713d2a51e3.png)

The total number of deaths due to the consumption of Morphine_NotHeroin is increasing over the years for both males and females.
![newplot5](https://user-images.githubusercontent.com/77979984/116888814-81ea0e00-abf1-11eb-9eac-3633b09628ad.png)

When the number of deaths due to both of the drugs are stacked it can be observed that the number of ethanol deaths are significantly greater than the number of Morphine_NotHeroin fr each of the 3  years.
![newplot6](https://user-images.githubusercontent.com/77979984/116889320-09378180-abf2-11eb-9eee-38ed62255f59.png)

Evaluating the numerical parameters we find that theere are 94% more deaths due to ethanol consumption than due to Morphine_NotHeroin consumption.

This proves the hypthesis.

## Hypothesis II -The proportion of deaths vs the total number of people admitted for the consumption of the drug Heroin is greater than the proportion of deaths vs the total number of people admitted for the consumption of the drug Cocaine.

A few number of people admitted due to any drug use result in deaths. We comapre the hospital admission to death proportion for the drugs Heroin and Cocaine for the years 2014-2106.

It can be observed from the plot that for each year the number of people admitted for Heroin consumption use is greater than the number admitted for Cocaine consumption.

![Capture-2](https://user-images.githubusercontent.com/77979984/116890833-a810ad80-abf3-11eb-8bed-0349fd0ea90b.PNG)


It can be observed from the plot that for each year the number of people died due to Heroin consumption use is greater than the number admitted for Cocaine consumption.
![Capture-1](https://user-images.githubusercontent.com/77979984/116890511-523c0580-abf3-11eb-96ad-915008d3fefb.PNG)

The Heroin death to admission ratio:0.305
The Cocaine death to admission ratio:0.290

Even though by a very small margin, the ratio of death to hospital ratio is greater for the Heroin.

![Capture-3](https://user-images.githubusercontent.com/77979984/116893605-c9bf6400-abf6-11eb-9f79-23c66f585129.PNG)

The proportion of deaths vs the total number of people admitted for the consumption of the drug Heroin is 0.3 and the proportion of deaths vs the total number of people admitted for the consumption of the drug Cocaine is 0.29. Even though the difference between the two is very small, the proportion for Heroin is greater. This proves the hypothesis.

## Hypothesis III -People are more likely to get injured due to Heroin at any other place than at their Residence.

In this Hypothesis we filtered the data for Heroin and grouped the deaths based on the location of death. 

![newplot10](https://user-images.githubusercontent.com/77979984/117709529-a8321f80-b196-11eb-8c3d-6060e19df30c.png)

Plotting a scatter plot for the same we can see that for any year the injuries occuring at each individuals residence is greater than any other location.
Plotting another plot for age vs injury

![newplot1010](https://user-images.githubusercontent.com/77979984/117710256-85ecd180-b197-11eb-8001-446deef9e637.png)

Based on the above graph we can infer that GenX are also most likely to get injured at their residence than Hotel/Motel or a homeless shelter

![download11](https://user-images.githubusercontent.com/77979984/117710673-001d5600-b198-11eb-9e37-896eb653c34f.png)

From these graphs we came to a conclusion that Residence and hotel/motel are the two prime locations where people are prone to injuries
Analysing each location one by one 

![newplot11](https://user-images.githubusercontent.com/77979984/117710849-2e029a80-b198-11eb-87db-3b68c774d4ac.png)

![newplot111](https://user-images.githubusercontent.com/77979984/117710866-34911200-b198-11eb-9bce-3b8f45d74242.png)

After calculating and comparing the injuries caused by Heroin at Residence or Hotel we came to the conclusion that the residence injuries are greater then hotel/motel injuries by 159.375 % 
This violates the hypthesis. Residence is the prime location where people are prone to injuries due to heroin consumption than any other location.

## Hypothesis IV -New Haven has seen a greater decline in admission to deaths ratio due to Cocaine consumption in the year 2015-2016 than New London
Firstly we counted the admission counts per city and we selected New Haven and New London for our analysis. Comparing both the cities and the admission rates: 

![newplot12](https://user-images.githubusercontent.com/77979984/117712636-31972100-b19a-11eb-8458-ebc23d994bcf.png)

Calculating the number of death counts for Heroin consumption in New Haven and New London. There has been an increase in the number of deaths due to Heroin consumption in New Haven and New London from 2015-2016. However, the change has been steeper in New Haven

![newplot13](https://user-images.githubusercontent.com/77979984/117712753-59868480-b19a-11eb-84a4-29d87e5f25d1.png)

Calculating the admission:death ratio

![newplot14](https://user-images.githubusercontent.com/77979984/117712901-8b97e680-b19a-11eb-8db7-35dbf34646f8.png)

![newplot16](https://user-images.githubusercontent.com/77979984/117713435-47591600-b19b-11eb-9e94-b7cf137e6745.png)

The percentage change in the admission:death ratio for New Haven is 29% whereas for New London is 13%. Therefore, New Haven has been a greater decline in the ratio. This proves the hypothesis.











