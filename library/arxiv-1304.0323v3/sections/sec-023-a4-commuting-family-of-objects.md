---
doc_id: arxiv-1304.0323v3
doc_title: "SYMMETRIC QUIVER HECKE ALGEBRAS"
section_id: sec-023-a4-commuting-family-of-objects
section_title: "A.4. Commuting family of objects"
section_number: null
pages: 70-71
source_pdf: 1304.0323v3.pdf
source_sha256: 92e2b9dc876e1a52
doc_brief: "SYMMETRIC QUIVER HECKE ALGEBRAS — Let J be a set of pairs consisting of good U ′ q(g)-modules and invertible elements in the base ﬁeld C(q)."
---
of object {Pi}i∈I inT and a family of isomorphisms {Bi,j : Pi⊗Pj ∼−→Pj⊗Pi}i,j∈I.
Deﬁnition A.4.1. We say that ({Pi}i∈I,{Bi,j}i,j∈I) is a commuting family if the iso-
morphisms Bi,j(i,j∈I) satisfy the following conditions:
(a) Bi,i = idPi⊗Pi for any i∈I,
(b) Bj,i◦Bi,j = idPi⊗Pj for any i,j ∈I,
(c) the isomorphisms {Bi,j}i,j∈I satisﬁes the Yang-Baxter equation; namely,
the following diagram is commutative for any i,j,k ∈I:
Pi⊗Pj⊗PkBi,j
/d115/d115❣❣❣❣❣❣ Bj,k
/d43/d43❲❲❲❲❲❲
Pj⊗Pi⊗Pk
Bi,k
/d15/d15
Pi⊗Pk⊗Pj
Bi,k
/d15/d15
Pj⊗Pk⊗Pi
Bj,k
/d43/d43❲❲❲❲❲❲ Pk⊗Pi⊗Pj
Bi,j
/d115/d115❣❣❣❣❣❣
Pk⊗Pj⊗Pi.
Let us denote by {ei}i∈I the canonical basis of Z⊕I. If ( {Pi}i∈I,{Bi,j}i,j∈I) is a
commuting family, then we can ﬁnd
(i) an object Pα ofT for any α∈ Z⊕I
≥0,
(ii) an isomorphism Pi ∼−→Pei for any i∈I,
(iii) an isomorphism fα,β : Pα⊗Pβ ∼−→Pα+β for any α,β ∈ Z⊕I
≥0,
satisfying the following conditions:
SYMMETRIC QUIVER HECKE ALGEBRAS AND R-MATRICES 71
(a) P 0 is isomorphic to 1,
(b) the diagram
Pα⊗Pβ⊗Pγ fα,β /d47/d47
fβ,γ
/d15/d15
Pα+β⊗Pγ
fα+β,γ
/d15/d15
Pα⊗Pβ+γ fα,β+γ /d47/d47Pα+β+γ
is commutative for any α,β,γ ∈ Z⊕I
≥0,
(c) the diagram
Pi⊗Pj
∼ /d47/d47
Bi,j
/d15/d15
Pei⊗Pej
fei,ej
/d38/d38▼▼▼▼▼▼▼▼▼▼▼
Pj⊗Pi
∼ /d47/d47Pej⊗Pei
fej ,ei
/d47/d47Pei+ej
is commutative for any i,j ∈I.
Moreover, such an ({Pα}α∈Z⊕I
≥0
,{fα,β}α,β∈Z⊕I
≥0
) is unique up to a unique isomorphism.
More generally, we have the following lemma.
Lemma A.4.2. Let ({Pi}i∈I,{Bi,j}i,j∈I) and ({P′
i}i∈I,{B′
i,j}i,j∈I) be two commuting
families, and let ({Pα}α∈Z⊕I
≥0
,{fα,β}α,β∈Z⊕I
≥0
) and ({P′α}α∈Z⊕I
≥0
,{f′
α,β}α,β∈Z⊕I
≥0
) be the cor-
responding families as above. Let ϕi : Pi→ P′
i (i∈ I) be a family of morphisms such
that the diagram
Pi⊗Pj
Bi,j
/d15/d15
ϕi⊗ϕj /d47/d47P′
i⊗P′
j
B′
i,j
/d15/d15
Pj⊗Pi
ϕj⊗ϕi /d47/d47P′
j⊗P′
i
is commutative for any i,j ∈ I. Then there exists a unique family of morphisms
ϕα : Pα→P′α (α∈ Z⊕I
≥0) such that the diagram
Pα⊗Pβ
fα,β
/d15/d15
ϕα⊗ϕβ /d47/d47P′α⊗P′β
f ′
α,β
/d15/d15
Pα+β ϕα+β /d47/d47P′α+β
is commutative for any α,β ∈ Z⊕I
≥0, and ϕei =ϕi for any i∈I.
