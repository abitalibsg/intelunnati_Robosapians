# Robosapians_Saintgits College Of Engineering_Accident Locations On Indian Roads
Final Report Submission for Intel Unnati Industrial Training
### Description: 
India ranks first in the world for the number of accidents and lives lost on the roads.The country has 1% of the vehicles in the world.Ministry of road transport uses concept of Blackspot to mark these locations to improve road safety on national highways in the country.Here we have collected data of the state kerala.
### Data mapping 
* We have chosen Kerala as the focus of our analysis.
* We obtained the latitude and longitude coordinates for the accident locations and identified nearby hospitals using geolocation data.
* By utilizing QGIS software, we plotted these locations on a map of the area.
* Additionally, we generated a heatmap with the nearest hospitals to visualize the concentration of accidents.

  <img src="https://github.com/abitalibsg/intelunnati_Robosapians/assets/133338993/63c2ba25-0fcd-4d35-96dc-52d7055efebf" width="300" height="300">
  
<img src="https://github.com/abitalibsg/intelunnati_Robosapians/assets/133338993/da5037af-82b4-4003-88a7-c2187c308922" width="300" height="300">
### Data processing and visualization
Based on the collected data, we created a visualization graph that depicts the severity of accidents and the number of accidents in each state.

<img src="https://github.com/abitalibsg/intelunnati_Robosapians/assets/133338993/8e237d05-3852-44b6-a098-751c4d9a80be" width="600" height="600">

<img src="https://github.com/abitalibsg/intelunnati_Robosapians/assets/133338993/c8ebfe03-d336-432e-ae60-21f2a165c259" width="400" height="400">

  
### Data processing and machine learning

Latitude and longitude data are utilized in machine learning to cluster points based on severity, fatality, and the total count of fatal and grievous injury crashes. An unsupervised machine learning model, specifically K-means clustering, is employed to create clusters based on the aforementioned data criteria.

<img src="https://github.com/abitalibsg/intelunnati_Robosapians/assets/133338993/7c270ca2-f3b1-4f76-9be3-38f9659204d6" width="400" height="400">

After performing the machine learning process, the data was classified into three groups based on severity. The blue group (y=0) represents accidents with lower severity, the orange group (y=1) represents accidents with moderate severity, and the green group (y=2) represents accidents with high severity.

### Future outcome
* Using these data a software can be developed for warning the drivers of the blackspot location by an alarm system.The proposed software application aims to 
  enhance driver safety by utilizing classified accident data and identifying blackspot locations. Integrated with GPS technology, the software will provide real- 
  time alerts to drivers when they approach or enter high-risk areas. The system can be implemented as a mobile app or integrated into in-car systems, allowing for 
  customizable alarm settings. Regular updates of accident data and user feedback can ensure accuracy and relevance of the blackspot information. By providing 
  timely warnings, the software empowers drivers to exercise caution and take necessary precautions, ultimately reducing the likelihood of accidents in identified 
  blackspot locations.
* By leveraging the data on nearby hospitals, it is possible to develop a software application that establishes a connection between the airbag system and these 
  hospitals. In the event of an accident where the airbag is deployed, the software would send a signal to the nearby hospitals, notifying them of the occurrence. 
  This timely alert can enable hospitals to prepare and respond promptly to provide necessary medical assistance to the accident victims.
