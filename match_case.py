while True:
  drink = input("What drink do you want?")
  def selection(drink):
   match drink:
     case "Pepsi":
       return 2000
     case "Mango juice":
       return "3000"
     case "Water":
       return "1000"
     case _:
       return 0
  break
print(selection(drink))