from flask import Flask
from flask import render_template
from flask import send_from_directory
from flask import abort, redirect, url_for, request

application = Flask(__name__, 
            static_folder='templates',
            template_folder='templates')

@application.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('templates/js', path)


@application.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('templates/css', path)


@application.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('templates/img', path)

@application.route('/favicon.ico')
def send_ico():
    return send_from_directory('templates', "favicon.ico")

@application.route('/robots.txt')
def send_robots():
    return send_from_directory('templates', "robots.txt")


@application.route('/')
def developing():
    return render_template('index.html')

@application.route('/secret')
def secret():
    return render_template('index.html')

@application.errorhandler(404)
def page_not_found(error):
    #return render_template('404.html'), 404
    return render_template('index.html')

@application.after_request
def apply_caching(response):
    response.headers["Cache-Control"] = "max-age=31536000"
    return response


        
# run the application.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production application.
    application.debug = True
    application.run()#ssl_context=('cert.pem', 'key.pem'))