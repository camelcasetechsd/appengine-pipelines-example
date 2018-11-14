from app.modules.home import HomeHandler

def handlers():
    return [
        (r'/', HomeHandler),
    ]
