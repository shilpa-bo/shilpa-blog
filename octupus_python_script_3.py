import multiprocessing
import threading
import time

# Function to simulate file sorting in each thread
def sort_files(thread_name, num_files):
    print(f"{thread_name} is starting to sort {num_files} files...")
    time_taken = num_files * 0.1  # Simulate time taken (0.1 seconds per file)
    time.sleep(time_taken)
    print(f"{thread_name} has finished sorting {num_files} files in {time_taken:.2f} seconds.")

# Function for each process to spawn 4 threads
def process_with_threads(process_name):
    threads = []
    for i in range(8):  # Each process creates 4 threads
        thread = threading.Thread(target=sort_files, args=(f"{process_name}-Arm-{i+1}", 30))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    start_time = time.time()  # Record the start time

    # Create 4 processes, each process will have 4 threads
    processes = []
    for i in range(4):  # Create 4 processes
        process = multiprocessing.Process(target=process_with_threads, args=(f"Octopus-{i+1}",))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

    end_time = time.time()  # Record the end time

    total_time = end_time - start_time
    print(f"All processes and threads have finished! Total time taken: {total_time:.2f} seconds.")

