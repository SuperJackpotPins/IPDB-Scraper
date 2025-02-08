import requests
from bs4 import BeautifulSoup
import time
import webbrowser
import os
import signal
import sys
import argparse

# Base URL for the search results
base_url = "https://www.ipdb.org"
search_url = "https://www.ipdb.org/search.pl?gtype=SS&yr=1951-1999&ng=checked&sortby=name&searchtype=advanced"

# File to store the last processed machine ID and elapsed time
progress_file = "progress.txt"

# Flag to indicate if the script should stop
stop_script = False

# Start time of the script
start_time = None

# Function to handle the stop command
def signal_handler(sig, frame):
    global stop_script
    print("\nStop command received. Saving progress and exiting...")
    stop_script = True

# Register the signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

# Function to fetch and parse the page content
def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to retrieve page: {url}")
        return None

# Function to extract machine links from the search results
def extract_machine_links(soup):
    machine_links = []
    for link in soup.find_all('a', class_='linkid'):
        href = link.get('href')
        if href and 'machine.cgi?id=' in href:
            machine_links.append(base_url + href)
    return machine_links

# Function to extract image links from a machine page
def extract_image_links(soup):
    image_links = []
    for link in soup.find_all('a', href=True):
        if 'showpic.pl?id=' in link['href']:
            image_links.append(base_url + link['href'])
    return image_links

# Function to load the last processed machine ID and elapsed time
def load_progress():
    if os.path.exists(progress_file):
        with open(progress_file, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 2:
                machine_id = lines[0].strip()
                elapsed_time = lines[1].strip()
                return machine_id, elapsed_time
    return None, None

# Function to save the current machine ID and elapsed time
def save_progress(machine_id, elapsed_time):
    with open(progress_file, 'w') as file:
        file.write(f"{machine_id}\n")
        file.write(f"{elapsed_time}\n")

# Function to format elapsed time in minutes and seconds
def format_elapsed_time(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes} mins {seconds} secs"

# Main function to loop through search results and images
def main(num_machines):
    global stop_script, start_time

    # Start the timer
    start_time = time.time()

    # Fetch the search results page
    soup = fetch_page(search_url)
    if not soup:
        return

    # Extract all machine links
    machine_links = extract_machine_links(soup)
    print(f"Found {len(machine_links)} machines.")

    # Load the last processed machine ID and elapsed time
    last_processed_id, last_elapsed_time = load_progress()

    # Determine which machine to start from
    if last_processed_id:
        print(f"Resuming from machine ID: {last_processed_id}")
        # Find the index of the last processed machine
        for i, link in enumerate(machine_links):
            if last_processed_id in link:
                machine_links = machine_links[i:]
                break
    else:
        print("Starting from the beginning.")

    # Process the specified number of machines
    processed_count = 0
    for machine_link in machine_links:
        if stop_script or processed_count >= num_machines:
            break

        print(f"Processing machine: {machine_link}")
        machine_soup = fetch_page(machine_link)
        if not machine_soup:
            continue

        # Extract image links
        image_links = extract_image_links(machine_soup)
        print(f"Found {len(image_links)} images for this machine.")

        for image_link in image_links:
            if stop_script:
                break

            print(f"Viewing image: {image_link}")
            # Open the image in the default web browser
            webbrowser.open(image_link)
            # Wait for 10 seconds before moving to the next image
            time.sleep(10)

        # Save the current machine ID and elapsed time to the progress file
        machine_id = machine_link.split('id=')[1]
        elapsed_time = time.time() - start_time
        save_progress(machine_id, format_elapsed_time(elapsed_time))

        print("Finished processing images for this machine.")
        processed_count += 1

    if stop_script:
        print("Script stopped by user. Progress saved.")
    else:
        print(f"Finished processing {processed_count} machines.")

    # Print total elapsed time
    elapsed_time = time.time() - start_time
    print(f"Total elapsed time: {format_elapsed_time(elapsed_time)}")

if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Process a specified number of pinball machine results.")
    parser.add_argument(
        "--num_machines",
        type=int,
        required=True,
        help="Number of machine results to process."
    )
    args = parser.parse_args()

    # Run the main function with the specified number of machines
    main(args.num_machines)