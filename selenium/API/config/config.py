import os 

class Config():
    # BASE_URL = 'https://reqres.in' hardcode
    BASE_URL = os.getenv("TESTS_BASE_URL") 

    # prod-https://reqres.in
    # qa -https://qa.reqres.in
    # dev -https://dev.reqres.in 