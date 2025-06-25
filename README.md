# ATOMS Lab Cell Testing Data Plotter

## Overview

At the Thermal Management Systems (TMS) Lab at ATOMS, my research project focuses on estimating the thermal characteristics of the Lithium-ion battery pouch cells
used for the University of Toronto Formula Racing Team. I regularly run tests on the cells to generate a temperature rise, after which I must plot the 
CSV file data to ensure that everything went well. This Python script loops through each CSV file in my 'Unprocessed Data' folder and plots each one on 
a separate graph. Running similar tests on cells led to a repetitive data analysis process, which could be automated to save time. This inspired me to complete 
this project. This project improved data analysis efficiency by 81%, resulting in a process that is 5× faster.

## Features

For some tests, the cell is rested for 2 hours to return to a state of thermal and electrochemical equilibrium. CSV files of such experiments are sliced so that only the 
relevant data is plotted.

The data from cell testing comes with two CSV files: a detail file (the data from the experiment) and a step file (the steps of the experiment). For estimating the 
thermal properties of the cell (e.g., conductivities, heat transfer coefficient), the step file is not necessary. Therefore, step files are not plotted.

