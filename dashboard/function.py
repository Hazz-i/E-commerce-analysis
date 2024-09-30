import pandas as pd
import numpy as np
import os

path = os.path.dirname(__file__)
all_df = pd.read_csv(os.path.join(path + '/', 'clean_data.csv'))
datetime_columns = ["order_approved_at", "order_delivered_customer_date"]
all_df.sort_values(by="order_approved_at", inplace=True)
all_df.reset_index(inplace=True)

def bystate_customer_df(df):
    bystate_customer_df = df.groupby(by="customer_city").agg({
        "order_id": "nunique",
        "payment_value": "sum",
        "product_name": pd.Series.mode
    }).nlargest(10, "order_id").reset_index()
    bystate_customer_df.rename(columns={
        "order_id": "customer_count"
    }, inplace=True)

    return bystate_customer_df

def bystate_seller_df(df):
    bystate_seller_df = df.groupby(by="seller_city").agg({
        "order_id": "nunique",
        "payment_value": "sum",
        "product_name": pd.Series.mode
    }).nlargest(10, "order_id").reset_index()
    bystate_seller_df.rename(columns={
        "order_id": "seller_count"
    }, inplace=True)

    return bystate_seller_df

def recency (df):
    frequency_df = df.groupby(by='customer_id',as_index=False)['order_approved_at'].max()
    frequency_df.columns = ['CustomerId', 'LastPurchaseDate']
    recent_date = frequency_df['LastPurchaseDate'].max()
    frequency_df['Recency'] = frequency_df['LastPurchaseDate'].apply(lambda x: (recent_date - x).days)
    return frequency_df

def frequency (df):
    frequency_df = df.drop_duplicates().groupby(
        by=['customer_id'], as_index=False)['order_approved_at'].count()
    frequency_df.columns = ['CustomerId', 'Frequency']
    return frequency_df


def monetary(df):
    monetary_df = df.groupby(by='customer_id', as_index=False)['payment_value'].sum()
    monetary_df.columns = ['CustomerId', 'Monetary']
    return monetary_df

def rfm (recency, frequency, monetary) :
    rf_df = recency.merge(frequency, on='CustomerId')
    rfm_df = rf_df.merge(monetary, on='CustomerId').drop(
        columns='LastPurchaseDate')

    rfm_df['R_rank'] = rfm_df['Recency'].rank(ascending=False)
    rfm_df['F_rank'] = rfm_df['Frequency'].rank(ascending=True)
    rfm_df['M_rank'] = rfm_df['Monetary'].rank(ascending=True)
    
    # normalizing the rank of the customers
    rfm_df['R_rank_norm'] = (rfm_df['R_rank']/rfm_df['R_rank'].max())*100
    rfm_df['F_rank_norm'] = (rfm_df['F_rank']/rfm_df['F_rank'].max())*100
    rfm_df['M_rank_norm'] = (rfm_df['F_rank']/rfm_df['M_rank'].max())*100
    rfm_df.drop(columns=['R_rank', 'F_rank', 'M_rank'], inplace=True)


    rfm_df['RFM_Score'] = 0.15*rfm_df['R_rank_norm']+0.28 * \
        rfm_df['F_rank_norm']+0.57*rfm_df['M_rank_norm']
    rfm_df['RFM_Score'] *= 0.05
    rfm_df = rfm_df.round(2)

    rfm_df["Customer_segment"] = np.where(rfm_df['RFM_Score'] > 4.5, "Top Customers",
                                (np.where(rfm_df['RFM_Score'] > 4,"High value Customer",
                                (np.where(rfm_df['RFM_Score'] > 3,"Medium Value Customer",
                                np.where(rfm_df['RFM_Score'] > 1.6,'Low Value Customers', 'Lost Customers'))))))
    return rfm_df

def tingkat_penjualan_2016(df):
    df_tingkat_penjualan_2016 = all_df[all_df.order_year == 2016]

    tingkat_penjualan_2016 = df_tingkat_penjualan_2016.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2016

def tingkat_penjualan_2017(df):
    df_tingkat_penjualan_2017 = all_df[all_df.order_year == 2017]

    tingkat_penjualan_2017 = df_tingkat_penjualan_2017.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2017

def tingkat_penjualan_2018(df):
    df_tingkat_penjualan_2018 = all_df[all_df.order_year == 2018]

    tingkat_penjualan_2018 = df_tingkat_penjualan_2018.groupby(by='order_month').agg({
        "order_id": "nunique",
        "order_month_name" : pd.Series.mode,
        "payment_value" : "sum"
    }).sort_values(by="order_month").reset_index()
    
    return tingkat_penjualan_2018
