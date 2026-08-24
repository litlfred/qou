---
doc_id: kmj-48-2-255
doc_title: "A formula for the colored Jones polynomial of 2-bridge knots"
section_id: sec-009-2-σik-σik-lik-lik
section_title: "(σik − σik′ )lik lik′ }"
section_number: 2
pages: 13-15
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A formula for the colored Jones polynomial of 2-bridge knots — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
+
∑
1≤k≤p′
σj
(
−
j−1∑
k=1
lk
) 
−
r′(j)∑
k=1
lik


= −d(l) +
∑
1≤k≤ p−t
2
1 − σik
2
∑
1≤s≤ik−1
ls +
∑
p−t
2 +1≤k≤p′
1 + σik
2 lik
−
∑
p−t
2 +1≤k≤p′
1 − σik
2
∑
1≤s≤ik−1
ls −
∑
t+1
2 +1≤k≤ p−t
2
1 + σik
2
∑
1≤s≤ik−1
ls
268 Toshie Takata
−
p′
∑
j=1
lj − 1
2
p′
∑
j=1
σjlj + 1
2
p′
∑
j=1
σjlj
2
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
2 (σik − σik′ )lik lik′



+
∑
1≤k≤p′
σj(
j−1∑
k=1
lk)(
r′(j)∑
k=1
lik ).
We compute the remaining term in the formula (2). Since σ1 = 1, s(1a) = 0,
and s(ja) = ∑j−1
k=1 lk(2 ≤ j ≤ p′),
c∏
j=1
{ s(j) + lj
lj
}
σj
(qσj (n−s(j)−1) − 1) · · · (qσj (n−s(j)−lj ) − 1)
=
p′
∏
j=1
{ ∑j
k=1 lk
lj
}
σj
(qσj (n−∑j−1
k=1 lk−1) − 1) · · · (qσj (n−∑j−1
k=1 lk−lj ) − 1).
Putting mj := ∑j
k=1 lk and m0 = 0, the right hand side is changed to
(9)
p′
∏
j=1
{ mj
mj − mj−1
}
σj
(qσj (n−mj−1−1) − 1) · · · (qσj (n−mj ) − 1).
Noting that
(qσj (n−mj−1−1) − 1) · · · (qσj (n−mj ) − 1) = (qσj )n−mj−1−1
(qσj )n−mj −1
,(10)
{ mj
mj − mj−1
}
σj
= (qσj )mj
(qσj )mj −mj−1(qσj )mj−1
,(11)
(qσ)m
(qσ′
)m
= (−1)
σ−σ′
2 mq
σ−σ′
2 · 1
2 m(m+1),(12)
(9) can be exchanged to
(qσp′ )n−1(qσp′ )mp′
(qσp′ )n−mp′ −1


p′
∏
j=1
(qσj )mj −mj−1


−1
A Formula for the Colored Jones Polynomial of 2-Bridge Knots 269
×
p′−1∏
j=2
(−1)
σj −σj+1
2 mj q
σj −σj+1
2
1
2 mj (mj +1)
×
p′−1∏
j=2
(−1)
σj+1 −σj
