class MultiStack:
    def __init__(self, stack_size):
        self.number_stacks = 3
        self.custom_list = [0] * (stack_size * self.number_stacks)
        self.sizes = [0] * self.number_stacks
        self.stack_size = stack_size


if __name__ == "__main__":
    pass
