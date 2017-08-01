import JsonLoader
import DictForJson


def main():
    private_list_group = DictForJson.get_private_list_group()
    dict_of_private_groups = DictForJson.get_dict_of_private_groups(private_list_group)

    JsonLoader.create_json_file(dict_of_private_groups)
    #Для проверки!
    JsonLoader.load_json_file('groups.txt')


if __name__ == '__main__':
    main()
