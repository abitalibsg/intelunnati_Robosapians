# Robosapians_Saintgits College Of Engineering_Accident Locations On Indian Roads
Final Report Submission for Intel Unnati Industrial Training
### Description: 
India ranks first in the world for the number of accidents and lives lost on the roads.The country has 1% of the vehicles in the world.Ministry of road transport uses concept of Blackspot to mark these locations to improve road safety on national highways in the country.Here we have collected data of the state kerala.
### Data mapping 
* We have chosen Kerala as the focus of our analysis.
* We obtained the latitude and longitude coordinates for the accident locations and identified nearby hospitals using geolocation data.
* By utilizing QGIS software, we plotted these locations on a map of the area.
* Additionally, we generated a heatmap to visualize the concentration of accidents.

### Data processing and visualization
Based on the collected data, we created a visualization graph that depicts the severity of accidents and the number of accidents in each state.
  
### Data processing and machine learning
Latitudinal and longitudinal data are used for machine learning for clustering the points based on severity,fatality and sum of fatal and grievous injury crashes.An unsupervised machine learning model is made using kmeans clustering that will cluster according to above data.
![machine_learning_severity](https://github.com/abitalibsg/intelunnati_Robosapians/assets/133338993/7c270ca2-f3b1-4f76-9be3-38f9659204d6)

After the machine learning process data is classified into 3 groups ,blue(y=0) having less severity,orange(y=1) having moderate severity and green(y=2) having high severity

### Future outcome
Using these data a software can be developed for warning the drivers of the blackspot location by an alarm system. 
