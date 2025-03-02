# 🏨 **ETL & Data Analysis of Hotel Reservations**

This project is focused on extracting, transforming, and loading (ETL) hotel reservation data, followed by exploratory data analysis to generate valuable insights. The dataset includes information about customers, hotels, reservations, and pricing. 


## 📚 **Project Description**  
The goal of this project is to analyze hotel reservation data to identify patterns in customer behavior, hotel performance, and revenue trends. The project goals includes:  
- Cleaning and transforming raw data from different sources.
- Extract data from Madrid Community APIs to analyze whether events had an impact on reservations.
- Standardization and unification of various files: raw files, transformed files, and files generated with new value.
- Storing structured data in a PostgreSQL database.  
- Running SQL queries to extract key insights.  
- Performing exploratory data analysis (EDA) and visualization.  

## 🗂️ **Project Structure**  

```
├── data/                 # Raw and processed data files  
├── env/                  # Virtual environment files  
├── jupyters/             # Jupyter notebooks for data processing and analysis  
├── src/                  # Python scripts for ETL and data modeling  
├── README.md             # Project documentation  
```

## 🛠️ **Installation & Requirements**  

To run this project, you need Python 3.8+ and the following libraries:  

```
- pandas  
- numpy  
- psycopg2  
- matplotlib  
- seaborn  
```

To install dependencies, run:  
```bash
pip install -r requirements.txt
```

## 🔍 **Key Insights & Results**  

- **Total Hotels:** Querying the database revealed the number of hotels available.  
- **Total Reservations:** Analyzed the number of reservations made over a period of time.  
- **Top Spending Customers:** Identified the top 10 customers who spent the most.  
- **Revenue Analysis:** Compared the revenue of competitor hotels vs. our brand.  
- **Peak Events:** Determined importance of events in the number of reservations.  

## 🛠 **Next Steps**  

- Enhance the ETL pipeline with more data sources.  
- Apply machine learning models for revenue prediction.  
- Integrate external factors (e.g., holidays, promotions) for deeper insights.  

## 🤝 **Contributing**  
Contributions are welcome! Feel free to open an issue or submit a pull request.  

## ✏️ **Authors**  
- **Marta Blanco Arévalo** – Data Analyst & Python Developer  



