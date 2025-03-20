

def GetModelFullname(model):
    if model == "4o":
            model = "gpt-4o-2024-08-06"
    elif model == "35-16":
        model = "gpt-3.5-turbo-16k"
    elif model == "35-32":
        model = "gpt-3.5-turbo-32k"
    return model