import threading
import time

def sort_files(thread_name, num_files):
    print(f"{thread_name} is starting to sort {num_files} files...")
    time_taken = num_files * 0.1  # Simulating time taken to sort files (0.1 seconds per file)
    time.sleep(time_taken)
    print(f"{thread_name} has finished sorting {num_files} files in {time_taken:.2f} seconds.")

# Create multiple threads (Bictopus' arms)
threads = []
start_time = time.time()  # Record the start time
for i in range(8):
    thread = threading.Thread(target=sort_files, args=(f"Arm-{i+1}", 30))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()  # Record the end time

total_time = end_time - start_time
print(f"All arms have sorted their files! Total time taken: {total_time:.2f} seconds.")

