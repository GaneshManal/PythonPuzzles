#!/bin/python

# Complete the sockMerchant function below.
def socks_merchant(socks):
    socks.sort()
    matched_count = 0
    while len(socks) > 1:
        if socks[0] == socks[1]:
            matched_count += 1
            socks.pop(0)
            socks.pop(0)
        else:
            socks.pop(0)
    return matched_count


if __name__ == '__main__':
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())

    result = socks_merchant(ar)
    print(result)
