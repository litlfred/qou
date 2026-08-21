---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-006-6-profondeur-67
section_title: "Profondeur 67"
section_number: 6
pages: 2-7
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
Appendice. Rappels sur les groupes alg´ ebriques unipotent s 76
Bibliographie 82
i
0. Introduction.
Si k est un corps de nombres, on dispose d’une cat´ egorie tannakienne MT(k) des motifs
de Tate mixte sur k, pour laquelle les groupes d’extensions de Q(0) par Q(n) ont la relation
d´ esir´ ee avec les groupes deK-th´ eorie dek. C’est le coeur d’une t-structure sur une sous-
cat´ egorie de la cat´ egorie triangul´ ee motivique de Levine (1998) ou Voevodsky (2000). La
conjecture d’annulation de Beilinson-Soul´ e est vraie surk, et c’est ce qui permet de d´ eﬁnir
la t-structure requise. Par Levine (1998) et Huber (2000), on di spose sur cette cat´ egorie
tannakienne de foncteurs ﬁbres “r´ ealisation” correspond ant aux th´ eories de cohomologie
usuelles (sauf que la cohomologie cristalline n’a jusqu’` a pr´ esent pas ´ et´ e consid´ er´ ee).
Variante: soient S un ensemble de places ﬁnies de k et OS l’anneau des S-entiers de
k. De fa¸ con peut-ˆ etre artiﬁcielle, mais commode, on peut d´eﬁnir la cat´ egorie tannakienne
MT(OS) de motifs de Tate mixte sur OS comme une sous-cat´ egorie de MT(k). Voir 1.6.
Autre variante: par descente d’une extension de k ` a k, on d´ eﬁnit la cat´ egorie tan-
nakienne MAT( k) des motifs d’Artin-Tate mixte, qui deviennent de Tate mixt e sur une
extension ﬁnie de k. Elle contient celle des motifs d’Artin (repr´ esentations rationnelles de
Gal(¯k/k)).
Dans Deligne (1989), l’un de nous a d´ eﬁni, pour certaines va ri´ et´ es alg´ ebriquesX
sur k, un “syst` eme de r´ ealisations” du groupe fondamental π1(X, 0) rendu unipotent:
une alg` ebre de Hopf commutative dans une cat´ egorie de Ind- syst` emes de r´ ealisations –
ou plutˆ ot son spectre. Si X est unirationelle, nous construisons un groupe fondamenta l
rendu unipotent motivique π1(X, 0)mot: une alg` ebre de Hopf commutative dans la cat´ egorie
Ind-MAT(k), des Ind-objets de MAT( k) dont la pr´ ec´ edente se d´ eduise par application
du foncteur r´ ealisation. Ceci implique des bornes sup´ eri eures sur la taille de l’action de
Galois sur le compl´ et´ eℓ-adique du π1 (cf. Hain, Matsumoto (2001)), et sur le degr´ e de
transcendance de corps engendr´ es par des p´ eriodes.
Nous consid´ erons aussi le cas de points base “` a l’inﬁni”. N ous le faisons ` a peu de
frais, en utilisant que le foncteur “r´ ealisations” est ple inement ﬁd` ele et r´ eﬂ` ete les sous-
quotients: pour prouver qu’un syst` eme de r´ ealisations est motivique, i.e. provient d’un objet
de MAT(k), il suﬃt de l’exhiber comme sous-quotient d’un autre syst` eme de r´ ealisations
1
dont on sache d´ ej` a qu’il est motivique.
Dans la ﬁn de l’article, nous utilisons ces constructions da ns le cas o` u X est le
compl´ ement, dans P1, de 0, ∞ et du groupe µN des racines N i` emes de l’unit´ e. Nous
obtenons des r´ esultats sur la structure de l’action du grou pe de Galois motivique sur
le π1. Pour N = 1, ils impliquent les r´ esultats de Terasoma (2002) donnan t la partie
“borne sup´ erieure” de la conjecture de Zagier sur le nombre de valeurs multizˆ eta de poids
w lin´ eairement ind´ ependantes surQ.
2
1. Motifs de T ate mixte sur l’anneau des S-entiers d’un corps de nombres.
1.1. Soit k un corps. Nombre de r´ esultats cit´ es d´ ependant de la r´ esolution des singularit´ es,
nous supposons k de caract´ eristique 0. Hanamura (1995), Levine (1998) et Vo evodsky
(2000) ont chacun d´ eﬁni une cat´ egorie triangul´ ee de motifs sur k, et Levine (1998) VI 2.5.5
construit une ´ equivalence entre sa cat´ egorie triangul´ ee et celle de Voevodsky. Cette derni` ere
sera pour nous la plus commode. Nous la noterons DM( k) et noterons DM( k)Q celle qui s’en
d´ eduit par tensorisation avec Q. On dispose dans DM( k) d’objets de Tate Z(n) ( n ∈ Z),
dont les images dans DM( k)Q seront not´ eesQ(n). Seule nous importera la sous-cat´ egorie
triangul´ ee DMT(k)Q de DM( k)Q engendr´ ee par les Q(n): celle des “extensions it´ er´ ees”
de Q(n)[m]. Rappelons que E est extension de B par A s’il existe un triangle distingu´ e
A → E → B → A[1].
On dispose dans DM( k) d’un produit tensoriel associatif et commutatif ` a unit´ e ⊗,
compatible ` a la structure triangul´ ee. L’automorphisme d e sym´ etrie de Z(1) ⊗ Z(1) est
l’identit´ e (Voevodsky (2000) 2.1.5), M ↦→M (1) := M ⊗ Z(1) est une ´ equivalence (loc.
cit. 4.1.3), et Z(n) est Z(1)⊗n (n ∈ Z). Le produit tensoriel ⊗ est rigide (loc. cit. 4.3.7):
existence pour tout objet M d’un dual M ∗ muni de ev: M ∗ ⊗ M → Z(0) et δ: Z(0) →
M ⊗ M ∗ tels que les compos´ esM → M ⊗ M ∗ ⊗ M → M et M ∗ → M ∗ ⊗ M ⊗ M ∗ → M ∗
soient l’identit´ e.
Rappelons, d’apr` es Levine (1993), comment, lorsque la con jecture d’annulation de
Beilinson Soul´ e est v´ eriﬁ´ ee pourk, on peut extraire de DMT( k)Q une cat´ egorie tannakienne
MT(k) qui m´ erite le nom de cat´ egorie des motifs de Tate mixte sur k.
Ecrivons Hom j(M, N ) pour Hom( M, N [j]). Les Hom ∗(Z(a), Z(b)) ne d´ ependant que
de i = b−a. Ils sont donn´ es par les groupes de Chow sup´ erieurs convenablement num´ erot´ es
de Spec( k) (loc. cit. 4.2.9 pour X = Spec( k)). Pour i < 0 ils sont nuls. Pour i = 0,
Homj(Z(0), Z(0)) = Z si j = 0,
0 sinon .(1.1.1)
Pour i = 1,
Homj(Z(0), Z(1)) = k∗ si j = 1,
0 sinon .(1.1.2)
3
Apr` es tensorisation avec Q, ces groupes sont encore donn´ ees par les sous-espaces pro-
pres des op´ erations d’Adams dans les groupes de K-th´ eorie dek (Levine (1998) II 3.6.6;
r´ ef´ erence originale: Bloch (1986) compl´ et´ e par Bloch (1994); voir aussi Levine (1994)). La
conjecture d’annulation de Beilinson-Soul´ e est que
(1.1.3) Hom j(Q(0), Q(i)) = 0 pour i > 0 et j ≤ 0.
Lorsque tel est le cas, Beilinson Bernstein Deligne (1982) 1 .3.14, appliqu´ e ` a la sous-cat´ egorie
pleine de DMT( k)Q d’objets les Q(n), montre que les extensions it´ er´ ees deQ(n) ( n ∈ Z)
forment une cat´ egorie ab´ elienne, coeur d’unet-structure sur DMT( k)Q. On l’appelle la
cat´ egorie MT(k) des motifs de Tate mixte sur k. Elle est stable par produit tensoriel et
passage au dual. Ces foncteurs ´ etant exacts, cela r´ esultede ce que Q(n)⊗Q(m) = Q(n+m)
et que Q(n)∗ = Q(−n). On obtient ainsi sur MT( k) un produit tensoriel exact en chaque
variable, associatif, commutatif, ` a unit´ e et rigide.
De ce que MT( k) est le coeur d’une t-structure sur DMT( k)Q r´ esulte que pourA et
B dans MT( k), on a
Ext1(A, B) = Hom 1(A, B) et(1.1.4)
Ext2(A, B)֒→Hom2(A, B).(1.1.5)
En particulier,
(1.1.6) Ext 1(Q(n), Q(m)) = 0 pour m ≤ n.
Pour A dans MT( k), il r´ esulte de (1.1.6), par induction sur une description de A comme
extension it´ er´ ee, queA admet une unique ﬁltration “par le poids” W , ﬁnie, croissante et
index´ ee par les entiers pairs, telle que
GrW
−2n(M ) := W−2n(M )/W−2(n+1)(M )
soit une somme de copies de Q(n). Posons
ωn(M ) := Hom( Q(n), GrW
−2n(M )).
4
On a donc
GrW
−2n(M ) = Q(n) ⊗Q ωn(M ).
La ﬁltration W est fonctorielle, exacte et compatible au produit tensorie l. Parce que
l’automorphisme de symm´ etrie deQ(1) ⊗ Q(1) est l’identit´ e, on dispose d’isomorphismes
Q(n) ⊗ Q(m) ∼− →Q(n + m) compatibles ` a l’associativit´ e et ` a la commutativit´ e de ⊗. Le
foncteur exact M ↦→ω(M ) := ⊕ωn(M ) est donc un ⊗-foncteur: c’est un foncteur ﬁbre et
la cat´ egorieM T(k) est tannakienne.
