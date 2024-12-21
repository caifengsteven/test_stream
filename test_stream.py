## Importing the required libraries
import streamlit as st

## What is Streamlit?
## Streamlit is an open-source Python library that makes it easy to build custom web apps for data science, machine learning, and general interactive purposes.
## It is popular because it enables rapid prototyping and deployment of web-based dashboards and applications without the need for extensive web development knowledge.

## Title of the Streamlit App
st.title('CAI ZHIXIU Streamlit App')

## Adding some text description
st.write("Hello, this is a my first Streamlit application!")

## A number input box for user interaction
user_input = st.number_input('Enter a number:', value=0)

## Displaying the value entered by the user
st.write(f'You entered: {user_input}')

## Adding a button to the interface
if st.button('Click Me!'):
    st.write('You clicked the button!')

## Explanation
## Streamlit apps run on the local server, and they allow you to build interactive components like buttons, sliders, and text inputs
## simply by using Python code. This makes it a go-to tool for data scientists to showcase their models or explore datasets interactively.
