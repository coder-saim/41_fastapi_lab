from fastapi import APIRouter 
from bson import ObjectId
from models.user import User
from schemas.schema import individual_seriallizer_user, list_seriallizer_user
from config.database import user_collectoin



router = APIRouter(tags=["User API"])

@router.get('/users')
async def get_users():
    users = list_seriallizer_user(user_collectoin.find())
    return users



@router.post('/register')
async def post_user(user: User):
    email = user_collectoin.find_one({'email': (user.email)})
    username = user_collectoin.find_one({'username': (user.username)})
    phone = user_collectoin.find_one({'phone': (user.phone)})

    if email or username or phone :
        return 'User email or phone or username already exists!'
    
    user_collectoin.insert_one(dict(user))
    return 'User created...'


  
