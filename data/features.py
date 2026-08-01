import pandas as pd

from config import *
from utils import *


#=====================================================


def generate_features():

    features_data = []


    for feature_name, launch_date in FEATURES.items():

        feature_id = generate_uuid()


        features_data.append(

            [

                feature_id,
                feature_name,
                launch_date

            ]

        )


    #=================================================


    columns = [

        "feature_id",
        "feature_name",
        "launch_date"

    ]


    features_df = pd.DataFrame(

        features_data,

        columns=columns

    )


    export_csv(

        features_df,

        "features.csv"

    )


    print_success_message(

        "features.csv"

    )


    return features_df


#=====================================================


if __name__ == "__main__":

    generate_features()
