from datetime import datetime
date_format="%d-%m-%Y"
CATEGORIES={"I":"income","E":"expenses"}
def get_date(promt,allow_default=False):
    date_str=input(promt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date=datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("invalid date format . plese enter the date in dd-mm-yyyy fromat"
              )
        return get_date(promt,allow_default)
    
    
    
    
    
def get_amount():
    try:
        amount=float(input("enter the amount: "))
        if amount<=0:
            raise ValueError("amount should be positive not negtive and non zero value")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
def get_category():
    category=input("enter the category ('I' for income or 'E' for expenses) ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    print("invalid catergory please enter 'I' for income or 'E' for expenses ")
    return get_category()

def get_description():
    return input("Enter a description (optinal):  ")