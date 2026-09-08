email=input("enter email address: ")
username,domain=email.split('@')
reversed_domain=domain[::-1]
print(username)
print(domain)
print(reversed_domain)

