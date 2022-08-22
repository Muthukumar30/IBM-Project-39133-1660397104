from customer import create_app

if __name__ == "__main__":
    # start the app only when this current file is being run directly
    app = create_app()
    app.run(debug=True)