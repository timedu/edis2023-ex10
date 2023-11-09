
from argparse import ArgumentParser

todo = {}


def _get_arguments():

    parser = ArgumentParser(
        description='Assignment 9'
    )
    parser.add_argument(
        '-r', '--review', choices=['0', '1', '2'], default='0',
        help='whose code is being run, default: 0 (your code)'
    ) 
    return vars(parser.parse_args())



def _get_todo_folder(args):
    
    return 'your_code' if not int(args.get('review')) else f'review_{args["review"]}'     



def set_config():

    args = _get_arguments()

    if args['review'] == '1':
         from todos.review_1 import todo_top_genres
         from todos.review_1 import todo_sort_merge_join

    elif args['review'] == '2':
         from todos.review_2 import todo_top_genres
         from todos.review_2 import todo_sort_merge_join

    else:
         from todos.your_code import todo_top_genres
         from todos.your_code import todo_sort_merge_join

    todo['top_genres'] = todo_top_genres  
    todo['sort_merge_join'] = todo_sort_merge_join  
    todo['folder'] = _get_todo_folder(args)
    todo['prompt'] = f'ex10 [{todo["folder"]}] > '
