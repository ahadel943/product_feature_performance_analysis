import random
import pandas as pd

from datetime import timedelta

from config import *
from utils import *


#=====================================================


def generate_users():

    users_data = []


    for _ in range(ROWS_COUNT["users"]):


        #-----------------------------

        user_id = generate_uuid()

        signup_date = generate_signup_date()


        #-----------------------------

        country = generate_country()

        city = generate_city(country)


        #-----------------------------

        age_group = generate_age_group()

        customer_type = generate_customer_type()


        #-----------------------------

        acquisition_channel = (

            generate_acquisition_channel()

        )

        device_type = generate_device()


        #-----------------------------


        is_premium = generate_is_premium()


        if is_premium:

            premium_start_date = (

                generate_premium_date(
                    signup_date
                )

            )

        else:

            premium_start_date = None


        #-----------------------------


        users_data.append(

            [

                user_id,
                signup_date,
                country,
                city,
                age_group,
                customer_type,
                is_premium,
                premium_start_date,
                acquisition_channel,
                device_type

            ]

        )


    #=================================================


    columns = [

        "user_id",
        "signup_date",
        "country",
        "city",
        "age_group",
        "customer_type",
        "is_premium",
        "premium_start_date",
        "acquisition_channel",
        "device_type"

    ]


    users_df = pd.DataFrame(

        users_data,
        columns=columns

    )


    export_csv(

        users_df,

        "users.csv"

    )


    print_success_message(

        "users.csv"

    )


    return users_df


#=====================================================


if __name__ == "__main__":

    generate_users()