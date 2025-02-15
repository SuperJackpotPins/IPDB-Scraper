# IPDB-Scraper
## Example `progress.txt` File
When the script is stopped, the progress.txt file will look like this:

```
4089
5 mins 30 secs
The first line is the last processed machine ID.
```

The second line is the elapsed time in minutes and seconds.

How to Use
Run the script with the --num_machines argument:

bash
Copy
python ipdb-webscraper.py --num_machines 10
This will process 10 machines and then stop.

To resume later, run the script again with a new --num_machines value:

bash
Copy
python ipdb-webscraper.py --num_machines 15
The script will resume from the last processed machine and process 15 more machines.

To stop the script manually, press Ctrl+C. The progress will be saved to progress.txt.

Example Output
Copy
Found 100 machines.
Resuming from machine ID: 4089
Processing machine: https://www.ipdb.org/machine.cgi?id=4089
Found 5 images for this machine.
Viewing image: https://www.ipdb.org/showpic.pl?id=4089&picno=6770
Viewing image: https://www.ipdb.org/showpic.pl?id=4089&picno=6771
...
Finished processing 10 machines.
Total elapsed time: 5 mins 30 secs
Notes
Flexibility: The --num_machines argument allows you to control how many machines to process in each run.

Progress Tracking: The progress.txt file ensures that the script can resume from where it left off.

Error Handling: Add additional error handling for edge cases, such as invalid machine IDs or network issues.

This updated script provides a flexible and user-friendly way to process a specific number of machines while maintaining progress tracking.

