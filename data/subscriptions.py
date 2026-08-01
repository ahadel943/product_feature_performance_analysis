import random
import pandas as pd

from datetime import timedelta

from config import *
from utils import *


#=====================================================


SUBSCRIPTION_TYPES = {

    "Monthly": 65,
    "Quarterly": 25,
    "Yearly": 10

}


#=====================================================


def generate_subscription_type():

    return weighted_choice(

        SUBSCRIPTION_TYPES

    )


#=====================================================


def generate_subscription_end_date(

        start_date,
        subscription_type

):

    if subscription_type == "Monthly":

        return start_date + timedelta(days=30)


    elif subscription_type == "Quarterly":

        return start_date + timedelta(days=90)


    return start_date + timedelta(days=365)


#=====================================================


def generate_is_active(

        end_date

):

    return end_date >= END_DATE


#=====================================================


def generate_subscriptions(

        users_df

):

    subscriptions_data = []


    premium_users = (

        users_df[
            users_df["is_premium"] == True
        ]

    )


    for _, row in premium_users.iterrows():


        subscription_id = (

            generate_uuid()

        )


        user_id = row["user_id"]


        start_date = (

            row["premium_start_date"]

        )


        subscription_type = (

            generate_subscription_type()

        )


        end_date = (

            generate_subscription_end_date(

                start_date,

                subscription_type

            )

        )


        is_active = (

            generate_is_active(

                end_date

            )

        )


        subscriptions_data.append(

            [

                subscription_id,
                user_id,
                subscription_type,
                start_date,
                end_date,
                is_active

            ]

        )


    #=================================================


    columns = [

        "subscription_id",
        "user_id",
        "subscription_type",
        "subscription_start_date",
        "subscription_end_date",
        "is_active"

    ]


    subscriptions_df = pd.DataFrame(

        subscriptions_data,

        columns=columns

    )


    export_csv(

        subscriptions_df,

        "subscriptions.csv"

    )


    print_success_message(

        "subscriptions.csv"

    )


    return subscriptions_df


#=====================================================


if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )