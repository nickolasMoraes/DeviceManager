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


    def storeUser(user: UserModel) -> None:
        with open('credentials.pickle', 'wb') as f:
            pickle.dump(user, f)
            print("usuário armazenado")

    def getUser() -> UserModel :
        if(os.path.exists("credentials.pickle")) :
            with open('credentials.pickle', 'rb') as f:
                currentUser = pickle.load(f)
                print("usuário requisitado")
        else :
            currentUser = User.UserModel("","")
        

        
        return currentUser

