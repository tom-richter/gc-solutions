// Solution for GC5TGF8 - Ausprobieren???
// This solution takes about 10 minutes. It can be optimized by memoization.

#include <iostream>
#include <chrono>

using namespace std; 
using namespace std::chrono; 

int main(int argc, char *argv[])
{
    long long starting_number_with_longest_series = 0;
    int longest_series_length = 0;

    auto start = high_resolution_clock::now(); 

    for (long long starting_number = 1; starting_number < 1000000000; starting_number++){
        long long current_number = starting_number;
        int current_length = 1;
        while (current_number > 1){
            current_length++;
            if (current_number % 2 == 0){
                current_number /= 2;
            } else {
                current_number = current_number * 3 + 1;
            }
        }
        if (current_length > longest_series_length){
            longest_series_length = current_length;
            starting_number_with_longest_series = starting_number;
        }
    }

    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(stop - start); 
  
    cout << "Time taken by function: " << duration.count() << " seconds" << endl; 
    cout << "Starting number with longest series: " << starting_number_with_longest_series << endl;
    cout << "Longest series length: " << longest_series_length << endl;
        
    return 0;
}
