friends = [
    {"name":"david","location":"lebanon","church":"world life"},
     {"name":"samson","location":"sebrepon","church":"christ life"},
      {"name":"percy","location":"jericho","church":"jw"},
       {"name":"junior","location":"zenu","church":"apostolic"},
        {"name":"bill","location":"teshie","church":"penticos"},
         {"name":"eli","location":"lebanon","church":"AG"}

]

for name in friends:
    print(name["name"],name["location"],sep=" , ")