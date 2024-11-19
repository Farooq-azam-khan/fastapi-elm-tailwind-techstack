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
* [ ] consider the following features and the products available for them 
   * [ ] auth: clerk, auth0
   * [ ] error tracking for python: sentry
   * [ ] payment processing: stripe, square
   * [ ] web analytics: posthog
   * [ ] a/b testing: posthog
   * [ ] key value storage : redis, upstash
   * [ ] relational db : postgres, aws, azure, gcp 
   * [ ] static asset storage : aws s3, azure storage account
   * [ ] vector db : upstash
   * [ ] rate limiting : upstash, custom dev 
* [ ] design considerations for a `cli` tool for easy setup
   * [ ] a watch script that looks at the `api.py` file and generate elm functions that make http requests based on the types
