import streamlit as st
import requests
import numpy as np

# Function to fetch GIFs from Giphy API
def search_gifs(api_key, search_term, limit=3, rating="g"):
    endpoint = "https://api.giphy.com/v1/gifs/search"
    params = {"api_key": api_key, "limit": limit, "q": search_term, "rating": rating}
    response = requests.get(endpoint, params=params).json()
    return response["data"]


def calculate(num1, num2, operation):
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = None
    return result




st.title('Slider Number')
number = st.slider('Pick a number', 0, 100)
st.write('You selected:', number)

# Streamlit app
st.title('Simple Calculator')

# User input for the numbers and operation
num1 = st.number_input('Enter the first number:', value=0.0, format='%f')
num2 = st.number_input('Enter the second number:', value=0.0, format='%f')
operation = st.radio('Select operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Button to trigger the calculation
if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.success(f'Result: {result}')

# Additional styling for a simple calculator-like appearance
st.markdown("""
<style>
    .st-eb {
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 1rem;
    }

    .stButton button {
        background-color: #007bff;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Your Giphy API key
API_KEY = "NxBNkj22iEIwGGxPftZJi2uT8fVtnZYO"

# Streamlit app
st.title('GIF Search App')
st.write('Search and display GIFs using the Giphy API')

# User input for search term
search_term = st.text_input('Enter a search term:', 'Hello, world!')


# Button to trigger the search
if st.button('Search'):
    st.write(f'Searching for GIFs related to "{search_term}"...')
    gifs = search_gifs(API_KEY, search_term)

    # Display the results
    if gifs:
        st.write('Here are some GIFs:')
        for gif in gifs:
            title = gif["title"]
            url = gif["images"]["fixed_height"]["url"]
            st.image(url, caption=title, use_column_width=True)
    else:
        st.write('No GIFs found. Try a different search term.')

# Additional information or instructions
st.write('Note: just a random note')
