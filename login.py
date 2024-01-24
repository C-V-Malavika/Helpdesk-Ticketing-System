import pickle

class Student:

    '''
    Class Student - representation of a student.
    Data Members - name, email, password.
    Member function - write_to_file : which writes the
    student object to a binary file using pickle.
    '''

    def __init__(self, name, email, password):

        self._name = name
        self._email = email
        self._password = password


    def write_to_file(self):

        with open('student_login.txt', 'ab') as f:

            pickle.dump(self, f)


class Responder:

    '''
    Class Responder - representation of the responder.
    Data Members - email, password.
    Member function - write_to_file : which writes the
    responder object to a binary file using pickle.
    '''

    def __init__(self, email, password):

        self._email = email
        self._password = password


    def write_to_file(self):

        with open('responder_login.txt', 'ab') as f:

            pickle.dump(self, f)


class Faculty:

    '''
    Class Faculty - representation of a student.
    Data Members - name, email, password.
    Member function - write_to_file : which writes the
    faculty object to a binary file using pickle.
    '''

    def __init__(self, name, email, password):

        self._name = name
        self._email = email
        self._password = password


    def write_to_file(self):

        with open('faculty_login.txt', 'ab') as f:

            pickle.dump(self, f)


def student_verify_login(email, password):

    '''The student_verify_login function is used to verify
    the login credentials of a student.

    Parameters - email and password

    Checks if they match with the stored email and password
    in the binary file 'student_login.txt'.

    If the email and password match, returns 'Login Successful'.
    If the email matches but the password does not, returns 'Invalid password',
    '''

    with open('student_login.txt', 'rb') as f:

        try:
            while True:
                content = pickle.load(f)

                if content._email == email and content._password != password:
                    return 'Invalid password'

                elif content._email == email and content._password == password:
                    return 'Login Successful', content._name

        except EOFError:
            pass

        return 'Invalid Student email'


def responder_verify_login(email, password):

    '''The responder_verify_login function is used to verify
    the login credentials of the responder.

    Parameters - email and password

    Checks if they match with the stored email and password
    in the binary file 'responder_login.txt'.

    If the email and password match, returns 'Login Successful'.
    If the email matches but the password does not, returns 'Invalid password',
    '''

    with open('responder_login.txt', 'rb') as f:

        try:
            while True:
                content = pickle.load(f)

                if content._email == email and content._password != password:
                    return 'Invalid password'

                elif content._email == email and content._password == password:
                    return 'Login Successful'

        except EOFError:
            pass

        return 'Invalid Responder email'


def faculty_verify_login(email, password):

    '''The faculty_verify_login function is used to verify
    the login credentials of a faculty.

    Parameters - email and password

    Checks if they match with the stored email and password
    in the binary file 'faculty_login.txt'.

    If the email and password match, returns 'Login Successful'.
    If the email matches but the password does not, returns 'Invalid password',
    '''

    with open('faculty_login.txt', 'rb') as f:

        try:
            while True:
                content = pickle.load(f)

                if content._email == email and content._password != password:
                    return 'Invalid password'

                elif content._email == email and content._password == password:
                    return 'Login Successful', content._name

        except EOFError:
            pass

        return 'Invalid Faculty email'


def responder_problem(email):

    d = {'sharmilaguduva73@gmail.com' : 'AC-Problem', 
        'valuerchandrakani@gmail.com' : 'Academic ERP & LMS Related', 
        'rckani@hotmail.com' : 'Attendance System',
        'cvmkani04@gmail.com' : 'Cafeteria', 
        'vijayalakshmikani@gmail.com' : 'Carpentery', 
        'nkmadhukrishaa@gmail.com' : 'CCTV & AV problem', 
        'ndkrish@rediffmail.com' : 'Civil - Mason', 
        'cvmalavika@gmail.com' : 'Electrical', 
        'mlmd0906@gmail.com' : 'House Keeping', 
        'nadesanmanish23903@gmail.com' : 'Painting, Plumbing', 
        'krishnanmallika2003@gmail.com' : 'RO - Problem', 
        'srinivasaelectricals637211@gmail.com' : 'Stores, Table, Chair requisition', 
        'nandanamanikandan.04@gmail.com' : 'Telephone - Intercom problem, Wifi - LAN Internet', 
        'manjusri2306@gmail.com' : 'Transport', 
        'padmapriya.chakravarthy@gmail.com' : 'Printer, Scanner, Projector, Desktop, Laptop, UPS-Problem'}
    
    return d[email]


def responder_dict():

    d = {'sharmilaguduva73@gmail.com' : 'AC-Problem', 
        'valuerchandrakani@gmail.com' : 'Academic ERP & LMS Related', 
        'rckani@hotmail.com' : 'Attendance System',
        'cvmkani04@gmail.com' : 'Cafeteria', 
        'vijayalakshmikani@gmail.com' : 'Carpentery', 
        'nkmadhukrishaa@gmail.com' : 'CCTV & AV problem', 
        'ndkrish@rediffmail.com' : 'Civil - Mason', 
        'cvmalavika@gmail.com' : 'Electrical', 
        'mlmd0906@gmail.com' : 'House Keeping', 
        'nadesanmanish23903@gmail.com' : 'Painting, Plumbing', 
        'krishnanmallika2003@gmail.com' : 'RO - Problem', 
        'srinivasaelectricals637211@gmail.com' : 'Stores, Table, Chair requisition', 
        'nandanamanikandan.04@gmail.com' : 'Telephone - Intercom problem, Wifi - LAN Internet', 
        'manjusri2306@gmail.com' : 'Transport', 
        'padmapriya.chakravarthy@gmail.com' : 'Printer, Scanner, Projector, Desktop, Laptop, UPS-Problem'}
    
    return d


# if __name__ == '__main__':

    # s1 = Student('C.V.Malavika', 'malavika2210770@ssn.edu.in', '1234')
    # s2 = Student('N.K.Madhukrishaa', 'madhukrishaa2210381@ssn.edu.in', 'krishaa04')
    # s3 = Student('M.Madhusudhanan', 'madhusudhanan2210528@ssn.edu.in', 'madhu@2003');
    # s4 = Student('N.K.Manish Kumar', 'manishkumar2210595@ssn.edu.in', 'manish@2002')
    # s5 = Student('A.Piriyadharshini', 'piriyadharshini2210418@ssn.edu.in', 'pdk164')
    # s6 = Student('R.Mohanakrishanaa', 'mohanakrishnaa2210701@ssn.edu.in', 'mohan@2004')
    # s7 = Student('Meduri Ujwal Sai', 'meduri2210112@ssn.edu.in', 'ujwal@2004')
    # s8 = Student('S.Paranthagan', 'paranthagan2210656@ssn.edu.in', 'paranthagan@2004')
    # s9 = Student('C.Padmapriya', 'padmapriya2210328@ssn.edu.in', 'pc1904')
    # s10 = Student('M.Nandana', 'nandana2210390@ssn.edu.in', 'nandhu04')

    # s1.write_to_file()
    # s2.write_to_file()
    # s3.write_to_file()
    # s4.write_to_file()
    # s5.write_to_file()
    # s6.write_to_file()
    # s7.write_to_file()
    # s8.write_to_file()
    # s9.write_to_file()
    # s10.write_to_file()

    # r1 = Responder('cvmalavika@gmail.com', '1234')
    # r2 = Responder('valuerchandrakani@gmail.com', 'rk76')
    # r3 = Responder('rckani@hotmail.com', '4567')
    # r4 = Responder('cvmkani04@gmail.com', '123#')
    # r5 = Responder('vijayalakshmikani@gmail.com', 'v1234')
    # r6 = Responder('nkmadhukrishaa@gmail.com', '12345') # Madhukrishaa
    # r7 = Responder('ndkrish@rediffmail.com', 'nd12345') # Madhukrishaa
    # r8 = Responder('sharmilaguduva73@gmail.com', 'sh12345') # Madhukrishaa
    # r9 = Responder('mlmd0906@gmail.com', 'mu0906') # Muthulakshmi
    # r10 = Responder('nadesanmanish23903@gmail.com', '23903') # Manish
    # r11 = Responder('krishnanmallika2003@gmail.com', '1234$') # Manish
    # r12 = Responder('srinivasaelectricals637211@gmail.com', '123567') # Manish
    # r13 = Responder('nandanamanikandan.04@gmail.com', 'nad1234') # Nandana
    # r14 = Responder('manjusri2306@gmail.com', 'manju') # Manjusri
    # r15 = Responder('padmapriya.chakravarthy@gmail.com', 'padma@2004') # Padmapriya

    # r1.write_to_file()
    # r2.write_to_file()
    # r3.write_to_file()
    # r4.write_to_file()
    # r5.write_to_file()
    # r6.write_to_file()
    # r7.write_to_file()
    # r8.write_to_file()
    # r9.write_to_file()
    # r10.write_to_file()
    # r11.write_to_file()
    # r12.write_to_file()
    # r13.write_to_file()
    # r14.write_to_file()
    # r15.write_to_file()

    # f1 = Faculty('S.Karthika', 'skarthika@ssn.edu.in', '1234')
    # f2 = Faculty('K.S.Gayathri', 'gayathriks@ssn.edu.in', '12345')

    # f1.write_to_file()
    # f2.write_to_file()