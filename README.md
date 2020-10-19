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
5. mainScript.sh will print each step as it's accomplished and end after the whoosh index has been created. 
6. Enter 'python3 query\_on\_whoosh.py \<queryTerm\> \<pageNum\> \<numResults\>' to search
    - \<queryTerm\>: The term to be searched
    - \<pageNum\>: Which page of results to return
    - \<numResults\>: The number of results per page

## Steps to Execute Code Individually
While I've written mainScript.sh for the user's convenience, you can follow the below steps if you'd like to execute each part of code individually.

1. Modify config.py with your API key and CSE ID
2. python3 cse.py > google\_search.txt
    - Retrieves search results from the custom search engine
3. grep "'link'" google\_search.txt | awk -F 'v=' '{print substr($2,1,11)}' > video\_ids.txt
    - Extracts video ids from the search results
4. mkdir -p youtube\_data
5. bash download\_youtube\_data\_batch.sh
    - Retrieves video data for each video
6. python3 create\_data\_for\_indexing.py
    - Extracts id, title, and description for each video and saves it in JSON format
7. python3 create\_whoosh\_index.py
    - Create the whoosh search index
8. Enter 'python3 query\_on\_whoosh.py \<queryTerm\> \<pageNum\> \<numResults\>' to search
    - \<queryTerm\>: The term to be searched
    - \<pageNum\>: Which page of results to return
    - \<numResults\>: The number of results per page

## Technologies
- Custom Search Engine
- YouTube Data API
- Whoosh
- Python
