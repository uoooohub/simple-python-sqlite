service_name=$1

sed -e "s/MY_WEB_SERVICE_NAME/${service_name}/g" tmp/docker-compose.yml > docker-compose.yml
sed -i -e "s/MY_DB_SERVICE_NAME/${service_name}/g" docker-compose.yml
cp tmp/build/python/Dockerfile python/Dockerfile

chmod 755 src/cgi-bin/api.py

docker-compose up