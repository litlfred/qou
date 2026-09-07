---
doc_id: arxiv-1608.07308v1
doc_title: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY"
section_id: sec-021-34-from-rouquier-complexes-to-khovanov-rozansky
section_title: "From Rouquier complexes to Khovanov-Rozansky homology"
section_number: 3.4
pages: 22-23
source_pdf: 1608.07308v1.pdf
source_sha256: bcc3b6f1a91a55c6
doc_brief: "FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY — We construct a categoriﬁcation of the maximal commutative subalgebra of the type A Hecke algebra."
---
2 ,
it is clear thatσi does not correspond to any Soergel bimodule. However, Rouquier showed that
σi can be realized in the homotopy category of complexes:
Kb(SBimn)
where we use the variable s to keep track of homological degree. Explicitly, objects in the
homotopy category of complexes will be denoted by:[
skMk→...→sk′
Mk′
]
for somek≤k′∈ Z. The variables may seem redundant when writing down chain complexes,
but we keep track of it for two reasons: ﬁrst of all, it will give rise to the equivariant parameter
t of Section 2 via (1.8). Second of all, we think of the object:
[M→sM′]∈Kb(SBimn)
as the cone of a morphism between the objectsM andsM′, and thus the power ofs makes the
homological degrees of our formulas manifest. Recall the Bott-Samuelson bimodules (3.9) and
consider the Rouquier complexes:
(3.12) σi :=
[
Bi
1⊗1↦→1
−−−−→sR
q
1
2
]
, σ −1
i :=
[
q
1
2R
s
1↦→xi⊗1−1⊗xi+1
−−−−−−−−−−→Bi
]
They satisfy the following equations [39, 52] (which can be deduced from (3.10) and (3.11)):
σi⊗σ−1
i
∼=σ−1
i ⊗σi∼= 1,
σi⊗σj∼=σj⊗σi for |i−j|> 1,
σi⊗σi+1⊗σi∼=σi+1⊗σi⊗σi+1,
and hence categorify the braid group. To any braidσ =∏n−1
i=1 σai
i (whereαi∈{− 1, 0, 1}) one
can associate a complex of bimodules obtained by tensoring together the various complexes
FLAG HILBERT SCHEMES, COLORED PROJECTORS AND KHOV ANOV-ROZANSKY HOMOLOGY 23
(3.12). We abuse notation and denote the resulting complex also by σ. Khovanov [39] deﬁned
the HOMFLY-PT homology of a braidσ as:
(3.13) HHH(σ) := RHomKb(SBimn)(1,σ ).
The right hand side is a triply graded vector space, endowed with the internal gradingq, the ho-
mological gradings of the complexes (3.12) and their coproducts, and the Hochschild grading
a given by taking theRHom. The appropriate derived category formalism can be found in [36].
With respect to these three gradings, Khovanov proved that (3.13) is a topological invariant of
the closure ofσ, after a certain renormalization.
Corollary 3.4. Letσ,σ′ be any two braids. Then:
HHH(σσ′) = RHomKb(SBimn)(1,σ⊗σ′) and HHH(σ′σ) = RHomKb(SBimn)(1,σ′⊗σ)
are isomorphic asR-modules, up to a twist bywσ.
The above formula follows from Corollary 4.19, which applies to all invertible objects in a
monoidal category.
Proposition 3.5. The Soergel bimoduleBi is self biadjoint, for all i. The Rouquier complex σ
for a braidσ is biadjoint toσ−1.
The second statement of the above Proposition also follows from Corollary 4.18 below,
which is quite general, and actually implies the following stronger result:
Corollary 3.6. For anyA,A′∈ SBimn and any braidσ there are canonical isomorphisms:
RHomKb(SBimn)(A⊗σ,A′⊗σ)∼= RHomKb(SBimn)(A,A′)∼= RHomKb(SBimn)(σ⊗A,σ⊗A′).
