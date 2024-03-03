import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_decimal

day_df = pd.read_csv("day.csv")
st.header('Bike Sharing Dataset')
st.subheader('Daily Bike Rentals 2011-2012')

total_rent = day_df['cnt'].sum()
st.metric("Total rentals", value=format_decimal(total_rent))

## visualisasi pertanyaan 1
st.subheader('Daily Bike Rentals for Each Season')

# menampilkan bar chart
fig, ax=plt.subplots(figsize=(35, 15))
color_palette = ["#FFA77A", "#FFA77A", "#FF6347", "#FFA77A" ]
data_season = day_df.groupby('season')['cnt'].sum().reset_index()
sns.barplot(
    y = "cnt",
    x = "season",
    data = data_season/1000,
    palette = color_palette
)

ax.set_title("Number of Bike Rentals by Season", loc = "center", fontsize = 40)
ax.set_ylabel("Rent (*1e3)", fontsize = 30)
ax.set_xlabel("Season", fontsize = 30)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
ax.set_xticklabels(["Spring", "Summer", "Fall", "Winter"])
st.pyplot(fig)

# menampilkan jumlah peminjaman sepeda pada musim gugur (jumlah peminjaman sepeda tertinggi)
total_rent_fall = day_df[day_df['season'] == 3]['cnt'].sum()
st.metric("The highest daily bike rentals occur in the **FALL**.", value=format_decimal(total_rent_fall))

## visualisasi pertanyaan 2
st.subheader('Relationship between Temperature and Number of Bike Rentals')

# menampilkan regression plot
fig, ax=plt.subplots(figsize=(35, 15))
sns.regplot(data=day_df, x="temp", y="cnt", color="#FF6347")

ax.set_title("Regression Plot of Bike Rentals with Correlation Line", loc = "center", fontsize = 40)
ax.set_ylabel("Temperature", fontsize = 30)
ax.set_xlabel("Rent", fontsize = 30)
ax.tick_params(axis='x', labelsize=30)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)
# menampilkan penjelasan grafik
correlation = day_df['temp'].corr(day_df['cnt'])
st.write('Temperature (temp) and the number of bike rentals (cnt) have a positive relationship where there is a tendency that the higher the temperature, the higher the number of bike rentals.\n')
st.metric('Correlation value:', value=correlation)
