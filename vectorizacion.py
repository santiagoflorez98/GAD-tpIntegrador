import torch
import torchvision.models as models

weights = models.ResNet18_Weights.DEFAULT
preprocess = weights.transforms()
model = models.resnet18(weights=weights)
layer = model._modules.get('avgpool')
model.eval()
def get_vector(image):
    # Create a PyTorch tensor with the transformed image
    t_img = preprocess(image)
    # Create a vector of zeros that will hold our feature vector
    my_embedding = torch.zeros(512)

    # Define a function that will copy the output of a layer
    def copy_data(m,i,o):
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