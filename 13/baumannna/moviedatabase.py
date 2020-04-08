from collections import defaultdict, namedtuple, Counter
import csv
from urllib.request import urlretrieve

MOVIE_DATA = 'movie_metadata.csv'
NUM_TOP_DIRECTORS = 20
MIN_MOVIES = 4
MIN_YEAR = 1960

movie_data = 'https://raw.githubusercontent.com/pybites/challenges/solutions/13/movie_metadata.csv'
movies_csv = 'movies.csv'
urlretrieve(movie_data, movies_csv)

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director(data=movies_csv):
    '''Extracts all movies from csv and stores them in a dictionary
    where keys are directors, and values is a list of movies (named tuples)'''
    directors = defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:
                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue
            if year >= MIN_YEAR:
                m = Movie(title=movie, year=year, score=score)
                directors[director].append(m)

    return directors


def get_average_scores(directors):
    '''Filter directors with < MIN_MOVIES and calculate averge score'''
    cnt = Counter()
    del_lst = []
    for director, movies in directors.items():
        cnt[director] += len(movies)
        if cnt[director] < MIN_MOVIES:
            del_lst.append(director)

    for item in del_lst:
        del directors[item]


    score_average = {}
    for director, movies in directors.items():
        score_average[director] = _calc_mean(movies)

    score_average_sorted = sorted(score_average.items(), key=lambda x: x[1], reverse=True)
    return score_average_sorted


def _calc_mean(movies):
    total_score = 0
    '''Helper method to calculate mean of list of Movie namedtuples'''
    for movie in movies:
        total_score += movie.score
        avg_score = round(total_score / len(movies), 1)
    return avg_score


def print_results(directors, avg_score):
    '''Print directors ordered by highest average rating. For each director
    print his/her movies also ordered by highest rated movie.
    See http://pybit.es/codechallenge13.html for example output'''
    counter = 1
    for director_name in avg_score:
        print(f'{counter}. {director_name[0]:<52} {director_name[1]:.1f}')
        print(f'-' * 60)

        for director, movies in directors.items():
            if director_name[0] == director:
                for movie in movies:
                    print(f'{movie.year}] {movie.title:<50} {movie.score}')
        print(" ")
        counter += 1


def main():
    '''This is a template, feel free to structure your code differently.
    We wrote some tests based on our solution: test_directors.py'''
    directors = get_movies_by_director()
    avg_score = get_average_scores(directors)
    print_results(directors, avg_score)


if __name__ == '__main__':
    main()

