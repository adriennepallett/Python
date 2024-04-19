def calc_fine():

    speedLimit_zone_Adrienne = int(input("Speed Limit: "))
    speed_veh_Adrienne = int(input("Vehicle Speed: "))
    teen = str(input("t teen n or no:"))
    miles_over = speed_veh_Adrienne-speedLimit_zone_Adrienne


    
    if miles_over < 0:
        fine = "No Fine"
        stmt = "You werent speeding, Good Job!"
        
    elif miles_over > 0 and miles_over <= 5:
        fine = 39.50
        stmt = "You can do better as a driver!"

    elif miles_over > 5 and miles_over <= 15:
        fine = 89.00
        stmt = "Please reduce your speed!"

    elif miles_over > 15 and miles_over <= 25:
        fine = 109.50
        stmt = "Be careful, you are driving recklessly!"

    elif miles_over > 25 and miles_over <= 35:
        fine = 149.99
        stmt = "You are over-speeding!"

    else:
        if miles_over > 35:
            fine = 0.00
            stmt = "Court is mandatory. Your fine will be decided in court"
            
        
    if teen == "t" or teen == "teen":
        if miles_over < 0:
            pass
        else:
            fine = fine * 3
        

    print(fine)
    print(stmt)
    print()

    
calc_fine()




