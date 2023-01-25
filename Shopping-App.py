# define product list with key
items={
    "A": "Apple",
    "O": "Orange",
    "P": "Pepsi",
    "W": "Water",
    "C": "Cucumber",
    "T": "Tomato"
    }
# define products price list with key
items_prices={
    "A":{"price":1.25},
    "O":{"price":1.300},
    "P":{"price":0.100},
    "W":{"price":0.05},
    "C":{"price":0.150},
    "T":{"price":0.5}
    }
# define products' categories list with key
items_categories= {
    "1":{"(O)range","(A)pple"},
    "2":{"(P)epsi","(W)ater"},
    "3":{"(C)ucumber","(T)omato"},
    }
# define cart to store selected product and quantity 
carts = {}
total_order = 0

def show_bill():
    print("="*50)
    print("Item  "," "*8,"Price"," "*9,"Total")
    print("="*50)
    # iterate throw carts
    for item in carts.keys():
        # get item key by its value
        item_key = [k for k, v in items.items() if v == item][0]
        # get item qty from cart
        item_qty = carts[item]
        # get item price by item key
        item_price = items_prices[item_key]["price"]
        print(str.format("{0}          {1} x {2}        {3:.3f}",item,item_qty,item_price,item_qty*item_price))
    # print line with repeated chars
    print("*"*50)
    print("="*50)
def edit_cart():
        # list of carts items
        items_list =[]
        for item in carts:
            # get item key
            item_key = [k for k, v in items.items() if v == item][0]
            # get current item qty
            item_qty = carts[item]
            # ask the user choose which item to edit
            items_list.append(str.format("({0}){1} x {2} ",item_key,item[1:],item_qty))
        
        items_list.insert(0,"Choose an item: ")
        # store selected item to edit
        selected_item = input(items_list)
        if str(selected_item).upper() not in items.keys(): return
        # get product item.
        product_item = items[selected_item.upper()]
        # ask for new qty, if the new qty is 0 so remove it from the cart.
        new_qty = input(str("Enter new qty or 0 to remove: "))
        if new_qty == "0" :
            # remove from the cart.
            del carts[product_item]
            print(product_item + " item removed")
        else:
            # update qty.
            carts.update({product_item:int(new_qty)})
            print(product_item + " item updated")

command = ""
while command.lower() not in ["q", "c"]:
    if command.lower() == "e":
        edit_cart()
        command = input("(E)dit Cart, (C)heck Out, (A)dd more items, (Q)uit: ")
        continue

    # ask the customer which category he want 
    chosen_category  = input("Choose a Category (1)Fruites, (2)Beverages, (3)Vegetables: ")
    
    # make sure the chosen category key exists
    if chosen_category not in items_categories.keys(): continue
    print("Choose:", end =" ")
    # store selected item key from a input
    selected_item = input(str(items_categories[chosen_category]) + ": " )
    # validate the selected keynot empty and exists in items list key
    if selected_item != "" and str(selected_item).upper() in items.keys():
        # ask how many items he needs.
        qty = input("Enter the Quantity (default 1): ")
        # validate the qty, if no choice, let qty=1 as default
        if qty == "0" or qty =='': qty=1
        qty = int(qty)

        # get the product item price from list by item key
        price = items_prices[selected_item.upper()]["price"]

        # calulate the amount.
        amount = float(price) * qty
        
        # get the product name from the items list using the item key.
        product_name = items[selected_item.upper()]
        # print a line display the current product,qty, and total amount.
        print(str.format("{0}       {1} x {2}       {3:.3f}",product_name ,qty ,price ,amount))

        # check if the item existing in cart.
        # if so, update the qty.
        if product_name in carts:
            # cumulative  the qty.
            product_qty = carts[product_name] + qty
            carts.update({product_name:product_qty})
        else:
            # otherwise add it.
            carts.update({product_name:qty})

        # cumulative  the total order amount.
        total_order += amount 
        # get total carts items. 
        total_items= sum(carts.values())

    if len(carts)> 0:
        command  = input("(E)dit Cart, (C)heck Out, (A)dd more items, (Q)uit: ")
    
    # Edit carts to remove or update item
    if command.lower() == "e":
        edit_cart()
        command  = input("(E)dit Cart, (C)heck Out, (A)dd more items, (Q)uit: ")
        


   # to add more product, press any key, otherwise Q to end
    # msg = "Press any key to continue, or Q to Checkout: "
    # if len(carts)> 0:
    #     msg = "Press Enter to add more item, or Q to Checkout: "
    
    # command = input(msg)

# if command.lower() == "e":
#     print(carts.keys())
#     product_item = input("Choose the item:")

if command.lower() in ["q","c"]:
    if len(carts) > 0:  
        # print a bill report and grand amount
        space = " "* 10
        show_bill()
        print(str.format("Total Items: {0} {2} Total Amount: {1:.3f} KD",total_items,total_order,space))
        print("*"*50)
