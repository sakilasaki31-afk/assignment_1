import streamlit as st
from db import run_query, create_tables
create_tables()

st.set_page_config(page_title="BrickView", page_icon="🏙️", layout="wide")

st.title("🏙️ BrickView: Real Estate Analytics")
st.caption("Explore property listings, pricing, agent performance and sales trends.")

kpi = run_query("""
SELECT
  (SELECT COUNT(*) FROM listings)                 AS total_listings,
  (SELECT COUNT(*) FROM sales)                    AS total_sold,
  (SELECT ROUND(AVG(price), 0) FROM listings)     AS avg_price,
  (SELECT ROUND(AVG(days_on_market), 1) FROM sales) AS avg_days,
  (SELECT COUNT(*) FROM agents)                   AS total_agents
""").iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Listings", f"{int(kpi.total_listings):,}")
c2.metric("Properties Sold", f"{int(kpi.total_sold):,}")
c3.metric("Avg Listing Price", f"₹{kpi.avg_price or 0:,.0f}")
c4.metric("Avg Days on Market", kpi.avg_days or 0)
c5.metric("Agents", int(kpi.total_agents))

st.divider()
st.subheader("Use the sidebar to navigate")
st.markdown("""
- 🔎 *Filters*: search listings by city, type, price, agent and date
- 📈 *Visualizations*: map, price by city, property types, monthly trend
- 🛠️ *CRUD*: view, add, update and delete records
- 🧮 *SQL Queries*: 30 business questions with their SQL and results
""")

st.subheader("Recent Listings")

st.dataframe(
    run_query("SELECT * FROM listings ORDER BY listing_date DESC LIMIT 10"),
    use_container_width=True
)