import random
import pandas as pd

from config import *
from utils import *


#=====================================================

CATEGORY_WEIGHTS = {

    "Electronics":28,
    "Fashion":24,
    "Home":18,
    "Beauty":12,
    "Sports":10,
    "Books":8

}


#=====================================================

def generate_category():

    return weighted_choice(
        CATEGORY_WEIGHTS
    )


#=====================================================

def generate_subcategory(

        category

):

    return random.choice(

        PRODUCT_CATEGORIES[category]

    )


#=====================================================

def generate_launch_date():

    return random_datetime(

        START_DATE,

        END_DATE

    )


#=====================================================

def generate_is_active():

    # 95% Active Products

    return random.random() <= 0.95


#=====================================================

def generate_products():

    products_data = []


    for _ in range(

            ROWS_COUNT["products"]

    ):


        #----------------------------------

        product_id = generate_uuid()


        #----------------------------------

        category = (

            generate_category()

        )


        subcategory = (

            generate_subcategory(
                category
            )

        )


        #----------------------------------

        price = (

            generate_product_price()

        )


        #----------------------------------

        launch_date = (

            generate_launch_date()

        )


        #----------------------------------

        is_active = (

            generate_is_active()

        )


        #----------------------------------


        products_data.append(

            [

                product_id,
                category,
                subcategory,
                price,
                launch_date,
                is_active

            ]

        )


    #=================================================


    columns = [

        "product_id",
        "category",
        "subcategory",
        "price",
        "launch_date",
        "is_active"

    ]


    products_df = pd.DataFrame(

        products_data,

        columns=columns

    )


    export_csv(

        products_df,

        "products.csv"

    )


    print_success_message(

        "products.csv"

    )


    return products_df


#=====================================================


if __name__ == "__main__":

    generate_products()
