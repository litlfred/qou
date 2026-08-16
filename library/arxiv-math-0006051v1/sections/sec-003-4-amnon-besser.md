---
doc_id: arxiv-math-0006051v1
doc_title: "logarithm”) in [Kon]. The ﬁnite logarithm is the case n = 1 of the n-th poly- logarithm li n ∈ Z/p [z] deﬁned by li n(z) = ∑ p− 1 k=1 zk/k n. In loc. cit. Kontsevich proved that th"
section_id: sec-003-4-amnon-besser
section_title: "AMNON BESSER"
section_number: 4
pages: 4-5
source_pdf: 0006051v1.pdf
source_sha256: 10483e75bd3655ea
doc_brief: "FINITE AND p-ADIC POLYLOGARITHMS AMNON BESSER 1. Introduction The finite logarithm was introduced by Kontsevich (under the name “ The 1 1 logarithm”) in [Kon]. The finite logarithm is the case n = 1 o"
---
This implies that
vp(ak(fn+1)) ≥ min
l<k
[vp(al(fn))] − vp(k) .
The lemma is clearly true for n = 0. Suppose it is true for n. Then
vp(ak(fn+1)) ≥ min
l≤ k
[−vp(l!)] − vp(k) ≥ −vp((k − 1)!) − vp(k) = −vp(k!) .
Since gn(w) = p− nfn(αpw ), to ﬁnish the proof we have to check that for every
k ≥ p we have k − n − vp(k!) > 0. The well known estimate vp(k!) ≤ k/ (p − 1) and
the assumption n < p imply that it is suﬃcient to require k(1 − 1/ (p − 1)) ≥ p, and
this is satisﬁed for k ≥ p + 1. The case k = p is also OK according to this analysis
unless n = p − 1.
Proof of Theorem 1.1. Using the fact that D is a derivation and that
D logk(z) = z(1 − z) d
dz logk(z) = z(1 − z)k logk− 1(z) 1
z = (1 − z)k logk− 1(z)
and
D Lik(z) = z(1 − z) d
dz Lik(z) = z(1 − z) Lik− 1(z) 1
z = (1 − z) Lik− 1(z)
we see that
DFn(z) = D
n− 1∑
k=0
ak logk(z) Lin− k(z)
= (1 − z)
n− 1∑
k=0
ak(k logk− 1(z) Lin− k(z) + logk(z) Lin− k− 1(z))
= (1 − z)
n− 1∑
k=0
logk(z) Lin− k− 1(z)(ak + (k + 1)ak+1) .
Here we understand that an = 0. Every z ∈ X can be written as α (1 + pw) with α
a root of unity in X and w ∈ W . We have
p− 1 log(α (1 + pw)) = p− 1 log(1 + pw) ≡ w (mod p) .
If we assume that ak ∈ Z[1/ (n + 1)!] we now ﬁnd from the last computation and
from proposition 2.3,
p1− nDFn(α (1 + pw))
≡ (1 − α )
n− 1∑
k=0
wk(ak + (k + 1)ak+1)
n− k− 1∑
m=0
1
m!
~Lin− k− 1− m(α )wm
≡ (1 − α )
n− 1∑
l=0
wl
l∑
k=0
(ak + (k + 1)ak+1) 1
(l − k)!
~Lin− l− 1(α ) .
FINITE AND p-ADIC POLYLOGARITHMS 5
It follows that to make the reduction of p1− nDFn independent of w for all p > n + 1
it is necessary and suﬃcient that for l = 1, . . . , n − 1 we have
l∑
k=0
(ak + (k + 1)ak+1) 1
(l − k)! = 0 .(2.1)
If this is satisﬁed then the reduction of p1− nDFn(α (1 + pw)) is ( a0 + a1)(1 −
α ) ~Lin− 1(α ) ≡ −(a0 + a1) lin− 1(σ (α )) so we should also require a0 + a1 = −1.
Let A(t) = ∑ n− 1
k=0 aktk. Then the relations (2.1) can be written as et(A(t) +
dA(t)/dt ) ≡ a (mod tn) where a is a constant. This implies that A(t) +dA(t)/dt ≡
ae− t (mod tn) and after solving the resulting diﬀerential equation that the n − 2
ﬁrst equations in (2.1) are equivalent to A(t) ≡ (at + b)e− t (mod tn− 1) for some
other constant b. We have −1 = a0 + a1 = b + (a − b) = a. Now, in ( b − t)e− t the
coeﬃcient of tn is
b (−1)n
n! − (−1)n− 1
(n − 1)! = (−1)n− 1
(n − 1)! (1 − b/n ) .
It is easy to see that for the equation (2.1) with l = n − 1 to be satisﬁed, this
coeﬃcient must be 0 and hence b = n. This gives the choice of the coeﬃcients in
the theorem and shows that they are the unique choice in Z[1/ (n + 1)!]. Now if we
have coeﬃcients in Q satisfying the theorem, then we may clear denominators not
dividing ( n + 1)! and using only independence of w we obtain that these must be a
rational multiple of our ak. But since the reduction of p1− nDFn is non-trivial the
multiplier must be 1.
Remark 2.5. We have the equation Fn(z) = −nLn(z) − Ln− 1(z) log(z), where
Ln(z) =
n− 1∑
m=0
(−1)m
m! Lin− m(z) logm(z)
is the function deﬁned in [BdJ00]. By loc. cit. the function Fn satisﬁes Fn(z) +
(−1)nFn(1/z ) = 0. Diﬀerentiating this relation one gets the relation zDF n(1/z ) +
(−1)nDFn(z) = 0. Reducing modulo p we ﬁnd z lin− 1(1/z ) + (−1)n lin− 1(z) = 0.
This relation is easily veriﬁed directly.
