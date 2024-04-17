# Machine_Learning_OSC_ISEN_Project_24
>Marie Devulder et Mathilde Rigaud.

## Le projet.
<div style="text-align: justify">Ce projet vise à exploiter les techniques de machine learning pour approfondir l'étude sur les cellules solaires organiques. L'objectif principal est d'optimiser leur efficacité et leur performance en analysant des ensembles de données. En utilisant des algorithmes d'apprentissage automatique, nous cherchons à identifier les facteurs clés qui influent sur le rendement des cellules solaires organiques, ce qui pourrait conduire à des avancées significatives dans le domaine de l'énergie solaire renouvelable. <br><br>
Ici le but est de se focaliser sur des combinaisions donc le PCE est autour des 15%.<br>
Les molécules donneuses et acceptrices dont on génère les SMILES (un schéma de la structure moléculaire traduit numériquement) ont des caractéristiques appelées descripteurs qui vont nous permettre d'identifier les paramètres qui favorisent ou défavorisent le rendement de la combinaison semiconductrice (Voc, Jsc, FF et PCE)</div>


## Trouver les SMILES
Comme il est difficile de trouver les SMILES selon les articles, grâce à des API comme ```pubchem``` et à la librairie python ```rdkit``` nous avons élaboré un script python avec deux méthode de recherche de SMILES.

Le fichier est dans le dossier 
<li> Par API

