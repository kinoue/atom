import logging
import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from agent import ask_agent

def app():
    if 'messages' not in st.session_state:
        st.session_state['messages'] = [
            AIMessage(content="Hi! I'm SG-1! How can I help you?")
        ]

    dialogue_area = st.empty()
    user_input = st.chat_input("Say something.")

    with dialogue_area.container():
        if user_input:
            logging.info('Got user_input: ' + str(user_input))
            st.session_state.messages.append(HumanMessage(content=user_input))
            bot_response = ask_agent(st.session_state.messages)
            logging.info('Got bot_response: ' + str(bot_response))
            st.session_state.messages.append(AIMessage(content=bot_response['output']))
        for message in st.session_state.messages:
            if message.type == 'human':
                st_message = st.chat_message(
                    message.type
                )
            else:
                st_message = st.chat_message(
                    message.type,
                    avatar='https://talent.wendy.ai/assets/wendy_avatar.f53354a1.svg'
                )
            st_message.write(message.content)
