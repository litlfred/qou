---
doc_id: arxiv-0801.3233v4
doc_title: "Twisted Deformation Quantization of Algebraic Varieties (Survey)"
section_id: sec-009-appendix-c-the-l-quasi-isomorphism-of-the-level
section_title: "Appendix C. The L quasi-isomorphism of the Level of Sheaves"
section_number: null
pages: 13-15
source_pdf: 0801.3233v4.pdf
source_sha256: d98f9d4a9ecb4c5e
toc_source: outline
doc_brief: "Twisted Deformation Quantization of Algebraic Varieties (Survey) — Let X be a smooth algebraic variety over a ﬁeld of characteristic 0. We introduce the notion of twisted associative (resp."
---
Here is an outline of the proof of Theorem 4.3. Details can be found in the
Erratum to [Ye1]. We assume R ⊂K, and X is a smooth n-dimensional algebraic
variety over K.
A formal coordinate system at a closed point x ∈X is an isomorphism of
K-algebras
k(x)[[t]] = k(x)[[t1, . . . , tn]]
≃
−→b
OX,x,
where k(x) is the residue ﬁeld, and b
OX,x is the complete local ring.
There is an inﬁnite dimensional scheme Coor X, called the coordinate bundle,
with a projection π : Coor X →X, which is a moduli space for formal coordinate
systems. (In [Ko1] the notation for Coor X is Xcoor.) In particular, for every closed
point x ∈X, the k(x)-rational points in the ﬁber π−1(x) stand in bijection to the
set of formal coordinate systems at x.
To get an idea of how the scheme Coor X looks, let us note that Coor X =
lim←Coori X, where each Coori X is the variety parameterizing formal coordinate
systems up to order i.
Let PX be the sheaf of principal parts on X (a.k.a. the jet sheaf). Recall that
PX is the formal completion of OX×X along the diagonal. As such, PX is a sheaf
of rings on X, with two ring homomorphisms OX →PX (corresponding to the two
projections X × X →X), which make PX into an OX-bimodule. When we view
PX as a left OX-module, it has the Grothendieck connection
∇: PX →Ω1
X ⊗OX PX,
which is the completion of pullback, under the ﬁrst projection X × X →X, of the
standard connection d : OX →Ω1
X . The Grothendieck connection is ﬂat, and its
kernel is OX (coming from the second projection).
Let us denote by π∗PX the pullback of the left OX-module PX; and let πb∗PX
be its adic completion. The universal property of π : Coor X →X implies that
there is a canonical isomorphism
(C.1)
OCoor X b⊗K K[[t]] ∼= πb∗PX,
of sheaves of OCoor X-algebras on Coor X.
Like (C.1), there are canonical isomorphisms
OCoor X b⊗K Tpoly(K[[t]]) ∼= πb∗(PX ⊗OX Tpoly,X)
and
OCoor X b⊗K Dpoly(K[[t]]) ∼= πb∗(PX ⊗OX Dpoly,X)
14
AMNON YEKUTIELI
of graded Lie algebras on Coor X. Let us write A := ΩCoor X, the sheaf of diﬀeren-
tial forms on Coor X; so in particular A0 = OCoor X. Then, by applying A b⊗A0 −,
we get canonical graded Lie algebra isomorphisms
(C.2)
A b⊗K Tpoly(K[[t]]) ∼= A b⊗A0 πb∗(PX ⊗OX Tpoly,X)
and
(C.3)
A b⊗K Dpoly(K[[t]]) ∼= A b⊗A0 πb∗(PX ⊗OX Dpoly,X)
on Coor X. However the diﬀerentials do not match: to compensate for the Grothen-
dieck connection on the right side, we have to add the diﬀerential ad(ω) on the left
side, where ω ∈A1 b⊗K T 0
poly(K[[t]]) is a universal MC element.
Due to the Kontsevich Formality Theorem (Theorem B.1) we obtain an induced
A-multilinear L∞quasi-isomorphism
Υ : A b⊗K Tpoly(K[[t]]) →A b⊗K Dpoly(K[[t]])
between sheaves of DG Lie algebras on Coor X. (This should be compared to the
L∞quasi-isomorphism (B.2) in the local case.) Using the isomorphisms (C.2) and
(C.3), and twisting Υ by the element ω (in the sense of [Ye3, Theorem 3.2]), we
then obtain an A-multilinear L∞quasi-isomorphism
Υω : A b⊗A0 πb∗(PX ⊗OX Tpoly,X) →A b⊗A0 πb∗(PX ⊗OX Dpoly,X).
If we had a section σ : X →Coor X then we could pull Υω down to an L∞
quasi-isomorphism on X. However usually there are no global sections of Coor X,
because of topological obstructions.
The group GLn acts on Coor X by linear change of coordinates. Let us deﬁne
LCC X to be the quotient scheme Coor X/ GLn. (“LCC” stands for “linear coordi-
nate classes”.) So the projection π : Coor X →X factors through LCC X. Recall
that the universal quantization of Kontsevich is invariant under linear change of
coordinates, namely under the action of the group GLn and its Lie algebra. This
implies that the L∞morphism Υω descends to LCC X; and hence it suﬃces to look
for sections σ : X →LCC X of the projection LCC X →X.
In the C∞context such global sections σ : X →LCC X do exists (because
the ﬁbers of the bundle LCC X are contractible). But this is not the case in our
algebraic situation; so we must use a trick.
Let G be the group of K-algebra automorphisms of K[[t]]. So G ∼= GLn ⋉N,
where N is the subgroup of elements that act trivially modulo (t)2. The group N
is pro-unipotent. It turns out that Coor X is a G-torsor over X, locally trivial in
the Zariski topology.
Suppose we are given a ﬁnite number of sections
σ0, . . . , σq : U →LCC X
over some open set U ⊂X. Using an averaging process for unipotent group actions
[Ye4], we show that there exists a morphism
σ : ∆q
K × U →LCC X
which restricts to σj on the j-th vertex of ∆q
K.
Here ∆q
K is the q-dimensional
geometric simplex.
TWISTED DEFORMATION QUANTIZATION
15
Figure 2. Simplicial sections, q = 1. We start with sections over
two open sets U0 and U1 in the left diagram; and we pass to a
simplicial section σ on the right.
Since sections exist locally, we can choose an open covering U = {Ui} of X,
with sections σi : Ui →LCC X. For any i0, . . . , iq we then obtain a morphism
σ : ∆q
K × (Ui0 ∩· · · ∩Uiq) →LCC X.
(See Figure 2 for an illustration of the case q = 1.) As q varies we have a simplicial
section of the projection LCC X →X. Details are in [Ye2].
Another device we use is mixed resolutions. The mixed resolution MixU(Tpoly,X)
is a sheaf of DG Lie algebras on X, depending on the covering U, and equipped
with a DG Lie algebra quasi-isomorphism
Tpoly,X →MixU(Tpoly,X).
Likewise for Dpoly,X.
The simplicial section σ allows us to pull the L∞quasi-isomorphism Υω down
to X, giving an L∞quasi-isomorphism
Ψσ : MixU(Tpoly,X) →MixU(Dpoly,X)
between these sheaves of DG Lie algebras on X. The dependence on U and σ
disappears when we pass to homotopy classes.
