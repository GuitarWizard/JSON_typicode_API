# JSON_typicode_API

Challenge:
Using http://jsonplaceholder.typicode.com, write a script to get the most recent N number of
TODOs, where N may be any number. The script must also be able to create a TODO and delete
a TODO given an ID.


The python file interacts with jsonplaceholder.typicode.com using a resository forked into my own github account
(located here: https://github.com/GuitarWizard/json_demo)

The different portions of the challenge are split into different functions.
get_data pulls the json data from the specified endpoint (https://my-json-server.typicode.com/GuitarWizard/json_demo/posts)

identify_most_recent_todo returns determines what the highest value is in the API, and establishes that the next post id shall be {highest_post_id} + 1, to ensure that there is no duplicate values posted when the function post_data is executed

Similarly, identify_oldest_todo determines the oldest value, by way of finding the minimul post id in the api, and sends this to the function delete_data to be removed
