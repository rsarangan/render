# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     print("sarang here")
#     return 'sarang here'

import streamlit as st

st.radio('Pick one', ['cats', 'dogs'])