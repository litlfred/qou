---
doc_id: arxiv-0707.2003v2
doc_title: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Univers"
section_id: sec-004-4-hochschild-homology-and-dg-algebras
section_title: "Hochschild homology and dg-algebras"
section_number: 4
pages: 12-14
source_pdf: 0707.2003v2.pdf
source_sha256: 0b8fe37aabeee412
doc_brief: "A geometric model for Hochschild homology of Soergel bimodules BEN WEBSTER GEORDIE WILLIAMSON School of Mathematics Mathematisches Institut Institute for Advanced Study der Universität Freiburg — An"
---
Recall that the Hochschild homology of an S⊗ S -module R can be deﬁned as
HH∗(R) = S
L
⊗S⊗S R
where S has been made into an S⊗S algebra by the multiplication map. Since
S∼=AB and S⊗ S∼=AB×B , this map is that induced by the diagonal group
homomorphism֒→B× B . Thus, we expect that the geometric analogue of
taking Hochschild homology is restricting from a B× B -action to the diagonal
B .
However, we must be careful about the difference between dg- modules and
modules. Hochschild homology is an operation on S− S -bimodules, not dg-
bimodules. Thus, to make a precise statement requires us to r estrict to formal
complexes.
Deﬁnition 5 Let M∈ dgModAG be a dg-module. If M∼= H ∗(M ) in dgModAG
we say that M is formal. Similarly ,F∈ DG(pt) is formal if Γ G(F) is.
The following proposition connects the Hochschild cohomology of formal equiv-
ariant sheaves with another equivariant cohomology . This i s our main techni-
cal tool.
12
Proposition 4.1 SupposeF∈ DB×B(pt) is formal. Then one has an isomor-
phism:
⨁
i
HHi(H∗
B×B(F))[i]∼= H∗
B(resB
B×BF)
as graded S -modules.
Furthermore this isomorphism is functorial. That is, if F andG are formal
sheaves in DB×B(pt), and ϕ :F →G is a morphism, the maps H∗
B(ϕ) and
HH∗(H∗
B×B(ϕ)) commute with this isomorphism.
Proof of Proposition 4.1 In order to work out the Hochschild homology of
H∗
B×B(F) we may take a free resolution of H∗
B×B(F) by S⊗ S -modules:
0→ P−2n→···→ P−1→ H∗
B×B(F)
We then apply S⊗S⊗S− and take cohomology . However, becauseH∗
B×B(F)∼=
Γ B×B(F) in dgModAB×B , we may also regard ⨁ Pi[−i] as aK-projective res-
olution of Γ(F). By Theorem 3.3 we have:
H∗
B(resB
B×BF)∼= H ∗(S
L
⊗S⊗S H∗
B×B(F))∼=
⨁
HHi(H∗
B×B(F))[i]
Proof of Theorem 1.2 LetF denote the image of the intersection cohomol-
ogy sheaf on BwB in DB×B(pt). We will see in the next section that F is
formal. Hence we can apply the above proposition. However, w e also know
that H∗
B×B(F) is the indecomposable Soergel bimodule Rw . Hence:
⨁
i
HHi(Rw)[i]∼= H∗
B(resB
B×BF)
But resB
B×B commutes with the map to a point and resB
B×B(IC(Gw))∼= IC(Gw)
(Lemma 3.4). Hence:
⨁
i
HHi(Rw)[i]∼= H∗
B(IC(Gw))
This then yields the main theorem.
13
