import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Online Food Delivery Dashboard",
    layout="wide"
)

st.title("🍔 Online Food Delivery – Business Dashboard")

# --------------------------------------------------
# Load Data
# --------------------------------------------------
DATA_PATH = r"C:\Users\Admin\OneDrive\Desktop\Online_Food_Delivery_Data_Analysis\data\raw\online_food_delivery_final.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# --------------------------------------------------
# Sidebar Filters
# --------------------------------------------------
st.sidebar.header("🔍 Filters")

city = st.sidebar.multiselect(
    "City",
    options=sorted(df["City"].dropna().unique()),
    default=sorted(df["City"].dropna().unique())
)

cuisine = st.sidebar.multiselect(
    "Cuisine",
    options=sorted(df["Cuisine_Type"].dropna().unique()),
    default=sorted(df["Cuisine_Type"].dropna().unique())
)

status = st.sidebar.multiselect(
    "Order Status",
    options=df["Order_Status"].unique(),
    default=df["Order_Status"].unique()
)

filtered_df = df[
    (df["City"].isin(city)) &
    (df["Cuisine_Type"].isin(cuisine)) &
    (df["Order_Status"].isin(status))
]

# --------------------------------------------------
# CSV DOWNLOAD BUTTON (MERGED HERE)
# --------------------------------------------------
st.sidebar.markdown("### ⬇️ Download Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.sidebar.download_button(
    label="Download filtered data as CSV",
    data=csv_data,
    file_name="food_delivery_dashboard_data.csv",
    mime="text/csv"
)

# --------------------------------------------------
# Handle Empty Data
# --------------------------------------------------
if filtered_df.empty:
    st.warning("⚠️ No data available for the selected filters. Please adjust the filters.")
    st.stop()

# --------------------------------------------------
# KPIs
# --------------------------------------------------
st.subheader("📊 Key Metrics")

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric("Total Orders", len(filtered_df))
c2.metric("Total Revenue", f"₹ {filtered_df['Final_Amount'].sum():,.0f}")
c3.metric("Avg Order Value", f"₹ {filtered_df['Order_Value'].mean():.0f}")
c4.metric("Avg Delivery Time", f"{filtered_df['Delivery_Time_Min'].mean():.1f} min")
c5.metric(
    "Cancellation Rate",
    f"{(filtered_df['Order_Status'] == 'cancelled').mean() * 100:.2f}%"
)

# --------------------------------------------------
# Charts
# --------------------------------------------------
st.subheader("📈 Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Orders by City**")
    fig, ax = plt.subplots()
    filtered_df["City"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("City")
    ax.set_ylabel("Orders")
    st.pyplot(fig)

with col2:
    st.markdown("**Revenue by Cuisine**")
    fig, ax = plt.subplots()
    filtered_df.groupby("Cuisine_Type")["Final_Amount"].sum().plot(kind="bar", ax=ax)
    ax.set_xlabel("Cuisine")
    ax.set_ylabel("Revenue")
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.markdown("**Delivery Performance**")
    fig, ax = plt.subplots()
    filtered_df["Delivery_Performance"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("Performance")
    ax.set_ylabel("Orders")
    st.pyplot(fig)

with col4:
    st.markdown("**Payment Mode Preference**")
    fig, ax = plt.subplots()
    filtered_df["Payment_Mode"].value_counts().plot(kind="bar", ax=ax)
    ax.set_xlabel("Payment Mode")
    ax.set_ylabel("Orders")
    st.pyplot(fig)

st.success("✅ Dashboard loaded successfully")
