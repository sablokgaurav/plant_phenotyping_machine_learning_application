#! /usr/bin/python
# Universitat Potsdam
# Author Gaurav Sablok
# date: 2024-2-23
# a streamlit application for the plant phenotyping and trait machine learning
import streamlit as st
import os
import logging
import pandas as pd
import sklearn as sk

st.title("plant phenotyping and trait machine learning")
st.header("this application uses the postgres as a backhand database")
columns = st.sidebar.selectbox("the number of the variables present in the datasets",
("variable1", "variable2", "variable3", "variable4"))
variable = st.sidebar.selectbox("the number of the variables present in the datasets",
                                   ([f"variable{i}" for i in range(len(pd.columns))])) 
Xdatasets = st.sidebar.selectbox("define the datasets for the machine learning X classification",
("variable1", "variable2", "variable3", "variable4"))
plant_phenotype = st.file_uploader("please upload a plant phenotyping datasets")

if plant_phenotype is not None:
datasets = pd.read_csv(plant_phenotype, sep = ",")
else:
st.write("No datasets selected")

# adding the final files for the vairables and the model declaration and deployment ot he cloud and will be ready by this evening.
# variable upload to be defined and the columns of the variables as the defined list
# [i for i in in range(len(plant_phenotype.columns)]
# "true" if len(pd.DataFrame([i for i in range(10)], columns=["values"]).columns) < 10 else "false"
