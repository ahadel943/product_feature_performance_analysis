import random
import pandas as pd

from config import *
from utils import *


#=====================================================


USER_SEGMENTS = {

    "Power User":5,
    "Heavy User":20,
    "Normal User":50,
    "Inactive User":25

}


#=====================================================


def generate_pages_viewed():

    return random.randint(1,30)


#=====================================================


def generate_is_converted():

    # Not every session converts

    return random.random() <= 0.07


#=====================================================


def generate_sessions_per_user():

    segment = weighted_choice(
        USER_SEGMENTS
    )


    if segment == "Power User":

        return random.randint(50,80)


    elif segment == "Heavy User":

        return random.randint(25,50)


    elif segment == "Normal User":

        return random.randint(8,24)


    return random.randint(1,7)


#=====================================================


def generate_session_start(

        signup_date

):

    return random_datetime(

        signup_date,

        END_DATE

    )


#=====================================================


def generate_sessions(

        users_df

):


    sessions_data = []


    for _, row in users_df.iterrows():


        user_id = row["user_id"]

        signup_date = row["signup_date"]

        country = row["country"]

        device_type = row["device_type"]


        sessions_count = (

            generate_sessions_per_user()

        )


        for _ in range(

                sessions_count

        ):


            #------------------------------------


            session_id = (

                generate_uuid()

            )


            session_start = (

                generate_session_start(

                    signup_date

                )

            )


            session_end = (

                generate_session_end(

                    session_start

                )

            )


            session_duration = (

                int(

                    (session_end - session_start)

                    .total_seconds()/60

                )

            )


            pages_viewed = (

                generate_pages_viewed()

            )


            is_converted = (

                generate_is_converted()

            )


            #------------------------------------


            sessions_data.append(

                [

                    session_id,
                    user_id,
                    session_start,
                    session_end,
                    device_type,
                    session_duration,
                    pages_viewed,
                    is_converted,
                    country

                ]

            )


    #=================================================


    columns = [

        "session_id",
        "user_id",
        "session_start",
        "session_end",
        "device_type",
        "session_duration_minutes",
        "pages_viewed",
        "is_converted",
        "country"

    ]


    sessions_df = pd.DataFrame(

        sessions_data,

        columns=columns

    )


    export_csv(

        sessions_df,

        "sessions.csv"

    )


    print_success_message(

        "sessions.csv"

    )


    return sessions_df


#=====================================================


if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )