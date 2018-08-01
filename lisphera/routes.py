from lisphera import app

@app.route('/')
def home():
    return 'hello'