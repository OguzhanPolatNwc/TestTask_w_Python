import pandas as pd
from datetime import datetime, timedelta
import time
import numpy as np

List = []
Previous_Id_List = []
while True:
    input_name = input("What is your name? ")
    Previous_Id_List.append(input_name)
    day_of_stay = int(input("How many day you will stay"))
    a = []
    creat_id = f"Res-{len(List) + 1} ID"
    checkin = datetime.now()
    checkout = checkin + timedelta(days=day_of_stay)
    a.append(input_name)
    a.append(creat_id)
    a.append(checkin)
    a.append(checkout)
    if len(List) == 0:
        a.append("-")
    else:
        for i in List:
            # print(i)
            if i[0] == input_name:
                # print(i[0])
                previous_id = f"Res-{len(List)} ID"
                a.append(previous_id)
            else:
                a.append("-")
    List.append(a)
    print("Hello " + input_name)

    Register_No = int(input("For another register choose 1 \n For exit choose 0"))
    if Register_No == 1:
        continue
    elif Register_No == 0:
        break

name_list = []
id_list = []
checkin_list = []
checkout_list = []
previous_id_list = []

for i in List:
    name_list.append(i[0])
    id_list.append(i[1])
    checkin_list.append(i[2])
    checkout_list.append(i[3])
    previous_id_list.append(i[-1])

df = pd.DataFrame({"Name": name_list, "ID": id_list, "Checkin": checkin_list, "Checkout": checkout_list,
                   "Previous ID": previous_id_list})
print(df)

while True:

    input_search = input("Search by name or ID : ")
    if df["Name"].str.contains(input_search).any():
        print(df[df["Name"] == input_search][["ID", "Checkin", "Checkout"]])
    else:
        print("Not Found")

    search_again = input("Search again? Choose 1, to exit Choose 0 ")
    if search_again == "1":
        continue
    elif search_again == "0":
        break
