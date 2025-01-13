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