---
doc_id: arxiv-math-9810105v2
doc_title: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS"
section_id: sec-030-c-since
section_title: "Since"
section_number: C
pages: 30-31
source_pdf: 9810105v2.pdf
source_sha256: 0a432946234949c1
doc_brief: "ON THE DISTRIBUTION OF THE LENGTH OF THE LONGEST INCREASING SUBSEQUENCE OF RANDOM PERMUTATIONS — The authors consider the length, lN, of the length of the longest increasing subsequence of a random"
---
v(3)v−1
p
=

1
−eq[γu+log(
√
1+u2−u)] + eq[γu−u+ 1
6 u3]
0
1

on O ∩Σ(3)
in ,
we have
∥v(3)v−1
p
−I∥L∞(O∩Σ(3)
in ) = O( 1
q2/3 ).
For O ∩Σ(3)
out, we have a similar estimation. On the other hand, for Oc, the error is
exponentially small ; ∥v(3)v−1
p
−I∥L∞(Oc∩Σ(3)) = ∥v(3) −I∥L∞(Oc∩Σ(3)) = O(e−cq).
Now deﬁne R(z) = m(3)m−1
p . The ratio is analytic in C −(Σ(3) ∪∂O) and the
above calculations show that the jump matrix vR = mp−v(3)v−1
p m−1
p−satisﬁes







∥vR −I∥∞≤C(M2)
q2/3
on O ∩Σ(3),
∥vR −I∥∞≤Ce−cq
on Oc ∩Σ(3),
vR = v−1
p
= m−1
p+ = I −mP II,2
1
(t)
λ(z)
+ OM2(
1
λ(z)2 )
on ∂O, as q →∞.
(5.34)
In (5.34), we have used the fact that mP II,2(z, t), and hence mp, is invertible and
bounded for (z, t) ∈C × [0, M2]. (see, (5.30)).
From (5.34) and (5.27), we see that ∥vR−I∥∞= ∥wR∥∞≤C(M2)
q1/3 . In particular,
(I −CwR) is invertible for large q and by (2.9), R is given by
R(z) = I +
1
2πi
Z
Σ(3)∪∂O
µ(s)(vR −I)
s −z
ds
where µ solves (I −CwR)µ = I. As ∥vR −I∥∞≤C(M2)
q1/3 , we have ∥µ −I∥L2 =
OM2(
1
q1/3 ), and also
R22(0) = 1 +
1
2πi
Z
Σ(3)∪∂O
(vR −1)22(s)ds
s + OM2( 1
q2/3 ).
Thus, using ∥vR −I∥∞≤C(M2)
q2/3
in (5.34) for the second equality, and mP II,2
1
=
mP II,1
1
(see (2.20)) for the last equality, we obtain
κ2
q−1 = R22(0)
= 1 +
1
2πi
Z
∂O
(vR −1)22(z)dz
z + OM2( 1
q2/3 )
= 1 −
1
2πi
Z
∂O
mP II,2
1,22 (t)
λ(z)
dz
z + OM2( 1
q2/3 )
= 1 −mP II,2
1,22 (t)
2πi
Z
u(∂O)
1
−i q1/3
24/3 u
du
(−
√
u2 + 1)
+ OM2( 1
q2/3 )
= 1 + i24/3
q1/3 mP II,2
1,22 (t) + OM2( 1
q2/3 )
= 1 + i24/3
q1/3 mP II,1
1,22 (t) + OM2( 1
q2/3 ).
(5.35)
Note that error in (5.35) is uniform for 0 ≤t ≤M2.
We summarize as follows.
LONGEST INCREASING SUBSEQUENCE
31
Lemma 5.1. Let M1 > 0 be a ﬁxed number which is suﬃciently large so that (5.18)
is satisﬁed. Also let M2 > 0 and 0 < δ1 < 1 be ﬁxed numbers. As q →∞, we have
the following results.
