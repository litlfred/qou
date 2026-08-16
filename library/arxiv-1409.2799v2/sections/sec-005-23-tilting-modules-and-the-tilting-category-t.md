---
doc_id: arxiv-1409.2799v2
doc_title: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY"
section_id: sec-005-23-tilting-modules-and-the-tilting-category-t
section_title: "Tilting modules and the tilting category T"
section_number: 2.3
pages: 8-10
source_pdf: 1409.2799v2.pdf
source_sha256: 2f2067b7b583e731
doc_brief: "DIAGRAM CATEGORIES FOR Uq-TILTING MODULES AT ROOTS OF UNITY — We give a diagrammatic presentation of the category of Uq(sl2)-tilting modules T for q being a root of unity and introduce a grading on"
---
Deﬁnition 2.12. (∆ - and ∇-ﬁltration) We say that a Uq-module M has a ∆ -ﬁltration if there
exists a descending sequence of Uq-submodules
M = F0 ⊃ F1 ⊃ · · · ⊃ Fi ⊃ . . . ,
∞⋂
i=0
Fi = 0,
such that for all i = 0, 1 . . . we have Fi/Fi+1 ∼= ∆ q(i′) for some i′ ∈ Z≥0. A ∇-ﬁltration is deﬁned
similarly, but using ∇q(i′) instead of ∆ q(i′) and an ascending sequence of Uq-submodules, that is
0 = F0 ⊂ F1 ⊂ · · · ⊂ Fi ⊂ . . . ,
∞⋃
i=0
Fi = M,
such that for all i = 0, 1 . . . we have Fi+1/Fi ∼
= ∇q(i′) for some i′ ∈ Z≥0. ▲
One can prove, following similar arguments as in [26, Propos ition II.4.16], that such ﬁltrations
are unique up to reordering. It is clear that a ﬁnite-dimensi onal Uq-module M has a ∆ -ﬁltration
iff M ∗ has a ∇-ﬁltration.
Deﬁnition 2.13. (Tilting modules) We call aUq-module M a Uq-tilting module if it has a ∆ - and
a ∇-ﬁltration. We say for short that M is tilting. ▲
Example 2.14. Recall that the category of ﬁnite-dimensional Uv-modules is semisimple. It fol-
lows that all ﬁnite-dimensional Uv-modules are tilting. Moreover, for i < l or i ≡ −1 mod l, by
Proposition 2.7 and Corollary 2.8, we see that ∆ q(i) ∼= Lq(i) ∼= ∇q(i) is tilting. ▲
It is easy to see (in our sl2 case - in general this is non-trivial, see e.g. [47, Theorem 3 .3]) that
∆ q(i) ⊗Q(q) ∆ q(i′) has a ∆ -ﬁltration with factors (likewise for ∇q(i) ⊗Q(q) ∇q(i′))
(4) ∆ q(|i − i′|), ∆ q(|i − i′| + 2), . . . , ∆ q(i + i′ − 2), ∆ q(i + i′), i, i ′ ≥ 0.
Deﬁnition 2.15. (Full tilting category) We denote by Tall the full subcategory of all Uq-modules
that are tilting. We denote its class of objects by Ob(Tall). ▲
Proposition 2.16. The category Tall has the following properties.
(a) If M, M ′ ∈ Ob(Tall), then M ⊕ M ′ ∈ Ob(Tall).
(b) If M ⊕ M ′ ∈ Ob(Tall), then M, M ′ ∈ Ob(Tall).
(c) If M, M ′ ∈ Ob(Tall), then M ⊗Q(q) M ′ ∈ Ob(Tall). □
Proof. Part (a) is immediate. For part (b) one can, for example, argu e as in [24, Proposition 3.7],
and the non-trivial part (c) can be deduced from (4) and the co rresponding statement for the dual
Weyl modules ∇q(i). ■
Deﬁnition 2.17. (The tilting category T) Let T be the full subcategory of Tall consisting of:
• The objects Ob(T) are all ﬁnite-dimensional Uq-tilting modules M ∈ Ob(Tall).
• The morphisms HomT(M, N ) are all Uq-intertwiners f ∈ HomUq (M, N ).
The objects of T have ﬁnite ﬁltrations, i.e. FN = FN +i for some N ∈ Z≥0 and all i ∈ Z≥0. ▲
8
Recall that an additive category is Krull-Schmidt, if each object can be uniquely decomposed
(up to permutation) into a ﬁnite direct sum of indecomposable objects, i.e. objects O such that
O ∼= O′ ⊕ O′′ implies that O′ ∼= 0 or O′′ ∼= 0.
Lemma 2.18. We have the following.
(a) The category T is additive (but not abelian), closed under ﬁnite direct sum s, ﬁnite tensor
products and under duals.
(b) T is a Krull-Schmidt category whose indecomposable objects are parametrized by Z≥0.
(c) ∆ q(i), ∇q(i) and Lq(i) are in T iff i < l or i ≡ −1 mod l. □
Proof. (a). From Proposition 2.16 and the fact that HomUq (·, Q(q)) commutes with ﬁnite sums.
(b). The Krull-Schmidt property follows from ﬁnite-dimensionality and (b) of Proposition 2.16.
By Proposition 2.20 below, all ﬁnite-dimensional indecomposable tiltings are of the form Tq(i).
(c). A direct consequence of Proposition 2.7 and Corollary 2.8. ■
Remark 2.19. It follows from Lemma 2.18 part (a) thatT is a rigid category (a monoidal category
with duals and certain compatibility properties). Moreove r, T is even a ribbon (tensor) category
and T gives rise to a modular category (roughly: one mods out by tiltings whose quantum trace is
zero) and thus, gives a 2 + 1-dimensional TQFT and can be used to deﬁne the Witten-Reshetikhin-
Turaev invariantsof 3-manifolds. Good treatments of this are [1, Section 4] or [51, Section 7]. ▲
Deﬁne, using Propositions 2.7 and 2.16 and (4), a family(Tq(i))i∈Z≥0 of indecomposable tiltings
as follows. We start by setting Tq(0) = ∆ q(0) and Tq(1) = ∆ q(1). Then we denote by mq ∈ Tq(1)
any eigenvector for K with eigenvalue q. For each i > 1 we deﬁne Tq(i) to be the indecomposable
summand of (Tq(1))⊗i which contains the vector mq ⊗ · · · ⊗ mq ∈ (Tq(1))⊗i.
Denote by (T : ∆ q(i)) ∈ Z≥0 the ﬁltration multiplicity for an Uq-tilting module T . It is clear,
by using (4), that
(5) ((Tq(1))⊗i : ∆ q(i)) = 1 , ((Tq(1))⊗i : ∆ q(i′)) = 0 , for i′ > i.
Hence, Tq(i) may also be described as the unique indecomposable summand o f (Tq(1))⊗i that
contains ∆ q(i). We note the following more precise statement.
Proposition 2.20.
(a) ∆ q(i) ∼= Lq(i) ∼= Tq(i) ∼= ∇q(i) iff i < l or i ≡ −1 mod l.
(b) Suppose i = al + b for some a, b ∈ Z≥0 with b ≤ l − 2. Set i′ = ( a + 2)l − b − 2. Then there
exist short exact sequences
0 − →∆ q(i′)֒− →Tq(i′) −։ ∆ q(i) − →0, 0 − → ∇q(i)֒− →Tq(i′) −։ ∇q(i′) − →0.
(c) We have Tq(i) ∼
= Tq(i′) iff i = i′. Moreover, if M ∈ Ob(T) is indecomposable, then there
exists an i ∈ Z≥0 such that M ∼= Tq(i). □
Proof. (a). Clear by Proposition 2.7 and Corollary 2.8.
(b). First let T = ∆ q((a + 1)l − 1) ⊗ ∆ q(1). Then T = Tq((a + 1)l − 1) ⊗ Tq(1) by (a), and,
by (4), we see that T has a ∆ q-ﬁltration giving us the short exact sequence
0 − →∆ q((a + 1)l)֒− →T −։ ∆ q((a + 1)l − 2) − →0.
By duality, T has an analogous ∇q-ﬁltration, showing that T is tilting. It is also indecomposable
since otherwise the summand Tq((a + 1)l) of T would be equal to ∆ q((a + 1)l), forcing it to be
simple, which contradicts (b) of Proposition 2.7. This proves the claim in case b = l − 2.
9
Now, if b < l − 2, then consider the diagram
0 /d47/d47 ∆ q(i′)/d31 /d127 /d47/d47 ∆ q(i′ − 1) ⊗ ∆ q(1) /d47/d47 /d47/d47/d127 /d95
/d15/d15
∆ q(i′ − 2) /d47/d47 0
Tq(i′ − 1) ⊗ Tq(1)
/d15/d15
/d15/d15
0 /d47/d47 ∇q(i′ − 2) /d31 /d127 /d47/d47 ∇q(i′ − 1) ⊗ ∇q(1) /d47/d47 /d47/d47 ∇q(i′) /d47/d47 0.
Here the bottom and top sequences come from (4). A computatio n shows that these split. This
gives an inclusion ∆ q(i′ − 2)֒→Tq(i′ − 1) ⊗ Tq(1) which extends to Tq(i′ − 2), and a surjection
Tq(i′ − 1) ⊗ Tq(1) ։ ∇q(i′ − 2) factoring through Tq(i′ − 2). The resulting endomorphism of
Tq(i′ − 2) is non-zero on the i′ − 2 weight space (the reader unfamiliar with this notion might
consider Remark 2.29 where the notation isMi for the i-th weight space) and thus, an isomorphism.
Hence, Tq(i′ − 1) ⊗ Tq(1) ∼= Tq(i′ − 2) ⊕ T for some Uq-module T , which is tilting by (a) of
Lemma 2.18. Using an inductive argument, we have that T has two ∆ q- and ∇q-factors as in the
statement of (b). As above, we see that T = Tq(i′), which proves the claim.
(c). To see the ﬁrst statement note that it sufﬁces to show that Tq(i) ⁄∼= Tq(i′) for i ⁄= i′. To
this end, assume without loss of generality that i′ > i . By (5), we see that ∆ q(i′) appears with
multiplicity 1 in Tq(i′), but not in Tq(i). Thus, Tq(i) ⁄∼= Tq(i′). That every ﬁnite-dimensional
indecomposable tilting is of this form needs a little bit mor e treatment. But it is a standard argu-
ment that appears in various contexts and can be adopted for e xample from [24, Section 11.2] or,
alternatively, from [26, Chapter II, Section E.6]. ■
Example 2.21. Let l = 3 again. The Uq-tilting module Tq(2) can be visualized as
⊗ m1
1 /d47/d47
q−1
/d4/d4
m01
/d111/d111
q+1
/d4/d4
m1
1
/d15/d15
q−1
/d50/d50 m11
1 /d47/d47
1
/d15/d15
q−2
/d46/d46 m011
/d111/d111
1
/d15/d15
+
q0
/d112/d112
m0
1
/d79/d79
q+1
/d50/d50 m10
1 /d47/d47
1
/d79/d79
q0
/d46/d46 m001
/d111/d111
1
/d79/d79
q+2
/d112/d112
,
where we use mij = mi ⊗ mj. By construction, Tq(2) contains m00 and it therefore has to be the
span of {m00, q−1m10 + m01, m11} as indicated above (which is isomorphic to Lq(2)). ▲
Remark 2.22. One can show that the category of all ﬁnite-dimensional proj ective Uq-modules
is a full subcategory of T. The same is true for ﬁnite-dimensional injective Uq-modules: T has
enough injectives and projectives. In fact, Tq(i) is injective and projective for all i ≥ l − 1.
Hence, {Tq(i) | i ≥ l − 1} is a complete set of pairwise non-isomorphic, projective-i njective
indecomposable, ﬁnite-dimensional Uq-modules. See for example [1, Section 5] ▲
