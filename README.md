# Department of DataScience-Results-Analysis

This project is a **Department of Data Science Results Analysis Tool** that processes student performance data to generate insights on pass/fail counts by section and subject. The project includes visualizations that display results breakdown across different sections, helping in analyzing academic performance trends and identifying areas of improvement.

## Features

- **Section-wise Pass/Fail Analysis**: Visualizes the number of students who passed or failed in each subject, separated by section.
- **Subject-wise Performance Comparison**: Compares performance metrics across subjects to give a clear view of student strengths and weaknesses.
- **Data Cleaning & Transformation**: Prepares raw data by handling missing values and converting data types as needed.
- **Interactive Data Visualization**: Generates visual charts (bar plots) to illustrate performance statistics.

## Dataset

The dataset includes columns such as:
- `Roll Number`, `Name`, `Section`
- Subject names (e.g., `BEFA`, `DM`, `OS`, `DBMS`, `DPA`) with corresponding status columns (`Befa_Status`, `Dm_Status`, etc.)
- `Total_Marks`, `SGPA`, `CGPA`, `Subjects_due`

### BEFA - Business Economics and Financial Analysis
### DM - Discrete Mathematics
### OS - Operating Systems
### DBMS - Database Management Systems
### DPA - Data Preparation and Analysis
### ES - Environmental Science
### SD-Lab - Skill Development Lab

This dataset allows for detailed analysis of student performance across various metrics.

## Project Structure

- **data.csv**: Contains the student performance data used in this analysis.
- **DataScience-Results-Analysis.ipynb**: Jupyter Notebook with data processing, analysis, and visualization code.
- **appp.py**:Contains the Selenium code for Data Scraping 

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SrigadaAkshayKumar/DataScience-Results-Analysis.git
   cd DataScience-Results-Analysis
