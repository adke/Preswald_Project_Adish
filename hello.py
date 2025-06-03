from preswald import connect, get_df, table, text, plotly, query

import plotly.express as px
import matplotlib.pyplot as plt

connect()  # Initialize connection to preswald.toml data sources
df = get_df("used_cars_data")  # Load data

sql = "SELECT * FROM used_cars_data WHERE year = 2010"
filtered_df = query(sql, "used_cars_data")

text("# Adish's Used Cars Project")
table(filtered_df, title="Cars from 2010")

# For matplotlib plots in preswald, use the plotly() function instead of plt.show()
plt.figure(figsize=(10, 10))
plt.scatter(filtered_df["KILOMETERS_DRIVEN"], filtered_df["PRICE"], alpha=0.7, color='blue')
plt.title("Kilometers Driven vs Price (2010 Cars)")
plt.xlabel("Kilometers Driven")
plt.ylabel("Price (₹ Lakhs)")
plt.grid(True)
plt.tight_layout()
plt.show()

fig = px.scatter(df, x="YEAR", y="PRICE", color="TRANSMISSION")
plotly(fig)
