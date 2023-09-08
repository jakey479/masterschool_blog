from datetime import datetime


def return_timestamp():
    current_datetime = datetime.now()
    # Format the datetime as a string without seconds
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M")
    return formatted_datetime


def return_dictionary_from_list_if_value_present(value_to_check, list_of_dicts: list[dict]) -> dict:
    for index, dictionary in enumerate(list_of_dicts):
        for key, value in dictionary.items():
            if value == value_to_check:
                dict_to_return = list_of_dicts[index]
                return dict_to_return
