# Command Design Pattern

from datetime import datetime
import json

# Command Interface
class Command:
    def execute(self, help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile):
        pass

# Concrete Command
class CloseTicket(Command):
    def __init__(self, user):
        self.User = user

    def execute(self, help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile):
        self.User.execute(help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile)

# Receiver
class Close_Ticket_Functions:

    def __init__(self, file_name_1, file_name_2):
        self.file1 = file_name_1
        self.file2 = file_name_2

    def get_help_entries(self, file_name):

        with open(file_name, 'r') as file:
            data = json.load(file)
        return data

    def save_help_entries(self, help_entries, file_name):

        with open(file_name, 'w') as file:
            json.dump(help_entries, file, indent=2)

    def execute(self, help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile):
        
        self.close_ticket(help_topic, issue_summary, problem, location, details, number, self.file1, self.file2, dt, time, user_closedticketjsonfile)

    def close_ticket(self, help_topic, issue_summary, problem, location, details, number, file_name1, file_name2, dt, time, user_closedticketjsonfile):

        '''
        This function definition is used to write the
        details into the json file

        file_name1 - file name of the Addresser file
        file_name2 - file name of the user's activeticket file
        
        For each type of problem, a separate file is being created
        whenever the respective ticket class is used
        '''

        help_entries = self.get_help_entries(file_name1)

        for ticket in help_entries:
            if (ticket['Date'] == dt and ticket['Time'] == time
                and ticket['Problem'] == problem and ticket['Help Topic'] == help_topic
                and ticket['Issue Summary'] == issue_summary and ticket['Location'] == location
                and ticket['Details'] == details and ticket['Number'] == number):

                help_entries.remove(ticket)

        self.save_help_entries(help_entries, file_name1)

        user_help_entries = self.get_help_entries(file_name2)

        for ticket in user_help_entries:

            if (ticket['Date'] == dt and ticket['Time'] == time
                and ticket['Problem'] == problem and ticket['Help Topic'] == help_topic
                and ticket['Issue Summary'] == issue_summary and ticket['Location'] == location
                and ticket['Details'] == details and ticket['Number'] == number):
                
                # file_name = user's closed ticket file name
                file_name = user_closedticketjsonfile

                self.fill_details_closed_ticket(help_topic, issue_summary, problem, location, details, number, file_name)
                user_help_entries.remove(ticket)

        self.save_help_entries(user_help_entries, file_name2)
            

    def fill_details_closed_ticket(self, help_topic, issue_summary, problem, location, details, number, file_name):

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

        d = {'Date' : x[0],
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


# Invoker
class CommandInvoker:

    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def execute_commands(self, help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile):
        self.command.execute(help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile)


def driver_code(addresser_jsonfile, user_openticketjsonfile, help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile):

    ct = Close_Ticket_Functions(addresser_jsonfile, user_openticketjsonfile)
    close_ticket = CloseTicket(ct)

    user = CommandInvoker()
    user.set_command(close_ticket)

    user.execute_commands(help_topic, issue_summary, problem, location, details, number, dt, time, user_closedticketjsonfile)

# driver_code('Electrical.json', 'malavika2210770@ssn.edu.in_activeticket.json', "Plug point is not working", "", "Electrical", "Ladies Hostel", "LH-1 & A-66", "+91 72000 68373", "2023-12-25", "16:29:49", 'malavika2210770@ssn.edu.in_closedticket.json')