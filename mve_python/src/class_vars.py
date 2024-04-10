class myClass():
    # unless I initialize this value, on import of this file,
    # it fails with "AttributeError: type object 'bob' has no attribute 'api_key'"
    # because it is unbound
    # api_key: str
    api_key: str = "alpha"

    def __init__(self, api_key: str):
        self.api_key = api_key

if __name__ == "__main__":
    print(f"{myClass.api_key=}")

    my_instance = myClass("beta")

    print(f"{my_instance.api_key=}")    # the dynamic passed into my INSTANCE variable
    print(f"{myClass.api_key=}")        # the constant value assigned to my CLASS variable
