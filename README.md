## Projet 1 LINFO1341 - Réseaux informatiques
### Victor Lepère, Ygor Lausberg

# Analyse d'applications réseaux

Cas de figures:
 - appel sans vidéo avec son
 - appel avec vidéo avec son
 - appel avec vidéo sans son
 - appel sans vidéo sans son
 - appel avec video avec Samson
 - pas d'appel (quand on fait rien skype echange quand même des paquets)
 - appel sans que l'autre personne ne réponde
 - alterner la personne qui racroche



Netcat
------

1) netcat => établit une connexion TCP

nc 'adresse IP' 'port'

2) Requête HTTP

GET / HTTP/1.1^M
Host: multipath-tcp.org^M
^M

Traceroute
----------
traceroute 'adresse IP / site web'


whois 'adresse IP'
