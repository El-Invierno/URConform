from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class WebLink(BaseModel):
    '''Any url or website link in the text.'''

    link : Optional[str] = Field(
        default=None, description="The link or url to any website or webapp."
    )

class LanguageSpoken(BaseModel):
    """A human language that is used to converse and communicate."""

    language : Optional[str] = Field(
        default=None, description="Any spoken or written human language mentioned in the text."
    )

class PersonalDetails(BaseModel):
    '''Personal Information and details of the person.'''

    name : Optional[str] = Field(
        default=None, description="The name of the person."
    )
    email : Optional[str] = Field(
        default=None, description="The email address of the person."
    )
    mobile_number : Optional[str] = Field(
        default=None, description="The mobile number of the person."
    )
    links : Optional[List[WebLink]] = Field(
        default=None,description="The list of all the links in the text."
    )
    personal_summary : Optional[str] = Field(
        default=None, description="A very detailed long-format career-objective that introduces and summarizes the expertise and experience of the person in discussion."
    )
    languages_spoken : Optional[LanguageSpoken] = Field(
        default=None, description="The list of all the human languages mentioned in the text."
    )
    years_of_experience : Optional[str] = Field(
        default=None, description="The total number of years of experience the candidate has mentioned in the text."
    )

def get_personal_chain():
    llm = ChatOpenAI(model="gpt-4o")

    structured_llm = llm.with_structured_output(schema=PersonalDetails)

    prompt_template = ChatPromptTemplate(
        [
            ('system', "You are an expert resume extraction algorithm. "
                "Extract all relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value."),
            ('human', """ Example Text : John Doe is a data scientist with 8 years of experience in the field of machine learning and artificial intelligence. 
                He is fluent in English and Spanish. John has worked on various AI projects, contributing significantly to open-source repositories. 
                His personal portfolio can be viewed at https://johndoeportfolio.com, and his LinkedIn profile is available at https://linkedin.com/in/johndoe. 
                You can reach him at john.doe@example.com or call him directly at +1-234-567-8901. 
                He is passionate about solving complex data challenges and has a strong background in both technical leadership and hands-on development."""),
            ('ai', """PersonalDetails(
                    name='John Doe', 
                    email='john.doe@example.com', 
                    mobile_number='+1-234-567-8901', 
                    links=[
                        WebLink(link='https://johndoeportfolio.com'), 
                        WebLink(link='https://linkedin.com/in/johndoe')
                    ], 
                    personal_summary='John Doe is a data scientist with 8 years of experience in the field of machine learning and artificial intelligence. He is passionate about solving complex data challenges and has a strong background in both technical leadership and hands-on development.', 
                    languages_spoken=LanguageSpoken(language='English, Spanish'), 
                    years_of_experience='8 years)
            """),          
            ('human', '{text}'),
        ]
    )
    chain = prompt_template | structured_llm
    return chain