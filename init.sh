python_version=$1
service_web_name=$2
service_db_name=$3

sed -e "s/MY_WEB_SERVICE_NAME/${service_web_name}/g" tmp/docker-compose.yml > docker-compose.yml
sed -i -e "s/MY_DB_SERVICE_NAME/${service_db_name}/g" docker-compose.yml
sed -i -e "s/PYTHON_VERSION/${python_version}/g" docker-compose.yml
sed -e "s/PYTHON_VERSION/${python_version}/g" tmp/build/python/Dockerfile > python/Dockerfile

chmod 755 src/cgi-bin/api.py

docker-compose run $service_db_name python ./app/create_db.py 'articles'
docker-compose run $service_db_name python ./app/insert.py 'articles' '今朝のおかず' '魚を食べました'
docker-compose run $service_db_name python ./app/insert.py 'articles' '今日のお昼ごはん' 'カレーを食べました'
docker-compose run $service_db_name python ./app/delete.py 'articles' '2'
docker-compose run $service_db_name python ./app/insert.py 'articles' '今夜の夕食' '夕食はハンバーグでした'
docker-compose run $service_db_name python ./app/insert.py 'articles' '今日のお昼ごはん' 'カレーを食べました'
docker-compose run $service_db_name python ./app/update.py 'articles' '今朝のおかず' '肉を食べました'

docker-compose up
