import numpy as np

def sinhma(m, p, s, n_output):
    output = s.copy()
    while(n_output > 0):
        n_output -= 1
        arr_m = np.array(output[len(output)-m:])
        bit = sum(arr_m*p) % 2
        output.append(bit)
    return output

if __name__ == '__main__':
    m = 4
    p = [1, 1, 0, 0]
    s = [0, 0, 1, 0]
    n_output = 15
    output = sinhma(m, p, s, n_output)
    print(''.join([str(x) for x in output]))