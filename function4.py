class intern():
    def __init__(self,firstname,lastname,address,phone,email):
        self.first_name = firstname
        self.last_mame = lastname
        self.address = address
        self.mobile_number = phone
        self.email = email
        
        
    def putdata(self):
        return new_intern.getdata()

    def getdata(self):      
#name = intern("champ","quobbi","g51","02465577","champ123@gmail.com")
        self.first_name = input('enter firstname : ')
        self.last_mame  = input('enter last name : ')
        self.address = input('enter address : ')
        self.mobile_number = input('enter phonr number : ')
        self.email = input('enter email : ')
        print("firstname :",self.first_name,"lastname:", self.last_mame,"address",self.address,"phone: ",self.mobile_number,"email: ",self.email)
new_intern= intern('champ','quobbi','g21','0254785','7685567')
#print(new_intern.getdata())
print(intern.putdata(1))