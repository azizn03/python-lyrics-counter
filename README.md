Prerequisites

- make
- docker 

## Getting Started

- Build Docker file using: `make build`
- Run Docker file using: `make run`
- Go into the /python directory within the container. command `cd /python`
- Run CLI python script using command `python lyrics_counter.py` 

## Program details

This program searches for 5 songs and average the word from the lyrics of those 5 songs.

## Bugs

While the songs have been filtered as much as possible the same song might appear more than once. Given more time I would have implemented a matching system which would discard the same song and re-run the loop which pulls another song via the musicbrainzngs.search_releases query

Sometimes the returned value does not return any lyrics and a HTTP error is returned. Simply re-run the program. Given more time I would have restructured the musicbrainzngs query so it always returns a song with lyrics and the URL section which parses the song name into the URL to work more consistantly.   