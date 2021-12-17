import requests
import os
import csv
import json


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
    "https://backend.careervira.com/content-manager/explorer/application::learn-content.learn-content?_limit=498&_sort=id%3AASC&status=pending_review&_start=0",
    headers={"Authorization": f"Bearer {response['token']}"},
).json()
#backend_courses = str(backend_courses).replace("\'", "\"")

data = []

'''
for i in range(len(backend_courses)):
    #data = backend_courses[i]['title'], backend_courses[i]['topics'][0]['default_display_label'], backend_courses[i]['status'], str(len(backend_courses[i]['title'])), backend_courses[i]['slug'], backend_courses[i]['partner']['name'], backend_courses[i]['provider_information']['provider']['name']
    data = backend_courses[i]['topics']

    print(data)
'''
#health_care = ['Healthcare & Medicine', 'Healthcare Operations', 'Health Management''Public Health','Mental Health', 'Health Informatics', 'Animal Health', 'Clinical Research']
with open('pending.csv', 'w', newline='') as out:
    csv_out = csv.writer(out)
    for i in range(len(backend_courses)):
        try:
            data = backend_courses[i]['title'], str(len(backend_courses[i]['title'])), backend_courses[i]['id'], backend_courses[i]['status'], backend_courses[i]['partner']['name'], "https://www.careervira.com/course/"+backend_courses[i]['slug'], backend_courses[i]['provider_information']['provider']['name']
            print(data[1])
            csv_out.writerow(data)
        except TypeError:
            data = backend_courses[i]['title'], str(len(backend_courses[i]['title'])), backend_courses[i]['id'], backend_courses[i]['status'], "", "", backend_courses[i]['provider_information']['provider']['name']
            csv_out.writerow(data)
        
