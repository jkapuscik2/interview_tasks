from random import randint


def create_dataset(level):
    print("Creating dataset with {} nested levels.".format(level))
    dataset = [[]] * level
    nestion_sum = level

    for idx, dataset_index in enumerate(dataset):
        a = []
        for i in range(level):
            a = [a]
            if randint(0, 1) > 0:
                a.append([])
                nestion_sum = nestion_sum + 1

        dataset[idx] = a

    return dataset, nestion_sum
