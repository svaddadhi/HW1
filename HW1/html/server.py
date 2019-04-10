from bottle import get, route, run, template, view, static_file


@route('/images/<filename:re:.*\.jpg>')
def send_image(filename):
    return static_file(filename, root='images', mimetype='image/jpg')

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='HW1')

@route('/css/<filename:re:.*.css>')
def serve_css(filename):
    return static_file(filename, root='css', mimetype='text/css')



run(reloader=True, host='localhost', port=8080)