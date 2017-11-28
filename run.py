from sys import argv, exit
from server import initApiServer

def http(app):
    app.run(host='0.0.0.0', port=80)

# DEV setting
# def http(app):
#     app.run(host='localhost', port=5000)

def https(app):
    sslContext = ('./ssl/cert.pem', './ssl/key.pem')
    app.run(host='localhost', port=443, ssl_context=sslContext)

# def getopts(argv):
#     """Collect command-line options in a dictionary"""
#     opts = {}  # Empty dictionary to store key-value pairs.
#     while argv:  # While there are arguments left to parse...
#         if argv[0][0] == '-':  # Found a "-name value" pair.
#             opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
#         argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
#     return opts

# def printUsage():
#     print("usage: run.py [-h] [-http] [-https PATH_TO_CERTIFICATES]\n")
#     print("Running the backend in either http or https mode\n")
#     print("Arguments:\n \
#       -h                            show this help message\n \
#       -http                         run server on http\n \
#       -http PATH_TO_CERTIFICATES    run server on https and provide path to certificates")
#     exit()

if __name__ == '__main__':
    # if len(argv) == 1:
    #     printUsage()
    # argOpts = getopts(argv)
    # if '-h' in argOpts:
    #     printUsage()
    # if ''
    app = initApiServer('server.config.DevelopmentConfig')
    ## user command below to generate ssl certificates
    # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
    https(app)