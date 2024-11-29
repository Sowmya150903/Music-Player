def min_subarray_len_brute_force(target, nums):
    n = len(nums)
    min_length = float('inf')

    # Iterate over all starting points
    for start in range(n):
        current_sum = 0
        # Iterate over all ending points for the current starting point
        for end in range(start, n):
            current_sum += nums[end]
            # Check if the sum is greater than or equal to the target
            if current_sum >= target:
                min_length = min(min_length, end - start + 1)
                break  # Stop checking further as we found a valid subarray
    
    # If no valid subarray found, return 0
    return min_length if min_length != float('inf') else 0

# Example usage
target = 7
nums = [2, 3, 1, 2, 4, 3]
result = min_subarray_len_brute_force(target, nums)
print(f"The minimum size of a subarray with sum >= {target} is: {result}")




def min_subarray_len(target, nums):
    n = len(nums)
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(n):
        current_sum += nums[right]
        
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

# Example usage
target = 7
nums = [2, 3, 1, 2, 4, 3]
result = min_subarray_len(target, nums)
print(f"The minimum size of a subarray with sum >= {target} is: {result}")



def length_of_longest_substring_brute_force(s):
    max_length = 0
    
    # Iterate over all possible substrings
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            # Check if the substring has all unique characters
            if len(set(substring)) == len(substring):
                max_length = max(max_length, len(substring))
    
    return max_length

# Example usage:
s = "abcabcbb"
result = length_of_longest_substring_brute_force(s)
print(f"The length of the longest substring without repeating characters is: {result}")



def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Example usage:
s = "abcabcbb"
result = length_of_longest_substring(s)
print(f"The length of the longest substring without repeating characters is: {result}")



def fullJustify(words, maxWidth):
    result = []
    line = []
    line_len = 0

    for word in words:
        # Check if adding the word exceeds maxWidth
        if line_len + len(word) + len(line) > maxWidth:
            # Distribute spaces evenly
            for i in range(maxWidth - line_len):
                line[i % (len(line) - 1 or 1)] += ' '
            result.append(''.join(line))
            line, line_len = [], 0
        line.append(word)
        line_len += len(word)

    # Handle the last line (left-justified)
    result.append(' '.join(line).ljust(maxWidth))
    return result

# Example Usage
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

output = fullJustify(words, maxWidth)
for line in output:
    print(f'"{line}"')


def fullJustify(words, maxWidth):
    result = []  # To store the justified lines
    i = 0        # Pointer to iterate through the list of words
    
    while i < len(words):  # Loop through all words
        # Step 1: Group words for the current line
        line_words = []
        line_len = 0
        
        while i < len(words) and line_len + len(words[i]) + len(line_words) <= maxWidth:
            line_words.append(words[i])
            line_len += len(words[i])
            i += 1
        
        # Step 2: Justify the current line
        if i == len(words):  # Last line: left-justify
            result.append(' '.join(line_words).ljust(maxWidth))
        else:  # Other lines: distribute spaces
            spaces_to_add = maxWidth - line_len
            if len(line_words) == 1:  # Only one word in the line
                result.append(line_words[0].ljust(maxWidth))
            else:
                spaces_between_words = spaces_to_add // (len(line_words) - 1)
                extra_spaces = spaces_to_add % (len(line_words) - 1)
                
                # Build the justified line
                line = ""
                for j in range(len(line_words) - 1):
                    line += line_words[j] + ' ' * (spaces_between_words + (1 if j < extra_spaces else 0))
                line += line_words[-1]  # Add the last word
                result.append(line)
    
    return result


def findSubstring(s, words):
    if not s or not words or len(words[0]) * len(words) > len(s):
        return []

    word_len = len(words[0])
    total_len = word_len * len(words)
    word_count = {}
    
    # Build the frequency map for words
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    result = []

    # Traverse the string with a sliding window
    for i in range(len(s) - total_len + 1):
        seen = {}
        valid = True
        
        # Check the substring from i to i + total_len
        for j in range(i, i + total_len, word_len):
            word = s[j:j + word_len]
            if word in word_count:
                seen[word] = seen.get(word, 0) + 1
                if seen[word] > word_count[word]:  # Exceeds allowed frequency
                    valid = False
                    break
            else:
                valid = False
                break

        if valid:
            result.append(i)
    
    return result
input="barfoothefoobarman"
word=["foo","bar"]
print(findSubstring(input,word))



from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])  # All words have the same length
    total_len = len(words) * word_len  # Length of the concatenated string
    word_count = Counter(words)  # Frequency map of words
    
    result = []
    
    # Loop through each possible starting index in s
    for i in range(len(s) - total_len + 1):
        substring = s[i:i + total_len]  # Substring of length total_len
        words_in_substring = [substring[j:j + word_len] for j in range(0, total_len, word_len)]  # Break into words
        
        if Counter(words_in_substring) == word_count:  # Compare frequency of words
            result.append(i)
    
    return result

def minWindowBruteForce(s, t):
    # Frequency map for characters in t
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    min_len = float("inf")
    min_window = ""

    # Generate all substrings and check if valid
    for i in range(len(s)):
        for j in range(i, len(s)):
            # Current substring
            substring = s[i:j+1]
            
            # Frequency map for current substring
            substring_freq = {}
            for char in substring:
                substring_freq[char] = substring_freq.get(char, 0) + 1
            
            # Check if all characters in t are satisfied in the substring
            valid = True
            for char, count in t_freq.items():
                if substring_freq.get(char, 0) < count:
                    valid = False
                    break
            
            # Update the minimum window if valid
            if valid and len(substring) < min_len:
                min_len = len(substring)
                min_window = substring

    return min_window

def minWindow(s, t):
    if not s or not t:
        return ""
    
    # Frequency map for characters in t
    t_freq = {}
    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1
    
    # Variables to track the sliding window
    left = 0
    right = 0
    min_len = float("inf")
    min_window = ""
    
    # Number of unique characters in t that need to match
    required_chars = len(t_freq)
    formed_chars = 0  # Number of characters in the window matching required counts
    
    # Window frequency map
    window_freq = {}
    
    while right < len(s):
        # Include the character at the right pointer
        char = s[right]
        window_freq[char] = window_freq.get(char, 0) + 1
        
        # Check if the current character satisfies the condition in t_freq
        if char in t_freq and window_freq[char] == t_freq[char]:
            formed_chars += 1
        
        # Try to shrink the window while it is valid
        while left <= right and formed_chars == required_chars:
            # Update the minimum window
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_window = s[left:right + 1]
            
            # Remove the leftmost character and move left pointer
            left_char = s[left]
            window_freq[left_char] -= 1
            if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                formed_chars -= 1
            left += 1
        
        # Expand the window by moving the right pointer
        right += 1
    
    return min_window




