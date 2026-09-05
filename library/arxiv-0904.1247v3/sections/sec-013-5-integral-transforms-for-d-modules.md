---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-013-5-integral-transforms-for-d-modules
section_title: "Integral transforms for D-modules"
section_number: 5
pages: 30-34
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — W e apply the ideas of derived algebraic geometry and topolog ical ﬁeld theory to the representation theory of reductive groups."
---
We continue with our standing assumptions of preceding sections. I n particular, by a scheme, we
mean a quasi-compact, separated derived scheme. By a stack, we mean a quasi-compact stack with
aﬃne diagonal, and by a representable morphism, we mean a quasi-co mpact schematic morphism.
A stack is safe if its de Rham cohomology functor is continuous, and m ore generally, a morphism is
safe if the pushforward of D-modules along it is continuous.
In the previous section, we recalled that for any stacks X1,X 2, external tensor product induces
an equivalence
D(X1)⊗D (X2) ∼ /d47/d47D(X1×X2).
Verdier duality induces a canonical self-duality
D(X1)≃D (X1)′
If in addition X1 is safe, then the integral transform construction provides a des cription of the
resulting equivalence
D(X1×X2) ∼ /d47/d47 FunL(D(X1),D (X2)) M ✤ /d47/d47π2∗(π!
1(−)⊗ M)
The above equivalences ﬁt into a canonically commuting diagram
D(X1)⊗D (X2)
∼
/d15/d15
∼ /d47/d47D(X1×X2)
∼
/d15/d15
D(X1)′⊗D (X2) ∼ /d47/d47 FunL(D(X1),D (X2))
Namely, for M1∈D (X1), M2∈D (X2), there is a canonical identity
π2∗(π!
1(−)⊗ (π!
1M1⊗π!
2M2))≃ Γ(X1, M1⊗− )⊗ M2≃ HomD(X1)(DX1 M1,−)⊗ M2
between going around the upper right and the lower left parts of th e diagram.
30
In this section, we will record some simple relative versions of the abo ve assertions. While we
will consider very restrictive hypotheses, the assertions often f ail in any more relaxed setting.
5.1. F unctoriality over schemes. We will not need the results of this section but they naturally
ﬁt into the theme of the paper and are likely useful elsewhere.
Theorem 5.1. For a diagram X1 → Y ← X2 where X1,X 2 are stacks and Y a scheme, the
canonical map induced by !-pullbacks is an equivalence
D(X1)⊗D(Y )D(X2) ∼ /d47/d47D(X1×Y X2).
Proof. The tensor product of D(Y )-modules can be calculated as the geometric realization of the
two-sided bar construction ([L2, 4.3.4]), the simplicial category with k-simplices
D(X1)⊗D (Y )⊗···⊗D (Y )⊗D (X2),
where the factor D(Y ) appears k times and the maps are given by the D(Y )-module structures in
the usual pattern. This is canonically equivalent to the simplicial cate gory with k-simplices
D(X1×Y×···× Y×X2)
where the factor Y appears k times and the maps are given by !-pullbacks in the usual pattern.
This extends to an augmented simplicial category with augmentation given by the pullback
j!
−1 :D(X1×X2) /d47/d47D(X1×Y X2)
along the relative diagonal
j−1 :X1×Y X2 /d47/d47X1×X2
The map j−1 is a base change of the diagonal map of Y , and since Y is a separated scheme, j−1 is
a closed embedding.
Similarly, the analogous diagonal maps
jk :X1×Y×···× Y×X2 /d47/d47X1×Y×···× Y×Y×X2
where the factor Y appears k times in the domain and k + 1 times in the codomain are closed
embeddings.
Now let us consider pushforwards along the above closed embedding s and apply Kashiwara’s
lemma: for a closed embedding j and a D-module M, the natural adjunction map M→j!j∗M is
an equivalence. Thus by base change, the pushforward
j−1∗ :D(X1×Y X2) /d47/d47D(X1×X2)
and its higher analogues
jk∗ :D(X1×Y×···× Y×X2) /d47/d47D(X1×Y×···× Y×Y×X2)
provide a lift to a split augmented simplicial category.
Finally, by [L1, Lemma 6.1.3.16], in any ∞-category, split augmented simplicial diagrams are
colimit diagrams. □
Theorem 5.2. Let X be a stack, Y a scheme, and f : X→ Y a safe morphism (for example, a
relative Deligne-Mumford stack). Then D(X) is a self-dual module over D(Y ).
Proof. By Theorem 5.1, we have a canonical equivalence
D(X)⊗D(Y )D(X)≃D (X×Y X).
Thus we can deﬁne a unit and counit by the correspondences
u = ∆ ∗f ! :D(Y ) /d47/d47D(X×Y X)≃D (X)⊗D(Y )D(X)
c =f∗∆ ! :D(X)⊗D(Y )D(X)≃D (X×Y X) /d47/d47D(Y )
31
where ∆ : X→X×Y X is the diagonal. Here we assume f :X→Y is safe to ensure the continuity
of the functor f∗.
We must check that the following composition is the identity
D(X)
u⊗id /d47/d47D(X)⊗D(Y )D(X)⊗D(Y )D(X)
id ⊗c /d47/d47D(X).
Consider the following commutative diagram with Cartesian square:
X
∆
/d15/d15
∆ /d47/d47X×Y X
π1 /d47/d47
id1×∆ 23
/d15/d15
X
X X ×Y X
π2/d111/d111 ∆ 12×id3 /d47/d47X×Y X×Y X
Using standard identities for composition and base change, we calcu late
(id⊗c)◦ (u⊗ id) = π1∗(id1× ∆ 23)!(∆ 12× id3)∗π!
2
≃ π1∗∆ ∗∆ !π!
2
≃ idD(X).
□
If X1 → Y is safe as in the previous theorem, and X2 → Y is arbitrary, then the integral
transform construction gives linear functors
D(X1×Y X2) /d47/d47 FunL
D(Y )(D(X1),D (X2)) M ✤ /d47/d47π2∗(π!
1(−)⊗ M)
Its evident compatibility with the self-duality of Theorem 5.2 and the id entiﬁcation of Theorem 5.1
immediately implies the following.
Corollary 5.3. Let X1,X 2 be stacks, Y a scheme, X1→ Y a safe morphism, and X2→ Y an
arbitrary morphism. Then the natural maps are equivalences
D(X1)⊗D(Y )D(X2) ∼ /d47/d47D(X1×Y X2) ∼ /d47/d47 FunL
D(Y )(D(X1),D(X2))
factoring the self-duality of D(X1) overD(Y ).
5.2. F unctoriality over classifying stacks. In this section, we present an equivariant general-
ization of Theorem 5.2 and its corollary realizing linear functors via inte grals kernels on the ﬁber
product. Unfortunately, results of this nature do not hold in grea t generality, but we will be content
with the case when the base stack Y is the classifying stack BG of an aﬃne group scheme G. What
we speciﬁcally use is the restrictive property that the diagonal map of such stacks is smooth.
Proposition 5.4. For a stack Y with smooth diagonal, the monoidal category D(Y ) is semi-rigid
with a canonical pivotal structure.
Proof. SinceD(Y ) is compactly generated and symmetric monoidal, it suﬃces to check that any
compact object is dualizable.
For any compact object M∈D (Y ), we will show that the monoidal dual is the shifted Verdier
dual DY (M)[2 dimY ]∈D (Y ).
Following the discussion of Section 2.2.1, it suﬃces to establish for any compact object M∈D (Y ),
and arbitrary objects L, N∈D (Y ), that there is a functorial equivalence
(3) Hom D(Y )(L⊗ M, N)≃ HomD(Y )(L, N⊗ DY (M)[2 dimY ])
Observe that it suﬃces to establish the equivalence for L, N∈H compact objects. For arbitrary
objects L, N∈H , it then follows by continuity by taking colimits ﬁrst in N then in L.
32
Using that the diagonal ∆ : Y → Y ×Y is smooth of relative dimension − dimY , note the
following functorial equivalence
DY (L⊗ M) = DY ∆ !(L ⊠ M)
≃ ∆ ∗(DY (L) ⊠ DY (M))
≃ ∆ !(DY (L) ⊠ DY (M))[2 dimY ]
≃ DY (L)⊗ DY (M)[2 dimY ]
Now returning to the sought after equivalence (3), we ﬁnd functo rial equivalences
HomD(Y )(L⊗ M, N) ≃ HomD(Y )(CY, DY (L⊗ M)⊗ N)
≃ HomD(Y )(CY, (DY (L)⊗ DY (M)[2 dimY ])⊗ N)
≃ HomD(Y )(L, DY (M)[2 dimY ]⊗ N)
□
Remark 5.5. Implicit in the proposition is the Poincar´ e duality identity DY (ωY )[2 dimY ]≃ ωY
since the dual of the monoidal unit must be the monoidal unit.
Corollary 5.6. Let Y be a stack with smooth diagonal, X a stack, and X → Y an arbitrary
morphism. Then D(X) is self-dual as a D(Y )-module.
Proof. As a plain category, D(X) is self-dual, so the previous proposition and Proposition 3.14
imply the corollary. □
If X1,X 2 are stacks, X1→ Y is safe and X2→ Y is arbitrary, then there is a canonical map
induced by !-pullbacks
Ψ : D(X1)⊗D(Y )D(X2) /d47/d47D(X1×Y X2)
and the integral transform construction gives linear functors
Φ : D(X1×Y X2) /d47/d47 FunL
D(Y )(D(X1),D (X2)) Φ M =π2∗(π!
1(−)⊗ M)
Tracing back through the constructions and applying standard ide ntities, the functors Ψ , Φ evidently
provide a factorization
D(X1×Y X2)
Φ
/d41/d41❙❙❙❙❙❙❙❙❙❙❙❙❙❙
D(X1)⊗D(Y )D(X2) ∼ /d47/d47
Ψ
/d53/d53❧❧❧❧❧❧❧❧❧❧❧❧❧❧
FunL
D(Y )(D(X1),D(X2))
of the equivalence provided by Corollary 5.6. In general neither Ψ , Φ is itself an equivalence, but
we have the following.
Proposition 5.7. Let Y be a smooth stack with smooth diagonal, X1,X 2 stacks, X1→ Y a safe
morphism, and X2→Y an arbitrary morphism.
Then the integral transform Φ admits a fully faithful left adjoint Φ L.
Proof. Tracing back through the algebraic arguments leading to Propositio n 3.14, one sees that the
functor category Fun L
D(Y )(D(X1),D(X2)) can be calculated as the limit of the cosimplicial category
with k-cosimplices
D(X1×Y×···× Y×X2)
where the factor Y appears k times and the maps are given by pushforwards in the usual pattern .
This naturally extends to an augmented cosimplicial category with au gmentation given by the
pushforward
j−1∗ :D(X1×Y X2) /d47/d47D(X1×X2)
33
along the relative diagonal
j−1 :X1×Y X2 /d47/d47X1×X2
By base change, this augmented cosimplicial category is left adjoint able in the sense of [L2,
Corollary 6.2.4.3], thus the integral transform construction
Φ : D(X1×Y X2) /d47/d47 FunD(Y )(D(X1),D(X2))
admits a fully faithful left adjoint.
□
