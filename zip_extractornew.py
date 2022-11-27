import json                       ##convert JSON to python objects
import os                         #functions for interacting with the operating system.

from country_converter import convert as iso2_to_3                ##will see later
from geopy.geocoders import Nominatim                              ##will see later
from geopy.extra.rate_limiter import RateLimiter                   ##will see later
from zipfile import ZipFile                                         ##will see later
from shapely.geometry import shape
#
geolocator = Nominatim(user_agent="geoapiExercises", timeout=1000)  #will see later
#
geocode = RateLimiter(geolocator.reverse, min_delay_seconds=0.5)   ##will see later



# os.listdir(r"D:\UOE MODULES PYTHON DIRECTORy_codes")

def dir_list(location_of_dir):               # get the names of files in folder
    return os.listdir(location_of_dir)


def question_1(element):   # element :- a single tweet
    return (element.get('id'), element.get('created_at')) if element.get('id') else None



#
def question_2(element):
    return (element.get('id_str'),(element.get('user').get("id_str")),(element.get('user').get("screen_name"))) if element.get('id_str') else None


def question_23(element):
    return element.get('id_str'), tuple(map(lambda x: (x.get("id")), (element.get("entities").get("user_mentions")))) if element.get('id_str') and element.get("entities").get("user_mentions") else None

# def question_23(element):
#     return element.get('id_str'), if element.get('id_str') and element.get("entities").get("user_mentions") else None


# def question_23(element):
    # return tuple(map(lambda x: (x.get("id_str")), (element.get("entities").get("user_mentions")))) if element.get('id_str') and element.get("entities").get("user_mentions") else None



#None.get("case")
def question_24(element):
    return (element.get('id_str'),(element.get('user').get("id_str")),tuple(map(lambda x: (x.get("id_str")), (element.get("entities").get("user_mentions")))),(element.get('place').get("country_code"))) if element.get('id_str') and element.get('place') else None

        # (element.get('id_str'),(element.get('user').get("id_str")),(element.get('place').get("country_code"))) if element.get('id_str') else None

        # ,tuple(map(lambda x: (x.get("id_str")), (element.get("entities").get("user_mentions")))) if element.get('id_str') and element.get("entities").get("user_mentions") else None

            # , (element.get('place').get("country_code")))
            #

# return tuple(map(lambda x: (x.get("id_str")), (element.get("entities").get("user_mentions")))) if element.get('id_str') and element.get("entities").get("user_mentions") else None
#             , ((element.get('place').get("country_code"))))

# (element.get('id_str'),(element.get('user').get("id_str")),(element.get('user').get("screen_name"))):- it worked
#element.get('id_str'),
# element.get('id_str'),(element.get('user').get("id_str")) :- worked
# element.get('id_str'),(element.get('user').get("id_str")),(element.get('user').get("screen_name")) :- not worked
# element.get('id_str'),(element.get('user').get("id_str")),((element.get('user').get("screen_name"))) :- not worked
# element.get('id_str'),element.get('user').get("id_str"),(element.get('user').get("screen_name"))
# ,(element.get('user').get("screen_name"))
# ,(element.get('user').get("screen_name"))

# ,element.get('user').get("screen_name"),element.get('entities').get("user_mentions").get("id"),element.get('entities').get("user_mentions").get("name") if element.get('id') else None

# def question_2(element):
#     return element.get('id'), (element.get('user').get("id")), (element.get("entities").get("user_mentions").get("id")) if element.get('id') else None

#"user_mentions": [{"id": 19019465, "indices"
#"id": 1531772510450208769,
# "user": {"id": 127625257,

def question_3(element):
    if element.get('id') and element.get('coordinates'):    #
        long, lat = element.get('coordinates').get('coordinates')
        return lat, long



def question_3_3(element):    #important for ques 3.3
    if element.get('id') and (place:=element.get('place')):
        return element.get('id'), shape(place.get('bounding_box'))






def question_4(element):
    return (element.get('id_str'),element.get("timestamp_ms") , (element.get('place').get("country_code"))) if  element.get('id_str') else None




def question_42(element):
    return (element.get('id_str'), (element.get("created_at")), (element.get("text")),(element.get('place').get("country_code")))  if element.get('id_str') and element.get('place') else None



# (element.get('id_str'),(element.get('user').get("id_str")),(element.get('user').get("screen_name"))):- it worked
# element.get('id_str'),(element.get('user').get("id_str")) :- worked

def zip_tweet_operator(zip_f, dir_path=r"D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data", json_get= question_1):
    # TODO: change the function to suit your needs

    """
    This function reads a json file form a zip folder, gets the value and returns the value
    :param json_get: function for the values to return
    :param zip_f: path of zip folder
    :param dir_path: the name of the directory containing zip folder
    """
    with ZipFile(f'{dir_path}/{zip_f}', 'r') as zip_folder:
        with zip_folder.open(zip_folder.namelist()[0], ) as json_file_obj:
            return tuple(map(json_get, map(json.loads, json_file_obj)))


def ques_op2(x):
    return zip_tweet_operator(x,json_get=question_2)

def ques_op23(x):
    return zip_tweet_operator(x,json_get=question_23)

def ques_op24(x):
    return zip_tweet_operator(x,json_get=question_24)

def ques_op3(x):
    return zip_tweet_operator(x, json_get=question_3)


# def ques_op4(x):
#     return zip_tweet_operator(x, json_get=question_4)


#
#
def con_iso2(point):
    return iso2_to_3(geocode(f'{point[0]},{point[1]}').raw.get('address').get('country_code'))


def ques_op3_3(x):
    return zip_tweet_operator(x, json_get=question_3_3)


def ques_op4_4(x):
    return zip_tweet_operator(x, json_get=question_42)





def zip_tweet_operator1(zip_f, dir_path=r"D:\UOE MODULES PYTHON DIRECTORy_codes\IDS\assignment\twitter_data", json_get= question_4):
    # TODO: change the function to suit your needs

    """
    This function reads a json file form a zip folder, gets the value and returns the value
    :param json_get: function for the values to return
    :param zip_f: path of zip folder
    :param dir_path: the name of the directory containing zip folder
    """
    with ZipFile(f'{dir_path}/{zip_f}', 'r') as zip_folder:
        with zip_folder.open(zip_folder.namelist()[0], ) as json_file_obj:
            return tuple(map(json_get, map(json.loads, json_file_obj)))
