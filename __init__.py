import pyrebase
from getpass import getpass
from firebase import firebase

# inicializando firebase
firebaseConfig = {
        "apiKey": "AIzaSyC3PdwUqSBKAA6Wsq3oS4J01ny01ANmRrQ",
        "authDomain": "paduasplayer.firebaseapp.com",
        "databaseURL": "https://paduasplayer.firebaseio.com",
        "projectId": "paduasplayer",
        "storageBucket": "paduasplayer.appspot.com",
        "messagingSenderId": "588241417634",
        "appId": "1:588241417634:web:1e3114f5330869aeb42efb"
    }
firebaseAuth = pyrebase.initialize_app(firebaseConfig)
auth = firebaseAuth.auth()

firebaseDatabase = firebase.FirebaseApplication("https://paduasplayer.firebaseio.com/", None)

def createUser(email, password):
    user = auth.create_user_with_email_and_password(email, password)
    uid = auth.refresh(user['refreshToken'])
    firebaseDatabase.patch('Users/' + uid['userId'], {
        'id': uid['userId'] ,
        'email': email
    })

    print(uid['userId'])
    print("Criado com sucesso...")


def loginUser(email, password):
    login = auth.sign_in_with_email_and_password(email, password)
    uid = auth.refresh(login['refreshToken'])
    print("Logado com sucesso: " + uid['userId'])


def main():
    email = input("Insira seu email: ")
    password = getpass("Insira sua senha: ")

    createUser(email, password)


main()



# # enviar email de confirmacao
# auth.send_email_verification(login['idToken'])
#
# # enviar email de recuperacao de senha
# auth.send_password_reset_email(email)

