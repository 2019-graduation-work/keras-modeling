import os

directory = "C:/Users/hhj73/Desktop/2019-2/졸업프로젝트2/data/"
outfile_name = "merged_travel_transport.txt"

out_file = open(directory + outfile_name, "w", encoding='UTF8')
files = os.listdir(directory)
print(len(files))

for filename in files:
    if "crawl" not in filename:
        continue

    file = open(directory + filename, 'rt', encoding='UTF8')
    for line in file:
        out_file.write(line)
    out_file.write("\n")
    file.close()
out_file.close()
