# Simple program that recommend movies and possiblilty to rate movies
import tkinter as tk
from tmdbv3api import TMDb, Movie
from tkinter import messagebox

tmdb = TMDb()
tmdb.api_key = '1d871c9485836112e3eeca2f25fbded4'

def rate_movie(title, rating_entry):
    rating = rating_entry.get()
    if rating.isdigit() and 0 <= int(rating) <= 10:
        # Code to submit the rating can be added here
        messagebox.showinfo("Rate Movie", f"Rated movie {title} as {rating}.")
    else:
        messagebox.showerror("Error", "Please enter a valid rating between 0 and 10.")


def get_recommendations():
    movie_name = movie_entry.get()    
    movie = Movie()

    search_result = movie.search(movie_name)
    if search_result:
        first_movie_id = search_result[0].id
        recommendations = movie.recommendations(first_movie_id)       
        for i, recommendation in enumerate(recommendations) :
                      
            if  i < 5:
        
                recommendation_label = tk.Label(root, text=f"{i+1}. {recommendation.title} Release date: {recommendation.release_date} ", font=("Helvetica", 10, "bold"))                
                recommendation_label.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)

                rating_entry = tk.Entry(root, width=10, font=("Helvetica", 10))                
                rating_entry.grid(row=i+1, column=1, padx=10, pady=5)

                rate_button = tk.Button(root, text="Rate", font=("Helvetica", 10, "bold"), command=lambda title=recommendation.title, entry=rating_entry: rate_movie(title, entry))                
                rate_button.grid(row=i+1, column=2, padx=10, pady=5)

            

root = tk.Tk()
root.title("Movie Recommendation")
root.geometry("500x500")
root.configure(bg="lightblue")

movie_label = tk.Label(root, text="Enter a movie name:" , font=("Helvetica", 12) )
movie_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

movie_entry = tk.Entry(root , width=30, font=("Helvetica", 12))
movie_entry.grid(row=0, column=1, padx=10, pady=5)

recommend_button = tk.Button(root, font=("Helvetica", 12, "bold"), text="Get Recommendations", command=get_recommendations)
recommend_button.grid(row=0, column=2, padx=10, pady=5)

root.mainloop()
