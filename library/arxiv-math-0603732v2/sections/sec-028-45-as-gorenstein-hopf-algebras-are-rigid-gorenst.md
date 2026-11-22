---
doc_id: arxiv-math-0603732v2
doc_title: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS"
section_id: sec-028-45-as-gorenstein-hopf-algebras-are-rigid-gorenst
section_title: "AS-Gorenstein Hopf algebras are rigid Gorenstein"
section_number: 4.5
pages: 15-16
source_pdf: 0603732v2.pdf
source_sha256: 3464a2ddc2e54f3a
toc_source: outline
doc_brief: "DUALISING COMPLEXES AND TWISTED HOCHSCHILD (CO)HOMOLOGY FOR NOETHERIAN HOPF ALGEBRAS — We show that many noetherian Hopf algebras A have a rigid du- alising complex R with R ∼ = νA1[d]."
---
4.5. AS-Gorenstein Hopf algebras are rigid Gorenstein. In this subsection
we prove the statement in the heading, and also that the automorphism ξS2 is the
Nakayama automorphism of A. (Recall that ξ is deﬁned in (2.5.1).) Throughout
this subsection we assume that S is bijective.
Lemma. Let A be a Hopf algebra and let π : A →k be an algebra map. Then, as
A-bimodules,
kπ ⊗A L(Ae) = kΞ[π] ⊗A L(Ae) ∼= 1AΞ[π]S2.
Proof. The lemma follows from a direct computation after we understand the mod-
ule structure on L(Ae).
As a k-vector space, Ae is isomorphic to A ⊗A; and there are four diﬀerent A-
actions on Ae which commute with each other. To avoid possible confusions we will
try to use diﬀerent notations to indicate diﬀerent places of A and diﬀerent actions
of A. Let B = A as a Hopf algebra and N = A as A-bimodule. We denote the four
A-module structures as follows. The left A-action on A and the right B-action on
A, both induced by the multiplication of A, are denoted by ∗1 and ∗2 respectively.
The left B-action on N induced by the multiplication of A is denoted by ∗3 and
another left A-action on N deﬁned by
a ∗4 n = nS(a).
Hence A ⊗N has a left A ⊗A-module structure induced by ∗1 and ∗4 and a B-
bimodule structure induced by ∗3 and ∗2. The left A-action on L(Ae) is deﬁned
via the coproduct ∆and the A ⊗A-action on A ⊗N. The assertion of the lemma
is equivalent to the following statement: as B-bimodules,
kπ ⊗A Res∆(A ⊗N) ∼= 1BΞ[π]S2.
(4.5.1)
Let J = ker π. Then A/J = kπ as right A-module and π induces a natural
B-bimodule homomorphism
f : Res∆(A ⊗N) →Res∆(A ⊗N)/J Res∆(A ⊗N) = kπ ⊗A Res∆(A ⊗N).
To prove the assertion (4.5.1) it suﬃces to show the following:
Ξ[π]S2(b) ∗3 (1 ⊗1) −(1 ⊗1) ∗2 b
=
(4.5.2)
1 ⊗Ξ[π]S2(b) −b ⊗1 ∈J Res∆(A ⊗N).
b ∗3 (1 ⊗1) = 1 ⊗b̸ ∈J Res∆(A ⊗N).
(4.5.3)
By Lemma 2.1(b), there is an isomorphism Φ : Res∆(A ⊗N) →A ⊗kN where
Φ(a ⊗n) = P a1 ⊗S(a2) ∗4 n. This isomorphism induces a commutative diagram
Res∆(A ⊗N)
Φ
−−−−→
A ⊗kN
f
y
yf ′
kπ ⊗A Res∆(A ⊗N)
∼
=
−−−−→A/J ⊗kN
where f ′ : A ⊗N →A ⊗N/J(A ⊗N) = A/J ⊗N = k ⊗N is the canonical
map. Now the conditions in (4.5.2) and (4.5.3) are equivalent to the following two
conditions
f ′Φ(1 ⊗Ξ[π]S2(b) −b ⊗1) = 0 for all b ∈B.
(4.5.4)
f ′Φ(1 ⊗b)̸ = 0 for all b ∈B.
(4.5.5)
16
K.A. BROWN AND J.J. ZHANG
By deﬁnition,
f ′Φ(b ⊗1) = f ′(
X
b1 ⊗S(b2) ∗4 1) = f ′(
X
b1 ⊗S2(b2)) =
X
π(b1) ⊗S2(b2).
By Lemma 2.5(d),
X
π(b1) ⊗S2(b2) =
X
π(S2(b1)) ⊗S2(b2) =
X
1 ⊗π(S2(b1))S2(b2).
Since S2 commutes with ∆, we have
X
1 ⊗π(S2(b1))S2(b2) = 1 ⊗Ξ[π]S2(b) = f ′Φ(1 ⊗Ξ[π]S2(b)).
Thus (4.5.4) follows. To see (4.5.5) we note, for every 0̸ = b ∈B,
f ′Φ(1 ⊗b) = 1 ⊗b
which is a nonzero element in k ⊗N.
□
Proposition. Let A be a noetherian AS-Gorenstein Hopf algebra (with bijective
antipode S). Let d be the injective dimension of A.
(a) A is rigid Gorenstein with Nakayama automorphism ξS2.
(b) The rigid dualising complex of A is
ξS2A1[d].
(c) R l
A = 1kξS2 = 1kξ.
Proof. (a) By Lemma 2.4(b), for all i ≥0,
Exti
Ae(A, Ae) ∼= Exti
A(k, L(Ae)).
Since L(Ae) is a free left A-module by Lemma 2.2(c), we have
Exti
A(k, L(Ae)) ∼= Exti
A(k, A) ⊗A L(Ae).
By the AS-Gorenstein condition, for every i < d, Exti
A(k, A) = 0 and hence
Exti
Ae(A, Ae) = 0. The only nonzero term is
Extd
Ae(A, Ae) ∼= Extd
A(k, A) ⊗A L(Ae) ∼= kξ ⊗A L(Ae) ∼= 1AξS2
where the last isomorphism follows from the above lemma. Therefore the assertion
follows.
(b) This follows from (a) and Proposition 4.3.
(c) This is immediate from the deﬁnition, since S2 ﬁxes all one-dimensional
representations of A.
□
Remark. The case of the above proposition where A has ﬁnite k-dimension (or,
equivalently, d = 0), is [Sc, Proposition 3.6]. Note also the earlier result of Oberst
and Schneider [OS]: a ﬁnite dimensional Hopf algebra is symmetric - that is, its
Nakayama automorphism is the identity - if and only if S2 = ξ = idA .
