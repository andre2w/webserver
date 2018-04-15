def parse_request(request):
    """Parse the entire request request to a dict"""
    request_lines = request.split('\r\n\r\n')
    
    # Get the first line with the request info 
    # and parse the rest has headers
    header_lines  = request_lines[0].split('\r\n')
    request_info  = __parse_request_info(header_lines[0])  
    (headers, cookies) = __parse_headers(header_lines[1:])

    request_info['headers'] = headers
    request_info['cookies'] = cookies
    request_info['body']    = request_lines[1]
    return request_info

def __parse_request_info(line):
    """
    Parse request info to a dict
    input: GET / HTTP/1.1 
    output: {'method': 'GET', 'path': '/', 'version': 'HTTP/1.1' }
    """
    request_info = line.split()
    return {
        'method' : request_info[0],
        'path'   : request_info[1],
        'version': request_info[2]
    }

def __parse_headers(lines):
    """Parse all the headers into a dict"""
    headers = {}
    cookies = {}
    for line in lines:
        splitted_line = line.split(':',1)
        if splitted_line[0].lower() == 'cookie':
            cookies = __parse_cookies(splitted_line[1])
        else:
            headers[splitted_line[0]] = splitted_line[1].strip()
        
    return headers, cookies

def __parse_cookies(cookies):
    cookie_array = cookies.split(';') 
    result = {}
    for cookie in cookie_array:
        attributes = cookie.split(',')
        name = attributes[0].split('=')[0].strip()
        result[name] = {
            'value': attributes[0].split('=')[1]
        } 

        for attribute in attributes[1:]:
            attribute = attribute.split('=')
            result[name][attribute[0].strip()] = attribute[1]
    
    return result
            