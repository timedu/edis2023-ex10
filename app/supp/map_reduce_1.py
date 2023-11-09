
from functools import reduce

def map_reduce(conf):

    input_data = conf['input']
    mapper = conf['mapper']
    reducer = conf['reducer']


    # for record in input_data[:10]: print(record)
    # --------------------------------------------
    # {'name': '.45', 'genre': 'Black comedy', 'directed_by': 'Gary Lennon', 'initial_release_date': '2006-11-30'}
    # {'name': '9', 'genre': 'Computer Animation', 'directed_by': 'Shane Acker', 'initial_release_date': '2005-04-21'}
    # {'name': '300', 'genre': 'Epic film', 'directed_by': 'Zack Snyder', 'initial_release_date': '2006-12-09'}
    # {'name': '¿Quién es el señor López?', 'genre': 'Documentary film', 'directed_by': 'Luis Mandoki'}
    # {'name': '15 Park Avenue', 'genre': 'Art film', 'directed_by': 'Aparna Sen', 'initial_release_date': '2005-10-27'}
    # {'name': '7G Rainbow Colony', 'genre': 'Drama', 'directed_by': 'Selvaraghavan', 'initial_release_date': '2004-10-15'}
    # {'name': '3-Iron', 'genre': 'Crime Fiction', 'directed_by': 'Kim Ki-duk', 'initial_release_date': '2004-09-07'}
    # {'name': '10.5: Apocalypse', 'genre': 'Disaster Film', 'directed_by': 'John Lafia', 'initial_release_date': '2006-03-18'}
    # {'name': '50 Cent: The New Breed', 'genre': 'Documentary film', 'directed_by': 'Don Robinson', 'initial_release_date': '2003-04-15'}
    # {'name': '24 Hour Party People', 'genre': 'Biographical film', 'directed_by': 'Michael Winterbottom', 'initial_release_date': '2002-02-13'}

    # return


    # --
    # 1. MAP input by mapper
    #

    key_value_pair_list = list(map(mapper, input_data))


    # for record in key_value_pair_list[:10]: print(record)
    # -----------------------------------------------------
    # {'key': 'Black comedy'}
    # {'key': 'Computer Animation'}
    # {'key': 'Epic film'}
    # {'key': 'Documentary film'}
    # {'key': 'Art film'}
    # {'key': 'Drama'}
    # {'key': 'Crime Fiction'}
    # {'key': 'Disaster Film'}
    # {'key': 'Documentary film'}
    # {'key': 'Biographical film'}

    # return


    # --
    # 2. Sort mapped input
    #
    
    key_value_pair_list.sort(key=lambda pair: pair['key'])


    # for record in key_value_pair_list[:10]: print(record)
    # -----------------------------------------------------
    # {'key': 'Absurdism'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}
    # {'key': 'Action Film'}

    # return


    # --
    # 3. Group values
    #

    key_values_array = []
    current_key = None
    current_values = []

    for pair in key_value_pair_list:
        key, value = pair['key'], pair.get('value')
        if key != current_key:
            if current_key is not None:
                key_values_array.append({'key': current_key, 'values': current_values})
            current_key = key
            current_values = [value]
        else:
            current_values.append(value)

    if current_key is not None:
        key_values_array.append({'key': current_key, 'values': current_values})


    # for record in key_values_array[:5]: print(record)
    # -------------------------------------------------
    # {'key': 'Absurdism', 'values': [None]}
    # {'key': 'Action Film', 'values': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]}
    # {'key': 'Action/Adventure', 'values': [None]}
    # {'key': 'Adventure Film', 'values': [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]}
    # {'key': 'Airplanes and airports', 'values': [None, None]}

    # return


    # --
    # 4. REDUCE results by reducer
    #

    key_result_array = []

    for key_value_pair in key_values_array:

        key, values = key_value_pair['key'], key_value_pair['values']
        result = reduce(reducer, values, 0)
        key_result_array.append({'key': key, 'result': result})


    # for record in key_result_array[:5]: print(record)
    # -------------------------------------------------
    # {'key': 'Absurdism', 'result': 1}
    # {'key': 'Action Film', 'result': 53}
    # {'key': 'Action/Adventure', 'result': 1}
    # {'key': 'Adventure Film', 'result': 19}
    # {'key': 'Airplanes and airports', 'result': 2}


    return key_result_array
