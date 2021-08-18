from api import *

email = "..."
password = "..."

token = login(email, password)
myData = getMyData(token)
claimDailyBonus(token)

print(myData)