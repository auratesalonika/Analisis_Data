import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load dataset with dynamic path
def load_data():
    current_dir = os.path.dirname(os.path.abspath(__file__))  # Dapatkan path direktori file ini
    data_path = os.path.join(current_dir, '..', 'data', 'day.csv')  # Path menuju folder 'data/day.csv'
    day_data = pd.read_csv(data_path)  # Pastikan file berada di path tersebut
    return day_data

day_data = load_data()

# Dashboard Title
st.title("Analisis Peminjaman Sepeda")

# Sidebar for navigation
option = st.sidebar.selectbox(
    "Pilih Pertanyaan:",
    ("Pengaruh Cuaca terhadap Peminjaman Sepeda", 
     "Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
)

# Pertanyaan 1: Bagaimana pengaruh kondisi cuaca terhadap jumlah peminjaman sepeda harian?
if option == "Pengaruh Cuaca terhadap Peminjaman Sepeda":
    st.header("Pengaruh Kondisi Cuaca terhadap Jumlah Peminjaman Sepeda")
    st.write("Visualisasi berikut menunjukkan bagaimana kondisi cuaca mempengaruhi jumlah peminjaman sepeda.")

    # Boxplot Jumlah Peminjaman Berdasarkan Kondisi Cuaca
    st.subheader("Distribusi Jumlah Peminjaman Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=day_data, ax=ax)
    ax.set_title('Distribusi Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca')
    ax.set_xlabel('Kondisi Cuaca')
    ax.set_ylabel('Jumlah Peminjaman')
    ax.set_xticklabels(['Cerah', 'Bersalju', 'Hujan', 'Berawan'])
    st.pyplot(fig)

    # Scatter Plot Suhu vs. Jumlah Peminjaman
    st.subheader("Hubungan antara Suhu dan Jumlah Peminjaman Sepeda")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_data, ax=ax)
    ax.set_title('Hubungan antara Suhu dan Jumlah Peminjaman Sepeda')
    ax.set_xlabel('Suhu (Normalized)')
    ax.set_ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

# Pertanyaan 2: Bagaimana pola penggunaan sepeda berdasarkan hari dalam seminggu?
elif option == "Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu":
    st.header("Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
    st.write("Visualisasi berikut menunjukkan pola peminjaman sepeda berdasarkan hari dalam seminggu.")

    # Countplot Jumlah Peminjaman Berdasarkan Hari dalam Seminggu
    st.subheader("Jumlah Peminjaman Berdasarkan Hari dalam Seminggu")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.countplot(x='weekday', data=day_data, ax=ax)
    ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Jumlah Peminjaman')
    ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot(fig)

    # Line Plot Rata-rata Peminjaman Berdasarkan Hari dalam Seminggu
    st.subheader("Rata-rata Peminjaman Berdasarkan Hari dalam Seminggu")
    fig, ax = plt.subplots(figsize=(10, 6))
    average_per_day = day_data.groupby('weekday')['cnt'].mean().reset_index()
    sns.lineplot(x='weekday', y='cnt', data=average_per_day, ax=ax)
    ax.set_title('Rata-rata Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    ax.set_xlabel('Hari dalam Seminggu')
    ax.set_ylabel('Rata-rata Jumlah Peminjaman')
    ax.set_xticklabels(['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot(fig)

# End of dashboard
st.write("---")
st.write("Terima kasih telah menjelajahi Analisis Peminjaman Sepeda!")
st.write("Copyright @ Aura Tesalonika 2024")
