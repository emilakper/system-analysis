import os

def main(v: str) -> list[list[int]]:
    lines = v.strip().split('\n')
    edges = []
    verts = set()

    for line in lines:
        v1, v2 = line.split(',')
        verts.add(v1)
        verts.add(v2)
        edges.append((v1,v2))

    verts = sorted(list(verts))

    n = len(verts)
    matrix = [[0] * n for _ in range(n)]

    for v1, v2 in edges:
        i = verts.index(v1)
        j = verts.index(v2)
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix

if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, "task0.csv")

    with open(csv_path,"r") as file:
        input_data = file.read()

    result = main(input_data)

    for row in result:
        print(row)
