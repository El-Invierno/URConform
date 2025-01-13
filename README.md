# URConform

### Guide to installation, setup & running.

1) Add a folder within the data folder called the initial_resume.
2) Add all the resume pdfs or word files in the 'data/initial_resume/' folder.
3) Create a '.env' file inside the root of the dir.
4) Add the "OPENAI_API_KEY" and "LLAMA_CLOUD_API_KEY" values inside the '.env' file.
5) Create a folder called output_tex in the root of the dir. This will be used to store the output latex (.tex) files.
6) Create a virtual env in the root of the dir.
7) Activate the virtual env.
8) Install all the requirements from the requirements.txt file. Use 'pip install -r requirements.txt'
9) Run the file using command 'py ./process_data.py'
10) Outputs will appear in the output_tex folder. They can be further be compiled to the pdf format.
11) You may need to install some vscode extensions to compile the '.tex' files into a standard '.pdf' format.


### Inner Workings [Code in Python]

1) Use Llama Parse to parse the resumes into a txt format. Store the data in a dict.
2) Created an asynchronous parsing mechanism on a single thread.
3) Used langchain for chain orchestration.
4) Used OpenAI api's gpt-4o to utilize the Structured Output functionality.
5) The extracted data is parsed and converted into a .tex [Latex file format].
6) The project uses Latex as we needed a precise typesetting language that would give consistent results in the required format.
7) The complete python app uses asynchronous single threaded programming wherever possible to increase the program's throughput.
