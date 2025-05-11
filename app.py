import streamlit as st
import requests
from bs4 import BeautifulSoup

def fetch_offers(location):
    # Placeholder offers
    return [
        {"store": "Store A", "offer": "Buy 1 Get 1 Free", "item": "Milk"},
        {"store": "Store B", "offer": "20% Off", "item": "Bread"},
        {"store": "Store C", "offer": "Free Delivery", "item": "Fruits"}
    ]

st.title("Grocery Offers Tracker")

location = st.text_input("Enter your location:")

if location:
    offers = fetch_offers(location)
    st.subheader(f"Offers near {location}:")
    for offer in offers:
        st.write(f"**{offer['store']}** - {offer['item']} - {offer['offer']}")
