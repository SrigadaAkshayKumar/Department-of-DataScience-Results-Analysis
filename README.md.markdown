**Department of Data Science Results Analysis Report**

**Introduction**

This report presents an analysis of student performance data to evaluate
trends across different subjects and sections. Key insights include
pass/fail distributions, average scores by subject, and overall
section-wise performance.

**Abstract**

This project is a **Department of Data Science Results Analysis** that
processes student performance data to generate insights on pass/fail
counts by section and subject. The project includes visualizations that
display results breakdown across different sections, helping in
analyzing academic performance trends and identifying areas of
improvement.

**Features**

- **Section-wise Pass/Fail Analysis**: Visualizes the number of
  students who passed or failed in each subject, separated by section.

- **Subject-wise Performance Comparison**: Compares performance
  metrics across subjects to give a clear view of student strengths
  and weaknesses.

- **Data Cleaning & Transformation**: Prepares raw data by handling
  missing values and converting data types as needed.

- **Interactive Data Visualization**: Generates visual charts (bar
  plots) to illustrate performance statistics.

**Dataset**

The dataset includes columns such as:

- Roll Number, Name, Section

- Subject names (e.g., BEFA, DM, OS, DBMS, DPA) with corresponding
  status columns (Befa_Status, Dm_Status, etc.)

- Total_Marks, SGPA, CGPA, Subjects_due

**Abbreviations:**

BEFA - Business Economics and Financial Analysis

DM - Discrete Mathematics

OS - Operating Systems

DBMS - Database Management Systems

DPA - Data Preparation and Analysis

ES - Environmental Science

SD-Lab - Skill Development Lab

**Project Structure**

- **data.csv**: Contains the student performance data used in this
  analysis.

- **DataScience-Results-Analysis.ipynb**: Jupyter Notebook with data
  processing, analysis, and visualization code.

- **app.py**: Contains the Selenium code for Data Scraping

**Insights and Findings**

**1. Subject-Wise Average Marks**

**Insight:** Subjects such as \`OS-Lab\`, \`DBMS-Lab\`, and \`SD-Lab\`
have higher average marks

compared to theory subjects like \`DM\` and \`DBMS\`.
![](media/image1.emf){width="6.268055555555556in"
height="3.3986111111111112in"}

**2. Subject-Wise Pass/Fail Counts**

**Insight:** Higher pass percentages were observed in subjects like
\`DPA\` and \`BEFA\`, while \`DM\` had a lower pass percentage.

![](media/image2.emf){width="6.268055555555556in"
height="3.158333333333333in"}

**3. Section-Wise Pass/Fail Counts**

**Insight:** Sections like 'A' and 'C' has high and equal no. of
students passed and the 'B' section has the high inn no. of students
failed

![](media/image3.emf){width="6.268055555555556in"
height="3.439583333333333in"}

**4. Subject-Wise Pass/Fail Counts - Section-Wise**

**Insight:** Higher pass percentages were observed in subjects like
\`DPA\` and \`BEFA\`, while \`DM\` had a lower pass percentage in each
Section.

![](media/image4.png){width="6.268055555555556in"
height="2.8506944444444446in"}

![](media/image5.emf){width="6.268055555555556in"
height="2.8in"}

![](media/image6.emf){width="6.268055555555556in"
height="2.841666666666667in"}

**5. Top 10 Students by CGPA and SGPA**

**Insight:** Students with high SGPA and CGPA tend to have consistently
strong marks across multiple subjects.

- **Top 10 Students by SGPA**

![](media/image7.png){width="6.268055555555556in"
height="3.8583333333333334in"}

- **Top 10 Students by CGPA**

![](media/image8.png){width="6.268055555555556in"
height="4.058333333333334in"}

**6. Section-Wise Pass Percentage**

**Insight:** Section \`A\` had a slightly Higher pass rate while Section
\`B\` had a slightly lower pass rate than Sections \`A\` and \`C\`, with
room for improvement in theoretical subjects.

![](media/image9.emf){width="4.3590277777777775in"
height="3.216666666666667in"}

**7. Subject wise pass percentage**

![](media/image10.emf){width="6.268055555555556in"
height="2.8402777777777777in"}

**8. Section-wise Analysis of Detained Students**

**Insight**: Section A has higher detention rate

![](media/image11.png){width="2.5833333333333335in"
height="1.3666666666666667in"}
