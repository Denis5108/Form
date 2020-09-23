
class Form:
  def __init__(self, name, age, password):
    self.name = name
    self.age  = age
    self.password = password
  def getAge(self):
    self.age = int(input("What is your age: "))
  def getUserName(self):
    self.name = str(input("Please enter your name: "))
  def setPassword(self, password):
    self.password = password
  def getPassword(self):
    self.password = int(input("Please enter your password: "))
  def submitForm(self):
    print("form submitted")
  def displayForm(self):
    print("Welcome: {}, age: {}, password: {}".format(self.name, self.age, self.password))

def main():
  # Create objects called form
  form1 = Form("Daniel", 21, 2376)
  form2 = Form("Peter", 19, 3456)
  form3 = Form("Davis", 35, 2030)
  form4 = Form("Max", 26, 9917)
  form5 = Form("Kevin", 8, 1936)

  # put the objects inside of a tuple
  forms = (form1, form2, form3, form4, form5)

  # get the name of the user
  for name in forms:
    print(name.getUserName())

  # get the age of the user
  for age in forms:
    print(age.getAge())
  
  # get the password for the user
  for password in forms:
    print(password.getPassword())

  # display the information
  for obj in forms:
    print(obj.displayForm())
  

  # delete the tuple
  del forms
  
main()