import base64
import os
import pickle

class User :

    class UserModel :
        def __init__(self, username, password) -> None:
            self.username = username
            self.password = password
            convertToken = base64.b64encode(f'{username}:{password}'.encode()).decode('ascii')
            self.token = convertToken


    def storeUser(user: UserModel, credentialFolder) -> None:
        if not os.path.exists(f'{credentialFolder}'):
            os.mkdir(f'{credentialFolder}')
        with open(f'{credentialFolder}\\credentials.pickle', 'wb') as f:
            pickle.dump(user, f)
            print("usuário armazenado")

    def getUser(credentialFolder) -> UserModel :
        if os.path.exists(f'{credentialFolder}\\credentials.pickle'):
            with open(f'{credentialFolder}\\credentials.pickle', 'rb') as f:
                currentUser = pickle.load(f)
                print("usuário requisitado")
        else :
            currentUser = User.UserModel("","")   
        print(f'{currentUser.username} {currentUser.password} {currentUser.token}')
        return currentUser

