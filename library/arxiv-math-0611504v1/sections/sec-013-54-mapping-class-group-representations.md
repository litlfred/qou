---
doc_id: arxiv-math-0611504v1
doc_title: "QUANTUM HYPERBOLIC GEOMETRY"
section_id: sec-013-54-mapping-class-group-representations
section_title: "Mapping class group representations"
section_number: 5.4
pages: 26-28
source_pdf: 0611504v1.pdf
source_sha256: a33d2771c873a97e
doc_brief: "Quantum hyperbolic geometry — 19 sections: Introduction; Universal QHG; Building blocks"
duplicate_of: "agt-v7-n2-p13-s"
---
with trivial vertical framing, and let Mod( g,r ) be the mapping class group of F , that is, the group
of homotopy classes of orientation-preserving diﬀeomorphisms of F ﬁxing pointwise each boundary
component. Given ψ± : ( ±F, (T,b, L)) → F × {±1}, put ψ = ψ−1
+ ψ− and [ψ] for the corresponding
element in Mod( g,r ). Denote by ˜W[ψ] the mapping torus (F × [−1, 1])/(x, −1) ∼ (ψ(x), 1) of ψ,
with tunnel boundary ˜L[ψ]. Let ρ be the conjugacy class of PSL (2, C)-valued representations of
π1(F × [−1, 1]) (identiﬁed with π1(F ))) associated to L. To simplify notations, in all statements of
this section we do not mention the weights (we understand they are ﬁxed).
QUANTUM HYPERBOLIC GEOMETRY 27
Lemma 5.10. Up to sign and multiplication by N th roots of unity (denoted ” =N ”) we have :
(1) For any ﬁxed (T,b, L) the amplitudes HN ( ˜Y, ˜LF,ρ, (±F, (T,b, L)), [ψ±]) depend only on [ψ]. We
denote them HN ([ψ]).
(2) HN ([id]) is the identity map from EN (α−) to EN (α+), and HN ([h2]) ◦ HN ([h1]) =N HN ([h2h1]).
In particular, for any [ψ] ∈ Mod(g,r ) the QHFT tensor HN ([ψ]) is invertible, with inverse HN ([ψ−1]),
and for a homotopically d-periodic [ψ] the QHFT tensor HN ([ψ]) is of ﬁnite order less than or equal
to d.
(3) If ψ(ρ) coincides with ρ, then Trace
(
HN ([ψ])
)
=N HN ( ˜W[ψ], ˜L[ψ],ρ ).
Proof. Point (1) follows from Theorem 5.4, because
HN ( ˜Y, ˜LF,ρ, (±F, (T,b, L)), [ψ±]) =N HN ( ˜Y, ˜LF,ρ, (±F, (T,b, L)), [id], [ψ])
(the homeomorphism ψ−1
− × id sends the ﬁrst mapping cylinder to the second). By Proposition
5.6 we have H2
N ([id]) =N HN ([id]), so HN ([id]) is an idempotent. It is invertible because the matrix
dilogarithms are. Both facts imply the ﬁrst claim in (2). The rest is a dir ect consequence of Proposition
5.6 and formula (11). ✷
The arguments in the proof of Lemma 5.10 imply also that, letting [ ψ] = [id] and ρ ﬁxed, the ampli-
tudes of any marking variation ( T,b, L) → (T1,b 1, L1) are invertible. Hence HN ([ψ]) is conjugated to
the tensor HN ( ˜Y, ˜LF,ρ, (±F, (T1,b 1, L1)), [ψ±]). Moreover HN (− ˜Y, ˜LF,ρ, (∓F, (T,b, L)), [ψ±]), the
amplitude with reversed orientation, clearly coincides with HN ([ψ]−1). Using Proposition 5.7 we
deduce:
Corollary 5.11. For any ﬁxed ρ ∈ R (g,r ), the homomorphisms ψ ↦→ HN ([ψ]) induce a conjugacy
class of linear representations of Mod(g,r ), well-deﬁned up to sign and multiplication by N th roots of
unity. For SL(2, R)-valued characters ρ these representations are unitary.
5.5. T unneling the (+)/(−) states. We use (+)-Log- I-parameters to deﬁne the QHFT because of
the existence of strongly idealizable cocycles on QHFT bordism triang ulations, which makes functo-
riality easy to check. Here we exhibit a family of tensors correlating t he ( ±)-Log-I-parameters, thus
recovering, in particular, the direct and nice interpretation of bou ndary structures having non trivial
holonomy at the punctures in terms of pleated hyperbolic surfaces (see Section 3.3). These tensors
are also used in Section 6.3.
For any base surface F with an e-triangulation (T,b ), let Z(F ) be the pseudo-manifold obtained by
collapsing to a point each boundary annulus of the cylinder C(F ) = F × [−1, 1]. Recall the bundle
E(F )+ in (18), and consider similarly E(F )− : ˜W −(T,b ) ×V (T,b ) → ˜W −(T,b ). We have:
Proposition 5.12. There exists a canonical family F of ﬂat/charged I-triangulations covering a
portion of Z(F ), with invertible trace tensor HN (F ) : E(F )+ →E(F )−.
Proof. Orient C(F ) so that ±F is identiﬁed with F × {±1}. Let P (T,b ) be the cell decomposition
of C(F ) made by the prisms with base the 2-simplices of T . Orient all the “vertical” (ie. parallel to
[−1, 1]) edges ofP (T,b ) towards +F . For every abstract prism P , every vertical boundary quadrilateral
R has both the two horizontal and the two vertical edges endowed w ith parallel orientations. So
exactly one vertex of R is a source (that belongs to −F ), and exactly one is a pit (that belongs to
+F ). Triangulate each R by the oriented diagonal going from the source to the pit. Finally ext end
the resulting triangulation of ∂P to a triangulation of P made of 3 tetrahedra, by taking the cone
from the b-ﬁrst vertex of the bottom base triangle of P (note that no further vertices nor further edges
have been introduced). Repeating this for every prism, we get a br anched distinguished triangulation
(C(T,b ),H ) of C(F ), where the vertical edges make the Hamiltonian tangle H. As in the proof of
Theorem 5.3 there exists integral charges on ( C(T,b ),H ).
LetF × [−1, 3] be triangulated by two adjacent copies of C(T,b ), glued each to the other at F × {+1}.
For any z ∈ ZI (T,b )+, consider the unique cocycle C0(z) on the composition C(T,b ) ∗C(T,b ) that:
extends z ∪ Ψ(z), given on ( F × {−1}) ∪ (F × {3}); takes the value P of (15) on each vertical edge
contained in F × [1, 2]; takes the value 1 on each vertical edge contained in F × [−1, 1]. Perturb C0(z)
with a 0-cochain s that: takes the value 1 on ( F × {−1}) ∪ (F × {3}); takes values in PB +(2, C) at
28 ST ´EPHANE BASEILHAC 1 AND RICCARDO BENEDETTI 2
each vertical boundary annulus; restricts to an idealizable cocycle on F × [−1, 1] and to a maximally
idealizable cocycle on F × [1, 3] (see Deﬁnition 3.7). Finally, glue I-cusps to the idealization. Note
that the only non idealizable tetrahedra are those in the star of a bo undary edge of the triangulation
of F × {3}. Lemma 2.9 gives ﬂattenings for the idealizable tetrahedra.
Look at the ideal triangulation ( T ′,b ′) of S \V corresponding to the copy of the triangulation ( T,b )
for the boundary component F × {3}. For every cochain s as above and every edge e ofT ′ we have two
complex numbers: the ( −)-exponential I-parameter W −(Ψ(z))(e), and, as in (7), the total product
W(e) of the cross-ratio moduli at the edges of T that enter the deﬁnition of W −(Ψ(z))(e). Recall that
there are two distinct such edges only when e contributes to make a marked corner. It is possible to
normalize s so that for every edge e of T ′ we have W −(Ψ(z))(e) = W(e)−1.
Varying the cocyclez ∈ ZI (T,b )+, this choice determines the family F in the statement. By perturbing
the initial cocycle z with 0-cochains t with values in PSL (2, C) \PB +(2, C), the same construction
leads to families Ft of ﬂat/charged I-triangulations covering the whole of F × [−1, 3].
Note that for suitable ﬂat/charges ( f1 = 0 in (3) and c1 = 0 in (6)) the matrix dilogarithms have well-
deﬁned ﬁnite limits when the cross-ratio modulus w0 → 0. From the symmetry relations of the matrix
dilogarithms (see [5], Corollary 5.6), this is true more in general for a ny degenerating sequence of I-
tetrahedra, that is when w0 goes to 0, 1 or ∞. Now, we can choose in a continuous way the ﬂat/charges
of Ft so that they satisfy the above constraints on the tetrahedra of Ft that become non idealizable
in F , when t → id. Then HN (F ) := limt HN (Ft) exists. As in Lemma 5.10 (2) we see that HN (Ft)
is invertible, with inverse HN (−Ft). Since HN (F ) ◦ HN (−F ) = lim t(HN (Ft) ◦ HN (−Ft)) =N id
(Proposition 5.9), we deduce that HN (F ) is invertible. ✷
Figure 12. Pasting opposite vertical sides yields an instance of C(T,b ) for the
once-punctured torus S, based on an economic triangulation of S as in Remark 3.12.
