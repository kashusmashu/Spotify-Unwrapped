from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.auth import router as auth_router
from app.routes.top_artists_tracks import router as at_router


# define web app
app = FastAPI()

# list of origins allowed, define endpoint/url of frontend server
# must define any ENDPOINTS that you want to access your web app, base origin ex. frontend url, server ip address, another fastapi

origins = [
    "http://localhost:5173"
]

# enable and configure cors middleware, endpoint security, give access to frontend to interact with backend by defining origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,     # what are JWT tokens
    allow_methods=["*"],        # allow all methods, can specify methods to not include like delete methods
    allow_headers=["*"]         # same with headers
)


app.include_router(auth_router)
app.include_router(at_router)


# initializes fastapi
# can then call different endpoints, define routes
@app.get("/")
def root():
    return {"message": "API running"}