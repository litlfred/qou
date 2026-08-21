---
doc_id: arxiv-1611.03697v5
doc_title: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY"
section_id: sec-034-7-quadratic-differentials-and-exact-wkb-analysis
section_title: "Quadratic differentials and exact WKB analysis"
section_number: 7
pages: 33-35
source_pdf: 1611.03697v5.pdf
source_sha256: 3d7e5a14a079c8c5
doc_brief: "RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY — We study a class of Riemann-Hilbert problems arising naturally in Donald son-Thomas theory."
---
The only examples of CY 3 categories where the full stability space is understood come from
quivers with potential associated to triangulated surfaces. The a ssociated stability spaces can
be identiﬁed with moduli spaces of meromorphic quadratic diﬀerentia ls on Riemann surfaces [ 10],
and the associated BPS invariants then count ﬁnite-length trajec tories of these diﬀerentials. It
turns out that the corresponding Riemann-Hilbert problems are clo sely related to the exact WKB
analysis of time-independent Schr¨ odinger equations. We give a brie f and sketchy treatment of this
connection here; we hope to return to this subject in future pape rs.
7.1. Quadratic diﬀerentials. For more details on the contents of this section see [ 10]. Let us
start by ﬁxing data
g≥ 0, m ={m1,··· , mk}, k ≥ 1, m i≥ 2,
and consider the space Quad( g, m) consisting of equivalence classes of pairs ( S, q), where S is a
compact Riemann surface of genus g and q a meromorphic quadratic diﬀerential on S with simple
zeroes, and poles of multiplicities mi. It is a complex orbifold of dimension
n = 6g− 6 +
∑
i
(mi + 1).
Associated to a point ( S, q) is a double cover π : ˆS→ S branched at the zeroes and odd-order
poles of q. We denote by ˆS◦⊂ ˆS the complement of the inverse image of the poles of q, and deﬁne
the hat-homology group
Γ = H1( ˆS◦; Z)−,
where the superscript denotes the −1 eigenspace under the action of the covering involution of
π : ˆS→ S. The intersection form deﬁnes a skew-symmetric form
⟨−,−⟩: Γ× Γ→ Z.
The groups Γ form a local system over Quad( g, m).
The meromorphic abelian diﬀerential √q is well-deﬁned on the double cover ˆS, and holomorphic
on ˆS◦. It deﬁnes a de Rham cohomology class in H 1( ˆS◦; C)− and can be viewed as a group
homomorphism Z : Γ → C
Z(γ) =
∫
γ
√q.
34 TOM BRIDGELAND
It was proved in [ 10] that the period map
π : Quad( g, m)→ HomZ(Γ , C)∼= Cn.
is a local analytic isomorphism.
By a trajectory of a diﬀerential ( S, q) we mean a path in S along which√q has constant phase
θ. A ﬁnite-length trajectory is of one of two types:
(a) a saddle connection connects two zeroes of the diﬀerential (n ot necessarily distinct);
(b) a closed trajectory: any such moves in an annulus of trajecto ries called a ring domain.
Any ﬁnite-length trajectory can be lifted to a closed cycle in ˆS which deﬁnes an associated class
γ∈ Γ. All trajectories in a ring domain have the same class, so we can also talk about the class
associated to the ring domain.
Let us assume that our quadratic diﬀerential is generic in the sense that if γ1, γ2 are two ﬁnite-
length trajectories of the same phase, then their classes are pro portional in Γ. We then deﬁne the
BPS invariants of q by
Ω( γ) = #
{
saddle connections of class γ
}
− 2· #
{
ring domains of class γ
}
.
The reason for the coeﬃcient −2 is that a ring domain leads to a moduli space of stable ob-
jects isomorphic to P1. See [ 10, Theorem 1.4]. In physical terms saddle connections represent
hypermultiplets, whereas ring domains represent vector multiplets .
Claim 7.1. The data (Γ , Z, Ω) described above deﬁnes a miniversal variation of convergen t BPS
structures over the orbifold Quad(g, m).
Sketch proof. To check the wall-crossing formula one can use the results of [ 10] to view Quad( g, m)
as an open subset of a space of stability conditions on a CY 3 triangulated category deﬁned by
a quiver with potential, and then apply the theory of wall-crossing fo r generalised DT invariants
[21, 23].
The fact that the BPS structures are convergent should follow fr om the results of [ 10, Section
5]. The basic point is that the only non-ﬁniteness in the BPS spectrum arises from ﬁnitely many
ring domains. Each of these contributes an inﬁnite collection of sadd le connections with classes of
the form γ + nα, where α is the class of the ring domain. But for suﬃciently large R > 0 these
saddle connections give a ﬁnite contribution to the sum ( 9). □
RIEMANN-HILBERT PROBLEMS FROM DONALDSON-THOMAS THEORY 35
