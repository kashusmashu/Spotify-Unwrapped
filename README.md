# Spotify-Unwrapped
This is a personal learning project


# Notes for Self


### Folder Structure
**backend_fastapi**
    **app**: source code of project
        **db**: database schema, i dont think i need to create one but if i were to itd be here
        **models**: where to store files that define models & their schemas, validation logic
        **services**: contains actual business logic
        **routes**: defines CRUD methods for endpoints, routers, authentication here before endpoints can be accessed; <ins>no business logic here, only specify where the routes are</ins>
        **util**: contains files used throughout app in different ways,
        *main.py*: create fastapi app
        *requirements.txt*: list of packages to install
    **tests**: where i would store my test files
**frontend_react**
    **src**: source code
        **components**
        **musicApi**: contains endpoints
        
        Will add more info once I undertand more about the structure



