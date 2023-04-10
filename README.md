<h1 align="center">
  <br>
  LINFO1341 – Réseaux informatiques
  <br>
</h1>

<h4 align="center">Projet 1 : Analyse d'application réseaux.</h4>

<p align="center">
  <a href="#sujets-étudiés">Sujets étudiés</a> •
  <a href="#usage">Usage</a> •
  <a href="#auteurs">Auteurs</a> •
  <a href="#ressources">Ressources</a>
</p>

## Contexte

Dans se répertoire vous retrouvez les fichiers pcap de captures d'échange de données faites via l'applictaion Skype. 
Ainsi que les scripts python utilisés pour l'analyse de ces fichiers.  
La majorité des captures ont été faites entre Victor et Ygor, Victor se situant  dans les environs de Namur et Ygor dans les environs de Bruxelles.
Certaines captures ont été faites sur le réseau eduroam de l'UClouvain.


## Hiérarchie du répertoire

* **pyshark/** : contient les scripts python utilisés pour l'analyse des fichiers pcap
* **Traces/** : contient les fichiers pcap analysés
  * **BiCapture/** : contient les fichiers pcap des captures bidirectionnelle
    * **V-POV/** : contient les fichiers pcap des captures bidirectionnelle capturé par Victor
    * **Y-POV/** : contient les fichiers pcap des captures bidirectionnelle capturé par Ygor
  * **SurEduroam/** : contient les fichiers pcap des captures faites sur le réseau eduroam de l'UClouvain
  * Reste des captures n'ayant pas de contexte particulier

## Utilisation des scripts

Dans le terminal exécuter les commandes suivantes :

```bash
$ python3 pyshark/script.py
```

## Auteurs

Les éléments de ce répertoire ont entièrement été créé par Ygor Lausberg et Victor Lepère dans le cadre du cours de *Réseaux Informatiques* dispensé par Pr. Olivier Bonaventure.

## Ressources

* [Réseaux informatique - LINFO1341](https://uclouvain.be/cours-2021-linfo1341) - Site du cours
* [Syllabus](https://beta.computer-networking.info/syllabus/default/index.html) - Syllabus du cours
* [Moodle](https://moodle.uclouvain.be/course/view.php?id=1269) - Moodle du cours

---

> GitHub [Projet](https://github.com/Lopiuy/LINFO1341_P1) &nbsp;&middot;&nbsp;
> [Ygor Lausberg](mailto:ygor.lausberg@student.uclouvain.be) &nbsp;&middot;&nbsp;
> GitHub [@Lopiuy](https://github.com/Lopiuy) &nbsp;&middot;&nbsp;
> [Victor Lepère](mailto:victor.lepere@student.uclouvain.be) &nbsp;&middot;&nbsp;
> GitHub [@victxrrr](https://github.com/victxrrr)