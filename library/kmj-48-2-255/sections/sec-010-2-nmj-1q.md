---
doc_id: kmj-48-2-255
doc_title: "A formula for the colored Jones polynomial of 2-bridge knots"
section_id: sec-010-2-nmj-1q
section_title: "(n−mj −1)q"
section_number: 2
pages: 15-16
source_pdf: KMJ-48-2-255.pdf
source_sha256: 720279042c6d762b
doc_brief: "A formula for the colored Jones polynomial of 2-bridge knots — We derive a formula for the colored Jones polynomial of 2-bridge knots."
---
σj+1 −σj
2
1
2
(n−mj )(n−mj −1)
=
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
q
−n ∑p′ −1
j=1
σj+1 − σj
2
mj
.
Here we used σ2 = σp′ = −1 if p < 2t and σ2 = σp′ = 1 if p > 2t. Recalling
mj − mj−1 = lj, it is changed to
(qσp′ )n−1(qσp′ )mp′
(qσp′ )n−mp′ −1
(−1)
∑p′
j=1 lj q− ∑p′
j=1
1
2 σj lj (lj +1)(13)
×


p′
∏
j=1
(q−σj )mj −mj−1


−1
q−n ∑p′ −1
j=1
σj+1 −σj
2 mj .
Accordingly, we obtain
d(l) −
p′−1∑
j=1
σj+1 − σj
2 mj
= − 1
2
p′
∑
j=1
{
p′
∑
k=r′(j)
(σik + σip′+1−k ) +
p′
∑
k=j
(σk + σp′+1−k)}(mj − mj−1)
−
p′
∑
j=1
σj −
p′−1∑
j=1
σj+1 − σj
2 mj
= − 1
2
p′
∑
j=1
p′
∑
k=r′(j)
(σik + σip′+1−k )(mj − mj−1) − 1
2
p′
∑
j=1
p′
∑
k=j
(σk + σp′+1−k)(mj − mj−1)
−
p′
∑
j=1
σj −
p′−1∑
j=1
σj+1 − σj
2 mj
= − 1
2
p′
∑
j=1
p′
∑
k=r′(j)
(σik + σip′+1−k )(mj − mj−1) − 1
2
p′
∑
j=1
(
p′
∑
k=j
(σk + σp′+1−k)mj
−
p′
∑
k=j+1
(σk + σp′+1−k)mj) −
p′
∑
j=1
σj −
p′−1∑
j=1
σj+1 − σj
2 mj
270 Toshie Takata
= − 1
2
p′
∑
j=1
p′
∑
k=r′(j)
(σik + σip′+1−k )(mj − mj−1) − 1
2
p′
∑
j=1
(σj + σp′+1−j)mj
−
p′
∑
j=1
σj − 1
2
p′−1∑
j=1
(σj+1 − σj)mj
= − 1
2
p′
∑
j=1
p′
∑
k=r′(j)
(σik + σip′+1−k )(mj − mj−1)
− 1
2
p′−1∑
j=1
(σj+1 + σp′+1−j)mj − 1
