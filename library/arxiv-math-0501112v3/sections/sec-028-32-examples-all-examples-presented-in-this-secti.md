---
doc_id: arxiv-math-0501112v3
doc_title: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF"
section_id: sec-028-32-examples-all-examples-presented-in-this-secti
section_title: "Examples. All examples presented in this section not only have the"
section_number: 3.2
pages: 13-14
source_pdf: 0501112v3.pdf
source_sha256: f95088789da2453a
doc_brief: "GAUSSIAN FLUCTUATIONS OF CHARACTERS OF — We study asymptotics of reducible representations of the symmetric groups Sq for large q."
---
character factorization property but additionally are as in Theorem 3.2.
Example 3.4 (Left-regular representation). It is easy to check that if ρq is
the left-regular representation of Sq then for any permutations σ 1, . . . , σ n
with disjoint supports
k(σ 1, . . . , σ n)q
|σ 1 |+···+|σ n |+2(n− 1)
2 =
{
1 if n = 1 and σ 1 = e,
0 otherwise.
It follows from condition (3.1) that the left-regular repre sentation has the
character factorization property and that the mean and the covariance of the
free cumulants are given by
(3.9) lim
q →∞
E(Rl+1)q− l+1
2 =
{
1 if l = 1,
0 if l ≥ 2,
and
(3.10) lim
q →∞
Cov(Rl1+1, R l2+1)q− l1 +l2
2 =





l1 if l1 = l2 ≥ 2,
0 if l1 = l2 = 1,
0 if l1 ⁄= l2.
By applying Corollary 3.3 we recover Kerov central limit the orem for the
Plancherel measure [Ker93b, IO02].
Example 3.5 (Tensor representations). For some integer dq ≥ 1 let ρq be
the representation of Sq acting on (Cd q )⊗q by permutation of factors. This
representation appears naturally within Schur-Weyl duali ty. It is easy to
check that for permutations σ 1, . . . , σ n with disjoint supports
k(σ 1, . . . , σ n)q
|σ 1 |+···+|σ n |+2(n− 1)
2 =



( √
q 
d q
) |σ 1 |
if n = 1,
0 otherwise,
hence if the limit p := limq →∞
√q 
d n
exists then (condition (3.1)) the se-
quence (ρq ) has the character factorization property and the mean and th e
covariance of the free cumulants are given by
lim
q →∞
E(Rl+1)q− l+1
2 = pl− 1,
and
lim
q →∞
Cov(Rl1 +1, R l2+1)q− l1 +l2
2 =
∑
r≥2
( l1
r
)( l2
r
)
r pl1+l2 − 2r
for all integers l, l 1, l 2 ≥ 1. Note that for p = 0 we recover the ﬂuctuations
of the Plancherel measure.
