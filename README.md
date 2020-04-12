# dockernameparser
Simple docker image using Python, Flask, uWsgi, and Nginx to expose a service that parses human names.
Behind the scene it uses the name parser library https://pypi.org/project/nameparser/

The images are available from Docker hub:
  - Flask App Image `docker pull shakeelosmani/nameparser:flask`
  - Nginx Image `docker pull shakeelosmani/nameparser:nginx`