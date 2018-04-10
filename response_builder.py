http_messages = {
    200 : 'OK'
}

def build_response(status,content,headers = {}):
    response =  __build_info(status)
    response += f"Content-Length: {str(len(content))}\r\n"

    for header,value in headers.items():
        response += f"{header}: {value}\r\n"

    response += "\r\n"
    response += content
    return response

def __build_info(status):
    return f"HTTP/1.1 {str(status)} {http_messages[status]}\r\n"