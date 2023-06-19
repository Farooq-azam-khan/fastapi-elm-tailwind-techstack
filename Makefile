build: 
	npm --prefix ./app/ run build 
	cp -r app/dist/assets/* assets/
	cp app/dist/index.html templates/
