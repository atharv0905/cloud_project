import os
from fastapi import Header, HTTPException, status
from dotenv import load_dotenv

load_dotenv()

POST_API_KEY = os.getenv("POST_API_KEY")
GET_API_KEY = os.getenv("GET_API_KEY")

def verify_post_api_key(x_post_api_key: str = Header(...)):
    if POST_API_KEY is None:
        raise RuntimeError("POST_API_KEY not configured")

    if x_post_api_key != POST_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid POST API key",
        )

def verify_get_api_key(x_get_api_key: str = Header(...)):
    if GET_API_KEY is None:
        raise RuntimeError("GET_API_KEY not configured")

    if x_get_api_key != GET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid GET API key",
        )