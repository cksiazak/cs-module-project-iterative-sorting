# takes in array
def simple_implementation(arr):
    # loop from 1 to end of array
    for i in range(1, len(arr)):

        # save in temp variable
        temp = arr[i]

        # j keeps track of where to swap
        j = i

        # while j is less than 0 and temp is less than number to left
        while j > 0 and temp < arr[j - 1]:
            # copy element from left to this position
            arr[j] = arr[j - 1]

            # decrement our location
            j -= 1

        # the area where j is at, place temp
        arr[j] = temp

    return arr


# my_arr = [10, 8, 122, 3821, 321, 23, 4, 54, 644]
# print(simple_implementation(my_arr))

# sorting books:


class Book:
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre

    def __str__(self):
        return f'{self.title} by {self.author} in {self.genre}'


books = [Book("Melville", "Moby Dick", "whale stories"),
         Book("Immortal William", "Hamlet", "emo Danish princess"),
         Book("Douglas Adams", "Hitchiker's guide",  "space comedy")]


def insertion_sort(books):
    # iterate through list
    for i in range(1, len(books)):
        # set our book in location i to temp
        temp = books[i]

        # j will keep track
        j = i

        # while j is not in front of list
        # and temp is less than left books genre
        while j > 0 and temp.genre < books[j - 1].genre:
            # copy over books where j is to right
            books[j] = books[j - 1]
            j -= 1

        books[j] = temp

    return books

print(insertion_sort(books))