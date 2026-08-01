import random
import pandas as pd


from config import *
from utils import *



#=====================================================
# Basket Size Distribution
#=====================================================

BASKET_SIZE = {

    1:45,
    2:30,
    3:15,
    4:10

}



#=====================================================
# Quantity Generator
#=====================================================

def generate_quantity():

    probability = random.random()


    if probability < 0.75:

        return 1


    elif probability < 0.95:

        return 2


    return random.randint(3,5)



#=====================================================
# Generate Order Items
#=====================================================

def generate_order_items(

        orders_df,

        products_df

):


    order_items_data = []


    #-----------------------------------------------

    products_list = (

        products_df[

            [

                "product_id",

                "price"

            ]

        ]

        .values

        .tolist()

    )


    #-----------------------------------------------


    for _, order in orders_df.iterrows():


        order_id = order["order_id"]


        basket_size = weighted_choice(

            BASKET_SIZE

        )


        selected_products = random.sample(

            products_list,

            basket_size

        )


        total_calculated = 0



        for product_id, price in selected_products:


            quantity = generate_quantity()


            unit_price = price


            item_total = round(

                unit_price * quantity,

                2

            )


            total_calculated += item_total



            order_item_id = generate_uuid()



            order_items_data.append(

                [

                    order_item_id,

                    order_id,

                    product_id,

                    quantity,

                    unit_price,

                    item_total

                ]

            )



        #-------------------------------------------

        # Adjust last item to match order amount

        order_amount = order["total_amount"]


        difference = round(

            order_amount - total_calculated,

            2

        )


        if difference != 0:


            last_item = order_items_data[-1]


            last_item[5] += difference



    #=================================================


    columns = [

        "order_item_id",

        "order_id",

        "product_id",

        "quantity",

        "unit_price",

        "item_total"

    ]



    order_items_df = pd.DataFrame(

        order_items_data,

        columns=columns

    )



    export_csv(

        order_items_df,

        "order_items.csv"

    )


    print_success_message(

        "order_items.csv"

    )


    return order_items_df




#=====================================================

if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )