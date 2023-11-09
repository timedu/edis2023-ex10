
import traceback
import subprocess
from os.path import  dirname, realpath, join
from os import environ
import json

try:
    import readline
except:
    pass 

from supp.config import todo, set_config
from supp.map_reduce_1 import map_reduce as map_reduce_1
from supp.map_reduce_2 import map_reduce as map_reduce_2

# --
# load files to be used
#

with open('/home/app/data/films-joined.json', 'r') as file:
    films_joined = json.load(file)

with open('/home/app/data/films.json', 'r') as file:
    films = json.load(file)

with open('/home/app/data/genres.json', 'r') as file:
    genres = json.load(file)

# --
# run repl
#

def repl():

    while True:

        try:
            user_input = input(todo['prompt'])

        except EOFError:
            print('')
            break        

        if not user_input.strip():
            continue

        input_strings = user_input.lower().split()

        command = input_strings[0]

        try:

            if len(input_strings) == 1:

                if command in ('exit', 'quit'):
                    break

                # --
                # sort merge join
                #     

                if command == 'smj':

                    map_reduce_result = map_reduce_2({
                        'inputs': [
                            { 'data': genres, 'mapper': todo['sort_merge_join'].genre_mapper },
                            { 'data': films,  'mapper': todo['sort_merge_join'].film_mapper }
                        ],
                        'reducer': todo['sort_merge_join'].reducer
                    })

                    result = todo['sort_merge_join'].finalizer(map_reduce_result)
                    for record in result[:10]: print(record)

                    continue

            if len(input_strings) == 2:

                if command == 'tg':

                    param = input_strings[1]

                    # --
                    # top genres using unix pipeline
                    #

                    if param == 'sh':

                        top_genres_env = environ

                        top_genres_env['FILMS_JOINED'] = \
                            '/home/app/data/films-joined.json'
                        top_genres_env['TODO_SORT'] = \
                            f'/home/app/todos/{todo["folder"]}/todo_sort.py'

                        top_genres = join(
                            dirname(realpath(__file__)), 
                            'todos',
                            todo['folder'],
                            'todo_top_genres.sh'
                        )

                        subprocess.run(
                            ['bash', top_genres],
                            env = top_genres_env
                        )

                        continue

                    # --
                    # top genres using python and map-reduce
                    #

                    if param == 'py':

                        map_reduce_result = map_reduce_1({
                            'input': films_joined,
                            'mapper':  todo['top_genres'].mapper,
                            'reducer': todo['top_genres'].reducer,
                        })

                        result = todo['top_genres'].finalizer(map_reduce_result)
                        for record in result[:5]: print(record)

                        continue

            raise AssertionError

        except AssertionError:
            print('Usage: { tg {sh|py} | smj | exit | quit }')

        except Exception as err:
            print(err)
            traceback.print_exc()

if __name__ == '__main__':

    set_config()
    repl()
