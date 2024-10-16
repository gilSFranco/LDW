from api import app, mongo
from api.models.Model import Fazendeiro
from api.services.Services import FazendeiroService

if __name__ == '__main__':
    with app.app_context():
        if 'fazendeiros' not in mongo.db.list_collection_names():
            fazendeiro = Fazendeiro(
                nome= '',
                idade= 0,
                endereco= '',
                telefone= ''
            )
            
            FazendeiroService.save(fazendeiro)
    
    app.run(port=5000, debug=True)