---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: sec-011-31-the-case-of-the-canonical-trace-in-this-secti
section_title: "The case of the canonical trace. In this section we consider the action of Sq"
section_number: 3.1
pages: 8-10
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
on (CN )⊗q by permutation of the factors in the tensor product. This rep resentation
plays a key role in the treatment by Schur and Weyl of the repre sentation theory
of both symmetric and general linear groups [W]. We consider the decomposition
of this representation into isotypic components
(CN )⊗q =
⨁
λ ∈Yq
Eλ
then the relative dimensions dimEλ
N q deﬁne a probability measure on Yq. Let Π q
be the image of this probability measure on Yq ⊂ CY by the scaling map ω ↦→
q−1/ 2ω (q1/ 2. ). Thus Π q is a probability measure on the set CY of continuous Young
diagrams.
Let arcsin take values in [ −π/ 2, +π/ 2] and arccos in [0 ,π ], and deﬁne
h(c,u ) = 2
π
(
u arcsin
[ u +c
2√1 +uc
]
+ 1
c arccos
[ 2 +uc −c2
2√1 +uc
]
+ 1
2
√
4 − (u −c)2
)
for 0 <c< ∞, and u ∈ [c − 2,c + 2]. Let us denote by Pc, the continuous diagram
given by the formula
(3.1.1)
P0(u) =
{ 2
π (u arcsin(u
2 ) +
√
4 −u2) if u ∈ [−2, +2]
|u| if u /∈ [−2, +2]
Pc(u) =
{
h(c,u ) if u ∈ [c − 2,c + 2]
|u| if u /∈ [c − 2,c + 2]
for 0 <c< 1
P1(u) =
{
u+1
2 + 1
π
(
(u − 1) arcsin(u−1
2 ) +
√
4 − (u − 1)2
)
if u ∈ [−1, 3]
|u| if u /∈ [−1, 3]
Pc(u) =



u + 2
c if u ∈ [− 1
c,c − 2]
h(c,u ) if u ∈ [c − 2,c + 2]
|u| if u /∈ [− 1
c,c + 2]
for c> 1
APPROXIMATE F ACTORIZATION AND CONCENTRATION 9
The diagrams are depicted below for various values of c.
−2 −1 0 1 2 3 4
0
0.5
1
1.5
2
2.5
3
3.5
4
c=0
c=1/2
c=1
c=2
The limit result for the Π q is the following.
Theorem 3. As q → ∞ and √q/N → c ∈ [0, +∞[, the measure Πq converges
uniformly, in probability, towards the Dirac measure at the continuous diagram Pc.
Proof. The character of the tensor representation can be computed i n the basis
ei1 ⊗... ⊗eiq , where ei is a basis of CN , one gets, for ρ ∈Sq,
tr(ρ) = Nc(ρ)−q =N −|ρ|
This is a positive deﬁnite function on Sq. Taking N =N (q) such that √q/N →c ∈
[0, +∞[, we see that the corresponding functions belong to Fn
c, 0 for all n, where the
sequence (cl =Cl)l≥1, with C = supq{√q/N (q)}, therefore we can apply Theorem
1 and 2, and Corollary 1 to see that under Π q, the sequence of cumulants of a ran-
dom diagram converges in probability towards the sequence ( 0, 1,c,c 2,...,c n,... ),
and the sequence of moments converges towards the correspon ding moments. The
correspondence between measures and diagrams given by (1.1 ) has the following
continuity property (see [K]):
if ω ∈ CY , then for all ε > 0 there exists n and δ such that, if ω ′ ∈ CY and
|ml(ω ) −ml(ω ′)|<δ for all l ≤n, then |ω (u) −ω ′(u)|<ε for all u ∈ R.
Therefore it is enough to check that the sequence (0 , 1,c,c 2,... ,c n,... ) is the
sequence of cumulants of the diagram Pc. For c = 0, Pc is the diagram correspond-
ing to the semi-circle distribution (see [K]), while for c >0 the constant sequence
(c−2,... ,c −2,... ) is the sequence of cumulants of the so-called Pastur-Marce nko
or free Poisson distribution (see [PM], or [VDN]), with para meter c−2. Taking the
image of this measure by the mapping x ↦→cx − 1
c yields the measure with free
cumulant sequence (0, 1,c,c 2,c 3... ). We shall now compute the corresponding dia-
gram, according to [K]. The R-transform with cumulant sequence (0, 1,c,c 2,c 3,... )
