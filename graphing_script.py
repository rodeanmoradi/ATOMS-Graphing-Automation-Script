# import libraries
import os
import glob
import pandas as pd
import matplotlib.pyplot as plt

# get files
folderPath = "/Users/rodeanmoradi/Documents/OneDrive - University of Toronto/ATOMS Summer'25/Rodean/Cell Cycling/Unprocessed Data"
files = glob.glob(os.path.join(folderPath, '*.csv'))

# iterate through files and plot all
for file in files: 
    # read csv file
    df = pd.read_csv(file, engine='python', skiprows=0)

    # only plot detail files
    if len(df) > 100:
        # plot csv files from experiments that rested cell differently
        if df.loc[2, 'Current(A)'] == 0:
            # locate where rest ends
            restEnd = min(df.index[df['Current(A)'] > 0])
            # create plot, only plotting temperature vals after rest
            dfSlice = df.loc[restEnd:]
            plt.figure()
            plt.plot(dfSlice['Test Time(s)'], dfSlice['Aux T1'])

            # set y-value range
            plt.ylim(20, 30)
            
            # set titles
            plt.title('Thermocouple Temp. vs. Time')
            plt.xlabel('Test Time')
            plt.ylabel('Thermocouple 1 Temperature')

            # display plot
            plt.grid(True)
            plt.show()

        else:
            # create plot
            plt.figure()
            plt.plot(df['Test Time(s)'], df['Aux T1'])

            # set y-value range
            plt.ylim(20, 30)
            
            # set titles
            plt.title('Thermocouple Temp. vs. Time')
            plt.xlabel('Test Time')
            plt.ylabel('Thermocouple 1 Temperature')

            # display plot
            plt.grid(True)
            plt.show()

    else:
        continue