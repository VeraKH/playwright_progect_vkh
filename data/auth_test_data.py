
valid_user = {
    "email": "customer@practicesoftwaretesting.com",
    "password": "welcome01",
    "name": "Jane Doe"
}

#1 positive user data

valid_users = [
     ({"email": "customer@practicesoftwaretesting.com", "password": "welcome01"}, "Jane Doe")
]

#2 positive admin data
valid_admin = [
    ({"email": "admin@practicesoftwaretesting.com", "password": "welcome01"}, "Sales over the years")
]

#3 wrong_email
invalid_email_data = [
     ({"email": "wrong_email@practicesoftwaretesting.com", "password": "welcome01"}, "Invalid email or password")
]

#4 wrong_password
invalid_password_data = [
     ({"email": "customer@practicesoftwaretesting.com", "password": "wrong_password"}, "Invalid email or password")
]

#5 wrong_email_and_password
invalid_email_and_password_data = [
    ({"email": "wrong_email@practicesoftwaretesting.com", "password": "wrong_password"}, "Invalid email or password")
]

#6 empty email field
empty_email_cases = [
    ({"email": "", "password": "welcome01"}, "Email is required")
]

#7 empty password field
empty_password_cases = [
    ({"email": "customer@practicesoftwaretesting.com", "password": ""}, "Password is required")
]

#8 empty email and password fields
empty_both_cases = [
    ({"email": "", "password": ""}, "Email is required", "Password is required")
]

#9 ALL capslook in Email
caps_look_email = [
    ({"email": "CUSTOMER@PRACTICESOFTWARETESTING.COM", "password": "welcome01"}, "Jane Doe")
]

#10 ALL capslook in Password
caps_look_password = [
    ({"email": "customer@practicesoftwaretesting.com", "password": "WELCOME01"}, "Invalid email or password")
]

#11 Various register in Email
small_and_caps_email = [
    ({"email": "CuStOmEr@PRACTiCESoFTWArETESTInG.COM", "password": "welcome01"}, "Jane Doe")
]

#12 Various register in Password
small_and_caps_password = [
    ({"email": "customer@practicesoftwaretesting.com", "password": "WeLcOMe01"}, "Invalid email or password")
]

# 13 Valid email
valid_emails = [
    "test@example.com",
    "user.name+tag@domain.co.uk",
    "email@123.123.123.123",
]

# 14 Invalid email
invalid_emails = [
    "user@@example.com",
    "plainaddress",
    "user' OR '1'='1@example.com",
]