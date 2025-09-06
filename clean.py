import re

def clean_lat_fragment(input_path, output_path):
    # Шукає фрагмент з lat, long та gps_accuracy
    pattern = re.compile(
        r'position_lat,"(-?\d+)",semicircles,position_long,"-?\d+",semicircles,'
    )

    with open(input_path, 'r', encoding='utf-8') as infile:
        lines = infile.readlines()

    cleaned_lines = []
    for line in lines:
        if line.startswith("Data"):
            match = pattern.search(line)
            if match:
                lat_value = int(match.group(1))
                if lat_value < 0:
                    line = line.replace(match.group(0), "")  # Видаляємо фрагмент
        cleaned_lines.append(line)

    with open(output_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(cleaned_lines)

# Використання:
clean_lat_fragment("output.csv", "cleaned.csv")
