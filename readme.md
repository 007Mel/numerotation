# Numérotation de fichiers par date de modification

Un petit script Python qui **renomme les fichiers d'un dossier en les numérotant**, dans l'ordre de leur date de modification (du plus ancien au plus récent).

Idéal pour remettre de l'ordre dans un dossier contenant un playlist des vidéos téléchargées sur YouTube.

## Fonctionnalités

- Demande à l'utilisateur le chemin du dossier à traiter
- Trie les fichiers par date de modification
- Ajoute un numéro d'ordre devant chaque fichier

## Prérequis

- [Python 3.8+](https://www.python.org/downloads/)

Aucune bibliothèque externe n'est nécessaire.

## Utilisation

1. Lancez le script :

   ```bash
   python main.py
   ```

2. Quand le programme vous le demande, saisissez le chemin du dossier à traiter, par exemple :
   - Windows : `C:\Users\Moi\Documents\MesFichiers`
   - Linux / macOS : `/home/moi/Documents/MesFichiers`

3. Les fichiers du dossier sont alors renommés avec un numéro, selon leur date de modification.

## Exemple

**Avant :**

```
Installation de l'interpréteur.mp4      (modifié le 12 mars à 20:00)
Introduction.mp4                        (modifié le 12 mars à 19:59)
Premier Programme.mp4                   (modifié le 12 mars à 20:01)
```

**Après :**

```
(1)_Introduction.mp4
(2)_Installation de l'interpréteur.mp4
(3)_Premier Programme.mp4
```

## Avertissement

Le script **renomme directement les fichiers**. Pensez à faire une **copie de sauvegarde** de votre dossier avant la première utilisation.
