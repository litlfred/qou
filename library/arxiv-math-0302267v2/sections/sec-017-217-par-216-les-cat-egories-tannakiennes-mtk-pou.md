---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-017-217-par-216-les-cat-egories-tannakiennes-mtk-pou
section_title: "Par 2.16, les cat´ egories tannakiennes MT(k), pour k variable, forment un pr´ echamp"
section_number: 2.17
pages: 24-28
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
sur le site ´ etale de Spec( Q). On note MAT le champ associ´ e et on appelle MAT( k) la
cat´ egorie des motifs d’Artin-Tate mixte surk. Explicitons cette d´ eﬁnition.
Soit k1 une extension galoisienne de k. Notons C(k1/k) la cat´ egorie des extensions
ﬁnies k′ de k dans lesquelles peut se plonger k1. Soit MAT( k1/k) la cat´ egorie des sections
de MT au-dessus de C(k1/k): la cat´ egorie des syst` emes d’objets M(k′) ∈ MT(k′) pour
k′ ∈ C(k1/k), et d’isomorphismes M(k′)(k′′)
∼− →M(k′′) pour k′ → k′′ dans C(k1/k), v´ eriﬁant
une compatibilit´ e pour k′ → k′′ → k′′′. La cat´ egorie MAT(k) est la limite inductive des
MAT(k1/k), pour C(k1/k) de plus en plus petit.
La ﬁltration par le poids des objets des MT( k′) ´ etant fonctorielle et compatible aux
extensions de corps de base, elle fournit une ﬁltration par l e poids sur chaque objet de
MAT(k1/k), ou de MAT( k).
La cat´ egorie MAT(k) h´ erite de MT(k′) de foncteurs ﬁbre ω, DR, σ et ℓ, et d’isomor-
phismes de comparaison.
Foncteur ﬁbre ω: le foncteur M = ( M(k′))k′∈C(k1/k) ↦→M(k1) est une ´ equivalence de
MAT(k1/k) avec la cat´ egorie des objets de MT( k1) munis d’une action semi-lin´ eaire de
Gal(k1/k) (donn´ ee de descente galoisienne). Cette donn´ ee de descente induit une action de
Gal(k1/k) sur ω(M ) := ω(M(k1)) et le groupe de Galois motivique Aut( ω) de MAT( k1/k)
est le produit semi-direct de Gal( k1/k) par le groupe de Galois motivique de MT( k1).
Soit ¯k une clˆ oture alg´ ebrique dek et passons ` a la limite sur k1 ⊂ ¯k. On d´ eﬁnit
ω(M ) := ω(M(k1)) pour k1 ⊂ ¯k assez grand .
Ce Q-espace vectoriel gradu´ e est muni d’une action continue de Gal(¯k/k).
22
Foncteur ﬁbre DR: d´ eﬁni par descente galoisienne ` a partir des foncteurs ﬁbres DR des
MT(k′). Pour M dans MAT(k1/k) et k′ ∈ C(k1/k), on a fonctoriellement en k′
MDR ⊗k k′ ∼− →(M(k′))DR,
et l’isomorphisme 2.10 fournit un isomorphisme de comparai son
MDR = (ω(M(k1)) ⊗ k1)Gal(k1/k).
Foncteur ﬁbre σ: pour σ un plongement de k dans une clˆ oture alg´ ebriqueC de R. C’est
Mσ := (M(k′))σ′
pour σ le compos´ ek ⊂ k′ σ′
֒− →C et k′ assez grand pour que M(k′) soit dans MT (k′).
Foncteur ﬁbre ℓ: il d´ epend du choix d’une clˆ oture alg´ ebrique¯k de k, et est d´ eﬁni comme
´ etant (M(k′))ℓ pour k′ ⊂ ¯k assez grand.
Cas particulier. Les objets purement de poids 0 de MT( k′), i.e. tels que Gr −2nW = 0 pour
n ⁄= 0, sont les sommes de copies de Q(0), et ω0 identiﬁe leur cat´ egorie ` a celle desQ-espaces
vectoriels. En cons´ equence, pour ¯k une clˆ oture alg´ ebrique dek, le foncteur ω identiﬁe la
cat´ egorie des objets purement de poids 0 de MAT( k) avec celle des Q-espaces vectoriels
munis d’une action continue de Gal( ¯k/k) (motifs d’Artin).
Soit k1 une extension galoisienne ﬁnie de k. Il r´ esulte de 2.16 que le foncteur MT(k) →
MAT(k1/k) est pleinement ﬁd` ele d’image essentielle stable par sous -objet. L’image essen-
tielle est aussi stable par extensions:
Proposition 2.18. Pour qu’un objet M de MAT(k1/k) soit dans MT(k), il faut et il suﬃt
que l’action de Gal(k1/k) sur ω(M ) soit triviale.
Si M est purement de poids 0, la proposition r´ esulte du “cas part iculier” ci-dessus.
Le cas o` u M est pur, i.e. purement d’un seul poids, en r´ esulte par tenso risation avec un
Q(n). Il reste ` a v´ eriﬁer une stabilit´ e par extensions.
23
1ere preuve. Une suite spectrale d’Hochschild-Serre fournit, pour M et N dans MT(k), des
isomorphismes
Extp
MAT(k1/k)(M, N ) ∼− →Extp(M(k1), N(k1))Gal(k1/k).
Pour v´ eriﬁer que
Extp
MT(k)(M, N ) → Extp
MAT(k′/k)(M, N ) = Ext p
MT(k1)(M(k1), N(k1))Gal(k1/k)
est bijectif pour p = 0, 1 et injectif pour p = 2, il suﬃt par d´ evissage de le v´ eriﬁer pour M
et N de la forme Q(m) et Q(n). Le cas p = 2 r´ esulte de la nullit´ e des Ext2, le cas p = 0
r´ esulte de ce que Hom = 0, sauf pour m = n, o` u End(Q(n)) = Q, et p = 1 est 2.16.
Plutot que de d´ eﬁnir la suite spectrale d’Hochschild-Serr e requise, on peut la para-
phraser:
2` eme preuve. Si M est une extension de Q(n) par Q(n + r), que M(k1) admette une donn´ ee
de descente de k1 ` a k, respectant la structure d’extension de Q(n) par Q(n + r), implique
que la classe de M(k1) dans Ext1
MT(k1)(Q(n), Q(n+r)) est ﬁxe sous Gal( k1/k). Elle provient
donc de la classe d’une extension ~M de Q(n) par Q(n+r) dans MT( k). On v´ eriﬁe, utilisant
que Hom MT(k1)(Q(n), Q(n + r)) = 0, que M est isomorphe ` a l’image de ~M .
Prouvons par r´ ecurrence surr ≥ 0 que 2.18 est vrai sous l’hypoth` ese additionnelle que
pour un n on ait M = W−2nM et W−2(n+r+1)M = 0.
Le cas o` u r = 0 ( M pur) a d´ ej` a ´ et´ e trait´ e. Le casr = 1 se r´ eduit ` a celui d’une extension
de Q(n) par Q(n + 1).
Pour r ≥ 1, l’hypoth` ese de r´ ecurrence assure que M ′ = M/W−2(n+r)M et M ′′ =
W−2(n+1)M proviennent de ~M ′ et ~M ′′ dans MT( k). Ce sont des extensions de la forme:
GrW
−2nM par N et N par Gr W
−2(n+r)M . Par nullit´ e des Ext2 dans MT( k), il existe dans
MT(k) un objet ~M , extension it´ er´ ee de GrW
−2nM par N par Gr W
−2(n+r)M , redonnant ~M ′
et ~M ′′. L’image de ~M dans MAT(k1/k) diﬀ` ere de M par une extension de Gr W
−2nM par
GrW
−2(n+r)M .
24
Cette derni` ere provient d’une extension dans MT( k), par r´ eduction au cas d’une ex-
tension de Q(n) par Q(n + r), et ceci permet de corriger ~M pour que son image devienne
isomorphe ` a M .
25
3. Cohomologie et groupe fondamental.
