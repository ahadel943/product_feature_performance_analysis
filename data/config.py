# ==============================================
# Imports
# ==============================================

from datetime import datetime


# ==============================================
# Dataset Size
# ==============================================

ROWS_COUNT = {

    "users": 300_000,
    "products": 15_000,
    "features": 6,
    "sessions": 6_000_000,
    "feature_events": 12_000_000,
    "orders": 420_000,
    "order_items": 1_500_000,
    "feature_adoptions": 1_200_000,
    "subscriptions": 200_000,
    "user_daily_activity": 15_000_000

}


# ==============================================
# Project Date Range
# ==============================================

START_DATE = datetime(2025, 1, 1)

END_DATE = datetime(2025, 12, 31)


# ==============================================
# Countries Distribution
# ==============================================

COUNTRIES = {

    "Egypt": 32,
    "Saudi Arabia": 23,
    "UAE": 18,
    "Kuwait": 12,
    "Jordan": 8,
    "Qatar": 4,
    "Bahrain": 3

}


# ==============================================
# Cities
# ==============================================

CITIES = {

    "Egypt": [
        "Cairo",
        "Alexandria",
        "Giza",
        "Mansoura",
        "Tanta",
        "Zagazig",
        "Assiut"
    ],

    "Saudi Arabia": [
        "Riyadh",
        "Jeddah",
        "Dammam",
        "Mecca",
        "Medina"
    ],

    "UAE": [
        "Dubai",
        "Abu Dhabi",
        "Sharjah",
        "Ajman"
    ],

    "Kuwait": [
        "Kuwait City",
        "Hawalli",
        "Farwaniya"
    ],

    "Jordan": [
        "Amman",
        "Irbid",
        "Zarqa"
    ],

    "Qatar": [
        "Doha",
        "Al Wakrah"
    ],

    "Bahrain": [
        "Manama",
        "Muharraq"
    ]

}


# ==============================================
# Device Types Distribution
# ==============================================

DEVICE_TYPES = {

    "Mobile": 68,
    "Desktop": 24,
    "Tablet": 8

}


# ==============================================
# Customer Types Distribution
# ==============================================

CUSTOMER_TYPES = {

    "New": 61,
    "Returning": 39

}


# ==============================================
# Premium Users Distribution
# ==============================================

PREMIUM_TYPES = {

    True: 33,
    False: 67

}


# ==============================================
# Acquisition Channels Distribution
# ==============================================

ACQUISITION_CHANNELS = {

    "Organic Search": 28,
    "Direct": 22,
    "Social Media": 18,
    "Paid Search": 15,
    "Referral": 9,
    "Email": 5,
    "Influencers": 3

}


# ==============================================
# Age Groups Distribution
# ==============================================

AGE_GROUPS = {

    "18-24": 18,
    "25-34": 41,
    "35-44": 24,
    "45-54": 11,
    "55+": 6

}


# ==============================================
# Product Categories
# ==============================================

PRODUCT_CATEGORIES = {

    "Electronics": [
        "Phones",
        "Laptops",
        "Accessories",
        "Gaming"
    ],

    "Fashion": [
        "Men",
        "Women",
        "Shoes",
        "Watches"
    ],

    "Home": [
        "Furniture",
        "Kitchen",
        "Decor",
        "Lighting"
    ],

    "Beauty": [
        "Skincare",
        "Makeup",
        "Perfumes"
    ],

    "Sports": [
        "Fitness",
        "Cycling",
        "Outdoor"
    ],

    "Books": [
        "Business",
        "Technology",
        "Fiction"
    ]

}


# ==============================================
# Features & Launch Dates
# ==============================================

FEATURES = {

    "Wishlist": "2025-01-15",

    "Buy Again": "2025-03-01",

    "Flash Deals": "2025-04-15",

    "Smart Search": "2025-06-01",

    "Recommendations": "2025-08-01",

    "Save for Later": "2025-10-01"

}


# ==============================================
# Target Adoption Rates
# ==============================================

FEATURE_ADOPTION_RATES = {

    "Wishlist": 55,

    "Smart Search": 58,

    "Flash Deals": 34,

    "Recommendations": 21,

    "Save for Later": 17,

    "Buy Again": 8

}


# ==============================================
# Business Rules Multipliers
# ==============================================

PREMIUM_MULTIPLIER = {

    "Wishlist": 1.10,
    "Buy Again": 1.80,
    "Flash Deals": 0.90,
    "Smart Search": 1.00,
    "Recommendations": 1.20,
    "Save for Later": 1.15

}


RETENTION_MULTIPLIER = {

    "Wishlist": 1.30,
    "Buy Again": 2.10,
    "Flash Deals": 1.10,
    "Smart Search": 1.60,
    "Recommendations": 1.50,
    "Save for Later": 1.80

}


CONVERSION_MULTIPLIER = {

    "Wishlist": 1.40,
    "Buy Again": 1.90,
    "Flash Deals": 1.50,
    "Smart Search": 0.80,
    "Recommendations": 1.60,
    "Save for Later": 0.85

}


REVENUE_MULTIPLIER = {

    "Wishlist": 1.30,
    "Buy Again": 2.30,
    "Flash Deals": 1.70,
    "Smart Search": 0.90,
    "Recommendations": 1.50,
    "Save for Later": 0.80

}


# ==============================================
# Default Session Duration (Minutes)
# ==============================================

SESSION_DURATION = {

    "MIN": 2,
    "MAX": 75

}


# ==============================================
# Order Amount Rules
# ==============================================

ORDER_AMOUNT = {

    "MIN": 25,
    "MAX": 5000

}


# ==============================================
# Export Path
# ==============================================

EXPORT_FOLDER = "datasets"
