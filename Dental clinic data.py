#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd


# In[2]:


PATH = "C:\\Program Files (x86)\\chromedriver.exe"


# In[3]:


service = Service(PATH)


# In[15]:


driver = webdriver.Chrome(service=service)


# In[16]:


driver.get("https://www.google.com/search?sca_esv=af0b90c6614b7d36&rlz=1C1CHBD_enKE776KE776&tbs=lf:1,lf_ui:2&tbm=lcl&q=dental+clinics+in+nairobi&rflfq=1&num=10&sa=X&ved=2ahUKEwi6wdPkwNWGAxX6_bsIHQw1DdMQjGp6BAghEAE&biw=1366&bih=589&dpr=1#rlfi=hd:;si:;mv:[[-1.1894227,36.9334433],[-1.3213423,36.7626953]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!2m4!1e17!4m2!17m1!1e2!3sIAE,lf:1,lf_ui:2")


# In[17]:


Al_clinic = []


# In[18]:


# Function to extract data from the current page
def extract_clinic_data():
    clinic_divs = driver.find_elements(By.CSS_SELECTOR, 'div.rllt__details')
    for div in clinic_divs:
        try:
            # Extract clinic name
            clinic_name = div.find_element(By.CSS_SELECTOR, 'div.dbg0pd').text

            # Try to extract rating
            try:
                rating_span = div.find_element(By.CSS_SELECTOR, 'span.Y0A0hc > span.yi40Hd.YrbPuc')
                rating = rating_span.text.strip()
            except:
                rating = 'No rating available'
            
            # Extract status and closing time
            status_and_closing_time = div.find_elements(By.TAG_NAME, 'div')[3].text

            # Extract location by splitting the text and removing the phone number
            location = status_and_closing_time.split('·')[0].strip()

            # Extract phone number
            phone_number = status_and_closing_time.split('·')[-1].strip()

            # Add the extracted information to the list
            Al_clinic.append({
                'Clinic Name': clinic_name,
                'Rating': rating,
                'Location': location,
                'Phone Number': phone_number
            })
        except Exception as e:
            print(f'An error occurred: {e}')



# Iterate through pages 1 to 11
for page_num in range(1, 11):
    extract_clinic_data()
    try:
        # Find the 'Next' button and click it to go to the next page
        next_button = driver.find_element(By.CSS_SELECTOR, 'a#pnnext')  # Adjust the selector if necessary
        next_button.click()
        time.sleep(3)  # Wait for the next page to load
    except Exception as e:
        print(f'Could not navigate to page {page_num + 1}: {e}')
        break

# Close the WebDriver
driver.quit()

# Convert the list of clinics to a DataFrame
df = pd.DataFrame(Al_clinic)

# Save the DataFrame to an Excel file
df.to_excel('Clinic_datas.xlsx', index=False)

print('Data has been saved to Clinic_datas.xlsx')


# In[ ]:




