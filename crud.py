from sqlmodel import Session, select
from models import Post




def get_public_posts(session: Session):
    return session.exec(select(Post).where(Post.is_public == True)).all()

def get_post_by_id(post_id: int, session: Session):
    return session.get(Post, post_id)

def create_post(post: Post, session: Session):
    session.add(post)
    session.commit()
    session.refresh(post)
    return post

def update_post(post_id: int, updated_post: Post, session: Session):
    db_post = session.get(Post, post_id)
    if db_post:
        db_post.title = updated_post.title
        db_post.content = updated_post.content
        db_post.author = updated_post.author
        db_post.is_public = updated_post.is_public
        db_post.last_updated = updated_post.last_updated
        session.commit()
        session.refresh(db_post)
        return db_post
    return None

def delete_post(post_id: int, session: Session):
    db_post = session.get(Post, post_id)
    if db_post:
        session.delete(db_post)
        session.commit()
        return True
    return False
