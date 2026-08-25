---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-090-332-the-birkhoﬀ-guenther-normal-form-going-from
section_title: "The Birkhoﬀ-Guenther normal form. — Going from two slopes"
section_number: 3.3.2
pages: 45-47
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
to general case rests on the following remark. The functor M ❀ M ′ :=
M≤µk−1 induces an onto mapping F(P1,...,P k) → F(P1,...,P k−1). The
inverse image in F(P1,...,P k) of the class of M ′ inF(P1,...,P k−1) is in
natural one-to-one correspondance with the space Ext 1(Pk,M ′). The latter is
a C-vector space of dimension ∑
1≤j<k
rjrk(µk−µj). This follows from the slope
ﬁltration 0 = M0⊂···⊂ Mk−1 = M ′ and the resulting exact sequences, for
1≤j <k:
0→Mj−1→Mj→Pj→ 0 =⇒
0→ Ext1(Pk,M j−1)→ Ext1(Pk,M j)→ Ext1(Pk,P j)→ 0.
40 CHAPTER 3. THE AFFINE SPACE OF ISOFORMAL ANALYTIC CLASSES
(Recall that Hom(Pk,P j) = 0.) Actually, there is a non canonical C-linear
isomorphism Ext 1(Pk,M ′)≃ ⨁
1≤j<k Ext1(Pk,P j). One can go further us-
ing the matricial description of paragraph 2.3.3. We keep th e notations re-
called at the beginning of subsection 3.3.1 and moreover den oteMU the class
inF(P1,...,P k) of the module MU := (K n, ΦAU ) for U := (Ui,j)1≤i<j≤k∈∏
1≤i<j≤k
Matri,rj(C({z})).
Proposition 3.3.4. — The map U ↦→MU from ∏
1≤i<j≤k
Matri,rj(Kµi,µj) to
F(P1,...,P k) is one-to-one.
Proof. — We already now that the map is onto and the conclusion will f ollow
from the following fact: for all U ∈ ∏
1≤i<j≤k
Matri,rj(C({z})), there exists a
unique pair (F,V )∈ G(C({z}))× ∏
1≤i<j≤k
Matri,rj(Kµi,µj) such that F[AV ] =
AU. Writing F as in equation (2.3) and V = (Vi,j), this is equivalent to the
following system:
∀(i,j ), 1≤i<j ≤k, Vi,j+
j−1∑
ℓ=i+1
(σqFi,ℓ)Vℓ,j+(σqFi,j)(zµjAj) = (zµiAi)Fi,j+
j−1∑
ℓ=i+1
Ui,ℓFℓ,j+Ui,j.
It is understood that an empty sum vanishes: if (tℓ) is any sequence,
j−1∑
ℓ=i+1
tℓ =
0 when j = i + 1. Then, U being given, the system is (uniquely) solved by
induction on j−i by the following formulas:
(Fi,j,V i,j) :=Red
(
µi,A i,µ j,A j,U i,j +
j−1∑
ℓ=i+1
Ui,ℓFℓ,j−
j−1∑
ℓ=i+1
(σqFi,ℓ)Vℓ,j
)
.
The following is a particular case of theorem 3.1.4, page 31 (itself a particu-
lar case of corollary A.6.5, page 155): the only novelty bein g that, in the case
of integral slopes, we obtain an explicit coordinate system .
Theorem 3.3.5. — The set F(P1,...,P k) is an aﬃne space of dimension∑
1≤i<j≤k
rirj(µj−µi).
Proof. — This is an immediate consequence of the proposition.
