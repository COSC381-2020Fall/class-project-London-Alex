#! /bin/bash
#! /bin/python
python3 cse.py > google_search.txt
echo "Executed cse.py Collected search results"
grep "'link'" google_search.txt | awk -F 'v=' '{print substr($2,1,11)}' > video_ids.txt
echo "Created video_ids.txt"
mkdir -p youtube_data
bash download_youtube_data_batch.sh
echo "Executed download_youtube_data_batch.sh Created youtube_data folder"
python3 create_data_for_indexing.py
echo "Executed create_data_for_indexing.py"
python3 create_whoosh_index.py
echo "Created whoosh index"
echo "To search: python3 query_on_whoosh.py <queryTerm> <pageNum> <numResults>"
