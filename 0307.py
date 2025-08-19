armstrong=lambda a:a==sum(int(i)**len(str(a)) for i in str(a))
print(armstrong(153))




