---
doc_id: arxiv-1305.7175v4
doc_title: "NONLINEAR TRACES"
section_id: sec-015-51-dimensions-and-traces-of-sheaf-categories-1-c
section_title: "Dimensions and traces of sheaf categories: 1-categorical consequences"
section_number: 5.1
pages: 30-31
source_pdf: 1305.7175v4.pdf
source_sha256: 5a09955f4fb6a57e
doc_brief: "NONLINEAR TRACES — W e combine the theory of traces in homotopical algebra with s heaf theory in de- rived algebraic geometry to deduce general ﬁxed point and ch aracter formulas."
---
graph of a map of derived stacks f : X → Y provides a correspondence from X to Y and
a correspondence from Y to X. We denote the respective induced maps by f∗ :S(X)→S (Y )
andf ! :S(Y )→S (X). The functoriality of S concisely encodes base change for f∗ andf !. For
π : X→ pt = Spec k, we denote by ωX = π!k∈S (X) the S-analogue of the dualizing sheaf,
and by ω(X) = π∗ωX∈S (pt) = dgVect k theS-analogue of “global volume forms”.
Next we will record formal consequences of our prior calculations d educed from the fact that
a sheaf theory is symmetric monoidal.
Proposition 5.2. Fix a sheaf theory S :Corrk→dgCatk, and X,Y ∈Corrk.
(1)S(X)∈dgCatk is canonically self-dual, and for any f :X→Y , f ! :S(Y )→S (X) and
f∗ :S(X)→S (Y ) are canonically transposes of each other.
(2)S(X) is canonically symmetric monoidal with tensor product
F⊗ !G = ∆ !(π!
1F⊗ π!
2G) F,G∈S (X)
(3) For any f :X→Y , the projection formula holds:
f∗F⊗ !G≃ f∗(F⊗ !f !G) F∈S (X),G∈S (Y )
(4) There is a canonical equivalence of functors and integra l kernels
HomdgCat k (S(X),S(Y ))≃S (X×Y )
(5) The functor q∗p! :S(X)→S (Y ) associated to a correspondence
X Z
p/d111/d111 q /d47/d47Y
is represented by the integral kernel (p×q)∗ωZ∈S (X×Y ).
Proof. (1) Follows immediately from Proposition 4.1.
(2) Follows immediately from the commutative algebra structure on X ∈ Corrk (in fact
commutative coalgebra structure on X∈Stacksk) provided by the diagonal map.
(3) Follows from base change for the diagram
X
id×f
/d15/d15
f /d47/d47Y
∆
/d15/d15
X×Y
f ×id /d47/d47Y×Y
(4) SinceS is monoidal, we have
S(X)⊗S (Y )≃S (X×Y )
The self-duality of S(X) provides
HomdgCat k (S(X),S(Y ))≃S (X)∨⊗S (Y )≃S (X)⊗S (Y )
By construction, the composite identiﬁcation assigns the functor
FK (F ) = π2∗ (π!
1F⊗ !K) K∈S (X×Y )
NONLINEAR TRACES 31
(5) Follows from the projection formula: consider the diagram
Z
p
/d123/d123✇✇✇✇✇✇✇✇✇
q
/d35/d35●●●●●●●●●
Π
/d15/d15
X X ×Y
π1/d111/d111 π2 /d47/d47Y
where Π = p×q. Then we have
q∗p!(−)≃π2∗Π ∗Π !π!
1(−)≃π2∗Π ∗(ωZ⊗! Π !π!
1(−))≃π2∗(Π ∗ωZ⊗!π!
1(−))
□
Proposition 5.3. Fix a sheaf theory S :Corrk→dgCatk.
(1) The S-dimension dim(S(X)) = HH ∗(S(X)) of any X ∈ Corrk is S1-equivariantly
equivalent withS-global volume forms on the loop space
dim(S(X))≃ω(LX).
In particular, for G an aﬃne algebraic group, characters of S-valued G-representations are
adjoint-equivariantS-global volume forms
dim(S(BG))≃ω(G/G)
(2) The S-trace of any endomorphism Z ∈ Corrk(X,X ) is equivalent to S-global volume
forms on the restriction to the diagonal
Tr(S(Z))≃ω(Z|∆ )
In particular, the S-trace of a self-map f : X→ X is equivalent to S-global volume forms
on the f -ﬁxed point locus
Tr(f∗)≃ω(Xf )
Proof. (1) Follows immediately from Proposition 4.1(1). To spell this out, usin g the previous
proposition and base change, dim( S(X)) results from applying the composition
π∗∆ !∆ ∗π!≃π∗p2∗p!
1π!≃Lπ∗Lπ! :dgVectk /d47/d47dgVectk
to the unit 1 dgVect k = k. Here π : X → pt and Lπ : Lx → pt are the maps to the
point, and p1,p 2 :LX ≃ X×X×X X → X are the two natural projections. Thus we ﬁnd
dim(S(X))≃L π∗Lπ!(k)≃ ω(LX). Furthermore, the S1-equivariance results from the one-
dimensional cobordism hypothesis: the one-dimensional topologica l ﬁeld theory deﬁned by
the dualizable object S(X)∈ dgCatk factors through that deﬁned by the dualizable object
X∈Corrk. Moreover, we identiﬁed the S1-action on the dimension LX with loop rotation. 6
(2) Similarly follows immediately from Proposition 4.1(2). □
