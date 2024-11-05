import os
import string  # Import the string module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Set up paths (replace with your actual paths)
brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
driver_path = r'C:\ML-projects\results\chromedriver.exe'
excel_file = 'student.xlsx'

# WebDriver setup
chrome_options = Options()
chrome_options.binary_location = brave_path
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open results page
print("Opening results page...")
driver.get("https://mrecresults.mrecexams.com/StudentResult/Index?Id=494&ex76brs22fbmm=35AAH3e5Ax3zN6wPvt")

# Generate roll numbers
def generate_roll_numbers():
    roll_numbers = []
    prefixes = ['J41A67']

    # Generate numbers from 01 to 99
    for i in range(1, 100):
        roll_number = f"22{prefixes[0]}{i:02}"
        roll_numbers.append(roll_number)

    # # Generate alphanumeric roll numbers a0 to k3
    for letter in string.ascii_uppercase[0:11]:  # Assuming a0 to k3 corresponds to a to k
        if letter == 'I':  # Skip the 'i' series
            continue
        for digit in range(0, 10):  # 0 to 9
            roll_number = f"22{prefixes[0]}{letter}{digit}"
            roll_numbers.append(roll_number)
            
    # Generate numeric roll numbers of Lateral entries
    for i in range(1,22):
        roll_number = f"23J45A67{i:02}"
        roll_numbers.append(roll_number)

    return roll_numbers

roll_numbers = generate_roll_numbers()

# Check if the Excel file exists, create if not
if not os.path.exists(excel_file):
    df = pd.DataFrame(columns=['Roll Number', 'Name', 'Total Marks', 'SGPA', 'CGPA', 'Subjects due'] )  
    df.to_excel(excel_file, index=False)

for roll_number in roll_numbers:
    try:
        # print(f"Entering roll number: {roll_number}")

        input_field = driver.find_element(By.NAME, "HallTicketNo")
        input_field.clear()
        input_field.send_keys(roll_number)
        input_field.send_keys(Keys.RETURN)

        # print("Waiting for results to load...")

        # Wait for SGPA element to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//div[@id='sgpa_{roll_number.upper()}']")))

        # Extract Total marks
        # marks_element =  driver.find_element(By.XPATH, f"//td[@id='marksobtained_{roll_number.upper()}']")
        # marks_text = marks_element.text 
        # marks = [int(mark.split('/')[0].strip()) for mark in marks_text.splitlines()]

        marks_element =  driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[14]/td[8]')
        marks = marks_element.text.strip()

        # Extract due subjects
        subject_element =  driver.find_element(By.XPATH, f"//td[@id='subjectdue_{roll_number.upper()}']")
        subject_text = subject_element.text 
        subjects = [int(sub.split('/')[0].strip()) for sub in subject_text.splitlines()]

        # Fetch SGPA and CGPA
        sgpa_element = driver.find_element(By.XPATH, f"//div[@id='sgpa_{roll_number.upper()}']")
        sgpa = sgpa_element.text.strip()
        # print(f"Found SGPA for {roll_number}: {sgpa}")

        cgpa_element = driver.find_element(By.XPATH, f"//td[@id='cgpa_{roll_number.upper()}']")
        cgpa = cgpa_element.text.strip()
        # print(f"Found CGPA for {roll_number}: {cgpa}")

        # Fetch Name
        name_element = driver.find_element(By.XPATH, "(//span[@style='color:#851fd0; font-weight:bold'])[2]")
        name = name_element.text.strip().title()  # Capitalize first letter of each word
        # print(f"Found Name for {roll_number}: {name}") 

        #subject wise marks 
        #1
        Befa_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[4]/td[8]') 
        Befa = Befa_element.text.strip() 

        Befa_status_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[4]/td[11]') 
        Befa_status = Befa_status_element.text.strip()
        #2
        Dm_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[5]/td[8]') 
        Dm = Dm_element.text.strip()

        Dm_status_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[5]/td[11]') 
        Dm_status = Dm_status_element.text.strip()
        #3
        Os_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[6]/td[8]') 
        Os = Os_element.text.strip()

        Os_status_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[6]/td[11]') 
        Os_status = Os_status_element.text.strip()
        #4
        Dbms_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[7]/td[8]') 
        Dbms = Dbms_element.text.strip()

        Dbms_status_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[7]/td[11]') 
        Dbms_status = Dbms_status_element.text.strip()
        #5
        Dpa_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[8]/td[8]') 
        Dpa = Dpa_element.text.strip()

        Dpa_status_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[8]/td[11]') 
        Dpa_status = Dpa_status_element.text.strip()
        #6
        Os_Lab_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[9]/td[8]') 
        Os_Lab = Os_Lab_element.text.strip()
        #7
        Dbms_Lab_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[10]/td[8]') 
        Dbms_Lab = Dbms_Lab_element.text.strip()
        #8
        Rtl_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[11]/td[8]') 
        Rtl = Rtl_element.text.strip()
        #9
        Sd_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[12]/td[8]') 
        Sd = Sd_element.text.strip()
        #10
        Es_element = driver.find_element(By.XPATH, f'//*[@id="myApp"]/body/div[2]/div[2]/div/div[3]/div/table[2]/tbody/tr[13]/td[8]') 
        Es = Es_element.text.strip()


        # Prepare data for Excel
        result = pd.DataFrame({'Roll Number': [roll_number], 'Name': [name], 'BEFA':[Befa], 'Befa_Status':[Befa_status], 'DM':[Dm], 'Dm_Status':[Dm_status], 'OS':[Os], 'Os_Status':[Os_status], 'DBMS':[Dbms], 'Dbms_Status':[Dbms_status], 'DPA':[Dpa], 'Dpa_Status':[Dpa_status], 'OS-Lab':[Os_Lab], 'DBMS-Lab':[Dbms_Lab], 'RTL-Lab':[Rtl], 'SD-Lab':[Sd], 'ES':[Es], 'Total Marks':[marks], 'SGPA': [sgpa], 'CGPA': [cgpa], 'Subjects due': [subjects]})

        print(f"Data for {roll_number} entered successfully.")

    except Exception as e:
        print(f"Result not found for {roll_number}: {e}")
        name = 'Detained'
        sgpa = 'Detained'
        cgpa = 'Detained'
        Befa = 'Detained'
        Befa_status = 'Detained'
        Dm = 'Detained'
        Dm_status = 'Detained'
        Os = 'Detained'
        Os_status = 'Detained'
        Dbms = 'Detained'
        Dbms_status = 'Detained'
        Dpa = 'Detained'
        Dpa_status = 'Detained'
        Os_Lab = 'Detained'
        Dbms_Lab = 'Detained'
        Rtl = 'Detained'
        Sd = 'Detained'
        Es = 'Detained'
        marks = 'Detained' 
        subjects = 'Detained'
        result = pd.DataFrame({'Roll Number': [roll_number], 'Name': [name], 'BEFA':[Befa], 'Befa_Status':[Befa_status], 'DM':[Dm], 'Dm_Status':[Dm_status], 'OS':[Os], 'Os_Status':[Os_status], 'DBMS':[Dbms], 'Dbms_Status':[Dbms_status], 'DPA':[Dpa], 'Dpa_Status':[Dpa_status], 'OS-Lab':[Os_Lab], 'DBMS-Lab':[Dbms_Lab], 'RTL-Lab':[Rtl], 'SD-Lab':[Sd], 'ES':[Es], 'Total Marks':[marks], 'SGPA': [sgpa], 'CGPA': [cgpa], 'Subjects due': [subjects]})

        print(driver.page_source)  # Print the page source for debugging

    # Append result to Excel immediately after fetching
    existing_df = pd.read_excel(excel_file)
    updated_df = pd.concat([existing_df, result], ignore_index=True)
    updated_df.to_excel(excel_file, index=False)
    # print(f"Results saved for roll number: {roll_number}")

# Close the browser
driver.quit()
print("Browser closed.")
