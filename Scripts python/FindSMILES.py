from rdkit import Chem
import requests
import json

def methode_1():
    def get_smiles_from_sdf(sdf_path):
        mols = Chem.SDMolSupplier(sdf_path)
        smiles_list = []
        for mol in mols:
            if mol is not None:
                smiles = Chem.MolToSmiles(mol)
                smiles_list.append(smiles)
        return smiles_list

    # On entre le chemin du fichier SDF (obtenu par le site https://cactus.nci.nih.gov/cgi-bin/osra/index.cgi)
    # on est du coup obligé de convertir par le site une image
    # et on doit l'entrer directement dans le code pour l'instant
    smiles_names = []
    smiles_list = []

    # ENTRER ICI LES IMAGES SDF
    # On ajoute les noms des molécules et les SMILES correspondants
    smiles_list.append(get_smiles_from_sdf('img/PTB7-Th-sdf'))
    smiles_names.append('PTB7-Th')

    # Affichage des SMILES
    for smiles in smiles_list:
        print("\n .......... USING SDF TO GET SMILES ..........")
        print("-----------------------------------------------")
        print("\n")
        print(f"SMILES for {smiles_names[smiles_list.index(smiles)]} : ")
        print("\n")
        print(smiles)
        print("\n")
        print("-----------------------------------------------")
        print("\n     N        E        X        T     \n")


def methode_2():
    def get_smiles_from_name(name):
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{name}/property/CanonicalSMILES/JSON"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            return data['PropertyTable']['Properties'][0]['CanonicalSMILES']
        else:
            return None

    # On entre le nom des molécules
    molecules = []
    while True:
        molecule = input("\n Veuillez entrer le nom de la molécule (ou entrez 'done' pour terminer) : ")
        if molecule.lower() == 'done':
            break
        molecules.append(molecule)

    # On ajoute les noms des molécules et les SMILES correspondants
    smiles_list2 = []

    for molecule in molecules:
        smiles = get_smiles_from_name(molecule)
        if smiles:
            smiles_list2.append(smiles)
        else:
            print(f"Aucun SMILES trouvé pour la molécule '{molecule}'")

    # Affichage des SMILES
    for smiles in smiles_list2:
        print("\n .......... USING NAME TO GET SMILES ..........")
        print("-----------------------------------------------")
        print("\n")
        print(f"SMILES for {molecules[smiles_list2.index(smiles)]} : ")
        print("\n")
        print(smiles)
        print("\n")
        print("-----------------------------------------------")
        print("\n     N        E        X        T     \n")


# On choisit la méthode à utiliser pour obtenir les SMILES des molécules
while True:
    choix = input("Veuillez choisir la méthode à utiliser pour obtenir les SMILES des molécules (1 pour obtenir le SMILES par image ou 2 par recherche du nom) : ")
    if choix == '1':
        methode_1()
        break
    elif choix == '2':
        methode_2()
        break
    else:
        print("Veuillez entrer 1 ou 2")
        continue

