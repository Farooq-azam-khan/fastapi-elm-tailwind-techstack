# Fastapi + Elm + Tailwindcss tech stack 

0. setup this repo + elm app repo 
```Bash 
npm i -g degit
mkdir work-dir
cd work-dir
npx degit https://github.com/Farooq-azam-khan/fastapi-elm-tailwind-techstack 
cd app 
npx degit https://github.com/Farooq-azam-khan/elm-vite-setup
cd ..
```
1. Install poetry 
    * ubuntu/debian based systems: `sudo apt install python3-poetry` 
2. Install dependencies
    * `poetry install` in the root folder 
3. Run the fastapi server 
    * `poetry run uvicorn main:app --reload`
    * visit: `localhost:8000/docs`
4. Install npm packages
    * `cd app`
    * `npm install` 
    * `npm start` - to start the local development server
    * visit: `http://localhost:5173`

