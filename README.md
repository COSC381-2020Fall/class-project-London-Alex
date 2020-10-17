# COSC381 Fall 2020 Project

## Setup
1. Create your Google API Key.
2. Create your custom search engine that searches youtube.com and save your Search Engine ID.
3. Make sure your Google API credentials are updated with your current IP address.
4. Clone this repository.
5. Make sure your python packages match those in requirements.txt
    - You can use 'pip install -r requirements.txt' to accomplish this

## How to Run the Code
1. Modify config.py
    - Replace placeholder text in config.py with your API key and CSE ID.
3. Enter 'bash mainScript.sh' to execute each python file and script in the correct order.
4. Note that for my particular search term("Continental Divide"), 12 duplicate video ids are returned, so we end up with only 88 unique video descriptions.
5. mainScript.sh will print each step as it's accomplished and then display the results from the whoosh description search. It should display the titles for 10 videos that contain the word 'trail' in the description.
