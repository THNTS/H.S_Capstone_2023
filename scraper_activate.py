
from Scraper import get_jobs
import os
import multiprocessing
from itertools import product
# "Cloud System Engineer", "IT Coordinator", "Help Desk Technician", "Data Quality Manager", 

if __name__ == '__main__':
    job_positions = [
                     "Applications Engineer", "Web Administrator",
                     "Management Information Systems Director", "IT director", "Data scientist",
                     "IT security specialist", "Software engineer", "Computer scientist",
                     "Database administrator", "User experience designer",  "Network engineer",
                     "System analyst", "IT technician", "Web developer", "Quality assurance tester",
                     "Computer programmer", "Support specialist"]
    cities = ["San Francisco", "London"]
    num_results = 30
    results = []
    # with multiprocessing.Pool(processes=2) as pool:
    #     results = pool.starmap(get_jobs, product([
    #                  "Network engineer",
    #                  "System analyst", "Quality assurance tester",
    #                  "Computer programmer"],
    #                                              ["London"], [100]))
    # result=get_jobs("Data Scientist", "San Francisco", 25)
    for position in job_positions:
        for city in cities:
            get_jobs(position, city, num_results)