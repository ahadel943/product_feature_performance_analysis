import os
import pandas as pd

FILE_PATH = r"E:\DataAnalysis\_Projects\proj_17\datasets"

def load_users(columns=None):

    parse_dates = ["signup_date", "premium_start_date"]

    if columns is not None:
        parse_dates = [
            col
            for col in parse_dates
            if col in columns
        ]

    file_path = os.path.join(FILE_PATH, "users.csv")

    return pd.read_csv(
        file_path,
        usecols=columns,
        parse_dates=parse_dates
    )


def load_orders(columns=None):
    """
        LOAD orders DATA
    """
    file_path = os.path.join(FILE_PATH, "orders.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["order_date"],
        usecols=columns
    )


def load_products(columns=None):
    """
        LOAD products DATA
    """
    file_path = os.path.join(FILE_PATH, "products.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["launch_date"],
        usecols=columns
    )

def load_sessions(columns=None):
    """
        LOAD sessions DATA
    """
    file_path = os.path.join(FILE_PATH, "sessions.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["session_start", "session_end"],
        usecols=columns
    )

def load_feature_adoptions(columns=None):
    """
        LOAD feature_adoptions data
    """
    file_path = os.path.join(FILE_PATH, "feature_adoptions.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["adoption_date"],
        usecols=columns
    )

def load_feature_events(columns=None):
    """
        load feature_events data
    """
    file_path = os.path.join(FILE_PATH, "feature_events.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["event_timestamp"],
        usecols=columns
    )

def load_features(columns=None):
    """
        load features data
    """
    file_path = os.path.join(FILE_PATH, "features.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["launch_date"],
        usecols=columns
    )

def load_order_items(columns=None):
    """
        load order_items data
    """
    file_path = os.path.join(FILE_PATH, "order_items.csv")
    return pd.read_csv(
        file_path,
        usecols=columns
    )

def load_subscriptions(columns=None):
    """
        load subscriptions data
    """
    file_path = os.path.join(FILE_PATH, "subscriptions.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["subscription_start_date", "subscription_end_date"],
        usecols=columns
    )

def load_user_daily_activity(columns=None):
    """
        load user_daily_activity data
    """
    file_path = os.path.join(FILE_PATH, "user_daily_activity.csv")
    return pd.read_csv(
        file_path,
        parse_dates=["activity_date"],
        usecols=columns
    )