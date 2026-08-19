---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-182-1221-proposition-soit-t-b-aun-k-foncteur-radicie
section_title: "Proposition. Soit T : B → Aun K-foncteur radiciel entre deux pe-"
section_number: 12.2.1
pages: 63-64
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
tites K-cat´egories de Wedderburn. Notons ¯A = A/rad(A), ¯B = B/rad(B) et
¯T : ¯B → ¯A le foncteur induit. Soit sA : ¯A → A(resp. sB : ¯B → B) une
section de la projection canonique. Alors il existe un syst `eme (uX ) d’´el´ements de
1T (X) + rad(A)(T (X),T (X)) tel que sA ¯T (h) = uX ′TsB(h)(uX )−1 pour tout
h∈ ¯B(X,X′).
D´emonstration. 1) PosonsR = rad(A). Commenc ¸ons par le cas o` uR2 = 0 . On
aTsB(h)−sA ¯T (h)∈ rad(A) pour touth∈ ¯B. Ceci d´ eﬁnit une d´ erivation de¯B ` a
valeurs dans le ¯Be-module rad(A) (1-cocycle de Hochschild). Cette d´ erivation est
int´ erieure (1-cobord de Hochschild) : il existe une famille nX = uX− 1T (X) ∈
R(T (X),T (X)) v´ eriﬁant, pour touth∈ ¯B(X,X′),
TsB(h)−sA ¯T (h) = nX ′TsB(h)−TsB(h)nX,
d’o` u l’assertion.
2) Supposons maintenant seulement que R = rad(A) soit nilpotent d’´ echelon
r + 1 , et raisonnons par r´ ecurrence sur r (le cas r = 1 ´ etant acquis). Con-
sid´ erons la compositionB T→ A → A(r) = A/R. En appliquant l’hypoth` ese
64 YVES ANDR ´E ET BRUNO KAHN
de r´ ecurrence au foncteur compos´ e, on trouve un syst` eme (uX) d’´ el´ ements de
1T (X) +R(T (X),T (X)) tel que
sA ¯T (h)≡uX ′TsB(h)(uX )−1 (modRr).
Quitte ` a remplacersA par la section conjugu´ ee par les(uA)−1, on se ram` ene au
cas o` usA ¯T (h)≡TsB(h) moduloRr. On peut alors remplacerB par ¯B etA par la
cat´ egorie˜A introduite au pas 3) de la preuve du th´ eor` eme 12.1.1. Comme le radical
de cette derni` ere est de carr´ e nul, on conclut par le pas pr´ec´ edent.
3) Dans le cas g´ en´ eral, on applique un raisonnement ` a la Zorn comme au dernier
pas de la preuve du th´ eor` eme 12.1.1 : bri` evement, il existe une sous-cat´ egorie pleine
maximaleC deB telle que la proposition vaille pourC. On peut alors supposer que
B contient un seul objet hors deC, et de mˆ eme queA contient un seul objet hors de
T (Ob(C)). On constate comme ci-dessus que le radical de cette nouvell e cat´ egorie
A est alors (globalement) nilpotent. □
Dans le paragraphe suivant, nous appliquerons la propositi on 12.2.1 dans le cas
o` uA est munie d’une structure mono¨ ıdale• et o` uT est le foncteur canoniqueA⊠K
A→A :X = (A,B )↦→A•B, suppos´ e radiciel (ce qui revient ` a supposer que le
radical est un id´ eal mono¨ ıdal). Pourh =f⊗g,s =sA, on a alors
sA ¯T (h) = s(f•g),TsB(h) = s(f )•s(g).
Le compl´ ement de Malcev au th´ eor` eme de Wedderburn dit qu’on peut choisir
un scindage de Wedderburn dont l’image contient une sous-al g` ebre semi-simple
donn´ ee d’uneK-alg` ebre de Wedderburn. En voici une variante ` a plusieursobjets.
