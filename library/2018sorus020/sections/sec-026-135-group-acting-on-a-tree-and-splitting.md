---
doc_id: 2018sorus020
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-026-135-group-acting-on-a-tree-and-splitting
section_title: "Group acting on a tree and splitting"
section_number: 1.3.5
pages: 34-36
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "HAL Id: tel-02108892 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 78 sections: Introduction"
---
Let X be an irreducible component of irreducible type ofX(Γ), which is reduced
and one dimensional, and letρ : Γ→ SL2(k(X)) be the tautological representation.
Let v∈ ˆX a point in the smooth projective model ofX, the pair (k(X),v ) is a
k-valuated ﬁeld, and we denote byTv the Bass-Serre tree described above. The
group Γ acts simplicially onTv as a subgroup ofSL2(k(X)) through the tautological
representation ρ. Although the representationρ is deﬁned up to conjugation, the
action on the Bass-Serre tree is well-deﬁned.
Proposition 1.3.11.The action ofΓ onTv is trivial if and only ifv∈ ˆX is a ﬁnite
point.
Proof. By deﬁnition, forv∈ ˆX a ﬁnite point, the ringk[X] is included inOv, which
means thatv(Yγ)≥ 0 for anyγ∈ Γ. Equivalently,Tr(ρ(γ))∈O v for anyγ∈ Γ,
and we want to prove that it is equivalent toρ(γ) to be conjugated to an element
of SL2(Ov). It is clear ifρ(γ) = ± Id, if not there exists a vectore∈ k(X)2 such
that{e,ρ (γ)e} is a basis of the two dimensional vector spacek(X)2, and in this
basis ρ(γ) acts as the matrix
( 0 1
−1 Tr(ρ(γ))
)
∈ SL2(Ov). Hence we have proved thatv
is a ﬁnite point iﬀ∀γ∈ Γ,ρ (γ)∈ SL2(Ov), and the proposition follows now from
Lemma 1.3.7.
33
Finite points and residual representations
If v is a ﬁnite point, Proposition 1.3.11 implies that the tautological representation
can be chosen, up to conjugation, to be of the formρ : Γ→ SL2(Ov), such a repre-
sentation will be saidconvergent. Given a convergent representationρ, we denote
by ¯ρ : Γ→ SL2(Ov)
mod t
−−−→SL2(k) the residual representation. Ifv corresponds to
the characterχ∈X, then the representation¯ρ is a lift ofχ.
Ideal points and incompressible surfaces
Here M is a 3-manifold with∂M = S1× S1, and Γ = π1(M). We pick an ideal
point v ∈ ˆX, and we know from Proposition 1.3.11 that no representativeρ of
the tautological representation converges (sends the whole groupΓ into SL2(Ov)).
Now we describe quickly how to construct, from the action ofΓ on Tv a surface
Σ ⊂ M, said dual to the action. The reader will ﬁnd many details about this
delicate construction in [Sha02, Til03].
The main point is to construct aπ1(M)-equivariant mapf : ˜M → Tv. Pick any
triangulation K of M, and lift it to aπ1(M)-invariant triangulation ˜K of ˜M ; then
pick a set of orbit representativesS(0) for the action of π1(M) on the set of 0-
simplices of ˜K, and any mapf0 :S(0)→Tv from this set to the set of vertices ofTv.
It induces an equivariant map from the0-squeleton of ˜K toTv, that we still denote
byf0 : ˜K(0)→Tv. Now it is possible to extend linearly this map to the1-squeleton,
as follows : pick a set of orbit representativesS(1) for the action ofπ1(M) on the
set of 1-simplices of ˜K. Any edgeσ∈ S(1) has endpoints mapped to some given
vertices through the mapf0, and we extend in the obvious wayf0 to σ. Now there
is a uniqueπ1(M)-equivariant extensionf1 : ˜K(1)→Tv of f0, it is continuous, and
can be made simplicial, up to subdivide the triangulation˜K. Repeat this process
up to obtain the desired simplicial, equivariant mapf : ˜M→Tv.
Now consider the set of midpointsE of the edges ofTv, the setf−1(E) is a surface
˜S⊂ ˜M. This surface is non-empty because the action ofπ1(M) on the treeTv is non
trivial, and orientable because the mapf is transverse toE. Moreover it is stable
under the action ofπ1(M) on ˜M, and hence its image through the covering map
˜M→ M is a surfaceS⊂ M, non empty and orientable, dual to the action. It is
worth to notice that it has no reason to be connected in general.
Remark1.3.12. Thereissomekindofconverseconstruction,whichmaybeexplains
the use of the term "dual". GivenS an oriented surface inM, and ˜S the preimage
ofS in the universal cover˜M, one can construct a treeTS as follows : vertices are in
34
bijection with the connected components on˜M\ ˜S, and they are joined with an edge
when the corresponding components are separated by a component of˜S. Because
the surface ˜S is π1(M)-invariant, this treeTS comes with a simplicial action of the
fundamental groupπ1(M). Moreover, the stabilizers of vertices are the fundamental
groups of the corresponding connected components ofM\S and stabilizers of edges
are the fundamental groups of the corresponding connected components ofS.
WheneverS is a surface produced by the action of the fundamental group on a tree
T, one has the following relation betweenTS andT : sinceTS is a retract of˜M, and
the mapf : ˜M→ T was constructed by extension to contractible cells, the com-
postion TS ↪→ ˜M
f
− →T if well-deﬁned and provides an injectiveπ1(M)-equivariant
map i : TS→ T, which can be made simplicial, after subdividingTS is necessary
(subdividing TS turns out to add parallel copies of˜S in ˜M in an equivariant way).
The mapi has no reason to be an isomorphism, but it implies that the stabilizers
of vertices ofTS (namely fundamental groups of connected components ofM\S)
are included in the stabilizers of some vertices ofT, and similarly for the stabilizers
of edges.
Deﬁnition 1.3.13.A surface Σ in a 3-manifoldM is saidincompressible if
1. Σ is oriented
