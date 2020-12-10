python_version=$1
service_web_name=$2
service_db_name=$3

sed -e "s/MY_WEB_SERVICE_NAME/${service_web_name}/g" tmp/docker-compose.yml > docker-compose.yml
sed -i -e "s/MY_DB_SERVICE_NAME/${service_db_name}/g" docker-compose.yml
sed -i -e "s/PYTHON_VERSION/${python_version}/g" docker-compose.yml
sed -e "s/PYTHON_VERSION/${python_version}/g" tmp/build/python/Dockerfile > python/Dockerfile

chmod 755 src/cgi-bin/api.py

docker-compose run $service_db_name python ./main.py
docker-compose up