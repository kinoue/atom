import streamlit as st

def app():
    # Title of the app
    st.title('Simple Calculator App')

    # Taking number inputs
    num1 = st.number_input('Enter First Number', value=0)
    num2 = st.number_input('Enter Second Number', value=0)

    # Selecting operation
    operation = st.selectbox('Select Operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

    # Performing operation and displaying result
    if st.button('Calculate'):
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
                result = 'Error! Division by zero'
        st.success(f'The result is: {result}')