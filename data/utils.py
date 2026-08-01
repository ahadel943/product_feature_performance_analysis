# ==============================================
# Imports
# ==============================================

import uuid
import random
import numpy as np
import pandas as pd

from pathlib import Path

from datetime import datetime
from datetime import timedelta

from config import *


# ==============================================
# UUID Generator
# ==============================================

def generate_uuid():

    return str(uuid.uuid4())


# ==============================================
# Weighted Random Choice
# ==============================================

def weighted_choice(data: dict):

    values = list(data.keys())

    weights = list(data.values())

    return random.choices(
        population=values,
        weights=weights,
        k=1
    )[0]


# ==============================================
# Random Date Generator
# ==============================================

def random_datetime(
        start_date,
        end_date
):

    seconds = int(
        (end_date - start_date).total_seconds()
    )

    random_second = random.randint(
        0,
        seconds
    )

    return start_date + timedelta(
        seconds=random_second
    )


# ==============================================
# Generate Signup Date
# ==============================================

def generate_signup_date():

    return random_datetime(
        START_DATE,
        END_DATE
    )


# ==============================================
# Generate Premium Date
# ==============================================

def generate_premium_date(
        signup_date
):

    max_days = max(
        1,
        (END_DATE - signup_date).days
    )

    return signup_date + timedelta(

        days=random.randint(
            1,
            min(max_days,90)
        )

    )


# ==============================================
# Country Generator
# ==============================================

def generate_country():

    return weighted_choice(
        COUNTRIES
    )


# ==============================================
# City Generator
# ==============================================

def generate_city(
        country
):

    return random.choice(
        CITIES[country]
    )


# ==============================================
# Device Generator
# ==============================================

def generate_device():

    return weighted_choice(
        DEVICE_TYPES
    )


# ==============================================
# Acquisition Channel Generator
# ==============================================

def generate_acquisition_channel():

    return weighted_choice(
        ACQUISITION_CHANNELS
    )


# ==============================================
# Customer Type Generator
# ==============================================

def generate_customer_type():

    return weighted_choice(
        CUSTOMER_TYPES
    )


# ==============================================
# Premium Generator
# ==============================================

def generate_is_premium():

    return weighted_choice(
        PREMIUM_TYPES
    )


# ==============================================
# Age Group Generator
# ==============================================

def generate_age_group():

    return weighted_choice(
        AGE_GROUPS
    )


# ==============================================
# Session Duration Generator
# ==============================================

def generate_session_duration():

    return random.randint(

        SESSION_DURATION["MIN"],

        SESSION_DURATION["MAX"]

    )


# ==============================================
# Order Amount Generator
# ==============================================

def generate_order_amount():

    return round(

        random.uniform(

            ORDER_AMOUNT["MIN"],

            ORDER_AMOUNT["MAX"]

        ),

        2

    )


# ==============================================
# Product Price Generator
# ==============================================

def generate_product_price():

    return round(

        random.uniform(
            10,
            4000
        ),

        2

    )


# ==============================================
# Feature Adoption Check
# ==============================================

def adopted_feature(
        feature_name
):

    probability = FEATURE_ADOPTION_RATES[
        feature_name
    ]

    return random.random() <= (
            probability / 100
    )


# ==============================================
# Session End Time Generator
# ==============================================

def generate_session_end(

        session_start

):

    duration = generate_session_duration()

    return session_start + timedelta(
        minutes=duration
    )


# ==============================================
# Create Folder
# ==============================================

def create_export_folder():

    Path(
        EXPORT_FOLDER
    ).mkdir(

        parents=True,
        exist_ok=True

    )


# ==============================================
# Export CSV
# ==============================================

def export_csv(

        dataframe,
        file_name

):

    path = (

        Path(EXPORT_FOLDER)

        / file_name

    )

    dataframe.to_csv(

        path,

        index=False

    )


# ==============================================
# Chunk Export CSV
# ==============================================

def chunk_export(

        dataframe,
        file_name,
        mode="a",
        header=False

):

    path = (

        Path(EXPORT_FOLDER)

        / file_name

    )

    dataframe.to_csv(

        path,

        mode=mode,

        header=header,

        index=False

    )


# ==============================================
# Date Validation
# ==============================================

def validate_dates(

        start_date,
        end_date

):

    return end_date >= start_date


# ==============================================
# Percentage Calculator
# ==============================================

def calculate_percentage(

        numerator,
        denominator

):

    if denominator == 0:

        return 0

    return round(

        (numerator / denominator) * 100,

        2

    )


# ==============================================
# Success Message
# ==============================================

def print_success_message(

        table_name

):

    print(

        f"{table_name} generated successfully."

    )
