---
doc_id: ant-v14-n7-s-p08
doc_title: "Burgess bounds for short character sums evaluated at forms"
section_id: sec-005-6-stratiﬁcation-and-a-menshovrademacher-argument
section_title: "Stratiﬁcation and a Menshov–Rademacher argument"
section_number: 6
pages: 25-31
source_pdf: ant-v14-n7-s-p08.pdf
source_sha256: 81b8f00fe5fbd0f6
toc_source: inferred
doc_brief: "Burgess bounds for short character sums evaluated at forms — 11 sections: Front matter; Introduction; Method of proof: an overview"
---
6A. Application of the stratiﬁcation for character sums. We now come to a critical novel step, which
is to estimate how often we obtain a certain quality of upper bound for the complete character sum
X
m (mod q)
χ(F{x}(m)).
For this, we call upon the stratiﬁcation of complete character sums stated in Theorem 4.4. Let us suppose
that k1 ≤. . . ≤kn ≤q. For each 1 ≤j ≤n, deﬁne
Y j :=

{x} ∈(0, k]2r :

X
m (mod q)
χ(F{x}(m))

 > Cq(n+ j−1)/2

,
in which C = C(n,r, D) is the constant provided by Theorem 4.4. Then by Theorem 4.4, we have
(0, k]2r =: Y0 ⊃Y1 ⊃Y2 ⊃· · · ⊃Yn ⊃Yn+1 := ∅, and #Y j ≤C′′∥k∥2r Bn,r( j; k)−1. Upon employing the
decomposition (0, k]2r = `n
j=0 Y j \ Y j+1 in (5-10) we have
X
m (mod q)
|S(F; m, k)|2r ≤
n
X
j=0
X
{x}∈Y j\Y j+1

X
m (mod q)
χ(F{x}(m))

(6-1)
≤
n
X
j=0
(#Y j)Cq(n+( j+1)−1)/2
≤C · C′′∥k∥2r
n
X
j=0
q(n+ j)/2Bn,r( j; k)−1.
To summarize, we have proved:
Lemma 6.1. Fix n,r, D, 1 ≥1, a prime q, and a multiplicative Dirichlet character χ of order 1
modulo q. Then for every form F ∈Z[X1, . . . , Xn] of degree D such that its reduction modulo q is
(1, q)-admissible, the following holds. For every k = (k1, . . . , kn) with 1 ≤k1 ≤k2 ≤· · · ≤kn ≤q, then
X
m (mod q)
|S(F; m, k)|2r ≪n,r,D,1 ∥k∥2r
n
X
j=0
q(n+ j)/2Bn,r( j; k)−1,
(6-2)
with Bn,r( j; k) as deﬁned in (4-5), and with the implicit constant dependent on n,r, D, 1 but independent
of q, χ, F, k.
However recall that the actual quantity we must bound in (5-9) is a moment of |S(F; m, k)| that
includes a maximum over k ≤2H/P. To do so, we will employ a Menshov–Rademacher argument.
6B. A Menshov–Rademacher argument with permutations. The Menshov–Rademacher argument
[Menshov 1923; Rademacher 1922] may be employed in a wide variety of circumstances; in general
it allows one to replace a supremum of a function | f (u j)| over an index set of size U by a sum of
differences | f (u j)−f (u j−1)| over an index set of size O(log U). In our present setting, these differences
1936
Lillian B. Pierce and Junyan Xu
are differences of partial sums over a box, which are themselves partial sums of the same kind, so that the
Menshov–Rademacher device is a useful tool.
However a typical Menshov–Rademacher argument would not immediately apply in our case, since we
cannot save a power of ∥k∥but typically only a power of kmin, the shortest side of the box. We see this
phenomenon is already present in Lemma 6.1, since we have assumed an ordering k1 ≤k2 ≤· · ·≤kn for the
side-lengths of the box. Even if we assume in the beginning that we have such an ordering, certain internal
steps in the Menshov–Rademacher argument do not preserve such an ordering, and thus arranging the argu-
ment so that we may apply Lemma 6.1 will require delicate considerations of permutations of the variables.
Our main result in this section is the following:
Proposition 6.2. If 1 ≤K1 ≤K2 ≤· · · ≤Kn ≤q, then
X
m
|mi|≤2q
max
k≤K|S(F; m, k)|2r ≪n,r,D,1 ∥K∥2r(log Kn)2nr
n
X
j=0
q(n+ j)/2eBn,r( j; K)−1
(6-3)
with the implicit constant dependent on n,r, D, 1 but independent of q, χ, K, and with
eBn,r( j; K) =



1
if j = 0,
K
θ j
1
if j = 1, . . . , n −1,
(K1 · · · Kn/2)(2r−1)
if j = n, n even,
(K1 · · · K(n−1)/2)(2r−1)(K(n+1)/2)r
if j = n, n odd.
(6-4)
Note that eBn,r(n; K)−1 loses one power in decay compared to Bn,r(n; K)−1. In contrast, in the one-
dimensional case, no decay is lost when passing from the nonmaximal estimate to the maximal estimate;
this minor loss will not affect our ﬁnal outcome, and we explain why it arises below.
6C. A dyadic decomposition. It sufﬁces to prove Proposition 6.2 for K = (K1, . . . , Kn) where each Ki
is a power of 2, say Ki = 2ti, in which case we naturally have t1 ≤t2 ≤· · · ≤tn, under the hypotheses of the
proposition. We ﬁx m and suppose that S(F; m, k) assumes its maximum for k ≤K at k = (k1, . . . , kn),
and for each i we decompose
ki =
X
δi∈Di
2ti−δi,
where Di is a set of distinct nonnegative integers δi ≤ti. Let δ = (δ1, . . . , δn) denote a tuple with δi ∈Di
for each i. Let t = (t1, . . . , tn) and deﬁne the notation 2t−δ = (2t1−δ1, . . . , 2tn−δn). Given a tuple v, we
deﬁne 2t−δ ◦v = (2t1−δ1v1, . . . , 2tn−δnvn). Furthermore let Vm,δ be an n-tuple deﬁned such that the i-th
entry is (Vm,δ)i = 2ti−δivm,δ,i, where
vm,δ,i =
X
ei∈Di,ei<δi
2δi−ei < 2δi.
Then we may express
S(F; m, k) =
X
δ,δi∈Di
S(F; m + Vm,δ, 2t−δ).
Burgess bounds for short character sums evaluated at forms
1937
After taking absolute values, we can obtain an upper bound by increasing the sum to run over all tuples δ
with δi ≤ti. We get
|S(F; m, k)| ≤
X
δ
0≤δi≤ti
|S(F; m + Vm,δ, 2t−δ)|.
Then by Hölder’s inequality,
|S(F; m, k)|2r ≤

n
Y
i=1
(ti + 1)
2r−1 X
δ
0≤δi≤ti
X
v
0≤vi<2δi
|S(F; m + 2t−δ ◦v, 2t−δ)|2r,
where we have possibly enlarged the right-hand side by summing over all possible values for vm,δ,i up to 2δi.
Recalling that for each m we chose k above to be the length at which the maximum is attained, we then have
X
m
|mi|≤2q
max
k≤K |S(F; m, k)|2r ≤T 2r−1
X
δ
0≤δi≤ti
X
v
0≤vi<2δi
X
m
|mi|≤2q
|S(F; m + 2t−δ ◦v, 2t−δ)|2r
≪T 2r−1 X
δ
0≤δi≤ti
∥2δ∥
X
m (mod q)
|S(F; m, 2t−δ)|2r,
where T := Qn
i=1(ti + 1). Now we perform the key step that accommodates the fact that we only achieve
a saving in the smallest direction of the box.
6D. Application of the nonmaximal upper bound. We would like to apply Lemma 6.1 to the innermost
sums over m. Fix δ (with 0≤δi ≤ti for each i). Notice that we may not have t1−δ1 ≤t2−δ2 ≤· · ·≤tn−δn
even though t1 ≤t2 ≤· · · ≤tn, so we may need to reorder t −δ before applying Lemma 6.1. Let σ be a
permutation of {1, 2, . . . , n} (depending on δ) such that
tσ(1) −δσ(1) ≤tσ(2) −δσ(2) ≤· · · ≤tσ(n) −δσ(n).
(6-5)
Given an n-tuple x, let xσ = (xσ(1), xσ(2), . . . , xσ(n)), and 2tσ −δσ = (2tσ(1)−δσ(1), . . . , 2tσ(n)−δσ(n)). Recall
the discussion on permutations of variables in Section 3D; for any permutation π of {1, . . . , n} deﬁne the
form Fπ(X) by setting Fπ(X1, . . . , Xn) = F(Xπ(1), . . . , Xπ(n)).
Letting σ −1 be the permutation inverse of σ, then
S(F; m, 2t−δ) =
X
x∈(m,m+2t−δ)
χ(F(x)) =
X
xσ ∈(mσ ,mσ +2tσ −δσ )
χ(Fσ −1(xσ)) = S(Fσ −1; mσ, 2tσ −δσ ).
Note that mσ ranges over all n-tuples with coordinates modulo q as m does, and that the last argument in
S(Fσ −1; mσ, 2tσ −δσ ) satisﬁes the requirement (6-5) so that we may apply Lemma 6.1 with n,r, D, 1, q, χ
as before but now to the form Fσ −1; here we use the uniformity of Lemma 6.1 with respect to the form.
(We recall from Lemma 3.5 that the reduction modulo q of Fσ −1 is (1, q)-admissible if and only if F is.)
1938
Lillian B. Pierce and Junyan Xu
We may conclude (using the fact that ∥2tσ −δσ ∥= ∥2t−δ∥= ∥2t∥· ∥2δ∥−1) that
X
m
|mi|≤2q
max
k≤K |S(F; m, k)|2r ≪n,r,D,1 T 2r−1 X
δ
0≤δi≤ti
∥2δ∥∥2tσ −δσ ∥2r
n
X
j=0
q(n+ j)/2Bn,r( j; 2tσ −δσ )−1
= T 2r−1 X
δ
0≤δi≤ti
∥2t∥2r∥2δ∥−(2r−1)
n
X
j=0
q(n+ j)/2Bn,r( j; 2tσ −δσ )−1
= T 2r−1∥2t∥2r
n
X
j=0
q(n+ j)/2 X
δ
0≤δi≤ti
∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1
≤T 2r∥K∥2r
n
X
j=0
q(n+ j)/2 max
δ
0≤δi≤ti

∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1	
.
(6-6)
Here we recall that ∥2t∥= ∥K∥. Note that in the case of dimension n = 1 (and θ1 = r), the sum over j is
comprised of the two terms
qn/22−δ(2r−1) + qn2−δ(2r−1)(2t−δ)−r ≤qn/2 + qn2−rt = qn/2 + qnK −r,
familiar from the classical 1-dimensional Burgess argument.
Now in general for n ≥2 we must reinterpret Bn,r( j; 2tσ −δσ )−1 in terms of the coordinates of K = 2t,
in which we recall that t1 ≤t2 ≤· · · ≤tn; this argument is more complicated, and in particular for j = n
we will get a positive power of 2δ we cannot ignore as in the case of n = 1 (e.g., compare to the top line
of [Heath-Brown 2013, p. 204]). We summarize the necessary result:
Lemma 6.3. For K = 2t with t1 ≤· · · ≤tn, for each δ ≤t, let σ be a permutation of the indices {1, . . . , n}
such that tσ(1) −δσ(1) ≤· · · ≤tσ(n) −δσ(n). Then
∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1 ≤



1
if j = 0,
K
−θ j
1
if j = 1, . . . , n −1,
(K1 · · · Kn/2)−(2r−1)
if j = n, n even,
(K1 · · · K(n−1)/2)−(2r−1)K −r
(n+1)/2
if j = n, n odd.
Once we apply this lemma to (6-6), upon noting that T 2r ≤22nr(log2 Kn)2nr ≪(log Kn)2nr, we have
proved Proposition 6.2.
6E. Proof of Lemma 6.3: rearrangement. We recall the deﬁnition of Bn,r( j; k) in (4-5) so that for a
tuple k=(k1, . . . , kn) with k1 ≤k2 ≤· · ·≤kn, Bn,r( j; k)=1 for j =0, Bn,r( j; k)=k
θ j
1 for j =1, . . . , n−1,
and for j = n we have Bn,r( j; k) = (k1 · · · kn/2)2r if n is even and Bn,r( j; k) = (k1 · · · k(n−1)/2)2rkr
(n+1)/2
if n is odd.
We may quickly dispatch the case j = 0, in which case
∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1 = ∥2δ∥−(2r−1) ≤1.
Burgess bounds for short character sums evaluated at forms
1939
For the remaining cases of j ≥1, it is helpful to invert, and take the logarithm, and prove for ﬁxed δ and
ﬁxed j a lower bound for the quantity
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

.
First we consider the case of 1 ≤j ≤n −1; for each of these j (using the fact that P
i δσ(i) = P
i δi),
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

= (2r −1)

n
X
i=1
δσ(i)

+ θ j(tσ(1) −δσ(1))
= θ jtσ(1) + (2r −1 −θ j)δσ(1) + (2r −1)
n
X
i=2
δσ(i) ≥θ jtσ(1).
Here we used that for 1 ≤j ≤n −1 we have θ j ≤r −1, and moreover δσ(i) ≥0 for all 1 ≤i ≤n. Thus
∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1 ≤2−θ jtσ(1) ≤2−θ jt1 = K
−θ j
1
,
upon recalling that t1 ≤t2 ≤· · · ≤tn.
Now we turn to the more complicated case of j = n. First we assume that n is even. Now we have
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

= (2r −1)
n
X
i=1
δσ(i) + 2r
n/2
X
i=1
(tσ(i) −δσ(i)).
It is convenient to set temporarily for each i = 1, . . . , n the parameter 2n,i = 2r if 1 ≤i ≤n/2 and
2n,i = 0 if n/2 < i ≤n. Then upon recalling that each δi ≤ti, we have
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

= (2r −1)
n
X
i=1
δσ(i) +
n
X
i=1
2n,i(tσ(i) −δσ(i)) =
n
X
i=1
2n,itσ(i) +
n
X
i=1
(2r −1 −2n,i)δσ(i)
≥
n
X
i=1
2n,itσ(i) +
n
X
i=1
2r−1−2n,i<0
(2r −1 −2n,i)tσ(i) +
n
X
i=1
2r−1−2n,i≥0
(2r −1 −2n,i) · 0
=
n
X
i=1
2r−1−2n,i<0
(2r −1)tσ(i) +
n
X
i=1
2r−1−2n,i≥0
2n,itσ(i).
(6-7)
(Here in the inequality, equality can occur for those δ such that δi = ti for all 1 ≤i ≤n/2 and δi = 0
for n/2 < i ≤n. The inequality is where we see that if 2n,i = 2r, we must replace δσ(i) by tσ(i) rather
than by 0; this is why in the ﬁnal statement of the inequality we lose slightly in the maximal moment,
compared to the nonmaximal moment. This effect is not possible in dimension n = 1.) Now by the
deﬁnition of 2n,i, the ﬁrst sum is over 1 ≤i ≤n/2; the second sum is over n/2 < i ≤n, in which range
2n,i = 0 so that the second sum is vacuous. Now we use the following simple observation.
1940
Lillian B. Pierce and Junyan Xu
Lemma 6.4 (rearrangement inequality). Let t1 ≤t2 ≤· · · ≤tn be a ﬁxed nondecreasing sequence of real
numbers and a1 ≥· · · ≥an a ﬁxed nonincreasing sequence of real numbers. Then for any permutation σ
on {1, . . . , n}, and for any 1 ≤M ≤n,
M
X
i=1
aiti ≤
M
X
i=1
aitσ(i).
(6-8)
This is a variant of a standard rearrangement inequality; for completeness we give a brief proof in
Section 7B. Applying this observation in (6-7) with M = n/2, we have shown that
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

≥(2r −1)
n/2
X
i=1
ti,
so that in the case of j = n even,
∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1 ≤(2t1 · · · 2tn/2)−(2r−1) = (K1 · · · Kn/2)−(2r−1).
The argument is similar for j = n with n odd, and we only specify the necessary changes, starting with
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

= (2r −1)
n
X
i=1
δσ(i) +2r
(n−1)/2
X
i=1
(tσ(i) −δσ(i))+r(tσ((n+1)/2) −δσ((n+1)/2)).
It is convenient to set temporarily for each i = 1, . . . , n the parameter 2n,i = 2r if 1 ≤i ≤(n −1)/2,
2n,(n+1)/2 = r and 2n,i = 0 if (n+1)/2 < i ≤n. With this notation, the argument then proceeds as before,
until we reach the statement of (6-7), which now holds with this new deﬁnition of 2n,i. Now the ﬁrst sum
on the right-hand side of (6-7) is over 1 ≤i ≤(n −1)/2, while the second sum on the right-hand side is
over i ≥(n+1)/2, and has its only nonzero contribution coming from i = (n+1)/2. We may conclude that
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

≥
(n−1)/2
X
i=1
(2r −1)tσ(i) +rtσ((n+1)/2).
We now apply (6-8) from Lemma 6.4 to conclude that
log2
 ∥2δ∥(2r−1)Bn,r( j; 2tσ −δσ )

≥
(n−1)/2
X
i=1
(2r −1)ti +rt(n+1)/2,
or equivalently,
∥2δ∥−(2r−1)Bn,r( j; 2tσ −δσ )−1 ≤(2t1 · · · 2t(n−1)/2)−(2r−1)(2t(n+1)/2)−r = (K1 · · · K(n−1)/2)−(2r−1)K −r
(n+1)/2.
This completes the proof of Lemma 6.3.
Burgess bounds for short character sums evaluated at forms
1941
