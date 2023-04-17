def cats_and_shelves(start_shelf, finish_shelf):
    difference = finish_shelf - start_shelf
    if difference < 3:
        return difference
    else:
        return 2