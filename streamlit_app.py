"""A Streamlit app for getting the Google autocomplete queries
"""
import json

import requests
import streamlit as st

def google_autocomplete(keyword: str) -> list[str]:
    """Get Google autocomplete queries for a seed keyword

    Args:
        keyword (str): The seed keyword

    Returns:
        list[str]: A list of the autocomplete queries
    """
    google_autocomplete_api: str = "https://www.google.com/complete/search"
    google_autocomplete_params: dict = {
        "q": keyword,
        "cp": 8,
        "client": "gws-wiz",
        "xssi": "t",
        "hl": "en-US"
    }

    response = requests.get(google_autocomplete_api, params=google_autocomplete_params)

    list_google_autocomplete_uncleaned: list[list] = json.loads((response.content).decode("UTF-8")[5:])[0]
    list_google_autocomplete_cleaned: list[str] = [
        element[0].replace('<b>', '').replace('</b>', '')
        for element in list_google_autocomplete_uncleaned
        ]

    return list_google_autocomplete_cleaned
