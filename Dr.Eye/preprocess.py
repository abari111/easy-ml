from torchvision import transforms





class RetNormalize:
    def __init__(self):
        pass


    def __call__(self, x):
        return x / 255
