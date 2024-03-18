#get user email address

email = input("What's your email address?: ").strip()

#slice out user name

username = email[:email.index("@")]

#slice out domain name

domainname = email[email.index("@")+1:]

#format message

output="your username is {} and your domain name is {}".format(username,domainname)

#display output message

print(output)
