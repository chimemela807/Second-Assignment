#Robust Password and Username Validator
Special_chars="!@#$%^&*(){}[]|/\?<>':;~`-_=+"
def validate_credentials(username,password):
    result={
        "username":"Valid",
        "password":"Correct",
        "errors":[]
    }
    username_errors=[]
    password_errors=[]
    #Guide for Username Input
    if len(username)<6:
        username_errors.append("Username must be at least 6 characters long❗.")
    if " " in username:
        username_errors.append("Username must not contain space❕.")
    if not username[0].isalpha:
        username_errors.append("Username must start with a letter❕.")
    
    #Guide for Password Input
    if len(password)<8:
        password_errors.append("Password must be at least 8 characters long.")
    hasupper=False
    haslower=False
    hasdigit=False
    hasspecial=False

    for char in password:
        if char.isalpha():
            if char.isupper():
                hasupper=True
            else:
                haslower=True
        elif char.isdigit():
            hasdigit=True
        else:
            if char in Special_chars:
                hasspecial=True
    if not hasupper:
        password_errors.append("Password must contain at least 1 uppercase letter,A-Z.")
    if not haslower:
        password_errors.append("Password must have at least 1 lowercase letter,a-z.")
    if not hasdigit:
        password_errors.append("Password must contain at least 1 digit,0-9")
    if not hasspecial:
        password_errors.append("Password must have at least 1 special character")
    valid_username=len(username_errors)==0
    valid_password=len(password_errors)==0
    return{
        "Valid username":valid_username,
        "Valid password":valid_password,
        "Generally valid":valid_username and valid_password,
        "Invalid username":username_errors,
        "Invalid password":password_errors,
    }
def generate_suggestion(password):
    #Provides ideas or tips for a valid password
    suggestion=[]
    if len(password)<8:
        missing=8-len(password)
        suggestion.append(f"Add {missing} more character(s), minimum of 8 characters.")
    hasupper=False
    haslower=False
    hasdigit=False
    hasspecial=False

    for char in password:
        if char.isalpha():
            if char.isupper():
                hasupper=True
            else:
                haslower=True
        elif char.isdigit():
            hasdigit=True
        else:
            if char in Special_chars:
                hasspecial=True
    if not hasupper:
        suggestion.append("Add an uppercase letter(A-Z)")
    if not haslower:
        suggestion.append("Add a lowercase letter(a-z)")
    if not hasdigit:
        suggestion.append("Add a digit (0-9)")
    if not hasspecial:
        suggestion.append("Include a special character(,!,@,#,%,^)")
    if not suggestion:
        suggestion.append("Password meets all requirements✅, for extra security make it longer❗")
    return suggestion

#Test with Six(6) Different Combination
Tests=[
    ("NOv@1256","Gi3na$girl"),
    ("joyce#500","alaN@2005"),
    ("Sonia_123","sonia9"),
    (" Jane","jalE@04"),
    ("KayC","OKARO"),
    ("_Fargo","3478@100%")
]
for i,(username,password) in enumerate(Tests,start=1):
    print(f"\nTests{i}")
    print(f"Username:{username}\nPassword:{password}")
    validation=validate_credentials(username,password)
    print(f"Generally valid:{validation['Generally valid']}")
    if validation["Generally valid"]:
        print("\nYou have entered correctly✅")
    if validation["Invalid username"]:
        print(f"\nUsername errors:")
        for err in validation["Invalid username"]:
            print(f"-{err}")
    if validation["Invalid password"]:
        print("\nPassword errors:")
        for err in validation["Invalid password"]:
            print(f"-{err}")
    if not validation["Valid password"]:
        print("\nSuggestions to improve password:")
        for guide in generate_suggestion(password):
            print(f"-{guide}")