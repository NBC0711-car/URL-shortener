This project is made in order to have an URL-shortener without using a data base, we use a DNS structure (IONOS) that stores our data.
with the use of the TXT we can store URLs, so we can decrease them later.
The project is simple in this case because we only use the URL-shortener for github but we can use it for other sites.
This project works thanks to two scripts made in python: 
The first one (server.py) is executed in a server enviroment like Flask and using dnspython.
the script start listening on port 8080 waiting for a request, then it defines a dinamic rute that gets any word written next to the domain.
It constructs the FQDN combining the short word and the domain, and at last it executes a request type TXT.
The script also have a try except in case the DNS log doesnt exist giving you a 404 error message.

The second script (shortpath.py) its used on a local enviroment, and it verificates the flooding of the DNS without using neither a web browser neither Flask.
It makes the same request as the server, but instead of redirect HTTP, it uses the webbrowser library to automatically open the URL in our default browser, 
in short it takes you to the site instead of giving you the address.

Then we have to use IONOS and create TXT logs and also A logs so all this can work:

<img src="Captura de pantalla_20251107_110008.png"/>
