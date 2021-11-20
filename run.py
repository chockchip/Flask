from flaskblog import create_app

app = create_app()

# Command to run the application on this file
if __name__ == '__main__':
    app.run(debug=True)