# Strategy Design Pattern

from datetime import datetime
import json


# Default Strategy class
class Strategy_class:

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):
        pass


class AC_Problem(Strategy_class):

    '''
    If AC_Problem is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'AC-Problem.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class ERP_LMS(Strategy_class):

    '''
    If ERP_LMS is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Academic ERP & LMS Related.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Attendance(Strategy_class):

    '''
    If Attendance is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Attendance System.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Cafeteria(Strategy_class):

    '''
    If Cafeteria is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):
        
        problem_file_name = 'Cafeteria.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Carpentry(Strategy_class):

    '''
    If Carpentry is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Carpentry.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class CCTV_AV(Strategy_class):

    '''
    If CCTV_AV is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'CCTV & AV problem.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Civil_Mason(Strategy_class):

    '''
    If Civil_Mason is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Civil - Mason.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Electrical(Strategy_class):

    '''
    If Electrical is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Electrical.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class House_Keeping(Strategy_class):

    '''
    If House_Keeping is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'House Keeping.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Painting_Plumbing(Strategy_class):

    '''
    If Painting_Plumbing is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Painting, Plumbing.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class RO_Problem(Strategy_class):

    '''
    If RO_Problem is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'RO - Problem.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Furniture_requirement(Strategy_class):

    '''
    If Furniture_requirement is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Stores, Table, Chair requisition.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Telephone_Wifi_LAN(Strategy_class):

    '''
    If Telephone_Wifi_LAN is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Telephone - Intercom problem, Wifi - LAN Internet.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Transport(Strategy_class):

    '''
    If Transport is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Transport.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Electronics(Strategy_class):

    '''
    If Electronics is chosen, an instance will be created for
    this class and this class object is passed as an attribute to 
    the Context class to fetch the problem details from the user
    '''

    def fill_details(name, email, self, help_topic, issue_summary, problem, location, details, number, file_name):

        problem_file_name = 'Printer, Scanner, Projector, Desktop, Laptop, UPS-Problem.json'

        fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


class Context:

    '''
    The ticket class' functions are accessed from the
    Context class
    '''

    def __init__(self, pb_type):

        self.Pb_Type = pb_type


    '''The problem description is obtained from the html forms
    and sent as a parameter to the fill_details'''

    def spec_pb(self, name, email, help_topic, issue_summary, problem, location, details, number, file_name):

        self.Pb_Type.fill_details(name, email, help_topic, issue_summary, problem, location, details, number, file_name)


def check(problem):

    '''
    This function definition is used to create an object
    for the respective tickets class (problem)
    '''

    if problem == 'AC-Problem':
        AC_Problem_obj = AC_Problem()
        return AC_Problem_obj
    
    elif problem == 'Academic ERP & LMS Related':
        ERP_LMS_obj = ERP_LMS()
        return ERP_LMS_obj
    
    elif problem == 'Attendance System':
        Attendance_obj = Attendance()
        return Attendance_obj
    
    elif problem == 'Cafeteria':
        Cafeteria_obj = Cafeteria()
        return Cafeteria_obj
    
    elif problem == 'Carpentry':
        Carpentry_obj = Carpentry()
        return Carpentry_obj
    
    elif problem == 'CCTV & AV problem':
        CCTV_AV_obj = CCTV_AV()
        return CCTV_AV_obj
    
    elif problem == 'Civil - Mason':
        Civil_Mason_obj = Civil_Mason()
        return Civil_Mason_obj
    
    elif problem == 'Electrical':
        Electrical_obj = Electrical()
        return Electrical_obj
    
    elif problem == 'House Keeping':
        House_Keeping_obj = House_Keeping()
        return House_Keeping_obj
    
    elif problem == 'Painting, Plumbing':
        Painting_Plumbing_obj = Painting_Plumbing()
        return Painting_Plumbing_obj
    
    elif problem == 'RO - Problem':
        RO_Problem_obj = RO_Problem()
        return RO_Problem_obj
    
    elif problem == 'Stores, Table, Chair requisition':
        Furniture_requirement_obj = Furniture_requirement()
        return Furniture_requirement_obj
    
    elif problem == 'Telephone - Intercom problem, Wifi - LAN Internet':
        Telephone_Wifi_LAN_obj = Telephone_Wifi_LAN()
        return Telephone_Wifi_LAN_obj
    
    elif problem == 'Transport':
        Transport_obj = Transport()
        return Transport_obj
    
    elif problem == 'Printer, Scanner, Projector, Desktop, Laptop, UPS-Problem':
        Electronics_obj = Electronics()
        return Electronics_obj
    

def fill_details_contd(name, email, help_topic, issue_summary, problem, location, details, number, file_name):

    '''
    This function definition is used to write the
    details into the json file

    file_name - it will have the name of the file to be opened

    For each type of problem, a separate file is being created
    whenever the respective ticket class is used
    '''

    x = datetime.now()
    x = str(x)
    x = x.split(' ')

    d = {'Name' : name, 
         'Email' : email, 
         'Date' : x[0],
         'Time' : x[1].split('.')[0],
         'Problem' : problem,
         'Help Topic' : help_topic,
         'Issue Summary' : issue_summary,
         'Location' : location,
         'Details' : details,
         'Number' : number}
        
    l = [d]

    try:

        with open(file_name, 'a+') as file:
            file.seek(0)
            details = json.load(file)

        details += l

        with open(file_name, 'w') as file1:
            json.dump(details, file1, indent = 2)
            
    except ValueError:

        with open(file_name, 'w') as file1:
            json.dump(l, file1, indent = 2)

# Driver code
def driver_code(name, email, help_topic, issue_summary, problem, location, details, number, file_name):
        
    # The ticket type(problem) is chosen from the dropdown list

    ans = check(problem)  # creates the object for the respective ticket class
    context = Context(ans)  # object creation for class Context
    context.spec_pb(name, email, help_topic, issue_summary, problem, location, details, number, file_name) # calls the function which is present inside the ticket class 

# driver_code('Plug point is not working', '', 'Electrical', 'Ladies Hostel', 'LH-1 & A-66', '+91 72000 68373', 'malavika2210770@ssn.edu.in_activeticket.json')
