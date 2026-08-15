---
doc_id: arxiv-0811.2435v1
doc_title: "Stability structures, motivic"
section_id: sec-026-orientation-data-from-a-splitting-of-bifunctors
section_title: "Orientation data from a splitting of bifunctors"
section_number: null
pages: 83-84
source_pdf: 0811.2435v1.pdf
source_sha256: 615b04eca83bcade
doc_brief: "Stability structures, motivic — 43 sections: Introduction; Counting problems for 3-dimensiona; Non-commutative varieties with pol"
---
LetC be a triangulated ind-constructive category over a ﬁeld k. We will
assume that all functors, bifunctors etc. respect this stru cture. In this section
we are going to discuss a special framework in which orientat ion data is easy
to construct.
Let F :C×C op→Perf (Spec(k)) be a biadditive bifunctor and d be an
integer. We deﬁne the dual bifunctor of degree d as a bifunctor F∨ = F∨,d
given by
F∨(E2,E 1) := F (E1,E 2)∗[−d] .
Clearly F↦→F∨ is an involution.
Deﬁnition 16 A self-duality structure on F of degree d is an isomorphism
F→F∨ of bifunctors such that for any two objects E1,E 2 the induced non-
degenerate pairing
F (E1,E 2)⊗F (E1,E 2)→ k[−d]
is symmetric on the level of cohomology H•(F (E1,E 2)). If F is endowed with
a self-duality structure of degree d then we call it self-dual.
For a Calabi-Yau category of dimension d the bifunctor ( E1,E 2) ↦→
Hom•(E1,E 2) is self-dual.
For any self-dual bifunctorF of odd degree d we can repeat considerations
of Section 5.2. Namely, we deﬁne an ind-constructible super line bundleDF
with the ﬁber DF
E := sdet(F (E,E )). Then for any exact triangle E1→E2→
E3 we have a canonical isomorphism
√
D
F
E2⊗ (
√
D
F
E1)−1⊗ (
√
D
F
E3)−1≃ sdet(F (E1,E 3))⊗2.
Then one can ask the same question: is there an ind-constructible super
line bundle
√
DF which is compatible with the above isomorphism in the sense
of Deﬁnition 15?
The answer is positive for any bifunctor of the form F≃H⊕H∨, with
the obvious self-duality structure. In this case we set
√
DFE := sdet(H(E,E )) .
83
More generally we can use an A1-homotopy in this special case. More pre-
cisely, suppose we are given a bifunctor 18 G : C×C op → Perf (A1
k). It
can be thought of as a family Gt :C×C op→ Perf (Spec(k)) of bifunctors,
parametrized by t∈ A1(k), namely Gt = i∗
t◦G, where it : Spec(k)→ A1
is the embedding corresponding to t. Since the category Perf (A1
k) has an
obvious duality functor (taking dual to a complex of vector b undles) then
the deﬁnition of self-duality structure extends naturally to families. Sup-
pose that we have a family of self-dual bifunctors Gt,t ∈ A1(k) such that
G0 ≃ Hom•(•,•) and G1 ≃ H⊕H∨ for some bifunctor H, and the iso-
morphisms preserve the self-duality structures. Then we ha ve a canonical
orientation data on C, since any super line bundle over A1
k is trivial and all
ﬁbers are canonically isomorphic.
