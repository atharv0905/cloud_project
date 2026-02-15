import os
from fastapi import Header, HTTPException, Request, status
from dotenv import load_dotenv

load_dotenv()

POST_API_KEY = os.getenv("POST_API_KEY")
GET_API_KEY = os.getenv("GET_API_KEY")
GET_IP_WHITELIST = os.getenv("GET_IP_WHITELIST")


def verify_post_api_key(
    x_api_key: str = Header(..., alias="x-api-key")
):
    if not POST_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server misconfiguration",
        )

    if x_api_key != POST_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid POST API key",
        )


def verify_get_api_key(
    x_api_key: str = Header(..., alias="x-api-key")
):
    if not GET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server misconfiguration",
        )

    if x_api_key != GET_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid GET API key",
        )


def verify_get_ip_whitelist(request: Request):
    if not GET_IP_WHITELIST:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server misconfiguration",
        )

    allowed_ips = [
        ip.strip() for ip in GET_IP_WHITELIST.split(",") if ip.strip()
    ]

    forwarded = request.headers.get("x-forwarded-for")

    if forwarded:
        # first IP in list is real client
        client_ip = forwarded.split(",")[0].strip()
    else:
        client_ip = request.client.host if request.client else None

    if not client_ip or client_ip not in allowed_ips:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="IP address not allowed",
        )