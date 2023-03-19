def build_heap(data):

    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        swaps += sift_down(data, i, n)
    return swaps

 

def sift_down(data, i, n):

    left_child = 2*i + 1
    right_child = 2*i + 2
    min_index = i

    
    if left_child < n and data[left_child] < data[min_index]:
        min_index = left_child

    if right_child < n and data[right_child] < data[min_index]:
        min_index = right_child

    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps = [(i, min_index)]

        swaps += sift_down(data, min_index, n)
        return swaps

    else:
        return []


def main():

    fileorno = input()

 

    if "I" in fileorno or "i" in fileorno:

        n = int(input())

        data = list(map(int, input().split()))

    elif "F" in fileorno or "f" in fileorno:

        file = input()

        if "a" not in file:

            with open("tests/" + file, 'r')as f:

                n = int(f.readline())

                data = list(map(int, f.readline().split()))

    assert len(data) == n

    swaps = build_heap(data)
    assert len(swaps) <= 4*n

        # output all swaps

    print(len(swaps))

    for i, j in swaps:

        print(i, j)
        
if __name__ == "__main__":

    main()
