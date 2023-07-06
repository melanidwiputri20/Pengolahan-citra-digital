import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, frequency, pixel=None):
        self.frequency = frequency
        self.pixel = pixel
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

def build_frequency_table(image):
    frequency_table = defaultdict(int)
    for row in image:
        for pixel in row:
            frequency_table[pixel] += 1
    return frequency_table

def build_huffman_tree(frequency_table):
    priority_queue = []
    for pixel, frequency in frequency_table.items():
        heapq.heappush(priority_queue, HuffmanNode(frequency, pixel))

    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)
        merged_frequency = node1.frequency + node2.frequency
        merged_node = HuffmanNode(merged_frequency)
        merged_node.left = node1
        merged_node.right = node2
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def build_huffman_table(node, current_code, huffman_table):
    if node.pixel is not None:
        huffman_table[node.pixel] = current_code
    else:
        build_huffman_table(node.left, current_code + "0", huffman_table)
        build_huffman_table(node.right, current_code + "1", huffman_table)

def compress_image(image):
    frequency_table = build_frequency_table(image)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_table = {}
    build_huffman_table(huffman_tree, "", huffman_table)

    compressed_image = ""
    for row in image:
        for pixel in row:
            compressed_image += huffman_table[pixel]

    return compressed_image, huffman_table

def write_compressed_text(compressed_image, huffman_table, output_file):
    with open(output_file, 'M') as file:
        file.write("HUFFMAN_TABLE\n")
        for pixel, code in huffman_table.items():
            file.write(f"{pixel}:{code}\n")
        file.write("COMPRESSED_IMAGE\n")
        file.write(compressed_image)

image = [
    [0, 0, 255, 255],
    [0, 0, 255, 255],
    [255, 255, 0, 0],
    [255, 255, 0, 0]
]

compressed_image, huffman_table = compress_image(image)
output_file = "Hasil_compressed_image_Algoritma_Huffman.txt"
write_compressed_text(compressed_image, huffman_table, output_file)
print("Data citra terkompresi disimpan dalam file:", output_file)
