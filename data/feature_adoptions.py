import random
import pandas as pd

from datetime import datetime

from config import *
from utils import *


#=====================================================

def calculate_adoption_probability(

        feature_name,

        is_premium,

        customer_type

):

    probability = (

        FEATURE_ADOPTION_RATES[

            feature_name

        ]

    )


    #---------------------------------

    if is_premium:

        probability *= (

            PREMIUM_MULTIPLIER[

                feature_name

            ]

        )


    #---------------------------------

    if customer_type == "Returning":

        probability *= 1.30


    #---------------------------------

    probability = min(

        probability,

        95

    )


    return probability /100


#=====================================================

def generate_adoption_date(

        signup_date,

        launch_date

):


    start_date = max(

        signup_date,

        datetime.strptime(

            launch_date,

            "%Y-%m-%d"

        )

    )


    return random_datetime(

        start_date,

        END_DATE

    )


#=====================================================

def generate_feature_adoptions(

        users_df,

        features_df

):


    adoptions_data = []


    for _, user in users_df.iterrows():


        user_id = user["user_id"]

        signup_date = user["signup_date"]

        is_premium = user["is_premium"]

        customer_type = (

            user["customer_type"]

        )


        #--------------------------------


        for _, feature in (

                features_df.iterrows()

        ):


            feature_id = (

                feature["feature_id"]

            )

            feature_name = (

                feature["feature_name"]

            )

            launch_date = (

                feature["launch_date"]

            )


            #----------------------------


            probability = (

                calculate_adoption_probability(

                    feature_name,

                    is_premium,

                    customer_type

                )

            )


            is_adopted = (

                random.random()

                <= probability

            )


            #----------------------------


            if not is_adopted:

                continue


            adoption_date = (

                generate_adoption_date(

                    signup_date,

                    launch_date

                )

            )


            days_since_launch = (

                adoption_date -

                datetime.strptime(

                    launch_date,

                    "%Y-%m-%d"

                )

            ).days


            #----------------------------


            adoption_id = (

                generate_uuid()

            )


            adoptions_data.append(

                [

                    adoption_id,

                    user_id,

                    feature_id,

                    adoption_date,

                    days_since_launch,

                    True

                ]

            )


    #=================================================


    columns = [

        "adoption_id",

        "user_id",

        "feature_id",

        "adoption_date",

        "days_since_launch",

        "is_adopted"

    ]


    adoptions_df = pd.DataFrame(

        adoptions_data,

        columns=columns

    )


    export_csv(

        adoptions_df,

        "feature_adoptions.csv"

    )


    print_success_message(

        "feature_adoptions.csv"

    )


    return adoptions_df


#=====================================================

if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )