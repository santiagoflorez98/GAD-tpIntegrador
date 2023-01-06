import torch
import torchvision
import torchvision.models as models
from PIL import Image
import torch.nn as nn

img = Image.open("C:/Users/santi/OneDrive/Escritorio/297.png").convert('RGB')
img2 = Image.open("C:/Users/santi/OneDrive/Escritorio/297.png").convert('RGB')
# Load the pretrained model
model = models.resnet18(weights='DEFAULT')

# Use the model object to select the desired layer
layer = model._modules.get('avgpool')

# Set model to evaluation mode
model.eval()

transforms = torchvision.transforms.Compose([
    torchvision.transforms.Resize(256),
    torchvision.transforms.CenterCrop(224),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def get_vector(image):
    # Create a PyTorch tensor with the transformed image
    t_img = transforms(image)
    # Create a vector of zeros that will hold our feature vector
    # The 'avgpool' layer has an output size of 512
    my_embedding = torch.zeros(512)

    # Define a function that will copy the output of a layer
    def copy_data(m, i, o):
        my_embedding.copy_(o.flatten())                 # <-- flatten

    # Attach that function to our selected layer
    h = layer.register_forward_hook(copy_data)
    # Run the model on our transformed image
    with torch.no_grad():                               # <-- no_grad context
        model(t_img.unsqueeze(0))                       # <-- unsqueeze
    # Detach our copy function from the layer
    h.remove()
    # Return the feature vector
    return my_embedding

"""
pic_vector = get_vector(img)
pic2_vector = get_vector(img2)

cos = nn.CosineSimilarity(dim=1, eps=1e-6)
cos_sim = cos(pic_vector.unsqueeze(0),
              pic2_vector.unsqueeze(0))
print('\nCosine similarity: {0}\n'.format(cos_sim))
"""