import torch
from torchvision import transforms
from PIL import Image
import numpy as np
from model import TransformerNet

def load_model(style_name, model_dir='models/saved_models'):
    model = TransformerNet()
    model.load_state_dict(torch.load(f"{model_dir}/{style_name}.pth", map_location='cpu'))
    model.eval()
    return model

def stylize_image(model, image):
    # Preprocessing: resize, convert to tensor, scale to [0, 255]
    transform = transforms.Compose([
        transforms.Resize(512),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x.mul(255))
    ])
    input_tensor = transform(image).unsqueeze(0) # [1, 3, H, W]

    # Stylize
    with torch.no_grad():
        output_tensor = model(input_tensor).squeeze(0).clamp(0, 255)
    
    # Convert output tensor to a displayable image
    output_image = output_tensor.permute(1,2,0).byte().numpy() # [H, W, 3]
    return Image.fromarray(output_image)
