#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt

#Read the data from csv and create a dataframe
growDataset_df = pd.read_csv('GrowLocations.csv')

#Rename the wrongly named columns
growDataset_df.rename(columns={"Latitude": "Longitude", "Longitude": "Latitude"}, inplace=True)

#Filtering the necesarry boundary from the data and remove the unnecessary data
filtered_growDataset_df = growDataset_df[(growDataset_df['Latitude'] >= 50.681) & (growDataset_df['Latitude'] <= 57.985) 
                        & (growDataset_df['Longitude'] >= -10.592) & (growDataset_df['Longitude'] <= 1.6848)]

# Creating the plot variables (x, y and area of plot)
x_axis = filtered_growDataset_df['Latitude']
y_axis= filtered_growDataset_df['Longitude']
figure, ax = plt.subplots()
ax.scatter(y_axis, x_axis, c='blue')

#Reading the UK image 
uk_map = plt.imread('map7.png')

#Plotting the filtered data on the uk map
plt.title("Plotting Grow Data")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
ax.imshow(uk_map, extent = (-10.5, 1.8, 50.6, 57.8))

#Saving Output in image
figure.savefig('2544403GrowLocationsMaps.png')