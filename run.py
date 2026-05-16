import traceback

try:
    from dotenv import load_dotenv
    load_dotenv()

    from app import create_app

    app = create_app()
    
except Exception as e:
    from flask import Flask
    app = Flask(__name__)
    
    error_msg = traceback.format_exc()
    print(error_msg)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return f"<pre>Application failed to start. Traceback:\n\n{error_msg}</pre>", 500

if __name__ == '__main__':
    print("About to run the app...")
    app.run(debug=True, host='0.0.0.0', port=5000)
