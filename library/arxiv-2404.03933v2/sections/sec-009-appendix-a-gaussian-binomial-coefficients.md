---
doc_id: arxiv-2404.03933v2
doc_title: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY"
section_id: sec-009-appendix-a-gaussian-binomial-coefficients
section_title: "Appendix A. Gaussian binomial coefficients"
section_number: null
pages: 30-31
source_pdf: 2404.03933v2.pdf
source_sha256: 48aff6e97e1f1267
doc_brief: "TENSOR POWERS OF VECTOR REPRESENTATION OF Uq(sl2) AT EVEN ROOTS OF UNITY — We study the decomposition of tensor powers of two dimensional irreducible rep- resentations of quantum sl2 at even roots of"
---
Let v be a formal parameter. The Gaussian binomial coefficient for m∈ Z, r∈ Z≥0, is
defined as follows 
m
r

=
rY
s=1
vm−s+1−v−m+s−1
vs−v−s ∈ Z[v,v−1].
We also define for n≥ 0 the quantum numbers
[n] = vn−v−n
v−v−1 , [n]! =
nY
s=1
vs−v−s
v−v−1 .
If 0≤r≤m, then 
m
r

= [m]!
[r]![m−r]!.
Now let q =e
πi
l , where l is an odd integer ≥ 3, so that q2l = 1 and qk̸= 1 for any 1≤k< 2l.
Proposition A.1. Let m = lm1 +m0, where 0≤ m0≤ l− 1, m1∈ Z, r = r1l +r0, where
0≤r0≤l− 1, r1∈ Z≥0. For the specialization v→q we have

lm1
lr1

= (−1)(m1+1)r1
m1
r1

.
TENSOR POWERS 31

m
r

= (−1)(m0r1−m1r0)+(m1+1)r1
m1
r1

m0
r0

.
This follows from [Lus94], 34.1.2.
Corollary A.2. For an integer p≥ 0 and the specialization v→q we have
[lp]!
([l]!)p =p!(−1)p(p−1)/2.
This follows from Proposition A.1 by induction on p.
Corollary A.3. (a) Letm =m0 +lm1, where 0≤m0≤l− 1, m1∈ Z. Then

m
l

= (−1)m+1m1.
(b) If m,n∈ Z satisfy qm =qn and

m
l

=

n
l

, then m =n.
Proof. If m1≥ 1, then (a) follows from Proposition A.1. If m1 = 0, then 0 ≤ m≤ l− 1 and
m
l

= 0 for an indeterminate v. If m1< 0, then we have

m1l +m0
l

= (−1)l

−m1l−m0 +l− 1
l

= (−1)l(−1)−m1+(l−1−m0)+1(−m1) = (−1)m1+m0+1m1.
Using the assumption that l is odd, we have (−1)m = (−1)lm1+m0 = (−1)m1+m0, and finally

m1l +m0
l

= (−1)m+1m1.
Now consider (b). Ifqm =qn, thenn =m+2lp for somep∈ Z. Then

n
l

=

l(m1 + 2p) +m0
l

=
(−1)m1+2p+m0+1(m1 + 2p) = (−1)m1+m0+1(m1 + 2p), and

m
l

= (−1)m1+m0+1m1, so the
equality

n
l

=

m
l

implies p = 0 and m =n. □
