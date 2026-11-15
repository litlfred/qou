---
doc_id: arxiv-1608.03227v4
doc_title: "Knot homology and sheaves on the Hilbert scheme of points on the plane"
section_id: sec-033-63-induction-functor-in-reduced-case
section_title: "Induction functor in reduced case"
section_number: 6.3
pages: 33-34
source_pdf: 1608.03227v4.pdf
source_sha256: c71128e9a6c35343
toc_source: outline
doc_brief: "Knot homology and sheaves on the Hilbert scheme of points on the plane — For each braid β ∈Brn we construct a 2-periodic complex Sβ of quasi-coherent C∗× C∗- equivariant sheaves on the"
---
Lie(Pk) × n. We also use notation W for the restriction of the potential W on the subspace X 2(Pk).
There is a natural embedding ¯ik : X 2(Pk) →X 2(Gn).
The map of the rings ¯ik : C[X 2(Gn)] →
C[X 2(Pk)] is the projection map with the kernel (Πk
−−(g)) and it is easy to see that these generators form
a regular sequence. Thus we have a well-deﬁned functor:
¯ik∗: MFsc
B2(X 2(Pk), W) →MFsc
B2(X 2(Gn), W).
We also have the projection map ¯pk : X 2(Pk) →X 2(Gk) × X 2(Gn−k).
The map ¯pk is B2
k × B2
n−k-equivariant and we extend B2
k × B2
n−k-equivariant structure to B2
n-equivariant
structure to obtain an induced map
¯p∗
k : MFsc
B2
k(X 2(Gk), W) × MFsc
B2
n−k(X 2(Gn−k), W) →MFsc
B2
n(X 2(Pk), W).
Thus we deﬁne
indk := ¯ik∗◦¯p∗
k.
Now let us discuss an analogs of the map ρk for reduced spaces and the corresponding properties of the
push forward ¯ik∗. Consider a space X
♭
2(Gn) := b × gln × n. There is a natural embedding ¯jn : X 2(Gn) →
X 2(Gn)♭induced by the embedding Gn →gn. If we deﬁne W
♭(X, g, Y ) = Tr(X(gY adj(g))) then we have
¯j∗
n(W
′) = W
♭, W
′ = W · det(g) and map
¯j∗
n : MFsc
B2
n(X 2(Gn)♭, W
♭) →MFsc
B2
n(X 2(Gn), W
′)
is well-deﬁned.
Similarly we deﬁne X 2(Pk) and X 2(Pk)♭. The natural open embedding ¯jk
n : X 2(Pk) →X 2(Pk)♭induces
the pull back map
¯jk∗
n : MFsc
B2(X 2(Pk), W
′) →MFsc
B2(X 2(Pk)♭, W
♭).
There is a natural linear projection
¯ρk : X 2(Gn)♭→X 2(Pk)♭
and a pull back map
¯ρ∗
k : MFsc(X 2(Pk)♭, W
♭) →MFsc(X (Gn)♭, ρ∗
k(W
♭)).
33
We can choose F′ ∈MFsc
B2(X2(Gn)♭, W) such that ¯jk∗
n (F′) = det(F) and we deﬁne
˜F := det−1 ◦¯jk∗
n ◦¯ρ∗
k(F′) ∈MFsc(X2(Gn), ¯jk∗
n ◦¯ρ∗
k(W
♭) · det−1).
Let δkW = W −¯jk∗
n ◦¯ρ∗
k(W
♭)/ det, then analogously to the non-reduced case we have:
¯ik∗(F)♯= ˜F ⊗KδkW (Πk
−−(g12)).
