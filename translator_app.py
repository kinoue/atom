def app():
    import streamlit as st
    from llms import llms
    from langchain.schema import HumanMessage, SystemMessage

    llm = llms['gpt4']['model']

    st.title('LangChain Translator')

    # Get user input
    text = st.text_input('Enter text to translate:')

    # List of languages supported by GPT4
    languages = ['English', 'French', 'German', 'Spanish', 'Italian', 'Dutch', 'Russian', 'Japanese', 'Chinese', 'Korean', 'Arabic']

    # Create a dropdown menu for language selection
    target_language = st.selectbox('Select target language:', languages)

    # Translate the text
    if st.button('Translate'):
        system_message = SystemMessage(content=f'Translate the following text into {target_language}')
        human_message = HumanMessage(content=text)
        messages = [system_message, human_message]
        system_message = llm(messages)
        translation = system_message.content
        st.write(f'Translation: {translation}')