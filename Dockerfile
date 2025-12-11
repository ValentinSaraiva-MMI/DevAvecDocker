#Create postgres Image for Tutorial Application
FROM postgres:18.1
COPY ./sqlfiles/migration-v001.sql /docker-entrypoint-initdb.d
EXPOSE 5432

