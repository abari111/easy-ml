import torch

@torch.no_grad
def test(model, dataloader_test):
    model.eval()
    acc = 0
    data_size = len(dataloader_test.dataset)
    for x, y in dataloader_test:
        y_pred = model(x) 
        acc += (y_pred.argmax(dim=1) == y).sum()
    print(f"test accuracy: {acc/data_size}")