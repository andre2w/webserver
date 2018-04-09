def parse_request(request):
    """Parse the entire request request to a dict"""
    request_lines = request.split('\r\n\r\n')
    header_lines  = request_lines[0].split('\r\n')
    request_info = __parse_request_info(header_lines.pop(0))
   
    headers = {}    
    for line in header_lines:
        headers.update (__parse_headers(line))
   
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

def __parse_headers(line):
    """Parse all the headers into a dict"""
    splitted_line = line.split(':',1)
    return  { splitted_line[0].strip(): splitted_line[1].strip() }
