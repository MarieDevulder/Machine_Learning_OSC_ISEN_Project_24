# Machine_Learning_OSC_ISEN_Project_24
>Marie Devulder et Mathilde Rigaud.

## Le projet.
Ce projet vise à exploiter les techniques de machine learning pour approfondir l'étude sur les cellules solaires organiques. L'objectif principal est d'optimiser leur efficacité et leur performance en analysant des ensembles de données. En utilisant des algorithmes d'apprentissage automatique, nous cherchons à identifier les facteurs clés qui influent sur le rendement des cellules solaires organiques, ce qui pourrait conduire à des avancées significatives dans le domaine de l'énergie solaire renouvelable. <br><br>
Ici le but est de se focaliser sur des combinaisions donc le PCE est autour des 15%.<br>
Les molécules donneuses et acceptrices dont on génère les SMILES (un schéma de la structure moléculaire traduit numériquement) ont des caractéristiques appelées descripteurs qui vont nous permettre d'identifier les paramètres qui favorisent ou défavorisent le rendement de la combinaison semiconductrice (Voc, Jsc, FF et PCE)


## Trouver les SMILES
Comme il est difficile de trouver les SMILES selon les articles, grâce à des API comme ```pubchem``` et à la librairie python ```rdkit``` nous avons élaboré un script python avec deux méthode de recherche de SMILES.

Le fichier est dans le dossier ```Scrpits python```
<li> ```methode_1()``` qui est la méthode qui utilise ```rdkit``` en construisant le SMILES par une image en *.sdf* (si vous n'avez que du JPG ou PNG il faut passer par un convertisseur). Le chemin de l'image est un intégrer directement dans le code à la ligne 23 : ```smiles_list.append(get_smiles_from_sdf('img/VOTRE-MOLECULE-EN-SDF'))``` et le nom de votre molécule à la ligne d'en dessous ```smiles_names.append('NOM-DE-VOTRE-MOLECULE')```

