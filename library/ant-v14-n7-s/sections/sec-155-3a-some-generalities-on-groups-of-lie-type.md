---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-155-3a-some-generalities-on-groups-of-lie-type
section_title: "3A. Some generalities on groups of Lie type"
section_number: null
pages: 297-298
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
follows, we begin by recalling some essentials about their blocks and characters.
Let q be a power of a prime. When G= G F is the group of ﬁxed points of a connected reductive
algebraic group G deﬁned over Fq under a Steinberg map F, the set of irreducible characters Irr(G) can be
written as a disjoint union ⨆ E(G, s) of so-called rational Lusztig series corresponding to G∗-conjugacy
classes of semisimple elements s∈ G∗ (i.e., elements of order relatively prime to q). Here G∗=(G∗)F∗
,
where(G∗, F∗) is dual to(G, F).
With this notation, we record the following lemma, proved in [Schaeffer Fry and Taylor 2018,
Lemma 3.4], which describes the action of H on the set of rational Lusztig series and will be useful
throughout this section.
Lemma 3.1. Let p be a prime and let s∈ G∗ be a semisimple element. Let f and b be integers and let
σ∈ H be such thatσ(ξ)=ξ p f
for all p′-roots of unityξ andσ(ζ)=ζ b for all p-power roots of unityζ .
Ifχ∈ E(G, s), thenχσ∈ E(G, s p f
p′ sb
p).
The characters in the series E(G, 1) are called unipotent characters, and there is a bijection E(G, s)→
E(CG∗(s), 1). Hence, characters of Irr(G) may be indexed by pairs (s,ψ) , where s∈ G∗ is a semisimple
element, up to G∗-conjugacy, andψ∈ Irr(CG∗(s)) is a unipotent character of CG∗(s). We remark that
CG∗(s) may fail to be connected, in which case unipotent characters of CG∗(s) are taken to be those lying
over a unipotent character of(CG∗(s)◦)F. In particular, we will denote by χs the character indexed by
(s, 1CG∗(s)), which are semisimple, and they have degree|G∗: CG∗(s)|q′.
Using [Cabanes and Enguehard 2004, Theorem 9.12], it follows that when p ∤q, the set Ep(G, 1):=⋃ E(G, s), where s ranges over elements of p-power order in G∗, is a union of p-blocks (ﬁrst shown
1964 Noelia Rizo, A. A. Schaeﬀer Fry and Carolina Vallejo
in [Broué and Michel 1989]) and that each such block intersects E(G, 1) nontrivially. Such blocks are
called unipotent blocks.
