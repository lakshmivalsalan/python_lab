def nearly_equal(a, b):
    # Step 1: if lengths differ, cannot be nearly equal
    if len(a) != len(b):
        return False

    # Step 2: count mismatched characters
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1

        # More than 1 mismatch → not nearly equal
        if count > 1:
            return False

    # Step 3: exactly 1 mismatch → nearly equal
    return count == 1


# --- Sample Runs ---
print(nearly_equal("book", "boak"))   # True (one character changed)
print(nearly_equal("test", "tent"))   # True
print(nearly_equal("apple", "apple")) # False (no mutation)
print(nearly_equal("cat", "cuts"))    # False (different lengths)