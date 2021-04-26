# Segmentation Client e-commerce Guidée par Intelligence Artificielle

Ce projet présente une solution de segmentation client orientée fidélisation pour la compagnie de vente e-commerce Olist. La fidélisation est vraisemblablement un véritable enjeu pour cette entreprise, car la grande majorité (97 %) de ses clients ne consomment qu'une seule fois.

Grâce aux données fournies par l'entreprise Olist, qui répertorient les achats de 96 milles clients sur une période de presque 2 ans (du 1er janvier 2017 au 31 août 2018), on est en mesure d'estimer le potentiel fidélité (ou score fidélité) d'un client sur la base de son dernier achat (prix, nombre et types d'articles achetés, type de paiement) et de ses données personnelles (non-intrusives), comme le code postal. En pratique, le score fidélité permet de séparer les clients potentiellement ponctuels d'un côté, et potentiellement fidèles de l'autre. La modéliation du score fidélité est effectuée à partir de l'algorithme d'apprentissage machine XGBoost.

La segmentation fidélité proposée s'appuie sur trois caractéristiques client : la récence, le score fidélité et le montant dépensé. Les critères de segmentation selon chacune des variables sont :
- la récence : 3 intervalles de taille semblable : [7, 4, 2, 0] mois
- le score fidélité : 2 intervalles. Les 80 % plus bas scores, et les 20% les plus hauts
- le montant : 3 intervalles de taille égales : [0, 56, 126, inf] reals

Au total, ce sont 3 x 2 x 3 = 18 segments client qui sont obtenus à partir des critères définis ci-dessus. Les segments sont facilement regroupables selon ses besoins. Par exemple, pour cibler les clients les plus susceptibles de consommer à nouveau, il est conseillé de sélectionner les segments client de récence inférieure à deux mois et de hauts scores fidélité (20% plus hauts scores). Enfin, la segmentation présente une grande stabilité sur une durée d'au moins 4 mois.

Ce dépôt contient les notebooks associés à la modélisation du score fidélité et de la segmentation client :
- [modélisation du score fidélité](https://nbviewer.jupyter.org/github/EloiLQ/fidelity-segments/blob/main/FidelityScore.ipynb) (FidelityScore.ipynb)
- [segmentation orienté fidélité](https://nbviewer.jupyter.org/github/EloiLQ/fidelity-segments/blob/main/FidelitySegmentation.ipynb) (FidelitySegmentation.ipynb)

Ce dépôt contient également une préparation des données d'Olist dans le but de réaliser une segmentation client, une étude sur les pistes de segmentations explorées  (recherche de patterns et RFM), et une segmentation de clustering classique à l'aide de l'algorithme K-Means (RFM plus note de satisfaction) : 
- [préparation des données](https://nbviewer.jupyter.org/github/EloiLQ/fidelity-segments/blob/main/DataWrangling.ipynb) (DataWrangling.ipynb)
- [pistes explorées, avec une recherche de patterns et une RFM](https://nbviewer.jupyter.org/github/EloiLQ/fidelity-segments/blob/main/ClusteringAndRFM.ipynb) (ClusteringAndRFM.ipynb)
- [segmentation K-Means, de variables RFM et note de satisfaction](https://nbviewer.jupyter.org/github/EloiLQ/fidelity-segments/blob/main/SegmentationKMeans.ipynb) (SegmentationKMeans.ipynb)
