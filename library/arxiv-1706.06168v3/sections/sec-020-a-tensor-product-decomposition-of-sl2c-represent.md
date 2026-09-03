---
doc_id: arxiv-1706.06168v3
doc_title: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization"
section_id: sec-020-a-tensor-product-decomposition-of-sl2c-represent
section_title: "A Tensor Product Decomposition of SL2(C) Representations"
section_number: null
pages: 31-34
source_pdf: 1706.06168v3.pdf
source_sha256: ab3383a95f369922
doc_brief: "A Representation Theoretic Explanation of the Borcea-Brändén Characterization — In 2009, Borcea and Br¨ and´ en characterized all linear oper ators on multivariate polynomials which preserve the"
---
In this appendix, we discuss in detail the decomposition of inner tens or products of SL 2(C) and (SL 2(C))m
representations. The results given here are for the most part st andard, and they are typically presented via
the theory of Lie groups and algebras (e.g., in [ FH13] and [ Hum12]). Here though, we discuss these results
in terms of the polynomial spaces V (n) and V (λ).
That said, the ﬁrst results we state demonstrate the importance of V (n) and V (λ) in the representation
theory of SL 2(C). In fact, these representations are precisely the irreducible re presentations of SL 2(C) and
(SL2(C))m, respectively (see Lecture 11 of [ FH13], and also Proposition 2.3.23 of [ Kow14]). We will not
make full use of this fact but will need the following simpler results.
Proposition A.1. For all n ∈ N0, we have that V (n) is an irreducible representation of SL2(C) of dimension
n + 1.
Proposition A.2. For all λ ∈ Nm
0 , we have that V (λ) ∼=V (λ1)⊠· · ·⊠V (λm) is an irreducible representation
of (SL2(C))m of dimension ∏
i(λi + 1).
In particular, outer tensor products of irreducible representat ions of SL2(C) are irreducible representations
of (SL 2(C))m. On the other hand, inner tensor products are not irreducible and their decomposition leads
to a natural deﬁnition of the apolarity form (see §3.2). We now set out to compute these decompositions,
which are often given as exercises in the literature (see, e.g., Exerc ise 11.11 of [ FH13]).
A.1 Decomposition of V (n) ⊗ V (m)
Fixn,m ∈ N0. We now consider the representation of SL 2(C) given by the inner tensor product, V (n)⊗V (m).
The importance of the tensor product comes from the fact that it relates to consideration of SL 2(C)-invariant
bilinear forms like the apolarity form. In particular, the decompositio n of the tensor product as a sum of
irreducible representations (Proposition A.7) will show us exactly how the D map (see Proposition 3.1) can
be used to deﬁne the apolarity form in the representation theoret ic context (Deﬁnition 3.3).
We begin with an important SL 2(C)-invariant map.
Proposition A.3. Let x and y denote the linear maps deﬁned on V (k) via multiplication by x and y,
respectively. The linear map U := (x ⊗y −y ⊗x) : V (n) ⊗V (m) →V (n + 1)⊗V (m + 1) is SL2(C)-invariant.
Proof. Straightforward computation, e.g., on simple tensors.
We then use this U map to show that Dk is not the zero map when k ≤m,n .
Lemma A.4. Fork ≤m ≤n, consider the map DU k :V (n −k) ⊗V (m −k) →V (n − 1) ⊗V (m − 1). We
have:
DU k =U kD +k(n +m −k + 1)U k−1
Proof. Follows from the fact that ( ∂xx −x∂x)p =p and (∂yy −y∂y)p =p.
Corollary A.5. Fork ≤m ≤n, consider the map DkU k :V (n −k) ⊗V (m −k) →V (n −k) ⊗V (m −k).
We have:
DkU k(xn−k ⊗xm−k) = k!(n +m −k + 1)!
(n +m − 2k + 1)! (xn−k ⊗xm−k) ⁄= 0
In particular, xn−k ⊗xm−k is in the image of Dk :V (n) ⊗V (m) →V (n −k) ⊗V (m −k).
Proof. Apply the previous lemma k times, and use the fact that D(xn−k ⊗xm−k) = 0.
We will use this fact about the image of Dk to determine the decomposition of V (n) ⊗V (m) into
irreducible components. We will also need the following fundamental r epresentation theory result.
31
Lemma A.6 (Schur’s Lemma). Let V,V ′,W be representations of a group G, and suppose V,V ′ are irre-
ducible. Then:
(i) Any G-invariant map π :W →V is either surjective or the zero map.
(ii) Any G-invariant map ι :V →W is either injective or the zero map.
(iii) Any G-invariant map ψ :V →V ′ is either an isomorphism or the zero map.
Further, if V,V ′ are vector spaces over an algebraically closed ﬁeld, then ψ is unique up to scalar.
Applying Schur’s lemma to each of the rth transvectants (discussed at the end of §3.2) yields the desired
representation decomposition.
Proposition A.7. Let m ≤n. We have the following decomposition of V (n) ⊗V (m), as a representation
of SL2(C), into irreducible components.
V (n) ⊗V (m) ∼=
⨁
r≤m
V (n +m − 2r)
In particular, V (n) ⊗V (n) ∼=V (2n) ⊕V (2n − 2) ⊕ · · · ⊕V (2) ⊕V (0).
Proof. For each r ∈ N0, ≤m, consider the SL 2(C)-invariantrth transvectant map:
V (n) ⊗V (m)
Dr
− − →V (n −r) ⊗V (m −r)
×
− →V (n +m − 2r)
By Corollary A.5, this map is not the zero map, as xn−r ·xm−r = xn+m−2r is in its image. Since V (n +
m − 2r) is irreducible by Proposition A.1, Schur’s lemma implies this map is surjective. This in turn implies
V (n) ⊗V (m) ∼= V (n +m − 2r) +Wr (as a representation) for some subspace Wr. Since this holds for all
r ≤m, we actually have
V (n) ⊗V (m) ∼=W +
⨁
r≤m
V (n +m − 2r)
for some subspace W . The sum of irreducible components here is direct, as any two distinc t irreducible
components must intersect trivially. To show that we can set W = 0, we use the following dimension
argument:
m∑
r=0
dim(V (n +m − 2r)) =
m∑
r=0
(n +m − 2r + 1) = (n + 1)(m + 1) = dim(V (n) ⊗V (m))
This completes the proof.
Along with the stated decomposition, we also obtain something else: t herth transvectant is a projection
from V (n) ⊗V (m) onto the irreducible component V (n +m − 2r). Schur’s lemma and the tensor product
decomposition then imply this projection is actually unique up to scalar . In a similar way, Schur’s lemma
also implies D and U must restrict to either a unique isomorphism or the zero map on each irreducible
component of V (n) ⊗V (m). In the following, we determine exactly what happens on each comp onent.
Theorem A.8. Consider the decomposition V (n) ⊗V (m) ∼=V (n +m) ⊕V (n +m − 2) ⊕ · · · ⊕V (n −m +
2) ⊕V (n −m). The maps
U :V (n) ⊗V (m) →V (n + 1) ⊗V (m + 1)
D :V (n + 1) ⊗V (m + 1) →V (n) ⊗V (m)
restrict to SL2(C)-invariant isomorphisms from V (n +m − 2r) to V (n +m − 2r) for all 0 ≤ r ≤ m ≤ n.
Additionally, D restricts to the zero map on V (n +m + 2).
32
Proof. By Schur’s lemma, the claim immediately follows if U is injective and D is surjective. That D is
surjective follows from the fact that the transvectant maps × ◦Dr are projections onto each of the irreducible
components ofV (n)⊗V (m) for 1 ≤r ≤m+1. That U is injective follows from the fact that U (v) = 0 implies
v = 0. One can see this by lexicographically ordering the basis {xjyn−j ⊗xkym−k : 0 ≤j ≤n, 0 ≤k ≤m}
and considering the highest component of a given v ∈V (n) ⊗V (m).
Our main application of this theory is given as follows. Consider the nth transvectant map × ◦ Dn :
V (n) ⊗V (n) → V (0) ∼= C, which is nonzero by the previous theorem. This map can be interpre ted as
an SL 2(C)-invariant bilinear form on V (n). It turns out that the apolarity bilinear form used in Grace’s
theorem also has this property, and this justiﬁes the following deﬁn ition.
Deﬁnition 3.3. We call the nth transvectant
V (n) ⊗V (n)
Dn
− − →V (0) ⊗V (0)
×
− →V (0) ∼= C
the apolarity form of V (n).
Corollary A.9. The apolarity form is the unique (up to scalar) nondegenerat e SL2(C)-invariant bilinear
form on V (n).
A.2 Decomposition of V (λ) ⊗ V (µ)
Fix λ,µ ∈ Nm
0 , and let V (λ) and V (µ) denote the irreducible representations of (SL 2(C))m given by the
outer tensor products:
V (λ) ∼=V (λ1) ⊠ · · · ⊠V (λm) V (µ) ∼=V (µ1) ⊠ · · · ⊠V (µm)
We next generalize the above results to the inner tensor product o f these two representations, V (λ) ⊗V (µ).
In particular, we determine the decomposition of this tensor produ ct and deﬁne a multivariate apolarity
form. Note that these statements strictly generalize the previou s analogous statements.
Proposition A.10 (c.f. Proposition A.7). Letµ ≤λ. We have the following decomposition of V (λ) ⊗V (µ),
as a representation of (SL2(C))m, into irreducible components.
V (λ) ⊗V (µ) ∼=
⨁
α≤µ
V (λ +µ − 2α)
Proof. We compute:
V (λ) ⊗V (µ) ∼=
(
V (λ1) ⊠ · · · ⊠V (λm)
)
⊗
(
V (µ1) ⊠ · · · ⊠V (µm)
)
∼=
(
V (λ1) ⊗V (µ1)
)
⊠ · · · ⊠
(
V (λm) ⊗V (µm)
)
∼=

 ⨁
α1≤µ1
V (λ1 +µ1 − 2α1)

 ⊠ · · · ⊠

 ⨁
αm≤µm
V (λm +µm − 2αm)


∼=
⨁
α≤µ
V (λ +µ − 2α)
The last step uses the distributive law for sums and tensor product s of representations.
Theorem A.11 (c.f. Theorem A.8). For any β ∈ Nm
0 , deﬁne U β :=U β1 ⊠ · · · ⊠U βm. Deﬁne Dβ similarly.
For any µ ≤λ ∈ Nm
0 , the maps
U β :V (λ) ⊗V (µ) →V (λ +β) ⊗V (µ +β)
Dβ :V (λ +β) ⊗V (µ +β) →V (λ) ⊗V (µ)
restrict to SL2(C)-invariant isomorphisms on the components of V (λ) ⊗V (µ) ∼= ⨁
α≤µV (λ +µ − 2α).
Finally, Dβ restricts to the zero map on the other irreducible component s of V (λ +β) ⊗V (µ +β).
33
Proof. Follows by induction on β, using Theorem A.8.
Deﬁnition 3.4 (c.f. Deﬁnition 3.3). We call the map
V (λ) ⊗V (λ)
Dλ
− − →V (0m) ⊗V (0m)
×
− →V (0m) ∼= C
the apolarity form of V (λ).
Corollary A.12 (c.f. Corollary A.9). The apolarity form is the unique (up to scalar) nondegenerat e
(SL2(C))m-invariant bilinear form on V (λ).
B The Grace-Walsh-Szeg˝ o Coincidence Theorem
A classical result in the representation theory of SL 2(C) is the fact that V (n) ∼= Symn(V (1)). Here,
Symn(V (1)) denotes the set of symmetric tensors in V (1)⊗n, or alternatively, the set of symmetric elements
inV (1n). That is, there is some SL 2(C)-invariant injection fromV (n) to V (1)⊗n, and by our conceptual the-
sis this map should transfer stability information. In fact, this idea is formalized in the Grace-Walsh-Szeg˝ o
coincidence theorem, and the injective map is known as the polarizat ion map.
