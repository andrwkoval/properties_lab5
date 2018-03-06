def get_valid_input(input_string, valid_options):
    """
    (str, str) -> str
    Checks if the input is correct
    param input_string: a message for input
    param valid_options: valid input to check with
    returns: a correct input for using in further functions
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Represents property and is a superclass of House and Apartment
    """

    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        """Initializes the main features of the property"""
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """Shows property details and features"""
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        """Static method which is used to create dictionary with class
        property features as keys and user inputs as values."""
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Represents an apartment as a subclass of property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """Initializes all the features of apartment."""
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """Shows all the apartment details and features, including that are not
        common with property."""
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        """Creates a dict to represent apartment features and updates unique
        new features."""
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does "
                                  "the property have? ",
                                  Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Represents an apartment as a subclass of property
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        """Initializes all the features of the house."""
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """Shows all the house details and features, including that are not
        common with property."""
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """Creates a dict to represent house features and updates unique
        new features."""
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """
    Represents purchase with details, like price or taxes.
    """

    def __init__(self, price='', taxes='', **kwargs):
        """Initializes the details of the purchase."""
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """Show all the purchase details, like price or taxes."""
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """Creates dict to represent purchase info."""
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Represents rental with details, like rent, utilities and so on.
    """

    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        """Initializes the details of the rental."""
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """Show all the rental details, like rent or utilities."""
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(
            self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """Creates dict to represent rental info."""
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input(
                "What are the estimated utilities? "),
            furnished=get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    """
    Represents a rental of a house using classes Rental and House
    """

    def prompt_init():
        """
        Combines prompt_init of House and Rental into one dictionary.
        returns: dict with house rental info
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Represents a rental of an apartment using classes Apartment and Rental
    """

    def prompt_init():
        """
        Combines prompt_init of Apartment and Rental into one dictionary.
        returns: dict with apartment rental info
        """
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Represents a purchase of an apartment using classes Apartment and Purchase
    """

    def prompt_init():
        """
        Combines prompt_init of Apartment and Purchase into one dictionary.
        returns: dict with apartment purchase info
        """
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Represents a purchase of a House using classes House and Purchase
    """

    def prompt_init():
        """
       Combines prompt_init of House and Purchase into one dictionary.
       returns: dict with house purchase info
       """
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Represents an agent which is the main class and is used for doing all
    the important actions.
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        """Initializes a property list"""
        self.property_list = []

    def display_properties(self):
        """Method is used to display all the properties"""
        for property in self.property_list:
            property.display()

    def add_property(self):
        """Method is used to add the property to property list"""
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]
        init_args = PropertyClass.prompt_init()

        self.property_list.append(PropertyClass(**init_args))

    def remove_property(self):
        """Method is used to delete property from property list."""
        try:
            print("Here are all the properties")

            for x, y in enumerate(self.property_list):
                print("Property number\n" + str(x + 1) + ".")
                y.display()

            del self.property_list[int(input("Choose property to del: ")) - 1]
        except ValueError:
            print("Enter valid index!")
            self.remove_property()

    def change_workplace(self):
        """Agent changes the workplace, all the properties are deleted."""
        self.property_list.clear()
        print("Okey, now I am free, but I should find a new work.")

