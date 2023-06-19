# Fastapi + Elm + Tailwindcss tech stack 

1. Setup elm app 
    * `git submodule init`
    * `git submodule update`
2. Remove `.git` for the project
    * `rm -rf .git`
    * `rm .gitmodules`
3. Install poetry 
    * ubuntu/debian based systems: `sudo apt install python3-poetry` 
4. Install dependencies
    * `poetry install` in the root folder 
5. Run the fastapi server 
    * `poetry run uvicorn main:app --reload`
6. Install npm packages
    * `cd app`
    * `npm install` 
    * `npm start` - to start the local development server 

