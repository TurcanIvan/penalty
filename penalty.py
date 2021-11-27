# RULES
speed_limit   = 70      # int
penalty_amount = 50.00  # float

# CONTEXTUAL
speed_vehicle = 71

######################

if speed_vehicle > speed_limit:
 # TIKET 
    print("#####################################################")
    print("You've surpassed the ", speed_limit,"km/h spped limit")
    print("Your vehicle had", speed_vehicle,"km/h")
    print("Penalty to be payed ", penalty_amount,"USD" )
    print("#####################################################")
else:
    print("Something else")

print("EVATUATION FINISHED!")
# ------> speed_vehicle > speed_limit ? ----> True ----> print(... TIKET ) ---->
#                        \-----------------------------------------------/ 