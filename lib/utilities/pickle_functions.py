import os
import pickle
import sys
sys.path.append('lib\\models')
from user_model import User


class PickleFunctions : 
    def __init__(self) -> None:
        pass

    def storeUser(user: User.UserModel):
        with open('example.pickle', 'wb') as f:
            pickle.dump(user, f)




print(os.getcwd())


