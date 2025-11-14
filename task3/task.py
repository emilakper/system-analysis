import json
import numpy as np

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        return content

def main(json_a, json_b):
    rank_a = json.loads(json_a)
    rank_b = json.loads(json_b)
    
    all_objs = set()
    for rank in [rank_a, rank_b]:
        for cluster in rank:
            if not isinstance(cluster, list):
                cluster = [cluster]
            all_objs.update(cluster)
    
    if not all_objs:
        return []
    n = max(all_objs)
    
    def build_matrix(rank):
        pos = [0] * n
        current_pos = 0
        for cluster in rank:
            if not isinstance(cluster, list):
                cluster = [cluster]
            for obj in cluster:
                pos[obj - 1] = current_pos
            current_pos += 1
        
        mat = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                if pos[i] >= pos[j]:
                    mat[i, j] = 1
        return mat
    
    YA = build_matrix(rank_a)
    YB = build_matrix(rank_b)
    
    YAB = YA * YB
    
    YA_T = YA.T
    YB_T = YB.T
    YAB_prime = YA_T * YB_T
    
    kernel = []
    for i in range(n):
        for j in range(i + 1, n):
            if YAB[i, j] == 0 and YAB_prime[i, j] == 0:
                kernel.append([i + 1, j + 1])
    
    return kernel


json_a = read_json_file('range_a.json')
json_b = read_json_file('range_b.json')
json_c = read_json_file('range_c.json')

print("СРАВНЕНИЕ РАНЖИРОВОК")
print("range_a.json vs range_b.json")
result_ab = main(json_a, json_b)
print(f"Ядро противоречий: {result_ab}")

print("\nrange_a.json vs range_c.json")
result_ac = main(json_a, json_c)
print(f"Ядро противоречий: {result_ac}")

print("\nrange_b.json vs range_c.json")
result_bc = main(json_b, json_c)
print(f"Ядро противоречий: {result_bc}")