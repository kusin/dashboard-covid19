# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;

# import any file 
from main_func import df_country;
from main_func import df_province;
from main_func import func_agg;

# set config ui-dasboard streamlit
st.set_page_config(
    page_title="My Dasboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": "https://www.github.com/kusin",
        "Report a bug": "https://www.github.com/kusin",
        "About": "### Copyright 2022 all rights reserved by Aryajaya Alamsyah"
    }
);

# --------------------------------------------------------------------------------------- #
# data acquisition 1 -------------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
dataset = df_country();
# ---------------------------------------------------------------------------------------

# container-header-fuild
with st.container():
    st.markdown("## Statistical Analysis and Data Visualization of Covid-19 in Indonesia Country");
    st.markdown("- Summary statistics, *updated 20 Oktober 2020");


# container-summary of covid-19
with st.container():
    col1, col2, col3, col4, col5, col6,col7, col8 = st.columns(8);
    col1.metric(
        label="Percentage recovery",
        value="{:.2f}".format((dataset["daily_recovery"].sum() / dataset["daily_positive"].sum())*100)+"%", 
        delta="0,35%"
    );
    col2.metric(
        label="Percentage dead",
        value="{:.2f}".format((dataset["daily_dead"].sum() / dataset["daily_positive"].sum())*100)+"%",
        delta="0,00%"
    );
    col3.metric(
        label="Cumulative Positive",
        value="{:,}".format(dataset["daily_positive"].sum()),
        delta="3,373 People"
    );
    col4.metric(
        label="Cumulative Recovery",
        value="{:,}".format(dataset["daily_recovery"].sum()),
        delta="3.919 People"
    );
    col5.metric(
        label="Cumulative Dead",
        value="{:,}".format(dataset["daily_dead"].sum()),
        delta="106 People"
    );
    col6.metric(
        label="Daily Positive",
        value="{:,}".format(dataset["daily_positive"].iloc[-1]),
        delta="-732 People"
    );
    col7.metric(
        label="Daily Recovery",
        value="{:,}".format(dataset["daily_recovery"].iloc[-1]),
        delta="187 People"
    );
    col8.metric(
        label="Daily Dead",
        value="{:,}".format(dataset["daily_dead"].iloc[-1]),
        delta="26 People"
    );

# container-time-series
with st.container():
    col1, col2 = st.columns(2);
    col1.markdown("- Cumulative positive, recovery, dead");
    col1.plotly_chart(
        px.line(
            dataset,
            x=dataset["date"], 
            y=["cumulative_positive", "cumulative_recovery", "cumulative_dead"],
            color_discrete_sequence=["blue", "green", "red"]
        ),
        use_container_width=True
    );
    df_agg = func_agg(dataset);
    col2.markdown("- Daily positive, recovery, dead");
    col2.plotly_chart(
        px.line(
            df_agg,
            x=df_agg.index, 
            y=["daily_positive", "daily_recovery", "daily_dead"],
            color_discrete_sequence=["blue", "green", "red"]
        ),
        use_container_width=True
    );



# container-scatter-plot
with st.container():
    col1, col2 = st.columns(2);
    col1.markdown("- scatter positive and recovery");
    col1.plotly_chart(
        px.scatter(
            dataset,
            x=dataset["daily_positive"],
            y=dataset["daily_recovery"],
            color_discrete_sequence=["#1E90FF"]
        ),
        use_container_width=True
    );
    col2.markdown("- scatter positive and dead");
    col2.plotly_chart(
        px.scatter(
            dataset,
            x=dataset["daily_positive"],
            y=dataset["daily_dead"],
            color_discrete_sequence=["#dc143c"]
        ),
        use_container_width=True
    );

# --------------------------------------------------------------------------------------- #
# data acquisition province ------------------------------------------------------------- #
# --------------------------------------------------------------------------------------- #
# load dataset covid-19
dataset = df_province();
# --------------------------------------------------------------------------------------- #

# calculate the percentage of positive, cured, dead for each province
dataset["percentage_recovery"] = round((dataset["sum_recovery"] / dataset["sum_positive"]) * 100, 2)
dataset["percentage_dead"] = round((dataset["sum_dead"] / dataset["sum_positive"]) * 100, 2);

# sorting sum-positive with most cases
df_positive = dataset.sort_values("sum_positive", ascending=False);
df_positive = df_positive[["province", "sum_positive"]].head();

# container pie-plot and bar-plot for sum_positive
with st.container():
    col1, col2 = st.columns(2);
    col1.markdown("- percentage top 5 province of sum positive");
    col1.plotly_chart(
        px.pie(
            df_positive, 
            values="sum_positive", 
            names="province", 
            color="province",
            hole=0.5,
            color_discrete_sequence=["#BAD0DE", "#D3EBE9", "#F2EDDC", "#DDE6CF", "#CADECD"]
        ),
        use_container_width=True
    );
    col2.markdown("- most cases top 5 province of sum positive");
    col2.plotly_chart(
        px.bar(
            df_positive,
            x="province",
            y="sum_positive",
            color_discrete_sequence=["#1E90FF"]
        ),
        use_container_width=True
    );

# sorting sum-recovery with most cases
df_recovery = dataset.sort_values("sum_recovery", ascending=False);
df_recovery = df_recovery[["province", "sum_recovery"]].head();

# container pie-plot and bar-plot for sum-recovery
with st.container():
    col1, col2 = st.columns(2);
    col1.markdown("- percentage top 5 province of sum recovery");
    col1.plotly_chart(
        px.pie(
            df_recovery, 
            values="sum_recovery", 
            names="province", 
            color="province",
            hole=0.5,
            color_discrete_sequence=["#FAEFCA", "#D1E5AE", "#9ABBD9", "#9292C2", "#DBA9CE"]
        ),
        use_container_width=True
    );
    col2.markdown("- most cases top 5 province of sum recovery");
    col2.plotly_chart(
        px.bar(
            df_recovery,
            x="province",
            y="sum_recovery",
            color_discrete_sequence=["#3CB371"]
        ), 
        use_container_width=True
    );

# sorting sum-dead with most cases
df_dead = dataset.sort_values("sum_dead", ascending=False);
df_dead = df_dead[["province", "sum_dead"]].head();

# container pie-plot and bar-plot for sum-dead
with st.container():
    col1, col2 = st.columns(2);
    col1.markdown("- percentage top 5 province of sum dead");
    col1.plotly_chart(
        px.pie(
            df_dead, 
            values="sum_dead", 
            names="province", 
            color="province",
            hole=0.5,
            color_discrete_sequence=["#9FC9C9", "#B4DBD4", "#F2F2C2", "#EEE8AE", "#F7D05E"]
        ),
        use_container_width=True
    );
    col2.markdown("- most cases top 5 province of sum dead");
    col2.plotly_chart(
        px.bar(
            df_dead,
            x="province",
            y="sum_dead",
            color_discrete_sequence=["#dc143c"]
        ),
        use_container_width=True
    );



