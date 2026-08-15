---
doc_id: arxiv-2412.04241v2
doc_title: "THE HABIRO RING OF A NUMBER FIELD"
section_id: sec-011-21-the-infinite-pochhammer-symbol
section_title: "The infinite Pochhammer symbol"
section_number: 2.1
pages: 18-20
source_pdf: 2412.04241v2.pdf
source_sha256: 308d1dd1c42bd979
doc_brief: "THE HABIRO RING OF A NUMBER FIELD — We introduce the Habiro ring of a number field K and modules over it graded by K3(K)."
---
Pochhammer symbol (t;q)∞ = Q
n≥0(1−qnt). In this section we collect some elementary,
although remarkable, properties of it. There are two well-known complementary expansions
of the logarithm of (t;q)∞
log(t;q)∞ = −
X
ℓ≥1
tℓ
ℓ(1−qℓ) (46)
=
X
k≥0
Bk
k! Li2−k(t) log(1 +x)k−1, (47)
where Lin(t) =P
k≥1
tk
kn is thenth polylogarithm and Bk =Bk(0) are the Bernoulli numbers
given by the generating series (60) with B0 = 1, B1 =−1/2, etc.
These two expansions in turn imply two complementary views of the Dwork-type differ-
ence, namely for every prime p, and for q = 1 +x, we have
log(tp;qp)∞−p log(t;q)∞ = p
X
ℓ≥1, p∤ℓ
tℓ
ℓ(1−qℓ) (48)
= −p
X
k≥0
Bk
k! Li(p)
2−k(t) log(1 +x)k−1, (49)
where
Li(p)
n (t) = Li n(t)− 1
pn Lin(tp) =
X
k≥1, p∤k
tk
kn (50)
is the p-version of the polylogarithm [11, Prop.6.2].
On the one hand, (48) implies that the coefficient of xk−1 in the Dwork-type difference
is in pZ(p)[ [t] ], and on the other hand, (49) implies that it is a Q-linear combination of the
series Li(p)
2−s(t) for s = 0,...,k . But in fact, more is true. In [11, Prop.6.2] Coleman proves
(working with the variable 1/t) that Li (p)
n (t)∈ Z(p)[ [t] ] is convergent for|t/(1−t)|<p (p−1)−1
and consequently lies in the ring Z[ t
1−t]∧
p of all series in Zp[ [t] ] that converge for|t/(1−t)|≤ 1.
In the present paper, we will only use a weaker statement with an elementary proof.
THE HABIRO RING OF A NUMBER FIELD 19
Lemma 2.1. For every integern and prime number p we have
Li(p)
n (t) ∈ Z[t, 1
1−t]∧
p . (51)
Proof. Forr = 1,...,p − 1 we have
1
r +pk = r−1
∞X
ℓ=0
(−1)ℓ(r−1pk)ℓ ∈ Zp. (52)
This implies that for all positive integers n and N we have
1
(r +pk)n ≡ 1
(r +p(k +pN))n (mod pN). (53)
Using equation (50) and separating the summation over the positive integers prime to p into
congruence classes modulo pN, we obtain that
Li(p)
n (t) ≡
p−1X
r=1
pN−1X
k=0
∞X
ℓ=0
tr+pk+pNℓ
(r +pk)n = 1
1−tpN
p−1X
r=1
pN−1X
k=0
tr+pk
(r +pk)n (mod pN). (54)
Moreover, 1
1−tpN ∈ Z[t, 1
1−t]∧
p , which completes the proof. □
Proposition 2.2. (a) For every prime p we have
log(tp;qp)∞−p log(t;q)∞ ∈ p
x Z[t, 1
1−t]∧
p [ [x] ], q = 1 + x. (55)
(b) Fix a root of unity ζ∈ Cp ∖{1} of order not a power of p. The function
log(ζp;qp)∞−p log(ζ;q)∞ ∈ pLi(p)
2 (ζ)
x +pZ(p)[ζ][ [x] ], q = 1 + x (56)
is meromorphic on the disc |x|< 1 with a simple pole at x = 0 and the residue as given.
Proof. Equation (55) follows from (48), Lemma 2.1, and the elementary identity
Z[t, 1
1−t]∧
p [ 1
p]∩ Z(p)[ [t] ]⊆ Z[t, 1
1−t]∧
p . (57)
Part (b) follows trivially from part (a) by applying the natural map
Z[t, 1
1−t]∧
p→ Zp[ζ], t 7→ζ, (58)
which is compatible with the Frobenius endomorphism t7→tp. □
The power series expansion in equation (47) was centred about q = 1, but it has an
extension at all roots of unity given by
log(t;q)∞ =
m−1X
j=0
log(qjt;qm)∞ =
m−1X
j=0
∞X
k=0
Bk(j/m)mk−1
k! Li2−k(ζj
mt) log(1+x/ζm)k−1, (59)
whereq =ζm +x and the Bernoulli polynomials Bk(y)∈ Q[y] are defined by the generating
series
xexy
ex− 1 =
∞X
k=0
Bk(y)
k! xk (60)
with B0(y) = 1 and B1(y) =y− 1/2.
20 STA VROS GAROUF ALIDIS, PETER SCHOLZE, CAMPBELL WHEELER, AND DON ZAGIER
