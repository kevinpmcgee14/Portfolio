import torch
from .install_compiled_dependencies import download_dependency
from Tweet_Sentiment.model import get_token
download_dependency('trained_model')

def load_model(name):
    model = torch.load(name)
    model.eval()
    model.cpu()
    return model

model = load_model('trained_model_4_epochs.pth')

def handler(event, context):
    
    value = event['value']
    token = get_token(value).unsqueeze(0)
    pred = model(token)
    pred = torch.argmax(pred).item()
    return {
        'status': 200,
        'prediction': pred
    }