---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory"
section_id: sec-154-6a-application-of-the-stratification-for-charact
section_title: "6A. Application of the stratification for character sums"
section_number: null
pages: 269-269
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
toc_source: outline
---
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
