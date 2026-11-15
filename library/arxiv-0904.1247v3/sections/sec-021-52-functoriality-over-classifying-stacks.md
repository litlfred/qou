---
doc_id: arxiv-0904.1247v3
doc_title: "THE CHARACTER THEORY OF A COMPLEX GROUP"
section_id: sec-021-52-functoriality-over-classifying-stacks
section_title: "Functoriality over classifying stacks"
section_number: 5.2
pages: 32-34
source_pdf: 0904.1247v3.pdf
source_sha256: 4a6f4dee6af66dac
toc_source: outline
doc_brief: "THE CHARACTER THEORY OF A COMPLEX GROUP — We apply the ideas of derived algebraic geometry and topological ﬁeld theory to the representation theory of reductive groups."
---
ization of Theorem 5.2 and its corollary realizing linear functors via integrals kernels on the ﬁber
product. Unfortunately, results of this nature do not hold in great generality, but we will be content
with the case when the base stack Y is the classifying stack BG of an aﬃne group scheme G. What
we speciﬁcally use is the restrictive property that the diagonal map of such stacks is smooth.
Proposition 5.4. For a stack Y with smooth diagonal, the monoidal category D(Y ) is semi-rigid
with a canonical pivotal structure.
Proof. Since D(Y ) is compactly generated and symmetric monoidal, it suﬃces to check that any
compact object is dualizable.
For any compact object M ∈D(Y ), we will show that the monoidal dual is the shifted Verdier
dual DY (M)[2 dim Y ] ∈D(Y ).
Following the discussion of Section 2.2.1, it suﬃces to establish for any compact object M ∈D(Y ),
and arbitrary objects L, N ∈D(Y ), that there is a functorial equivalence
(3)
HomD(Y )(L ⊗M, N) ≃HomD(Y )(L, N ⊗DY (M)[2 dim Y ])
Observe that it suﬃces to establish the equivalence for L, N ∈H compact objects. For arbitrary
objects L, N ∈H, it then follows by continuity by taking colimits ﬁrst in N then in L.
32
Using that the diagonal ∆: Y →Y × Y is smooth of relative dimension −dim Y , note the
following functorial equivalence
DY (L ⊗M)
=
DY ∆!(L ⊠M)
≃
∆∗(DY (L) ⊠DY (M))
≃
∆!(DY (L) ⊠DY (M))[2 dim Y ]
≃
DY (L) ⊗DY (M)[2 dim Y ]
Now returning to the sought after equivalence (3), we ﬁnd functorial equivalences
HomD(Y )(L ⊗M, N)
≃
HomD(Y )(CY , DY (L ⊗M) ⊗N)
≃
HomD(Y )(CY , (DY (L) ⊗DY (M)[2 dim Y ]) ⊗N)
≃
HomD(Y )(L, DY (M)[2 dim Y ] ⊗N)
□
Remark 5.5. Implicit in the proposition is the Poincar´e duality identity DY (ωY )[2 dim Y ] ≃ωY
since the dual of the monoidal unit must be the monoidal unit.
Corollary 5.6. Let Y be a stack with smooth diagonal, X a stack, and X →Y an arbitrary
morphism. Then D(X) is self-dual as a D(Y )-module.
Proof. As a plain category, D(X) is self-dual, so the previous proposition and Proposition 3.14
imply the corollary.
□
If X1, X2 are stacks, X1 →Y is safe and X2 →Y is arbitrary, then there is a canonical map
induced by !-pullbacks
Ψ : D(X1) ⊗D(Y ) D(X2)
/ D(X1 ×Y X2)
and the integral transform construction gives linear functors
Φ : D(X1 ×Y X2)
/ FunL
D(Y )(D(X1), D(X2))
ΦM = π2∗(π!
1(−) ⊗M)
Tracing back through the constructions and applying standard identities, the functors Ψ, Φ evidently
provide a factorization
D(X1 ×Y X2)
Φ
)❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
❙
D(X1) ⊗D(Y ) D(X2)
∼
/
Ψ
5❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
❧
FunL
D(Y )(D(X1), D(X2))
of the equivalence provided by Corollary 5.6. In general neither Ψ, Φ is itself an equivalence, but
we have the following.
Proposition 5.7. Let Y be a smooth stack with smooth diagonal, X1, X2 stacks, X1 →Y a safe
morphism, and X2 →Y an arbitrary morphism.
Then the integral transform Φ admits a fully faithful left adjoint ΦL.
Proof. Tracing back through the algebraic arguments leading to Proposition 3.14, one sees that the
functor category FunL
D(Y )(D(X1), D(X2)) can be calculated as the limit of the cosimplicial category
with k-cosimplices
D(X1 × Y × · · · × Y × X2)
where the factor Y appears k times and the maps are given by pushforwards in the usual pattern.
This naturally extends to an augmented cosimplicial category with augmentation given by the
pushforward
j−1∗: D(X1 ×Y X2)
/ D(X1 × X2)
33
along the relative diagonal
j−1 : X1 ×Y X2
/ X1 × X2
By base change, this augmented cosimplicial category is left adjointable in the sense of [L2,
Corollary 6.2.4.3], thus the integral transform construction
Φ : D(X1 ×Y X2)
/ FunD(Y )(D(X1), D(X2))
admits a fully faithful left adjoint.
□
