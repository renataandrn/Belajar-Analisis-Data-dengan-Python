import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Bike Rental Dashboard")
st.subheader("Syahadat'aini Renata Andriana")

day_df = st.file_uploader("day.csv", type=["csv"])
hour_df = st.file_uploader("hour.csv", type=["csv"])

if day_df is not None:
    day_df = pd.read_csv(day_df)
    st.write("Day Overview")
    st.dataframe(day_df.head())

if hour_df is not None:
    hour_df = pd.read_csv(hour_df)
    st.write("Hour Overview")
    st.dataframe(hour_df.head())

if day_df is not None:
    st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Per Hari)")
    plt.figure(figsize=(10,5))
    sns.barplot(x='weathersit', y='cnt', data=day_df, estimator='mean')
    plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Per Hari)')
    st.pyplot(plt)

if hour_df is not None:
    st.subheader("Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Per Jam)")
    plt.figure(figsize=(10,5))
    sns.barplot(x='weathersit', y='cnt', data=hour_df, estimator='mean')
    plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Per Jam)')
    st.pyplot(plt)

if day_df is not None:
    st.subheader("Rata-rata Penyewaan Sepeda Pada Hari Kerja (Per Hari)")
    plt.figure(figsize=(10,5))
    sns.barplot(x='workingday', y='cnt', data=day_df, estimator='mean')
    plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Per Hari)')
    st.pyplot(plt)

if hour_df is not None:
    st.subheader("Rata-rata Penyewaan Sepeda Pada Hari Kerja (Per Jam)")
    plt.figure(figsize=(10,5))
    sns.barplot(x='workingday', y='cnt', data=hour_df, estimator='mean')
    plt.title('Rata-rata Penyewaan Sepeda Berdasarkan Kondisi Cuaca (Per Jam)')
    st.pyplot(plt)