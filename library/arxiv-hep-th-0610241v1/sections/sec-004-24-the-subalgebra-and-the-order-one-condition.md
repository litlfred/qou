---
doc_id: arxiv-hep-th-0610241v1
doc_title: "Gravity and the standard model with neutrino mixing"
section_id: sec-004-24-the-subalgebra-and-the-order-one-condition
section_title: "The subalgebra and the order one condition"
section_number: 2.4
pages: 8-10
source_pdf: hep-th-0610241.pdf
source_sha256: 6a71ab6f6459c070
toc_source: inferred
doc_brief: "Gravity and the standard model with neutrino mixing — We present an eﬀective uniﬁed theory based on noncommutative geometry for the standard model with neutrino mixing, minimally coupled to gravity."
---
We let HF be the sum of N = 3 copies of the ALR-bimodule MF of Proposition 2.4, that is,
HF = M⊕3
F .
(2.17)
Remark 2.10. The multiplicity N = 3 here is an input, and it corresponds to the number
of particle generations in the standard model. The number of generations is not predicted by
our model in its present form and has to be taken as an input datum.
We deﬁne the Z/2-grading γF by
γF = c −JF c JF ,
c = (0, 1, −1, 0) ∈ALR.
(2.18)
One then checks that
J2
F = 1 ,
JF γF = −γF JF .
(2.19)
The relation (2.19), together with the commutation of JF with the Dirac operators, is char-
acteristic of KO-dimension equal to 6 modulo 8 (cf. Deﬁnition 2.7).
By Proposition 2.4 one can write HF as the direct sum
HF = Hf ⊕H ¯f
(2.20)
of N = 3 copies of E of (2.4) with the contragredient bimodule, namely
Hf = E ⊕E ⊕E,
H ¯f = E0 ⊕E0 ⊕E0.
(2.21)
The left action of ALR splits as the sum of a representation π on Hf and a representation π′
on H ¯f.
These representations of ALR are disjoint (i.e. they have no equivalent subrepresentations).
As shown in Lemma 2.12 below, this precludes the existence of operators D in HF that fulﬁll
the order one condition (2.11) and intertwine the subspaces Hf and H ¯f.
We now show that the existence of such intertwining of Hf and H ¯f is restored by passing to
a unique subalgebra of maximal dimension in ALR.
Proposition 2.11. Up to an automorphism of ALR, there exists a unique subalgebra AF ⊂
ALR of maximal dimension admitting an oﬀdiagonal Dirac operators, namely operators that
intertwine the subspaces Hf and H ¯f of HF. The subalgebra is given by
AF = {(λ, qL, λ, m) | λ ∈C , qL ∈H , m ∈M3(C)} ∼C ⊕H ⊕M3(C).
(2.22)
GRAVITY AND THE STANDARD MODEL WITH NEUTRINO MIXING
9
Proof. For any operator T : Hf →H ¯f we let
A(T) = {b ∈ALR | π′(b)T = Tπ(b) , π′(b∗)T = Tπ(b∗)}.
(2.23)
It is by construction an involutive unital subalgebra of ALR.
We prove the following preliminary result.
Lemma 2.12. Let A ⊂ALR be an involutive unital subalgebra of ALR. Then the following
properties hold.
1. If the restriction of π and π′ to A are disjoint, then there is no oﬀdiagonal Dirac
operator for A.
2. If there exists an oﬀdiagonal Dirac for A, then there exists a pair e, e′ of minimal
projections in the commutants of π(ALR) and π′(ALR) and an operator T such that
e′Te = T̸ = 0 and A ⊂A(T).
Proof. 1) First the order one condition shows that [D, a0] cannot have an oﬀdiagonal part
since it is in the commutant of A. Conjugating by J shows that [D, a] cannot have an oﬀ
diagonal part. Thus the oﬀdiagonal part Doff of D commutes with A i.e. [Doff, a] = 0, and
Doff = 0 since there are no intertwining operators.
2) By 1) the restrictions of π and π′ to A are not disjoint and there exists a non-zero operator
T such that A ⊂A(T). For any elements x, x′ of the commutants of π and π′, one has
A(T) ⊂A(x′Tx)
since π′(b)T = Tπ(b) implies π′(b)x′Tx = x′Txπ(b). Taking a partition of unity by minimal
projections there exists a pair e, e′ of minimal projections in the commutants of π and π′
such that e′Te̸ = 0 so that one can assume e′Te = T̸ = 0.
We now return to the proof of Proposition 2.11.
Let A ⊂ALR be an involutive unital subalgebra. If it admits an oﬀdiagonal Dirac, then
by Lemma 2.12 it is contained in a subalgebra A(T) with the support of T contained in a
minimal projection of the commutant of π(ALR) and the range of T contained in the range
of a minimal projection of the commutant of π′(ALR).
This reduces the argument to two cases, where the representation π is the irreducible represen-
tation of H on C2 and π′ is either the representation of C in C or the irreducible representation
of M3(C) on C3.
In the ﬁrst case the support E of T is one dimensional. The commutation relation (2.23)
deﬁnes the subalgebra A(T) from the condition λTξ = Tqξ, for all ξ ∈E, which implies
λξ −qξ = 0. Thus, in this case the algebra A(T) is the pullback of
{(λ, q) ∈C ⊕H | q ξ = λ ξ ,
∀ξ ∈E}
(2.24)
under the projection on C ⊕H from ALR. The algebra (2.24) is the graph of an embedding
of C in H.
Such an embedding is unique up to inner automorphisms of H.
In fact, the
embedding is determined by the image of i ∈C and all elements in H satisfying x2 = −1 are
conjugate.
The corresponding subalgebra AF ⊂ALR is of real codimension 4. Up to the exchange of
the two copies of H it is given by (2.22).
In the second case the operator T has at most two dimensional range R(T). This range is
invariant under the action π′ of the subalgebra A and so is its orthogonal since A is involutive.
Thus, in all cases the M3(C)-part of the subalgebra is contained in the algebra of 2 ⊕1 block
diagonal 3 × 3 matrices which is of real codimension 8 in M3(C). Hence A is of codimension
at least 8 > 4 in ALR.
10
CHAMSEDDINE, CONNES, AND MARCOLLI
It remains to show that the subalgebra (2.22) admits oﬀdiagonal Dirac operators.
This
follows from Theorem 2.21 below.
