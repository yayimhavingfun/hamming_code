def calculate_redundant_bits(m):
    for r in range(m):
        if 2**r >= m + r + 1:
            return r


def position_redundant_bits(data, r):
    j = 0
    k = 1
    m = len(data)
    result = ''

    for i in range(1, m + r + 1):
        if i == 2**j:
            result += '0'
            j += 1
        else:
            result += data[-1 * k]
            k += 1
    return result[::-1]


def calculate_parity_bits(arr, r):
    n = len(arr)

    for i in range(r):
        value = 0
        for j in range(1, n + 1):
            if j & 2**i == 2**i:
                value ^= int(arr[-1*j])

        arr = arr[:n - 2**i] + str(value) + arr[n - 2**i + 1:]
    return arr


def calculate_hamming_rate(data):
    m = len(data)
    r = calculate_redundant_bits(m)
    total_bits = m + r
    rate = m / total_bits
    return rate

data = '0101001101111011011010110000001001100110111010110100000000110111001101100001000'

m = len(data)
r = calculate_redundant_bits(m)
array = position_redundant_bits(data, r)
array = calculate_parity_bits(array, r)
print("Encoded value: " + array)
rate = calculate_hamming_rate(data)
print("Rate: " + str(rate))


