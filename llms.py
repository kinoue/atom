import os
from typing import Mapping, Any
from langchain_openai.chat_models import AzureChatOpenAI
from langchain_openai.chat_models import ChatOpenAI
from langchain.globals import set_llm_cache
from langchain.cache import SQLiteCache
from langchain_community.llms.bedrock import Bedrock
from langchain_community.llms.bedrock import BedrockBase

set_llm_cache(SQLiteCache(database_path="cache/langchain.db"))

class MyBedrock(Bedrock):
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {
            'model_id': self.model_id,
            **BedrockBase._identifying_params.__get__(self)
        }

class MyChatOpenAI(ChatOpenAI):
    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {
            key: value
            for key, value in ChatOpenAI._identifying_params.__get__(self).items()
            if key != 'max_tokens'
        }

gpt35az = {
    'model': AzureChatOpenAI(
        azure_endpoint='https://keisuke-openai-test.openai.azure.com/',
        deployment_name="gpt-35-turbo-ds-1",
        model_name="gpt-35-turbo (version 0301)",
        api_version='2023-03-15-preview',
        api_key=os.environ['AZURE_OPENAI_API_KEY'],
        temperature=0.0,
        max_tokens=500
    ),
    'metadata': {
        'model_type': 'gpt-3.5-turbo',
        'model_source': 'OpenAI',
        'model_service': 'Azure OpenAI'
    }
}

gpt35 = {
    'model': MyChatOpenAI(
        model_name="gpt-3.5-turbo",
        api_key=os.environ['OPENAI_API_KEY'],
        temperature=0.0,
        max_tokens=500
    ),
    'metadata': {
        'model_type': 'gpt-3.5-turbo',
        'model_source': 'OpenAI',
        'model_service': 'OpenAI'
    }
}

gpt4 = {
    'model': MyChatOpenAI(
        model_name='gpt-4',
        api_key=os.environ['OPENAI_API_KEY'],
        temperature=0.0,
        max_tokens=1200,
        organization='org-nsLrrVGLQ88wMLmkhC2HGDi7'
    ),
    'metadata': {
        'model_type': 'gpt-4',
        'model_source': 'OpenAI',
        'model_service': 'OpenAI'
    }
}

titan = {
    'model': MyBedrock(
        credentials_profile_name="default",
        model_id="amazon.titan-tg1-large",
        model_kwargs = {
            'maxTokenCount': 1500,
            'temperature': 0.1,
            'topP': 0.9,
        },
        cache=False
    ),
    'metadata': {
        'model_type': 'Titan Text Large',
        'model_source': 'Amazon',
        'model_service': 'AWS Bedrock'
    }
}


llama2 = {
    'model': MyBedrock(
        credentials_profile_name="default",
        model_id="meta.llama2-70b-chat-v1",
        model_kwargs = {
            'max_gen_len': 1500,
            'temperature': 0.1,
            'top_p': 0.9,
        }
    ),
    'metadata': {
        'model_type': 'Llama 2 70B',
        'model_source': 'Meta',
        'model_service': 'AWS Bedrock'
    }
}

claude2 = {
    'model': MyBedrock(
        credentials_profile_name="default",
        model_id="anthropic.claude-v2",
        model_kwargs={
            "max_tokens_to_sample": 500,
            "temperature": 0.1,
            "top_p": 0.9,
        }
    ),
    'metadata': {
        'model_type': 'Claude 2',
        'model_source': 'Anthropic',
        'model_service': 'AWS Bedrock'
    }
}

cohere = {
    'model':  MyBedrock(
        credentials_profile_name="default",
        model_id="cohere.command-text-v14",
        model_kwargs = {
            "max_tokens": 100,
            "temperature": 0.8,
            "return_likelihood": "GENERATION"
        }
    ),
    'metadata': {
        'model_type': 'Cohere Command V14.7',
        'model_source': 'Cohere',
        'model_service': 'AWS Bedrock'
    }
}

llms = {
    'gpt35az': gpt35az,
    'gpt35': gpt35,
    'gpt4': gpt4,
    'llama2': llama2,
    'claude2': claude2,
    'cohere': cohere,
    'titan': titan
}
