"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten, Pac-12 and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""
#bring in the json module
import json
#open the file
infile = open('school_data.json','r')
#load in the whole json file in dictionaries and lists
schools = json.load(infile)
#print(type(schools)) the type is a list

conference_schools = [372,130,107,108]

#Graduation rate of women above 75%
for key in schools:
    for i in conference_schools:
        if key["NCAA"]["NAIA conference number football (IC2020)"] == i:
            if key["Graduation rate  women (DRVGR2020)"] > 75:
                 print(f"University Name: {key['instnm']}")
                 print(f"graduation rate for women: {key['Graduation rate  women (DRVGR2020)']}%\n")
            
#Total price for in-state students living off campus over $50,000          
for key in schools:
    for i in conference_schools:
        if key["NCAA"]["NAIA conference number football (IC2020)"] == i:
            total_price = key.get("Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)")
            if total_price is not None and total_price > 50000:
                print(f"University Name: {key.get('instnm')}")
                print(f"Total price for in-state students living off campus: ${total_price}\n")
