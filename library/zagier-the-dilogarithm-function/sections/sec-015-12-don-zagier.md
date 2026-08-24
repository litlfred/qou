---
doc_id: zagier-the-dilogarithm-function
doc_title: "The dilogarithm function"
section_id: sec-015-12-don-zagier
section_title: "Don Zagier"
section_number: 12
pages: 10-10
source_pdf: zagier-the-dilogarithm-function.pdf
source_sha256: 05079cf525c6ba0f
doc_brief: "The dilogarithm function — 56 sections: Don Zagier; The dilogarithm function in geomet; The Bloch-Wigner function D(z) and"
---
where f : P1(C)→ P1(C) is a function of degree n and a0 = f(z0). (Equa-
tion (1) is the special case when f is a polynomial, so f −1(∞)i s∞ with
multiplicityn.)
Finally, we mention that a real-analytic function on P1(C) /integerdivide{0,1,∞},
built up out of the polylogarithms in the same way as D(z) was constructed
from the dilogarithm, has been deﬁned by Ramakrishnan [6]. His function
(slightly modiﬁed) is given by
Dm(z)= ℜ
(
im+1
[ m∑
k=1
(−log|z|)m−k
(m−k)! Lik(z)− (−log|z|)m
2m!
])
(so D1(z) = log|z1/2−z−1/2|, D2(z)=D (z)) and satisﬁes
Dm
( 1
z
)
=( −1)m−1Dm(z),
∂
∂zDm(z)= i
2z
(
Dm−1(z)+ i
2
(−ilog|z|)m−1
(m− 1)!
1+z
1−z
)
.
However, it does not seem to have analogues of the properties (II) and (III):
for example, it is apparently impossible to expressD
3(z) for arbitrary complex
z in terms of only the functionD3(eiθ)= ∑∞
n=1(cosnθ)/n3, and passing from
Li3 toD3 removes many but not all of the numerous lower-order terms in the
various functional equations of the trilogarithm, e.g.:
D3(x)+D 3(1−x)+ D3
( x
x− 1
)
=D3(1) + 1
12 log
⏐⏐x(1−x)
⏐
⏐log
⏐
⏐
⏐
⏐
x
(1−x)2
⏐
⏐
⏐
⏐log
⏐
⏐
⏐
⏐
x
2
1−x
⏐
⏐
⏐
⏐,
D
3
( x(1−y)2
y(1−x)2
)
+D3(xy)+D 3
(x
y
)
− 2D3
( x(1−y)
y(1−x)
)
− 2D3
( 1−y
1−x
)
−2D3
( x(1−y)
x− 1
)
− 2D3
( y(1−x)
y− 1
)
− 2D3(x)− 2D3(y)
=2 D3(1)− 1
4 log
⏐
⏐xy
⏐
⏐log
⏐
⏐
⏐
⏐
x
y
⏐
⏐
⏐
⏐log
⏐
⏐
⏐
⏐
x(1−y)
2
y(1−x)2
⏐
⏐
⏐
⏐.
Nevertheless, these higher Bloch-Wigner functions do occur. In studying the
so-called “Heegner points” on modular curves, B. Gross and I had to study
for n =2 ,3,... “higher weight Green’s functions” for H/Γ (H = complex
upper half-plane, Γ = SL
2(Z) or a congruence subgroup). These are func-
