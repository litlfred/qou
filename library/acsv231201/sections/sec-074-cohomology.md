---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-074-cohomology
section_title: "Cohomology"
section_number: null
pages: 493-495
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
Finally, we deﬁne a product on pairs by
(X′, Y′)× (X′′, Y′′) = (X′× X′′, X′× Y′′∪ Y′× X′′) .
One nice property of this deﬁnition is that the singular chain complexC(X, Y)
for a pair ( X, Y) = (X′, Y′)× (X′′, Y′′) turns out to be isomorphic to a tensor
product of the singular chain complexes for the pairs (X′, Y′) and (X′′, Y′′). The
K¨unneth product formula for chain complexes results in a homology formula
for products of pairs.
Corollary B.17 (K¨unneth formula for pairs). For pairs (X′, X′′) and (Y′, Y′′),
Hn(X′× X′′, X′× Y′′∪ Y′× X′′) = Hn((X′, Y′)× (X′′, Y′′))

⨁
p+q=n
Hp(X′, Y′)⊗ Hq(X′′, Y′′).
B.3 Cohomology
Given a chain complex
···→ Cn+1
∂n+1
−−−→Cn
∂n
−→Cn−1→···
we may replace each vector space Cn by its dual Cn consisting of linear maps
from Cn to C. As for homology, we consider cohomology with complex co-
eﬃcients. The elements of Cn are called n-cochains and the boundary map
∂n : Cn→ Cn−1 on n-chains induces a dual mapδn : Cn−1→ Cn on n-cochains:
if f ∈ Cn−1 is a linear map from Cn−1 toC thenδn( f )∈ Cn is the linear map
f◦∂n from Cn toC. It can be veriﬁed thatδn◦δn−1 = 0 for all n, so we have a
cochain complex
···← Cn+1 δn
←−Cn δn−1
←−−−Cn−1←··· .
The quotient of the kernel of δn (the n-cocycles) by the image of δn−1 (the n-
coboundaries) is called the nth cohomology group ofC and is denoted Hn(C).
The value of an n-cocycle ν evaluated at an n-cycle σ depends only on the
cohomology class [ν] ofν and the homology class [σ] ofσ, so this evaluation
deﬁnes a product ⟨ω,η⟩ for ω∈ Hn(C) and η∈ Hn(C). IfC =C(X) is the
singular chain complex (or smooth chain complex) of a topological space X,
then we use the notation Cn(X) = Cn for the singular n-cochains of X and
Hn(X) = Hn(C) for the nth singular cohomology group of X. If X is a cell
complex then Hn(X) is the dual space of Hn(X).
476 Algebraic topology
The functor taking a topological space to its singular or smooth chain com-
plex is covariant, as is the functor from a chain complex to its homology
groups. Hence, as noted above, any map f : X → Y of topological spaces
induces maps f∗ :C(X)→C (Y) and f∗ : H∗(X)→ H∗(Y). Conversely, the
singular or smooth cochain complex of a space is a contravariant functor, so a
map f : X→ Y induces a map f∗ : H∗(Y)→ H∗(X).
On a manifold we may identify a p-formω with the smooth p-cochain de-
ﬁned by α ↦→
∫
αω. Using the deﬁnition of the coboundary δ and Stokes’s
Theorem,
δω(C) =ω(∂C) =
∫
∂C
ω =
∫
C
dω = dω(C).
In other words,δω = dω, so cocycles correspond to closed forms and we have
the following.
Theorem B.18 (integral depends only on homology class). Letω be a closed
p-form holomorphic on an embedded complex manifoldM⊆ Cn (if p = n then
ω is always closed). Let C be a singular p-cycle on M. Then
∫
Cω depends
onC only via the homology class [C] ofC in H p(M) and on ω only via the
cohomology class [ω] ofω in H p(M). □
This theorem is one reason for our detour into topology. Another is the de
Rham Theorem. Let ι be the map that takes the smooth p-formω and maps it
to the p-cochainC↦→
∫
Cω asC varies over p-chains. This map is in general
not a bijection: there may be linear maps on chains that are not represented by
integrals of smooth forms. Nevertheless, the induced mapι∗ will be an isomor-
phism from the singular cohomology of M with coeﬃcients in R orC to the
cohomology H∗
DR of the de Rham complex of smooth p-forms with cobound-
ary given by the diﬀerential operator d.
Theorem B.19 (de Rham Theorem). Let X be a real manifold. The identiﬁca-
tion of p-forms with cochains induces an isomorphism H∗
DR(X) H∗(X).
Proof See [Lee03, Theorem 18.7]. □
Remark. A product called the cup product may be deﬁned on cochains, sat-
isfying a product rule with respect to the d operator. The cup product endows
cohomology with the structure of a graded C-algebra, and the isomorphism
in the de Rham Theorem is in fact a ring isomorphism, mapping the wedge
product to the cup product.
