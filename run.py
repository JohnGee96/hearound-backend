from server import initApiServer

def http(app):
    app.run(host='0.0.0.0', port=80)

# DEV setting
# def http(app):
#     app.run(host='localhost', port=5000)

if __name__ == '__main__':
    app = initApiServer('server.config.DevelopmentConfig')
    http(app)