import random
import pandas as pd

from config import *
from utils import *


#=====================================================


def generate_features_used_count():

    return random.randint(0, 5)


#=====================================================


def generate_orders_count():

    probability = random.random()

    if probability <= 0.90:
        return 0

    elif probability <= 0.98:
        return 1

    return random.randint(2, 4)


#=====================================================


def generate_total_minutes(

        sessions_count

):

    if sessions_count == 0:

        return 0

    total_minutes = 0

    for _ in range(sessions_count):

        total_minutes += (

            generate_session_duration()

        )

    return total_minutes


#=====================================================


def generate_is_active(

        sessions_count,
        features_count,
        orders_count

):

    return (

        sessions_count > 0

        or

        features_count > 0

        or

        orders_count > 0

    )


#=====================================================


def generate_user_daily_activity(

        users_df

):

    activity_data = []


    for _, row in users_df.iterrows():


        user_id = row["user_id"]

        signup_date = row["signup_date"]


        #-------------------------------------

        current_date = signup_date.date()


        while current_date <= END_DATE.date():


            #---------------------------------

            is_active_today = (

                random.random() <= 0.20

            )


            if is_active_today:

                sessions_count = (

                    random.randint(1,4)

                )

            else:

                sessions_count = 0


            #---------------------------------


            total_minutes = (

                generate_total_minutes(

                    sessions_count

                )

            )


            #---------------------------------


            features_used_count = (

                generate_features_used_count()

                if sessions_count > 0

                else 0

            )


            #---------------------------------


            orders_count = (

                generate_orders_count()

                if sessions_count > 0

                else 0

            )


            #---------------------------------


            is_active = (

                generate_is_active(

                    sessions_count,

                    features_used_count,

                    orders_count

                )

            )


            #---------------------------------


            activity_id = (

                generate_uuid()

            )


            activity_data.append(

                [

                    activity_id,
                    user_id,
                    current_date,
                    sessions_count,
                    total_minutes,
                    features_used_count,
                    orders_count,
                    is_active

                ]

            )


            current_date += timedelta(

                days=1

            )


    #=================================================


    columns = [

        "activity_id",
        "user_id",
        "activity_date",
        "sessions_count",
        "total_minutes",
        "features_used_count",
        "orders_count",
        "is_active"

    ]


    activity_df = pd.DataFrame(

        activity_data,

        columns=columns

    )


    export_csv(

        activity_df,

        "user_daily_activity.csv"

    )


    print_success_message(

        "user_daily_activity.csv"

    )


    return activity_df


#=====================================================


if __name__ == "__main__":

    print(

        "Use generate_data.py"

    )
