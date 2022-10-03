class Intern():
    def __init__(self, first_name,last_name,address,mobile_number,e_mail):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.mobile_number=mobile_number
        self.e_mail=e_mail

        

    def getdata(self):

        print("Enter first_name")
        self.first_name = input()
        print("Enter last_name")
        self.last_name = input()
        print("Enter address")
        self.address = input()
        print("Enter mobile_number")
        self.mobile_number = input()
        print("Enter e_mail")
        self.e_mail = input()
      

   


print(Intern.getdata('s'))