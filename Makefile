build:
	docker build -t lyricscount .

run:
	docker run --rm -it -v ${PWD}:/python lyricscount:latest bash