#AdrienneOrderReceiptList.py

import AdrienneFootwear

def main():
    dTotalPrice = 0.00
    iTotalWeight = 0
    
    footwear1 = AdrienneFootwear.Footwear( "Nike", 10, "Mens wear Yellow", 11, 59.99)         
    footwear2 = AdrienneFootwear.Footwear( "Addidas", 7, "Womens wear Black", 8, 39.99)         
    footwear3 = AdrienneFootwear.Footwear( "New Balance", 11, "Boys Basketball White", 10, 79.59)         
    footwear4 = AdrienneFootwear.Footwear( "Vans", 10, "Girls Floral", 7, 21.39)
    footwear5 = AdrienneFootwear.Footwear( "Kirkland", 5, "Child wear Brown", 4, 19.99)
    
    footwear2.set_quantity(3)      
    footwear5.set_quantity(2)
    
    print("Here are your shopping cart contents.")         
        
    footwearList = []
    
    footwearList.append(footwear1)
    footwearList.append(footwear2)
    footwearList.append(footwear3)
    footwearList.append(footwear4)
    footwearList.append(footwear5)
    
    for i in footwearList:
        print(i)
        dTotalPrice += i.get_order_price()
        iTotalWeight += i.get_order_weight_in_ounces()

    print(f"\nThe Price of your order is ${dTotalPrice:0.2f}")        
    print(f"The shipping weight is {iTotalWeight // 16} pounds {iTotalWeight % 16} ounces")
    
    
if __name__ == "__main__":
    main()
