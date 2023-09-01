from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException,\
    ElementNotVisibleException, ElementNotInteractableException, StaleElementReferenceException, TimeoutException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from lxml import etree as et
from csv import writer
from selenium import webdriver
import time
import random

# job_search_keyword = [' Data+Scientist', 'Business+Analyst', 'Data+Engineer', 'Python+Developer', 'Full+Stack+Developer', 'Machine+Learning+Engineer']
# location_search_keyword = ['New+York', 'California', 'Los+Angeles']

# # define base and pagination URLs
# base_url = 'https://www.indeed.com'
# paginaton_url = "https://www.indeed.com/jobs?q={}&l={}&radius=35&start={}"

# # Initializing the webdriver
# options = webdriver.FirefoxOptions()
# driver = webdriver.Firefox(options=options)
# driver.set_window_size(1120, 1000)# open initial URL
# driver.get("https://www.indeed.com/q-USA-jobs.html?vjk=823cd7ee3c203ac3")

# def get_dom(url):
#    driver.get(url)
#    page_content = driver.page_source
#    product_soup = BeautifulSoup(page_content, 'html.parser')
#    dom = et.HTML(str(product_soup))
#    return dom

# # functions to extract job link
# def get_job_link(job):
#    try:
#        job_link = job.xpath('./descendant::h2/a/@href')[0]
#    except Exception as e:
#        job_link = 'Not available'
#    return job_link


# # functions to extract job title
# def get_job_title(job):
#    try:
#        job_title = job.xpath('./descendant::h2/a/span/text()')[0]
#    except Exception as e:
#        job_title = 'Not available'
#    return job_title


# # functions to extract the company name
# def get_company_name(job):
#    try:
#        company_name = job.xpath('./descendant::span[@class="companyName"]/text()')[0]
#    except Exception as e:
#        company_name = 'Not available'
#    return company_name


# # functions to extract the company location
# def get_company_location(job):
#    try:
#        company_location = job.xpath('./descendant::div[@class="companyLocation"]/text()')[0]
#    except Exception as e:
#        company_location = 'Not available'
#    return company_location


# # functions to extract salary information
# def get_salary(job):
#    try:
#        salary = job.xpath('./descendant::span[@class="estimated-salary"]/span/text()')
#    except Exception as e:
#        salary = 'Not available'
#    if len(salary) == 0:
#        try:
#            salary = job.xpath('./descendant::div[@class="metadata salary-snippet-container"]/div/text()')[0]
#        except Exception as e:
#            salary = 'Not available'
#    else:
#        salary = salary[0]
#    return salary


# # functions to extract job type
# def get_job_type(job):
#    try:
#        job_type = job.xpath('./descendant::div[@class="metadata"]/div/text()')[0]
#    except Exception as e:
#        job_type = 'Not available'
#    return job_type


# # functions to extract job rating
# def get_rating(job):
#    try:
#        rating = job.xpath('./descendant::span[@class="ratingNumber"]/span/text()')[0]
#    except Exception as e:
#        rating = 'Not available'
#    return rating


# # functions to extract job description
# def get_job_desc(job):
#    try:
#        job_desc = job.xpath('./descendant::div[@class="job-snippet"]/ul/li/text()')
#    except Exception as e:
#        job_desc = ['Not available']
#    if job_desc:
#        job_desc = ",".join(job_desc)
#    else:
#        job_desc = 'Not available'
#    return job_desc

# # Open a CSV file to write the job listings data
# with open('indeed_jobs1.csv', 'w', newline='', encoding='utf-8') as f:
#    theWriter = writer(f)
#    heading = ['job_link', 'job_title', 'company_name', 'company_location', 'salary', 'job_type', 'rating', 'job_description', 'searched_job', 'searched_location']
#    theWriter.writerow(heading)
#    for job_keyword in job_search_keyword:
#        for location_keyword in location_search_keyword:
#            all_jobs = []
#            for page_no in range(0, 100, 10):
#                url = paginaton_url.format(job_keyword, location_keyword, page_no)
#                page_dom = get_dom(url)
#                jobs = page_dom.xpath('//div[@class="job_seen_beacon"]')
#                all_jobs = all_jobs + jobs
#            for job in all_jobs:
#                job_link = base_url + get_job_link(job)
#                time.sleep(2)
#                job_title = get_job_title(job)
#                time.sleep(2)
#                company_name = get_company_name(job)
#                time.sleep(2)
#                company_location = get_company_location(job)
#                time.sleep(2)
#                salary = get_salary(job)
#                time.sleep(2)
#                job_type = get_job_type(job)
#                time.sleep(2)
#                rating = get_rating(job)
#                time.sleep(2)
#                job_desc = get_job_desc(job)
#                time.sleep(2)
#                record = [job_link, job_title, company_name, company_location, salary, job_type, rating, job_desc, job_keyword, location_keyword]
#                theWriter.writerow(record)

# # Closing the web browser
# driver.quit()

def get_jobs(keyword, city, num_jobs, verbose=False):
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''

    # Initializing the webdriver
    options = webdriver.FirefoxOptions()

    # Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    # options.add_argument('headless')

    # Change the path to where chromedriver is in your home folder.
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1120, 1000)

    keyword = '+'.join(keyword.split())

    cities_dict = {
        'San Francisco': 'San+Francisco%2C+CA',
        'London': 'London%2C Greater London'
    }

    # url = 'https://www.indeed.com/jobs?q=data%20scientist&l=San%20Francisco%2C%20CA&vjk=7cc7569616e07186'
    url = 'https://www.indeed.com/jobs?q={}&l={}'.format(keyword, city)
    
    driver.get(url)
    print("hello")
    time.sleep(random.randint(3, 6))
    print("wow")
    jobs = []

    while len(jobs) < num_jobs:  # If true, should be still looking for new jobs.

        # Let the page load. Change this number based on your internet speed.
        # Or, wait until the webpage is loaded, instead of hardcoding it.
        time.sleep(random.randint(2, 7))

        # Going through each job in this page
        try:
            job_buttons = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")  # jl for Job Listing. These are the buttons we're going to click.
        except ElementNotInteractableException:
            button_x = driver.find_element(By.CSS_SELECTOR, 'button.popover-x-button-close')
            button_x.click()
            job_buttons = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")
        collected_successfully = False

        print(job_buttons)
        #         //Now after all your stuff done inside frame need to switch to default content
        for job_button in job_buttons[:-1]:

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))
            if len(jobs) >= num_jobs:
                break

            try:
                job_button.location_once_scrolled_into_view
                job_button.click()# You might
                print("clicked")
            except ElementClickInterceptedException:
                button_x = driver.find_element(By.CSS_SELECTOR, 'button.popover-x-button-close')
                button_x.click()
            collected_successfully = False

            try:
                salary = job_button.find_element(By.CSS_SELECTOR, 'div.estimated-salary-container').text
            except NoSuchElementException:
                salary = -1
            job_url = job_button.find_element(By.CSS_SELECTOR, 'a.jcs-JobTitle').get_attribute('href')

            # try:
            #     list = job_button.find_elements(By.CSS_SELECTOR, 'div.attribute_snippet')
            #     if len(list) == 1:
            #         job_type = list[0].text
            #     elif len(list) == 2:
            #         job_type, shift = list[0].text, list[1].text
            # except NoSuchElementException:
            #     job_type = -1
            #     shift = -1

            time.sleep(random.randint(1, 3))
            # wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "jobsearch-ViewjobPaneWrapper")))
            # info_right_side = driver.find_element_by_id('jobDescriptionText')
            # driver.find_element(By.CSS_SELECTOR, "div.fastviewjob").click()
            driver.find_element(By.CSS_SELECTOR, 'div.jobsearch-RightPane').click()
            # print("focused")

            
            top = driver.find_element(By.CSS_SELECTOR, "div.jobsearch-InfoHeaderContainer")
            job_title = top.find_element(By.CSS_SELECTOR, "div.jobsearch-JobInfoHeader-title-container").text
            # print("topped")

            company_info = top.find_element(By.CSS_SELECTOR, 'div[data-testid="jobsearch-CompanyInfoContainer"]')
            # print("found info")
            # company_name = company_info.text

            try:
                # meta = company_info[0].find_elements(By.CSS_SELECTOR, "meta")
                # company_rating = meta[0].get_attribute("content")
                # company_review_count = meta[1].get_attribute("content")
                company_name = company_info.find_element(By.CSS_SELECTOR, 'div[data-testid="inlineHeader-companyName"]').text
                company_rating = company_info.find_element(By.CSS_SELECTOR, 'div[id="companyRatings"]').getAttribute("aria-label")
                location = company_info.find_element(By.CSS_SELECTOR, 'div[data-testid="inlineHeader-companyLocation"]').text
            except:
                company_name = None
                company_rating = -1
                location = None
            # location = company_info[1].text

            # print("infoed")

            bottom = driver.find_element(By.CSS_SELECTOR, "div.jobsearch-JobComponent-description")
            # print("got bottom")
            try:
                details = bottom.find_element(By.CSS_SELECTOR, "div[id='jobDetailsSection']").get_attribute('innerHTML')
                job_description = bottom.find_element(By.CSS_SELECTOR, "div[id='jobDescriptionText']").get_attribute('innerHTML')
            except:
                continue
            # try:
            #     salary_estimate = driver.find_element_by_xpath('.//span[@class="gray small salary"]').text
            # except NoSuchElementException:
            #     salary_estimate = -1  # You need to set a "not found value. It's important."
            #
            # try:
            #     rating = driver.find_element_by_xpath('.//span[@class="rating"]').text
            # except NoSuchElementException:
            #     rating = -1  # You need to set a "not found value. It's important."

            # Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary: {}".format(salary))
                print("Job Description: {}".format(job_description))
                print("Rating: {}".format(company_rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))
                print("description: {}".format(job_description))
            # Going to the Company tab...
            # clicking on this:
            # <div class="tab" data-tab-type="overview"><span>Company</span></div>
            # try:
            #
            #     WebDriverWait(driver, 10).until(
            #         expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[1]/div/div/div[2]/span')))
            #     driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/div/div[2]/section/div/div/article/div/div[2]/div[1]/div[1]/div/div/div[2]/span').click()
            #     time.sleep(2)
            #
            #     try:
            #         # <div class="infoEntity">
            #         #    <label>Headquarters</label>
            #         #    <span class="value">San Francisco, CA</span>
            #         # </div>
            #         headquarters = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Headquarters"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         headquarters = -1
            #
            #     try:
            #         size = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Size"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         size = -1
            #
            #     try:
            #         founded = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Founded"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         founded = -1
            #
            #     try:
            #         type_of_ownership = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Type"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         type_of_ownership = -1
            #
            #     try:
            #         industry = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Industry"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         industry = -1
            #
            #     try:
            #         sector = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Sector"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         sector = -1
            #
            #     try:
            #         revenue = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Revenue"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         revenue = -1
            #
            #     try:
            #         competitors = driver.find_element_by_xpath(
            #             './/div[@class="infoEntity"]//label[text()="Competitors"]//following-sibling::*').text
            #     except NoSuchElementException:
            #         competitors = -1
            #
            # except NoSuchElementException:  # Rarely, some job postings do not have the "Company" tab.
            #     headquarters = -1
            #     size = -1
            #     founded = -1
            #     type_of_ownership = -1
            #     industry = -1
            #     sector = -1
            #     revenue = -1
            #     competitors = -1
            # except StaleElementReferenceException:
            #     headquarters = -1
            #     size = -1
            #     founded = -1
            #     type_of_ownership = -1
            #     industry = -1
            #     sector = -1
            #     revenue = -1
            #     competitors = -1
            # except TimeoutException:
            #     headquarters = -1
            #     size = -1
            #     founded = -1
            #     type_of_ownership = -1
            #     industry = -1
            #     sector = -1
            #     revenue = -1
            #     competitors = -1
            # except ElementClickInterceptedException:
            #     headquarters = -1
            #     size = -1
            #     founded = -1
            #     type_of_ownership = -1
            #     industry = -1
            #     sector = -1
            #     revenue = -1
            #     competitors = -1
            # if verbose:
            #     print("Headquarters: {}".format(headquarters))
            #     print("Size: {}".format(size))
            #     print("Founded: {}".format(founded))
            #     print("Type of Ownership: {}".format(type_of_ownership))
            #     print("Industry: {}".format(industry))
            #     print("Sector: {}".format(sector))
            #     print("Revenue: {}".format(revenue))
            #     print("Competitors: {}".format(competitors))
            #     print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

            jobs.append({"Job Title": 'new post ' + job_title,
                         "Salary": salary,
                         "Job Description": job_description,
                         "Job details": details,
                         "Rating": company_rating,
                         "Company Name": company_name,
                         "Location": location,
                         "URL": job_url})
            time.sleep(random.randint(3, 8))
            # add job to jobs
            # driver.switch_to.default_content()
        # Clicking on the "next page" button
        try:
            print("going next")
            WebDriverWait(driver, 10).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'a[aria-label="Next Page"]')))
            driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Next Page"]').click()
            time.sleep(2)
        except :
            print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs,
                                                                                                         len(jobs)))
            break

    df = pd.DataFrame(jobs)
    df.insert(0, "Position", keyword)
    df.insert(1, "City", city)
    df.to_csv(keyword + "_" + city + ".csv")
    driver.quit()

    return 0