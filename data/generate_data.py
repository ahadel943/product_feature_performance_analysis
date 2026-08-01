import time

from users import generate_users
from products import generate_products
from features import generate_features
from subscriptions import generate_subscriptions
from sessions import generate_sessions
from user_daily_activity import generate_user_daily_activity
from feature_adoptions import generate_feature_adoptions
from feature_events import generate_feature_events
from orders import generate_orders
from order_items import generate_order_items

from validation import run_validation

from utils import create_export_folder



# =====================================================
# Main Pipeline
# =====================================================


def generate_all_data():


    start_time = time.time()


    print("\n========== START DATA GENERATION ==========\n")


    # -----------------------------------------------
    # Create Output Folder
    # -----------------------------------------------

    create_export_folder()



    # -----------------------------------------------
    # Users
    # -----------------------------------------------

    print("Generating Users...")

    users_df = generate_users()



    # -----------------------------------------------
    # Products
    # -----------------------------------------------

    print("Generating Products...")

    products_df = generate_products()



    # -----------------------------------------------
    # Features
    # -----------------------------------------------

    print("Generating Features...")

    features_df = generate_features()



    # -----------------------------------------------
    # Subscriptions
    # -----------------------------------------------

    print("Generating Subscriptions...")

    subscriptions_df = generate_subscriptions(

        users_df

    )



    # -----------------------------------------------
    # Sessions
    # -----------------------------------------------

    print("Generating Sessions...")

    sessions_df = generate_sessions(

        users_df

    )



    # -----------------------------------------------
    # Daily Activity
    # -----------------------------------------------

    print("Generating User Daily Activity...")

    user_daily_activity_df = (

        generate_user_daily_activity(

            users_df

        )

    )



    # -----------------------------------------------
    # Feature Adoption
    # -----------------------------------------------

    print("Generating Feature Adoptions...")

    feature_adoptions_df = (

        generate_feature_adoptions(

            users_df,

            features_df

        )

    )



    # -----------------------------------------------
    # Feature Events
    # -----------------------------------------------

    print("Generating Feature Events...")

    feature_events_df = (

        generate_feature_events(

            feature_adoptions_df,

            features_df,

            sessions_df,

            users_df

        )

    )



    # -----------------------------------------------
    # Orders
    # -----------------------------------------------

    print("Generating Orders...")

    orders_df = generate_orders(

        sessions_df

    )



    # -----------------------------------------------
    # Order Items
    # -----------------------------------------------

    print("Generating Order Items...")

    order_items_df = generate_order_items(

        orders_df,

        products_df

    )



    # -----------------------------------------------
    # Validation
    # -----------------------------------------------


    print("\nRunning Validation...")


    datasets = {


        "users": users_df,

        "products": products_df,

        "features": features_df,

        "subscriptions": subscriptions_df,

        "sessions": sessions_df,

        "user_daily_activity": user_daily_activity_df,

        "feature_adoptions": feature_adoptions_df,

        "feature_events": feature_events_df,

        "orders": orders_df,

        "order_items": order_items_df


    }



    run_validation(

        datasets

    )



    # -----------------------------------------------
    # Finished
    # -----------------------------------------------


    elapsed = round(

        time.time() - start_time,

        2

    )


    print(

        "\n========== DATA GENERATION FINISHED =========="

    )


    print(

        f"Total Time: {elapsed} seconds"

    )


    return datasets




# =====================================================
# Run
# =====================================================


if __name__ == "__main__":


    generate_all_data()