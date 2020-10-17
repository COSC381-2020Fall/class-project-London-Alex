#! /bin/bash
#! /bin/python
while IFS= read -r video_id; do
	python3 download_youtube_data.py $video_id
done < video_ids.txt
