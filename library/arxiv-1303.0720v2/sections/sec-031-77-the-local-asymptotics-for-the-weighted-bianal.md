---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-031-77-the-local-asymptotics-for-the-weighted-bianal
section_title: "The local asymptotics for the weighted bianalytic Bergman kernel: the corrective algo-"
section_number: 7.7
pages: 25-28
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
rithm I. The implementation of the corrective algorithm is rather analogous to the holomorphic
situation of Subsection 6.6. However, since there are certain diﬀerences, we explain everything
in rather great detail. We recall from Subsection 7.2 that the kernel M2,m given by (7.2.4) is a
local bi-reproducing kernel mod(me−δ0m); see Proposition 7.1. If we correct M2,m by adding a
bi-negligible amplitude, then it remains a local bi-reproducing kernel mod(me−δ0m), in view of
(7.4.2). That is, we replace M2,m by the kernel
K⟨k⟩
2,m(z, w) := b⟨2,k⟩(z, w)e2mQ(z,w),
where
(7.7.1)
b⟨2,k⟩:= m2b2
0 + mb2
1 + · · · + m−k+1b2
k+1
is a ﬁnite asymptotic expansion (where each term b2
j is independent of m), with
(7.7.2)
b⟨2,k⟩= −4m2
π |z −w|2( ¯∂wθ)2 + 4m
π
¯∂wθ −2m
π (¯z −¯w) ¯∂2
wθ + ¯∂wθ [∇M ¯∂wθ∇X]⟨k⟩.
Here, X ∼X0 + m−1X1 + m−2X2 + . . . is some asymptotic expansion in m (where every Xj
is independent of m), where each Xj(z, w) should be bi-holomorphic in z and C∞-smooth in
w. Then K⟨k⟩
2,m(z, w) is a local bi-reproducing kernel mod(m−k) as a result of perturbing by the
abschnitt of a negligible amplitude (multiplied by e2mQ(z,w)). We want to add the condition
that b⟨2,k⟩(z, w) be bi-holomorphic in ¯w, to obtain a local weighted bianalytic Bergman kernel
mod(m−k). If we write
v(2) := −4m2
π |z −w|2( ¯∂wθ)2 + 4m
π
¯∂wθ −2m
π (¯z −¯w) ¯∂2
wθ,
so that the kernel M2,m in (7.2.4) may be written as
(7.7.3)
M2,m(z, w) = v(2)(z, w) e2mQ(z,w),
then the relation (7.7.2) may be expressed in condensed form:
(7.7.4)
b(2) −v(2)
¯∂wθ
⟨k⟩
= [∇M ¯∂wθ∇X]⟨k⟩.
Here, b(2) ∼m2b2
0 + mb2
1 + b2
2 + . . . is the asymptotic expansion with abschnitt b⟨2,k⟩. This now
puts us in a position to apply Proposition 7.2, which says that (7.7.4) holds for some X if and
only if
(7.7.5)

S
b(2) −v(2)
¯∂wθ
⟨k⟩
∈Mz−wR2
and
S′
b(2) −v(2)
¯∂wθ
⟨k⟩
∈Mz−wR2.
Also, Remark 7.3 tells us how to recover the corresponding abschnitt of X:
(7.7.6)
X⟨k+2⟩= (2m)−2

S−1NS′
b(2) −v(2)
¯∂wθ
⟨k⟩
.
This formula is valuable when we need to estimate the contribution from the bi-negligible
amplitude using (7.4.2).
It remains to see how (7.7.5) helps us determine the asymptotic expansion b(2). A ﬁrst remark
is that it no longer will be enough to determine b(2)(z, w) along the diagonal z = w, as functions
which are biharmonic in each of the variables (z, ¯w) need not be uniquely determined by their
diagonal restrictions (e.g., consider the function ¯zw −z ¯w).
26
ANTTI HAIMI AND HAAKAN HEDENMALM
Before we carry on to analyze the relations (7.7.5) further, we recall the Taylor expansions
(6.2.2), (6.2.3), and (6.2.4), and rewrite (6.2.3) in the form
(7.7.7)
¯∂wθ = ∂z ¯∂wQ(z, w)

1 +
+∞
X
j=1
1
(j + 1)!(w −z)j ∂j+1
z
¯∂wQ(z, w)
∂z ¯∂wQ(z, w)

,
It follows from (6.2.4) and (7.7.7) that
(7.7.8)
∂wθ
¯∂wθ −1
2
∂2
zQ(z, w)
∂z ¯∂wQ(z, w) ∈Mz−wR1.
A more reﬁned version of (7.7.8) is
(7.7.9) ∂wθ
¯∂wθ −1
2
∂2
zQ(z, w)
∂z ¯∂wQ(z, w) −(w −z)
1
3
∂3
zQ(z, w)
∂z ¯∂wQ(z, w) −1
4
[∂2
zQ(z, w)][∂2
z ¯∂wQ(z, w)]
[∂z ¯∂wQ(z, w)]2

∈M2
z−wR1.
We now return to the corrective algorithm, which takes the criteria (7.7.5) as its starting point.
We express v(2) in terms of the diﬀerential operators ∂w and ∂θ, using that ∂θ ¯w = 1/ ¯∂wθ:
(7.7.10)
v(2)
¯∂wθ = M∂θ ¯w[v(2)] = −4m2
π
|z −w|2
∂θ ¯w
+ 4m
π −2m
π (¯z −¯w)∂θ
1
∂θ ¯w.
We ﬁrst rewrite the criteria (7.7.5) in the more appropriate form
(7.7.11)
n
SM∂θ ¯w[b(2) −v(2)]
o⟨k⟩∈Mz−wR2
and
n
S′M∂θ ¯w[b(2) −v(2)]
o⟨k⟩∈Mz−wR2.
In view of the asymptotic expansion for b(2) (see (7.7.1)) and the deﬁnition (6.5.3) of the operator
S, it follows that
(7.7.12)
n
SM∂θ ¯w[b(2)]
o⟨k⟩=
k+1
X
j=0
m2−j
j
X
i=0
2−i
i! (∂w∂θ)iM∂θ ¯wb2
j−i.
We would also like to calculate the corresponding expression involving the operator S′ in place
of S (see (7.5.1)). In a ﬁrst step, we get that
n
S−1NSM∂θ ¯w[b(2)]
o⟨k⟩=
k+1
X
j=0
m2−j
j
X
i2=0
i2
X
i1=0
(−1)i2−i12−i2
i1!(i2 −i1)! (∂w∂θ)i2−i1N(∂w∂θ)i1M∂θ ¯wb2
j−i2,
and, in a second step, we obtain (since M∂θ ¯w = M−1
¯∂wθ)
(7.7.13)
n
S′M∂θ ¯w[b(2)]
o⟨k⟩=
n
SM∂θ ¯wS−1NSM∂θ ¯w[b(2)]
o⟨k⟩
=
k+1
X
j=0
m2−j
j
X
i3=0
i3
X
i2=0
i2
X
i1=0
(−1)i2−i12−i3
i1!(i2 −i1)!(i3 −i2)!(∂w∂θ)i3−i2M∂θ ¯w(∂w∂θ)i2−i1N(∂w∂θ)i1M∂θ ¯wb2
j−i3.
We also need to calculate the corresponding expressions for v(2). First, we ﬁnd that (see (7.7.10))
(7.7.14)
n
SM∂θ ¯w[v(2)]
o⟨k⟩=

S

−4m2
π
|z −w|2
∂θ ¯w
+ 4m
π −2m
π (¯z −¯w)∂θ
1
∂θ ¯w
⟨k⟩
= 4m
π −4m2
π
|z −w|2
∂θ ¯w
−
k+1
X
j=1
(2m)2−j
j!π
(∂w∂θ)j−1

j(¯z −¯w)∂θ
1
∂θ ¯w + ∂w∂θ
|z −w|2
∂θ ¯w

,
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
27
and, consequently,
(7.7.15)
n
NSM∂θ ¯w[v(2)]
o⟨k⟩= −4m2
π
¯z −¯w
∂θ ¯w
−
k+1
X
j=1
(2m)2−j
j!π
N(∂w∂θ)j−1

j(¯z −¯w)∂θ
1
∂θ ¯w + ∂w∂θ
|z −w|2
∂θ ¯w

= −
k+1
X
j=0
(2m)2−j
j!π
N

j(∂w∂θ)j−1M¯z−¯w ∂θ
1
∂θ ¯w + (∂w∂θ)j |z −w|2
∂θ ¯w

,
where we interpret the term for j = 0 is the natural fashion. By expansion of the operators
involved, it is clear that, formally,
SM∂θ ¯wS−1 =
+∞
X
j=0
(2m)−j
j
X
i=0
(−1)i
i!(j −i)!(∂w∂θ)j−iM∂θ ¯w(∂w∂θ)i,
which we apply to (7.7.15):
(7.7.16)
n
S′M∂θ ¯w[v(2)]
o⟨k⟩=
n
SM∂θ ¯wS−1NSM∂θ ¯w[v(2)]
o⟨k⟩= −1
π
k+1
X
j=0
(2m)2−j
j
X
i2=0
i2
X
i1=0
(−1)i2−i1
i2!i1!(i2 −i1)!
× (∂w∂θ)i1M∂θ ¯w(∂w∂θ)i2−i1N

(j −i2)(∂w∂θ)j−i2−1M¯z−¯w∂θ
1
∂θ ¯w + (∂w∂θ)j−i2 |z −w|2
∂θ ¯w

.
We may now apply the criterion (7.7.11) for each power of m separately. The ﬁrst part of the
criterion, which involves S, says (for j = 0)
(7.7.17)
4
π
|z −w|2
∂θ ¯w
+ M∂θ ¯wb2
0 ∈Mz−wR2,
and (for j = 1)
(7.7.18)
−4
π + 2
π(¯z −¯w)∂θ
1
∂θ ¯w + 2
π∂w∂θ
|z −w|2
∂θ ¯w
+ M∂θ ¯wb2
1 + 1
2∂w∂θM∂θ ¯wb2
0 ∈Mz−wR2,
while (for j = 2, 3, 4, . . .)
(7.7.19)
22−j
j!π (∂w∂θ)j−1

j(¯z −¯w)∂θ
1
∂θ ¯w + ∂w∂θ
|z −w|2
∂θ ¯w

+
j
X
i=0
2−i
i! (∂w∂θ)iM∂θ ¯wb2
j−i ∈Mz−wR2.
As for the second part of the criterion (7.7.11), which involves S′, it says that (use (7.7.13) and
(7.7.16)) for j = 0, 1, 2, . . .,
(7.7.20)
j
X
i3=0
i3
X
i2=0
i2
X
i1=0
(−1)i2−i12−i3
i1!(i2 −i1)!(i3 −i2)!(∂w∂θ)i3−i2M∂θ ¯w(∂w∂θ)i2−i1N(∂w∂θ)i1M∂θ ¯wb2
j−i3
+ 22−j
π
j
X
i2=0
i2
X
i1=0
(−1)i2−i1
i2!i1!(i2 −i1)!
× (∂w∂θ)i1M∂θ ¯w(∂w∂θ)i2−i1N

(j −i2)(∂w∂θ)j−i2−1M¯z−¯w∂θ
1
∂θ ¯w + (∂w∂θ)j−i2 |z −w|2
∂θ ¯w

∈Mz−wR2.
28
ANTTI HAIMI AND HAAKAN HEDENMALM
For j = 0, the condition (7.7.20) reads
(7.7.21)
4
πM∂θ ¯wN|z −w|2
∂θ ¯w
+ M∂θ ¯wNM∂θ ¯wb2
0 ∈Mz−wR2,
and for j = 1,
(7.7.22)
M∂θ ¯wNM∂θ ¯wb2
1 + 1
2∂w∂θM∂θ ¯wNM∂θ ¯wb2
0 −1
2M−1
∂θ ¯w∂w∂θNM∂θ ¯wb2
0
+ 1
2M∂θ ¯wN∂w∂θM∂θ ¯wb2
0 + 2
π∂w∂θM∂θ ¯wN
|z −w|2
∂θ ¯w

−2
πM∂θ ¯w∂w∂θN
|z −w|2
∂θ ¯w

+ 2
πM∂θ ¯wN∂w∂θ
|z −w|2
∂θ ¯w

+ 2
πM∂θ ¯wN

(¯z −¯w)∂θ
1
∂θ ¯w

∈Mz−wR2.
As the function 1/∂θ ¯w is in R1, we may rewrite (7.7.21) in the form
(7.7.23)
N
 4
π
|z −w|2
∂θ ¯w
+ M∂θ ¯wb2
0

∈Mz−wR2.
and we may reorganize (7.7.22):
(7.7.24)
NM∂θ ¯wb2
1 + M−1
∂θ ¯w∂w∂θM∂θ ¯wN
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

−∂w∂θN
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

+ N∂w∂θ
1
2M∂θ ¯wb2
0 + 2
π
|z −w|2
∂θ ¯w

+ 2
πN

(¯z −¯w)∂θ
1
∂θ ¯w

∈Mz−wR2.
In terms of the usual commutator ⌊A,B⌋:= AB −BA, we may express (7.7.24) as
(7.7.25)
N

M∂θ ¯w[b2
1] + ∂w∂θ
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

+ M−1
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
∈Mz−wR2.
