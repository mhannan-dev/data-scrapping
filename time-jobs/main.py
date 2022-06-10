from bs4 import BeautifulSoup
import requests
import time


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'Posted' in published_date:
            company_name = job.find(
                'h3', class_='joblist-comp-name').text
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            with open(f'jobs/{index}.txt', 'w') as f:
                f.write(f"Company name: {company_name.strip()} \n")
                f.write(f"Skills: {skills.strip()} \n")
                f.write(f"More info: {more_info.strip()} \n")
            print(f"Jobs saved: {index}")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting { time_wait } seconds.....")
        time.sleep(time_wait * 60)
