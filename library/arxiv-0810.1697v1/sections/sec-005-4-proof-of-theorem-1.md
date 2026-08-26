---
doc_id: arxiv-0810.1697v1
doc_title: "ON THE CABLE EXPANSION FORMULA QIHOU LIU"
section_id: sec-005-4-proof-of-theorem-1
section_title: "Proof of Theorem 1"
section_number: 4
pages: 8-12
source_pdf: 0810.1697v1.pdf
source_sha256: 1aef66179da3c154
doc_brief: "ON THE CABLE EXPANSION FORMULA QIHOU LIU — In this paper, a generalized version of Morton’s formula [8] is proved."
---
Proof.
Assume it’s true for (p,q), let’s do the calculation in the case (q,p).
By explicit calculation, we got
⟨ωr⟩U (A2 − A−2)2 ≡ −2(r + 1)
So by lemma 2,
(−1)l+sgl
σ(q, p; s)(−2(r + 1))
= 4
r−1∑
t=0
∑
k≥0
(−1)k+tgk
σ(p, q; t) sinh((t + 1)(l + 1)C) sinh((s + 1)(k + 1)C)
where we evaluate these polynomials at A = exp( πi
2(r+1) ), and we denote the con-
stant πi
r+1 by C.
CABLE EXPANSION 9
And then using the formula for g(p, q; t), we have
(−1)l+sgl
σ(q, p; s)(−2(r + 1))
= (−1)qN 4
r−1∑
t=0
∑
k≥0
(−1)k+t exp(ǫ(−t2 − 2t + k2 + 2k)C/2)
× sinh((t + 1)(l + 1)C) sinh((s + 1)(k + 1)C)
×
N∑
k′=−N
k′+N even
exp((αk′2 + 2βk ′(t + 1))C/2){δ(k − t − pk′) − δ(k + t + 2 + pk′)}
Note that gk
σ(p, q; t) is 0, unless k + t + pN is even, so ( −1)k+t = (−1)pN .
So
(A) ( −1)l+sgl
σ(q, p; s)(−2(r + 1)) = ( −1)qN (−1)pN × S
where
S = 4
r−1∑
t=0
∑
k≥0
exp(ǫ(−t2 − 2t + k2 + 2k)C/2)
· sinh((t + 1)(l + 1)C) sinh((s + 1)(k + 1)C)
·
N∑
k′=−N
k′+N even
exp((αk′2 + 2βk ′(t + 1))C/2){δ(k − t − pk′) − δ(k + t + 2 + pk′)}
= 4
N∑
k′=−N
k′+N even
r−1∑
t=0
exp(αk′2C/2 + βk ′(t + 1)C) sinh((t + 1)(l + 1)C)
·
∑
k≥0
exp(ǫ(−t2 − 2t + k2 + 2k)C/2) sinh((s + 1)(k + 1)C)
· {δ(k − t − pk′) − δ(k + t + 2 + pk′)}
Lemma 3. Let f (x) be an even function and g(x) be an odd function, then
∑
k≥0
f (k + 1)g(k + 1){δ(k − t − pk′) − δ(k + t + 2 + pk′)}
= f (pk′ + t + 1)g(pk′ + t + 1)
The proof of this lemma will be given later. Now we apply it to calculate th e
innermost summation of S.—- let
f (x) = exp( ǫ(−(t + 1)2 + x2)C/2)
and
g(x) = sinh(( s + 1)Cx),
10 QIHOU LIU
we have
S = 4
N∑
k′=−N
k′+N even
r−1∑
t=0
exp(αk′2C/2 + βk ′(t + 1)C) sinh((t + 1)(l + 1)C)
× exp(ǫpk′(pk′ + 2t + 2)C/2) sinh((s + 1)(pk′ + t + 1)C)
= 4
N∑
k′=−N
k′+N even
r−1∑
t=0
exp(qpk ′2C/2 + qk′(t + 1)C)
× sinh((t + 1)(l + 1)C) sinh((s + 1)(pk′ + t + 1)C)
= 4
r−1∑
t=0
sinh((t + 1)(l + 1)C)
×
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + qk′(t + 1)C) sinh((s + 1)(pk′ + t + 1)C)
Note that α + ǫp2 = qp and β + ǫp = q.
Lemma 4.
N∑
k′=−N
k′+N even
exp(α1k′2 + α2k′) sinh(α3k′ + ζ)
=
N∑
k′=−N
k′+N even
exp(α1k′2
+ α3k′) sinh(α2k′ + ζ)
Apply this lemma to the inner summation of (3.4), we have
CABLE EXPANSION 11
S = 4
r−1∑
t=0
sinh((t + 1)(l + 1)C)
×
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + qk′(t + 1)C) sinh(pk′(s + 1)C + (s + 1)(t + 1)C)
= 4
r−1∑
t=0
sinh((t + 1)(l + 1)C)
×
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + pk′(s + 1)C) sinh(qk′(t + 1)C + (s + 1)(t + 1)C)
= 4
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + pk′(s + 1)C)
×
r−1∑
t=0
sinh((t + 1)(l + 1)C) sinh((t + 1)(qk′ + s + 1)C)
= 2
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + pk′(s + 1)C)
×
r−1∑
t=0
(cosh((t + 1)(l + s + 2 + qk′)C) − cosh((t + 1)(l − s − qk′)C))
our calculation will be done with the help of the following lemma
Lemma 5. Suppose r+1 is a prime number, η an integer, and r + 1 ∤ η, then
r−1∑
t=0
cosh((t + 1)ηC ) = − 1 + cos(ηπ)
2
where C = πi
r+1
So if both l + s + 2 + qk′ and l − s − qk′ are nonzero, by choosing a suﬃciently
large prime number r+1, we have
r−1∑
t=0
(cosh((t + 1)(l + s + 2 + qk′)C) − cosh((t + 1)(l − s − qk′)C) = 0
if l + s + 2 + qk′ = 0, then l − s − qk′ is nonzero, since the sum of the two is
2l + 2, which is always positive and even, in this case
r−1∑
t=0
(cosh((t + 1)(l + s + 2 + qk′)C) − cosh((t + 1)(l − s − qk′)C) = r − (−1) = r + 1
12 QIHOU LIU
if l − s − qk′ = 0, the situation is similar, and we get
r−1∑
t=0
(cosh((t + 1)(l + s + 2 + qk′)C) − cosh((t + 1)(l − s − qk′)C) = −1 − r
in summary,
r−1∑
t=0
(cosh((t + 1)(l + s + 2 + qk′)C) − cosh((t + 1)(l − s − qk′)C))
= −(r + 1){δ(l − s − qk′) − δ(l + s + 2 + qk′)}
so
S = −2
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + pk′(s + 1)C)
× (r + 1){δ(l − s − qk′) − δ(l + s + 2 + qk′)}
Finally from (A) and the above result we have
(−1)l+sgl
σ(q, p; s)(−2(r + 1)) = ( −1)qN (−1)pN × S
= (−1)pN +qN (−2(r + 1))
N∑
k′=−N
k′+N even
exp(qpk ′2C/2 + pk′(s + 1)C)
× {δ(l − s − qk
′
) − δ(l + s + 2 + qk
′
)}
cancel (-2(r+1)) from both sides, we got two polynomials which are equal at
inﬁnitely many points, i.e., the primitive 4(r+1)-th root of unity, henc e the two
polynomials are equal. Note further that gl
σ(q, p; s) = 0 unless l + s + qN is even–
due to the δ function, thus one can check that the sign factor before the sum mation
takes the form as we expected, which is ( −1)pN . And our formula for g,s is proved.
□
