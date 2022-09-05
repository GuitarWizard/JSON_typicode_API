import requests
import json

# API Interaction
# Using http://jsonplaceholder.typicode.com, write a script to get the most recent N number of
# TODOs, where N may be any number. The script must also be able to create a TODO and delete
# a TODO given an ID.


# Per the API's direction, the API does not actually modifiy data (http://jsonplaceholder.typicode.com/guide/)
# Additionally it was run off my github account per instructions here:
# https://my-json-server.typicode.com/

ENDPOINT = "https://my-json-server.typicode.com/GuitarWizard/json_demo/posts"


def get_data():
    """Retrieves the data from the API at the designated endpoint"""
    todo_response = requests.get(url=ENDPOINT)
    todo_response.raise_for_status()

    todo = todo_response.json()
    print(todo)

    return todo


def identify_most_recent_todo(data_input):
    """Identifies the most recent todo posting in retrieved data
    Returns a value for the next post ID by adding 1 to the maximum value
        inputs:
    data_input | the JSON data from the get_data function"""
    # print(len(data_input))
    length = len(data_input)
    id_list = []
    for n in range(0, length):
        id_list.append(data_input[n]["id"])

    next_post = (max(id_list)) + 1

    return next_post


def identify_oldest_todo(data_input):
    """Identifies the oldest  todo posting in retrieved data
        Returns a value for the oldest post ID by finding the minimum value
            inputs:
        data_input | the JSON data from the get_data function"""
    print(len(data_input))
    length = len(data_input)
    id_list = []
    for n in range(0, length):
        id_list.append(data_input[n]["id"])

    oldest_post = min(id_list)
    print(f"Oldest post: {oldest_post}")
    return oldest_post


def post_data(post_id):
    """Adds user defined data into the JSON file at the specified endpoint.
    id | the id tag of the input data
    title | the description of the post. Must be a string"""
    parameters = {
        "id": post_id,
        "title": "Post 4"
    }

    post_response = requests.post(url=ENDPOINT, json=parameters)
    post_response.raise_for_status()
    print(post_response)
    print(post_response.text)


def delete_data(outdated_post):
    """Deletes a line of data in the API database"""
    # parameters = {
    #     "id": outdated_post
    #     }
    delete_response = requests.delete(url=ENDPOINT + f"/{outdated_post}")
    delete_response.raise_for_status()
    print("delete successful")
    print(ENDPOINT + f"/{outdated_post}")


# PROCEDURAL EXECUTIONS-------------

# Collect the API data
data_retrieved = get_data()

# identify the next post id
next_id = identify_most_recent_todo(data_input=data_retrieved)
post_data(post_id=next_id)

# Identify the oldest post and delete it
old_post = identify_oldest_todo(data_input=data_retrieved)
delete_data(outdated_post=old_post)
