from api import app, mongo
from api.models.Model import UsuarioModel
from api.services.Services import UsuarioService

if __name__ == '__main__':
    with app.app_context():
        if 'usuarios' not in mongo.db.list_collection_names():
            usuario = UsuarioModel(
                nome= '',
                email= '',
            )
            
            UsuarioService.save(usuario)
    app.run(port=5000, debug=True)