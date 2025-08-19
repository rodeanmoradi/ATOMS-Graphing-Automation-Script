# ATOMS Lab Cell Testing Data Plotter

## Overview

At the Thermal Management Systems (TMS) Lab at ATOMS, my research project focuses on estimating the thermal characteristics of lithium-ion battery pouch cells used by the University of Toronto Formula Racing Team. I regularly run tests on the cells to generate a temperature rise, after which I plot the CSV data to ensure that everything went well. This Python script loops through each CSV file in my 'Unprocessed Data' folder and plots each one on a separate graph.

Running similar tests on cells led to a repetitive data analysis process that could be automated to save time. This inspired me to complete this project. It increased analysis efficiency by 81%, accelerating the workflow 5×.

## Features

For some tests, the cell is rested for 2 hours to return to a state of thermal and electrochemical equilibrium. CSV files from such experiments are sliced so that only the relevant data is plotted.

The data from cell testing comes with two CSV files: a detail file (the experimental data) and a step file (the procedural steps). For estimating the thermal properties of the cell (e.g., conductivities, heat transfer coefficient), the step file is not necessary. Therefore, step files are not plotted.
