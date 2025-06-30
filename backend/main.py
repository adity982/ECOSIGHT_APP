import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import strawberry
from strawberry.asgi import GraphQL
from strawberry.file_uploads import Upload
from strawberry.types import Info
from typing import Optional

# Define the GraphQL schema using Strawberry
@strawberry.type
class Query:
    @strawberry.field
    def hello(self, name: Optional[str] = "World") -> str:
        return f"Hello {name}!"

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def upload_image(self, info: Info, file: Upload) -> str:
        # Process the file here
        # For now, just save it to a directory
        os.makedirs("uploads", exist_ok=True)
        file_path = f"uploads/{file.filename}"

        # Read the file content and save it
        file_content = await file.read()
        with open(file_path, "wb") as buffer:
            buffer.write(file_content)

        return f"File {file.filename} uploaded successfully."

schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create a FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add GraphQL endpoint
app.add_route("/graphql", GraphQL(schema))

@app.get("/")
def read_root():
    return {"Hello": "World"}

