#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())


    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        total = 0
        for b in self.buckets:
            total += b.length()
        return total
        # TODO: Count number of key-value entries in each of the buckets

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for i in bucket:
            if i.data[0] == key:
                return True
        return False

        # TODO: Check if the given key exists in a bucket

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        for i in bucket:
            if i.data[0] == key:
                return i.data[1]
        raise KeyError


        # TODO: Check if the given key exists and return its associated value


    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        entry = (key, value)
        reset = None
        for i in bucket:
            if i.data[0] == key:
                i.data = entry
                return
        bucket.append(entry)


        # TODO: Insert or update the given key-value entry into a bucket

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        toDelete = None
        for i in bucket:
            if key == i.data[0]:
                toDelete = i
                break

        if toDelete:
            bucket.delete(toDelete.data)
        else:
            raise KeyError

        # TODO: Find the given key and delete its entry if found

    def keys(self):
        """Return a list of all keys in this hash table"""
        allKeys = []
        for b in self.buckets:
            for i in b:
                allKeys.append(i.data[0])
        return allKeys


        # TODO: Collect all keys in each of the buckets

    def values(self):
        """Return a list of all values in this hash table"""
        allValues = []
        for b in self.buckets:
            for i in b:
                allValues.append(i.data[1])
        return allValues
        # TODO: Collect all values in each of the buckets
        pass
