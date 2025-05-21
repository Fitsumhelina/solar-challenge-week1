import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Streamlit config
st.set_page_config(page_title="Solar Data Dashboard", layout="wide")
st.title("🔆 Cross-Country Solar Energy Dashboard")

# Load Data
@st.cache_data
def load_data():
    benin = pd.read_csv("data/benin_clean.csv")
    togo = pd.read_csv("data/togo_clean.csv")
    sl = pd.read_csv("data/sierra_leone_clean.csv")
    benin["country"] = "Benin"
    togo["country"] = "Togo"
    sl["country"] = "Sierra Leone"
    return pd.concat([benin, togo, sl], ignore_index=True)

df_all = load_data()

# Sidebar: Country selection
countries = df_all["country"].unique().tolist()
selected_country = st.sidebar.selectbox("Select Country", countries)

df_selected = df_all[df_all["country"] == selected_country]

# KPIs
st.subheader(f"📈 Summary Stats: {selected_country}")
st.write(df_selected[["GHI", "DNI", "DHI"]].describe())

# Boxplots for Irradiance
st.subheader("🧪 Irradiance Distribution (Boxplots)")
fig, axs = plt.subplots(1, 3, figsize=(18, 5))
sns.boxplot(data=df_all, x="country", y="GHI", ax=axs[0])
axs[0].set_title("GHI")
sns.boxplot(data=df_all, x="country", y="DNI", ax=axs[1])
axs[1].set_title("DNI")
sns.boxplot(data=df_all, x="country", y="DHI", ax=axs[2])
axs[2].set_title("DHI")
st.pyplot(fig)

# Ranking Bar Chart
st.subheader("🏆 Country Ranking by Average GHI")
avg_ghi = df_all.groupby("country")["GHI"].mean().sort_values(ascending=False)
st.bar_chart(avg_ghi)

# Display Data
with st.expander("📂 View Raw Data"):
    st.dataframe(df_selected)

st.markdown("---")
st.caption("Built with ❤️ for 10 Academy – Fitsum Helina")
    