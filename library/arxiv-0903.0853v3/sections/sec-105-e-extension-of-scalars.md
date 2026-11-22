---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-105-e-extension-of-scalars
section_title: "Extension of scalars"
section_number: E
pages: 156-158
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
We want to see F(P1, . . . , Pk) as a scheme over C, that is as a representable
functor C′ ❀F(C′ ⊗C P1, . . . , C′ ⊗C Pk) from commutative C-algebras to
sets. To that end, we shall extend what we did to a “relative” situation.
Let C′ be a commutative C-algebra. We set:
K′ := C′ ⊗C K and σ′ := 1 ⊗C σ.
Then K′ is a commutative C′-algebra and σ′ an automorphism of that C′-
algebra. Moreover:
DK′,σ′ := K′ < σ′, σ′−1 >= K′ ⊗K DK,σ = C′ ⊗C DK,σ.
These equalities should be interpreted as natural (functorial) isomorphisms.
From any diﬀerence module M = (E, Φ) over (K, σ), one gets a diﬀerence
module M′ = (E′, Φ′) over (K′, σ′) by putting:
E′ = K′ ⊗K E = C′ ⊗C E and Φ′ = σ′ ⊗K Φ = 1 ⊗C Φ.
A.5. EXTENSION OF SCALARS
151
(This is indeed a left DK′,σ′-module and it is projective of ﬁnite rank over K′.)
We shall write it M′ = C′ ⊗k M to emphasize the dependency on C′. The
following proposition is the tool to tackle the case k = 2.
Proposition A.5.1. — Let M, N be two diﬀerence modules over (K, σ). One
has a functorial isomorphism of C′-modules:
ExtDK′,σ′(C′ ⊗C M, C′ ⊗C N) ≃C′ ⊗C ExtDK,σ(M, N),
and a functorial epimorphism of C′-modules:
C′ ⊗C HomDK,σ(M, N) →HomDK′,σ′(C′ ⊗C M, C′ ⊗C N).
Proof. — We shall write M′ = C′ ⊗C M, E′ = K′ ⊗K E etc. The K-modules
E, F beeing projective of ﬁnite rank, there are natural isomorphisms:
C′ ⊗C LK(E, F) = LK′(E′, F ′) et C′ ⊗C Lσ(E, F) = Lσ′(E′, F ′).
(This is immediate if E and F are free, the general case follows.) By tensoring
the (functorial) exact sequence:
0 →HomDK,σ(M, N) →LK(E, F) →Lσ(E, F) →ExtDK,σ(M, N) →0,
we get the exact sequence:
C′⊗CHomDK,σ(M, N) →C′⊗CLK(E, F) →C′⊗CLσ(E, F) →C′⊗CExtDK,σ(M, N) →0.
Both conclusions then come by comparison with the exact sequence:
0 →HomDK′,σ′(M′, N ′) →LK′(E′, F ′) →Lσ′(E′, F ′) →ExtDK′,σ′(M′, N ′) →0.
Proposition A.5.2. — Let 0 = M0 ⊂M1 ⊂· · · ⊂Mk = M be a k-ﬁltration
with associated graded module P1 ⊕· · · ⊕Pk. Then, setting M′
i := C′ ⊗C Mi
and P ′
i := C′ ⊗C Pi, we get a k-ﬁltration 0 = M′
0 ⊂M′
1 ⊂· · · ⊂M′
k = M′ with
associated graded module P ′
1 ⊕· · · ⊕P ′
k.
Proof. — The Pi being projective as K-modules, the exact sequences 0 →
Mi−1 →Mi →Pi →0 are K-split, so they give rise by the base change K′⊗K
to exact sequences 0 →M′
i−1 →M′
i →P ′
i →0.
If (M, u) denotes the pair made up of the above k-ﬁltered object and of a
ﬁxed isomorphism from grM to P1 ⊕· · ·⊕Pk, we shall write (C′ ⊗C M, 1⊗C u)
the corresponding pair deduced from the proposition.
152
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
Deﬁnition A.5.3. — We deﬁne as follows a functor F from the category
of commutative C-algebras to the category of sets. For any commutative C-
algebra C′, we set:
F(C′) := F(C′ ⊗C P1, . . . , C′ ⊗C Pk).
For any morphism C′ →C′′ of commutative C-algebras, the map F(C′) →
F(C′′) is given by:
class of (M′, u′) 7→class of (C′′ ⊗k′ M′, 1 ⊗C u′).
The set F(C′) is well deﬁned according to the previous constructions. The
map F(C′) →F(C′′) is well deﬁned on pairs thanks to the proposition, and
the reader will check that it goes to the quotient.
Last, the functoriality
(preservation of the composition of morphisms) comes from the contraction
rule of tensor products:
C′′′ ⊗C′′ (C′′ ⊗C′ M′) = C′′′ ⊗C′ M′.
