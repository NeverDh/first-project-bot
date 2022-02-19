import os

INPUT_DIR = "alvos"
OUTPUT_DIR = "saida"

def in_file(filename):
    return os.path.join(INPUT_DIR, filename)

def out_file(filename):
    return os.path.join(OUTPUT_DIR, filename)