import asyncio
import aiofiles
from parse_data import main as alt_main
from ext.per import get_personal_chain
from ext.tool import get_tools_chain
from ext.emp import get_employment_chain 
from ext.edu import get_education_chain
from ext.tex import get_tex_chain
from ext.project import s

async def create_tex_files(final_data):
    output_dir = "./output_tex/"
    chain = get_tex_chain()
    async def process_file(file_name, file_content):
        sanitized_file_name = file_name.split('.')[0]
        result = await chain.ainvoke({'text' : file_content, 'template' : s})
        async with aiofiles.open(f"{output_dir}{sanitized_file_name}.tex", "w") as file:
            await file.write(result.content)
    await asyncio.gather(*(process_file(file_name,file_content) for file_name, file_content in final_data.items()))
    print("All the files have been created.")

def invoke_chain(chain_func, data):
    chain = chain_func()
    return chain.invoke({'text': data}).dict()

async def parallel_exec(data):
    final_data = {}
    async def process_file(file_name, file_content):
        tasks = {
            'personal': get_personal_chain().ainvoke({'text': file_content}),
            'tools': get_tools_chain().ainvoke({'text': file_content}),
            'employment': get_employment_chain().ainvoke({'text': file_content}),
            'education': get_education_chain().ainvoke({'text': file_content})
        }
        results = await asyncio.gather(*tasks.values(), return_exceptions=True)
        print(results)
        results_dict = {}
        for key, result in zip(tasks.keys(), results):
            if isinstance(result, Exception):
                print(f"Error in {key} chain: {result}")
            else:
                results_dict[key] = result

        final_data[file_name] = results_dict

    await asyncio.gather(*(process_file(file_name, file_content) for file_name, file_content in data.items()))

    return final_data

async def main():
    data = await alt_main()
    final_data = await parallel_exec(data)
    await create_tex_files(final_data)

if __name__ == "__main__":
    asyncio.run(main())