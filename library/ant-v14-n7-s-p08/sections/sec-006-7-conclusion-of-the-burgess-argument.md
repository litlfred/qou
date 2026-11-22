---
doc_id: ant-v14-n7-s-p08
doc_title: "Burgess bounds for short character sums evaluated at forms"
section_id: sec-006-7-conclusion-of-the-burgess-argument
section_title: "Conclusion of the Burgess argument"
section_number: 7
pages: 31-36
source_pdf: ant-v14-n7-s-p08.pdf
source_sha256: 81b8f00fe5fbd0f6
toc_source: inferred
doc_brief: "Burgess bounds for short character sums evaluated at forms — 11 sections: Front matter; Introduction; Method of proof: an overview"
---
We now apply Proposition 6.2 to (5-9) with K = 2H/P, recalling that we are working under the
assumption (5-1) that H1 ≤H2 ≤· · · ≤Hn. (Also recall that Kn ≤Hn < q.) We conclude that
|S(F; N, H)|2r ≪n,r,1,D (log q)2r(n+1)P2nr−1∥H∥−1
∥H∥
Pn
2r
n
X
j=0
q(n+ j)/2eBn,r( j; H/P)−1
= (log q)2r(n+1)∥H∥2r−1P−1qn/2
n
X
j=0
q j/2eBn,r( j; H/P)−1,
(7-1)
in which we recall the deﬁnition of the function eBn,r( · , · ) from (6-4).
At this stage of the Burgess argument in the one-dimensional setting n = 1, one knows that θ0 = 0 and
θ1 = r, so that the sum over j ∈{0, 1} contributes (1 + q1/2(H1/P)−r). To balance this, we would then
choose P to be an integer with
1
2 H1q−1/(2r) ≤P ≤H1q−1/(2r).
(7-2)
Thus when n = 1, we recover
|S(F; N, H)| ≪∥H∥1−1/rq(r+1)/4r2(log q)2,
which agrees with Burgess’s statement (1-1) up to a logarithm. Now for n ≥2, we observe:
Lemma 7.1. For 1 ≤K1 ≤K2 ≤· · · ≤Kn,
n
X
j=0
q j/2eBn,r( j; K)−1 ≪n,r 1
precisely when
q1/2K −θ1
1
≤1.
(7-3)
Under this assumption, the sum over j is dominated by the terms with j = 0, 1.
In particular, this lemma (whose proof we defer to Section 7B) shows that the sum is ≫1 if the
relation (7-3) does not hold; hence it is advantageous to assume (7-3). Under this assumption, we can
dominate the sum by the terms with j = 0, 1 and hence we conclude from (7-1) that
|S(F; N, H)|2r ≪n,r,1,D (log q)2r(n+1)∥H∥2r−1P−1qn/2(1 + q1/2(H1/P)−θ1).
To balance the last two terms within parentheses, we choose P to be an integer with
H1
2q1/(2θ1) ≤P ≤
H1
q1/(2θ1) ,
(7-4)
where we recall that θ1 = ⌊(r −1)/(n −1)⌋if n ≥2. We recall that earlier in (5-2) and (5-8) we had the
requirements that P ≤Hi for all i and Hi P < q for all i. The ﬁrst is clearly true; the second we may
verify as long as we assume Hn H1 < q1+1/(2θ1), as we do in our theorem statement.
1942
Lillian B. Pierce and Junyan Xu
With this choice for P, we have
|S(F; N, H)|2r ≪n,r,1,D ∥H∥2r−1H−1
1 qn/2+1/(2θ1)(log q)2r(n+1),
and hence we conclude that
|S(F; N, H)| ≪n,r,1,D ∥H∥1−1/(2r)H−1/(2r)
1
q(nθ1+1)/4rθ1(log q)n+1.
This proves Theorem 1.1, upon recalling that we have reduced to the setting in which Hmin = H1,
Hmax = Hn, and we have set
2 = θ1 =
j r −1
n−1
k
if n ≥2.
7A. Proof of Corollaries 1.3 and 1.4. Below, we prove Corollaries 1.3 and 1.4 simultaneously; for the
case of Corollary 1.3, simply set c0 = 1 in each instance below. We recall from Theorem 1.1 that
|S(F; N, H)| ≪∥H∥1−1/(2r)H−1/(2r)
min
q(n2+1)/4r2(log q)n+1,
(7-5)
where for every r ≥1 we have set
2 = 2n,r =
j r −1
n−1
k
.
First let us determine for a given n ≥2 the threshold governing for which lengths H the bound (7-5) is
nontrivial, that is o(∥H∥), under the assumption that ∥H∥1/n = qβ and Hmin ≫∥H∥c0/n = qc0β. Then
the bound (7-5) is nontrivial as long as

1 −1
2r

nβ −c0
2r β + n2 + 1
4r2
< nβ,
that is,
β > βn,r :=
n2 + 1
22(n + c0) = 1
2 −
c02 −1
22(n + c0).
(7-6)
Given n ≥2 and 0 < c0 ≤1, as long as we take r sufﬁciently large that 2 = 2n,r > 1/c0, we have βn,r < 1
2.
(In particular if c0 = 1, note that 2n,r > 1 when (r −1)/(n −1) ≥2, or equivalently, r ≥2n −1.) On the
other hand, note that for ﬁxed n ≥2, for all r ≥1
1
2 −
c02 −1
22(n + c0) > 1
2 −
c0
2(n + c0) ≥1
2 −
1
2(n + 1),
for all 0 < c0 ≤1, and this a limitation on the range of β for which the bound is nontrivial.
We now compute that the bound (7-5) is of the form ∥H∥q−δ where
δ = n + c0
2r
β −n2 + 1
4r2 .
(7-7)
Burgess bounds for short character sums evaluated at forms
1943
We make the approximation that 2 = (r −1)/(n −1), which is an identity when n = 2, and will not be
far from the truth, when we later take r very large. Then we compute that after this approximation, δ can
be represented as a function of r by
fa,b,c(r) = a
r −br −c
r(r −1),
where
a = (n + c0)β
2
,
b = n
4,
c = 1
4.
As a function of r, this attains a maximum at
r = (a −b)−1{(a −c) ±
p
(a −c)2 −(a −c)(a −b)}.
(7-8)
To have r > 0 we must have (a −b) > 0, that is
β > βn,c0 :=
n
2(n + c0) = 1
2 −
c0
2(n + c0),
(7-9)
agreeing with our previous observation. Thus from now on we assume β = βn,c0 + κ for some small κ,
and we will study how δ = δn(κ) behaves as κ →0. From (7-7) with β = βn,c0 + κ (and without
approximating 2), we see that for any r,
δ = δn(κ) := n + c0
2r
κ −
1
4r2.
To maximize this, according to (7-8), as κ →0 we will take r to be the integer closest to
n −1
κ(n + c0).
For an approximation, we set r = (n −1)/(κ(n + c0)) in the expression for δn(κ), and using the
approximation 2 ≈r/(n −1) (which is reasonable as κ →0 since then r →∞), we see that
δn(κ) ≈(n + c0)2
4(n −1) κ2
(7-10)
as κ →0. Here we use ≈because we have made two types of approximations: ﬁrst, we used approximations
of the value of 2 and r for simplicity, which introduced errors that become vanishing small, relative to
the true size of δn(κ), as κ →0. Second, to simplify certain expressions, we used the fact that we are in
the limiting case κ →0.
Alternatively, we can encapsulate the restriction (7-9) by recording it as the restriction
∥H∥Hmin ≫∥H∥1+c0/n ≫(qnβ)1+c0/n,
where β = βn,c0 + κ for any small κ > 0. Therefore we will obtain a nontrivial bound as long as
∥H∥Hmin ≫qn/2+κ for any small κ > 0.
1944
Lillian B. Pierce and Junyan Xu
7B. Proofs of technical lemmas.
Proof of Lemma 5.2. This argument originates in [Heath-Brown 2013, §4] and is similar but not identical
to lemmas in [Heath-Brown and Pierce 2015; Pierce 2016]; for completeness we provide an argument.
The ﬁrst property in Lemma 5.2 is a direct result of the deﬁnition of A(m). Since each A(m) is a
nonnegative integer,
X
m
A(m) ≤
X
m
A(m)2,
and it sufﬁces to prove the third property. We write
X
m
A(m)2 =
X
m
#

p, p′, a, a′ : mi ≤Ni −aiq
p
< mi + Hi/P, mi ≤Ni −a′
iq
p′
< mi + Hi/P

≪

n
Y
i=1
Hi
P

#

p, p′, a, a′ : 0 ≤

Ni −aiq
p
−Ni −a′
iq
p′

 ≤Hi/P

= ∥H∥P−n X
p,p′∈P
M(p, p′),
(7-11)
where
M(p, p′) = #

a, a′, 0 ≤ai < p, 0 ≤a′
i < p′ : 0 ≤

Ni −aiq
p
−Ni −a′
iq
p′

 ≤Hi/P

.
First consider p = p′. Then
M(p, p) ≤#

a, a′ : |(Ni −aiq) −(Ni −a′
iq)| ≤p(Hi/P) ≤2Hi, i = 1, . . . , n
	
≤#

a, a′ : |ai −a′
i| ≤2Hi/q < 2, i = 1, . . . , n
	
.
Here we have used Hi < q. This shows that once a is chosen, there are at most 3n choices for a′, so that
M(p, p) ≪Pn and hence P
p=p′∈P M(p, p′) ≪Pn+1, which sufﬁces for our desired bound for (7-11).
Next, consider the case p̸ = p′. For each i = 1, . . . , n we choose (by Bertrand’s postulate) a prime li
such that
q
Hi
< li ≤2q
Hi
.
(Here we use the assumption that Hi < q for each i.) For each i, let Mi = [Nili/q] or Mi = [Nili/q]+ 1,
so that li ∤Mi. Then |Nili/q −Mi| ≤1 implies that |Ni −qMi/li| ≤q/li, so that
M(p, p′) ≪#

a, a′ :

qMi/li −aiq
p
−qMi/li −a′
iq
p′

 ≤Hi
P + q
li p + q
li p′ , i = 1, . . . , n

≪#

a, a′ : |(p′ −p)Mi −(ai p′ −a′
i p)li| ≤12P, i = 1, . . . , n
	
.
Burgess bounds for short character sums evaluated at forms
1945
Given p, p′ and an integer δ, for each ﬁxed index i there is at most one way to choose ai, a′
i with
0 ≤ai < p, 0 ≤a′
i < p′ such that ai p′ −a′
i p = δ. Thus
X
p̸=p′∈P
M(p, p′)≪#

p̸ = p′ ∈P, u =(u1, . . . , un), |ui|≤12P : Mi(p′−p)≡ui (modli), i =1, . . . , n
	
.
Now we use the fact that li ∤Mi. Thus for a ﬁxed i, the condition Mi(p′ −p) ≡ui (mod li) determines
p′ −p uniquely modulo li, and hence uniquely in Z, as long as P < li, which is guaranteed by the
assumption P < q/Hi, that is P Hi < q. In particular, there is at most one value for the difference p′ −p
that will satisfy all n conditions. So we may choose p freely and then p′ is determined. As a result, after
counting up the possible choices for u, we conclude that
X
p̸=p′∈P
M(p, p′) ≪Pn+1.
Applying this in (7-11), we conclude that
X
m
A(m)2 ≪∥H∥P.
□
Proof of Lemma 6.4. We may restrict our attention to permutations that map {1, . . . , M} to itself, or
equivalently, we may suppose going forward that M = n. For indeed, any indices i that occur in the sums
such that i ≤M but σ(i) > M, clearly contribute no more to the left-hand side than to the right-hand side,
since ti ≤tσ(i).
Now let σ be the permutation that minimizes
a1tσ(1) + · · · + antσ(n);
(7-12)
if there is more than one such permutation, we choose σ to be the one with the greatest number of
ﬁxed points. We will show that σ is the identity. For suppose otherwise, and let i be the smallest index
such that σ(i)̸ = i. Then σ(i) > i and hence tσ(i) ≥ti. Furthermore, denoting by k the index such that
σ(k) = i, we must also have that k > i and hence ak ≤ai. We then see that (tσ(i) −ti)(ai −ak) ≥0, or
equivalently, tσ(i)ai + tiak ≥tiai + tσ(i)ak. Deﬁne a new permutation σ ′ by σ ′(u) = u for u = 1, . . . , i,
σ ′(k) = σ(i), and σ ′(u) = σ(u) for all the remaining u ∈{i + 1, . . . , n} \ {k}. Then we see that
tσ(i)ai + tσ(k)ak ≥tσ ′(i)ai + tσ ′(k)ak so that (7-12) does not increase in value if we replace σ by σ ′, and σ ′
must also be a minimizer. Yet σ ′ has one more ﬁxed point than σ, which is a contradiction. We conclude
that σ is the identity.
□
Proof of Lemma 7.1. By the deﬁnition of the θ j, the sum over j = 0, 1, . . . , n −1 takes the form
1 +
n−1
X
j=1
q j/2K
−θ j
1
= 1 +
n−2
X
j=1
q j/2K −jθ1
1
+ q(n−1)/2K −(r−1)
1
≤1 +
n−1
X
j=1
(q1/2K −θ1
1
) j
(7-13)
in which θ1 = ⌊(r −1)/(n −1)⌋. Here we have used the fact that for j = n −1, θn−1 = r −1 ≥
(n −1)⌊(r −1)/(n −1)⌋= (n −1)θ1. Now we see from the right-most expression that under the
1946
Lillian B. Pierce and Junyan Xu
assumption (7-3), all terms j ≥2 are dominated by j = 0, 1. On the other hand, we see from the middle
expression that if (7-3) does not hold, then that expression is ≫1, as claimed.
It remains to examine the terms with j = n, which we divide into the even and odd cases. For n ≥2
even, the j = n term is
qn/2(K1 · · · Kn/2)−(2r−1) ≤qn/2K −(2r−1)n/2
1
≤(q1/2K −θ1
1
)n,
where we have used the ordering K1 ≤K2 ≤· · ·≤Kn and the fact that (2r−1)(n/2)≥n(r−1)/(n−1)≥nθ1
holds when n ≥2. Thus the above expression is ≪1 under the assumption (7-3).
For n ≥3 odd, the j = n term is
qn/2(K1 · · · K(n−1)/2)−(2r−1)K −r
(n+1)/2 ≤qn/2K −{(2r−1)(n−1)/2+r}
1
≤(q1/2K −θ1
1
)n,
upon verifying that n ≥2 sufﬁces to show that (2r −1)(n −1)/2 +r ≥n(r −1)/(n −1) ≥nθ1. Under
the assumption (7-3) we see that the j = n term is also ≪1. This concludes the proof of Lemma 7.1. □
