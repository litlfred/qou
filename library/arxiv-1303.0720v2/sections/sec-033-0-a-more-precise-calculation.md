---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-033-0-a-more-precise-calculation
section_title: "A more precise calculation"
section_number: 0
pages: 29-31
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
shows that
(7.9.8)
M∂θ ¯wb2
0 + 4
π
|z −w|2
∂θ ¯w
+ 4
π(z −w)|z −w|2∂zλ(z, w) ∈M3
z−wR2,
from which we may conclude that
(7.9.9)
N
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

+ 2
π|z −w|2∂zλ(z, w) ∈M2
z−wR2,
and that
(7.9.10)
∂w∂θ

M∂θ ¯wb2
0 + 4
π
|z −w|2
∂θ ¯w
+ 4
π(z −w)|z −w|2∂zλ(z, w)

∈M2
z−wR2.
30
ANTTI HAIMI AND HAAKAN HEDENMALM
If we recall (6.5.1) and (7.7.8), we see that
(7.9.11)
∂θ∂w
n
(z −w)|z −w|2∂zλ(z, w)
o
=
1
¯∂wθ
¯∂w

∂w −∂wθ
¯∂wθ
¯∂w
n
(z −w)|z −w|2∂zλ(z, w)
o
∈
1
¯∂wθ
¯∂w
n
−2|z−w|2∂zλ(z, w)
o
+ M2
z−wR2 = 2(z−w)∂zλ(z, w)
λ(z, w) −2|z−w|2∂z ¯∂wλ(z, w)
λ(z, w)
+ M2
z−wR2.
By combining this calculation with (7.9.10), we see that
(7.9.12) ∂θ∂w
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

+ 4
π(z −w)∂zλ(z, w)
λ(z, w) −4
π|z −w|2 ∂z ¯∂wλ(z, w)
λ(z, w)
∈M2
z−wR2.
In view of (7.9.5), (7.9.12), we see that (7.8.2) taken modulo Mz−wR2 (see (7.7.18)) gives
b2
1
¯∂wθ
−4
π + 2
π(¯z −¯w)
¯∂wλ(z, w)
λ(z, w)
∈Mz−wR2,
which suggests that we should look for b2
1 of the form
(7.9.13)
b2
1(z, w) := 4
πλ(z, w) −2
π(¯z −¯w) ¯∂wλ(z, w) + 2
π(z −w)∂zλ(z, w) + |z −w|2Ξ1(z, w),
where Ξ1(z, w) is holomorphic in (z, ¯w). We ﬁnd that
(7.9.14)
M∂θ ¯wb2
1 =
b2
1
¯∂wθ ∈4
π −2
π(¯z −¯w)
¯∂wλ(z, w)
λ(z, w)
−4
π(w −z)∂zλ(z, w)
λ(z, w)
−1
π|z −w|2 [∂zλ(z, w)][ ¯∂wλ(z, w)]
[λ(z, w)]2
+ |z −w|2 Ξ1(z, w)
λ(z, w) + M2
z−wR2.
As we add up the relations (7.9.5), (7.9.12), and (7.9.14), the result is
(7.9.15)
M∂θ ¯wb2
1 + ∂θ∂w
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

−4
π + 2
π(¯z −¯w)∂θ
1
∂θ ¯w
∈4
π −2
π(¯z −¯w)
¯∂wλ(z, w)
λ(z, w)
−4
π(w −z)∂zλ(z, w)
λ(z, w) −1
π|z −w|2 [∂zλ(z, w)][ ¯∂wλ(z, w)]
[λ(z, w)]2
+ |z −w|2 Ξ1(z, w)
λ(z, w) −4
π(z −w)∂zλ(z, w)
λ(z, w) + 4
π|z −w|2 ∂z ¯∂wλ(z, w)
λ(z, w)
−4
π
+ 2
π(¯z −¯w)
n ¯∂w log λ(z, w) + 1
2(w −z)∂z ¯∂w log λ(z, w)
o
+ M2
z−wR2,
which we simplify to
(7.9.16)
M∂θ ¯wb2
1 + ∂w∂θ
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

−4
π + 2
π(¯z −¯w)∂θ
1
∂θ ¯w
∈|z −w|2
 3
π
∂z ¯∂wλ(z, w)
λ(z, w)
+ Ξ1(z, w)
λ(z, w)

+ M2
z−wR2.
We want to implement this information into (7.8.2). Then we need the commutator calculation
(7.9.17)
∂w∂θ,M∂θ ¯w
 = M∂w∂2
θ ¯w + M∂2
θ ¯w∂w + M∂w∂θ ¯w∂θ,
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
31
which together with (7.9.9) leads to
(7.9.18)
M−1
∂θ ¯w
∂θ∂w,M∂θ ¯w
 N
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

∈−2
π(¯z −¯w)[∂zλ(z, w)][ ¯∂wλ(z, w)]
[λ(z, w)]2
+ Mz−wR2.
Putting (7.9.16) and (7.9.18) together, we ﬁnd that
(7.9.19)
M∂θ ¯wb2
1 + ∂w∂θ
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

−4
π + 2
π(¯z −¯w)∂θ
1
∂θ ¯w
+ Mz−wM−1
∂θ ¯w
∂w∂θ, M∂θ ¯w
 N
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

∈|z −w|2
 3
π
∂z ¯∂wλ(z, w)
λ(z, w)
+ Ξ1(z, w)
λ(z, w) −2
π
[∂zλ(z, w)][ ¯∂wλ(z, w)]
[λ(z, w)]2

+ M2
z−wR2
By Lemma 7.4, we may conclude from (7.9.19) that
(7.9.20)
Ξ1(z, w) = −3
π∂z ¯∂wλ(z, w) + 2
π
[∂zλ(z, w)][ ¯∂wλ(z, w)]
λ(z, w)
.
In conclusion, we obtain that b2
1 has the form
(7.9.21)
b2
1(z, w) = 4
πλ(z, w) −2
π(¯z −¯w) ¯∂wλ(z, w) + 2
π(z −w)∂zλ(z, w)
−3
π|z −w|2∂z ¯∂wλ(z, w) + 2
π|z −w|2 [∂zλ(z, w)][ ¯∂wλ(z, w)]
λ(z, w)
.
We have also obtained an explicit expression for the third term b2
2, but we omit the rather long
computation. The result is
(7.9.22)
b2
2(z, w) = 2
π∂z ¯∂w log λ + 1
π( ¯w −¯z)∂z ¯∂2
w log λ + 1
π(z −w)∂2
z ¯∂w log λ + |z −w|2Ξ2(z, w),
where
(7.9.23)
Ξ2(z, w) = 3
2π
[∂z ¯∂2
wλ][∂zλ]
[λ]2
−13
2π
[∂zb][∂z ¯∂wλ][ ¯∂wλ]
[λ]3
+ 3
2π
[∂z ¯∂wλ]2
[λ]2
−1
π
[∂zλ]2[ ¯∂2
wλ]
[λ]3
+ 17
4π
[∂zλ]2[ ¯∂wλ]2
[λ]4
−2
3π
∂2
z ¯∂2
wλ
λ
+ 3
2π
[∂2
z ¯∂wλ][ ¯∂wλ]
[λ]2
−1
π
[∂2
zλ][ ¯∂wλ]2
[λ]3
+ 1
3π
[∂2
zλ][ ¯∂2
wλ]
[λ]2
.
Remark 7.6. The formula for b2
0 is given by (7.9.7), the formula for b2
1 is given by (7.9.21), while
b2
2 is expressed by (7.9.22).
