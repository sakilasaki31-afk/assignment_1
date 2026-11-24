# 🏠 BrickView: Real Estate Analytics Platform

**Real Estate Analytics | Property Insights | SQL | Python | Streamlit**

## 1. Project Introduction

BrickView is an interactive Real Estate Analytics Platform developed using Python, SQL, Pandas and Streamlit.

The platform analyses real estate property listings, pricing trends, sales performance, agent productivity and buyer behaviour.

It provides an interactive dashboard that helps buyers, sellers, investors and real estate agents make data-driven decisions through data analysis, SQL queries and visualizations.

## 2. Problem Statement

The real estate market is vast and dynamic, with properties being listed, sold and evaluated every day.

Buyers, sellers and agents often lack accessible tools to monitor property trends, pricing, sales performance and market behaviour.

BrickView addresses this problem by developing a Real Estate Listings Dashboard that helps users:

- Analyse property listings, agent performance and sales patterns.
- Understand pricing trends and time on market.
- Compare property types and locations.
- Filter properties based on city, property type, price and sales agent.
- Explore interactive maps, charts and analytical reports.

## 3. Project Objectives

- Collect and process real estate datasets.
- Clean and transform raw JSON and CSV files.
- Create a normalized SQL database.
- Perform SQL-based business analysis.
- Analyse property prices and sales performance.
- Evaluate real estate agent performance.
- Understand buyer and financing behaviour.
- Build an interactive Streamlit dashboard.
- Provide meaningful business insights through visualizations.

## 4. Skills and Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming and data processing |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| SQL | Data querying and analysis |
| SQLite | Database management |
| Streamlit | Interactive dashboard |
| Plotly | Interactive visualizations |
| Matplotlib | Data visualization |
| Seaborn | Statistical analysis |
| Git & GitHub | Version control |

**Domain:** Real Estate, Property Analytics, Urban Development and Location Intelligence.

## 5. Dataset Description

The project uses the following datasets:

| Dataset | Description |
|---|---|
| listings_final_expanded.json | Property listing information |
| property_attributes_final_expanded.json | Property specifications |
| agents_cleaned.json | Real estate agent information |
| sales_cleaned.csv | Property sales information |
| buyers_cleaned.json | Buyer and financing information |

### 5.1 Listings – Property Listings

Contains core property-level information.

- Listing_ID – Unique property listing identifier.
- City – Property location.
- Property_Type – Apartment, Villa, Condo, etc.
- Price – Listed property price.
- Area_sqft – Property area in square feet.
- Agent_ID – Agent reference.
- Listed_Date – Property listing date.
- Latitude – Property latitude.
- Longitude – Property longitude.

### 5.2 Property Attributes

Contains additional property specifications.

- Attribute_ID
- Listing_ID
- Bedrooms
- Bathrooms
- Floor_Number
- Total_Floors
- Year_Built
- Is_Rented
- Tenant_Count
- Furnishing_Status
- Metro_Distance_Km
- Parking_Available
- Power_Backup

### 5.3 Agents – Real Estate Agents

Contains agent information and performance metrics.

- Agent_ID
- Name
- Phone
- Email
- Commission_Rate
- Deals_Closed
- Rating
- Experience_Years
- Avg_Closing_Days

### 5.4 Sales – Property Sales

Contains property transaction information.

- Listing_ID
- Sale_Date
- Sale_Price
- Days_On_Market

### 5.5 Buyers – Buyer Information

Contains buyer and financing details.

- Buyer_ID
- Sale_ID
- Buyer_Type
- Payment_Mode
- Loan_Taken
- Loan_Provider
- Loan_Amount

## 6. Project Approach

### Step 1: Data Preparation

- Read JSON and CSV datasets using Python.
- Flatten nested JSON structures where required.
- Handle missing and duplicate values.
- Standardize date, numeric and boolean fields.
- Ensure consistent price and area values.

### Step 2: Database Creation

- Create an SQLite database.
- Design normalized database tables.
- Establish primary key and foreign key relationships.
- Create SQL views and indexes where required.
- Store cleaned datasets in the database.

### Step 3: SQL Data Analysis

Perform SQL queries to analyse:

- Property pricing trends.
- City-wise property distribution.
- Sales performance.
- Agent productivity.
- Buyer behaviour.
- Loan and payment patterns.

### Step 4: Streamlit Application Development

Develop an interactive dashboard with:

- Dashboard filters.
- Property analytics.
- Interactive charts.
- Location-based maps.
- SQL query results.
- CRUD operations.

### Step 5: Deployment

Deploy the application locally or through Streamlit Community Cloud for stakeholder access.

## 7. Database Architecture

The platform uses an SQL database containing five major tables:

1. Listings
2. Property Attributes
3. Agents
4. Sales
5. Buyers

### Database Relationships

- Listings and Property Attributes: One-to-One.
- Agents and Listings: One-to-Many.
- Listings and Sales: One-to-Zero-or-One, assuming one recorded sale per listing.
- Sales and Buyers: One-to-One or One-to-Many depending on the dataset relationships.

SQL joins are used to combine information across tables for business analysis.

## 8. Key SQL Business Questions

### 8.1 Property and Pricing Analysis

1. What is the average listing price by city?
2. What is the average price per square foot by property type?
3. How does furnishing status impact property prices?
4. Do properties closer to metro stations command higher prices?
5. Are rented properties priced differently from non-rented properties?
6. How do bedrooms and bathrooms affect pricing?
7. Do properties with parking and power backup sell at higher prices?
8. How does year built influence listing price?
9. Which cities have the highest average property prices?
10. How are properties distributed across price ranges?

### 8.2 Sales and Market Performance

1. What is the average days on market by city?
2. Which property types sell the fastest?
3. What percentage of properties are sold above listing price?
4. What is the sale-to-list price ratio by city?
5. Which listings took more than 90 days to sell?
6. How does metro distance affect time on market?
7. What is the monthly sales trend?
8. Which properties are currently unsold?

### 8.3 Agent Performance

1. Which agents have closed the most sales?
2. Who are the top agents by total sales revenue?
3. Which agents close deals fastest?
4. Does experience correlate with deals closed?
5. Do agents with higher ratings close deals faster?
6. What is the average commission earned by each agent?
7. Which agents currently have the most active listings?

### 8.4 Buyer and Financing Behaviour

1. What percentage of buyers are investors versus end users?
2. Which cities have the highest loan uptake rate?
3. What is the average loan amount by buyer type?
4. Which payment mode is most commonly used?
5. Do loan-backed purchases take longer to close?

## 9. Streamlit Dashboard Features

### 9.1 Filters Page

The dashboard provides interactive filters:

- City – Multi-select filter.
- Property Type – Apartment, Villa, Condo, etc.
- Price Range – Minimum and maximum price slider.
- Agent – Searchable agent selection.
- Date Range – Listing date or sale date.

### 9.2 Visualizations Page

The platform includes:

- **Interactive Map:** Property locations using latitude and longitude.
- **Bar Chart:** City-wise property listings and average prices.
- **Pie Chart:** Property type distribution.
- **Line Chart:** Monthly property sales and listing trends.
- **Table View:** SQL query results with sorting and filtering.

### 9.3 CRUD Operations Page

Implement Create, Read, Update and Delete operations for all database tables.

Each table should support:

- View existing records.
- Add new records.
- Update existing records.
- Delete records.

### 9.4 SQL Queries Display Page

Display SQL business queries in expandable sections.

Each section should include:

- Business question.
- SQL query.
- Query output in tabular format.
- Related analytical insights.

## 10. Business Use Cases

BrickView supports different real estate business activities.

**Buyers and Investors**
- Compare property prices across cities.
- Identify potential investment opportunities.
- Understand location-based pricing trends.

**Real Estate Agents**
- Monitor sales performance.
- Track active property listings.
- Evaluate closing time and agent productivity.

**Property Businesses**
- Analyse demand across property types.
- Understand pricing trends.
- Monitor sales performance across regions.

**Urban Development**
- Explore property distribution.
- Analyse proximity to metro stations.
- Understand location-based development patterns.

## 11. Project Deliverables

- Cleaned and processed datasets.
- Normalized SQL database schema.
- 15+ SQL business analysis queries.
- Interactive Streamlit dashboard.
- Property and agent analytics.
- CRUD operations.
- Interactive charts and maps.
- Final project report with business insights and screenshots.

## 12. Project Evaluation Metrics

The project is evaluated based on:

- Proper SQL schema and normalized tables.
- Accuracy of SQL queries and aggregations.
- Quality of Streamlit visualizations.
- Functional filters and interactive features.
- Completeness of CRUD operations.
- User-friendly dashboard navigation.
- Quality of business insights.

## 13. Future Enhancements

- Integrate live real estate listing APIs.
- Add predictive property price modelling.
- Implement advanced location intelligence.
- Develop property recommendation features.
- Add advanced market trend forecasting.
- Deploy the dashboard on a cloud platform.

## 14. Conclusion

BrickView: Real Estate Analytics Platform demonstrates the practical application of Python, SQL, data analysis and Streamlit in the real estate domain.

The project transforms raw property, agent, sales and buyer datasets into meaningful business insights.

By combining database management, SQL analytics and interactive visualizations, BrickView provides a foundation for smarter property analysis and data-driven real estate decision-making.

---

**Developed as a Real Estate Analytics Capstone Project.**

**Technical Tags:** Python | SQL | Streamlit | Pandas | SQLite | Data Analysis | Real Estate Analytics