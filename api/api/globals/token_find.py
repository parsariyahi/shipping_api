def token_finder(authorization_header: str) -> str:
    return authorization_header.replace("Token ", "")