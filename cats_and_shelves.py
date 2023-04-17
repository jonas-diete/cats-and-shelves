def cats_and_shelves(start_shelf, finish_shelf):
    difference = finish_shelf - start_shelf
    return difference // 3 + difference % 3