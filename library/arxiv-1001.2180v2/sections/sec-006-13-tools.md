---
doc_id: arxiv-1001.2180v2
doc_title: "ASYMPTOTICS OF q-PLANCHEREL MEASURES"
section_id: sec-006-13-tools
section_title: "Tools"
section_number: 1.3
pages: 5-7
source_pdf: 1001.2180v2.pdf
source_sha256: f4225d7b024940aa
doc_brief: "ASYMPTOTICS OF q-PLANCHEREL MEASURES — In this paper, we are interested in the asymptotic size of the rows and columns of a random Young diagram under a natural deformation of the Plancherel measure"
---
2. The q-Plancherel measure
In this section, we deﬁne and present basic properties of the q-Plancherel measure. The characterization
given in paragraph 2.2 is the one which will be used in the next sections. The algebra ic interpretation of
paragraph 2.3 gives some motivation to consider at this measure.
Let us ﬁx some notations related to the representation theor y of Sn. If λ is a partition in Yn, it
corresponds to an irreducible Sn-module Sλ — the Specht module of type λ — whose dimension will be
denoted dim λ. We shall also denote ς λ the irreducible character of Sλ, and χλ the normalized character,
so that ς λ = (dim λ) χλ.
2.1. Deﬁnition. Let us recall the deﬁnition of Young graph ( cf. for example [ KOO98, p. 5]): its set of
vertices is the disjoint union Y = ⨆
n∈ /C6
Yn, and its edges are the pairs (λ, Λ) , where the Young diagram
Λ can be obtained by adding one box to the Young diagram λ (this situation will be denote λ ր Λ ). The
(standard) Plancherel growth process is the markovian part ition-valued process (λn)n∈ /C6
deﬁned by:
λ0 = ∅ ; p(λ, Λ) =
{
1
|Λ |
dim Λ
dim λ if λ ր Λ ,
0 otherwise.
Because of the branching rules for the symmetric groups, p(·, ·) is indeed a transition function on Y , and
the law of the n-th partition λn is the Plancherel measure on Yn:
/C8 [λn = λ] = /BD
|λ|=n
(dim λ)2
n! .
The q-Plancherel measures and the q-Plancherel process are natural q-analogs of these objects that have
been studied by Kerov [ Ker92] and more recently by Strahov [ Str08]. Recall that the dimension dim λ is
given by the hook length formula ( dim λ = n!/ ∏
/oblong∈λ h(/oblong), the hook length h(/oblong) of a box /oblong= (i, j) being
(λj − i) + (λ′
i − j) + 1). As a consequence, assuming that λ ր Λ , the transition probability p(λ, Λ) is a
quotient of hook products:
p(λ, Λ) =
∏
/oblong∈λ h(/oblong)
∏
/oblong∈Λ h(/oblong) .
S. Kerov has shown that one can deform the markovian process b y considering q-transition probabilities:
pq(λ, Λ) = qb(Λ) −b(λ)
∏
/oblong∈λ{h(/oblong)}q∏
/oblong∈Λ {h(/oblong)}q
,
where b(λ) = ∑ ℓ(λ)
i=1 (i − 1)λi and the q-analog {n}q of a positive integer is by deﬁnition qn−1
q−1 .
6 V ALENTIN FÉRAY AND PIERRE-LOÏC MÉLIOT
D = 1 ; M1,q = 1
1
q+1
q
q+1
D = 1 ; M2,q = 1/ (q + 1)M2,q = q/ (q + 1)
D = q
q2
q2+q+1
q+1
q2+q+1
q2+q
q2+q+1 1
q2+q+1
M3,q = (2q)/ (q2 + q + 1)
D = q2 + q
q3+q
q4+2q3+2q2+2q+1
D = q3
M3,q = q3/ (q3 + 2q2 + 2q + 1)q3
q3+q2+q+1
D = q6
M4,q = q6/ (q6 + 3q5 + 5q4
+6q3 + 5q2 + 3q + 1)
M3,q = 1/ (q3 + 2q2 + 2q + 1)
D = 1
D = q4 + q2
q2+q+1
q3+q2+q+1
q4+q3+q2
q4+2q3+2q2+2q+1
D = q3 + q2 + q
M4,q = (3q)/ (q4 + 2q3 + 2q2 + 2q + 1)D = q5 + q4 + q3
M4,q = (3q3)/ (q4 + 2q3 + 2q2 + 2q + 1)
1
q3+q2+q+1
D = 1
M4,q = 1/ (q6 + 3q5 + 5q4
+6q3 + 5q2 + 3q + 1)
M4,q = (2q2)/ (q4 + 3q3 + 4q2 + 3q + 1)
q3+q2+q
q3+q2+q+1
q2+q+1
q4+2q3+2q2+2q+1
Figure 3. Generic degrees, q-Plancherel measures and q-transition probabilities on di-
agrams of size n ≤ 4.
Deﬁnition - Proposition 1. The q-Plancherel process is the markovian partition-valued process (λn)n∈ /C6
deﬁned by:
λ0 = ∅ ; pq(λ, Λ) =
{
qb(Λ) −b(λ)
∏
/oblong∈λ{h(/oblong)}q∏
/oblong∈Λ {h(/oblong)}q
if λ ր Λ in the Young graph ,
0 otherwise.
Its marginal distribution of the n-th partition of the q-Plancherel process is called the q-Plancherel mea-
sure. This probability measure Mn,q on the set Yn of Young diagrams of size n can be alternatively deﬁned
by:
∀λ ⊢ n, M n,q({λ}) = Mn,q(λ) = Dλ(q) dim λ
{n!}q
,
where dim λ is the dimension of the irreducible representation of Sn indexed by λ, and Dλ(q) is its generic
degree as deﬁned in [GP00, Chapter 8] :
Dλ(q) = qb(λ) {n!}q∏
/oblong∈λ{h(/oblong)}q
.
The equivalence between the two deﬁnitions (as marginal dis tribution of a markovian process or via a
direct formula for the probability to pick each diagram) is e xplained in [ Str08, Section 3].
In the next two paragraphs, we explain why this q-analog is natural in the context of Hecke algebras
and general linear groups in ﬁnite characteristic.
ASYMPTOTICS OF q-PLANCHEREL MEASURES 7
