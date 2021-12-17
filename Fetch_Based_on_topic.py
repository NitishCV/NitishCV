import requests
import os
import csv


os.chdir('C:/Users/nitis/Music')

response = requests.post(
    "https://backend.careervira.com/admin/login",
    data={
        "email": "robiul@ajency.in",
        "password": "Ajency#123",
        "Content-Type": "application/json",
    },
).json()["data"]
# Courses

backend_courses = requests.get(
    "https://backend.careervira.com/content-manager/explorer/application::learn-content.learn-content?_limit=7953&_sort=id%3AASC&status=approved&_start=6000",
    headers={"Authorization": f"Bearer {response['token']}"},
).json()

print(backend_courses[0]['topics'][0]['sub_category'])

data = []
'''
for i in range(len(backend_courses)):
    #data = backend_courses[i]['title'], backend_courses[i]['topics'][0]['default_display_label'], backend_courses[i]['status'], str(len(backend_courses[i]['title'])), backend_courses[i]['slug'], backend_courses[i]['partner']['name']
    print(backend_courses[i]['topics'][0]['sub_category'])
'''

health_care = ["Healthcare Operations", "Health Management", "Healthcare & Medicine", "Health Informatics", "Public Health", "Fitness Instruction", "Mental Health", "Psychology", "Clinical Research", "Biopharmaceuticals", "Basic Science", "Patient Care", "Research", "Animal Health", "Teaching & Research", "Personality Development", "Learning & Development"]
with open('healthcare_new_4.csv', 'w', newline='') as out:
    csv_out = csv.writer(out)
    for i in range(len(backend_courses)):
        try:
            data = backend_courses[i]['title'], backend_courses[i]['id'], backend_courses[i]['status'], backend_courses[i]['topics'][0]['default_display_label'], backend_courses[i]['partner']['name'], "https://www.careervira.com/course/"+backend_courses[i]['slug']
            if data[3] in health_care:
                print(data[1])
                csv_out.writerow(data)
        except  ValueError:
            pass
        except IndexError:
            pass
  

