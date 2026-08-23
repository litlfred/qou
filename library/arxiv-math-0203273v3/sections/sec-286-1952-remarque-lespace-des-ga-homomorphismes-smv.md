---
doc_id: arxiv-math-0203273v3
doc_title: "Nilpotence, radicaux et structures monoïdales"
section_id: sec-286-1952-remarque-lespace-des-ga-homomorphismes-smv
section_title: "Remarque. L’espace des Ga-homomorphismes SmV → SnV est de di-"
section_number: 19.5.2
pages: 111-112
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "Nilpotence, radicaux et structures monoïdales — 302 sections: YVES ANDR ´E ET BRUNO KAHN; Introduction; YVES ANDR ´E ET BRUNO KAHN"
---
mension|P (m,n )|, avec P (m,n ) = {j||m−n|≤ j ≤ m +n, j ≡ m +n
mod 2}.
En effet, comme SmV est auto-dual, ces homomorphismes s’identiﬁent aux in-
variants sous Ga dans SmV ⊗SnV . Or on a la d´ ecomposition de SL2-modules
SmV⊗SnV ∼
=⊕j∈P (m,n)SjV (Clebsch-Gordan), et chaqueSjV n’a qu’une droite
de vecteurs invariants sous Ga.
Pour compl´ eter l’´ etude deRepKGa, mentionnons le r´ esultat suivant, qui nous
servira ult´ erieurement.
19.5.3. Proposition. RepK Ga est strictement de Wedderburn.
D´emonstration. Il s’agit de montrer que le radical inﬁni est nul. Commenc ¸ons par
quelques remarques sur les ind´ ecomposables de RepKGa. Ils sont de la forme
SmV , o` uV est la repr´ esentation fondamentale de dimension 2, et admettent une
unique suite de composition (` a crans de dimension1). Tout homomorphismef de
SmV versSnV envoie le vecteur invariant deSmV sur 0 sim>n ou sim =n et
f n’est pas un isomorphisme.
Soient alorsW,W′ deux repr´ esentations, etf1,...f N une chaˆ ıne d’homomorphis-
mes dans le radical reliantW etW′. Quitte ` a remplacerf1 (resp. le compos´ ef des
fi) par le morphisme correspondant ˜f1 : 1→W∨⊗W1 (resp. ˜f : 1→W∨⊗W′),
etfi, pouri> 1, par ˜fi = 1 W ∨⊗fi (qui sont tous dans le radical puisque le radical
112 YVES ANDR ´E ET BRUNO KAHN
est un id´ eal mono¨ ıdal), on se ram` ene au casW = 1 (noter que ˜f est le compos´ e des
˜fi).
En outre, par additivit´ e, on peut supposer les sources et buts des fi ind´ ecompo-
sables, i.e. de la formeSnV . On a donc une chaˆ ıne de non-isomorphismes
1
f1
→Sn1V
f2
→Sn2V →···
fN
→SnNV
o` unN est ﬁx´ e (et inf´ erieur au produit des dimensions desW etW′ originaux). Si
N >nN, on aura doncni+1≤ni pour au moins l’un desi, et alors le compos´ e des
fj de 1 ` ai s’annulera d’apr` es l’observation pr´ ec´ edente. □
19.5.4. Remarques.
a) Il suit de l’exemple 14.3.2 et du th´ eor` eme 14.3.3 que le g roupo¨ ıde
Γ⊗(RepK Ga) a le mˆ eme type d’homotopie queGa → SpecK (au sens
de loc. cit. ).
b) Supposons K de caract´ eristiquep > 0. Alors le radical de RepK(Ga)
n’est pas mono¨ıdal. En effet, consid´ erons la repr´ esentation ind´ ecomposa-
ble standardW de dimensionp de Ga donn´ ee part↦→exptnp−1, o` unp−1
est l’endomorphisme nilpotent d’´ echelonp (un seul bloc de Jordan). Les
endomorphismes de cette repr´ esentation sont donn´ es par des matrices tri-
angulaires dont les coefﬁcients diagonaux sont tous ´ egaux ; leur trace est
donc nulle, ce qui montre qu’avec les notations de§4,W devient nul dans
RepK(Ga)/N . AinsiR⁄=N , etR n’est pas mono¨ ıdal d’apr` es 8.2.2.
c) Revenons ` a la caract´ eristique nulle. Consid´ erons la cat´ egorie tannakienne
A = RepKZ des repr´ esentations de dimension ﬁnie surK du groupe dis-
cret Z. Un r´ esultat de ‘folklore’, bas´ e sur la d´ ecomposition deJordan, dit
que son enveloppe pro-alg´ ebrique est le produit de Ga par un K-groupe
afﬁne de type multiplicatifT×µ∞ (T est un pro-tore,µ∞ est le groupe de
torsion, cyclique). Il d´ ecoule de l` a, du th´ eor` eme pr´ ec´ edent et du corollaire
19.4.4, que ¯A est⊗-´ equivalente ` aRepK(SL2×T×µ∞).
