from app import create_app

app = create_app()

if __name__ == '__main__':
    # Running the Flask app with debug mode enabled
    app.run(debug=True, host='0.0.0.0',port=5000)
    