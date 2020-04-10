from firebase import firebase

# instancia o database
firebase = firebase.FirebaseApplication("https://paduasplayer.firebaseio.com/", None)

def post(idUser, artista, desc):
    data = {
        'descricao': desc,
        'artista': artista
    }
    response = firebase.patch('/Users/' + idUser + '/Playlist/1', data)
    print(response)


def get(child, id):
    response = firebase.get('/' + child, id)
    print(response)


def put(child, id):
    firebase.put('/' + child, id)
    print('Atualizado')


def delete(child, id):
    firebase.delete('/' + child, id)
    print('Deletado')


def main():
    # post passando (id do usuario + parametros)
    artista = input("Insira nome do artista: ")
    descricao = input("Insira nome da musica: ")
    post("By9bZPdQqrWtAqr2ib4r7q6d32g1", artista, descricao)

    # get passando o caminho das collections + id do usuario + o que querer busar (passando nada ele tras tudo)
    get("Users", "By9bZPdQqrWtAqr2ib4r7q6d32g1", )

    # delete passando id do usuario + atributos
    delete('Users', 'By9bZPdQqrWtAqr2ib4r7q6d32g1')



main()

