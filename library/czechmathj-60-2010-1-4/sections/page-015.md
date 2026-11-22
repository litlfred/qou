---
doc_id: czechmathj-60-2010-1-4
doc_title: "Czechoslovak Mathematical Journal"
section_id: page-015
section_title: "Page 15"
section_number: null
pages: 15-15
source_pdf: CzechMathJ_60-2010-1_4.pdf
source_sha256: 7595f81d1398d0bf
toc_source: undetermined
doc_brief: "Czechoslovak Mathematical Journal — 19 sections: Page 1; Page 2; Page 3"
---
satisﬁes the identities
⟨x1, x2, . . . , xm; y, z⟩= −⟨x1, x2, . . . , xm; z, y⟩,
⟨x1, x2, . . . , xr, a, b, xr+1, . . . , xm; y, z⟩−⟨x1, x2, . . . , xr, b, a, xr+1, . . . , xm; y, z⟩
+
r
X
k=0
X
α
⟨xα1, . . . , xαk, ⟨xαk+1, . . . , xαr; a, b⟩, . . . , xm; y, z⟩= 0,
σx,y,z(⟨x1, x2, . . . , xr, x; y, z⟩+
r
X
k=0
X
α
⟨xα1, . . . , xαk; ⟨xαk+1, . . . , xαr; y, z⟩, x⟩) = 0,
where α runs over the set of all bijections of type α: {1, 2, . . ., r} →{1, 2, . . ., r},
i 7→αi, α1 < α2 < . . . < αk, αk+1 < . . . < αr, r ⩾0 and σx,y,z denotes the cyclic
sum by x, y, z.
Let X = {ai | i ∈Λ} be a well ordered basis of V . We deﬁne the deg-lex ordering
on X∗. Let ∆: V →V ⊗V be a linear map which satisﬁes ∆(ai) = 1 ⊗ai + ai ⊗1,
(Id ⊗∆)∆= (∆⊗Id)∆(coassociativity) and if τ∆= ∆then τ(x ⊗y) = y ⊗x
(cocommutativity). It is customary to write ∆(x) = P x(1) ⊗x(2).
Let T (V ) be the tensor algebra over V endowed with its natural structure of
cocommutative Hopf algebra, that is, V ⊆Prim (T (V )) (the primitive element of
T (V )). Let ⟨; ⟩: T (V ) ⊗V ⊗V →V be a map. Then we may shortly write the
deﬁnition of a Sabinin algebra as
⟨x; a, b⟩= −⟨x; b, a⟩, ⟨x[a, b]y; c, e⟩+
X
⟨x(1)⟨x(2); a, b⟩y; c, e⟩= 0,
σa,b,c(⟨xc; a, b⟩+
X
⟨x(1); ⟨x(2); a, b⟩, c⟩) = 0,
where [a, b] = ab −ba.
Deﬁnition 7.2 ([21]).
Let (V, ⟨; ⟩) be a Sabinin algebra. Then
˜S(V ) = T (V )/span
D
xaby −xbay +
X
x(1)⟨x(2); a, b⟩y|x, y ∈T (V ), a, b ∈V
E
is called the universal enveloping module for V .
Since T (V ) ≃k⟨X⟩as k-algebras, we can view ˜S(V ) as a right k⟨X⟩-module:
˜S(V ) = mod⟨X|I⟩k⟨X⟩,
where I = {xab −xba + P x(1)⟨x(2); a, b⟩| x ∈X∗, a > b, a, b ∈X}.
For the right module, we have a right compatible well ordering ≺on XX∗by a
similar deﬁnition as in (∗). Then we have the following theorem.
72
