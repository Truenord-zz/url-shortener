# endpoints from fastapi
from fastapi import FastAPI, HTTPException, Depends 
from fastapi.responses import RedirectResponse 

from pydantic import BaseModel, HttpUrl
from sqlalchemy.orm import Session # the seesion object

# own files
from database import get_db
from models import URL
from utils import short_url_generator

# this will be the api
app = FastAPI(
    title="URLShortener",
    description="Shortens urls of arbitrary lengths to a new unique url",
    version="0.1.0"
)

def URLRequest():
    url: HttpUrl  # verify it is actual url with pydantic
    
def URLResponse(): # contents of repsonses
    original_url: str
    short_code: str
    short_url: str


#get
@app.get("/")
def read_root():
    #return naive message
    return {
        "message": "URL Shortener API",
        "version": ".0.0",
        "endpoints": {
            "POST /shorten": "Shorten some URL",
            "GET /{short_code}": "Redirect to original URL",
            "GET /statistics/{short_code}": "Get URL statistics"
        }
    }
