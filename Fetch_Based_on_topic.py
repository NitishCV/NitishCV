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
    "https://backend.careervira.com/content-manager/explorer/application::learn-content.learn-content?_limit=7000&_sort=id%3AASC&_start=0",
    headers={"Authorization": f"Bearer {response['token']}"},
).json()
#backend_courses = str(backend_courses).replace("\'", "\"")
print(backend_courses)

data = []

health_care = ['Healthcare & Medicine', 'Healthcare Operations', 'Health Management''Public Health',
               'Mental Health', 'Health Informatics', 'Animal Health', 'Clinical Research']
with open('healthcare.csv', 'w', newline='') as out:
    csv_out = csv.writer(out)
    for i in range(len(backend_courses)):
        try:
            data = backend_courses[i]['title'], backend_courses[i]['id'], backend_courses[i]['status'], backend_courses[i]['topics'][0]['default_display_label'], backend_courses[i]['partner']['name'], "https://www.careervira.com/course/"+backend_courses[i]['slug']
            print(data[1])
            if data[3] in health_care:
                csv_out.writerow(data)
        except  ValueError:
            pass
        except IndexError:
            pass
