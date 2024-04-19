#FootwearMain.py

import AdrienneFootwear

def main():
    dTotalPrice = 0.0         
    iTotalWeight = 0
    # Put the 4 footwears being ordered in footwear1 through footwear 4         
    footwear1 = AdrienneFootwear.Footwear( "Nike", 10, "Mens wear Yellow", 11, 59.99)         
    footwear2 = AdrienneFootwear.Footwear( "Addidas", 7, "Womens wear Black", 8, 39.99)         
    footwear3 = AdrienneFootwear.Footwear( "New Balance", 11, "Boys Basketball White", 10, 79.59)         
    footwear4 = AdrienneFootwear.Footwear( "Vans", 10, "Girls Floral", 7, 21.39)
    footwear5 = AdrienneFootwear.Footwear( "Kirkland", 5, "Child wear Brown", 4, 19.99)
    
    footwear2.set_quantity(3)      
    footwear5.set_quantity(2)
                                   
    # Show the details of the order using:         
    print("Here are your shopping cart contents.")         
    print(footwear1)         
    print(footwear2)        
    print(footwear3)         
    print(footwear4)
    print(footwear5)
                                   
    # Compute the total cost and total weight in this section        
    dTotalPrice += footwear1.get_order_price()         
    dTotalPrice += footwear2. get_order_price()         
    dTotalPrice += footwear3. get_order_price()         
    dTotalPrice += footwear4. get_order_price()
    dTotalPrice += footwear5.get_order_price()
    
    iTotalWeight += footwear1.get_order_weight_in_ounces()        
    iTotalWeight += footwear2. get_order_weight_in_ounces ()         
    iTotalWeight += footwear3. get_order_weight_in_ounces ()         
    iTotalWeight += footwear4. get_order_weight_in_ounces ()
    iTotalWeight += footwear5. get_order_weight_in_ounces ()
    print()
    
    # Here we show the order details        
    print(f"The Price of your order is ${dTotalPrice:0.2f}")        
    print(f"The shipping weight is {iTotalWeight // 16} pounds {iTotalWeight % 16} ounces")
   
if __name__ == "__main__":
    main()
