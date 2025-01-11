## Dental Clinics Data Scraper
# Project Overview
This project is a web scraping application built with Python and Selenium to gather information about dental clinics in Nairobi. The application automates the process of collecting clinic details from Google search results and stores the data in an organized Excel file. This scraper extracts the following information for each clinic:
- Clinic Name
- Rating
- Location
- Phone Number
The project demonstrates effective use of Selenium for automating browser actions, scraping dynamic content, handling pagination, and exporting results to Excel for easy use.

# Features
1. Web Scraping with Selenium: Automatically navigates through Google search results for dental clinics and extracts relevant details.
2. Data Extraction: Pulls clinic name, rating, location, and phone number from each clinic listing.
3. Pagination Handling: Automates clicking the "Next" button to navigate through multiple pages of Google search results.
4. Data Export: Organizes the scraped data into a Pandas DataFrame and saves it to an Excel file (Clinic_datas.xlsx).

# Technologies Used
- Python: The primary programming language for this project.
- Selenium: A web scraping tool for automating browser interactions and handling dynamic web pages.
- Pandas: Used for organizing data into DataFrames and exporting it to Excel.
- ChromeDriver: Used to interact with Google Chrome for the web scraping task.
  
# Installation
Prerequisites
- Python 3.x: 
- ChromeDriver: You need to install ChromeDriver to allow Selenium to interact with the Chrome browser.
  
Required Python Libraries:
- selenium
- pandas
- openpyxl (for saving data to Excel)

# Conclusion
This project is an example of web scraping with Selenium, showcasing the ability to navigate dynamic web pages, extract structured data, and save it for further use. It can be further extended and customized based on user needs, making it a great tool for anyone looking to automate web scraping tasks.

# Project Disclaimer:

This project is intended for educational purposes only. The data extraction and web scraping activities conducted are solely for learning and instructional use. I do not endorse or support the unauthorized use of web scraping techniques to collect data from websites without permission. All information retrieved through this project should be handled responsibly and in accordance with applicable laws and regulations. Please ensure to respect the terms of service and privacy policies of any websites you interact with.
