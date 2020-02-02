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

While the songs have been filtered as much as possible the same song might appear more than once.
Sometimes the returned value does not return any lyrics and a HTTP error is returned. Simply re-run the program.