import asyncio
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

parser = LlamaParse(result_type="text")
file_extractor = {'.pdf': parser, '.docx': parser}

async def process_documents():
    print("Starting document processing...")
    documents = await SimpleDirectoryReader(input_dir="./data/initial_resume", file_extractor=file_extractor).aload_data()
    print(f"Number of documents loaded: {len(documents)}")

    final_data = {}
    existing_file_names = set()

    for doc in documents:
        current_content = doc.text
        current_file = doc.metadata['file_name']
        if current_file in existing_file_names:
            final_data[current_file] += "\n\n" + current_content
        else:
            existing_file_names.add(current_file)
            final_data[current_file] = current_content

    print("Document processing completed successfully!")
    return final_data

async def main():
    print("Starting the asynchronous document loading process...")
    data = await process_documents()
    print("Asynchronous document loading process completed!")
    return data

if "__name__" == "__main__":
    asyncio.run(main())