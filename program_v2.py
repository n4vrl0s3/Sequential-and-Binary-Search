# Proses Pencarian Sequential Search
def sequential_search(nama, data):
    for i in range(len(data)):
        if data[i][0] == nama:
            return data[i][1]
    return "Tidak ditemukan"

# Proses Pencarian Binary Search
def binary_search(nama, data):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid][0] == nama:
            return data[mid][1]
        elif data[mid][0] < nama:
            low = mid + 1
        else:
            high = mid - 1
    return "Tidak ditemukan"

# Contoh Data
data = [["budi", "LULUS"],
        ["andi", "TIDAK LULUS"],
        ["tini", "LULUS"],
        ["cindi", "LULUS"],
        ["tono", "TIDAK LULUS"],
        ["joko", "LULUS"]]

# Sorting Data (Wajib untuk Binary Search)
data.sort(key=lambda x: x[0])

# Contoh Pencarian
nama = "joko"

# Output Pencarian Sequential Search
result_seq = sequential_search(nama, data)
print(f"Hasil Pencarian Sequential Search: {result_seq}")

# Output Pencarian Binary Search
result_bin = binary_search(nama, data)
print(f"Hasil Pencarian Binary Search: {result_bin}")
