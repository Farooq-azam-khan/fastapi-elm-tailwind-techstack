build: 
	pnpm --prefix app build 
	mkdir -p assets 
	mkdir -p templates
	cp -r app/dist/assets/* assets/
	cp app/dist/index.html templates/
	rm -r app/dist

format: 
	pnpm --prefix ./app run format 
	ruff format .
	isort .

stats:
	cloc --exclude-dir=favicons,node_modules,elm_stuff,.mypy_cache,__pycache__,.git,Makefile,tests,.vscode,.ruff_cache,.pytest_cache,.coverage --exclude-ext=js,css,html,jsonl,json,txt,md,yml,yaml,json,csv,excalidraw,env,sh .
	
test:
	pytest .
	pnpm --prefix app test

test-coverage: 
	pytest --cov
	pnpm --prefix app test:coverage

backend: 
	uvicorn main:app --reload

frontend: 
	pnpm --prefix app start

# TODO: figure out which process id to kill 
# kill_backend: 
# 	kill -9 $(pgrep uvicorn)

