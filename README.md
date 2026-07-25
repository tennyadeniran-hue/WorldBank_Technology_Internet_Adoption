# 🌍 Global Technology & Internet Adoption Analysis (2000--2024)

## 📌 Project Overview

This project analyses global technology and internet adoption using the
**World Bank World Development Indicators (WDI)** dataset from **2000 to
2024**.

The project was completed as the **Week 8 Data Analytics Capstone
Project** for the AnalystLab Africa Data Analytics Internship.

The analysis focuses on digital connectivity indicators and explores how
internet adoption differs across countries, regions, and income groups.

## 🎯 Project Objective

The main objective is to analyse global technology adoption patterns and
communicate the findings through an interactive Power BI dashboard.

The project examines: - How internet adoption changed globally between
2000 and 2024. - Which countries have the highest internet usage. - How
internet adoption differs across regions. - How mobile and fixed
broadband subscriptions compare with internet usage. - How digital
connectivity varies by income group.

## 📊 Dataset

**Source:** World Bank World Development Indicators (WDI)

The original dataset contained **396,970 rows and 70 columns**.

The analysis focused on 2000--2024 and selected: 1. Individuals using
the Internet (% of population) 2. Mobile cellular subscriptions (per 100
people) 3. Fixed broadband subscriptions (per 100 people) 4. Secure
Internet servers (per 1 million people) 5. GDP per capita (current US\$)
6. Population, total

Country metadata including **Region** and **Income Group** was also
incorporated.

## 🧹 Data Cleaning & Transformation

Python and Pandas were used to: 1. Explore the original WDI dataset. 2.
Select relevant indicators. 3. Filter the analysis period to 2000--2024.
4. Reshape the data from wide to long format. 5. Handle missing
observations. 6. Remove aggregate regional/income-group observations. 7.
Add Region and Income Group classifications. 8. Prepare the final
dataset for Power BI.

### Dataset progression

  Stage                                       Rows   Columns
  -------------------------------------- --------- ---------
  Original WDI dataset                     396,970        70
  Filtered dataset                           1,590        70
  Cleaned long-format dataset               33,810         6
  Final enriched dataset                    33,810         8
  Final country-level analysis dataset      28,082         8

### Final dataset columns

-   Country Name
-   Country Code
-   Indicator Name
-   Indicator Code
-   Year
-   Value
-   Region
-   Income Group

## 📈 Power BI Dashboard

**Global Technology & Internet Adoption Dashboard (2000--2024)**

### KPI Cards

-   Number of Countries
-   Average Internet Usage (%)
-   Average Mobile Subscriptions
-   Average Broadband Subscriptions

### Visualisations

-   Internet Adoption Trend (2000--2024)
-   Global Internet Usage Map (2024)
-   Top 10 Countries by Internet Usage
-   Average Internet Usage by Region (2024)

### Interactive Filters

-   Year
-   Region
-   Income Group

## 🔎 Key Findings

-   Global internet adoption increased substantially between 2000 and
    2024.
-   The dashboard covers **217 countries** in the final country-level
    view.
-   The dashboard reports approximately **40.0% average internet
    usage**, **81.2 mobile subscriptions per 100 people**, and **11.6
    fixed broadband subscriptions per 100 people** across the selected
    data.
-   Internet adoption varies considerably between countries and regions.
-   Mobile connectivity is substantially more widespread than fixed
    broadband connectivity in the overall dataset.
-   Regional and income-group filters reveal important differences in
    digital adoption.

> Dashboard averages can change when users apply different slicer
> selections.

## 💡 Insights

Digital connectivity has expanded significantly over the past two
decades, but growth has not eliminated the global digital divide.

The difference between mobile subscriptions, fixed broadband
subscriptions, and internet usage suggests that countries can experience
digital development through different infrastructure pathways.

## 📌 Recommendations

1.  Expand affordable and reliable broadband infrastructure in
    underserved areas.
2.  Reduce affordability barriers associated with internet services and
    digital devices.
3.  Prioritise regions and communities with lower levels of digital
    connectivity.
4.  Invest in digital literacy and skills programmes.
5.  Continue monitoring digital adoption using country- and region-level
    indicators.
6.  Strengthen secure and resilient digital infrastructure.
7.  Use data-driven dashboards to support digital inclusion policies and
    investment decisions.

## 🛠️ Tools & Technologies

-   Python
-   Pandas
-   Power BI
-   Power Query
-   Microsoft Excel / CSV
-   World Bank World Development Indicators

## 📁 Repository Structure

``` text
WorldBank_Capstone_Project/
│
├── Data/
│   ├── final_wdi_dashboard.csv
│   └── cleaned_wdi.csv
│
├── Python/
│   └── worldbank_analysis.py
│
├── PowerBI/
│   └── WorldBank_Technology_Adoption.pbix
│
├── Images/
│   └── dashboard.png
│
├── Report/
│   └── WorldBank_Technology_Internet_Adoption_Capstone_Report.docx
│
└── README.md
```

### Recommended uploads

-   **Data/** --- final analysis dataset; the original WDI download is
    optional because of its size.
-   **Python/** --- final Python analysis/cleaning script.
-   **PowerBI/** --- completed `.pbix` file.
-   **Images/** --- dashboard screenshot.
-   **Report/** --- final report.
-   **README.md** --- this documentation.

## 🚀 How to Use

1.  Download or clone the repository.
2.  Review the final dataset.
3.  Open `Python/worldbank_analysis.py` to review the data preparation
    workflow.
4.  Open `PowerBI/WorldBank_Technology_Adoption.pbix` in Power BI
    Desktop.
5.  Explore the dashboard using the Year, Region, and Income Group
    filters.

## 📷 Dashboard Preview

Add the completed dashboard screenshot to `Images/dashboard.png`, then
add:

``` markdown
![Global Technology & Internet Adoption Dashboard](Images/dashboard.png)
```

## 📚 Data Source

World Bank --- World Development Indicators (WDI)

https://datatopics.worldbank.org/world-development-indicators/

## 👩‍💻 Project Author

**Teniola Adeniran**

Data Analytics Capstone Project\
AnalystLab Africa --- Batch B\
June--August 2026

## 📄 Project Status

**Completed ✅**

The project includes data preparation, analysis, interactive Power BI
visualisation, documentation, and recommendations.
