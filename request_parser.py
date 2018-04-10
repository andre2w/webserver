def parse_request(request):
    """Parse the entire request request to a dict"""
    request_lines = request.split('\r\n\r\n')
    
    # Get the first line with the request info 
    # and parse the rest has headers
    header_lines  = request_lines[0].split('\r\n')
    request_info  = __parse_request_info(header_lines[0])  
    headers       = __parse_headers(header_lines[1:])

    request_info['headers'] = headers
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
    for line in lines:
        splitted_line = line.split(':',1)
        headers[splitted_line[0]] = splitted_line[1].strip()
        
    return headers 
