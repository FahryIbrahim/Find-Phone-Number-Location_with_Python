import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Masukkan Nomor HP : ")
mobileNo = phonenumbers.parse(mobileNo)

#Mendapatkan Lokasi
print(timezone.time_zones_for_number(mobileNo))

#Mendapatkan Provider
print(carrier.name_for_number(mobileNo, "id"))

#Mendapatkan Negara
print(geocoder.description_for_number(mobileNo, "id"))

#Validasi sebuah nomor hp
print("Valid Mobile Number : ", phonenumbers.is_valid_number(mobileNo))

#Cek posibilitas sebuah nomor
print("Mengecek posibilitas sebuah nomor : ",phonenumbers.is_possible_number(mobileNo))