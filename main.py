
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends, HTTPException, Header
from sqlmodel import Session
from database import create_db_and_tables, get_session
from models import Post
from crud import  get_public_posts, get_post_by_id, create_post, update_post, delete_post
import jwt
from auth import router as auth_router

SECRET_KEY = "3f8e1f8b9c5a4c1b2f6e8d7f6b5a4c3d8e1f9b6a7c5e4d3f2a1b0c9e8d7f6b5a"


app = FastAPI()

# Register the auth routes
app.include_router(auth_router, prefix="/auth")



app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://blogi-frontend.vercel.app",  # ✅ Vercel frontend
        "http://localhost:3000",              # ✅ Local development
    ],
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all HTTP methods
    allow_headers=["*"],  # ✅ Allow all headers
)





# def verify_token(token: str = Header(None)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return payload["sub"]
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token expired")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token")





def verify_token(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Token missing")

    try:
        token = authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        
        print("Token payload:", payload)  # 🟢 Log payload
        return payload["username"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

 


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.post("/create-public-post/")
def create_public_post(post: Post, session: Session = Depends(get_session)):
    return create_post(post, session)

@app.get("/public-posts/")
def public_posts(session: Session = Depends(get_session)):
    return get_public_posts(session)

@app.get("/posts/{post_id}")
def get_post(post_id: int, session: Session = Depends(get_session)):
    post = get_post_by_id(post_id, session)
    if post:
        return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/create-post/")
def create_new_post(post: Post, username: str = Depends(verify_token), session: Session = Depends(get_session)):
    post.author = username  # Set author from token
    return create_post(post, session)

@app.put("/update-post/{post_id}")
def update_existing_post(
    post_id: int,
    updated_post: Post,  # Expect a Post model
    username: str = Depends(verify_token),  
    session: Session = Depends(get_session)
):
    db_post = get_post_by_id(post_id, session)

    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")

    if db_post.author != username:
        raise HTTPException(status_code=403, detail="You can only edit your own posts")

    db_post = update_post(post_id, updated_post, session)
    return db_post


# @app.delete("/delete-post/{post_id}")
# def delete_existing_post(post_id: int, username: str = Depends(verify_token), session: Session = Depends(get_session)):
#     success = delete_post(post_id, session)
#     if success:
#         return {"message": "Post deleted"}
#     raise HTTPException(status_code=404, detail="Post not found")


@app.delete("/delete-post/{post_id}")
def delete_existing_post(
    post_id: int,
    username: str = Depends(verify_token),
    session: Session = Depends(get_session)
):
    post = get_post_by_id(post_id, session)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    # 🛡️ Only allow the author to delete their post
    if post.author != username:
        raise HTTPException(status_code=403, detail="You are not authorized to delete this post")

    success = delete_post(post_id, session)
    if success:
        return {"message": "Post deleted"}
    raise HTTPException(status_code=500, detail="Failed to delete post")
