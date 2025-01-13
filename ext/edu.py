from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class EducationEntry(BaseModel):
    """
    Represents a single educational qualification, including degree, institution, and performance.
    """
    degree_or_standard: Optional[str] = Field(
        default=None, description="The name of the degree or standard completed (e.g., B.Tech, High School Diploma)."
    )
    institute_name: Optional[str] = Field(
        default=None, description="The name of the educational institution attended."
    )
    duration: Optional[str] = Field(
        default=None, description="The duration of study (e.g., Jan 2009 - Jan 2013)."
    )

class EducationHistory(BaseModel):
    """
    Represents the complete educational background of an individual.
    """
    education: Optional[List[EducationEntry]] = Field(
        default=None, description="A list of educational qualifications."
    )
    certificates : Optional[List[str]] = Field(
        default=None,description="List of all the certifications and their titles."
    )

def get_education_chain():
    llm = ChatOpenAI(model="gpt-4o")
    
    structured_llm_4 = llm.with_structured_output(schema=EducationHistory)

    prompt_template4 = ChatPromptTemplate(
        [
            ('system', "You are an expert resume extraction algorithm. "
                "Extract all relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value."),
            ('human', """
                Education:
                B. Tech, Biju Pattnaik University of Technology, Bhubaneswar
                JANUARY 2009 — JANUARY 2013
                Kendriya Vidyalaya
                MARCH 2009
                Prabhujee E.M. School, Bhubaneswar
                JANUARY 2007
                """),
            ('ai', """EducationHistory(
                education=[
                    EducationEntry(
                        degree_or_standard="B. Tech",
                        institute_name="Biju Pattnaik University of Technology, Bhubaneswar",
                        duration="January 2009 – January 2013"
                    ),
                    EducationEntry(
                        degree_or_standard=None,
                        institute_name="Kendriya Vidyalaya",
                        duration="March 2009"
                    ),
                    EducationEntry(
                        degree_or_standard=None,
                        institute_name="Prabhujee E.M. School, Bhubaneswar",
                        duration="January 2007"
                    )
                ]
            )
            """),          
            ('human', '{text}'),
        ]
    )
    chain4 = prompt_template4 | structured_llm_4
    return chain4