---
doc_id: arxiv-1707.00196v3
doc_title: "Yang-Baxter representations of the inﬁnite symmetric group"
section_id: sec-007-42-parameterization-by-pairs-of-young-diagrams
section_title: "Parameterization by pairs of Young diagrams"
section_number: 4.2
pages: 20-22
source_pdf: 1707.00196v3.pdf
source_sha256: 9908b71521275b17
toc_source: outline
doc_brief: "Yang-Baxter representations of the inﬁnite symmetric group — Every unitary involutive solution of the quantum Yang-Baxter equation (R- matrix) deﬁnes an extremal character and a representation of the"
---
Parameterization by pairs of Young diagrams
The correspondence in Thm. 4.7 classiﬁes the family of Yang-Baxter characters, but
it does not classify R0/∼because the dimension of the base space is not recorded
in the Thoma parameters. However, it is now easy to incorporate the dimension as
well: Given R ∈R0 with Thoma parameters (α, β) and dimension d, we switch to the
rescaled Thoma parameters
ai := dαi,
bi := dβi.
(4.13)
By Thm. 3.7, the ai, bi are integers summing to d. We can therefore view (a, b) as
an ordered pair of integer partitions, or, equivalently, Young diagrams. Denoting the
set of all Young diagrams (with an arbitrary number of boxes) by Y, we arrive at the
following theorem, which in particular implies Thm. I from the Introduction.
Theorem 4.8.
i) R0/∼is in one to one correspondence with Y × Y\{(∅, ∅)} via mapping [R] to
the pair (a, b) (4.13). Classes of R-matrices of dimension d correspond to pairs
of Young diagrams with d boxes in total.
ii) Let R ∈R0. The eigenvalues of ptr R lie in {±1, ±2, . . . , ±d} and for each
eigenvalue λ, there exists nλ ∈N such that its multiplicity is nλ · |λ|. Deﬁne
an integer partition a as the ordered set of positive eigenvalues, in which λ is
repeated nλ times, and analogously for b and the negative eigenvalues. Then R
corresponds to (a, b) via the bijection in part i).
Proof. i) If R, S ∈R0 are equivalent, they have the same dimension d and the same
Thoma parameters (α, β) and hence the same rescaled parameters (4.13). Conversely,
if R, S ∈R0 have the same parameters (a, b), they have the same dimension d =
P
i(ai + bi) and therefore the same Thoma parameters, i.e. R ∼S. This also shows
the claim about the dimension, and that all pairs of Young diagrams with the exception
of (∅, ∅) occur.
ii) We may switch from R to its normal form N (with dimensions d±), which has
the same partial trace ptr N ∼= ptr R. Repeated application of Lemma 4.2 iv) shows
ptr N = L
i ptr(1d+
i ) ⊕L
i ptr(−1d−
i ). But ptr(±1d±
i ) = ±d±
i idi,±, where idi,± is the
identity matrix on Cd±
i . Hence the eigenvalues of ptr R are precisely the numbers ±d±
i .
The eigenvalue ±d±
i has multiplicity nd±
i · d±
i , where nd±
i is the number of times that
d±
i occurs in d±.
In view of (4.10) and (4.13), the rescaled Thoma parameters of N are exactly
ai = d+
i , bi = d−
i . As d±
i occurs nd±
i times in this list, the proof is ﬁnished.
To illustrate the correspondence with ordered pairs of Young diagrams, let us list
all normal forms of dimension two in terms of box sums and diagrams:
12
−12
11 ⊞11
−11 ⊞−11
11 ⊞−11
(
, ∅)
(∅,
)
( , ∅)
(∅, )
( , )
From left to right, these R-matrices (in End(C4)) are: 1) the identity, 2) the negative
identity, 3) the ﬂip, 4) equivalent to the negative ﬂip, and 5)
11 ⊞−11 =




1
1
1
−1



.
20
As a higher dimensional example, consider (
,
). This R-matrix has dimension 8
(the number of boxes) and Thoma parameters α = (3
8, 1
8), β = (1
4, 1
4).
The rescaled Thoma parameters are also useful for describing the ⊞operation
introduced in Sect. 4.1. We have already seen that ⊞gives R0 the structure of an
abelian semigroup and preserves equivalence, i.e., descends to the quotient R0/∼.
Recalling the eﬀect of ⊞on the level of Thoma parameters (Prop. 4.4 ii)), it becomes
apparent that for the rescaled parameters, we have
(a, b) ⊞(a′, b′) = (a ∪a′, b ∪b′),
(4.14)
where a ∪a′ denotes the partition whose parts are the union of those of a and a′.
Another operation on R is the tensor product of R-matrices.
For R ∈R(V ),
S ∈R(W), we deﬁne R ⊠S ∈R(V ⊗W) by
R ⊠S = F2(R ⊗S)F2 : V ⊗W ⊗V ⊗W →V ⊗W ⊗V ⊗W,
(4.15)
where F2 exchanges the second and third tensor factors. It is evident that ⊠preserves
the Yang-Baxter equation and involutivity, i.e. it deﬁnes a product on R and R0.
Lemma 4.9. Let R, R′ ∈R0 have rescaled Thoma parameters (a, b) and (a′, b′), re-
spectively. Then the rescaled Thoma parameters of R ⊠R′ are the non-increasing
arrangements of
{ˆaij} = {aia′
j, bib′
j},
{ˆbij} = {aib′
j, bia′
j}.
(4.16)
Proof. With d, d′ the dimensions of R, R′, we have on an n-cycle, n ≥2,
(d · d′)nχR⊠R′(cn) = Tr(V ⊗W )⊗n((R ⊠R′)1 · · · (R ⊠R′)n−1)
= TrV ⊗n(R1 · · · Rn−1) TrW ⊗n(R′
1 · · · R′
n−1)
= dnχR(cn) · (d′)nχR′(cn)
=

X
i
an
i + (−1)n+1 X
j
bn
j


 X
k
(a′
k)n + (−1)n+1 X
l
(b′
l)n
!
=
X
i,k
(aia′
k)n +
X
j,l
(bjb′
l)n + (−1)n+1

X
i,l
(aib′
l)n +
X
j,k
(bja′
k)n

,
and the claim follows.
It follows that ⊠deﬁnes an associative commutative product on R0/∼for which
the class [11] = ( , ∅) (consisting of the identity R-matrix in dimension d = 1) is the
unit, that is, R0/∼has a second unital abelian semigroup structure.
From the description of ⊠and ⊞in terms of the rescaled Thoma parameters, it is
evident that they satisfy the distributive law
([R] ⊞[S]) ⊠[T] = ([R] ⊠[T]) ⊞([S] ⊠[T]) ,
R, S, T ∈R0 .
(4.17)
These operations give R0/∼the structure of a semiring, sometimes also referred to as a
rig (ring without negatives). Additionally, the multiplication rules for rescaled Thoma
parameters in Lemma 4.9 can be generalized to a λ-operation. This λ-operation is
21
most easily described using symmetric polynomials and we therefore postpone it until
Sect. 5.2. The consequences of the ring and λ structures of R0/∼will be an interesting
topic of further study. For example, can the λ operation be directly interpreted in
terms of R and its base space V without reference to rescaled Thoma parameters?
As yet another operation on R, we brieﬂy mention the cabling procedure known
from the braid groups, applied to the Yang-Baxter equation by Wenzl [41]: Given any
p ∈N, one can form cabling powers Rc(p), which lie in R (or R0) if R does. We do
not give details here because it turns out that Rc(p) ∼R⊠p for all R ∈R0, p ∈N.
