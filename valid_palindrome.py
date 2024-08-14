string="Was it a car or a at I saw?"
res=""
for s in string:
    if s.isalnum():
        res+=s.lower()
print(res==res[::-1])