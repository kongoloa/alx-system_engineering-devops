# Install Nginx web server
exec { 'config':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; echo "Hello World!" > /var/www/html/index.nginx-debian.html; sed -i "48i location /redirect_me{\nrewrite ^/(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;\n}\n" /etc/nginx/sites-available/default;
sudo service nginx restart'
}
