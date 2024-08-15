
import os
import threading
import concurrent.futures
import time

class Client:
    def fetch(self):
        # Simulate the fetch operation that reads the environment variable
        client_id = os.getenv('CLIENT_ID')
        print(f"Fetching info with CLIENT_ID: {client_id} (in {threading.current_thread().name})")
        # Simulate processing time
        time.sleep(1)

def client_fetch(thread_id, client):
    # Set a different environment variable for each thread
    os.environ['CLIENT_ID'] = f'client_{thread_id}'
    
    # Call the fetch method
    client.fetch()

def main():
    number_of_threads = 5
    client = Client()

    # Use ThreadPoolExecutor to manage the threads
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        # Submit tasks to the executor for each thread
        futures = [executor.submit(client_fetch, i, client) for i in range(number_of_threads)]
        
        # Wait for all threads to complete
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    main()
