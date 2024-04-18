build: 
	pnpm --prefix ./app/ run build 
	mkdir -p assets 
	mkdir -p templates
	cp -r app/dist/assets/* assets/
	cp app/dist/index.html templates/
	cp app/dist/*.js assets/
	cp app/dist/manifest.webmanifest assets/

format: 
	pnpm --prefix ./app run format 
	ruff format .
	isort .


stats:
	cloc --exclude-dir=favicons,node_modules,elm_stuff,.mypy_cache,__pycache__,.git,Makefile,tests,.vscode,.ruff_cache,.pytest_cache,.coverage --exclude-ext=js,css,html,jsonl,json,txt,md,yml,yaml,json,csv,excalidraw,env,sh .

