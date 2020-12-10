root_path=$(pwd) \
&& git clone https://github.com/uoooohub/simple-python-sqlite.git . \
&& bash create_requirements.sh $root_path/python 'requests' 'bs4' \
&& bash init.sh 'python:3.8-slim' 'web123' 'db123'


