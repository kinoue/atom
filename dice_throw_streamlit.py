import streamlit as st
import random

def app():
    st.title('Dice Throw Simulator')
    if st.button('Throw Dice'):
        result = random.randint(1, 6)
        st.success('You rolled {}'.format(result))