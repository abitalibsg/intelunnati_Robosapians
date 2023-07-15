## Steps to Identify High-Risk Hotspots in Kerala based on Accident Severity

1. **Collecting Data:**
   - Gathered data related to road accidents in Kerala, including accident latitude and longitude.

2. **Collecting Nearby Hospitals Data:**
   - Obtained data on the locations of nearby hospitals.

3. **Collecting Severity Data:**
   - Collected data on accident severity, including fatalities and the sum of fatal and grievous injury crashes.

4. **Uploading Data to QGIS:**
   - Imported the accident latitude and longitude data, nearby hospitals data, and severity data into the QGIS software.

5. **Creating Heatmaps and Blackspots:**
   - Utilized QGIS to generate heatmaps and identify blackspots based on the accident data and the locations of nearby hospitals.

6. **Visualization of Data:**
   - Created visual graphs to analyze the number of accident cases in each city for each year and determine the vehicles causing the most accidents.

7. **Applying k-means Clustering:**
   - Employed unsupervised machine learning using the k-means clustering algorithm.
   - Utilized accident severity, fatalities, and the sum of fatal and grievous injury crashes as factors for clustering.

8. **Mapping Accident Clusters:**
   - Mapped the clusters obtained from the k-means clustering into the OpenStreetMap of Kerala.
   - Visualized the accident clusters on the map based on severity, fatalities, and the sum of fatal and grievous injury crashes.

9. **Identification of High-Risk Hotspots:**
   - Analyzed the clustering model and identified the locations with the highest accident severity.
   - Found that out of the 238 locations, there are 16 high-risk hotspots with the most severe accidents.
