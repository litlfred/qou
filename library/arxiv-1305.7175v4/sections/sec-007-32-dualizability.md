---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-007-32-dualizability
section_title: "Dualizability"
section_number: 3.2
pages: 17-23
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
Deﬁnition 3.3. An object A of the symmetric monoidal ( ∞, 2)-category A is said to be
dualizable (equivalently,A is dualizable in the ( ∞, 1)-category f (A)) if it admits a monoidal
dual: there is a dual object A∨∈A and evaluation and coevaluation morphisms
ǫA :A∨⊗A /d47/d47 1A ηA : 1 A /d47/d47A⊗A∨
such that the usual compositions are naturally equivalent to the ide ntity morphism
A
ηA⊗idA /d47/d47A⊗A∨⊗A
idA ⊗ǫA /d47/d47A A ∨ idA∨ ⊗ηA /d47/d47A∨⊗A⊗A∨ ǫA⊗idA∨
/d47/d47A∨
Example 3.4. Any algebra object A∈ Alg(C) is dualizable with dual the opposite algebra
Aop∈ Alg(C). The evaluation morphism
ǫA :Aop⊗A /d47/d47 1C
is given by A itself regarded as an A-bimodule. The coevaluation morphism
ηA : 1 C /d47/d47A⊗Aop
is also given by A itself regarded as an A-bimodule.
3.2.1. Dualizable morphisms. Consider two objects A,B ∈A , and a morphism
Φ : A /d47/d47B.
Example 3.5. IfA = Alg(C), then Φ is simply an Aop⊗B-module.
18 DA VID BEN-ZVI AND DA VID NADLER
If B is dualizable with dual B∨, we can package Φ in the equivalent form of the morphism
eΦ :B∨⊗A→ 1A
deﬁned by
B∨⊗A
idB∨ ⊗Φ
/d15/d15
eΦ /d47/d47 1A
B⊗B∨
ǫB
/d59/d59✈✈✈✈✈✈✈✈✈
If A is dualizable with dual A∨, we can package Φ in the equivalent form of the morphism
uΦ : 1 A→B⊗A∨
deﬁned by
A⊗A∨
Φ ⊗idA∨
/d15/d15
1A
ηA
/d59/d59✈✈✈✈✈✈✈✈✈uΦ /d47/d47B⊗A∨
If both A and B are dualizable, we can also encode Φ by its dual morphism
Φ ∨ :B∨ /d47/d47A∨
deﬁned by
B∨
Φ ∨
/d52/d52
idB∨ ⊗ηA /d47/d47B∨⊗A⊗A∨ idB∨ ⊗Φ ⊗idA∨
/d47/d47B∨⊗B⊗A∨ ǫB∨ ⊗idA∨
/d47/d47A∨
There is a natural composition identity
(ΦΨ) ∨≃ Ψ ∨Φ ∨
Note that for ﬁxed A,B , the construction Φ ↦→Φ ∨ naturally deﬁnes a covariant map
(−)∨ : Hom(A,B ) /d47/d47 Hom(B∨,A ∨)
and in particular a morphism Φ 1→ Φ 2 induces a natural morphism Φ ∨
1→ Φ ∨
2 .
Let us record the canonical equivalences encoded by the following c ommutative diagrams
(3.1) A⊗A∨
Φ ⊗idA∨
/d15/d15
A∨⊗A
ǫA∨
/d35/d35❍❍❍❍❍❍❍❍❍
1A
ηA
/d59/d59✈✈✈✈✈✈✈✈✈
ηB
/d35/d35❍❍❍❍❍❍❍❍❍
uΦ /d47/d47B⊗A∨ B∨⊗A
Φ ∨⊗idA
/d79/d79
eΦ /d47/d47
idB∨ ⊗Φ
/d15/d15
1A
B⊗B∨
idB ⊗Φ ∨
/d79/d79
B⊗B∨
ǫB
/d59/d59✈✈✈✈✈✈✈✈✈
Example 3.6. In the setting of algebras, bimodules and intertwiners, the morphis ms Φ, uΦ ,
eΦ and Φ ∨ are all diﬀerent manifestations of the same bimodule Φ, making their v arious com-
patibilities particularly evident.
NONLINEAR TRACES 19
Deﬁnition 3.7. (1) A morphism Φ : A→ B is said to be left dualizable if it admits a left
adjoint: there is a morphism Φ ℓ :B→A and unit and counit morphisms
ηΦ : idB /d47/d47 Φ◦ Φℓ ǫΦ : Φ ℓ◦ Φ /d47/d47 idA
satisfying the usual identities.
(2) A morphism Φ : A→B is said to be right dualizable if it admits a right adjoint: there
is a morphism Φ r :B→A and unit and counit morphisms
ηΦ : idA /d47/d47 Φr◦ Φ ǫΦ : Φ ◦ Φr /d47/d47 idB
satisfying the usual identities.
Remark 3.8. If A and B are dualizable, and Φ : A→ B is left (resp. right) dualizable, then
Φ ∨ : B∨→ A∨ is right (resp. left) dualizable with right adjoint (Φ ℓ)∨ : A∨→ B∨ (resp. left
adjoint (Φ r)∨ :A∨→B∨).
3.3. T races and dimensions. (We continue to refer to [TV, HSS] for thorough treatments of
the theory of traces in higher category theory.)
Let A∈A be a dualizable object with dual A∨. Consider an endomorphism
Φ : A /d47/d47A
Since A is dualizable, Φ has a trace deﬁned as follows.
Deﬁnition 3.9. (1) The trace of Φ : A→A is the object Tr(Φ) ∈ ΩA deﬁned by
1A
ηA /d47/d47
Tr(Φ)
A⊗A∨ Φ ⊗idA /d47/d47A⊗A∨ ǫA /d47/d47 1A .
Given a natural transformation ϕ : Φ → Ψ, we deﬁne the induced morphism
Tr(ϕ) : Tr(Φ) /d47/d47 Tr(Φ ′)
by applying ϕ⊗ idA∨ to the middle arrow above.
(2) The dimension (or Hochschild homology) of A is the trace of the identity
dim(A) = Tr(idA)∈ ΩA
or in other words, the object deﬁned by
1A
ηA /d47/d47
dim(A)
A⊗A∨ ǫA /d47/d47 1A
Remark 3.10. Equivalently, we can describe the trace as the composition
1A
Φ /d47/d47 End(A) ∼ /d47/d47A⊗A∨ ǫA /d47/d47 1A
where the middle arrow is the identiﬁcation deduced from the dualizab ility of A.
Remark 3.11. Observe that for ﬁxed dualizable A∈A , taking traces gives a functor
Tr : End(A) /d47/d47 ΩA
Remark 3.12. Observe that for any dualizable endomorphism Φ, the standard iden tities encoded
by Diagrams 3.1 give rise to an identiﬁcation
Tr(Φ)≃ Tr(Φ ∨)
20 DA VID BEN-ZVI AND DA VID NADLER
Example 3.13. When A = 1 A is the monoidal unit, and Φ : 1 A→ 1A is an endomorphism,
we have an evident equivalence of endomorphisms
Tr(Φ)≃ Φ
Theorem 3.14 ([L3]). There is a canonical S1-action on the dimension dim(A) of any dual-
izable object A of a symmetric monoidal ∞-categoryA.
3.3.1. Cyclic symmetry.
Proposition 3.15. Given two morphisms
A
Φ /d47/d47B
Ψ
/d111/d111
between dualizable objects A,B∈A , there is a canonical equivalence
m(Φ, Ψ) : Tr(Φ ◦ Ψ) ∼ /d47/d47 Tr(Ψ◦ Φ)
functorial in morphisms of both Φ and Ψ .
Proof. We construct m(Φ, Ψ) following the commutative diagram below:
A⊗A∨ Φ ⊗idA∨
/d47/d47
idA ⊗Ψ ∨
/d28/d28✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿ B⊗A∨ Ψ ⊗idA∨
/d47/d47
idB ⊗Ψ ∨
/d28/d28✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿ A⊗A∨
ǫA
/d36/d36❍❍❍❍❍❍❍❍❍
1A
ηA
/d59/d59✈✈✈✈✈✈✈✈✈
ηB
/d36/d36❍❍❍❍❍❍❍❍❍ 1A
B⊗B∨
Ψ ⊗idB∨
/d47/d47A⊗B∨
Φ ⊗idB∨
/d47/d47B⊗B∨
ǫB
/d59/d59✈✈✈✈✈✈✈✈✈
Following the top edge, we ﬁnd the deﬁnition of Tr(Ψ ◦ Φ). Following the bottom edge, we
ﬁnd the deﬁnition of Tr(Φ ◦ Ψ). The identiﬁcations ﬁlling the left and right diamonds arise from
the standard identities encoded by Diagrams 3.1. The identiﬁcation ﬁ lling the central square
results from the symmetric monoidal structure.
The construction is evidently functorial for morphisms Φ → Φ ′. The functoriality for mor-
phisms Ψ → Ψ ′ is similar, once one recalls that the construction Ψ ↦→Ψ ∨ is covariantly
functorial in morphisms of Ψ. □
Example 3.16. Taking Φ = id A yields a canonical equivalence
γ′ : id Tr(Φ ′)
∼ /d47/d47m(idA, Φ ′
A)
and likewise, taking Φ ′ = idA yields a canonical equivalence
γ : id Tr(Φ)
∼ /d47/d47m(ΦA, idA)
Thus taking Φ = Φ ′ = idA yields an automorphism of the identity of the Hochschild homology
(γ′)−1◦γ : id Tr(idA)
∼ /d47/d47 idTr(idA)
called the BV homotopy .
Remark 3.17. The proposition is only the initial part of the full cyclic symmetry of tr ace (see
Remark 3.28), and the example is the lowest level structure of the S1-action on Hochschild
homology (see Theorem 3.14) deﬁning cyclic homology.
NONLINEAR TRACES 21
Lemma 3.18. Given morphisms
A Φ /d47/d47B Ψ /d47/d47C Υ /d47/d47A
between dualizable objects A,B,C ∈A , there is a canonical commutative diagram
Tr(ΨΦΥ)
m(Ψ ,ΦΥ) /d47/d47
m(ΨΦ ,Υ) /d41/d41❘❘❘❘❘❘❘❘❘❘❘❘❘❘ Tr(ΦΥΨ)
m(Φ,ΥΨ)
/d15/d15
Tr(ΥΨΦ)
Proof. We construct the desired equivalence from the following diagram:
C⊗C∨ Υ /d47/d47
Ψ ∨
/d37/d37▲▲▲▲▲▲▲▲▲▲ A⊗C∨ Φ /d47/d47
Ψ ∨
/d37/d37▲▲▲▲▲▲▲▲▲▲ B⊗C∨ Ψ /d47/d47
Ψ ∨
/d37/d37▲▲▲▲▲▲▲▲▲▲ C⊗C∨
ǫC
/d35/d35❍❍❍❍❍❍❍❍❍
1A
/d59/d59✈✈✈✈✈✈✈✈✈ /d47/d47
/d35/d35❍❍❍❍❍❍❍❍❍ B⊗B∨ Ψ /d47/d47
Φ ∨
/d37/d37▲▲▲▲▲▲▲▲▲▲ C⊗B∨ Υ /d47/d47
Φ ∨
/d37/d37▲▲▲▲▲▲▲▲▲▲ A⊗B∨ Φ /d47/d47
Φ ∨
/d37/d37▲▲▲▲▲▲▲▲▲▲ B⊗B∨ /d47/d47 1A
A⊗A∨ Φ /d47/d47B⊗A∨ Ψ /d47/d47C⊗A∨ Υ /d47/d47A⊗A∨
ǫA
/d59/d59✈✈✈✈✈✈✈✈✈
The natural transformations m(Ψ, ΦΥ) and m(Φ, ΥΨ) describe passage from the top row to
the middle row and from the middle to the bottom, respectively. The t ransformationm(ΨΦ , Υ)
can then be identiﬁed with the transformation from the top row to t he bottom given by inserting
the diagonal morphisms id ⊗Φ ∨◦ Ψ ∨ and using standard composition identities. □
3.4. F unctoriality of dimension. LetAcont⊂A denote the (∞, 2)-subcategory of dualizable
objects and continuous or right dualizable morphisms (morphisms that are left duals).
Deﬁnition 3.19. Let Ψ : A→B denote a morphism in Acont with right adjoint Ψ r :B→A.
We deﬁne the induced morphism of dimensions
dim(Ψ) : dim( A) /d47/d47 dim(B)
to be the composition
Tr(idA)
ηΨ /d47/d47 Tr(Ψr◦ Ψ)
m(Ψ r,Ψ) /d47/d47 Tr(Ψ◦ Ψ r)
ǫΨ /d47/d47 Tr(idB)
Remark 3.20. In other words, the morphism dim(Ψ) is deﬁned by the following diagra m
A⊗A∨
Ψ ⊗idA∨
/d15/d15
ǫA
/d34/d34❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊
1A
ηA
/d60/d60②②②②②②②②②②②②②②②②②② uΨ /d47/d47
ηB
/d34/d34❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊❊ B⊗A∨
Ψ r⊗idA
/d79/d79
cΨ /d47/d47
idB∨ ⊗Ψ r∨
/d15/d15
1A 1A
Tr(Ψ rΨ) ≃Tr(ΨΨ r) /d47/d47
dim(B)
dim(A)
1A
B⊗B∨
idB ⊗Ψ ∨
/d79/d79
ǫB
/d60/d60②②②②②②②②②②②②②②②②②
22 DA VID BEN-ZVI AND DA VID NADLER
Following the top and bottom edge, we ﬁnd the respective deﬁnitions of dim(A) and dim(B).
The unit ηΨ deﬁnes a morphism from the top edge to the top zig-zag. The counit ǫΨ deﬁnes a
morphism from the bottom zig-zag to the bottom edge. The passag e from the top to bottom
zig-zag is given by the construction m(Ψ r, Ψ) and the identiﬁcation
Tr(Ψr∨◦ Ψ ∨)≃ Tr((Ψ◦ Ψ r)∨)≃ Tr(Ψ◦ Ψ r)
Proposition 3.21. For a diagram
A Φ /d47/d47B Ψ /d47/d47C
withinAcont, there is a canonical equivalence
dim(Ψ ◦ Φ)≃ dim(Ψ) ◦ dim(Φ) : dim( A) /d47/d47 dim(C)
Proof. The equivalence is given by ﬁlling in the following diagram
dim(A)
ηΦ /d47/d47
ηΨ
/d38/d38◆◆◆◆◆◆◆◆◆◆◆ Tr(ΦrΦ) m /d47/d47
ηΨ
/d15/d15
Tr(ΦΦ r)
ǫΦ /d47/d47
ηΨ
/d15/d15
dim(B)
ηΨ
/d15/d15
Tr(ΦrΨ rΨΦ) m /d47/d47
m
/d40/d40PPPPPPPPPPPP Tr(ΨrΨΦΦ r)
ǫΦ /d47/d47
m
/d15/d15
Tr(ΨrΨ)
m
/d15/d15
Tr(ΨΦΦ rΨ r)
ǫΦ /d47/d47
ǫΨΦ
/d39/d39❖❖❖❖❖❖❖❖❖❖❖ Tr(ΨΨ r)
ǫΨ
/d15/d15
dim(C)
Along the three boundary edges, we ﬁnd the deﬁnitions of dim(Φ), d im(Ψ) and dim(ΨΦ)
respectively.
The two corner triangles are given by the composition identities for a djoints (for example,
at the top left, relating the adjoint of ΦΨ with the composition of adj oints of Ψ and Φ).
The middle triangle is given by the identity of Lemma 3.18.
The top right square is given by taking traces of the evident commut ative diagram of endo-
morphisms
ΦΦ r⊗ IdB∨
/d15/d15
/d47/d47 IdB⊗ IdB∨
/d15/d15
ΦΦ r⊗ (Ψ rΨ) ∨ /d47/d47 IdB⊗(Ψ rΨ) ∨
and using the canonical identiﬁcation Tr( F ) = Tr(F ∨) for any dualizable morphism.
Finally, the two remaining commuting squares are given by the functo riality of the cyclic
rotation of the trace in its two arguments. For instance, in the top left square, we may either
rotate Tr(Φ r◦ (IdA◦Φ)) and then apply the unit ηΨ : IdA→ Ψ rΨ or ﬁrst apply the unit and
then rotate.
This concludes the construction. □
Since we have an evident equivalence dim(1 A) ≃ 1A for the unit 1 A ∈ A, we have the
following specialization of Proposition 3.21 in which we adopt suggestive notation.
NONLINEAR TRACES 23
Corollary 3.22 (Abstract Grothendieck-Riemann-Roch) . Let A,B ∈A cont and V : 1 A→A
and π∗ :A→B morphisms in Acont. Then the following diagram naturally commutes
1A
dim(π∗V ) /d35/d35●●●●●●●●●
dim(V )/d47/d47 dim(A)
dim(π∗)
/d15/d15
dim(B)
Remark 3.23. One can show along the same lines as the proposition that taking dimen sions
extends to a symmetric monoidal functor
dim :Acont /d47/d47 ΩA.
3.5. F unctoriality of traces. We would like to capture the functoriality for traces of arbitrary
endomorphisms of dualizable objects. For this purpose we deﬁne a m orphism between pairs
A∈A cont ΦA∈ EndA(A)
of an object and an endomorphism to consist of a pair
Ψ ∈ HomAcont (A,B ) ψ : Ψ ◦ ΦA
≃ /d47/d47 ΦB◦ Ψ
of a morphism and a commuting structure.
Deﬁnition 3.24. For a morphism
(Ψ,ψ ) : (A, ΦA)→ (B, ΦB)
as above, we deﬁne the induced morphism of traces
Tr(Ψ,ψ ) : Tr(Φ A) /d47/d47 Tr(ΦB)
to be the composition
Tr(ΦA)
ηΨ /d47/d47 Tr(ΨrΨΦ A)
ψ /d47/d47 Tr(ΨrΦBΨ)
m(Ψ r,Φ B Ψ) /d47/d47 Tr(ΦBΨΨ r)
ǫΨ /d47/d47 Tr(ΦB)
Remark 3.25. Note that we could alternatively deﬁne a morphism Tr(Ψ ,ψ ) by applying the
unit ηΨ to the right of Φ A, rotating the trace in the opposite direction, and again using the
counit on the right. It is elementary to give a natural equivalence of the two constructions using
nothing more than the dualizability of A.
