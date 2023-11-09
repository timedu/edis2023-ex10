
from functools import reduce

def map_reduce(conf):
    
    inputs, reducer = conf['inputs'], conf['reducer']


    # for record in inputs[0]['data'][:5]: print(record)
    # --------------------------------------------------
    # {'id': 0, 'name': 'Black comedy'}
    # {'id': 1, 'name': 'Computer Animation'}
    # {'id': 2, 'name': 'Epic film'}
    # {'id': 3, 'name': 'Documentary film'}
    # {'id': 4, 'name': 'Art film'}

    # for record in inputs[1]['data'][:5]: print(record)
    # --------------------------------------------------
    # {'id': 0, 'name': '.45', 'directed_by': 'Gary Lennon', 'initial_release_date': '2006-11-30', 'genre_id': 0}
    # {'id': 1, 'name': '9', 'directed_by': 'Shane Acker', 'initial_release_date': '2005-04-21', 'genre_id': 1}
    # {'id': 2, 'name': '300', 'directed_by': 'Zack Snyder', 'initial_release_date': '2006-12-09', 'genre_id': 2}
    # {'id': 3, 'name': '¿Quién es el señor López?', 'directed_by': 'Luis Mandoki', 'genre_id': 3}
    # {'id': 4, 'name': '15 Park Avenue', 'directed_by': 'Aparna Sen', 'initial_release_date': '2005-10-27', 'genre_id': 4}

    # return


    # --
    # MAP inputs by their mapper
    #

    key_value_pair_arrays = []
    for input_data in inputs:
        key_value_pair_arrays.append( list(map(input_data['mapper'], input_data['data'])))


    # for record in key_value_pair_arrays[0][:5]: print(record)
    # ---------------------------------------------------------
    # {'key': 0, 'value': 'Black comedy'}
    # {'key': 1, 'value': 'Computer Animation'}
    # {'key': 2, 'value': 'Epic film'}
    # {'key': 3, 'value': 'Documentary film'}
    # {'key': 4, 'value': 'Art film'}

    # for record in key_value_pair_arrays[1][:5]: print(record)
    # ---------------------------------------------------------
    # {'key': 0, 'value': {'id': 0, 'name': '.45'}}
    # {'key': 1, 'value': {'id': 1, 'name': '9'}}
    # {'key': 2, 'value': {'id': 2, 'name': '300'}}
    # {'key': 3, 'value': {'id': 3, 'name': '¿Quién es el señor López?'}}
    # {'key': 4, 'value': {'id': 4, 'name': '15 Park Avenue'}}

    # return


    # --
    # Sort mapped inputs
    #

    for arr in key_value_pair_arrays:
        arr.sort(key=lambda x: x['key'])


    # for record in key_value_pair_arrays[0][:5]: print(record)
    # ---------------------------------------------------------
    # {'key': 0, 'value': 'Black comedy'}
    # {'key': 1, 'value': 'Computer Animation'}
    # {'key': 2, 'value': 'Epic film'}
    # {'key': 3, 'value': 'Documentary film'}
    # {'key': 4, 'value': 'Art film'}

    # for record in key_value_pair_arrays[1][:5]: print(record)
    # ---------------------------------------------------------
    # {'key': 0, 'value': {'id': 0, 'name': '.45'}}
    # {'key': 0, 'value': {'id': 26, 'name': 'About Schmidt'}}
    # {'key': 0, 'value': {'id': 52, 'name': 'American Cowslip'}}
    # {'key': 0, 'value': {'id': 56, 'name': 'American Psycho'}}
    # {'key': 0, 'value': {'id': 69, 'name': 'Anger Management'}}

    # return


    # --
    # Group values
    #

    key_values_array = []
    index1_start = 0

    for pair0 in key_value_pair_arrays[0]:

        key_values_array.append({
            'key': pair0['key'],
            'values': [pair0['value']]
        })

        for i in range(index1_start, len(key_value_pair_arrays[1])):
            pair1 = key_value_pair_arrays[1][i]
            if pair0['key'] != pair1['key']:
                index1_start = i
                break
            key_values_array[-1]['values'].append(pair1['value'])


    # for record in key_values_array[:5]: 
    #     print(f'key: {record["key"]}, number of values: {len(record["values"])}')
    #     for value in record['values'][:3]: print(f'- {value}')
    #     if len(record["values"]) > 3: print('- ...')

    # key: 0, number of values: 18
    # - Black comedy
    # - {'id': 0, 'name': '.45'}
    # - {'id': 26, 'name': 'About Schmidt'}
    # - ...
    # key: 1, number of values: 5
    # - Computer Animation
    # - {'id': 1, 'name': '9'}
    # - {'id': 237, 'name': 'Digital Monster X-Evolution'}
    # - ...
    # key: 2, number of values: 2
    # - Epic film
    # - {'id': 2, 'name': '300'}
    # key: 3, number of values: 58
    # - Documentary film
    # - {'id': 3, 'name': '¿Quién es el señor López?'}
    # - {'id': 8, 'name': '50 Cent: The New Breed'}
    # - ...
    # key: 4, number of values: 3
    # - Art film
    # - {'id': 4, 'name': '15 Park Avenue'}
    # - {'id': 84, 'name': 'Astitva'}

    # return


    # --
    # REDUCE results by reducer
    #

    key_result_array = []

    for pair in key_values_array:
        key, values = pair['key'], pair['values']
        key_result_array.append({
            'key': key,
            'result': reduce(reducer, values, [])
        })


    # for record in key_result_array[:5]: 
    #     print(f'key: {record["key"]}, number of records: {len(record["result"])}')
    #     for value in record['result'][:3]: print(f'- {value}')
    #     if len(record["result"]) > 3: print('- ...')

    # key: 0, number of records: 17
    # - {'id': 0, 'name': '.45', 'genre': 'Black comedy'}
    # - {'id': 26, 'name': 'About Schmidt', 'genre': 'Black comedy'}
    # - {'id': 52, 'name': 'American Cowslip', 'genre': 'Black comedy'}
    # - ...
    # key: 1, number of records: 4
    # - {'id': 1, 'name': '9', 'genre': 'Computer Animation'}
    # - {'id': 237, 'name': 'Digital Monster X-Evolution', 'genre': 'Computer Animation'}
    # - {'id': 240, 'name': 'Dinosaur', 'genre': 'Computer Animation'}
    # - ...
    # key: 2, number of records: 1
    # - {'id': 2, 'name': '300', 'genre': 'Epic film'}
    # key: 3, number of records: 57
    # - {'id': 3, 'name': '¿Quién es el señor López?', 'genre': 'Documentary film'}
    # - {'id': 8, 'name': '50 Cent: The New Breed', 'genre': 'Documentary film'}
    # - {'id': 16, 'name': 'A League of Ordinary Gentlemen', 'genre': 'Documentary film'}
    # - ...
    # key: 4, number of records: 2
    # - {'id': 4, 'name': '15 Park Avenue', 'genre': 'Art film'}
    # - {'id': 84, 'name': 'Astitva', 'genre': 'Art film'}

    return key_result_array
