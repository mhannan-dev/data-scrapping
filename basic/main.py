from bs4 import BeautifulSoup
with open('index.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courseCards = soup.find_all('div', class_='card')
    
    for course in courseCards:
        courseName = course.h5.text
        coursePrice = course.a.text.split()[-1]

        print(courseName)
        print(coursePrice)


