---
doc_id: equations-aux-q-differences
doc_title: "´Equations aux q-diﬀ´erences"
section_id: sec-017-35-classiﬁcation-locale-des-equations-irregulier
section_title: "Classiﬁcation locale des ´ equations irr´eguli`eres"
section_number: 3.5
pages: 17-18
source_pdf: Equations_aux_q-differences.pdf
source_sha256: 357d4e0b546b27e6
doc_brief: "Équations aux q-différences — 28 sections: Di Vizio, J-P. Ramis, J. Sauloy ∗,; Introduction; L. DI VIZIO, J.-P. RAMIS, J. SAULO"
---
Nous consid´erons ici une ´equation
P.f(x)= a0(x)f(qnx)+ a1(x)f(qn−1x)+ ··· + an(x)f(x)=0
`a coeﬃcients analytiques, que nous ne supposons plus fuchsienne. Nous sup-
poserons cependant, pour simpliﬁer, que toutes les pentes de son polygone de
Newton sont enti`eres. On trouvera alors dans [Zha99] et dans [MZ00] la preuve
de l’existence d’une factorisation analytique de l’op´erateur P en facteurs de
degr´e 1. Ce r´esultat est ´etonnant, compar´e`a ce que l’on sait des op´erateurs
diﬀ´erentiels : pour ceux-ci, on ne peut esp´erer en g´en´eral qu’une factorisation
formelle. Ce th´eor`eme de factorisation n’est autre qu’une version moderne et
pr´ecis´ee du « canonical system » mentionn´ep a rB i r k h o ﬀ .
Une variante ab´elienne de ce th´eor`e m ed i tq u el em o d u l ea u xq-diﬀ´erences
correspondant admet une ﬁltration canonique ` a quotients purs de pentes
d´ecroissantes ([Sau02a] et [Sau02b]). On montre mˆeme que le gradu´e associ´e
est l’unique invariant formel. Ces r´esultats sont d’ailleurs valables sans sup-
poser les pentes enti`eres. La classiﬁcation des sommes directes de modules
purs est ais´ee `a partir de ce que nous avons vu sur les modules fuchsiens :
on retrouve ainsi la classiﬁcation formelle obtenue par Praagman ([Pr83],
[vdPS97]). La d´etermination des classes analytiques isoformelles revient alors
`al ad ´etermination des classes de modules ﬁltr´es `ag r a d u ´eﬁ x ´e.
Concr`etement, un module M de gradu´e associ´e:
gr(M)= M1 ⊕···⊕ Mk,
(Mi est pur de rang ri,d ep e n t eµi)p e u tˆetre d´ecrit par un syst`eme dont la
matrice A est triangulaire sup´erieure par blocs. Notons A1,...,A k ses blocs
SMF – Gazette – 96, Avril 2003
´EQUATIONS AUX q-DIFF´ERENCES 37
diagonaux. La matrice Ai est de rang ri et le syst`eme de matrice Ai est associ´e
au module pur Mi. Comme nous avons suppos´e les pentes enti`eres, on peut
mˆeme exiger que Ai soit de la forme xµi × une matrice de GLri (C). Avec ces
notations, un isomorphisme respectant la graduation deM vers un module M ′
(associ´e`al am a t r i c eA′) est donn´e par une matriceF telle que (σqF)A = A′F,
et, de plus, triangulaire sup´erieure par blocs et dont les blocs diagonaux sont
Ir1 ,...,I rk .
Exemple 3.11.
Le module `a deux pentes correspondant ` al am a t r i c ed ’ ´equation Au(x)=(1 u
0 x
)
est formellement isomorphe `a son gradu´e, autrement dit, il existe une
transformation de jauge formelle Fu(x) telle que Fu(qx)Au(x)= A0(x)Fu(x).
Si l’on exige de plus que l’isomorphisme soit compatible `a la graduation, c’est-
`a-dire que Fu soit de la forme
(
1 ˆyu
01
)
,i lyam ˆeme unicit´ed el as ´erie formelle
ˆyu, qui doit alors satisfaire l’´equation fonctionnelleˆyu(x)= u(x)+ xˆyu(qx). On
v´eriﬁe que deux telles matrices Au et Av sont analytiquement isomorphes si et
seulement si ˆyu − ˆyv est convergente. Par exemple, ˆy1 n’est autre que la s´erie
de Tschakaloﬀ cit´ee dans l’introduction, qui diverge, de sorte que A1 n’est pas
isomorphe `a A0. Nous reverrons cette s´erie au paragraphe 4. 2
En vue de d´ eﬁnir les « essential transcendental invariants » demand´es
par Birkhoﬀ, on est donc conduit, comme dans la th´ eorie des ´equations
diﬀ´erentielles, `a´etudier les moyens de sommer de telles s´ eries divergentes :
c’est l’objet du paragraphe 4.
