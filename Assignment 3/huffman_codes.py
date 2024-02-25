import heapq
import os
import time
import random
import matplotlib.pyplot as plt

""" 
    Alexander Holmes
    2/25/24
    CS 4310 - Algorithm Analysis and Design
    https://github.com/ahalex73

"""


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char    # Given character
        self.freq = freq    # Given freqency of character
        self.left = None    # Left child node
        self.right = None   # Right child node

    def __lt__(self, other):
        """ Less than comparator fuction """
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    """ Constructs a huffman tree given a dictionary of frequencies """
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]


def build_huffman_tree_for_timing_n_frequencies(frequencies):
    """ Constructs huffman tree, times the construction of it, and sends back the root and building time"""
    start_time = time.time()
    priority_queue = [HuffmanNode(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        internal_node = HuffmanNode(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(priority_queue, internal_node)

    end_time = time.time()
    return priority_queue[0], end_time - start_time


def build_huffman_codes(node, current_code="", codes=None):
    """ Generates huffman codes, 0 for left path, 1 for right path"""
    if codes is None:
        codes = {}
    if node:
        if node.char is not None:
            codes[node.char] = current_code
        build_huffman_codes(node.left, current_code + "0", codes)
        build_huffman_codes(node.right, current_code + "1", codes)
    return codes

def total_weighted_external_path_length(node, depth=0):
    """ Gets the total weight external path length of generated huffman tree """
    if not node:
        return 0
    if not node.left and not node.right:
        return node.freq * depth
    return (total_weighted_external_path_length(node.left, depth + 1) +
            total_weighted_external_path_length(node.right, depth + 1))

def generate_huffman_code(frequencies):
    """ Generates a huffman code given frequencies """
    root = build_huffman_tree(frequencies)
    codes = build_huffman_codes(root)
    total_length = total_weighted_external_path_length(root)
    return codes, total_length

def generate_huffman_tree_and_codes(frequencies):
    huffman_codes, total_weighted_length = generate_huffman_code(frequencies)
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    print("\nTotal Weighted External Path Length:", total_weighted_length, "\n")

def generate_random_frequencies(n):
    return {chr(i): random.random() for i in range(65, 65+n)}

def clear_terminal():
    """ A function to allow clearing of terminal for better option displaying """
    # Windows
    if os.name == 'nt':
        os.system('cls')

    # Linux and MacOS
    else:
        os.system('clear')

def get_american_alphabet():
    """ Gather American alphabet frequencies for each character """
    char_frequencies = {
        'A': 0.073, 'B': 0.009, 'C': 0.030, 'D': 0.044, 'E': 0.130,
        'F': 0.028, 'G': 0.016, 'H': 0.035, 'I': 0.074, 'J': 0.002,
        'K': 0.003, 'L': 0.035, 'M': 0.025,  'N': 0.078, 'O': 0.074, 
        'P': 0.027, 'Q': 0.003, 'R': 0.077, 'S': 0.063, 'T': 0.093, 
        'U': 0.027, 'V': 0.013, 'W': 0.016, 'X': 0.005, 'Y': 0.019, 
        'Z': 0.001
    }

    return char_frequencies

def get_russian_alphabet():
    """ Gather russian alphabet frequencies for each character """
    char_frequencies = {
        'О': 11.18, 'Е': 8.75, 'А': 7.64, 'И': 7.09, 'Н': 6.78,
        'Т': 6.09, 'С': 4.97, 'Л': 4.96, 'В': 4.38, 'Р': 4.23,
        'К': 3.30, 'М': 3.17, 'Д': 3.09, 'П': 2.47, 'Ы': 2.36,
        'У': 2.22, 'Б': 2.01, 'Я': 1.96, 'Ь': 1.84, 'Г': 1.72,
        'З': 1.48, 'Ч': 1.40, 'Й': 1.21, 'Ж': 1.01, 'Х': 0.95,
        'Ш': 0.72, 'Ю': 0.47, 'Ц': 0.39, 'Э': 0.36, 'Щ': 0.30,
        'Ф': 0.21, 'Ё': 0.20, 'Ъ': 0.02
    }

    return char_frequencies

def get_japenese_alphabet():
    """ Gather japenese alphabet frequencies for each character """
    char_frequencies = {
        # Calculations were not done by hand.
        'い': 0.063412, 'し': 0.049721, 'う': 0.049311, 'ん': 0.049247, 'の': 0.039832,
        'か': 0.036568, 'た': 0.036276, 'と': 0.033021, 'す': 0.031056, 'で': 0.028984,
        'に': 0.026270, 'く': 0.026185, 'は': 0.026069, 'て': 0.025312, 'こ': 0.025107,
        'ま': 0.024642, 'な': 0.024082, 'が': 0.022140, 'き': 0.022134, 'る': 0.021247,
        'り': 0.018127, 'を': 0.017447, 'も': 0.016944, 'れ': 0.016202, 'つ': 0.016046,
        'じ': 0.015854, 'ら': 0.015216, 'あ': 0.014112, 'せ': 0.013260, 'ち': 0.012176,
        'お': 0.012064, 'さ': 0.011268, 'わ': 0.011186, 'だ': 0.010340, 'そ': 0.010145,
        'け': 0.009366, 'よ': 0.009308, 'ど': 0.008504, 'え': 0.008498, 'み': 0.007685,
        'ひ': 0.006620, 'め': 0.006318, 'ろ': 0.005144, 'ば': 0.005015, 'ぶ': 0.004669,
        'や': 0.004650, 'ほ': 0.004506, 'ね': 0.004219, 'ふ': 0.004138, 'げ': 0.003469,
        'ご': 0.003453, 'ぎ': 0.003088, 'む': 0.002958, 'び': 0.002924, 'ず': 0.002629,
        'べ': 0.002462, 'ざ': 0.002187, 'ぼ': 0.002007, 'ぜ': 0.001981, 'ぐ': 0.001834,
        'ゆ': 0.001830, 'ぷ': 0.001785, 'へ': 0.001756, 'ぞ': 0.001730, 'ぱ': 0.001248,
        'づ': 0.000770, 'ぽ': 0.000686, 'ぴ': 0.000668, 'ぺ': 0.000389, 'ぬ': 0.000307,
        'ぢ': 0.000038
}
    
    return char_frequencies

def get_arabic_alphabet():
    """ Gather arabic alphabet frequencies for each character """
    char_frequencies = {
    'ء': 0.0031, 'ؤ': 0.0009, 'ئ': 0.0028, 'ا': 0.125, 'آ': 0.0015,
    'أ': 0.0289, 'إ': 0.01, 'ب': 0.0467, 'ة': 0.0142, 'ت': 0.0261,
    'ث': 0.0087, 'ج': 0.0123, 'ح': 0.0186, 'خ': 0.0079, 'د': 0.0267,
    'ذ': 0.0096, 'ر': 0.042, 'ز': 0.0052, 'س': 0.0247, 'ش': 0.0073,
    'ص': 0.0104, 'ض': 0.0044, 'ط': 0.005, 'ظ': 0.0018, 'ع': 0.0401,
    'غ': 0.0033, 'ف': 0.0284, 'ق': 0.0269, 'ك': 0.0204, 'ل': 0.1207,
    'م': 0.0652, 'ن': 0.0661, 'ه': 0.0508, 'و': 0.058, 'ى': 0.0129,
    'ي': 0.0636
}
    
    return char_frequencies


if __name__ == "__main__":
    """ Call to main """
    """ Part 1 - Run for the frequencies of three """
    clear_terminal()

    num_desired_frequencies = 3 # This number controls how many times you'll
                                # Be prompted to use a type of frequency
    options = {
        '1': 'American frequencies',
        '2': 'Russian frequencies',
        '3': 'Japenese frequencies',
        '4': 'Arabic frequencies',
        '5': 'Exit (Continue to part 2 of program)\n'
    }

    while(num_desired_frequencies > 0):
        # Display options and number of selections left
        print("Number of selections left:" ,num_desired_frequencies)
        for option, info in options.items():
            print(f"Option {option}: {info}")

        # Gather desired frequency from the user
        option = input("Enter a number to select an option: ")
        clear_terminal()

        # Generate huffman codes based on user response
        if option == '1':
            frequencies = get_american_alphabet()
            generate_huffman_tree_and_codes(frequencies)
            num_desired_frequencies -= 1

        elif option == '2':
            frequencies = get_russian_alphabet()
            generate_huffman_tree_and_codes(frequencies)
            num_desired_frequencies -= 1

        elif option == '3':
            frequencies = get_japenese_alphabet()
            generate_huffman_tree_and_codes(frequencies)
            num_desired_frequencies -= 1

        elif option == '4':
            frequencies = get_arabic_alphabet()
            generate_huffman_tree_and_codes(frequencies)
            num_desired_frequencies -= 1

        elif option == '5':
            break

        else:
            print("Invalid option. Please enter '1' or '2'.\n\n")

    time.sleep(3)
    clear_terminal()
    
    print("Continuing to Part 2 of the assignment\n")

    """ Part 2 - Generate sets of n frequencies at random and run program for increasing n
        Time the execution of: 
        (1) building the initial heap keyed with the frequencies ; and 
        (2) the complete generation of the Huffman tree. Graph the times as a function of n.
    """

    # Iniate awesome countdown to second part of assignment
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)

    clear_terminal()
    print("Part 2!\n")

    num_generated_frequencies = [100, 500, 1000, 2000, 3000, 5000]  # Increase n as needed
    heap_building_times = []
    huffman_tree_times = []

    for n in num_generated_frequencies:
        frequencies = generate_random_frequencies(n)
        
        heap_building_avg_time = 0
        huffman_tree_avg_time = 0
        num_iterations = 10  # Number of iterations to get average time
        
        for _ in range(num_iterations):
            root, heap_building_time = build_huffman_tree_for_timing_n_frequencies(frequencies)
            heap_building_avg_time += heap_building_time
            
            start_time = time.time()
            generate_huffman_code(frequencies)
            end_time = time.time()
            huffman_tree_avg_time += end_time - start_time

        heap_building_avg_time /= num_iterations
        huffman_tree_avg_time /= num_iterations
        
        heap_building_times.append(heap_building_avg_time)
        huffman_tree_times.append(huffman_tree_avg_time)

    plt.plot(num_generated_frequencies, heap_building_times, label="Heap Building Time")
    plt.plot(num_generated_frequencies, huffman_tree_times, label="Huffman Tree Construction Time")
    plt.xlabel('Number of Frequencies (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Execution Time vs. Number of Frequencies')
    plt.legend()
    plt.show()
    
else:
    print("Failed to launch main")