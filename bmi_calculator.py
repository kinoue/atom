import streamlit as st

def app():
    st.title('BMI Calculator')

    weight = st.number_input("Enter your weight (in kg)")
    height = st.number_input("Enter your height (in cm)")

    if st.button('Calculate BMI'):
        height = height / 100  # convert cm to meters
        bmi = weight / (height * height)
        st.text('Your Body Mass Index is: {}'.format(bmi))

if __name__ == "__main__":
    app()