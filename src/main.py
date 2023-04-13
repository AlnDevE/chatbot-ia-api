from predict import predict

def get(message: str):
    message = message.replace('\n','') if '\n' in message else message
    return predict.get(message)