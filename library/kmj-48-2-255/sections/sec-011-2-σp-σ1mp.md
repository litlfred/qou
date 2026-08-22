---
doc_id: kmj-48-2-255
doc_title: "A formula for the colored Jones polynomial of 2-bridge knots"
section_id: sec-011-2-σp-σ1mp
section_title: "(σp′ + σ1)mp′ −"
section_number: 2
pages: 16-19
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A formula for the colored Jones polynomial of 2-bridge knots — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
p′
∑
j=1
σj
= a(m),
and for the case where p < 2t,
C 0(l) −
p′
∑
j=1
1
2 σjlj(lj + 1)
= −a(m) − 1
2
p′−1∑
j=1
(σj+1 − σj)mj
+
∑
1≤k≤ p−t
2
1 − σik
2 mik−1 +
∑
p−t
2 +1≤k≤ t−1
2
1 + σik
2 mik−1
+
∑
p−t
2 +1≤k≤p′
1 + σik
2 mik −
∑
p−t
2 +1≤k≤p′
mik−1 − mp′ −
p′
∑
j=1
σj(mj − mj−1)
− 1
2



∑
1≤k≤p′
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)



+
∑
1≤k≤p′
σjmj−1(
r′(j)∑
k=1
(mik − mik−1))
= −a(m) − (1 + σp′)mp′ + 1
2
p′−1∑
j=1
(σj+1 − σj)mj
+
∑
1≤k≤ p−t
2
1 − σik
2 mik−1 +
∑
p−t
2 +1≤k≤ t−1
2
1 + σik
2 mik−1
+
∑
p−t
2 +1≤k≤p′
1 + σik
2 mik −
∑
p−t
2 +1≤k≤p′
mik−1
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 271
− 1
2



∑
1≤k≤p′−1
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)



+
∑
1≤k≤p′
σjmj−1
r′(j)∑
k=1
(mik − mik−1)
= b1(m) + b2(m),
and for the case where p > 2t,
C 0(l) −
p′
∑
j=1
1
2 σjlj(lj + 1)
= −a(m) − 1
2
p′−1∑
j=1
(σj+1 − σj)mj
+
∑
1≤k≤ p−t
2
1 − σik
2 mik−1 +
∑
p−t
2 +1≤k≤ p−1
2
1 + σik
2 mik −
∑
p−t
2 +1≤k≤ p−1
2
mik−1
−
∑
t+1
2 +1≤k≤ p−t
2
1 + σik
2 mik−1 − mp′ −
p′
∑
j=1
σj(mj − mj−1)
− 1
2



∑
1≤k≤p′
∑
k+1≤k′≤p′
1 + sign(ik − ik′ )
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)



+
∑
1≤k≤p′
σjmj−1(
r′(j)∑
k=1
(mik − mik−1))
= −a(m) − (1 + σp′)mp′ + 1
2
p′−1∑
j=1
(σj+1 − σj)mj
+
∑
1≤k≤ p−t
2
1 − σik
2 mik−1 +
∑
p−t
2 +1≤k≤p′
1 + σik
2 mik −
∑
p−t
2 +1≤k≤p′
mik−1
−
∑
t+1
2 +1≤k≤ p−t
2
1 + σik
2 mik−1
− 1
2



∑
1≤k≤p′−1
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)



+
∑
1≤k≤p′
σjmj−1(
r′(j)∑
k=1
(mik − mik−1)) = b1(m) + b2(m).
272 Toshie Takata
Thus we obtain the formula (1).
For example, we give an explicit formula for the colored Jones polynomial of
the knot 6 2, which is not a twist knot. The knot 6 2 has the Schubert’s normal form
S(11, 7). We see p′ = 5,
σ1 = 1, σ2 = −1, σ3 = −1, σ4 = 1, σ5 = 1,
r′(1) = 4 , r′(2) = 1 , r′(3) = 5 , r′(4) = 3 , r′(5) = 2 , i1 = 2, i2 = 5, i3 = 4, i4 = 1, i5 = 3,
σi1 = −1, σi2 = −1, σi3 = 1, σi4 = 1, σi5 = −1,
and so
5∑
k=r′(1)
(σik + σi6−k ) = −2,
5∑
k=r′(2)
(σik + σi6−k ) = −2,
5∑
k=r′(3)
(σik + σi6−k ) = −2,
5∑
k=r′(4)
(σik + σi6−k ) = 0 ,
5∑
k=r′(5)
(σik + σi6−k ) = 0 ,
4∑
j=1
(σj+1 + σ6−j) = −2m1 − 2m4.
Thus, we get a(m) = 1 + m1 + m3 + m4. Moreover, we calculate
∑
1≤k≤2
1 − σik
2 mik−1 = m1+m4,
∑
3≤k≤2
mik−1 = m3+m2,
∑
3≤k≤5
1 + σik
2 mik = m4+m1,
1 + σ5 = 0,
4∑
j=1
(σj+1 − σj)mj = −2m1 + 2m3 − 2m4,
∑
1≤k≤p′−1
∑
k+1≤k′≤p′
1 + sign(ik − ik′)
2 (σik − σik′ )(mik − mik−1)(mik′ − mik′ −1)
= −2(m2 − m1)m1 − 2(m5 − m4)(m4 − m3) − 2(m5 − m4)m1 + 2(m4 − m3)(m3 − m2),
p′
∑
j=1
σj(
r′(j)∑
k=1
(mik − mik−1))mj−1
= −m1(m2 − m1) − m2m5) + m3(m2 − m1 + m5 − m3) + (−m4)(m2 − m1 + m5 − m4),
and so b1(m) = −1 − m2 − m3 + m1m5 − m2m5 − m1m3. It is easy to compute
b2(m) = m3.
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 273
Finally, we obtain
JS(11,7)(n)
=
∑
0≤mj−1 ≤mj ≤n−1
1≤j≤5
qn(1+m1+m3+m4)−1−m2+m1m5−m2m5−m1m3
× (q)n−1(q)m5
(q)n−m5−1
((¯q)m1(q)m2−m1 (q)m3−m2 (¯q)m4−m3(q)m5−m4)−1 (−1)m5 .
