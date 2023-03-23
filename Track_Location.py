import phonenumbers
from phonenumbers import geocoder
phn1=phonenumbers.parse("+917294536271")
phn2=phonenumbers.parse("+918878586271")
phn3=phonenumbers.parse("+12136574429")
phn4=phonenumbers.parse("+201234567890")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phn1,"en"))
print(geocoder.description_for_number(phn2,"en"))
print(geocoder.description_for_number(phn3,"en"))
print(geocoder.description_for_number(phn4,"en"))
