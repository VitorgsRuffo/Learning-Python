# Topics: static methods, method overriding.

class Customer:

    # Constructor method that is invoked when an object is created (instantiated) from the class.
    # this method initializes the attributes of the just created object.
    def __init__(self, id_num, name, membership):
        self.id_num = id_num
        self.name = name
        self.membership = membership

    def update_membership(self, new_membership):
        self.membership = new_membership

    # static method: a method that does not operate on customer objects but is related to the customer class.
    # It cannot be invoked by a customer object but only by referencing the class.
    @staticmethod
    def read_customer_from_db():
        print("Reading costumer from db...")

    @staticmethod
    def print_customers(customers):
        for customer in customers:
            print(customer)

    # Overriding methods: __str__ is a class method that has a built-in definition.
    #                     It simply returns a string representation of the object self.
    #                     We are able to override it so that it can better describe Customer objects.
    #                     It is invoked when we refer to an object.
    #
    def __str__(self):
        return "(" + str(self.id_num) + ") " + self.name + " - " + self.membership

    # Another built-in method that we can override in order to make this functionality specific to the Customer class.
    # The default definition of this method would compare the two objects by memory address.
    def __eq__(self, other):
        return self.id_num == other.id_num


c = Customer(1550, "Vitor", "gold")
print(c.name, c.membership)

c2 = Customer(1401, "Tom", "Silver")
print(c2.name, c2.membership)

Customer.read_customer_from_db()
Customer.print_customers([c, c2])

print(c)
print(c2)

# when we use the == operator for two objects of the same class their __eq__ method is implicitly invoked.
print(c == c2)
c2.id_num = 1550
print(c == c2)

#30:55