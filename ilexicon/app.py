from ilexicon import create_app


app = create_app()

@app.errorhandler(Exception)
def handle_errors(error):
    app.logger.error(f'系统异常：{str(error)}')
    return error

if __name__ == '__main__':
    app.run()