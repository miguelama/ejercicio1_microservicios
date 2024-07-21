from ninja import NinjaAPI
from api_usuarios.usuarios.models import Usuario
from api_usuarios.usuarios.schemas import UsuarioSchema

api = NinjaAPI()

@api.post('/usuarios/')
def list_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios


@api.put('/usuarios/{usuario_id}')
def update_usuario(usuario_id: int, payload: UsuarioSchema):
    usuario = Usuario.objects.filter(id=usuario_id).update(**payload.dict())
    return usuario


@api.delete('/usuarios/{usuario_id}')
def delete_usuario(usuario_id: int):
    usuario = Usuario.objects.filter(id=usuario_id).delete()
    return {'success': usuario}
