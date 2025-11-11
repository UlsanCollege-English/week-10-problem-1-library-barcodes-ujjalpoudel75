import random

def hash_basic(key):
    """Hash function that sums ASCII values of characters and mods by table size."""
    return sum(ord(c) for c in key)

def make_table(size):
    """Create a hash table with the given size (list of empty lists for chaining)."""
    return [[] for _ in range(size)]

def put(table, key, value):
    """Insert or update a key-value pair in the hash table."""
    bucket_index = hash_basic(key) % len(table)
    bucket = table[bucket_index]
    
    # Check if key already exists and update it
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    
    # Key doesn't exist, append new pair
    bucket.append((key, value))

def get(table, key):
    """Retrieve the value for a given key, or None if not found."""
    bucket_index = hash_basic(key) % len(table)
    bucket = table[bucket_index]
    
    for k, v in bucket:
        if k == key:
            return v
    
    return None

def has_key(table, key):
    """Check if a key exists in the hash table."""
    bucket_index = hash_basic(key) % len(table)
    bucket = table[bucket_index]
    
    for k, v in bucket:
        if k == key:
            return True
    
    return False

def size(table):
    """Return the total number of key-value pairs in the hash table."""
    count = 0
    for bucket in table:
        count += len(bucket)
    return count