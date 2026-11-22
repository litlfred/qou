---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-002-2-construction-of-weyl-group-representations
section_title: "Construction of Weyl group representations"
section_number: 2
pages: 2-4
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
We keep the notation introduced in part I, except that (until further notice) g can be any complex,
semisimple Lie algebra (not necessarily ≈go × go), b1 any Borel subalgebra of g containing the Cartan
subalgebra h. For any (not necessarily regular) λ ∈h∗we set
Ωλ = {ξ ∈g∗: p(ξ) = p(λ) for all G-invariant polynomials p on g∗}.
The map
pλ = pb1,λ : B∗→Ωλ, u · (b1, ν) →u · (λ + ν).
with u ∈U (compact form of G), ν ∈b1
⊥is then well-deﬁned and surjective for all λ ∈h∗.
Assume now λ regular. Then pλ is bijective and for any w ∈W we may deﬁne a transformation
aλ(w) = ab1,λ(w) of B∗by
aλ(w) = pwλ−1 ◦pλ : B∗→B∗.
It is evident that
aλ(wy) = ayλ(w)aλ(y).
(1)
If one could set λ = 0 in this equation, one would get an action of W on B∗, which would leave the
map po : B∗→Ω0 invariant, so that W would permute the ﬁbers of this map. This is of course only
trivially possible, as the ﬁbers are generically single points: the map p0 is the Springer map, which is a
desingularization π : B∗→N of the nilpotent cone Ωo = N in g∗[Steinberg 1976]. Borrowing an idea
of Kazhdan and Lusztig [1980] we look for what one might call a (proper) homotopy action of W on B∗,
meaning a homomorphism of W into the group of proper homotopy equivalences of B∗, rather than a
genuine action. But we shall not use the Kazhdan-Lusztig construction (which in fact they could not
prove to give a homotopy action); instead we use the aλ(w). (We shall prove in an appendix that our
construction agrees with Kazhdan-Lusztig’s, proving incidentally that their construction gives a homotopy
action after all. Of course, what we are ultimately interested in is a representation of W in homology, and
that they did obtain -at least for the top-dimensional homology. Several other constructions of (variants
of) this representation of W are known, ﬁrst of all Springer’s original construction [Springer 1976,1978],
another construction of Lusztig [1981], and others.)
We write out explicitly the deﬁnition of aλ(w) :
aλ(w)(u · (b1, ν)) = u′ · (b1, ν′) where u′ · (wλ + ν′) = u(λ + ν).
Thus
u′ · ν′ −u · ν = −u′ · wλ + u · λ
REPRESENTATIONS OF WEYL GROUPS
3
hence
|u′ · ν′ −u · ν| ≤const.|λ|.
Thus for λ close to 0 (but regular) the transformations aλ(w) leave the Springer map π : B∗→N
approximately invariant in the sense that
|π(aλ(w)(b, ν)) −π(b, ν))| ≤const.|λ|.
(2)
For any subset V of N let
B∗(V ) = {(b, ν) ∈B∗: ν ∈V },
the inverse image of V in B∗. We wish to constuct a proper homotopy action of W on B∗(V ). This
requires a regularity condition on V. Namely, for ﬁxed ϵ > 0, let U the be the ϵ-neighbourhood of V in N,
U = {ν ∈N : |ν −ν′| < ϵ for some ν′ ∈V },
and
B∗(U) = {(b, ν) ∈B∗: |ν −ν′| < ϵ for some ν′ ∈V }
(3)
its inverse image in B∗. We require that
for suﬃciently small ϵ > 0, the inclusion i : B∗(V ) →B∗(U) should admit a proper homotopy
inverse p : B∗(U) →B∗(V ), i.e.
p ◦i ∼1 on B∗(V ), and i ◦p ∼1 on B∗(U)
(4)
with “∼” meaning “properly homotopic”.
We observe that this condition is satisﬁed in either the following two cases:
(a) V is a ﬁnite subpolyhedron of a triangulation of N,
(5)
(b) V is a constructible subset of N, stable under scalar multiplications.
(6)
The ﬁrst condition may be explained as follows. Let ¯g∗= P(g∗⊕C) be the projective completion of g∗,
¯
N the closure of N in ¯g∗, ¯B∗the closure of B∗⊂B × N in B × ¯
N. As a projective algebraic variety, ¯
N
admits a triangulation [Hironaka 1975], hence (5) makes sense.
That (5) implies (4) is seen as follows. Assume (5). Then B∗(V ) is also a ﬁnite subpolyhedron of a
triangulation of B∗. It is an elementary fact that a ﬁnite subpolyhedron has a retractable neighbourhood
[Alexandroﬀ-Hopf, 1935, sections 6.1-2]. In particular B∗(V ) has a retractible neighbourhood W in B∗.
Since π is a proper map, there is a neighbourhood U of V in N so that π−1(U) ⊂W, which gives (4).
That the condition (6) also implies (4) is seen as follows. One may suppose that V excludes 0, as
a neighbourhood of 0 may be treated separately. Because of the assumption that V is stable under scalar
multiplications and excludes 0, one may then replace V by V ∩{|ν| = 1} in order to prove (4). Since V
is also constructible, one may apply (5).
From now on we shall assume that all sets V under consideration satisfy either (5) or (6), so that
(4) applies. (This may well be unnecessarily restrictive, but is suﬃcient for the applications we have in
mind.) It is clear from (2) and (3) that
aλ(w)B∗(V ) ⊂B∗(U)
for λ ∈h∗suﬃciently close to 0. Thus the transformation
aλ,V (w) = p ◦aλ(w) ◦i
(7)
REPRESENTATIONS OF WEYL GROUPS
4
of B∗(V ) is deﬁned for all regular λ in a small ball about 0 in h∗. Since these λ form a connected set, the
proper homotopy class aV (w) of aλ,V (w) is independent of λ, and the equation (1) implies that
aV (wy) = aV (w)aV (y)
so that the aV (w) give a proper homotopy action of W on B∗(V ).
As a consequence we have a representation of W in the homology with integral coeﬃcients, denoted
H∗(B∗(V ), Z). As in Kazhdan-Lusztig [1980], “homology” may here be understood either as “Borel-Moore
homology” or as relative homology H∗( ¯B∗(V ), ∂B∗(V ); Z) of the ﬁnite polyhedron ¯B∗(V ) with respect to
its ﬁnite subpolyhedron ∂B∗(V ) (see the explanations in connection with (5)). The coeﬃcient ring Z will
be omitted from the notation when understood or unimportant.
For the further analysis of the representations of W in these H∗(B∗(V )) we follow Kazhdan-Lusztig
[1980]. Suppose X ⊂Y are closed subvarieties of N, and put U = Y −X. There is a long exact sequence
· · · →Hi+1(B∗(U)) →Hi(B∗(X)) →Hi(B∗(Y )) →Hi(B∗(U)) →Hi−1(B∗(X)) →· · ·
(8)
In top degree, when i = 2m, m = dimCB∗(Y ),
H2m+1(B∗(U)) = 0, trivially, and the boundary map
H2m(B∗(U)) →H2m−1(B∗(X)) is = 0 because the topological boundary of a complex variety has real
codimension at least 2. So (8) leads to the short exact sequence
0 →H2m(B∗(X)) →H2m(B∗(Y )) →H2m(B∗(U)) →0
(9)
The maps (7) and (9) are W-maps.
