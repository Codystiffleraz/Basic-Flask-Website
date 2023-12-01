from website import create_app

app = create_app()

# Will run server if we run this line
if __name__ == '__main__':
    app.run(debug=True)