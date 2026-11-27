---
doc_id: arxiv-1507.06276v2
doc_title: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS"
section_id: sec-011-32-the-coproduct-on-u
section_title: "The coproduct on U"
section_number: 3.2
pages: 13-14
source_pdf: 1507.06276v2.pdf
source_sha256: f552aa5de7125b23
toc_source: outline
doc_brief: "UNIVERSAL K-MATRIX FOR QUANTUM SYMMETRIC PAIRS — Let g be a symmetrizable Kac-Moody algebra and let Uq(g) de- note the corresponding quantized enveloping algebra."
---
For(2) : Oint × Oint → Vect, (M,N ) ↦→ For(M ⊗N ) = For(M ) ⊗ For(N ),
(f,g ) ↦→ For(f ⊗g).
Let U (2)
0 = End( For(2)) denote the set of natural transformations from For(2)
to itself. Again, U (2)
0 is an algebra for which the multiplication · is given by
composition of natural transformations. The map
i(2) : U ⊗ U → U (2)
0 , (ϕM ) ⊗ (ψN ) ↦→(ϕM ⊗ψN )
14 MARTINA BALAGOVI ´C AND STEF AN KOLB
is an injective algebra homomorphism. However, it is not surjective, as the following
example shows.
Example 3.4. ForM,N ∈Ob(Oint) deﬁne a linear map
κM,N :M ⊗N →M ⊗N, m ⊗n ↦→q(µ,ν)m ⊗n if m ∈Mµ and n ∈Nν.
The collection κ = (κM,N )M,N ∈Ob(Oint) lies in U (2)
0 . However, one can show that
κ is not of the form ∑ n
k=1fi ⊗gi for any n ∈ N and any collection fi,gi ∈ U .
Henceκ does not lie in the image of the map i(2) described above.
The element κ is an important building block of the universal R-matrix for Uq(g),
see Section 3.3. For κ to be well deﬁned the ground ﬁeld needs to contain q(µ,ν) for
all µ,ν ∈P . This gives one of the reasons why we work over the ﬁeld K(q1/d).
Any natural transformation ϕ ∈ U can be restricted to all For(M ⊗N ) for
M,N ∈Ob(Oint). Moreover, restriction is compatible with composition and linear
combinations of natural transformations. Hence we obtain an alge bra homomor-
phism
∆U : U → U (2)
0 , (ϕM )M∈Ob(Oint) ↦→(ϕM⊗N )M,N ∈Ob(Oint).
We call ∆U the coproduct of U . The restriction of ∆U to Uq(g) coincides with
the coproduct of Uq(g) from Section 2.2. For this reason we will drop the subscript
U and just denote the coproduct on U by∆.
We would also like to consider families of linear maps ﬂipping the two tenso r
factors by a similar formalism. To that end consider the functor
For(2)op : Oint × Oint → Vect, (M,N ) ↦→ For(N ⊗M ) = For(N ) ⊗ For(M ),
(f,g ) ↦→ For(g ⊗f ).
Deﬁne U (2)
1 = Hom(For(2), For(2)op). For M,N ∈Ob(Oint) let
ﬂipM,N :M ⊗N →N ⊗M, m ⊗n ↦→n ⊗m
denote the ﬂip of tensor factors. Then ﬂip = (ﬂip M,N )M,N ∈Ob(Oint) is an element
of U (2)
1 . The direct sum
U (2) = U (2)
0 ⊕ U (2)
1
is a Z2-graded algebra where multiplication · is given by composition of natural
transformations. This is the natural algebra for the deﬁnition of t he commutativity
isomorphisms in the next subsection.
