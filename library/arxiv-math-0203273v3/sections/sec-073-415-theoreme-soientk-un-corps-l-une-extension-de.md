---
doc_id: arxiv-math-0203273v3
doc_title: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéa"
section_id: sec-073-415-theoreme-soientk-un-corps-l-une-extension-de
section_title: "Th´eor`eme. SoientK un corps, L une extension de K,V unL-espace vec-"
section_number: 4.1.5
pages: 24-25
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
doc_brief: "NILPOTENCE, RADICAUX ET STRUCTURES MONO ÏDALES YVES ANDRÉ ET BRUNO KAHN AVEC UN APPENDICE DE PETER O’SULLIVAN TABLE DES MATI ÈRES Introduction 3 I. Radicaux et nilpotence 7 1. Idéaux et radicaux 7 — 3"
---
toriel de dimension ﬁnie, et A une sous-K-alg`ebre deEndL(V ). On suppose que,
pour tout a∈ A, le polyn ˆome caract´eristique de a dansV est `a coefﬁcients dans
K. Alors
a) Le radicalR deA est nilpotent d’´echelon≤n = dimV .
b) SiK est inﬁni,A/R est semi-simple, produit d’au plusn composants simples. Si
de plusK est parfait,A/R est s´eparable.
c) Supposons K inﬁni et parfait. Alors le radical de la sous- L-alg`ebre AL de
EndL(V ) engendr´ee par A est RL, on a RL∩A = R, et l’application canon-
ique (A/R)⊗KL→AL/RL est bijective.
12V oir§5 ci-dessous pour plus de d´ etails.
NILPOTENCE, RADICAUX ET STRUCTURES MONO ¨
IDALES 25
D´emonstration. a) D’apr` es [5,§11, ex. 1 a)],R est a priori un nil-id´ eal. Montrons
mˆ eme que toutu∈ R v´ eriﬁeun = 0 . Pour cela, il sufﬁt de voir que les valeurs
propres de u dansV sont toutes nulles. Supposons le contraire et soit λ⁄= 0 une
telle valeur propre. Commeλ est alg´ ebrique surK, il existe un polynˆ omeQ∈K[T ]
tel queλQ(λ) = 1 . Mais 1−uQ(u) est inversible, donc 1−λQ(λ) est inversible,
contradiction.
Comme l’image de R dans EndL(V ) est un semi-groupe multiplicatif form´ e
d’´ el´ ements nilpotents, un th´ eor` eme de N. Jacobson permet de conclure que R est
nilpotent d’´ echelon≤ dimV , cf. [51, 2.6.30].
b) Cela r´ esulte de [5,§11, ex. 1 d)].
c) Notons provisoirement RL le radical de AL. D’apr` es la proposition 4.1.1 b),
on a rad(A⊗K L) = R⊗K L, donc l’homomorphisme surjectif A⊗K L →
AL induit un homomorphisme surjectif (A/R)⊗K L→ AL/RL. Comme A/R
est s´ eparable etR nilpotent, le th´ eor` eme de Wedderburn (cf. th´ eor` eme 12.1.1 ci-
dessous, dans le cas d’un seul objet) permet de relever A/R dans A. Notons ce
relev´ eB, et soitK′ le centre d’un facteur simple deB :K′ est une extension ﬁnie
deK. Soitx un ´ el´ ement primitif deK′ : comme le polynˆ ome caract´ eristique dex
op´ erant surV est ` a coefﬁcients dansK, c’est n´ ecessairement une puissance du poly-
nˆ ome caract´ eristique dex op´ erant surK′. Ceci implique que la surjection K′⊗K
L→K′L est bijective, et donc queB⊗KL→BL est bijective. Il en r´ esulte que
A/R⊗KL→AL/RL est bijective, d’o` u l’on d´ eduitRL =RL. Enﬁn, (RL∩A =
)RL∩A =R d´ ecoule imm´ ediatement de la nilpotence deR. □
4.1.6. Remarques.
a) L’hypoth` ese queK est parfait n’est pas superﬂue dans b) et c). On obtient
un contre-exemple en prenant pour A = L une extension ﬁnie ins´ eparable
deK,V =L⊗KL avec la structure gauche deL-espace, et֒→EndL(V )
donn´ e parℓ↦→(ℓ1⊗ℓ2↦→ℓ1⊗ℓℓ2).
b) Si l’on suppose que V =⨁ Vi est un L-espace vectoriel gradu´ e et queA
est une sous-alg` ebre de∏ End(Vi), la borne sur l’´ echelon de nilpotencen
de R dans le point a) du th´ eor` eme 4.1.5 se rafﬁne en :n≤ max dimVi
(mˆ eme d´ emonstration).
c) Le point a) du th´ eor` eme 4.1.5 reste valable si on remplace l’hypoth` ese que
pour touta∈A, le polynˆ ome caract´ eristique dea est ` a coefﬁcients dansK
par : K est de cardinal strictement sup´ erieur ` adimKA, cf. [5, no. 12, ex.
16].
