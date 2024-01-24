from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

import json

def welcome(request):

    return render(request, "Welcome.html")


def login(request):
    
    if request.method == "GET":

        return render(request, 'Login.html')
    
d = {}

def input_login(request):

    from login import student_verify_login
    from login import responder_verify_login
    from login import faculty_verify_login
    
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['pass']

        request.session['email'] = email

        flag = 0

        if student_verify_login(email, password)[0] == 'Login Successful':
            flag = 1
            request.session['name'] = student_verify_login(email, password)[1]
        
        if faculty_verify_login(email, password)[0] == 'Login Successful':
            flag = 1
            request.session['name'] = faculty_verify_login(email, password)[1]
            
        if responder_verify_login(email, password) == 'Login Successful':
            flag = 2
            
        if student_verify_login(email, password) == 'Invalid Student email' and \
            responder_verify_login(email, password) == 'Invalid Responder email' and \
                faculty_verify_login(email, password) == 'Invalid Faculty email':
            flag = 3

        if student_verify_login(email, password) == 'Invalid password' or \
            responder_verify_login(email, password) == 'Invalid password' or \
                faculty_verify_login(email, password) == 'Invalid password':
            flag = 4

        if flag == 1:
            return render(request, "Openticket.html")
        elif flag == 2:
            return render(request, "Responder.html")
        elif flag == 3:
            return render(request, 'Emaillogin.html')
        elif flag == 4:
            return render(request, 'Passwordlogin.html')


def openticket(request):

    if request.method == "GET":

        return render(request, "Openticket.html")
    

def open_ticket(request):

    from strategy import driver_code
    from mail import Sending_Mail
    from login import responder_dict

    class Data:

        def __init__(self, name):

            self.name = name

    if request.method == "POST":

        help_topic = request.POST['topic']
        issue_summary = request.POST['issue']
        problem = request.POST['problem']
        location = request.POST['place']
        details = request.POST['details']
        number = request.POST['number']

        e = request.session.get("email")
        n = request.session.get('name')
        data = []

        data.append(Data(n))

        message1 = "This email is to inform you that you have opened a new ticket to be addressed by \
SPEEDY SUPPORT." + "<br>" + "The details of the ticket is given below:-<br>" +\
f"Help Topic : {help_topic}" + "<br>" +\
f"Issue Summary : {issue_summary}" + "<br>" +\
f"Detail on the reason(s) for opening the ticket : {problem}" + "<br>" +\
f"Location : {location}" + "<br>" +\
f"Department / Hostel Number & Room Number : {details}" + "<br>" +\
f"Mobile Number : {number}" + "<br>"
        
        message2 = "This email is to inform you that a new ticket to be addressed by you on behalf of \
SPEEDY SUPPORT." + "<br>" + "The details of the ticket is given below:-<br>" +\
f"Help Topic : {help_topic}" + "<br>" +\
f"Issue Summary : {issue_summary}" + "<br>" +\
f"Detail on the reason(s) for opening the ticket : {problem}" + "<br>" +\
f"Location : {location}" + "<br>" +\
f"Department / Hostel Number & Room Number : {details}" + "<br>" +\
f"Mobile Number : {number}" + "<br>"

        Sending_Mail(e, "New ticket created at SPEEDY SUPPORT", message1)

        d = responder_dict()
        for item in d:
            if  d[item] == problem:
                sender_email = item

        Sending_Mail(sender_email, "New ticket to be addressed at SPEEDY SUPPORT", message2)

        driver_code(n, e, help_topic, issue_summary, problem, location, details, number, f'active_ticket/{e}_activeticket.json')
        driver_code(n, e, help_topic, issue_summary, problem, location, details, number, f'to_address/{problem}.json')

        return render(request, "TicketCreated.html", {'data' : data})
    

def active_ticket(request):

    class Data1:

        def __init__(self, name, email, date, time, topic, issue, reason, location, dept, number):

            self.name = name
            self.email = email
            self.date = date
            self.time = time
            self.topic = topic
            self.issue = issue
            self.reason = reason
            self.location = location
            self.dept = dept
            self.number = number


    class Data2:

        def __init__(self, name, email):

            self.name = name
            self.email = email

    if request.method == "GET":

        e = request.session.get('email')
        n = request.session.get('name')
        data1 = []
        data2 = []

        data2.append(Data2(n, e))

        try:

            with open(f"active_ticket/{e}_activeticket.json", 'r') as file:
                file.seek(0)
                details = json.load(file)
            
            if details != []:

                for item in details:
                    data1.append(Data1(n, e, item['Date'], item['Time'], item['Help Topic'], item['Issue Summary'], item['Problem'], item['Location'], item['Details'], item['Number']))

                return render(request, "ActiveTicket.html", {'data1' : data1})

            else:
                return render(request, "NoActive.html", {'data2' : data2})

        except FileNotFoundError:
            return render(request, "NoActive.html", {'data2' : data2})
        

def closed_ticket(request):

    class Data1:

        def __init__(self, name, email, date, time, topic, issue, reason, location, dept, number, filename):

            self.name = name
            self.email = email
            self.date = date
            self.time = time
            self.topic = topic
            self.issue = issue
            self.reason = reason
            self.location = location
            self.dept = dept
            self.number = number
            self.filename =  filename


    class Data2:

        def __init__(self, name, email):

            self.name = name
            self.email = email


    if request.method == "GET":

        e = request.session.get("email")
        n = request.session.get("name")
        data1 = []
        data2 = []

        data2.append(Data2(n, e))

        try:

            with open(f"closed_ticket/{e}_closedticket.json", 'r') as file:
                file.seek(0)
                details = json.load(file)

                count = 1

            for item in details:
                data1.append(Data1(n, e, item['Date'], item['Time'], item['Help Topic'], item['Issue Summary'], item['Problem'], item['Location'], item['Details'], item['Number'], f'/static/reports/{e}_ticket{count}.txt'))
                count += 1

            return render(request, "ClosedTicket.html", {'data1' : data1})

        except FileNotFoundError:
            return render(request, "NoClosed.html", {'data2' : data2})


def responder(request):

    from login import responder_problem

    class Data1:

        def __init__(self, name, email, date, time, topic, issue, reason, location, dept, number):

            self.name = name
            self.email = email
            self.date = date
            self.time = time
            self.topic = topic
            self.issue = issue
            self.reason = reason
            self.location = location
            self.dept = dept
            self.number = number


    class Data2:

        def __init__(self, email):

            self.email = email

    if request.method == "GET":

        e = request.session.get('email')
        data1 = []
        data2 = []

        data2.append(Data2(e))
        problem = responder_problem(e)

        try:

            with open(f"to_address/{problem}.json", 'r') as file:
                file.seek(0)
                details = json.load(file)
            
            if details != []:
                for item in details:
                    data1.append(Data1(item['Name'], item['Email'], item['Date'], item['Time'], item['Help Topic'], item['Issue Summary'], item['Problem'], item['Location'], item['Details'], item['Number']))

                return render(request, "Responderticket.html", {'data1' : data1})

            else:
                return render(request, "NoClosable.html", {'data2' : data2})

        except FileNotFoundError:
            return render(request, "NoClosable.html", {'data2' : data2})
        

def closeticket(request):

    from login import responder_problem

    class Data1:

        def __init__(self, ticket):

            self.ticket= ticket


    class Data2:

        def __init__(self, email):

            self.email = email

    if request.method == "GET":

        e = request.session.get('email')
        data1 = []
        data2 = []

        data2.append(Data2(e))
        problem = responder_problem(e)

        try:

            with open(f"to_address/{problem}.json", 'r') as file:
               file.seek(0)
               details = json.load(file)
            
            if details != []:

                for item in details:
                    data1.append(Data1(item['Name'] + " , " + item['Email'] + " , " + item['Date'] + " , " + item['Time'] + " , " + item['Help Topic'] + " , " + item['Issue Summary'] + " , " + item['Problem'] + " , " + item['Location'] + " , " + item['Details'] + " , " + item['Number']))

                return render(request, "CloseTicket.html", {'data1' : data1})
        
            else:
                return render(request, "NoClosable.html", {'data2' : data2})

        except FileNotFoundError:
            return render(request, "NoClosable.html", {'data2' : data2})
        

def close_ticket(request):

    from command import driver_code
    from login import responder_problem
    from mail import Sending_Mail

    if request.method == "POST":

        e = request.session.get('email')
        problem = responder_problem(e)

        ticket = request.POST['ticket']
        item = ticket.split( " , ")

        message = "This email is to inform you that the ticket with the following \
details has been closed by SPEEDY SUPPORT service  personnel:-<br>" +\
f"Help Topic : {item[4]}" + "<br>" +\
f"Issue Summary : {item[5]}" + "<br>" +\
f"Detail on the reason(s) for opening the ticket : {item[6]}" + "<br>" +\
f"Location : {item[7]}" + "<br>" +\
f"Department / Hostel Number & Room Number : {item[8]}" + "<br>" +\
f"Mobile Number : {item[9]}" + "<br>"

        Sending_Mail(item[1], "Ticket Closed at SPEEDY SUPPORT", message)

        condn = True
        no = 1
        filename = f'PDPHTS_App/static/reports/{item[1]}_ticket{no}.txt'

        while condn:
            try:
                f = open(filename)
            except FileNotFoundError:
                filename = f'PDPHTS_App/static/reports/{item[1]}_ticket{no}.txt'
                condn = False
            else:
                 no += 1
                 filename = f'PDPHTS_App/static/reports/{item[1]}_ticket{no}.txt'

        print(filename)

        with open(filename, 'w') as f:

            f.write('TICKET DETAILS\n')
            f.write(f'Name : {item[0]}' + '\t\t\t' + f'Email ID : {item[1]}\n')
            f.write('Date : ' + item[2]+ '\n')
            f.write('Time : ' + item[3]+ '\n') 
            f.write('Help Topic : ' + item[4]+ '\n') 
            f.write('Issue Summary : ' + item[5]+ '\n') 
            f.write('Problem : ' + item[6]+ '\n')
            f.write('Location : ' + item[7]+ '\n')
            f.write('Details : ' + item[8]+ '\n')
            f.write('Contact Number : ' + item[9]+ '\n')
        
        driver_code(f"to_address/{problem}.json", f"active_ticket/{item[1]}_activeticket.json", item[4], item[5], item[6], item[7], item[8], item[9], item[2], item[3], f"closed_ticket/{item[1]}_closedticket.json")

        return render(request, "Responder.html")


def support(request):

    if request.method == "GET":

        return render(request, "Support.html")


def contact(request):

    if request.method == "GET":

        return render(request,"Contact.html")
