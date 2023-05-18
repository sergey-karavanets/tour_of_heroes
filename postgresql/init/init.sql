CREATE USER myuser WITH ENCRYPTED PASSWORD 'password';
CREATE DATABASE tour_of_heroes WITH OWNER myuser;
GRANT ALL ON DATABASE tour_of_heroes TO myuser;