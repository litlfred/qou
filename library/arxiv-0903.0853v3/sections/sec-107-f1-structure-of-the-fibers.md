---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-107-f1-structure-of-the-fibers
section_title: "Structure of the fibers"
section_number: F.1
pages: 159-160
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
toc_source: inferred
doc_brief: "Local analytic classification of q-difference equations — 114 sections: Front matter; The problem; The generalized Riemann problem an"
---
rem, we need an auxiliary result. Remember that, all along, we assume that
Hom(Pj, Pi) = 0 for 1 ≤i < j ≤k.
Proposition A.6.3. — Let C′ be a commutative C-algebra and let M′ be
a diﬀerence module over K′ := C′ ⊗C K, equipped with a (k −1)-ﬁltration:
0 = M′
0 ⊂M′
1 ⊂· · · ⊂M′
k−1 = M′ such that grM′ ≃P ′
1 ⊕· · · ⊕P ′
k−1
(as usual, P ′
i := C′ ⊗C Pi).
Then the functor in commutative C′-algebras
C′′ ❀Ext(C′′ ⊗C Pk, C′′ ⊗C′ M′) is an aﬃne space over C′ with dimension
P
1≤i≤k
δi,k.
Proof. — After proposition A.5.1,
this is the functor C′′
❀
C′′ ⊗C′
Ext(P ′
k, M′).
From each exact sequence 0 →M′
i−1 →M′
i →P ′
i →0
one draws the cohomology long exact sequence of corollary A.4.4; but, from
proposition A.5.1, one draws that, for any commutative C-algebra C′, one has
Hom(C′ ⊗C Pj, C′ ⊗C Pi) = 0 and that the C′-module Ext(C′ ⊗C Pj, C′ ⊗C Pi)
is free of ﬁnite rank δi,j. According to the equalities Hom(P ′
j, P ′
i) = 0, the
long exact sequence is here shortened as:
0 →Ext(P ′
k, M′
i−1) →Ext(P ′
k, M′
i) →Ext(P ′
k, P ′
i) →0,
154
APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFERENCE MODULES
and, for i = 1, . . . , k −1, these sequences are split, the term at the right being
free. So, in the end:
Ext(P ′
k, M′) ≃
M
1≤i≤k
Ext(P ′
k, P ′
i),
which is free of rank
P
1≤i≤k
δi,k. As in the case k = 2 (which is a particular
case of the proposition), the functor mentioned is represented by the symetric
algebra of the dual of this module.
For all ℓsuch that 1 ≤ℓ≤k, let us write:
Vℓ:=
M
1≤i≤ℓ
Ext(Pℓ, Pi),
Wℓ:=
M
1≤i<j≤ℓ
Ext(Pj, Pi),
V ′
ℓ:=
M
1≤i≤ℓ
Ext(P ′
ℓ, P ′
i),
W ′
ℓ:=
M
1≤i<j≤ℓ
Ext(P ′
j, P ′
i).
We consider Vℓ, Wℓas aﬃne schemes over C and V ′
ℓ, W ′
ℓas aﬃne schemes over
C′, so that:
V ′
ℓ= C′ ⊗C Vℓ,
W ′
ℓ= C′ ⊗C Wℓ.
We improperly write C′⊗CV the base change of aﬃne schemes Spec C′⊗Spec C
V . Also, we do not distinguish between the direct sums of the free C-modules
Ext(Pj, Pi) and the product of the corresponding aﬃne schemes. Note that, in
the proof of the proposition, the isomorphism Ext(P ′
k, M′) ≃V ′
ℓis functorial
in C′. This entails:
Corollary A.6.4. — Each ﬁber Ext(P ′
k, M′) is isomorphic to V ′
k as a scheme
over C′.
