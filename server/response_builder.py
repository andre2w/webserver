http_messages = {
    200 : 'OK'
}

def __build_info(status):
    return f"HTTP/1.1 {str(status)} {http_messages[status]}\r\n"

def build_info(status,content):
    response =  f"HTTP/1.1 {str(status)} {http_messages[status]}\r\n"
    response += f"Content-Length: {str(len(content))}\r\n"
    return response

def build_headers(headers):
    response = ""
    for key, value in headers.items():
        response += f"{str(key)}: {str(value)}\r\n"
    return response

def build_cookies(cookies):
    response = ""
    for cookie in cookies:
        response += f"Set-Cookie: {cookie['name']}={cookie['value']}"
        
        if 'expiration' in cookie:
            response += f"; Expires={cookie['expiration']}"

        if cookie['secure']:
            response += f"; Secure"

        if cookie['httponly']:
            response += f"; HttpOnly"

        response += '\r\n'

    return response

def create_cookie(name,value,expiration = None,secure = False,httponly = False):
    cookie = { 
        'name'    : name,
        'value'   : str(value),
        'secure'  : secure,
        'httponly': httponly
    }

    if expiration is not None:
        cookie['expiration'] = str(expiration)
        
    return cookie

def build_body(content):
    return f"\r\n{str(content)}\r\n"