---
doc_id: kmj-48-2-255
doc_title: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata"
section_id: sec-012-3-results-for-a-twist-knot
section_title: "Results for a twist knot"
section_number: 3
pages: 19-24
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A Formula for the Colored Jones Polynomial of 2-Bridge Knots Toshie Takata — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
In this section, we will consider the twist knots S(4p1 + 1, 2p1 + 1) and S(4p1 −
1, 2p1 − 1).
From Theorem 1, we get explicit formulas for the colored Jones polynomials of
these twist knots.
Corollary 5.
JS(4p1+1,2p1+1)(n) (14)
=
∑
0≤mj−1≤mj ≤n−1
q−n ∑2p1−1
i=1 (−1)imi+∑p1 −1
i=1 m2i(1+m2i+1)
×
(¯q)n−1(¯q)mp′
(¯q)n−mp′ −1
(−1)mp′


p1−1∏
j=0
(¯q)m2j+1−m2j
p1∏
j=1
(q)m2j −m2j−1


−1
,
and
JS(4p1−1,2p1−1)(n) (15)
=
∑
0≤mj−1≤mj ≤n−1
qn(−1+∑2p1 −2
i=1 (−1)imi−2m2p1 −1)+1−∑p1−1
i=1 m2i−1(1+m2i)
×
(q)n−1(q)mp′
(q)n−mp′ −1
(−1)mp′


p1−1∏
j=0
(¯q)m2j+1−m2j
p1−1∏
j=1
(q)m2j −m2j−1


−1
.
Proof. Firstly, let us consider the knot S(4p1 + 1, 2p1 + 1) for p1 ≥ 1. It is easy to
see that
Lemma 6. (1) σj = (−1)j−1
(2) ik =
{
2p1 + 2 − 2k if 1 ≤ k ≤ p1
2(k − p1) − 1 if p1 + 1 ≤ k ≤ 2p1, σik =
{
−1 if 1 ≤ k ≤ p1
1 if p1 + 1 ≤ k ≤ 2p1.
274 Toshie Takata
Lemma 7. (1) σik + σip′+1−k = 0. (2) σj+1 + σp′+1−j = (−2)j.
From the above lemmas, we obtain
(16) a(m) = −
2p1−1∑
j=1
(−1)jmj.
We compute b1(m) and b2(m). One calculate
(17)
∑
1≤k≤ p−t
2
1 − σik
2 mik−1 =
p1∑
j=1
m2j−1,
∑
p−t
2 +1≤k≤p′
mik−1 =
p1−1∑
j=1
m2j,
∑
p−t
2 +1≤k≤p′
1 + σik
2 mik(18)
=
∑
p1+1≤k≤2p1
mik =
∑
p1+1≤k≤2p1
m2k−2p1−1 =
p1∑
j=1
m2j−1
(1 + σp′ )mp′ = 0,(19)
p′−1∑
j=1
(σj+1 − σj)mj = −2
p1∑
j=1
m2j−1 + 2
p1−1∑
j=1
m2j = 2
2p1−1∑
j=1
(−1)jmj.(20)
Moreover, it follows that k < k ′ and σik ⁄= σik′ if and only if 1 ≤ k ≤ p1 and
p1 + 1 ≤ k′ ≤ 2p1. We note that sign( ik − ik′ ) = 1 if and only if ik > i k′ and that
ik = 2p1 + 2 − 2k for 1 ≤ k ≤ p1 and ik′ = 2k′ − 2p1 − 1 for p1 + 1 ≤ k′ ≤ 2p1.
So, we obtain
∑
1≤k≤p′
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)
= −2
∑
1≤k≤p1
∑
p1+1≤k′≤2p1+1−k
(m2p1+2−2k − m2p1+1−2k)(m2k′−2p1−1 − m2k′−2p1−2)
= −2
∑
1≤j≤p1
∑
1≤j′≤j
(m2j − m2j−1)(m2j′−1 − m2j′−2),
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 275
and
p′
∑
j=1
σj(
r′(j)∑
k=1
(mik − mik−1))mj−1
=
p1∑
j=1
σ2j−1(
r′(2j−1)∑
k=1
(mik − mik−1))m2j−2 +
p1∑
j=1
σ2j(
r′(2j)∑
k=1
(mik − mik−1))m2j−1
=
p1∑
j=1
σ2j−1(
p1+j∑
k=1
(mik − mik−1))m2j−2 +
p1∑
j=1
σ2j(
p1−j+1∑
k=1
(mik − mik−1))m2j−1
=
p1∑
j=1
(
p1∑
k=1
(m2p1+2−2k − m2p1+1−2k) +
p1+j∑
k=p1+1
(m2k−2p1−1 − m2k−2p1−2))m2j−2
−
p1∑
j=1
(
p1−j+1∑
k=1
(m2p1+2−2k − m2p1+1−2k))m2j−1
=
p1∑
j=1
(
p1∑
j′=1
(m2j′ − m2j′−1) +
j∑
j′=1
(m2j′−1 − m2j′−2))m2j−2
−
p1∑
j=1
(
p1∑
j′=j
(m2j′ − m2j′−1))m2j−1
=
p1∑
j=1
(m2j +
p1∑
j′=j+1
(m2j′ − m2j′−1))m2j−2 −
p1∑
j=1
(
p1∑
j′=j
(m2j′ − m2j′−1))m2j−1
=
p1∑
j=1
(
p1∑
j′=j
(m2j′ − m2j′−1) + m2j−1)m2j−2 −
p1∑
j=1
(
p1∑
j′=j
(m2j′ − m2j′−1))m2j−1.
Summing up, we obtain
(21) b1(m) + b2(m) =
p1−1∑
j=1
m2j(1 + m2j+1).
Next, we consider the knot S(4p1 − 1, 2p1 − 1) for p1 ≥ 1. It is not hard to show
the following two lemmas.
Lemma 8. It follows that (1) σj = (−1)j−1, and
(2) ik =
{
2p1 − 2k + 1 if 1 ≤ k ≤ p1,
2(k − p1) if p1 + 1 ≤ k ≤ 2p1 − 1, σik =
{
1 if 1 ≤ k ≤ p1,
−1 if p1 + 1 ≤ k ≤ 2p1 − 1.
Lemma 9. (1) σik + σip′+1−k =
{
2 if k = p1,
0 if k ⁄= p1. (2) σj+1 + σp′+1−j = 0.
276 Toshie Takata
From these lemmas, it follows that
(22) a(m) =
2p1−2∑
i=1
(−1)imi − 2m2p1−1 − 1,
We compute
∑
1≤k≤ p−t
2
1 − σik
2 mik−1 =
∑
1≤k≤p1
1 − σik
2 mik−1 = 0,(23)
∑
p−t
2 +1≤k≤p′
mik−1 =
∑
p1+1≤k≤2p1−1
mik−1 =
∑
p1+1≤k≤2p1−1
m2k−2p1−1(24)
=
p1−1∑
j=1
m2j−1,
∑
p−t
2 +1≤k≤p′
1 + σik
2 mik =
∑
p1+1≤k≤2p1−1
1 + σik
2 mik = 0,(25)
(1 + σp′)mp′ = 2m2p1−1,(26)
p′−1∑
j=1
(σj+1 − σj)mj =
2p1−2∑
j=1
(σj+1 − σj)mj = 2
2p1−2∑
i=1
(−1)imi.(27)
Moreover, it follows that k < k ′ and σik ⁄= σik′ if and only if 1 ≤ k ≤ p1 and
p1 + 1 ≤ k′ ≤ 2p1 − 1. We note that sign( ik − ik′) = 1 if and only if ik > i k′ and
that ik = 2p1 − 2k + 1 for 1 ≤ k ≤ p1 and ik′ = 2k′ − 2p1 for p1 + 1 ≤ k′ ≤ 2p1 − 1.
So, we compute
∑
1≤k≤p′
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)
= 2
∑
1≤k≤p1
∑
p1+1≤k′≤2p1−k
(m2p1−2k+1 − m2p1−2k)(m2k′−2p1 − m2k′−2p1−1)
= 2
∑
0≤j≤p1−1
∑
1≤j′≤j
(m2j+1 − m2j)(m2j′ − m2j′−1),
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 277
and
p′
∑
j=1
σj(
r′(j)∑
k=1
(mik − mik−1))mj−1
=
p1∑
j=1
σ2j−1(
r′(2j−1)∑
k=1
(mik − mik−1))m2j−2 +
p1−1∑
j=1
σ2j(
r′(2j)∑
k=1
(mik − mik−1))m2j−1
=
p1∑
j=1
(
p1−j+1∑
k=1
(mik − mik−1))m2j−2 −
p1−1∑
j=1
(
p1−j∑
k=1
(mik − mik−1))m2j−1
=
p1∑
j=1
(
p1−j+1∑
k=1
(m2p1−2k+1 − m2p1−2k))m2j−2
−
p1−1∑
j=1
(
p1∑
k=1
(m2k−2p1+1 − m2k−2p1) +
p1+j∑
k=p1+1
(m2p1−2k − m2p1−2k−1))m2j−1
=
p1∑
j=1
(
p1∑
j′=j
(m2j′−1 − m2j′−2)m2j−2 −
p1−1∑
j=1
(
p1−1∑
j′=1
(m2j′+1 − m2j′) +
j∑
j′=1
(m2j′ − m2j′−1))m2j−1
=
p1∑
j=1
(
p1∑
j′=j
(m2j′−1 − m2j′−2))m2j−2 −
p1−1∑
j=1
(
p1∑
j′=j+1
(m2j′−1 − m2j′−2) + m2j)m2j−1
=
∑
0≤j′≤p1−1
∑
1≤j≤j′
(m2j′+1 − m2j′)(m2j − m2j−1) −
p1−1∑
j=1
m2jm2j−1.
Thus we obtain
(28) b1(m) + b2(m) = 1 −
p1−1∑
j=1
m2j−1(1 + m2j).
□
Using Corollary 5, we give explicit formulas for the trefoil knot S(3, 1) and the
ﬁgure eight knot S(5, 3).
By the formula (15) with p1 = 1 and p′ = 1, we get
JS(3,1)(n) =
∑
0≤m1≤n−1
(q)n−1(q)m1 (−1)m1
(q)n−m1−1(¯q)m1
qn(−1−2m1)+1
=
∑
0≤m1≤n−1
(¯qn−1 − 1) · · · (¯qn−m1 − 1)(−1)m1qn(−1−m1)+1.
278 Toshie Takata
By the formula (14) with p1 = 1 and p′ = 1,
JS(5,3)(n) =
∑
0≤m1≤m2≤n−1
(¯q)n−1(¯q)m2
(¯q)n−m2−1(¯q)m1 (q)m2−m1
qnm1 (−1)m2,
and using the formula
k∑
i=0
(q)k
(q)k−i(¯q)i
q− i
