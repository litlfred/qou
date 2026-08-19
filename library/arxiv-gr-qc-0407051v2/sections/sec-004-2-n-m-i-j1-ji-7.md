---
doc_id: arxiv-gr-qc-0407051v2
doc_title: "Black hole entropy from Quantum Geometry"
section_id: sec-004-2-n-m-i-j1-ji-7
section_title: "N, m i ∈ {−j1, ..., ji} (7)"
section_number: 2
pages: 4-7
source_pdf: 0407051v2.pdf
source_sha256: 2de07e909b17c5a5
doc_brief: "Black hole entropy from Quantum Geometry — Quantum Geometry (the modern Loop Quantum Gravity using gra phs and spin-networks instead of the loops) provides microscopic d egrees of freedom that"
---
for i = 1, ..., n. The ji labels are assumed not to vanish,
ji ⁄= 0 . (8)
The space HΣ is the orthogonal sum
HΣ =
⨁
(P,j,m)
HP,j,m
Σ , (9)
where P runs through all the ﬁnite subsets of S, ( j, m) through all the ﬁnite labeling (7,8),
and the empty set P = ∅ is also associated a (non-trivial) single Hilbert space H∅
Σ . Each
4
of the subspaces HP,j,m
Σ is a certain (inﬁnitely dimensional) Hilbert space. To unde rstand
the (quantum) geometric meaning of these subspaces, consid er any piece S′ of the horizon
S (more precisely, S′ is an arbitrary 2-sub-manifold in the 2-sphere S). The quantum area
operator ˆAS′ is deﬁned in HΣ . Another operator of the quantum geometry in Σ assigned to
S′ is the ﬂux ˆES′ of the vector ﬁeld normal to S.2 Every subspace HP,j,m
Σ is the eigenspace
of the operators. The corresponding eigenvalues are:
aP,j
S′ = 8 πγℓ 2
Pl
∑
pi∈P∩S′
√
ji(ji + 1), (10)
eP,m
S′ = 8 πγℓ 2
Pl
∑
pi∈P∩S′
mi (11)
where only those points pi ∈ P contribute which are contained also in S′, and γ > 0 is a
free parameter of Quantum Geometry known as Barbero-Immirz i parameter. In particular,
if we take for S′ the whole horizon S, then the corresponding eigenvalue of the horizon area
operator is (we drop P because only the set of the values of j matters)
aj
S = 8 πγℓ 2
Pl
∑
i
√
ji(ji + 1). (12)
Of course the quantum area and ﬂux operators are deﬁned also f or 2-dimensional sub-
manifolds of Σ which do not intersect S, and there are also other interesting operators of
Quantum Geometry acting in HΣ but they are not used in the Isolated Horizon framework.
We turn now to the horizon Hilbert space HS. Recall, that the ABCK framework requires
ﬁxing an arbitrary value for the classical horizon area a. In order to quantize consistently
the horizon degrees of freedom, it is assumed in [8] that the ﬁ xed classical area a is quantized
in the following way,
a = 4 πγℓ 2
Plk, k ∈ N, (13)
where k is arbitrary. The horizon Hilbert space can also be orthogon ally decomposed in a
way analogous to (9). In this case the labeling set consists o f all the ﬁnite sequences ⃗P of
points in S, labeled by arbitrary non-zero integers deﬁned modulo k, and whose sum is zero
modulo k,
⃗P = ( p1, ..., pn) b = ( b1, ..., bn) , (14)
bi ∈ Zk, i = 1, ..., n,
n∑
i=1
bi = 0 . (15)2 There are two subtleties, which may be intriguing for the rea der. The ﬁrst one is that classically
the ﬂux of a vector ﬁeld normal to a surface is the same as the ar ea of the surface. In our quantum
case however, the vector ﬁeld is a quantum operator itself, i n fact it is one of the SU(2) spin
operators. The area, on the other hand, is given by the total S U(2) spin operator. The second
subtlety is, that S′ contained in the horizon is assigned the area and ﬂux by the bulk geometry.
5
To every labeled sequence ( ⃗P, b) there is assigned a 1-dimensional Hilbert space H
⃗P,b
S . The
points pi are often called punctures, and for every pi, the U(1) element ei 2πb i
k is the eigenvalue
of the holonomy transport along a circle containing pi. The full horizon Hilbert space can
be written as the orthogonal sum
HS =
⨁
( ⃗P,b)
H
⃗P,b
S , (16)
where to the labeling set of pairs ( ⃗P, b) we add the empty sequence which labels a single,
1-dimensional space H
⃗∅
S.
Now, the quantum condition that S be a section of a spherically symmetric isolated
horizon is introduced in the product Hilbert space
HS ⊗ HΣ =
⨁
( ⃗P,b)
⨁
(P ′,j,m)
(
H
⃗P,b
S ⊗ HP ′,j,m
Σ
)
. (17)
It involves the holonomy operators acting in H
⃗P,b
S on the one hand and the ﬂux operators
acting in HP ′,j,m
Σ on the other hand (see [8] or [3] for a summary). The set of solu tions is the
orthogonal sum of products H
⃗P,b
S ⊗ HP,j,m
Σ such that the points coincide modulo the ordering
⃗P = (p1, ..., pn), P = {p1, ..., pn} (18)
and the labelings agree with each other in the following way
bi = −2mi mod k. (19)
In conclusion, the kinematic Hilbert space of states in the A BCK quantum Isolated Horizon
framework is the orthogonal sum with respect to all the label ed sequences of points in S
which satisfy (18,19),
Hkin =
⨁
⃗P,j,m
H
⃗P,b(m)
S ⊗ HP,j,m
Σ , (20)
where we emphasized the dependence of each sequence b = ( b1, ..., bn) on a sequence m =
(m1, ..., mn) via (19).
The ﬁnal step of the ABCK framework is to take into account the quantum Einstein
constraints [1–3] adjusted to the Isolated Horizon framewo rk [8]. The vector constraints
generate diﬀeomorphisms of Σ which preserve the boundary S. The diﬀeomorphisms act
naturally in Hkin and this action is unitary. In the Quantum Geometry framewor k, the
quantum vector constraints come down to the diﬀeomorphism i nvariance. Whereas there
is only one normalizable diﬀeomorphism invariant state in Hkin, the invariance condition is
imposed in a certain larger space (dual to an appropriate sub space of Hkin). A Hilbert space
of solutions is constructed via the diﬀeomorphism averagin g procedure whose Quantum
Geometry version is well described in [1,3]. It is particula rly easy to explain the result of the
6
analogous diﬀeomorphism averaging suitable for the space HS itself. Assign to every ﬁnite
sequence b = (b1, ..., bn) deﬁned in (15) a 1-dimensional Hilbert space Hb
S, and deﬁne
HS,phys =
⨁
b
Hb
S . (21)
The averaging applied to the full space Hkin provides a Hilbert space of the following struc-
ture
H =
⨁
j,m
˜Hb(m),j,m, (22)
where b = ( b1, ..., bn), j = ( j1, ...jn) and m = ( m1, ..., mn) are arbitrary triples of ﬁnite
sequences such that (7,15,19) holds. The remaining constra ints are the scalar and the Gauss
constraint. The Gauss constraint amounting to the invarian ce with respect to the local SU(2)
rotations of the spin frames is already satisﬁed at S due to (19). The scalar constraint, on
the other hand, has been solved at the horizon already on the c lassical level. Since the
quantum numbers ( j, m) used in (23) characterize the quantum geometry of bulk Σ rig ht
at the boundary S, the plausible, but non-trivial assumption made in [8] is th at the bulk
scalar constraints with laps functions vanishing on S do not aﬀect ( j, m), and that for every
choice of ( j, m) there is a solution of the bulk scalar constraints.
We are lead to a conclusion, that the ﬁnal physical Hilbert Hphys of the quantum states
can be characterized as
Hphys =
⨁
j,m
Hb(m),j,m, (23)
where b = ( b1, ..., bn), j = ( j1, ...jn) and m = ( m1, ..., mn) are arbitrary triples of ﬁnite
sequences such that (7,15,19) is satisﬁed, and none of the sp aces Hb(m),j,m is empty. Since
the horizon area operator ˆAS commutes with all the constraints in this framework, it pass es
to the physical Hilbert space. It also follows from the detai ls of the diﬀeomorphism averaging
map, that each of the subspaces Hb(m),j,m is an eigenspace corresponding to the eigenvalue
(12). In this way, the sequences j are responsible for the area assigned to the 2-surface
S of the horizon by the bulk Quantum Geometry, whereas the sequ ences b represent the
intrinsic quantum degrees of freedom of the horizon. This is the key conclusion of the
ABCK framework.
