def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, amount):
    cc_pet_shop["admin"]["total_cash"] += amount

    
# def add_or_remove_cash(cc_pet_shop, amount):
#     cc_pet_shop["admin"]["total_cash"] -= amount



def get_pets_sold(cc_pet_shop):
    pets_sold = cc_pet_shop["admin"]["pets_sold"]
    return pets_sold

def increase_pets_sold(cc_pet_shop, num1):
    cc_pet_shop["admin"]["pets_sold"] += num1


def get_stock_count(cc_pet_shop):
    stock_count = len(cc_pet_shop["pets"])
    return(stock_count)


def get_pets_by_breed(cc_pet_shop, breed):
    pets = []
    for pet_breed in cc_pet_shop["pets"]:
        if pet_breed["breed"] == breed:
            pets.append(pet_breed)
    return pets

def get_pets_by_breed(cc_pet_shop, breed):
    pets = []
    for pet_not_found in cc_pet_shop["pets"]:
        if pet_not_found["breed"] == breed:
            pets.append(pet_not_found)
    return pets

def find_pet_by_name(cc_pet_shop, name):
    found_pet = None
    for pet in cc_pet_shop["pets"]:
        if pet["name"] == name:
            found_pet = pet
    return found_pet

# def




def remove_pet_by_name(cc_pet_shop, name):
    pets = cc_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == name:
            del pets[pets.index(pet)]
            del pets[4]


# def add_pet_to_stock(cc_pet_shop, new_pet):
#    COPY/MOVE new_pet dictionary into dict with other pets?
    



def get_customer_cash(customers):
    return customers["cash"]


# def remove_customer_cash(customers, cash_amount):
#     customers.remove["cash"](cash_amount)


def get_customer_pet_count(customers):
    pet_count = len(customers["pets"])
    return(pet_count)

# def add_pet_to_customer(customers):
