import spacy

def watch_next(description:str):
    """Returns the title of a movie from 'movies.txt' whose description is most similar to 'description'."""
    nlp = spacy.load('en_core_web_md')

    # Reading in movie descriptions to compare
    with open("movies.txt", "r", encoding="utf-8") as movies:
        movie_descriptions = movies.read().split("\n")

    # Dict to hold titles and similarity scores
    movie_titles = {}
    
    for index, movie in enumerate(movie_descriptions):
        
        # Correcting for blank lines in movies.txt
        if movie.strip() == "":
            movie_descriptions.pop(index)

        # Performing similarity analysis
        else:
            title = movie.split(" :")[0]
            movie_descriptions[index] = movie.split(" :")[1]

            movie_titles[title] = nlp(movie).similarity(nlp(description))

    for title in movie_titles:
        if movie_titles[title] == max(movie_titles.values()):
            return title


description_to_compare = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

recommended = watch_next(description_to_compare)

print(f"The description for '{recommended}' is most similar to the description for 'Planet Hulk'")


'''
I expect that this is outputing Movie C, due to the relatively naive model and method that are being used.
The literal meanings of the words in the description are semantically closest to those in the description
for Planet Hulk - even if the film is of a completely different genre.

That said, if we don't account for genre-weighting, and look solely the thematic similarity in the descriptions of the plot,
perhaps this isn't actualy the poor result it initially appears to be.

Remotes and GitHub have not been covered on the course to date. 
For that reason, I have simply committed this to same repo on GitHub as for Compulsory Task 1.
'''