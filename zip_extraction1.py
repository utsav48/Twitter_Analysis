import json    #Python has a built-in package called json, which can be used to work with JSON data.
import os
from zipfile import ZipFile


def dir_list(path):   #: str):           # get the names of files in folder
    return os.listdir(path)              #os.listdir :- it will names of the files inside twitter folder path (os.listdir)

x = dir_list(r"D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data")
print(dir_list(r"D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data"))
print(len(x))


def zip_extraction1(zip_filename, dir_path= r"D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data"):  #
    with ZipFile(f'{dir_path}/{zip_filename}', 'r') as zip_folder:  #dir_path:- D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data  #zip_filename:- geoEurope_2022060100.zip  #returns obj which is zip folder  (each obj for eaach zip file going on by one)
        with zip_folder.open(zip_folder.namelist()[0]) as json_file_obj:    #first zip file and opening first zip folder and then naming on 1st json so [0] there is one file in the list
            # user_id = None  # initialize user
            twitter_id = []

            while tweet_as_str := json_file_obj.readline():   #assignment expression :=  ability to assign value where number assignment can

                tweet_dict = json.loads(tweet_as_str) #loads the string

                try:

                    #user_date = (tweet_dict.get('user').get('id'))
                    twitter_id.append((tweet_dict.get("id"), tweet_dict.get("created_at"), tweet_dict.get("text"),(tweet_dict.get('place').get("country_code"))))
                    #twitter_id.append(( tweet_dict.get("id"),tweet_dict.get("created_at"),(tweet_dict.get('place').get("country_code"))))  #, (tweet_dict.get("user").get("id")))) #, tweet_dict.get('user').get('id') ))
                    # twitter_id.append((tweet_dict.get("entities").get("user_mentions")))

                except AttributeError:
                    twitter_id.append(None)

            return twitter_id







print(zip_extraction1("geoEurope_2022060100.zip"))
print(len(zip_extraction1("geoEurope_2022060100.zip")))   #12156
print(dir_list(r"D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data"))









    # ## TODO: change the function to suit your needs
    # """
    # Above function reads a json file form a zip folder, gets the value and returns the value
    # :param zip_name: path of zip folder
    # :param dir_path: the name of the directory containing zip folder
    # :return: tweet user id
    # """

