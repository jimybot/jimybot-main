from models.utils.clean import clean_all_database
from sandboxes import creators

def create_sandbox(name, with_clean=True, **kwargs):
    if with_clean:
        clean_all_database()
    getattr(creators, name).create_sandbox(**kwargs)
