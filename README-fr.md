# Extract to TXT

![Version](https://img.shields.io/badge/version-b1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-beta-orange.svg)

Extract to TXT est une extension pour le logiciel de cartes mémoire Anki qui vous permet d'extraire vos notes et leur contenu dans un fichier texte brut. Cela vous offre un moyen pratique d'exporter vos données Anki pour une analyse ultérieure ou un partage (par exemple soumettre vos cartes à ChatGPT pour automatiser la production de nouvelles cartes...).

**Veuillez noter que cette extension prend en charge uniquement la langue anglaise.**

## Fonctionnalités

- Extrait les notes et leur contenu d'Anki vers un fichier texte brut.
- Prend en charge l'exportation de notes à partir de plusieurs paquets.
- Options de configuration conviviales pour spécifier le chemin du fichier de sortie.

## Utilisation

1. Installez l'extension dans Anki.
2. Ouvrez Anki et accédez au menu Outils.
3. Sélectionnez "Modules complémentaires", puis "Extract to TXT" et "Configuration" pour définir le chemin du fichier de sortie.
4. Dans la boîte de dialogue de configuration, spécifiez le chemin du fichier de sortie souhaité dans la clé `01_output_path` et cliquez sur Enregistrer. Plusieurs exemples de chemins sont disponibles pour vous aider à choisir le bon chemin de fichier, et l'opération est intuitive. Le chemin par défaut dirige le fichier vers le dossier "user".
5. Ouvrez la section Parcourir d'Anki.
6. Sélectionnez les notes que vous souhaitez extraire.
7. Cliquez avec le bouton droit sur les notes sélectionnées dans la section des notes et choisissez "Extraire vers un fichier TXT" dans le menu contextuel.
8. Les notes sélectionnées seront extraites et enregistrées dans le fichier texte spécifié.

## Informations importantes

Les informations collectées et exportées par cette extension peuvent être utiles pour générer automatiquement des cartes mémoire à l'aide de modèles d'IA textuels tels que ChatGPT.

## Commentaires et support

Cette extension est actuellement en version bêta, et vos commentaires sont grandement appréciés. Si vous rencontrez des problèmes ou avez des suggestions d'amélioration, veuillez créer une nouvelle demande (issue) sur le dépôt GitHub.

## Licence

Cette extension est sous licence [MIT License](LICENSE).
