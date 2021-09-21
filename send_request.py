import requests

GET_TOKEN_URIL = 'https://login.microsoftonline.com/bbd362fc-c32f-4307-8cbc-c7afa65351a8/oauth2/v2.0/token'
CLIENT_ID_KEY = 'client_id'
CLIENT_ID_VALUE = '7c6888db-88af-42c6-924a-8fda7356ec43'
CLIENT_SECRET_KEY = 'client_secret'
CLIENT_SECRET_VALUE = '9G67Q~DePOXtPubk0v6eUaBfsXmXkWV0qjrwF'
SCOPE_KEY = 'scope'
SCOPE_VALUE = 'api://548590dc-da93-46d7-ae0a-9ada58c0ff7c/.default'
GRANT_TYPE_KEY = 'grant_type'
GRANT_TYPE_VALUE = 'client_credentials'


def get_token():

    payload = {
        CLIENT_ID_KEY: CLIENT_ID_VALUE,
        CLIENT_SECRET_KEY: CLIENT_SECRET_VALUE,
        SCOPE_KEY: SCOPE_VALUE,
        GRANT_TYPE_KEY: GRANT_TYPE_VALUE
    }
    response = requests.post(GET_TOKEN_URIL, json=payload).json()

    return response.access_token

token = get_token()

'''def get_items_lists() -> list:
        cards = requests.get(
            TrelloApi.URL_GET_CARDS, params=TrelloApi.PARAMS_GET_CARDS).json()
        lists = TrelloApi.get_lists()
        items = join_lists_of_dicts(cards, lists, FieldNames.LIST_ID)
        return items
        '''
