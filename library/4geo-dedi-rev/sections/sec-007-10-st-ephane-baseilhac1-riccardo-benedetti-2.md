---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-007-10-st-ephane-baseilhac1-riccardo-benedetti-2
section_title: "ST ´EPHANE BASEILHAC1, RICCARDO BENEDETTI 2"
section_number: 10
pages: 11-13
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 27 sections: ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE; ST ´EPHANE BASEILHAC1, RICCARDO BE"
---
on C asw↦→γrw +b, where γr∈ C∗ andb∈ C. The coeﬃcient γr is that squared eigenvalue selected
by [(r,{ξΓ}Γ)].
We have (see [5] and [6]):
Theorem 3.5. (1) There exists a determined regular rational map κN : A0,N→ (C∗)2r such that the
imageκN(A0,N) is the open subset of (C∗)2r made of all the classes κ∈H1(∂ ¯Mφ; C∗) such thatκ(lj)N
and κ(mj)N are equal up to a sign respectively to the squared eigenvalues selected by [(r,{ξΓ}Γ)] at
the curves lj and mj, where r := [(r,{ξΓ}Γ)] =hol(w) for some w∈A0.
(2) Given r∈hol(A0) andκ∈H1(∂ ¯Mφ; C∗) as above, the value ofHred
N (T, ˜b, w) is independent, up
to multiplication by 4N-th roots of unity, of the choice of (T, ˜b, w) among all weakly branched layered
triangulations of Mφ endowed with a system of quantum shape parameters w such that hol(w) = r
and κN(w) =κ.
We denote the resulting invariant by Hred
N (Mφ, r,κ ) := Hred
N (T, ˜b, w). By the results of [6], it
actually depends on the ﬁbration of Mφ.
The map κN in Theorem 3.5 is a lift to A0,N of j∗◦hol|A0, where j∗ is the restriction map
X(Mφ)→ X(∂Mφ). Here is a concrete way to compute κN(w)(α), for α∈ H1(∂ ¯Mφ; Z). It is well
known that the truncated tetrahedra of an ideal triangulation T of Mφ provide a cell decomposition
of ¯Mφ which restricts to a triangulation ∂T of ∂ ¯Mφ. Every abstract vertex of T corresponds to an
abstract triangle of ∂T (at which a tetrahedron has been “truncated”); every vertex of such a triangle
is contained in one abstract edge of T . Represent the class α by an oriented simple closed curve a
on ∂ ¯Mφ, transverse to ∂T . The intersection of a with a triangle F of ∂T is a collection of oriented
arcs. We can assume that none of these arcs enters and exits F by a same edge. Then, each one turns
around a vertex of F . If ∆ is a tetrahedron of T andF corresponds to a vertex of ∆, for every vertex
v ofF we denote byEv the edge of ∆ containing v, and write a→Ev to mean that some subarcs of a
turn around v. We count them algebraically, by using the orientation of a: if there are s+ (resp. s−)
such subarcs whose orientation is compatible with (respectively, opposite to) the orientation of ∂ ¯Mφ
as viewed from v, then we set ind(a,v ) :=s+−s−. Then
(5) κN(w)(α) =
∏
a→Ev
w(Ev)ind(a,v).
In the case where α is the class of a positively oriented meridian curve mi of ∂ ¯Mφ, this gives
(6) κN(w)(α) =
∏
mi→Ev
w(Ev).
Let us give now more details about the deﬁnition of the reduced QH state sum Hred
N (T, ˜b, w). We
are going to do it in terms of the QH-operator associated to the cylinder Cφ, already mentioned in
the Introduction.
By cutting (T, ˜b, w) along one of the surfaces (S,λj) (that is, a triangulated ﬁbre of Mφ), we get a
QH-triangulation (TCφ,˜b, w) of the cylinder Cφ having as “source” boundary component ( S,λ ), and
as “target” boundary component ( S,λ′), where λ =λj and λ′ =φ(λj). It carries in a contravariant
way the QH-operatorHred
N (TCφ,˜b, w)∈ End
(
(CN)⊗2m)
, which is such that
Trace
(
Hred
N (TCφ,˜b, w)
)
=Hred
N (T, ˜b, w).
We deﬁne the QH-operatorHred
N (TCφ,˜b, w) by means of elementary tetrahedral and 2-face operators,
as follows.
We can regard the QH triangulation (T, ˜b, w) ofMφ as a network of abstract QH-tetrahedra(∆,b, w),
with gluing data along the 2-faces. To each QH-tetrahedron (∆,b, w) we associate a linear isomorphism
called basic matrix dilogarithm (“basic” refers to the fact that we have dropped a symmetrization factor
from the matrix dilogarithms that enter the deﬁnition of the unreduced QHI),
LN(∆,b, w): V2⊗V0→V3⊗V1
ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS 11
where Vj is a copy of CN associated to the 2-face of (∆ ,b ) opposite to the vertex vj. The basic
matrix dilogarithms will be deﬁned explicitly below. For the moment, note that V1, V3 correspond
to the 2-faces with pre-branching co-orientation pointing inside ∆. Concerning the gluing data, every
2-face F of T is obtained by gluing a pair of abstract 2-faces. Denote by Fs and Ft the “source” and
“target” 2-face of the pair, with respect to the transverse co-orientation deﬁned by the pre-branching
ω˜b. Denote by VFs and VFt the copies of CN associated to Fs and Ft. The identiﬁcation Fs→Ft is
given by an even permutation on three elements, which encodes the image of the vertices of Fs inFt.
So it can be encoded by an element r(F )∈ Z/3Z. The triangulation TCφ of the cylinder Cφ has 2m
free 2-faces at both the source and target boundary components, (S,λ ) and (S,λ′). Note that at every
2-face of (S,λ ) the pre-branching orientation points inside Cφ, while it points outside at the 2-faces
of (S,λ′). For every gluing Fs→Ft occuring at an internal 2-face F ofTCφ, as well as to every 2-face
F of (S,λ′), we associate an endomorphism (again in contravariant way)
(7) Qr(F)
N :VFt→VFs.
By deﬁnition, the QH-operator Hred
N (TCφ,˜b, w) is the total contraction of the network of tensors
{LN(∆,b, w)}∆ and{Qr(F)
N }F . In formulas:
(8) Hred
N (TCφ,˜b, w) =
∑
s
∏
∆
LN(∆,b, w)s
∏
F
Qr(F)
N,s
where the sum ranges over all maps s:{abstract 2-faces of T}∪{ 2-faces of (S,λ′)}→{ 0,...,N − 1}
(the states of (TCφ,˜b, w)), andLN(∆,b, w)s and QN,s denote the entries of the tensors LN(∆,b, w)
and QN selected by s, when the tensors are written in the canonical basis {ej} of CN. Note that
the domain of s contains two copies of each 2-face F in the target boundary component of Cφ. They
correspond to the source and target spaces VFs, VFt of Qr(F)
N .
Finally, we provide an operator theoretic deﬁnition of the basic matrix dilogarithms (it is a straight-
forward rewriting of formula (32) in [4]), as well as their entries and those of the endomorphisms QN.
Since it is the transposed tensorHred
N (TCφ,˜b, w)T mentioned in the Introduction (see formula (3)) that
occurs in Theorem 1.1, we consider the transposed endomorphisms of QN and of the basic matrix
dilogarithm instead:
QT
N :V′
Fs→V′
Ft , LT
N(∆,b, w) :V′
3⊗V′
1→V′
2⊗V′
0
whereV′
Fs =V′
Ft =V′
j = (CN)′, the dual space of CN, for every j. The matrix elements will be given
with respect to the canonical basis of
(
(CN)′)⊗2
.
Remark 3.6. If{ej} is the canonical basis of CN, and{ej} the dual basis of (CN)′, the identiﬁcation
map ι : CN → (CN)′, ι(ej) = ej, extends to a canonical identiﬁcation, also denoted by ι, between
(CN)⊗2 and
(
(CN)′)⊗2
. Below we will rather deal with the endomorphisms
ι−1◦QT
N◦ι∈ End
(
CN)
, ι−1◦LT
N(∆,b, w)◦ι∈ End
(
(CN)⊗2)
.
Obviously, they have the same matrix elements as QT
N andLT
N(∆,b, w) with respect to the canonical
basis of CN and (CN)′, and ( CN)⊗2 and
(
(CN)′)⊗2
, respectively. Similarly we will consider
ι−1◦Hred
N (TCφ,˜b, w)T◦ι∈ End
(
(CN)⊗2m)
.
For simplicity we will systematically omit the maps ι from the notations .
The endomorphism QT
N : VFs→ VFt is deﬁned in the standard basis {ej} of (the copies VFs, VFt
of) CN by
(9) QT
N(ek) = 1√
N
N−1∑
j=0
q2kj+j2
ej.
Deﬁne the endomorphisms A0, A1, A2∈ End(CN) by
(10) A0ek =q2kek, A1ek =ek+1, A2ek =q1−2kek−1.
