import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
def load_data():
    day_data = pd.read_csv('day.csv')
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
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='weathersit', y='cnt', data=day_data)
    plt.title('Distribusi Jumlah Peminjaman Sepeda Berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Jumlah Peminjaman')
    plt.xticks([0, 1, 2, 3], ['Cerah', 'Bersalju', 'Hujan', 'Berawan'])
    st.pyplot(plt)
    plt.clf()  # Clear figure

    # Scatter Plot Suhu vs. Jumlah Peminjaman
    st.subheader("Hubungan antara Suhu dan Jumlah Peminjaman Sepeda")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='temp', y='cnt', data=day_data)
    plt.title('Hubungan antara Suhu dan Jumlah Peminjaman Sepeda')
    plt.xlabel('Suhu (Normalized)')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(plt)
    plt.clf()  # Clear figure

# Pertanyaan 2: Bagaimana pola penggunaan sepeda berdasarkan hari dalam seminggu?
elif option == "Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu":
    st.header("Pola Penggunaan Sepeda Berdasarkan Hari dalam Seminggu")
    st.write("Visualisasi berikut menunjukkan pola peminjaman sepeda berdasarkan hari dalam seminggu.")

    # Countplot Jumlah Peminjaman Berdasarkan Hari dalam Seminggu
    st.subheader("Jumlah Peminjaman Berdasarkan Hari dalam Seminggu")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='weekday', data=day_data)
    plt.title('Jumlah Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Jumlah Peminjaman')
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot(plt)
    plt.clf()  # Clear figure

    # Line Plot Rata-rata Peminjaman Berdasarkan Hari dalam Seminggu
    st.subheader("Rata-rata Peminjaman Berdasarkan Hari dalam Seminggu")
    plt.figure(figsize=(10, 6))
    average_per_day = day_data.groupby('weekday')['cnt'].mean().reset_index()
    sns.lineplot(x='weekday', y='cnt', data=average_per_day)
    plt.title('Rata-rata Peminjaman Sepeda Berdasarkan Hari dalam Seminggu')
    plt.xlabel('Hari dalam Seminggu')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks([0, 1, 2, 3, 4, 5, 6], ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu'])
    st.pyplot(plt)
    plt.clf()  # Clear figure

# End of dashboard
st.write("---")
st.write("Terima kasih telah menjelajahi Analisis Peminjaman Sepeda!")