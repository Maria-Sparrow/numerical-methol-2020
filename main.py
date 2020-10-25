def main():
    A = [

        [8.30, 3.08, 4.10, 1.90],
        [3.92, 8.45, 7.32, 2.46],
        [3.77, 7.67, 8.04, 2.28],
        [2.21, 3.19, 1.69, 6.69]
    ]
    n = len(A);
    det = 1
    v = matrix(n)
    c = matrix(n)
    for i in range(0, n):
        for j in range(0, n):
            v[i].append(A[i][j])

    for i in range(0, n):
        for j in range(0, n):
            c[i].append(A[i][j])
    for k in range(0, n):
        max = abs(v[k][k])

        w = k
        for l in range(k + 1, n):
            if max < v[k][l]:
                max = abs(v[k][l])
                w = l
        for d in range(0, n):
            value = v[k][d]
            v[k][d] = v[w][d]
            v[w][d] = value

        for d in range(0, n):
            if d < k:
                value = c[d][k]
                c[d][k] = c[d][w]
                c[d][w] = value
            else:
                value = v[d][k]
                v[d][k] = v[d][w]
                v[d][w] = value

        det = det * pow((-1), w + k) * v[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                c[k][j] = v[k][j] / v[k][k]
                v[i][j] = v[i][j] - v[i][k] * c[k][j]
    print(det)


def matrix(n):
    empty_matrix = []
    for column in range(0, n):
        empty_matrix.append([])
    return empty_matrix


if __name__ == '__main__':
    main()
