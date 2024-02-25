import random
import time
import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(10000) # This is needed as to allow for more recursive calls

"""
Alexander Holmes


"""


# Function to find the position of the largest element in array
def max_position(low, high, array_of_values):
    if low == high:
        return low
    else:
        position = max_position(low + 1, high, array_of_values)
        if array_of_values[low] > array_of_values[position]:
            position = low
        return position


# Function to generate random values for an array of length n  
def generate_array(n):
    return [random.randint(0, 999) for _ in range(n)]


# Get a theoretical value for comparing n-1
def theoretical_result(n):
    """ Known n-1 Theoretical time complexity function """
    if n == 0:
        return 1
    else:
        return n * theoretical_result(n - 1)


if __name__ == "__main__":
    n_values = [10, 100, 500, 1000, 2000, 4000, 8000]  # Adjust these values as needed

    # Arrays to store the theoretical and experimental results
    theoretical_results = []
    max_position_results = []

    # Time each function for varying number of elements and print elapsed times
    for n in n_values:
        array_of_values = generate_array(n)

        # Measure the max_position function 
        start_time = time.perf_counter()
        max_position(0, n - 1, array_of_values)
        end_time = time.perf_counter()
        elapsed_time_seconds = end_time - start_time
        elapsed_time_nanoseconds = elapsed_time_seconds * 10**9
        
        # Measure the theoretical results function
        start_time_t = time.perf_counter()
        theoretical_result(n)
        #print(n)    # its not measuring theoretical results function
        end_time_t = time.perf_counter()
        elapsed_time_seconds_theo = end_time_t - start_time_t
        elapsed_time_nanoseconds_theo = elapsed_time_seconds_theo * 10**9

        print("Max-position-function\t\t", n, elapsed_time_nanoseconds, "nanoseconds")
        print("Theoretical-time\t\t", n, elapsed_time_nanoseconds_theo, "nanoseconds\n")

        # Get a list of time results to give to matplotlib to plot out
        max_position_results.append(elapsed_time_nanoseconds)
        theoretical_results.append(elapsed_time_nanoseconds_theo)


    # Plot the times out
    plt.plot(n_values, max_position_results, label='Experimental')
    plt.plot(n_values, theoretical_results, label='Theoretical')
    plt.xlabel('Array Size (n)')
    plt.ylabel('Time (nanoseconds)')
    plt.title('Experimental vs Theoretical Timing')
    plt.legend()
    plt.grid(True)
    plt.savefig('timing_graph.png')
    plt.show()
