from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class Blog(BaseModel):
    title: str 
    body : str


@app.get("/")
def index():
    return "Welcome to FastAPI"

@app.get("/about")
def about_section():
    return "This is the about section of the course .."

    
@app.get("/about/unpublished")
def unpublished():
    return {"unpublished_blogs": "This is the list of unpublised blogs ..."}

@app.get("/about/{id}")
def about(id: int):
    # fetch the comments corresponding when id == id
    return {"data": {f"{id}": "comments string",
                     f"{id + 1}": "comments of the strings..."}}
    
@app.get("/blogs")
def blogs(limit:int=10, published:bool=True, sort: str | None = None):
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}
    
@app.post("/add_blog")
def add_blog(request:Blog):
    return f"Blog with the title {request.title} has been created."


# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=8000)