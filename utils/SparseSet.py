class SparseSet:
    """A Sparse Set with O(1) add, remove, and lookup.

    Stores items in a dense list for fast iteration,
    and a dict mapping items -> index for O(1) operations.
    """

    __slots__ = ("dense", "sparse")

    def __init__(self):
        self.dense = []       # actual objects (contiguous)
        self.sparse = {}      # maps object -> index in dense

    def add(self, value):
        """Add a value in O(1)."""
        if value in self.sparse:
            return  # already present
        self.sparse[value] = len(self.dense)
        self.dense.append(value)

    def remove(self, value):
        """Remove a value in O(1) by swapping with the last element."""
        idx = self.sparse.pop(value, None)
        if idx is None:
            return  # not present

        last = self.dense.pop()  # remove last element
        if idx < len(self.dense):  # if not removing last one
            self.dense[idx] = last
            self.sparse[last] = idx

    def __contains__(self, value):
        """Check membership in O(1)."""
        return value in self.sparse

    def __iter__(self):
        """Iterate over all elements (order is arbitrary)."""
        return iter(self.dense)

    def __len__(self):
        return len(self.dense)

    def clear(self):
        """Remove all elements."""
        self.dense.clear()
        self.sparse.clear()

    def __repr__(self):
        return f"SparseSet({self.dense!r})"
