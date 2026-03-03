# Analyse de l'entropie d'un mot de passe

Utilisation de Python pour évaluer la complexité d'un mot de passe à l'aide de l'entropie de Shannon.

---

## Contexte

La sécurité d'un mot de passe ne dépend pas uniquement de sa longueur, en effet, un mot de passe long mais répétitif (ex. `aaaaaaaaaaaa`) reste très vulnérable. L'entropie de Shannon permet de **quantifier mathématiquement l'imprévisibilité** d'un mot de passe en mesurant la diversité de ses caractères.

---

## Formule de Shannon

L'entropie est calculée selon la formule suivante :

$$H = -\sum_{i} p_i \cdot \log_2(p_i)$$

Où :
- `H` est l'entropie (en bits par caractère)
- `p_i` est la fréquence relative du caractère `i`, c'est-à-dire son nombre d'occurrences divisé par la longueur totale du mot de passe

**Intuition :** plus les caractères sont variés et équitablement répartis, plus `H` est élevée, et plus le mot de passe est imprévisible.

| Exemple | Entropie | Interprétation |
|---|---|---|
| `aaaaaaaaaaaa` | 0.00 bits | Aucune diversité |
| `abcdabcdabcd` | 2.00 bits | Faible diversité |
| `aB3!xZ9#mQ2@` | ~3.58 bits | Haute diversité |

---

## Fonctionnement

1. L'utilisateur saisit un mot de passe
2. Le programme vérifie la longueur (minimum 12 caractères requis)
3. L'entropie est calculée via la formule de Shannon
4. Un verdict automatique est affiché selon le score :

| Score d'entropie | Verdict |
|---|---|
| `< 2.0 bits` | Risque élevé : trop de répétitions |
| `2.0 – 3.5 bits` | Sécurité modérée |
| `> 3.5 bits` | Haute résistance |

**Comprendre les bits :** le score est exprimé en bits par caractère. Un bit représente un choix binaire (0 ou 1) : une entropie de 4 bits par caractère signifie que chaque caractère peut prendre $2^4 = 16$ valeurs également probables, ce qui le rend très difficile à prédire.

En multipliant ce score par la longueur du mot de passe, on obtient l'**entropie totale**. Un mot de passe de 10 caractères avec 4 bits par caractère offre ainsi une résistance de 40 bits, soit $2^{40}$ combinaisons, plus de 1 000 milliards.

---

## Utilisation

```bash
python entropie.py
```

```
Entrez un mot de passe à tester : MonMotDePasse!99
Longueur du mot de passe : 16 caractères
Longueur satisfaisante.
Score d'entropie : 3.81 bits par caractère
Haute résistance : grande diversité de caractères.
```

Un score de 3.81 bits par caractère indique que les caractères du mot de passe sont très diversifiés et répartis de façon quasi uniforme. Combiné à une longueur de 16 caractères, cela représente une entropie totale d'environ 61 bits ($2^{61}$ combinaisons), ce qui rend une attaque par force brute statistiquement inviable.

---

## Ce que j'ai appris

- Appliquer un concept mathématique (l'entropie de Shannon, issue de la théorie de l'information) à un problème concret de cybersécurité
- Utiliser `collections.Counter` pour transformer une chaîne de texte en données statistiques exploitables, sans avoir à construire manuellement un dictionnaire de fréquences
- Comprendre que l'entropie par caractère est additive : si chaque caractère apporte 4 bits d'incertitude, un mot de passe de 10 caractères offre $2^{40}$ combinaisons possibles, ce qui rend une attaque par force brute statistiquement inviable
