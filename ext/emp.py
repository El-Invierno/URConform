from typing import List, Optional
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class Project(BaseModel):
    """
    Represents a project the individual has worked on within a specific role at a company.
    """
    project_name: Optional[str] = Field(
        default=None, description="The name or title of the project worked on."
    )
    contributions: Optional[str] = Field(
        default=None, 
        description="A complete copy of the contribution and a very detailed and in-depth description of the roles, responsibilities, and contributions made to the project."
    )

class EmploymentRole(BaseModel):
    """
    Represents a role held by the individual at a company during a specific period.
    """
    role: Optional[str] = Field(
        default=None, 
        description="The job title or role held at the company."
    )
    company_name: Optional[str] = Field(
        default=None, 
        description="The name of the company where the role was held."
    )
    duration: Optional[str] = Field(
        default=None, 
        description="The duration for which the individual held this role (e.g., Jan 2020 - Dec 2021)."
    )
    projects: Optional[List[Project]] = Field(
        default=None, 
        description="A list of projects the individual worked on during this role, with detailed information on each project."
    )

class EmploymentExperience(BaseModel):
    """
    Represents the complete employment history of an individual, including multiple companies and roles.
    """
    employment_history: Optional[List[EmploymentRole]] = Field(
        default=None, 
        description="A list of employment roles across different companies, detailing the projects and contributions made in each role."
    )


def get_employment_chain():
    llm = ChatOpenAI(model="gpt-4o")

    structured_llm_3 = llm.with_structured_output(schema=EmploymentExperience)

    prompt_template3 = ChatPromptTemplate(
        [
            ('system', "You are an expert resume extraction algorithm. "
                "Extract all relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value."),
            ('human', """
                Senior Data Engineer, TechCorp Inc.
                AUGUST 2021 — PRESENT
                Roles & Responsibilities:
                • Led the migration of a legacy data platform to Azure Synapse, optimizing ETL pipelines and significantly improving data performance.
                • Implemented performance tuning strategies using partition pruning and spot VM optimizations, reducing data processing time by 30%.
                • Designed and deployed a comprehensive ACL framework in Unity Catalog, ensuring granular access control at the table, row, and column levels.
                • Created standardized PySpark notebooks for project teams, streamlining the loading of data into bronze, silver, and gold layers through autoloader and delta streaming processes.
                • Developed a data quality metrics framework focusing on completeness, uniqueness, and accuracy across datasets.
                • Tools Used: * Python * PySpark * Azure Synapse * Unity Catalog * SQL * PowerShell * Databricks * Azure Data Factory

                Data Analyst, DataWorks Ltd.
                JANUARY 2018 — JULY 2021
                Roles & Responsibilities:
                • Conducted customer segmentation analysis using clustering techniques and statistical modeling to identify market trends.
                • Built dashboards and reporting solutions for data-driven insights using Power BI and SQL Server.
                • Collaborated with cross-functional teams to enhance ETL pipelines and maintain data integrity across multiple business units.
                • Implemented data validation techniques to reduce data discrepancies by 20% across datasets.
                • Tools Used: * Power BI * SQL Server * Python * JIRA * Excel * Pandas
                """),
            ('ai', """EmploymentExperience(
                employment_history=[
                    EmploymentRole(
                        role="Senior Data Engineer",
                        company_name="TechCorp Inc.",
                        duration="Aug 2021 - Present",
                        projects=[
                            Project(
                                project_name="Data Platform Migration",
                                contributions="Led the migration of legacy data platform to Azure Synapse, implemented performance optimizations, and established ETL pipelines for streamlined data ingestion."
                            ),
                            Project(
                                project_name="Data Quality Metrics Framework",
                                contributions="Designed and implemented a framework for monitoring data quality metrics including completeness, accuracy, and validity across multiple datasets."
                            )
                        ]
                    ),
                    EmploymentRole(
                        role="Data Analyst",
                        company_name="DataWorks Ltd.",
                        duration="Jan 2018 - July 2021",
                        projects=[
                            Project(
                                project_name="Customer Segmentation Analysis",
                                contributions="Performed advanced customer segmentation using clustering techniques and provided actionable insights for marketing strategies."
                            )
                        ]
                    )
                ]
            )
            """),          
            ('human', '{text}'),
        ]
    )
    chain3 = prompt_template3 | structured_llm_3
    return chain3