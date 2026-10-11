---
doc_id: arxiv-2401.00636v2
doc_title: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS"
section_id: sec-021-53-casimir-connections
section_title: "Casimir connections"
section_number: 5.3
pages: 25-27
source_pdf: 2401.00636v2.pdf
source_sha256: 35e372d04cedf234
toc_source: outline
doc_brief: "PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS — We introduce a new notion of a periodic pencil of ﬂat connections on a smooth algebraic variety X."
---
5.3.1. Rational Casimir connections. Consider the setting of 5.1.1. Let hreg be the regular
part of the Cartan subalgebra h ⊂g as in 5.2.1. Let V be a ﬁnite dimensional g-module.
The Casimir connection (also called the dynamical connection) is the connection on
the trivial bundle on hreg with ﬁber V given by
∇(ℏ) = d −ℏ
X
α∈R+
e−αeα + e−αeα
2
dα
α ,
where eα are the root elements of g deﬁned in 5.1.1. This connection is ﬂat and has regular
singularities. It was ﬁrst deﬁned by De Concini around 1995 (unpublished), and then was
studied in the papers [FMTV], [TL1], [MTL] and many subsequent ones.
In particular,
Toledano-Laredo proved ([TL2],[TL3]) that the monodromy of ∇(ℏ) is given by the quantum
Weyl group action on the representation Vq of the quantum group Uq(g) corresponding to
V , where q = eπiℏ(as had been conjectured independently by Toledano-Laredo and C. De
Concini and proved for g = sln in [TL1]). Since ∇is h-invariant, the same is clearly true on
every weight subspace V [µ].
This can be generalized in various ways. First of all, one can take V to be a module
from category O with rational weights and restrict ∇(ℏ) to a weight subspace V [µ]. The
monodromy of ∇is then still given by the (pure) quantum Weyl group ([ATL]).
Also we can consider the multiparameter version. To this end take V = M(λ), the Verma
module over g with highest weight λ, and take µ = λ −β for ﬁxed β ∈Q+. Then V [µ] ∼=
U(n−)[−β], and in this realization the operators e−αeα depend linearly (inhomogeneously)
on λ. Thus ∇(ℏ)|M(λ)[λ−β] can be viewed as a multiparameter pencil with poarameter s =
(ℏ, ℏλ). By [ATL], the monodromy of ∇(s) is given by the pure quantum Weyl group, so
depends on e2πis.
Finally, this whole story extends to the case when g is a symmetrizable Kac-Moody algebra,
since this is the generality of the monodromy result of [ATL].
5.3.2. Trigonometric Casimir connections. The trigonometric version of the Casimir con-
nection was introduced in [TL4]. To deﬁne it, keep the setting of the previous subsection
and the notation of 5.2.2. Let Y (g) be Drinfeld’s Yangian of g in which the Planck constant
ℏis set to 1, and let J : g →Y (g), be the g-invariant map deﬁning the Drinfeld generators of
Y (g) ([TL4], Section 3). Let V be a ﬁnite dimensional irreducible representation of Y (g) on
which J(ω∨
i ) acts with rational eigenvalues (i.e., its Drinfeld polynomial has rational roots).
26
PAVEL ETINGOF AND ALEXANDER VARCHENKO
The trigonometric Casimir connection is the connection on the trivial bundle on Hreg
with ﬁber V given by
∇(ℏ) = d −ℏ

X
α∈R+
1
4
eα + 1
eα −1(eαe−α + e−αeα)dα −
rank(g)
X
i=1
J(ω∨
i )dαi

.
It is shown in [TL4] that this connection is ﬂat, and it clearly has regular singularities. Note
that ∇falls into a direct sum of connections on h-weight spaces of V . Also ∇is a pencil,
and it arises as the equivariant quantum connection for quiver varieties of ﬁnite type ([MO]),
hence is periodic and quasi-motivic.
Also for g = sl2 it is shown in [GTL] that the monodromy of ∇(ℏ) is given by the action
of the quantum Weyl group on the corresponding representation Vq of the quantum aﬃne
algebra Uq(bg), and the proof for general g is forthcoming in a joint work of Gautam and
Toledano-Laredo. This also will imply the quasi-motivic and periodic properties of ∇(ℏ).
There is also a multiparameter version of this pencil. To describe it, denote by V (z) the
shift of the representation V by z ∈C, which is V as a g-module with
J(a)|V (z) = (J(a) + za)|V .
Let V1, ..., Vn be irreducible ﬁnite dimensional Y (g)-modules whose Drinfeld polynomials have
rational roots, and let V := V1(z1) ⊗... ⊗Vn(zn) (tensor product using the Hopf structure
on Y (g)). Recall that
∆(J(h)) = J(h) ⊗1 + 1 ⊗J(h) + 1
2[h ⊗1, Ω].
Thus V = V1 ⊗... ⊗Vn as a g-module, and
J(h)|V =
n
X
j=1
zj(J(h)|Vj)(j) + J0(h)|V1⊗...⊗Vn,
where J0(h) ∈U(g)⊗n does not depend on zj. Thus the pencil ∇(ℏ)|V can be viewed as a
multiparameter pencil ∇(s) with parameter s = (ℏ, ℏz), where z := (z1, ..., zn). This pencil
arises as the equivariant quantum connection for quiver varieties of ﬁnite type ([MO]), so it
is quasi-motivic and periodic. This will also follow from the forthcoming results of Gautam
and Toledano-Laredo on the monodromy of ∇(s).
Remark 5.8. 1. If g = sln then the (trigonometric) Casimir connection is equivalent to the
(trigonometric) KZ connection for glm, via the Howe duality between gln and glm, see [GTL],
[TL1]. As explained in these papers, this duality can be used to compute the monodromy of
the trigonometric Casimir connection in type A.
2. Let V = g be the adjoint representation of g. Then the Casimir connection on V [0]
coincides with the Dunkl connection for the Weyl group W of g in its reﬂection representation
h. Similarly, in the trigonometric case consider the adjoint representation V of the Yangian
Y (g) (evaluated at 0), which is g for type A and g ⊕C otherwise as a g-module. Then the
trigonometric Casimir connection in V [0] coincides with the trigonometric Dunkl connection
on the reﬂection representation of the degenerate aﬃne Hecke algebra H(W), which is h in
type A and h ⊕C otherwise.
PERIODIC AND QUASI-MOTIVIC PENCILS OF FLAT CONNECTIONS
27
