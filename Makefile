build:
	docker build -t lyricscount .

run:
	docker run -it -w $pwd:/python lyricscount:latest bash 