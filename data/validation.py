import pandas as pd


from config import *



# =====================================================
# Row Count Validation
# =====================================================

def check_row_counts(dataframes):

    print("\n===== ROW COUNT CHECK =====")


    for table_name, expected in ROWS_COUNT.items():

        if table_name in dataframes:

            actual = len(
                dataframes[table_name]
            )


            status = (
                "PASS"
                if actual == expected
                else "WARNING"
            )


            print(
                f"{table_name}: {actual:,} / {expected:,} --> {status}"
            )



# =====================================================
# Primary Key Check
# =====================================================

def check_primary_keys(

        dataframe,
        column_name,
        table_name

):

    print(
        f"\nChecking PK: {table_name}"
    )


    nulls = dataframe[column_name].isna().sum()


    duplicates = dataframe[column_name].duplicated().sum()



    if nulls == 0 and duplicates == 0:

        print(
            "PASS"
        )

    else:

        print(
            f"FAILED | Nulls={nulls}, Duplicates={duplicates}"
        )



# =====================================================
# Foreign Key Check
# =====================================================

def check_foreign_key(

        child_df,
        child_column,
        parent_df,
        parent_column,
        relation_name

):

    print(
        f"\nChecking FK: {relation_name}"
    )


    missing = (

        ~child_df[child_column]

        .isin(

            parent_df[parent_column]

        )

    ).sum()



    if missing == 0:

        print(
            "PASS"
        )

    else:

        print(
            f"FAILED | Missing FK Records = {missing}"
        )



# =====================================================
# Date Validation
# =====================================================

def check_dates(

        users_df,
        sessions_df,
        orders_df,
        subscriptions_df

):


    print(
        "\n===== DATE QUALITY CHECK ====="
    )


    # Session after signup

    invalid_sessions = (

        sessions_df.merge(

            users_df[

                [
                    "user_id",
                    "signup_date"

                ]

            ],

            on="user_id"

        )

        .query(

            "session_start < signup_date"

        )

        .shape[0]

    )


    print(

        f"Sessions before signup: {invalid_sessions}"

    )



    # Orders after sessions


    invalid_orders = (

        orders_df.merge(

            sessions_df[

                [
                    "session_id",
                    "session_start"

                ]

            ],

            on="session_id"

        )

        .query(

            "order_date < session_start"

        )

        .shape[0]

    )


    print(

        f"Orders before session: {invalid_orders}"

    )



    # Premium date after signup


    premium_check = (

        subscriptions_df.merge(

            users_df[

                [
                    "user_id",
                    "signup_date"

                ]

            ],

            on="user_id"

        )

        .query(

            "subscription_start_date < signup_date"

        )

        .shape[0]

    )


    print(

        f"Premium before signup: {premium_check}"

    )




# =====================================================
# Feature Launch Validation
# =====================================================

def check_feature_dates(

        feature_adoptions_df,

        features_df

):


    print(

        "\n===== FEATURE DATE CHECK ====="

    )


    result = (

        feature_adoptions_df.merge(

            features_df,

            on="feature_id"

        )

    )


    invalid = (

        result.query(

            "adoption_date < launch_date"

        )

        .shape[0]

    )


    print(

        f"Adoption before launch: {invalid}"

    )




# =====================================================
# Distribution Check
# =====================================================

def check_distributions(

        users_df

):


    print(

        "\n===== DISTRIBUTION CHECK ====="

    )


    print("\nDevice Distribution")

    print(

        users_df["device_type"]

        .value_counts(normalize=True)

        .mul(100)

        .round(2)

    )



    print("\nPremium Distribution")

    print(

        users_df["is_premium"]

        .value_counts(normalize=True)

        .mul(100)

        .round(2)

    )




# =====================================================
# Feature Adoption Check
# =====================================================

def check_feature_adoption_rates(

        feature_adoptions_df,

        features_df

):


    print(

        "\n===== FEATURE ADOPTION ====="

    )


    total_users = (

        feature_adoptions_df

        ["user_id"]

        .nunique()

    )


    result = (

        feature_adoptions_df.merge(

            features_df,

            on="feature_id"

        )

        .groupby(

            "feature_name"

        )

        ["user_id"]

        .nunique()

        .reset_index()

    )


    result["adoption_rate"] = (

        result["user_id"]

        /

        total_users

        *

        100

    ).round(2)



    print(result)




# =====================================================
# Main Validation Runner
# =====================================================

def run_validation(

        dataframes

):


    print(

        "\n\n========== START VALIDATION =========="

    )


    check_row_counts(

        dataframes

    )


    check_primary_keys(

        dataframes["users"],

        "user_id",

        "users"

    )


    check_primary_keys(

        dataframes["orders"],

        "order_id",

        "orders"

    )


    check_primary_keys(

        dataframes["products"],

        "product_id",

        "products"

    )


    check_foreign_key(

        dataframes["sessions"],

        "user_id",

        dataframes["users"],

        "user_id",

        "sessions -> users"

    )


    check_foreign_key(

        dataframes["orders"],

        "session_id",

        dataframes["sessions"],

        "session_id",

        "orders -> sessions"

    )


    check_foreign_key(

        dataframes["order_items"],

        "product_id",

        dataframes["products"],

        "product_id",

        "order_items -> products"

    )


    check_dates(

        dataframes["users"],

        dataframes["sessions"],

        dataframes["orders"],

        dataframes["subscriptions"]

    )


    check_feature_dates(

        dataframes["feature_adoptions"],

        dataframes["features"]

    )


    check_distributions(

        dataframes["users"]

    )


    check_feature_adoption_rates(

        dataframes["feature_adoptions"],

        dataframes["features"]

    )


    print(

        "\n========== VALIDATION FINISHED =========="

    )