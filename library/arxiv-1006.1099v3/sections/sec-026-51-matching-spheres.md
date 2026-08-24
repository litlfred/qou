---
doc_id: arxiv-1006.1099v3
doc_title: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS IV AN SMITH"
section_id: sec-026-51-matching-spheres
section_title: "Matching Spheres"
section_number: 5.1
pages: 52-54
source_pdf: 1006.1099v3.pdf
source_sha256: 76c1c4173cdee9d8
doc_brief: "FLOER COHOMOLOGY AND PENCILS OF QUADRICS — There is a classical relationship in algebraic geometry bet ween a hyperelliptic curve and an associated pencil of quadric hypersurfaces."
---
matching cycle is by deﬁnition a path χ : [−1, 1]→ P1 in the base of a Lefschetz ﬁbration which
ends at distinct critical values (and is otherwise disjoint from the se t of critical values) and for
which the associated vanishing cycles are Hamiltonian isotopic in the ﬁb re over χ(0). Any path
between critical points for Z→ P1 is a matching path, by Lemma 4.1.
Lemma 5.1. Any matching path χ : [−1, 1]→ P1 for Z → P1 deﬁnes a Lagrangian sphere
Lχ⊂Z, unique up to Hamiltonian isotopy.
Proof. The monotone symplectic form on Z is restricted from a global K¨ ahler form onP2g+1×P1.
We deﬁne the sphere Lχ to be the vanishing cycle of the nodal algebraic degeneration of Z in
which two critical values coalesce along χ (such a degeneration is easily obtained by moving Z
in a Lefschetz pencil on P2g+1× P1). □
Remark 5.2. If one restricts to Z⁄=t for some t⁄∈χ, there is another description of this sphere.
By hypothesis the vanishing cycles associated to χ|[−1,0] and χ|[0,1] are Hamiltonian isotopic in
the ﬁbre Q0, by a Hamiltonian isotopy Hs. One can deform the symplectic connection of the
ﬁbration Z⁄=t→ C so that the parallel transport along χ|[−δ,δ] incorporates this isotopy, and
exactly matches up the boundaries of the two vanishing thimbles, cf . Lemma 8.4 of [9]. It is
standard that the two constructions give rise to the same Lagran gian sphere up to isotopy. Note
that the matching cycle construction, requiring a deformation of s ymplectic connection, a priori
only yields a Lagrangian sphere for a cohomologically perturbed symp lectic form on the total
space of Z, rather than of Z⁄=t, which is why the deﬁnition as a vanishing cycle is preferable.
A matching sphere Lχ can be oriented by choosing an orientation of the matching path χ
and of the vanishing cycle in the ﬁbre. (Since Dehn twists act on even -dimensional spheres by
reversing orientation, the latter choice will not generally be preser ved by monodromy.) The
FLOER COHOMOLOGY AND PENCILS OF QUADRICS 53
spheres Lχ are homologically essential, which implies that they are non-zero obje cts of F(Z),
with Floer homology additively given by H ∗(S2g+1).
Lemma 5.3. For a matching path γ⊂ C deﬁning Lγ⊂Z, HF (Lγ,L γ)∼=H ∗(S2g+1) as a ring.
Proof. From Lemma 3.2, there are natural maps
QH ∗(Z)→HF ∗(Lγ,L γ)→QH ∗(Z) (5.1)
whose composite is given by quantum product
QH ∗(Z)−→QH ∗(Z), α ↦→[Lγ]∗α
with the fundamental class [ Lγ]∈ QH ∗(Z). Let L†
γ denote the matching cycle associated to a
path meeting γ transversely once, so [L†
γ] and [Lγ] represent Poincar´ e dual cycles inZ. Equation
5.1 takes [L†
γ]↦→[Lγ]∗ [L†
γ]. The image is non-zero, since the classical cup-product of the class es
is±1 and deformation to the quantum product does not change the co eﬃcient in the maximal
cohomological degree. It follows that
QH ∗(Z)→HF ∗(Lγ,L γ)
is surjective, with 1 Z and [L†
γ] mapping to generators (the image of the ﬁrst is non-trivial by
unitality; the images of the two classes are distinct since they have d iﬀerent mod 2 degrees).
Since [L†
γ]∗ [L†
γ] = 0∈QH ev(Z) by graded commutativity, the Floer product in HF ∗(Lγ,L γ) is
undeformed. □
Seidel [87] proved there are no Lagrangian spheres in P2g+1, so these matching spheres neces-
sarily intersect the exceptional divisor E⊂Z. Any such intersection point lies on a ruling curve
R⊂E, which can then be viewed as a Maslov index 2 disk with (collapsed) boun dary on Lγ.
Lemma 5.4. For any matching path γ, the sphere Lγ∈ F(Z; 1).
Proof. Let L = Lγ, and ﬁx a Poincar´ e dual sphere L† as before. By Lemma 5.3, it suﬃces to
compute the coeﬃcient of the dual cycle [ L] in the quantum cup-product c1(Z)∗[L†]∈QH odd(Z).
A dimension count shows that only Chern class 2 spheres contribute , and the only such sphere
with a holomorphic representative is the ruling curve R, so we are interested in the algebraic
number ofR-curves passing through L,L† andE. The spinning construction of L andL† given in
Section 4.6 shows we can take them to come from (2 g− 1)-spheres inside E meeting transversely
once. The R-curve through that intersection point is then the unique curve wh ich contributes to
the product. □
Lemma 5.5. For a matching path γ⊂ C, the spun sphere ˆVγ and the matching sphere Lγ are
quasi-isomorphic objects of F(Z).
Proof. Take a loop Y →S1 of genus g curves {Σ t
g}t∈S1 with monodromy the Dehn twist tγ. Y
is obtained as the double cover of P1×S1 over a multi-section comprising 2 g constant sections
and a bi-section in which the branch points undergo a half-twist. The re is an obvious inclusion
֒Y→ C to a Lefschetz ﬁbration in which the curve deﬁned by γ has collapsed in the central
ﬁbre. Y deﬁnes algebraic Lefschetz ﬁbrations with generic ﬁbre Z in two ways. First, one can
construct a family of relative quadrics acquiring a node, with vanishin g cycleLγ, as in Lemma 5.1.
Second, one can consider the Lefschetz ﬁbration of (2 , 2)-intersections{Q2,2}t∈C with vanishing
cycle Vγ, deﬁne a family of relative quadrics by blowing up C∗× P2g+1 along C∗× (Q2,2)t, and
noting that the total space again extends to an algebraic Lefsche tz ﬁbration over C. The induced
monodromy around the circle is then a Dehn twist in ˆVγ, by Lemma 4.42. The constructions
exhibit both Lγ and ˆVγ as vanishing cycles for the algebraic degeneration of Z with monodromy
induced by tγ, which implies they are Hamiltonian isotopic. □
54 IV AN SMITH
Corollary 5.6. The subcategory P⊂ F(Z; 1) generated by the matching spheres Lγ for arbitrary
pathsγ has Hochschild cohomology HH ∗(P, P)∼=H ∗(Σ g).
Proof. Lemma 5.5 shows that P is the same as the subcategory deﬁned by spun spheres ˆVγ.
According to Lemma 4.44 this is in turn the subcategory which is the ima ge of the functor
Φ + :Tw πF(Q0∩Q1)→Tw πF(Z). On the other hand, this summand of the functor Φ is fully
faithful, by Lemma 4.38; and ﬁnally, the Hochschild cohomology of F(Q0∩Q1) (and hence its
split-closure) was calculated in Corollary 4.16. □
Remark 5.7. The relative quadric Z ⊂ P2g+1× P1 is a divisor of bidegree (2 , 1), from which
perspective it is straightforward to construct a Lefschetz penc il with ﬁbre Z and with vanishing
cycles matching spheres in the sense of Lemma 5.1. However, the cy cle class C(w) for the
corresponding ﬁbration w :BlZ∩Z′ (P2g+1× P1)→ P1 does not act nilpotently on HF (Lχ,L χ),
which means we can’t compute the Hochschild cohomology of P by direct appeal to Corollary
3.11. This accounts for the somewhat roundabout proof of Corolla ry 5.6, and its appeal to
Lemma 4.44.
We take the matching paths of the pentagram, Figure 1, and write A for the subcategory of
F(Z) generated by the associated matching spheres.
