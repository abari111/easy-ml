import yaml


if __name__=="__main__":
    with open('retmodel.yml') as f:
        model_arch = yaml.safe_load(f)

    for k, v in model_arch.items():
        print(k + ":")
        for k_1, v_1 in v.items():
            if k_1 == "conv":
                print("Convolutional layer: ", v_1)
            elif k_1 == "linear":
                print("Linear: ", v_1)
            elif k_1 == "pool":
                print("Pooling: ", v_1)
