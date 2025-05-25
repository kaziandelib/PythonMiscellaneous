# List of website URLs stored as strings
links = ['www.wiki.com', 'www.youtube.com', 'www.amazon.co.uk']

# Loop through each URL in the list one by one
for link in links:
    # For each URL, remove the prefix 'www.' if it exists at the start
    # The removeprefix() method returns a new string without that starting substring
    # If 'www.' is not at the start, it returns the string unchanged
    cleaned_link = link.removeprefix('www.')
    
    # Print the cleaned URL to the console/output
    print(cleaned_link)
