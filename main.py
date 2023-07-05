import requests
import datetime as dt

### Create pixela user by post req 

pixela_end_point = 'https://pixe.la/v1/users'

# Token must be at least 8 at most 128 characters
TOKEN="create-your-token"
USERNAME="choose-your-username"

user_params={
    "token" : TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#### CREATE POST REQ TO REGISTER USER 
#POST
# After run 1 time succesfully then comment out; we can register only once 
# post_req = requests.post(url=pixela_end_point,json=user_params)
# print(post_req.text)

### Create Pixela graph for an habit using Post req
graph_end_point = f"https://pixe.la/v1/users/{USERNAME}/graphs"

GRAPH_ID = "graphofhabit1"

graph_params = {
    "id": GRAPH_ID,
    "name":"coding",
    "unit":"commit",
    "type":"int",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
    }

## Create post request to create graph 
# graph_req = requests.post(url=graph_end_point, json=graph_params, headers=headers)
# print(graph_req.text)

#Get today 
now = dt.datetime.now()
today = now.date()
today = today.strftime("%Y%m%d")

# Post value to the graph
value_end_point = f"{pixela_end_point}/{USERNAME}/graphs/{GRAPH_ID}"

value_params = {
    "date":today,
    "quantity":"6"
}

# post_value_req = requests.post(url=value_end_point, headers=headers, json=value_params)
# print(post_value_req.text) 

# PUT
# We did another commits today, so update pixel value for the habit

update_end_point = f"{value_end_point}/{today}"

update_params = {
    "quantity":"16"
}

# update_req = requests.put(url=update_end_point, headers=headers, json=update_params)
# print(update_req.text)

# DELETE 

# delete_req = requests.delete(url=update_end_point, headers=headers)
# print(delete_req.text)