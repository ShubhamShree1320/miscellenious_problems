def group_anagrams_with_stack(strs):
    def creating_char_int_array(string):
        char_array = [char for char in string]
        int_array = [ord(char) for char in char_array]
        return sorted(int_array)

    anagram_groups = []
    
    for s in strs:
        int_array_s = creating_char_int_array(s)
        found = False
        # Use stack-like list to check and place anagrams
        for group in anagram_groups:
            int_array_g = creating_char_int_array(group[0])
            if int_array_s == int_array_g:
                group.append(s)
                found = True
                break
        
        if not found:
            anagram_groups.append([s])
    
    return anagram_groups

# Example usage
strs = ["act", "pots", "tops", "cat", "stop", "hat"]
output = group_anagrams_with_stack(strs)
print(output)  # Output: [["act", "cat"], ["pots", "tops", "stop"], ["hat"]]
