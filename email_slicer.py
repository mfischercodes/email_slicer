''' Get user email name. Output registered with Google, Yahoo etc... 
or if custom domain name then say custom domain name '''

#popular email domains with their corresponding company name
popular_domains = {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

#get user's email address
user_email = input("What is your email address? ")

#seperate the email address into the name and the domain without .com / .ca
user_name = user_email.split('@')[0]
user_domain = user_email.split('@')[-1]
user_domain = user_domain.split('.')[0]

#if user's domain is in the popular domains keys then print the keys value
#else print user_domain as the custom domain name
if user_domain in popular_domains.keys():
    print(f"Hey {user_name} it seems like your email is registered with {popular_domains[user_domain]}!")
else:
    print(f"Hey {user_name} it seems like you have your own custom domain at {user_domain}!")

