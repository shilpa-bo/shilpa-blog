import multiprocessing
import time

def sort_files(process_name, num_files):
    print(f"{process_name} is starting to sort {num_files} files...")
    time_taken = num_files * 0.1  # Simulate time taken (0.1 seconds per file)
    time.sleep(time_taken)
    print(f"{process_name} has finished sorting {num_files} files in {time_taken:.2f} seconds.")

if __name__ == '__main__':
    start_time = time.time()  # Record the start time
    
    # Create multiple processes (Bictopus and friends)
    processes = []
    for i in range(8):
        process = multiprocessing.Process(target=sort_files, args=(f"Octopus-{i+1}", 30))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    end_time = time.time()  # Record the end time

    total_time = end_time - start_time
    print(f"All octopuses have sorted their files! Total time taken: {total_time:.2f} seconds.")

