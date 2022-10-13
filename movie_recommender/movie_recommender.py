# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_movie_recommender.ipynb.

# %% auto 0
__all__ = ['get_movie_recs', 'search_movies_n_recommend']

# %% ../nbs/00_movie_recommender.ipynb 19
def get_movie_recs(full_title):
    "This function will use the `nn.CosineSimilarity` on the 50 latent factors for each movie to find the 30 movies most similar to your favorite movie."
    movie_factors = learn.model.i_weight.weight
    idx = int(titles[titles.title == full_title].midx)
    distances =  nn.CosineSimilarity(dim=1)(movie_factors,movie_factors[idx][None])
    idx = distances.argsort(descending=True)
    return [o for o in titles.title[idx.tolist()][:30]]

# %% ../nbs/00_movie_recommender.ipynb 20
def search_movies_n_recommend(favorite_movie:str # The movie title typed into the `gr.Textbox()` that the user will see on the `gradio` app
                             ):
    "This function returns 30 recommendations using `get_movie_recs` after searching through all movie titles to find any titles that contain the words in the `favorite_movie` variable."
    movies_found = ''
    s = favorite_movie.lower()
    #remove THE from the title
    if s[:4] == 'the ':
        s = s[4:]

    lst = titles['title'].tolist()
    index = []
    i=0
    length = len(lst)
    while i<length:
        if s in lst[i].lower():
            full_title = lst[i]
            movies_found+= str(full_title) +'\n'
#             print(f'Your Favorite Movies:  {full_title}')
        i+=1
    # write explaination in case multiple movies
    explainer = f'If there are multiple movies above: Please paste your favorite movie into the "favorite_movie" box.\n The box below is currently showing recommendations for the movie:  {full_title}'
    #print movies found and explainer
    output_str =  movies_found+'\n\n'+explainer
    
    #get recommendations from model
    recommendations = get_movie_recs(full_title) 
    #create list of all the recommendations to print
    print_lst = ''
    for o in recommendations:    print_lst =print_lst+str(o) + '\n'
    
    
#     return  f'Will Recommend for:  {full_title}', output_str, recomendations
    return output_str, f'Recommendations for {full_title}: \n\n {print_lst}'