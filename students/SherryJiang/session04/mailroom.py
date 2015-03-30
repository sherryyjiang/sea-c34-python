#Mail Assignment: pseudocode

donation_amount = {'Anna': 300, 'Michael':200, 'Kevin':200}
donation_times = {'Anna': 4, 'Michael':2, 'Kevin':1}

answer = raw_input("Choose 'Send a Thank You' or Create a Report' ")

if answer == "Send a Thank You":
    full_name == raw_input("Please input a Full Name")
    if full_name == "list":
        print donation_amount.keys()
        full_name == raw_input("Please input a Full Name") #not sure where to indent this
    if full_name not n donation_amount.keys():
        donation_amount[full_name] = ''
        amount = int(raw_input("Please enter in an amount"))
        donation_amount[full_name] = amount
        donation_times[full_name] = 1
    else:
        if full_name in donation_amount.keys():
            amount = int(raw_input("Please enter in an amount"))
            donation_amount[full_name] = donation_amount[full_name] + amount
            donatio_times[full_name] = donatio_times[full_name] + 1
    print donation_amount
    for k,v in donation_amount.items():
        str(k)
        str(v)
    print """"Dear %s, 
        Thank you very much for your kind donation of %s
        We hope to see you continue supporting our organization.
        """ % (full_name, amount)
   #return to the original prompt - some kind of while loop maybe? Ask during office hours

if answer == "Create a Report":
    sorted_donations = sorted(donation_amount.items())
    for i in sorted_donations:
        name_list = []
        name_list.append(i[0])
        print name_list
        total_donated = []
        total_donated.append(i[2])
        print total_donated
        for k,v in donation_times.items():

"""Need to create some sort of array that holds information in each row, with the name of the person as the primary key"""





