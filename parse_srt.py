import re
from translate_model import zh2en

def to_srt(seq, time, text):
    output = ""
    for i in range(len(seq)):
        output += seq[i] + "\n" + time[i] + "\n" + text[i] + "\n\n"
    
    return output

def split_srt(text):
    # Split the input text into lines
    lines = text.strip().split('\n')

    # Initialize empty arrays for sequence numbers, timestamps, and text
    sequence_numbers = []
    timestamps = []
    text_data = []

    # Iterate through the lines and extract sequence numbers, timestamps, and text
    for i in range(0, len(lines), 4):
        # Extract sequence number from the first line in each group
        sequence_numbers.append(lines[i])

        # Extract timestamp from the second line in each group
        timestamp_match = re.search(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', lines[i+1])
        if timestamp_match:
            timestamps.append(timestamp_match.group())

        # Extract text from the third line in each group
        text_data.append(lines[i+2])
        
    return sequence_numbers, timestamps, text_data

def translate(arr):
    translated_arr = zh2en(arr)
    return translated_arr

def new_filename(path):
    path_arr = path.split("/")
    filename = path_arr[-1].split(".")

    new_filename = filename[0] + "_en." + filename[1]
    out = '/'.join(path_arr[:-1]) + "/" + new_filename
    
    return out

"""
Main Program
"""
path = "./validation_data/sukhothai_captions.srt"
fin = open(path, "r")
raw = fin.read()

seq, time, text = split_srt(raw)
text_en = translate(text)
output = to_srt(seq, time, text_en)
print(output)

filename_en = new_filename(path)
fout = open(filename_en, "w")
fout.write(output)
fout.close()
