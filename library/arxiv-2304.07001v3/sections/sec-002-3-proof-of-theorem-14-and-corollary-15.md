---
doc_id: arxiv-2304.07001v3
doc_title: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES"
section_id: sec-002-3-proof-of-theorem-14-and-corollary-15
section_title: "Proof of Theorem 1.4 and Corollary 1.5"
section_number: 3
pages: 13-17
source_pdf: 2304.07001v3.pdf
source_sha256: b6c0d7f50b6407f1
doc_brief: "RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES — We prove resurgence properties for the Borel transform of a f ormal power series associated to elements in the Habiro ring that come from radi al"
---
In order to prove Theorem 1.4 and Corollary 1.5, we require some general preliminaries. Recall
the periodic function χ(n,m)
s,t (k) given by ( 1.18).
Lemma 3.1. For all k∈ Z, 1≤ m≤ t− 1 and 1≤ n≤ s− 1, we have
χ(n,m)
s,t (k) = χ(s−n,t−m)
s,t (k).
Proof. By replacing n→ s− n and m→ t− m, we see that
±((s− n)t− (t− m)s) =±(ms− nt) =∓(nt− ms) ,
±((s− n)t + (t− m)s) =±(2st− ms− nt)≡∓ (nt + ms) (mod 2 st) , (3.1)
and thus the result follows from ( 3.1). □
In view of Lemma 3.1, the map
(n, m)− →
{
(n, m) if 1 ≤ n≤ s−1
2 , 1≤ m≤ t−1
2 ,
(s− n, t− m) otherwise . (3.2)
is a bijection between the pairs deﬁned by D1(s, t) and D2(s, t) in ( 1.19) and ( 1.20), respectively.
Lemma 3.2. Let s and t be coprime positive integers and D(s, t) be the set given by ( 1.21).
Then the integers in the set
S ={±(nt± ms) : ( n, m)∈ D(s, t)}
are distinct and thus |S| = 2(s− 1)(t− 1).
14 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
Proof. We assume that s and t are coprime odd integers. A similar argument applies when s
and t are of opposite parities. Let us consider two integers of the forms n1t + m1s and n2t + m2s
where− s−1
2 ≤ n1, n2≤ s−1
2 and−(t− 1)≤ m1, m2≤ t− 1. Then
n1t + m1s = n2t + m2s ⇐⇒ (n1− n2)t + (m1− m2)s = 0. (3.3)
Since s and t are coprime, ( 3.3) implies that s| (n1− n2), which yields |n1− n2|≥ s. On the
other hand, since − s−1
2 ≤ n1, n2≤ s−1
2 , we obtain −(s− 1)≤ n1− n2≤ s− 1, or equivalently,
|n1− n2| ≤s− 1, a contradiction. This shows that n1 = n2 and thus ( 3.3) implies that
m1 = m2. □
Deﬁne
Sn′, m′
n, m =
√
8
st (−1)nm′+mn′+1 sin
(nn′t
s π
)
sin
(mm′s
t π
)
.
Proposition 3.3. For all k∈ Z, and (n, m)∈ D(s, t), we have
˜χ(n,m)
s,t (k) =−
√
st
8
∑
(n′, m′)∈D(s,t)
Sn′, m′
n, m χ(n′, m′)
s,t (k). (3.4)
Proof. We assume that nt− ms > 0. A similar argument holds for nt− ms < 0. By ( 1.12), we
have
˜χ(n,m)
s,t (k) = (−1)k sin
((nt + ms−| nt− ms|)kπ
2st
)
sin
((2st−| nt− ms|− (nt + ms))kπ
2st
)
= (−1)k sin
(mkπ
t
)
sin
((s− n)kπ
s
)
=− sin
(mkπ
t
)
sin
(nkπ
s
)
. (3.5)
Clearly, the support of ˜χ(n,m)
s,t is contained within the set of integers k such that s ∤ k and t ∤ k.
By inclusion-exclusion, the total number of integers betwe en 0 and 2 st− 1 which are either
multiples of s or t is 2s + 2t− 2. By Lemma 3.2, the number of distinct integers k =±(m′s± n′t)
between 0 and 2 st− 1, where ( n′, m′)∈ D(s, t) is 2( s− 1)(t− 1). Since ˜χ(n,m)
s,t has period 2 st,
this implies that the support of ˜ χ(n,m)
s,t is contained in the following set of distinct integers
T ={±(m′s± n′t) (mod 2 st) : ( n′, m′)∈ D(s, t)}. (3.6)
Thus it suﬃces to prove ( 3.4) for integers in T. From ( 3.5), we have
˜χ(n,m)
s,t (±(m′s± n′t)) =− sin
(±m(m′s± n′t)π
t
)
sin
(±n(m′s± n′t)π
s
)
=− sin
(
±mn′π + mm′s
t π
)
sin
(
nm′π± nn′t
s π
)
=±(−1)mn′+nm′+1 sin
(mm′s
t π
)
sin
(nn′t
s π
)
= (−1)mn′+nm′
sin
(mm′s
t π
)
sin
(nn′t
s π
)
χ(n′,m′)
s,t (±(m′s± n′t)) (3.7)
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 15
where in the last step we use that the sign ± depends on the sign of ( m′s± n′t), and it is
−χ(n′,m′)
s,t (±(m′s± n′t)). Since the integers in T are distinct, then from ( 3.7) we ﬁnd:
˜χ(n,m)
s,t (±(m′s± n′t)) =−
√
st
8
∑
(n′′, m′′)∈D(s,t)
Sn′′, m′′
n, m χ(n′′, m′′)
s,t (±(m′s± n′t)). (3.8)
It follows from ( 3.8) that ( 3.4) is true for integers k given by ( 3.6), which are non-multiples of s
or t and between 0 and 2 st− 1. It remains to show that ( 3.4) remains true when k is a multiple
of s or t. Without loss of generality, we assume that k is a multiple of s. Then ( 3.5) implies that
˜χ(n,m)
s,t (k) = 0. Thus, it suﬃces to show that χ(n′, m′)
s,t (k) = 0 for all ( n′, m′)∈ D(s, t). To this
end, we note that since s and t are coprime, s|± (n′t± m′s) if and only if s| n′, which implies
that n′≥ s, a contradiction. Thus, for ( n′, m′)∈ D(s, t), it follows ±(n′t± m′s)⁄≡0 (mod s).
Hence k⁄=±(n′t± m′s), and χ(n′,m′)
s,t (k) = 0. □
Finally, we recall two key properties for the non-holomorph ic Eichler integral
ˆΦ (n,m)(z) :=
√
sti
8π2
∫ +i∞
¯z
θ(0)
0,4st,χ(n,m)
s,t
(τ )
(τ− z)3/2 dτ
where z∈ H− [37, Eqn. (16)]. For z∈ H− and α∈ Q, consider the period function
r(n,m)(z; α) :=
√
sti
8π2
∫ +i∞
α
θ(0)
0,4st,χ(n,m)
s,t
(τ )
(τ− z)3/2 dτ ,
as deﬁned in [ 37, Eqn. (18)]. Then, we have
ˆΦ (n,m)(z) +
( 1
iz
) 3/2 ∑
(n′, m′)∈D(s,t)
Sn′, m′
n,m ˆΦ (n′, m′)
(
− 1
z
)
= r(n,m)(z; 0) (3.9)
and
ˆΦ (n,m)(α) =− 1
2 θ(1)
0,4st,χ(n,m)
s,t
(α) (3.10)
where ( 3.9) is [ 37, Eqn. (17)] and ( 3.10) is [ 37, below Eqn. (19)].
Proof of Theorem 1.4. By Proposition 3.3, we have
θ(ν)
0,4(2st)2, ˜χ(n,m)
s,t
(4stz) =−
√
st
8
∑
(n′,m′)∈D(s,t)
Sn′,m′
n,m θ(ν)
0,4st,χ(n′,m′)
s,t
(z). (3.11)
Also, [ 37, Eqn. (10)] states
θ(0)
0,4st,χ(n′,m′)
s,t
(z) =
√
i
z
∑
(n′, m′)∈D(s,t)
Sn′, m′
n,m θ(0)
0,4st,χ(n′,m′)
s,t
(
− 1
z
)
. (3.12)
Applying Theorem 1.2 part (3) and ( 3.11) gives
Smed
χ(n,m)
s,t
(
− 1
2πiα
)
=− 2eπi/4
π(iα)3/2
√
st
8
∫ +i∞
0
∑
(n′,m′)∈D(s,t) Sn′,m′
n,m θ(0)
0,4st,χ(n′,m′)
s,t
(p)
(1
α + p
) 3/2 dp
16 S. CREW, V. F ANTINI, A. GOSW AMI, R. OSBURN, AND C. WHEELER
− 1
(iα)3/2
∑
(n′,m′)∈D(s,t)
Sn′,m′
n,m θ(1)
0,4st,χ(n′,m′)
s,t
(
− 1
α
)
. (3.13)
Then, by ( 3.12), we rewrite ( 3.13) as follows:
Smed
χ(n,m)
s,t
(
− 1
2πiα
)
=− 2eπi/4
π(iα)3/2
√
sti
8
∫ +i∞
0
θ(0)
0,4st,χ(n,m)
s,t
(−1/p)
√p
(1
α + p
) 3/2 dp
− (iα)−3/2 ∑
(n′,m′)∈D(s,t)
Sn′,m′
n,m θ(1)
0,4st,χ(n′,m′)
s,t
(
− 1
α
)
. (3.14)
We now perform the change of coordinates p→− 1/p to the integral in ( 3.14) and simplify to
obtain
2eπi/4
π(iα)3/2
√
sti
8
∫ +i∞
0
θ(0)
0,4st,χ(n,m)
s,t
(−1/p)
√p
(1
α + p
) 3/2 dp = 2
√
sti
8π2
∫ +i∞
0
θ(0)
0,4st,χ(n,m)
s,t
(p)
(p− α)3/2 dp .
Then, going back to ( 3.14) we ﬁnd
Smed
χ(n,m)
s,t
(
− 1
2πiα
)
=−2
√
sti
8π2
∫ +i∞
0
θ(0)
0,4st,χ(n,m)
s,t
(p)
(p− α)3/2 dp
− (iα)−3/2 ∑
(n′,m′)∈D(s,t)
Sn′,m′
n,m θ(1)
0,4st,χ(n′,m′)
s,t
(
− 1
α
)
= θ(1)
0,4st,χ(n,m)
s,t
(α)
(3.15)
where the last line of ( 3.15) follows from ( 3.9) and ( 3.10). This proves the result. □
Proof of Corollary 1.5. Let u∈ Z≥1. For 0 ≤ ℓ≤ u− 1, deﬁne
X (ℓ)
u (q) :=
∞∑
k1,k2,...,ku=0
(q)ku qk2
1+···+k2
u−1+kℓ+1+···+ku−1
u−1∏
i=1
[
ki+1 + δi,ℓ
ki
]
(3.16)
where δi,ℓ is the characteristic function; see [ 36, Eqn. (11)]. The expression X (ℓ)
u (q) matches the
N th colored Jones polynomial for T (2, 2u + 1) when ℓ = 0 and q = ζN and is an element of H;
see [ 36, Proposition 16]. Take s = 2, t = 2u + 1, n = 1 and m = ℓ + 1 in ( 1.18). Then Hikami’s
strange identity [ 36, Eqn. (15)] 1 reads
X (ℓ)
u (q)“ = ”− 1
2 θ(1)
(2u−2ℓ−1)2,2(8u+4),χ(1,ℓ+1)
2,2u+1
(q). (3.17)
Claims (1) and (2) of Conjecture 1.1 follow from Theorem 1.2 parts (1) and (2), namely the
formal series Fχ(1,ℓ+1)
2,2u+1
(x) has a resurgent Borel transform and its median resummation is an
1Taking u = 1 and ℓ = 0 in ( 3.16) and ( 3.17) yields ( 1.6).
RESURGENCE, HABIRO ELEMENTS AND STRANGE IDENTITIES 17
analytic function for ℜ(x) > 0 with radial limits at points 1
2πi Q. In particular, this is true for
FT (2,2u+1)(x) =Fχ(1,1)
2,2u+1
(x) .
Then, part (3) of Conjecture 1.1 follows by Theorem 1.4 applying ( 3.17) for ℓ = 0. In fact, we
can prove a stronger result:
Smed
χ(1,ℓ+1)
2,2u+1
(
− 1
2πiα
)
.=Fχ(1,ℓ+1)
2,2u+1
(e2πiα) (3.18)
for every 0 ⁄= α∈ Q and 0≤ ℓ≤ u− 1.
Let k∈ Z≥1 and Fk(q) denote the element in H that matches the N th colored Jones polyno-
mial for T (3, 2k) at a root of unity q = e
2πi
N (see [ 6, Eqn. (1.8)] for an explicit q-hypergeometric
expression). Choose s = 3, t = 2 k, n = 2 and m = 1 in ( 1.18). Then the strange identity
Fk(q)“ = ”− 1
2 θ(1)
(2k+1−3)2,3·2k+2,χ(2,1)
3,2k
(q) (3.19)
was proved in [ 6, Theorem 2.4] 2. Claims (1) and (2) of Conjecture 1.1 follow from Theorem 1.2
parts (1) and (2), namely the formal series
FT (3,2k)(x) =Fχ(2,1)
3,2k
(x)
has a resurgent Borel transform and its median resummation i s an analytic function for ℜ(x) > 0
with radial limits at points 1
2πi Q. Then, part (3) of Conjecture 1.1 follows by Theorem 1.4
applying ( 3.19). □
