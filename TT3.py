import datetime
TheDate=input("Enter the date")
date_converter=datetime.datetime(TheDate)
print(date_converter.strftime('%A %B %Y'))
