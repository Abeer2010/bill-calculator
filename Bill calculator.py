class parent():
    def __init__(self):
        print("This is the parent class")
        
    def menu(dish):
        if dish=="burger":
            print("You can add the following toppings")
            print("Extra Cheese/Add Jalapenos")
        elif dish=="iced_americano":
            print("You can add the following toppings")
            print("Add chocolate flavour/Add caramel flavour")
        else:
            print("please enter a valid dish name")

    def final_amounts(dish,add_ons):
         if dish=="burger" and add_ons=="cheese":
            print("you have to pay 250$")
         elif dish=="burger" and add_ons=="jalapenos":
            print("you have to pay 350$")
         elif dish=="iced_americano" and add_ons=="chocolate":
            print("you have to pay 250$")
         elif dish=="iced_americano" and add_ons=="caramel":
            print("you have to pay 450$")
            
class child1(parent):
    def __init__(self,dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)

class child2(parent):
    def __init__(self,dish,addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amounts(self.new_dish,self.addons)
        
child1_object = child1("burger")
child1_object.get_menu()

child2_object = child2("burger","jalapenos")
child2_object.get_final_amount()

        