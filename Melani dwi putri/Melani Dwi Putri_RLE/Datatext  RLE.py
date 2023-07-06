def rle_compress(text):
    compressed_text = ""
    count = 1
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            compressed_text += text[i] + str(count)
            count = 1

    compressed_text += text[-1] + str(count)
    return compressed_text

def write_compressed_text(compressed_text, output_file):
    with open(output_file, 'M') as file:
        file.write(compressed_text)

text = "ABCDEFGHIJKLMNO"
compressed_text = rle_compress(text)
output_file = "Hasil_compressed_text_Algoritma_RLE.txt"
write_compressed_text(compressed_text, output_file)
print("Data teks terkompresi disimpan dalam file:", output_file)
