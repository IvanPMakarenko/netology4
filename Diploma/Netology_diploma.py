import func_get_json
import func_get_dict_for_json


if __name__ == '__main__':
    private_list_group = func_get_dict_for_json.get_private_list_group()
    dict_of_private_groups = func_get_dict_for_json.get_dict_of_private_groups(private_list_group)

    func_get_json.create_json_file(dict_of_private_groups)
    #Для проверки!
    func_get_json.load_json_file('groups.txt')
