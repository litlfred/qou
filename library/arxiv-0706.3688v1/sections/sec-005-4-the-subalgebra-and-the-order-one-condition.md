---
doc_id: arxiv-0706.3688v1
doc_title: "WHY THE STANDARD MODEL"
section_id: sec-005-4-the-subalgebra-and-the-order-one-condition
section_title: "The subalgebra and the order one condition"
section_number: 4
pages: 8-11
source_pdf: 0706.3688.pdf
source_sha256: f2a18b0defebff66
toc_source: outline
doc_brief: "WHY THE STANDARD MODEL — The Standard Model is based on the gauge invariance principle with gauge group U(1) × SU(2) × SU(3) and suitable representations for fermions and bosons, which are begging"
---
We take (A, H, J, γ) from the above discussion, i.e. (3.1) and Proposition 3.2.
The center of our algebra Z(A) is non-trivial and in that way the corresponding space
is not connected. We look for “Dirac operators” D which connect non-trivially the two
pieces (we call them “oﬀ-diagonal”) i.e. operators such that:
(4.1)
[D, Z(A)]̸ = {0}.
The main requirement on such operators is the order one condition (1.2). We now
look for subalgebras AF ⊂Aev, the even part of A, for which this order condition
WHY THE STANDARD MODEL
9
(∀a, b ∈AF) allows for operators which fulﬁll (4.1). We can now state our main result
which recovers in a more conceptual manner the main “input” of [7].
Theorem 4.1. Up to an automorphism of Aev, there exists a unique involutive sub-
algebra AF ⊂Aev of maximal dimension admitting oﬀ-diagonal Dirac operators. It is
given by
(4.2)
AF = {(λ ⊕q, λ ⊕m) | λ ∈C , q ∈H , m ∈M3(C)} ⊂H ⊕H ⊕M4(C) ,
using a ﬁeld morphism C →H. The involutive algebra AF is isomorphic to C ⊕H ⊕
M3(C) and together with its representation in (H, J, γ) it gives the noncommutative
geometry F of [7].
We now give the argument (which is similar to that of [7] Proposition 2.11). Let us
consider the decomposition of (2.10),
H = e1H ⊕e2H = H1 ⊕H2 .
We consider an involutive subalgebra AF ⊂Aev and let πj be the restriction to AF of
the representation of A in Hj. We have (cf. [7] Lemma 2.12),
Lemma 4.2. If the representations πj are disjoint, then there is no oﬀdiagonal Dirac
operator for AF.
Proof. By construction the projections ej are the minimal projections in Z(A) and
since Je1J−1 = e2, they are also the minimal projections in Z(A0). Moreover one has
πj(a) = aej = eja = ejaej ,
∀a ∈AF .
Let us assume that the representations πj are disjoint. For any operator T in H, one
has
(4.3)
[T, a] = 0 ,
∀a ∈AF ⇒[e1Te2, a] = 0 ,
∀a ∈AF ⇒e1Te2 = 0 ,
since any intertwining operator such as e1Te2 must vanish as the two representations
are disjoint. The same conclusion applies to e2Te1. Similarly one gets, after conjugating
by J,
(4.4)
[T, a0] = 0 ,
∀a ∈AF ⇒e1Te2 = e2Te1 = 0 .
(one has [JTJ−1, a] = 0 for all a ∈A hence e2JTJ−1e1 = 0 and e1Te2 = 0). Now let
the operator D satisfy the order one condition
(4.5)
[[D, a], b0] = 0
∀a, b ∈AF .
It follows from (4.4) that e1[D, a]e2 = 0 for all a ∈AF. Since the ej commute with a
this gives
[e1De2, a] = 0 ,
∀a ∈AF .
By (4.3) we thus get e1De2 = 0 and there is no oﬀdiagonal Dirac operator for AF.
□
For any operator T : H1 →H2 we let
(4.6)
A(T) = {b ∈Aev | π2(b)T = Tπ1(b) , π2(b∗)T = Tπ1(b∗)}.
It is by construction an involutive unital subalgebra of Aev.
10
CHAMSEDDINE AND CONNES
We now complete the proof of Theorem 4.1. We let AF ⊂Aev be an involutive sub-
algebra with an oﬀdiagonal Dirac operator. Then by Lemma 4.2, the representations
πj are not disjoint and thus there exists a non-zero operator T : H1 →H2 such that
AF ⊂A(T). If we replace T →c2Tc1 where cj belongs to the commutant of Aev, we
get
A(T) ⊂A(c2Tc1) ,
since the cj commute with the πj(b). This allows one to assume that the support of
T is contained in an irreducible subspace of the restriction of the action of Aev on H1
and that the range of T is contained in an irreducible subspace of the restriction of the
action of Aev on H2. We can thus assume that π1 is the irreducible representation of
one of the two copies of H in C2, while π2 is the irreducible representation of M4(C)
in C4. We can remove the other copy of H and replace Aev = H ⊕H ⊕M4(C) by its
projection C = H ⊕M4(C). The operator T is a non-zero operator T : C2 →C4 and
with
(4.7)
C(T) = {b ∈C | π2(b)T = Tπ1(b) , π2(b∗)T = Tπ1(b∗)}.
we have that A(T) = {(q, y) | q ∈H , y ∈C(T)}.
In particular dim A(T) = 4 +
dim C(T). Let us ﬁrst assume that the rank of T is equal to 2. The range E of T is a
two dimensional subspace of C4 and by (4.7) it is invariant under the action of b ∈C
as well as its orthogonal complement. This shows that in that case
C(T) ⊂H ⊕M2(C) ⊕M2(C) ,
and moreover the relation (4.7) shows that the component of π2(b) in the copy of M2(C)
corresponding to E is determined by the quaternion component π1(b). Thus we get
C(T) ⊂H ⊕M2(C) .
In particular the dimension fulﬁlls
dimR C(T) ≤4 + 8 = 12 .
Let us now consider the other possibility, namely that the rank of T is equal to 1. The
range E of T is a one dimensional subspace of C4 and by (4.7) it is invariant under the
action of b ∈C as well as its orthogonal complement. The support S ⊂C2 of T is a one
dimensional subspace and since both the unitary group SU(2) of H and U(4) of M4(C)
act transitively on the one dimensional subspaces (of C2 and C4) we are reduced to the
case
S = {(a, 0) ∈C2} ,
E = {(a, 0, 0, 0) ∈C4} ,
T(a, b) = (a, 0, 0, 0) ,
∀a, b ∈C .
One then obtains, for the natural embedding
C ⊂H , λ 7→

λ
0
0
¯λ

that,
C(T) = {(λ, λ ⊕m) ∈H ⊕M4(C) | λ ∈C , m ∈M3(C)} .
Thus the dimension fulﬁlls
dimR C(T) = 2 + 18 = 20 .
WHY THE STANDARD MODEL
11
Thus we see that this gives the solution with maximal dimension, and it is unique up
to an automorphism of Aev.
We can now combine the above discussion with the result of [7] Theorem 4.3 and get,
Theorem 4.3. Let M be a Riemannian spin 4-manifold and F the ﬁnite noncommu-
tative geometry of K-theoretic dimension 6 described above, but with multiplicity4 3.
Let M × F be endowed with the product metric.
(1) The unimodular subgroup of the unitary group acting by the adjoint representa-
tion Ad(u) in H is the group of gauge transformations of SM.
(2) The unimodular inner ﬂuctuations of the metric give the gauge bosons of SM.
(3) The full standard model (with neutrino mixing and seesaw mechanism) min-
imally coupled to Einstein gravity is given in Euclidean form by the action
functional
(4.8)
S = Tr(f(DA/Λ)) + 1
2 ⟨J ˜ξ, DA ˜ξ⟩,
˜ξ ∈H+
cl,
where DA is the Dirac operator with the unimodular inner ﬂuctuations.
We refer to [7] for the notations and for the predictions.
Remark 4.4. The “unimodularity” condition imposed in Theorem 4.3 (cf. [7]) on our
gauge transformations can now be viewed as the restriction to AF of the condition
giving the group of inner automorphisms of A. Indeed this group is described as the
unimodular unitary group:
(4.9)
Int(A) ∼SU(A) = {u ∈A |uu∗= u∗u = 1, det(u) = 1} .
This applies also to the product geometry by the manifold M.
