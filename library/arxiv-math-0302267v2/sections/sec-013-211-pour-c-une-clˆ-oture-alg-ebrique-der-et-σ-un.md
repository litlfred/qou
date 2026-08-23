---
doc_id: arxiv-math-0302267v2
doc_title: "Groupes fondamentaux motiviques de Tate mixte"
section_id: sec-013-211-pour-c-une-clˆ-oture-alg-ebrique-der-et-σ-un
section_title: "Pour C une clˆ oture alg´ ebrique deR et σ un plongement de k dans C, ` a la th´ eorie"
section_number: 2.11
pages: 19-21
source_pdf: 0302267v2.pdf
source_sha256: c09c8cabd5f9d8e6
doc_brief: "Groupes fondamentaux motiviques de Tate mixte — We deﬁne the category of mixed Tate motives over the ring of S-integers of a number ﬁeld."
---
de cohomologie
X sur k ↦− →H ∗ (espace topologique X(C), Q)
correspond un foncteur ﬁbre M ↦→Mσ, fonctoriel en C. Parler de “plongement dans
C” plutˆ ot que de plongement complexe (i.e. dans C) a l’avantage que la fonctorialit´ e en
C fournit un isomorphisme Mσ → M¯σ. Pour un plongement r´ eel, i.e. pour σ = ¯σ, cet
isomorphisme est une involution de Mσ, le Frobenius r´ eel.
Un isomorphisme de comparaison canonique d’un foncteur ﬁbr e α vers un foncteur
ﬁbre β sera not´ e compβ,α, et son inverse comp α,β. La relation entre la cohomologie de de
Rham et la cohomologie singuli` ere fournit
(2.11.1) comp σ,DR: MDR ⊗k,σ C ∼− →Mσ ⊗Q C,
17
fonctoriel en C. Il induit
(2.11.2) comp σ,ω: Mω ⊗ C ∼− →Mσ ⊗ C
et permet de voir Mσ comme une Q-structure sur MDR ⊗k,σ C = Mω ⊗ C. On a
Q(1)σ = 2πiQ ⊂ C = Q(1)DR ⊗k,σ C
et donc Q(n)σ = (2 πi)nQ ⊂ C. Dans ces formules, le choix de la racine carr´ ee i de −1
n’importe pas.
On reconstitue la Q-structure Mω de l’espace vectoriel gradu´ eMDR ` a partir de Mσ
et comp σ,DR par
(2.11.3) ( Mω)n ⊂ (MDR)n ⊂ (MDR ⊗k,σ C)n est 1
(2πi)n compDR,σGrW
−2n(Mσ).
Ecrivons Gω = Gm⋉Uω pour Gω ⟨MT(k)⟩ et sa d´ ecomposition 2.5, etτ pour l’inclusion
de Gm dans Gω.
Proposition 2.12. Il existe aσ dans Gω(C) tel que
(2.12.1) Mσ = comp σ,ω(aσMω).
Si i est une racine carr´ ee de −1 dans C, on peut choisir les aσ de la forme
(2.12.2) aσ = a0
στ (2πi)
avec a0
σ ∈ Uω(C) et a0
¯σ = (a0
σ)−, d’o` u pour σ r´ eel,
(2.12.3) a0
σ ∈ Uω(R) (pour σ = ¯σ)
La preuve est la mˆ eme que celle de Deligne (1989) 8.10. Noter que (2.12.1) d´ etermine
aσ ` a multiplication ` a droite pr` es par un ´ el´ ement de Gω(Q). Choisissons i dans C. La
fonctorialit´ e enC montre que si aσ v’eriﬁe (2.12.1), alors ¯aσ v´ eriﬁe (2.12.1) pour ¯σ. Si
on impose ` a aσ d’ˆ etre de la forme (2.12.2), avec a0
σ dans Uω(C), alors ¯aσ = ¯a0
στ (−2πi) =
18
¯a0
στ (2πi)τ (−1) et ¯a0
σ est bien un choix possible pour a¯σ. Pour la v´ eriﬁcation qu’on peut
mˆ eme prendrea0
σ ∈ Uω(R) si σ = ¯σ, on renvoie ` a loc. cit. Si on impose ` a aσ d’ˆ etre de la
forme (2.12.2), son ind´ etermination est r´ eduite ` aUω(Q). Si σ est r´ eel et qu’on impose en
outre (2.12.3), elle est r´ eduite ` a
U +(Q) : = U (Q) ∩ τ (2πi)−1U (R)τ (2πi)
= exp
( ∏
u2n
)
.
