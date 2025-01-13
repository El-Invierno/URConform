from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def get_tex_chain():
    llm = ChatOpenAI(model='gpt-4o')
    prompt_template = ChatPromptTemplate(
        [
            ('system',"""
                You are a LaTeX expert specializing in generating professional documents. 
                When provided with structured data such as personal information, education details, certifications, tools, technologies, and professional experience, generate a complete LaTeX document.
                The document should include appropriate formatting, sections, and styling. 
                Ensure the output adheres strictly to the provided data without fabricating or hallucinating any information. 
                Maintain clean and professional design using standard LaTeX packages like `graphicx`, `amsmath`, `hyperref`, and `fullpage`. 
                Provide only the LaTeX code as the response, with no additional comments, explanations, or deviations.
            """),
            ('human',"""Fill this data into the template and give the output. Just the latex code nothing else. Please don't hallucinate.
                Data:
                {text}
                Template: 
                {template}
                Do not include the '''latex code block indicator in the output.
            """),
        ]
    )
    chain = prompt_template | llm
    return chain