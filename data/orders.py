import random
import pandas as pd

from config import *
from utils import *


#=====================================================
# Payment Methods
#=====================================================

PAYMENT_METHODS = {

    "Credit Card":35,
    "Cash":30,
    "Wallet":20,
    "BNPL":10,
    "Bank Transfer":5

}


#=====================================================
# Order Status
#=====================================================

ORDER_STATUS = {

    "Completed":92,
    "Cancelled":5,
    "Returned":3

}


#=====================================================
# Conversion probability
#=====================================================

def calculate_order_probability(

        session_row

):

    probability = 0.06


    # Longer sessions convert better

    if session_row["session_duration_minutes"] > 20:

        probability *= 1.5


    # More pages viewed

    if session_row["pages_viewed"] > 10:

        probability *= 1.3


    probability = min(

        probability,

        0.5

    )


    return probability



#=====================================================
# Generate Order Amount
#=====================================================

def generate_total_amount():

    return round(

        np.random.lognormal(

            mean=5.8,

            sigma=0.8

        ),

        2

    )



#=====================================================
# Generate Orders
#=====================================================

def generate_orders(

        sessions_df

):


    orders_data = []


    # Shuffle sessions

    sessions_sample = sessions_df.sample(

        frac=1,

        random_state=42

    )


    for _, session in sessions_sample.iterrows():


        probability = calculate_order_probability(

            session

        )


        if random.random() > probability:

            continue



        order_id = generate_uuid()


        user_id = session["user_id"]

        session_id = session["session_id"]


        session_start = session["session_start"]


        # order happens after session

        order_date = random_datetime(

            session_start,

            END_DATE

        )


        payment_method = weighted_choice(

            PAYMENT_METHODS

        )


        order_status = weighted_choice(

            ORDER_STATUS

        )


        total_amount = generate_total_amount()



        orders_data.append(

            [

                order_id,

                user_id,

                session_id,

                order_date,

                payment_method,

                order_status,

                total_amount

            ]

        )


        if len(orders_data) >= ROWS_COUNT["orders"]:

            break



    #=================================================

    columns = [

        "order_id",

        "user_id",

        "session_id",

        "order_date",

        "payment_method",

        "order_status",

        "total_amount"

    ]


    orders_df = pd.DataFrame(

        orders_data,

        columns=columns

    )


    export_csv(

        orders_df,

        "orders.csv"

    )


    print_success_message(

        "orders.csv"

    )


    return orders_df



#=====================================================

if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )