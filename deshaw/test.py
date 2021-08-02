import requests
import csv
# open file containing abstract
file = open("hello.txt", "r", errors="ignore")
csvfile=open('deshaw.csv','w')
csv_writer=csv.writer(csvfile)

csv_writer.writerow(["job_id", "job_title", "company_name", "url", "desirable_candidate", "day_to_day_responsibility",
              'Experience', 'abstract', "address", "application_message"])

abstract = file.read()

address = "Plot No. 573, B & C, Road No. 1 Jubilee Hills, Hyderabad 500 096 Telangana, India"
application_message = "Join our team in Hyderabad"
r = requests.get("https://www.deshawindia.com/recruit/services/jobs/getAllJobsForWebsite/2")
jobs_data = r.json()
jobs_data = jobs_data.replace('\t','').replace("\n",'')
print("".join(i for i in text if ord(i)<128))

jobs_count = len(jobs_data)


for i in range(jobs_count):
    lis = []
    job_id = jobs_data[i]["id"]
    job_title = jobs_data[i]["displayName"]
    company_name = "D.E Shaw & Co"
    url = "https://www.deshawindia.com/careers/{}".format(job_id)
    desirable_candidate = jobs_data[i]["jobDescription"]["websiteDescription"]
    responsibilities = jobs_data[i]["jobDescription"]["responsibilities"]
    # try and except block as requirements can be empty and can cause error
    try:
        requirements = ''.join(jobs_data[i]["jobDescription"]["peopleWeAreLookingFor"])
    except:
        requirements = None
    csv_writer.writerow([job_id, job_title, company_name, url, desirable_candidate, responsibilities, requirements, abstract, address, application_message])
    

csvfile.close()


