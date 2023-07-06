import os
import hashlib

def compare(file_a, file_b):
    digest_a = generate_file_digest(file_a)
    digest_b = generate_file_digest(file_b)
    return digest_a == digest_b

def generate_file_digest(file_path):
    with open(file_path , "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
    return digest.hexdigest() 