import json 

#Load JSON below
PNM_json_data = '''{"ResultCount":21,"Data":[{"First Name":"Moriah","Last Name":"Owens","State":"California","California Counties":"San Diego","Hometown":"Encinitas","Major":["Computer Science"],"Involvement":["New Student Orientation Program","Villanova Student Musical Theatre"],"Activities":["R\u0026amp;B Music","Photography","Study abroad"],"HappendAt":"\/Date(1711381153410)\/","InstanceId":null},{"First Name":"Maya","Last Name":"McFadden","State":"New Jersey","New Jersey Counties":"Monmouth","Hometown":"Aberdeen","Major":["Computer Science"],"Involvement":["Blue Key","New Student Orientation Program"],"Activities":["Fashion","Makeup","Traveling"],"HappendAt":"\/Date(1712521779662)\/","InstanceId":null},{"First Name":"Gina","Last Name":"Imperiale","State":"New Jersey","New Jersey Counties":"Monmouth","Hometown":"Belmar","Major":["Psychology"],"Involvement":["Dance Groups","NovaDance "],"Activities":["Yoga/Pilates","The beach","Rap music"],"HappendAt":"\/Date(1712522179326)\/","InstanceId":null},{"First Name":"Lee Ann","Last Name":"McDowell","State":"New York","New York Counties":"Albany","Hometown":"Buffalo","Major":["Biology"],"Involvement":["WXVU","Club Tennis","Rays of Sunshine"],"Activities":["Mindfulness","Rom coms","Concerts"],"HappendAt":"\/Date(1712521876557)\/","InstanceId":null},{"First Name":"Grace","Last Name":"Lepre","State":"New Jersey","New Jersey Counties":"Union","Hometown":"New Providence","Major":["Psychology"],"Involvement":["NovaDance ","Special Olympics "],"Activities":["Yoga/Pilates","Dancing","Weight lifting"],"HappendAt":"\/Date(1712521868303)\/","InstanceId":null},{"First Name":"Ami","Last Name":"Tha","State":"North Dakota","North Dakota Counties":"Barnes","Hometown":"OldTown","Major":["Biology","Classical Studies"],"Involvement":["Club Rugby","Mock Trial","Intramural Sports"],"Activities":["Swimming","Pop culture","Gardening"],"HappendAt":"\/Date(1712521916961)\/","InstanceId":null},{"First Name":"Sarah","Last Name":"Smith","State":"New Hampshire","New Hampshire Counties":"Hillsborough","Hometown":"Band","Major":["Cognitive and Behavioral Neuroscience"],"Involvement":["Special Olympics ","Club Field Hockey","Villanova TV"],"Activities":["Foodie","Coffee","Makeup"],"HappendAt":"\/Date(1712521967854)\/","InstanceId":null},{"First Name":"Filemina","Last Name":"Gerrard","State":"Colorado","Colorado Counties":"Eagle","Hometown":"Denver","Major":["Mechanical Engineering"],"Involvement":["NovaDance ","New Student Orientation Program","ROTC"],"Activities":["Baking","Rom coms","Cars"],"HappendAt":"\/Date(1712521826752)\/","InstanceId":null},{"First Name":"Ciara","Last Name":"Daly","State":"Florida","Florida Counties":"Broward","Hometown":"Tampa","Major":["Finance"],"Involvement":["Blue Key","New Student Orientation Program","Intramural Sports"],"Activities":["Makeup","Fashion","Crafting"],"HappendAt":"\/Date(1712521970574)\/","InstanceId":null},{"First Name":"Lilly","Last Name":"Lichtenberger","State":"Colorado","Colorado Counties":"Denver","Hometown":"Denver","Major":["Economics (CLAS)"],"Involvement":["Special Olympics ","ROTC"],"Activities":["Dancing","Concerts","Cars"],"HappendAt":"\/Date(1711381236019)\/","InstanceId":null},{"First Name":"Brooke","Last Name":"Clark","State":"California","California Counties":"Marin","Hometown":"Mount Talampais","Major":["Communication"],"Involvement":["NovaDance ","LEVEL"],"Activities":["Weight lifting","Astrology","Self-care"],"HappendAt":"\/Date(1711381182614)\/","InstanceId":null},{"First Name":"Ellie","Last Name":"Petroutsas","State":"New Jersey","New Jersey Counties":"Passaic","Hometown":"Clifton","Major":["Finance"],"Involvement":["New Student Orientation Program","A Capella"],"Activities":["R\u0026amp;B Music","Swimming","Mindfulness"],"HappendAt":"\/Date(1712521892968)\/","InstanceId":null},{"First Name":"Janylle","Last Name":"Banka","State":"Maine","Maine Counties":"Androscoggin","Hometown":"Lewiston","Major":["Political Science","Management"],"Involvement":["Club Rugby","ROTC"],"Activities":["Yoga/Pilates","Concerts","The beach"],"HappendAt":"\/Date(1712521790167)\/","InstanceId":null},{"First Name":"Abby","Last Name":"Fusco","State":"Massachusetts","Massachusetts Counties":"Plymouth","Hometown":"Marshfield","Major":["Accounting"],"Involvement":["WXVU","Club Softball"],"Activities":["Jazz Music","R\u0026amp;B Music","The beach"],"HappendAt":"\/Date(1711381210014)\/","InstanceId":null},{"First Name":"Shay","Last Name":"McDowell","State":"Pennsylvania","Pennsylvania Counties":"Allegheny","Hometown":"Pittsburgh","Major":["Computer Science"],"Involvement":["Blue Key","Special Olympics ","Intramural Sports"],"Activities":["Yoga/Pilates","Running","Study abroad"],"HappendAt":"\/Date(1712521449776)\/","InstanceId":null},{"First Name":"Shanna","Last Name":"Riches","State":"California","California Counties":"Riverside","Hometown":"Temecula","Major":["Real Estate"],"Involvement":["NovaDance ","RUIBAL","Villanova Student Theatre"],"Activities":["Cooking","Study abroad"],"HappendAt":"\/Date(1712521836026)\/","InstanceId":null},{"First Name":"Keaira ","Last Name":"Ecklof","State":"Massachusetts","Massachusetts Counties":"Hampshire","Hometown":"Amherst","Major":["English"],"Involvement":["Blue Key","A Capella"],"Activities":["The beach","Thrifting","Writing"],"HappendAt":"\/Date(1712521876025)\/","InstanceId":null},{"First Name":"Kirsten","Last Name":"Farhm","State":"New Hampshire","New Hampshire Counties":"Rockingham","Hometown":"Portsmouth","Major":["Real Estate","Cultural Studies"],"Involvement":["NovaDance ","Club Tae Kwon Do"],"Activities":["Dancing","Skiing","Study abroad"],"HappendAt":"\/Date(1712522051788)\/","InstanceId":null},{"First Name":"Grace","Last Name":"Estelle","State":"New York","New York Counties":"Suffolk","Hometown":"Babylon","Major":["Biology"],"Involvement":["Dance Groups","STEM organizations"],"Activities":["Hip Hop Music","Dancing","Makeup"],"HappendAt":"\/Date(1712521919266)\/","InstanceId":null},{"First Name":"Sarah","Last Name":"Krapels","State":"Pennsylvania","Pennsylvania Counties":"Delaware","Hometown":"Wayne","Major":["Marketing"],"Involvement":["LEVEL","Club Field Hockey"],"Activities":["Jazz Music","Dancing","Yoga/Pilates"],"HappendAt":"\/Date(1712522024978)\/","InstanceId":null},{"First Name":"Lauren","Last Name":"Klein","State":"Illinois","Illinois Counties":"Shelby","Hometown":"Chicago","Major":["Accounting"],"Involvement":["Intramural Sports","Club Running","Business organizations"],"Activities":["Running","Sports fan","Thrifting"],"HappendAt":"\/Date(1712521780576)\/","InstanceId":null}]}
'''
member_json_data = '''{"ResultCount":15,"Data":[{"First Name":"Rachel","Last Name":"Dzurina","State":"California","California Counties":"San Francisco","Hometown":"San Francisco","Major":["Marketing","Business Analytics"],"Involvement":["Dance Groups"],"Activities":["Makeup","Self-care","The beach"],"HappendAt":"\/Date(1712521901725)\/","InstanceId":null},{"First Name":"Sarah","Last Name":"Krusen","State":"New Jersey","New Jersey Counties":"Burlington","Hometown":"Jobstown","Major":["Nursing"],"Involvement":["Special Olympics ","NovaDance "],"Activities":["Weight lifting","Rap music","Makeup"],"HappendAt":"\/Date(1712521918500)\/","InstanceId":null},{"First Name":"Kelly","Last Name":"Obermann","State":"Tennessee","Tennessee Counties":"Knox","Hometown":"Knoxville","Major":["Environmental Science","Economics (CLAS)"],"Involvement":["WXVU","STEM organizations","The Villanovan"],"Activities":["Cooking","Baking","Traveling"],"HappendAt":"\/Date(1712521788193)\/","InstanceId":null},{"First Name":"Francesca","Last Name":"Raimondi","State":"New York","New York Counties":"Nassau","Hometown":"Manhasset","Major":["Italian","Psychology"],"Involvement":["Club Swim"],"Activities":["Dancing","Foodie","Pop culture"],"HappendAt":"\/Date(1712522033360)\/","InstanceId":null},{"First Name":"Lisa","Last Name":"Louelle","State":"Delaware","Delaware Counties":"New Castle","Hometown":"New Castle","Major":["Mechanical Engineering"],"Involvement":["The Villanovan","WXVU"],"Activities":["Yoga/Pilates","Comedy movies","Self-care"],"HappendAt":"\/Date(1712521992608)\/","InstanceId":null},{"First Name":"Helen","Last Name":"Badger","State":"New Hampshire","New Hampshire Counties":"Cheshire","Hometown":"Keene","Major":["Theology and Religious Studies"],"Involvement":["Villanova Student Theatre"],"Activities":["Yoga/Pilates","Pop culture","Photography"],"HappendAt":"\/Date(1712522096285)\/","InstanceId":null},{"First Name":"Andy","Last Name":"Alvarez","State":"Hawaii","Hawaii Counties":"Honolulu","Hometown":"Waikkiki","Major":["Cognitive and Behavioral Neuroscience"],"Involvement":["NovaDance ","Special Olympics "],"Activities":["Skiing","The beach","Card games"],"HappendAt":"\/Date(1712424069571)\/","InstanceId":null},{"First Name":"Delayney","Last Name":"Harrison","State":"New Jersey","New Jersey Counties":"Monmouth","Hometown":"Belmar","Major":["Psychology"],"Involvement":["Dance Groups","NovaDance "],"Activities":["Yoga/Pilates","The beach","Rap music"],"HappendAt":"\/Date(1712522181733)\/","InstanceId":null},{"First Name":"Isabella","Last Name":"Scorzelli","State":"New Hampshire","New Hampshire Counties":"Hillsborough","Hometown":"Hillsborough","Major":["Cognitive and Behavioral Neuroscience"],"Involvement":["Blue Key","Philly Justice"],"Activities":["Jazz Music","Playing an instrument","Photography"],"HappendAt":"\/Date(1712522010220)\/","InstanceId":null},{"First Name":"Madison ","Last Name":"Stell","State":"Virginia","Virginia Counties":"Arlington","Hometown":"Arlington","Major":["Economics (CLAS)"],"Involvement":["NovaDance ","Special Olympics "],"Activities":["Concerts","Sports fan","Surfing"],"HappendAt":"\/Date(1712522097637)\/","InstanceId":null},{"First Name":"Ella","Last Name":"Kilgore","State":"Massachusetts","Massachusetts Counties":"Norfolk","Hometown":"Wellesley","Major":["Criminology","Honors"],"Involvement":["A Capella","Blue Key"],"Activities":["Baking","Dancing","Skiing"],"HappendAt":"\/Date(1712521942420)\/","InstanceId":null},{"First Name":"Shyla","Last Name":"Werneke","State":"New Jersey","New Jersey Counties":"Monmouth","Hometown":"Aberdeen","Major":["Accounting"],"Involvement":["A Capella","Business organizations"],"Activities":["R\u0026amp;B Music","Foodie","The beach"],"HappendAt":"\/Date(1712521840286)\/","InstanceId":null},{"First Name":"Sarah","Last Name":"Abeywardena","State":"Delaware","Delaware Counties":"Sussex","Hometown":"Wilmington","Major":["Computer Science"],"Involvement":["Dance Groups","STEM organizations"],"Activities":["Cooking","Dancing","Weight lifting"],"HappendAt":"\/Date(1712521963425)\/","InstanceId":null},{"First Name":"Madeleine ","Last Name":"Brooks","State":"Rhode Island","Rhode Island Counties":"Kent County","Hometown":"East Greenwich","Major":["English","Spanish Studies"],"Involvement":["A Capella","Villanova Student Musical Theatre"],"Activities":["Baking","Jazz Music","Yoga/Pilates"],"HappendAt":"\/Date(1712521966759)\/","InstanceId":null},{"First Name":"Alexa","Last Name":"Wood","State":"Colorado","Colorado Counties":"Boulder","Hometown":"Boulder","Major":["Real Estate","Civil Engineering"],"Involvement":["Special Olympics ","Club Rugby","Rays of Sunshine"],"Activities":["Weight lifting","Jazz Music","Baking"],"HappendAt":"\/Date(1712522069980)\/","InstanceId":null}]}'''

state_third_element = { #this dictionary maps each State name to the county selected
    "Alabama": "Alabama Counties",
    "Alaska": "Alaska Counties",
    "Arizona": "Arizona Counties",
    "Arkansas": "Arkansas Counties",
    "California": "California Counties",
    "Colorado": "Colorado Counties",
    "Connecticut": "Connecticut Counties",
    "Delaware": "Delaware Counties",
    "Florida": "Florida Counties",
    "Georgia": "Georgia Counties",
    "Hawaii": "Hawaii Counties",
    "Idaho": "Idaho Counties",
    "Illinois": "Illinois Counties",
    "Indiana": "Indiana Counties",
    "Iowa": "Iowa Counties",
    "Kansas": "Kansas Counties",
    "Kentucky": "Kentucky Counties",
    "Louisiana": "Louisiana Counties",
    "Maine": "Maine Counties",
    "Maryland": "Maryland Counties",
    "Massachusetts": "Massachusetts Counties",
    "Michigan": "Michigan Counties",
    "Minnesota": "Minnesota Counties",
    "Mississippi": "Mississippi Counties",
    "Missouri": "Missouri Counties",
    "Montana": "Montana Counties",
    "Nebraska": "Nebraska Counties",
    "Nevada": "Nevada Counties",
    "New Hampshire": "New Hampshire Counties",
    "New Jersey": "New Jersey Counties",
    "New Mexico": "New Mexico Counties",
    "New York": "New York Counties",
    "North Carolina": "North Carolina Counties",
    "North Dakota": "North Dakota Counties",
    "Ohio": "Ohio Counties",
    "Oklahoma": "Oklahoma Counties",
    "Oregon": "Oregon Counties",
    "Pennsylvania": "Pennsylvania counties",
    "Rhode Island": "Rhode Island Counties",
    "South Carolina": "South Carolina Counties",
    "South Dakota": "South Dakota Counties",
    "Tennessee": "Tennessee Counties",
    "Texas": "Texas Counties",
    "Utah": "Utah Counties",
    "Vermont": "Vermont Counties",
    "Virginia": "Virginia Counties",
    "Washington": "Washington Counties",
    "West Virginia": "West Virginia Counties",
    "Wisconsin": "Wisconsin Counties",
    "Wyoming": "Wyoming Counties"
}

def parse(json_data):
    data = json.loads(json_data)    

    # Extract required fields and format into a list of lists
    formatted_data = []
    for entry in data['Data']: #Iterates thru each "response"
        fname = entry['First Name']
        lname = entry['Last Name']
        hometown_state = entry['State']
        third_element_key = state_third_element.get(hometown_state, '') #run dictionary
        third_element = entry.get(third_element_key, '') # set county value to "find"
        city = entry['Hometown']
        major = entry.get('Major', [])
        campus_involvement = entry.get('Involvement', [])
        activities = entry.get('Activities', [])
    
        #creates list of dictionaries for each pnm then sorts alphabetically
        formatted_entry = {"first name": fname, "last name": lname, "state": hometown_state, "county": third_element, "hometown": city, "major": major, "involvement": campus_involvement, "activities": activities}
        formatted_data.append(formatted_entry)

    return formatted_data

# Sorts pnms alphabetically by last name
sorted_list_of_PNMs = sorted(parse(PNM_json_data), key=lambda x: x['last name'])
counter = 1
for entry in sorted_list_of_PNMs:
    entry["PNM number"] = counter
    counter += 1

list_of_members = parse(member_json_data)

memberCounter = 1
for member in list_of_members:
    member['Bump Group number'] = memberCounter
    memberCounter += 1
    if memberCounter == 6:
        memberCounter = 1

