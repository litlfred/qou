---
doc_id: arxiv-0903.0853v3
doc_title: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS"
section_id: sec-109-431-study-of-h-1eq-λi-we-choose-τ-cℑτ-0-such-tha
section_title: "Study of H 1(Eq; ΛI). — We choose τ ∈ C,ℑ(τ) > 0, such that"
section_number: 4.3.1
pages: 63-65
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Jean-Pierre Ramis Jacques Sauloy Changgui Zhang LOCAL ANALYTIC CLASSIFICATION OF q-DIFFERENCE EQUATIONS — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symm"
---
q =e−2iπτ . Since (1,τ ) is a basis of theR-vector space C, the group morphism:
p0 : (u,v )↦→e2iπ(u+vτ )
from R2 to C∗ is onto with kernel Z×{ 0}, and the preimage of qZ is
p−1
0 (qZ) = Z× Z.
Therefore, the composition p◦p0 of p0 with the natural projection p : C∗→
Eq = C∗/qZ is a group epimorphism with discrete kernel Z2; it is clearly a
local diﬀeomorphism.
Remark 4.3.1 . — The morphism p0 induces an isomorphism between
R2/Z2 and Eq = C∗/qZ. Through this isomorphism, the natural splitting of
R2/Z2 is carried to the splitting:
C∗ = U×qR,
where U denotes the unit circle in C∗ and, for v∈ R, we denote qv =e−2iπτ v
We will call open parallelogram of Eq the image by the mapp◦p0 : R2→ Eq
of an open parallelogram ]u1,u 2[×]v1,v 2[⊂ R2 whereu2−u1≤ 1,v 2−v1≤ 1.
This is the same as the image by x↦→e2iπx of:
{u +vτ∈ C| u1 <u<u 2,v 1 <v <v 2},
We will call closed parallelogram of Eq the closure of an open parallelogram
such that u2−u1 < 1,v 2−v1 < 1. We will say that a parallelogram is small
if u2−u1 < 1/4 and v2−v1< 1/4.
For every open covering V of Eq, there exists a ﬁnite open covering U =
(Ui)i∈I, ﬁner than V, such that:
(i) the Ui are open parallelograms,
(ii) the open sets Ui are four by four disjoint.
We will call good such a covering. There is a similar deﬁnition for closed
coverings. It is then clear that:
– Every element of H j(Eq; GLn(A )),j = 0, 1 can be represented by an
element of H j(U; GLn(A )), where U is a good covering.
– The natural map H j(U; GLn(A ))→H j(Eq; GLn(A )) is always injective.
Let U be a good open covering of Eq; we denote by ˜C 0(U; GLn(A )) the
subspace of the space of 0-cochains ( gi)∈C 0(U; GLn(A )) whose coboundary
(gij := gig−1
j ) belongs to C 1(U; ΛI). Thus, a cochain C 0(U; GLn(A )) is any
family (gi) such that gi∈ A (Ui), and it belongs to ˜C 0(U; GLn(A )) if, and
58 CHAPTER 4. THE q-ANALOGS OF BIRKHOFF-MALGRANGE-SIBUYA THEOREMS
only if, the gi (i∈I) admit the same asymptotic expansion ˆg∈ GLn
(
C[[z]]
)
.
It is also equivalent to say that the natural image of the coch ain (gi) in
C 0(U; GLn
(
C[[z]]
)
) is a cocycle.
Lemma 4.3.2 . — (i) Let U be a good open covering of Eq. The cobound-
ary map ∂ induces an injection on the double quotient:
C 0(U; ΛI)\ ˜C 0(U; GLn(A ))/H 0(
U; GLn(A )
)
→H 1(U; ΛI).
(ii) We have a canonical injection:
lim
− →U
C 0(U; ΛI)\ ˜C 0(U; GLn(A ))/GLn
(
C{z}
)
→H 1(Eq; ΛI),
where the direct limit is indexed by the good coverings.
Proof. — We have two natural maps:
˜C 0(U; GLn(A ))→Z 1(U; ΛI),
which sends the family (gi) to the family (gij) and
˜C 0(U; GLn(A ))→ GLn
(
C[[z]]
)
,
which sends the family ( gi) to ˆg∈ GLn
(
C[[z]]
)
, the common asymptotic ex-
pansion of all the gi.
Two cochains ( gi), (g′
i) ∈ ˜C 0(U; GLn(A )) deﬁne the same element of
H 1(U; ΛI) if and only if:
g′
ig′−1
j =higig−1
j h−1
j , with (hi)∈C 0(U; ΛI).
This is equivalent to g′−1
j hjgj =g′−1
i higi, which thus deﬁnes an element f∈
H 0(
U; GLn(A )
)
and we have g′ =hgf −1.
Proposition 4.3.3. — For every good open covering U of Eq we have a nat-
ural isomorphism:
C 0(U : ΛI)\ ˜C 0(U; GLn(A ))/H 0(
U; GLn(A )
)
→ GLn
(
C[[z]]
)
/GLn
(
C{z}
)
.
(Note that the double quotient on the left hand side is the sam e as the double
quotient on the left hand side of assertion (i) in the lemma ab ove.)
Proof. — Let U be a good open covering of Eq. Let ˆg∈ GLn
(
C[[z]]
)
. Using
the q-analog of Borel-Ritt (theorem 4.1.4), we can represent it b y an element
gi on each open setUi such thatgi admits ˆg as asymptotic expansion, therefore
the natural map:
˜C 0(U; GLn(A ))→ GLn
(
C[[z]]
)
is onto. The proposition follows.
