---
doc_id: arxiv-2605.28781v1
doc_title: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS"
section_id: sec-010-4-the-construction
section_title: "The construction"
section_number: 4
pages: 9-11
source_pdf: 2605.28781v1.pdf
source_sha256: eee6d535af1996ca
doc_brief: "THE SUM-PRODUCT CONJECTURE IS FALSE FOR REAL NUMBERS — We disprove the sum-product conjecture for real numbers by con- structing arbitrarily largeA⊂R(whose elements are algebraic integers in a number"
---
In this section we use the algebraic number theory facts of the previous section
to prove Theorems 1.2 and 1.4.
Lemma 4.1.There exists an absolute constantc>0such that the following holds.
LetKbe a totally real number field of degreed≥2with discriminant∆ K and let
X,Y≥2. There exists a setA⊂O K such that
(cXY) d
Y∆ 3/2
K
≤|A|≤(XY/c) d,
|AA|≤c −dY 1−d∆2
K|A|2,
and
|A+A|≤(e Y/c)d∆1/2
K |A|.
Theorem 1.2 is an immediate consequence, lettingKbe a totally real field of
sufficiently large degreed≥2 with ∆ K≤C d for some absolute constantC >0, as
provided by Theorem 3.2, and choosingY= 4C 2c−1, say.
Proof.Without loss of generality, we can assume thatXandYare both sufficiently
large (in absolute terms), and thatXis an integer. LetG=B ×(Y), so that by
Lemma 3.5 and Lemma 3.1
Yd−1d−1/2∆−1
K ≤Y d−1d−1/2R−1
K ≤|G|≤10(5Y+ 1) d−1.
SinceGG⊆B ×(2Y),
|GG|≤(CY) d−1≤(C′)d∆K|G|
for some absolute constantsC,C ′ >0. Letϵ>0 be some small absolute constant
to be chosen soon, and
P=X+B +(ϵX),
10 THOMAS F. BLOOM, WILL SA WIN, CARL SCHILDKRAUT, AND DMITRII ZHELEZOV
so that by Lemma 3.3
(ϵX)d∆−1/2
K ≤|P|≤(2ϵX+ 1) d.
LetA=GP. We first claim that|A|=|G||P|, for which it suffices to prove
that ifu 1/u2 =p 1/p2 withu i∈Gandp i∈Pthenu 1 =u 2. This follows since
u1/u2∈O×
K, and for all embeddingsσandp∈P,
σ(p)∈[X−ϵX,X+ϵX],
whence
1−ϵ
1 +ϵ ≤σ(p 1/p2)≤ 1 +ϵ
1−ϵ .
Hence, providedϵ>0 is sufficiently small andXis sufficiently large (which we can
assume without loss of generality),σ(p 1/p2)∈(ϕ −1,ϕ). So by Lemma 3.4 we have
u1/u2∈{±1}, and in factu 1/u2̸=−1 since otherwiseσ(p 1/p2) =−1. Therefore
there exist constants 0<c<Csuch that
(cXY) d
Y∆ 3/2
K
≤|A|≤(CXY) d.
For the product set, we note (using the trivial bound|PP|≤|P| 2)
|AA|≤|GG||PP|≤c −dY 1−d∆2
K|A|2.
Finally, everyα∈Ais an algebraic integer such that|σ(α)|≤2Xe Y for allσ, and
henceA+A⊆B +(4XeY ). By Lemma 3.3
|A+A|≤(Ce YX)d≤(C′eY )d∆1/2
K |A|
(using|A|≥|P|≥(ϵX) d∆−1/2
K ) for some absolute constantsC,C ′ >0.□
A similar construction works for the proof of Theorem 1.4 – in fact here the
construction is even simpler, since we can just takeA=B ×(Y).
Lemma 4.2.There exists an absolute constantc>0such that the following holds.
LetKbe a totally real number field of degreed≥2with discriminant∆ K and let
Y≥2. There exists a setA⊂O K such that
(cY)d
Y∆ 3/2
K
≤|A|≤(Y/c) d
and
max(|kA|,|A (k)|)≤(ke Y/c)d for anyk≥2.
Once again, Theorem 1.4 is an immediate consequence, lettingKbe a totally
real number field of large degreedwith ∆ K≤C d for some constantC >0 and
choosingY= (C ′)1/ϵ for some other constantC ′, so that
max(|kA|,|A (k)|)≤(ke Y/c)d≤|A| C1/ϵ+ϵlogk .
This proves the second statement; to prove the first takeϵ=C/log logkfor some
sufficiently large constantC >0 (note that the choice ofAthen depends onk).
THE SUM-PRODUCT CONJECTURE IS F ALSE FOR REAL NUMBERS 11
Proof.We argue as in the previous lemma, except that we simply takeA=G=
B×(Y), so that by Lemma 3.5 and Lemma 3.1
Yd−1d−1/2∆−1
K ≤|A|≤10(5Y+ 1) d−1.
For anyk≥2, sinceA (k)⊆B×(kY),
|A(k)|≤(CkY) d−1
for some absolute constantC >0. Furthermore,A⊆B +(eY ), and hencekA⊆
B+(keY ), so
|kA|≤(Cke Y )d.□
