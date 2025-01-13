from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class ToolCategory(BaseModel):
    """A category of tools with a list of tools under it."""
    category: Optional[str] = Field(default=None, description= "Category of tech-tools. It has a list of tools associated with itself.")
    tools: Optional[List[str]] = Field(default=None, description= "List of all the tech tools related to a certain category.")

class ToolsAndTechnologies(BaseModel):
    """A flexible schema representing tools and technologies."""
    categories: Optional[List[ToolCategory]] = Field(default=None, description= "It is a list of ToolCategories.")

def get_tools_chain():
    llm = ChatOpenAI(model="gpt-4o")

    structured_llm_2 = llm.with_structured_output(schema=ToolsAndTechnologies)

    prompt_template2 = ChatPromptTemplate(
        [
            ('system', "You are an expert resume extraction algorithm. "
                "Extract all relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value."),
            ('human', """ 
                Example Text: 

                The following table represents various tools and technologies categorized under specific domains:

                - **Databases**: MS SQL Server
                - **Programming**: Python, PySpark, Spark, Hive, Azure DevOps, SQL, U-SQL, Oozie, NoSQL (Cosmos DB)
                - **Data Integration & ETL**: Azure Data Factory
                - **Issue Tracking & Project Management**: JIRA
                - **Visualization Tools**: Power BI
                - **Cloud Data**: Databricks, Azure Data Lake, Azure Synapse

                The goal is to extract the information into a structured format with the following fields:

                - `category`: The category name representing the type of tools or technologies.
                - `tools`: A list containing the tools mentioned under each category."""),
            ('ai', """ToolsAndTechnologies(
                categories=[
                    ToolCategory(category="Databases", tools=["MS SQL Server"]),
                    ToolCategory(category="Programming", tools=[
                        "Python", "PySpark", "Spark", "Hive", "Azure DevOps", "SQL", "U-SQL", "Oozie", "NoSQL (Cosmos DB)"
                    ]),
                    ToolCategory(category="Data Integration & ETL", tools=["Azure Data Factory"]),
                    ToolCategory(category="Issue Tracking & Project Management", tools=["JIRA"]),
                    ToolCategory(category="Visualization Tools", tools=["Power BI"]),
                    ToolCategory(category="Cloud Data", tools=["Databricks", "Azure Data Lake", "Azure Synapse"])
                ]
                )
            """),          
            ('human', '{text}'),
        ]
    )
    chain2 = prompt_template2 | structured_llm_2
    return chain2