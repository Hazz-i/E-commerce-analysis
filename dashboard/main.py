import os
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from babel.numbers import format_currency
from function import bystate_customer_df, recency, frequency, monetary, rfm, tingkat_penjualan_2016, tingkat_penjualan_2017, tingkat_penjualan_2018

# read dataset
path = os.path.dirname(__file__)
all_df = pd.read_csv(os.path.join(path + '/', 'clean_data.csv'))
datetime_columns = ["order_approved_at", "order_delivered_customer_date"]
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

datetime_columns = ["order_approved_at","order_delivered_carrier_date",'order_delivered_customer_date','order_estimated_delivery_date' ]
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])
    all_df[column] = all_df[column].dt.date
    all_df[column] = pd.to_datetime(all_df[column])

st.title("Tingkat penjualan dalam beberapa tahun terakhir")

t1, t2, t3 = st.tabs(["Tahun 2016", "Tahun 2017", "Tahun 2018"])
with t1:
    tingkat_penjualan_2016 = tingkat_penjualan_2016(all_df)
    col1, col2 = st.columns(2)

    with col1:
        total_orders = tingkat_penjualan_2016.order_id.sum()
        st.metric("Total orders", value=total_orders)

    with col2:
        total_revenue = format_currency(tingkat_penjualan_2016.payment_value.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)

    # Create the plot using plt
    with st.container():
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(tingkat_penjualan_2016["order_month_name"], tingkat_penjualan_2016["order_id"], marker='o', color='red', linestyle='-', linewidth=2)

        # Add annotations
        for x, y in zip(tingkat_penjualan_2016["order_month_name"], tingkat_penjualan_2016["order_id"]):
            ax.annotate(str(y), xy=(x, y + 15), ha='center', fontsize=12)

        ax.set_title('Sales Performance 2016', fontsize=14)
        ax.set_xlabel('Order Month', fontsize=12)
        ax.set_ylabel('Number of orders', fontsize=12)

        # Display the chart
        st.pyplot(fig)

    # Expander for interpretations
    with st.expander("Interpretasi", expanded=False):
        st.write("Tingkat penjualan di tahun 2016 tidak dapat diamati dengan baik dikarenakan ketidaklengkapan data yang ada. Yaitu hanya terdapat 1 transaksi pada bulan Desember 2016.")
        
    with st.expander("Saran", expanded=False):
        st.write("Mengumpulkan data yang Lebih Komprehensif: Sebaiknya dipastikan untuk mengumpulkan data penjualan yang lebih lengkap dan komprehensif di masa mendatang. Hal ini dapat dilakukan dengan merekam setiap transaksi penjualan dengan lebih baik. Dengan data yang lengkap, maka dapat dilakukan identifikasi produk yang memiliki tingkat penjualan secara lebih akurat.")


with t2:
    tingkat_penjualan_2017 = tingkat_penjualan_2017(all_df)
    col1, col2 = st.columns(2)

    with col1:
        total_orders = tingkat_penjualan_2017.order_id.sum()
        st.metric("Total orders", value=total_orders)

    with col2:
        total_revenue = format_currency(tingkat_penjualan_2017.payment_value.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)

    # Create the plot using plt
    with st.container():
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(tingkat_penjualan_2017["order_month_name"], tingkat_penjualan_2017["order_id"], marker='o', color='red', linestyle='-', linewidth=2)

        # Add annotations
        for x, y in zip(tingkat_penjualan_2017["order_month_name"], tingkat_penjualan_2017["order_id"]):
            ax.annotate(str(y), xy=(x, y + 150), ha='center', fontsize=12)

        ax.set_title('Sales Performance 2017', fontsize=14)
        ax.set_xlabel('Order Month', fontsize=12)
        ax.set_ylabel('Number of orders', fontsize=12)

        # Display the chart
        ax.tick_params(axis='x', rotation=45)
        st.pyplot(fig)

    # Expander for interpretations
    with st.expander("Interpretasi", expanded=False):
        st.write("Tingkat penjualan pada tahun 2018 menunjukan tren pertumbuhan yang baik hingga akhir tahun. Bulan november merupakan bulan yang memiliki jumlah transaksi tertinggi yaitu sebesar 7146 transaksi dengan total penjualan selama 1 tahun sebesar 43352 dan total pemasukan dari keseluruhan transaksi sebesar 8 juta USD atau sekitar 121 milyar rupiah.")
        
    with st.expander("Saran", expanded=False):
        st.write("- Memanfaatkan Tren Pertumbuhan:")
        st.write("  Memanfaatkan adanya tren pertumbuhan yang baik pada tahun 2017 untuk meningkatkan penjualan di tahun-tahun berikutnya dengan mengidentifikasi faktor-faktor yang berkontribusi terhadap peningkatan penjualan pada bulan November, seperti promosi khusus, produk yang populer, atau strategi pemasaran yang efektif.")
        st.write("- Analisis Bulan November:")
        st.write("  meneliti dengan lebih mendalam mengapa bulan November memiliki jumlah transaksi tertinggi. Apakah ada peristiwa khusus, seperti liburan atau acara penjualan besar, yang mendorong pertumbuhan tersebut. Analisis ini dapat membantu untuk merencanakan kegiatan promosi atau penjualan yang serupa di masa depan.")

with t3:
    tingkat_penjualan_2018 = tingkat_penjualan_2018(all_df)
    col1, col2 = st.columns(2)

    with col1:
        total_orders = tingkat_penjualan_2018.order_id.sum()
        st.metric("Total orders", value=total_orders)

    with col2:
        total_revenue = format_currency(tingkat_penjualan_2018.payment_value.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)

    # Create the plot using plt
    with st.container():
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(tingkat_penjualan_2018["order_month_name"], tingkat_penjualan_2018["order_id"], marker='o', color='red', linestyle='-', linewidth=2)

        # Add annotations
        for x, y in zip(tingkat_penjualan_2018["order_month_name"], tingkat_penjualan_2018["order_id"]):
            ax.annotate(str(y), xy=(x, y + 150), ha='center', fontsize=12)

        ax.set_title('Sales Performance 2017', fontsize=14)
        ax.set_xlabel('Order Month', fontsize=12)
        ax.set_ylabel('Number of orders', fontsize=12)

        # Display the chart
        st.pyplot(fig)
    
        with st.expander("Interpretasi", expanded=False):

            # Konten expander
            st.write("Tingkat penjualan pada tahun 2018 menujukan tren yang cukup stagnan dan cenderung turun dengan bulan maret menjadi bulan yang memiliki jumlah transaksi tertinggi yaitu sebesar 7085 transaksi.dengan total penjualan selama 1 tahun sebesar 52859 dan total pemasukan dari keseluruhan transaksi sebesar 10 juta USD atau sekitar 151 milyar rupiah.")
        
        with st.expander("Saran", expanded=False):

            # Konten expander
            st.write("- Identifikasi Penyebab Stagnansi dan Penurunan: ")
            st.write("  Meneliti dengan lebih mendalam untuk mengidentifikasi faktor-faktor yang menyebabkan penurunan dan stagnannya tingkat penjualan. Meninjau faktor-faktor internal dan eksternal yang mungkin berperan, seperti perubahan preferensi pelanggan, persaingan yang meningkat, perubahan tren pasar, atau perubahan dalam strategi pemasaran.")


st.title("Pesebaran daerah tempat pelanggan yang melakukan transaksi 2016 - 2018")
bystate_customer_df = bystate_customer_df(all_df)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(bystate_customer_df['customer_city'], bystate_customer_df['customer_count'], color=["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"])

ax.set_xlabel('Customer Count')
ax.set_title('Number of Customers by City')

for bar in bars:
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height() / 2, f'{width}', va='center')

st.pyplot(fig)

with st.expander("Interpretation", expanded=False):
    st.write("Jumlah pelanggan berdasarkan wilayah:")
    st.write("- Sao Bernando Campo memiliki pelanggan terendah dari 10 wilayah, dengan jumlah 907 jiwa")
    st.write("- Sao Paulo memiliki pelanggan tertinggi dari 10 wilayah, dengan jumlah 15045 jiwa")

with st.expander("Saran", expanded=False):
    st.write("Mengembangkan Pasar di Daerah Dengan Pelanggan Yang Tinggi dan Penawaran Promo Khusus Daerah Dengan Pelanggan yang Rendah.")

st.title("Customer Segmentation Over 2016 - 2018")

tab1, tab2 = st.tabs(["RFM Analysis", "Customer Segmentation Analysis"])

with tab1:
    recency = recency(all_df)
    frequency = frequency(all_df)
    monetary = monetary(all_df)
    rfm_df = rfm(recency, frequency, monetary)
    displayed_df = rfm_df[['CustomerId', 'Recency', 'Frequency', 'Monetary', 'RFM_Score', 'Customer_segment']].head(5)
    segment_counts = rfm_df['Customer_segment'].value_counts()

    st.write("**Customer RFM Analysis**")
    st.table(displayed_df)

with tab2:
    # Define a pastel color palette
    color_palette = ['#B7D7D8', '#F3B1B3', '#B5B8C3', '#F9D9B4']

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(7, 5))

    # Create the pie chart with labels, percentage, and colors
    wedges, texts, autotexts = ax.pie(
        segment_counts.values, 
        labels=segment_counts.index, 
        autopct='%1.1f%%',  # Display percentages
        colors=color_palette,
        startangle=50,  # Start pie chart from the top
        textprops=dict(color="black", fontsize=7),  # Text font size and color
        wedgeprops=dict(width=0.3, edgecolor='black')  # Adjust wedge width and border
    )

    # Set the title
    ax.set_title('Customer Segmentation', fontsize=16)

    # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.axis('equal')
    st.pyplot(fig)

with st.expander("Interpretasi", expanded=False):
    st.write("Sebagian besar pelanggan adalah pelanggan dengan indeks 'Low Value Customer' yang berarti ia memiliki nilai RFM score dibawah 1.6 yang bisa dibilang sangat rendah. Hal tersebut disebabkan kaarena banyak sekali customer yang hanya melakukan transaksi sebanyak 1 kali dan tidak pernah melakukan transaksi lagi selama rentang tahun 2016 - 2018.")

with st.expander("Saran", expanded=False):
    st.write("Fokus Meminimalkan Tingkat Retensi Pelanggan dengan Memberikan Reward Kepada 'High Value Customer' dan 'Top Customer'.")