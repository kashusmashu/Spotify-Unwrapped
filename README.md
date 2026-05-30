# Spotify-Unwrapped
This is a personal learning project


# Notes for Self


### Folder Structure
**backend_fastapi**
    **app**: source code of project
        **db**: database schema, i dont think i need to create one but if i were to itd be here
        **models**: where to store files that define models, schemas, validation logic
        **services**: contains actual business logic, functions that define them
        **routes**: defines CRUD methods for endpoints, calls functions from services.py, authentication here before endpoints can be accessed; <ins>no business logic here, only specify where the routes are</ins>
        **dependencies**: contains files used throughout app in different ways,
        *main.py*: create fastapi app, imports routes and uvicorn, base route?
        *requirements.txt*: list of packages to install
    **tests**: where i would store my test files
**frontend_react**
    **src**: source code
        **components**
        **musicApi**: contains endpoints
        
        Will add more info once I undertand more about the structure



