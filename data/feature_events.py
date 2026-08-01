import random
import pandas as pd

from config import *
from utils import *


#======================================================


FEATURE_EVENTS = {

    "Wishlist":[

        "Open Wishlist",
        "Add Product",
        "Remove Product",
        "Move To Cart"

    ],

    "Buy Again":[

        "View History",
        "Buy Again Click",
        "Add To Cart"

    ],

    "Flash Deals":[

        "View Deal",
        "Click Deal",
        "Add To Cart"

    ],

    "Smart Search":[

        "Search",
        "Apply Filters",
        "View Product"

    ],

    "Recommendations":[

        "View Recommendation",
        "Click Recommendation",
        "View Product"

    ],

    "Save for Later":[

        "Save Product",
        "Move To Cart",
        "Remove Product"

    ]

}


#======================================================


def generate_conversion_probability(


        feature_name

):

    probabilities = {


        "Wishlist":0.18,

        "Buy Again":0.45,

        "Flash Deals":0.28,

        "Smart Search":0.09,

        "Recommendations":0.30,

        "Save for Later":0.12


    }


    return probabilities[

        feature_name

    ]


#======================================================


def generate_feature_events(

        feature_adoptions_df,

        features_df,

        sessions_df,

        users_df

):


    feature_events_data = []


    #--------------------------------------------------


    feature_mapping = {

        row["feature_id"]:

        row["feature_name"]

        for _, row

        in features_df.iterrows()

    }


    #--------------------------------------------------


    user_country = {

        row["user_id"]:

        row["country"]

        for _, row

        in users_df.iterrows()

    }


    #--------------------------------------------------


    user_sessions = (


        sessions_df.groupby(

            "user_id"

        )["session_id"]

        .apply(list)

        .to_dict()


    )


    #--------------------------------------------------


    for _, row in (


            feature_adoptions_df.iterrows()


    ):


        user_id = row["user_id"]

        feature_id = row["feature_id"]


        feature_name = (

            feature_mapping[

                feature_id

            ]

        )


        #------------------------------------------


        if user_id not in user_sessions:

            continue


        session_id = random.choice(

            user_sessions[user_id]

        )


        #------------------------------------------


        country = (

            user_country[user_id]

        )


        event_names = (

            FEATURE_EVENTS[

                feature_name

            ]

        )


        conversion_probability = (

            generate_conversion_probability(

                feature_name

            )

        )


        #------------------------------------------


        is_converted = (

            random.random()

            <=

            conversion_probability

        )


        #------------------------------------------


        base_time = (

            row["adoption_date"]

        )


        #------------------------------------------


        for index, event_name in (

                enumerate(

                    event_names

                )

        ):


            event_id = (

                generate_uuid()

            )


            event_timestamp = (

                base_time +

                timedelta(

                    minutes=index*5

                )

            )


            feature_events_data.append(

                [

                    event_id,

                    user_id,

                    session_id,

                    feature_id,

                    event_name,

                    event_timestamp,

                    country,

                    is_converted

                ]

            )


    #=================================================


    columns = [

        "event_id",

        "user_id",

        "session_id",

        "feature_id",

        "event_name",

        "event_timestamp",

        "country",

        "is_converted"

    ]


    feature_events_df = pd.DataFrame(

        feature_events_data,

        columns=columns

    )


    export_csv(

        feature_events_df,

        "feature_events.csv"

    )


    print_success_message(

        "feature_events.csv"

    )


    return feature_events_df


#======================================================


if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )