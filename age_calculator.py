# Age calculator needs:
# 1. today's date
# 2. date of birth 

def ageCalculator(y,m,d):
    import datetime
    today = datetime.datetime.now().date()
    date_of_birth = datetime.date(y,m,d)
    age = int((today-date_of_birth).days/365)
    print(age)

ageCalculator(2000,12,8)