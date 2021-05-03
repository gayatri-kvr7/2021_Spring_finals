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


This proves the hypothesis






