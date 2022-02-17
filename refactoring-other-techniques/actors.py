# by Kami Bigdely
# Extract class
first_names = ['elizabeth', 'Jim']
last_names = ['debicki', 'Carrey']
birth_year = [1990, 1962]
movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],\
     ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man']]
emails = ['deb@makeschool.com', 'jim@makeschool.com']

class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email
    
    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def get_movies(self):
        print('Movies: ')
        for i in self.movies:
            print(i)
    
    def email(self):
        print('Send email to:', self.email)

def send_hiring_email(email):
    print("email sent to: ", email)
    
for i, value in enumerate(emails):
    if birth_year[i] > 1985:
        print(first_names[i], last_names[i])
        print('Movies Played: ', end='')
        for m in movies[i]:
            print(m, end=', ')
        print()
        send_hiring_email(value)
