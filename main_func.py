import streamlit as st;
import pandas as pd;

@st.cache(allow_output_mutation=True)
def df_country():
    # load dataset covid-19
    dataset = pd.read_excel("dataset/dataset_covid.xlsx", sheet_name="data-covid-indonesia", engine="openpyxl");

    # convert obj or str to datetime
    dataset["date"] = pd.to_datetime(dataset["date"], format="%Y-%m-%d");

    # remove hh:mm:ss in columns date
    dataset["date"] = dataset['date'].dt.date;

    # return value
    return dataset;

@st.cache(allow_output_mutation=True)
def df_province():
    return pd.read_excel("dataset/dataset_covid.xlsx", sheet_name="data-covid-provinsi", engine="openpyxl");

def func_agg(dataset):
    # chose a columns for agg
    df_agg = dataset[["date","daily_positive","daily_recovery", "daily_dead"]];

    # set index datetime
    df_agg = df_agg.set_index(pd.to_datetime(df_agg["date"]));

    # resample mountly
    df_agg = df_agg.resample('M').sum();

    # return value
    return df_agg;