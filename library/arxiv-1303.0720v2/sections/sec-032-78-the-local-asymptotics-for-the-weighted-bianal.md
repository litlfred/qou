---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-032-78-the-local-asymptotics-for-the-weighted-bianal
section_title: "The local asymptotics for the weighted bianalytic Bergman kernel: the corrective al-"
section_number: 7.8
pages: 28-29
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
gorithm II. Here, we show how to combine the given criteria involving S and S′ in a single
criterion for b2
j, which we explain for j = 0, 1.
We ﬁrst observe ﬁrst that (7.7.17) and (7.7.23) may be united in a single condition:
(7.8.1)
M∂θ ¯wb2
0 + 4
π
|z −w|2
∂θ ¯w
∈M2
z−wR2.
Second, we observe that (7.7.18) and (7.7.25) may be united in a single condition too:
(7.8.2)
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
j
∂w∂θ,M∂θ ¯w
k
N
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

∈M2
z−wR2.
Similar but more complicated statements apply for j = 2, 3, 4, . . . as well. Finally, we observe
that by Lemma 7.4, the condition (7.8.1) determines b2
0 uniquely, and as a consequence, the
condition (7.8.2) determines b2
1 uniquely. Although in principle we are now set to obtain the
concrete expressions for b2
j, the computation is quite messy. For this reason, we show below
how to proceed.
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
29
7.9. The local asymptotics for the weighted bianalytic Bergman kernel: the corrective algo-
rithm III. We continue the analysis of the corrective algorithm, with the aim to obtain concrete
expressions for b2
j, for j = 0, 1, 2. To simplify the notation, we shall at times write
(7.9.1)
λ(z, w) = λQ(z, w) := ∂z ¯∂wQ(z, w),
and sometimes we abbreviate λ = λ(z, w). The function λ(z, w) has the interpretation of the
polarization of ∆Q, which deﬁnes in a natural fashion a Riemannian metric wherever ∆Q > 0
(see, e.g., [2]).
We recall that 1/∂θ ¯w = ¯∂wθ, and observe that
(7.9.2)
∂θ
1
∂θ ¯w = [ ¯∂wθ]−1 ¯∂2
wθ =
¯∂2
wθ
¯∂wθ = ¯∂w log( ¯∂wθ),
and that by (6.2.3),
(7.9.3)
|z −w|2
∂θ ¯w
= |z −w|2 ¯∂wθ =
+∞
X
i=0
1
(i + 1)!( ¯w −¯z)(w −z)i+1∂i+1
z
¯∂wQ(z, w)
=
+∞
X
i=0
1
(i + 1)!( ¯w −¯z)(w −z)i+1∂i
zλ(z, w).
By (7.7.7) combined with Taylor expansion, we see that
(7.9.4)
log( ¯∂wθ) = log(∂z ¯∂wQ(z, w)) +
+∞
X
n=1
(−1)n−1
n
 +∞
X
i=1
1
(i + 1)!(w −z)i ∂i+1
z
¯∂wQ(z, w)
∂z ¯∂wQ(z, w)
n
,
so that in view of (7.9.2), using standard coset notation,
(7.9.5)
∂θ
1
∂θ ¯w ∈¯∂w log λ(z, w) + 1
2(w −z)∂z ¯∂w log λ(z, w) + M2
z−wR1.
From the expansion (7.9.3), we get that
(7.9.6)
|z −w|2
∂θ ¯w
∈|z −w|2λ(z, w) + 1
2|z −w|2(w −z)∂zλ(z, w) + M3
z−wR2,
Next, we put
(7.9.7)
b2
0(z, w) := −4
π|z −w|2[λ(z, w)]2 = −4
π|z −w|2[∂z ¯∂wQ(z, w)]2,
which is biholomorphic in each of the variables (z, ¯w). We quickly check that the condition
(7.8.1) is met. By Lemma 7.4, this is the only possible choice of b2
