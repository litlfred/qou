---
doc_id: arxiv-1003.4808v2
doc_title: "Quantum Field Theory and the Volume Conjecture"
section_id: sec-004-23-groups-and-representations
section_title: "Groups and representations"
section_number: 2.3
pages: 11-13
source_pdf: 1003.4808v2.pdf
source_sha256: 72301d4bee491f86
doc_brief: "Quantum Field Theory and the Volume Conjecture — 14 sections: Preliminaries; The many dimensions of the volume ; Parametrized VC"
---
So far, we have considered two continuous deformations of the volume conjecture,
in u and ℏ, as drawn schematically in Figure 3. In addition, there are two discrete
generalizations that we can make.
VC
Figure 3: Continuous and discrete generalizations of the volume conjecture.
The ﬁrst such generalization involves the “gauge groups” and representations that
deﬁne colored Jones polynomials. Recall from Section 1 that the N-colored Jones
polynomial is a quantum SU (2) invariant that corresponds to coloring a knot with the
N-dimensional representation of SU (2). More generally, one can consider “quantum
SU (n) invariants,” or in fact invariants for any compact Lie group G. Knots or links
should then be colored by ﬁnite-dimensional representations R ofG. For semisimple G
and irreducibleR, the representation can be labelled by a highest weightλ in the weight
lattice Λwt⊂ g∗, where g = Lie(G). The resulting quantum polynomial invariant of a
knot in S3 may be denoted
PG
Rλ(K;q). (2.23)
Just like the colored Jones polynomial, PG
R (K;q) depends on a root of unity q =
e
2πi
k . Also like the colored Jones, these invariants satisfy
PG
⊕iRi(K;q) =
∑
i
PG
Ri(K;q), and PG
R⊗n(K;q) =PG
R (Kn;q). (2.24)
More general tensor products can also be produced by cabling a knot or link and
coloring each component of the cable with a diﬀerent representation. WhenG =SU (n)
and R is the fundamental representation (or any of its conjugates), the polynomial
PG
R (K;q) satisﬁes a skein relation similar to (1.2).
Using the positive nondegenerate trace form−Tr : g× g→ R, the weightλ can be
identiﬁed with its dual element λ∗ in t, the Cartan subalgebra of g. Let us also deﬁne
ρ to be half the sum of positive roots, and ρ∗∈ t⊂ g its dual. Then the interesting
10
limit to consider for PG
Rλ(K,q ) is
k→∞ , λ ∗→∞ , u := iπ
k (λ∗ +ρ∗) ﬁxed , (2.25)
or
q =e2ℏ =e
2πi
k → 1 ( ℏ→ 0), q λ∗+ρ∗
=e2u ﬁxed. (2.26)
The parameter u has now become a diagonal matrix, an element of tC. Coming back
to the case of SU (2) and an N-dimensional representation, in this notation we have
λ∗ =
(N− 1 0
0 −(N− 1)
)
, ρ ∗ =
(1 0
0 −1
)
, u =iπ
(N
k 0
0 −N
k
)
. (2.27)
The asymptotics of the invariant PG
R (K;q) should look very similar to those of the
colored Jones polynomial, namely
PG
Rλ(K;q)
ℏ→0
∼ exp
(
− 1
4ℏICS(u)− δ
2 log ℏ + 1
2 logiT (u)
4π +
∞∑
n=2
Sn(u)ℏn−1
)
. (2.28)
The leading term ICS(u) is now the Chern-Simons functional (1.9) evaluated at a ﬂat
GC connectionA(u) — in other words, a connection taking values in the complexiﬁed
Lie algebra gC — whose holonomy around the meridian of the knot as in Figure 2a is
Hol(µ) =m =eu. (2.29)
For genericu, this holonomy is an element of the complexiﬁed maximal torusTC⊂GC.
Again, ICS(u) can be expressed as
ICS(u) = const. + 4
∫
γ(u)
θ, (2.30)
where θ∼− ∑r
i=1vidui + exact is a diﬀerential on an r-dimensional complex variety
cut out by r equationsAj(ev,eu) = 0, with r = rank(G). The equations Aj(ev,eu) = 0
describe the moduli space of ﬂat GC connections on S3\K.
Subleading terms on the right side of (2.28) also have a geometric interpretation.
The functionT (u) is the Ray–Singer torsion of the knot complement twisted by the ﬂat
connectionA(u), and the number δ is a ﬁxed integer which can be computed in terms
of cohomology of S3\K with coeﬃcients in the associated ﬂat bundle, with structure
group GC and connection A(u) ( cf. [28, 11]). More generally, the full asymptotic
expansion can be written as a perturbative path integral just like (2.22), which takes
into account the quantum ﬂuctuations of a ﬂat GC connection.
11
