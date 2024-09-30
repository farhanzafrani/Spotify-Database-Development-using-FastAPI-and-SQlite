from fastapi import FastAPI

app = FastAPI()


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
    