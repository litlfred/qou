---
doc_id: arxiv-math-0203273v3
doc_title: "arXiv:math/0203273v3 [math.CT] 12 Oct 2002"
section_id: sec-025-b1-premiere-correction
section_title: "Premi`ere correction"
section_number: B.1
pages: 126-127
source_pdf: 0203273v3.pdf
source_sha256: 824715d110e34305
toc_source: inferred
---
sufﬁt de supposer que le corps de base k est de type ﬁni sur Fp.
B.1.1. Lemme. Soient H : Motrat →Modf-L une cohomologie de Weil classique
`a coefﬁcients dans une Q-alg`ebre commutative semi-simple L et MotH la cat´ego-
rie des k-motifs H-homologiques `a coefﬁcients rationnels. Pour tout A ∈MotH,
notons
H+(A) =
M
i pair
Hi(A), H−(A) =
M
i impair
Hi(A).
Alors, pour A, B ∈MotH, on a
RH(A, B) =
{f ∈MotH(A, B) | ∀g ∈MotH(B, A), ∀i ∈Z, trHi(g ◦f) = 0}
= {f ∈MotH(A, B) | ∀g ∈MotH(B, A), trH+(g ◦f) = trH−(g ◦f) = 0},
o`u RH est le radical de MotH.
D´emonstration. D’apr`es [1, prop. 5], MotH est semi-primaire, donc son radical de
Kelly co¨ıncide avec son radical de Gabriel. L’´enonc´e r´esulte alors du lemme 1.4.3.
□
B.1.2. Lemme. Avec les notations du lemme B.1.1, l’image r´eciproque snum de
RH dans la cat´egorie Motrat des motifs de Chow ne d´epend pas du choix de H.
D´emonstration. ´Etant donn´e le lemme B.1.1, il sufﬁt de voir que, pour toute k-
vari´et´e projective lisse X et toute correspondance c ∈CHdim X(X × X) et tout
i ∈Z, trHi(c) est un nombre rationnel qui ne d´epend pas de H. Par changement
de base propre et lisse et par sp´ecialisation des cycles alg´ebriques, on se r´eduit par
r´ecurrence sur le degr´e de transcendance de k sur Fp au cas o`u k est ﬁni (cf. [1, d´em.
de la prop. 5]). L’assertion r´esulte alors de [29].
□
NILPOTENCE, RADICAUX ET STRUCTURES MONO¨IDALES
127
B.1.3. Lemme (cf. [1, lemme 7]). Soient, pour ﬁxer les id´ees, ℓ̸ = ℓ′̸ = p deux nom-
bres premiers. Alors le noyau du foncteur Motℓℓ′ →Motℓest un id´eal localement
nilpotent.
D´emonstration. Cela r´esulte des lemmes B.1.1 et B.1.2.
□
B.1.4. Lemme. Les foncteurs pleins Motℓ→Motsnum, Motℓ′ →Motsnum in-
duisent des bijections sur les classes d’isomorphisme d’objets. En particulier, pour
tout objet M de Motℓ, bi(M) = dim Hi
ℓ(M) ne d´epend pas de ℓ, et ne d´epend que
de la classe d’isomorphisme de l’image de M dans Motsnum.
D´emonstration. Par le lemme B.1.3, ces foncteurs sont essentiellement surjectifs et
conservatifs.
□
B.1.5. Lemme. L’image M∗
snum de M∗
ℓdans Motsnum consiste en la sous-cat´ego-
rie pleine form´e des objets isomorphes `a des sommes ﬁnies d’objets n’ayant qu’un
seul nombre de Betti non nul. En particulier, M∗
snum est ind´ependant de ℓ. De mˆeme
avec M±.
D´emonstration. C’est clair par le lemme B.1.4, car on a la mˆeme propriet´e au
niveau de M∗
ℓ.
□
B.1.6. Lemme. M∗
snum = M∗
num et M±
snum = M±
num.
D´emonstration. C’est clair.
□
