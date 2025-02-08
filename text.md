Markdown Notes
Overview
This script is a web scraper that:

Fetches a list of pinball machines from the IPDB (Internet Pinball Database) search results.

Loops through each machine, extracts image links, and opens them in the default web browser.

Tracks the elapsed time and saves progress to a file (progress.txt) so the script can be stopped and resumed later.

Key Features
Progress Tracking:

The script saves the last processed machine ID and elapsed time to a file (progress.txt).

When restarted, it resumes from the last processed machine.

Stop Command:

Press Ctrl+C in the terminal to stop the script gracefully.

The current machine ID and elapsed time are saved before exiting.

Elapsed Time:

The script tracks the total time spent running and saves it in a human-readable format (e.g., 5 mins 30 secs).

Image Viewing:

Each image is opened in the default web browser, and the script waits for 10 seconds before moving to the next image.

How It Works
Fetching Search Results:

The script sends an HTTP request to the IPDB search URL and parses the HTML using BeautifulSoup.

Extracting Machine Links:

It extracts links to individual machine pages (e.g., machine.cgi?id=4089).

Processing Machines:

For each machine, it extracts image links (e.g., showpic.pl?id=4089&picno=6770).

Each image is opened in the browser, and the script waits for 10 seconds.

Saving Progress:

After processing each machine, the script saves the machine ID and elapsed time to progress.txt.

Resuming:

If the script is restarted, it reads the last processed machine ID and elapsed time from progress.txt and resumes from that point.

File Structure
progress.txt
Line 1: Last processed machine ID (e.g., 4089).

Line 2: Elapsed time in minutes and seconds (e.g., 5 mins 30 secs).

Example:

Copy
4089
5 mins 30 secs
Usage
Run the Script:

bash
Copy
python scraper.py
Stop the Script:

Press Ctrl+C in the terminal to stop the script.

The progress will be saved to progress.txt.

Resume the Script:

Run the script again, and it will resume from the last processed machine.

Dependencies
Install the required libraries:

bash
Copy
pip install requests beautifulsoup4
Customization
Change Delay:

Modify the time.sleep(10) line to adjust the delay between images.

Split into Thirds:

To process the machines in thirds, split the machine_links list into three parts and process them sequentially.

Browser Automation:

For more advanced browser interaction, replace webbrowser with selenium.

Error Handling
The script includes basic error handling for failed HTTP requests.

Add additional error handling for edge cases (e.g., invalid machine IDs, file read/write errors).

Example Output
Copy
Found 100 machines.
Resuming from machine ID: 4089
Processing machine: https://www.ipdb.org/machine.cgi?id=4089
Found 5 images for this machine.
Viewing image: https://www.ipdb.org/showpic.pl?id=4089&picno=6770
Viewing image: https://www.ipdb.org/showpic.pl?id=4089&picno=6771
...
Script stopped by user. Progress saved.
Total elapsed time: 5 mins 30 secs
Notes
Respectful Scraping: Ensure compliance with the website's robots.txt and terms of service.

Rate Limiting: Add delays between requests to avoid overloading the server.

Cross-Platform: Works on Windows, macOS, and Linux.

This Markdown documentation provides a clear explanation of the script's functionality, usage, and customization options.

