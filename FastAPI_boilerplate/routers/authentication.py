from fastapi import APIRouter , Depends , HTTPException , status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas , database , models , token
from ..hashing import Hash
from sqlalchemy.orm import Session
# from blog.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
 
 
router = APIRouter(
    tags= [' Authentication']
)
 
 
@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "Invalid Credentials")
 
    # Remove password verification for testing purposes
    if not Hash.verify(user.password , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail = "Incorrect password")
 
 
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.email}
        # , expires_delta=access_token_expires
    )
    id = user.id
    return {"access_token": access_token, "token_type": "bearer"}
 
 