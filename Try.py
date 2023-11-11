from bs4 import BeautifulSoup;
with open("home.html",'r') as Html_file:
    content = Html_file.read()
    soup = BeautifulSoup(content,'lxml')
    course = soup.find_all('div')
    for course in course:
        unit = (course.h1.text)
        cost =(course.a.text.split()[-1])
        print(f"{unit} costs {cost}")