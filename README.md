# Tech Stack

## Technologies 
* FastAPI
* Elm
* Tailwindcss
* Typescript

## Setup 
0. setup this repo + elm app repo 
```bash 
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


## TODO
* [ ] add `termcolor` to list of python packages
* [ ] look into auth with clerk
* [ ] look into error tracking with sentry
* [ ] looking into stripe testing
* [ ] look into posthog for web analytics + a/b testing
* [ ] look into vector db + key value db with upstash
* [ ] design considerations for a `cli` tool for easy setup
