#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Adding various required libraries
from ast import increment_lineno
import pandas as pd
from sklearn.cluster import KMeans
import folium
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Code for reading the csv file containing the data
df = pd.read_csv("Kerala Blackspots with nearest hospitals finalised dataset (csv) (2).csv")
df.head()


# In[3]:


#Assigning columns "Accident Severity Index","Number of Fatalities", "Sum of Fatal & Grievous Injury Crashes" to a variable 'z'
z = df[["Accident Severity Index","Number of Fatalities", "Sum of Fatal & Grievous Injury Crashes"]]

#Printing z
z.head()


# In[5]:


#Below 3 lines of code is for finding the optimum number of clusters using Elbow method.


# In[6]:


wcss = []
for i in range(1,11):
    model = KMeans(n_clusters=i)
    y_kmeans = model.fit_predict(z)
    wcss.append(model.inertia_)


# In[7]:


model.inertia_


# In[8]:


#Plotting it into the Elbow graph
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method')
plt.show()


# In[9]:


#Therefore the optimum number of clusters is 3 from the Elbow graph


# In[10]:


#Clustering the data into 3 clusters
model = KMeans(n_clusters=3)
y_kmeans = model.fit_predict(z)


# In[11]:


df['y'] = y_kmeans


# In[12]:


#Downloading the data to be clustered
df.to_csv("final_data_with_cluster.csv")


# In[13]:


#Printing data to be mapped with k means variable 'y'
df.head()


# In[14]:


#Creating clusters
plt.scatter(df['Longitude'], df['Lattitude'],c=df['y'],)


# In[15]:


#below 3 lines are for categorising and grouping the locations based on (low,moderate and high)


# In[16]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[17]:


df['y'] = pd.Categorical(df.y)
df.y.value_counts()


# In[18]:


sns.countplot(x ='y', data = df)


# In[19]:


#Below codes are for deviding the clusters into 3 groups (cluster1,cluster2 and cluster3)
cluster1 = df[['Lattitude', "Longitude"]][df['y'] == 0].values.tolist()
cluster2 = df[['Lattitude', "Longitude"]][df['y'] == 1].values.tolist()
cluster3 = df[['Lattitude', "Longitude"]][df['y'] == 2].values.tolist()


# In[20]:


#Printing the Kerala state openstreet map
kerala_map = folium.Map(location=[10.8505, 76.2711], zoom_start=8,tiles = "openstreetmap")
kerala_map


# In[21]:


#Below is the code for embedding or mapping the clusters into street map of kerala


# In[22]:


#for embedding or mapping the clusters into openstreet map of kerala
for i in cluster1:
    folium.CircleMarker(i, radius=2,color='blue',fill_color='lightblue').add_to(kerala_map)

for i in cluster2:
    folium.CircleMarker(i, radius=2,color='red',fill_color='lightred').add_to(kerala_map)

for i in cluster3:
    folium.CircleMarker(i, radius=2,color='green',fill_color='lightgreen').add_to(kerala_map)


# In[23]:


#Printing the map
kerala_map


# In[ ]:




