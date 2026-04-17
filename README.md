# 📊 End-to-End Sales Analytics
### **Revenue Insights & Customer Segmentation**

---

## 🛠️ Tech Stack
* **Language:** Python (Pandas, NumPy)
* **Database:** SQL (Querying & Aggregations)
* **Visualization:** Power BI
* **Storage:** CSV / Flat Files

---

## 🎯 Objective
This project performs a comprehensive analysis of e-commerce sales data to identify high-value territories and categorize customers based on their spending behavior. By implementing the same logic across **Python** and **SQL**, this project demonstrates cross-functional data processing capabilities and final visualization in **Power BI**.

---

## 🚀 Key Features & Logic

### 1. Customer Segmentation
I implemented a three-tier classification system using `numpy.select` in Python and `CASE WHEN` in SQL:
* **💎 VIP:** Revenue $\ge$ 60,000
* **💳 Regular:** 30,000 $\le$ Revenue $<$ 60,000
* **📉 Low:** Revenue $<$ 30,000

### 2. Revenue Distribution
* Calculated percentage contribution per city to identify market share.
* Automated scripts to extract the highest-grossing customers and cities.

---

## 💡 Key Insights
* 📍 **Top City:** **Mumbai** leads in total revenue generation.
* 👤 **Top Customer:** **Ankit** is the highest contributor and the only **VIP** customer.
* 📈 **Concentration:** Revenue is heavily concentrated among a few high-value customers, suggesting a focus on retention.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `analysis.py` | Python script for data cleaning & segmentation. |
| `queries.sql` | SQL implementation of the business logic. |
| `dashboard.pbix` | Interactive Power BI Report. |
| `sales_data.csv` | The underlying dataset. |

---

## 🛠️ Installation & Usage
1. **Python:** Run `python analysis.py` to generate the processed CSV.
2. **SQL:** Execute `queries.sql` in any standard SQL environment.
3. **Power BI:** Open `dashboard.pbix` to view interactive visualizations.
