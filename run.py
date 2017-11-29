from sys import argv, exit
from server import initApiServer

def http(app):
    app.run(host='0.0.0.0', port=80)

# DEV setting
# def http(app):
#     app.run(host='localhost', port=5000)

def https(app):
    sslContext = ('./ssl/cert.pem', './ssl/key.pem')
    app.run(host='0.0.0.0', port=443, ssl_context=sslContext)

if __name__ == '__main__':
    app = initApiServer('server.config.DevelopmentConfig')
    ## use command below to generate ssl certificates
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    https(app)