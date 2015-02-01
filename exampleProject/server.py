import os

if __name__ == '__main__':
    from exampleApi import app
    app.run(host='0.0.0.0', port=int(os.getenv('VCAP_APP_PORT', os.getenv('PORT', 5000))))