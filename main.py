data = ["72366235", 2435234, False, 5.76334]

# Code here:

import itertools

data_generator = (item for item in data)

def reverse_data_generator(data):
    reversed_data = list(reversed(data))
    for item in reversed_data:
        yield item

class DataMerger:
    def __init__(self, generator1, generator2):
        self.generator1 = generator1
        self.generator2 = generator2
        self.current_pair = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_pair is None:
            self.current_pair = (next(self.generator1), next(self.generator2))
        else:
            self.current_pair = (self.generator1.send(self.current_pair[1]), self.generator2.send(self.current_pair[0]))
        return self.current_pair

def prefix_decorator(prefix):
    def decorator(generator):
        for item in generator:
            yield prefix + str(item)
    return decorator

def remove_duplicates(lst):
    unique_set = set(lst)
    unique_list = sorted(list(unique_set))
    str_list = [str(item) for item in unique_list]
    ascii_sums = [sum([ord(char) for char in item]) for item in str_list]
    sorted_str_list = [item for _, item in sorted(zip(ascii_sums, str_list))]
    result_list = [eval(item) for item in sorted_str_list]
    return result_list

def combine_data_generators(generator1, generator2):
    for pair in itertools.product(generator1, generator2):
        yield pair

decorated_data_generator = prefix_decorator("Item: ")(data_generator)
reversed_data_generator = reverse_data_generator(data)
combined_data_generator = combine_data_generators(decorated_data_generator, reversed_data_generator)
data_merger = DataMerger(decorated_data_generator, reversed_data_generator)

def concatenate_and_suffix(pair):
    return str(pair[0]) + " - " + str(pair[1])

merged_data = [concatenate_and_suffix(pair) for pair in combined_data_generator]

for loop in range(0, len(merged_data)):
    merged_data[loop] = merged_data[loop].replace('Item: ', '').split(' - ')[0]

for item in remove_duplicates(merged_data): print(item)
