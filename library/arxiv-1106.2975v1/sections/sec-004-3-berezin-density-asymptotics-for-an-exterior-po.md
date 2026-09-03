---
doc_id: arxiv-1106.2975v1
doc_title: "The Polyanalytic Ginibre Ensembles"
section_id: sec-004-3-berezin-density-asymptotics-for-an-exterior-po
section_title: "Berezin density asymptotics for an exterior point"
section_number: 3
pages: 14-21
source_pdf: 1106.2975v1.pdf
source_sha256: 7e966c7392b70ae0
doc_brief: "The Polyanalytic Ginibre Ensembles — For integers n, q = 1, 2, 3, . . ., let Poln,q denote the C-linear space of polynomials in z and ¯z, of degree ≤n −1 in z and of degree ≤q −1 in ¯z."
---
Convergence to harmonic measure. We show that the Berezin measures have the
convergence dB⟨z⟩
m,n,q →dωz for z ∈De as m, n →+∞while n = m + O(1). Here, ωz
is harmonic measure with respect to the point z and the exterior disk De.
Concentration of the Berezin mass. We ﬁrst study the concentration of the Berezin
measure to neighborhoods of the closed unit disk ¯D. We recall the standard
notation D(z0, ρ) for the open disk of radius ρ centered at z0.
Lemma 3.1. Suppose z ∈De and that ρ > 1. Then
(3.1)
Z
C\D(0,ρ)
B⟨z⟩
m,n,q(w) dA(w) →0,
as m, n →+∞while n ≤m + O(1).
Proof. Let w ∈C \ D(0, ρ). We note that
(3.2)
n −1 ≤m + O(1) ≤2m
for suﬃciently big m, and so, by Lemma 2.3,
(3.3)
n−r−1
X
i=0
r!
(r + i)!

(mz ¯w)iLi
r(m|z|2)Li
r(m|w|2)

≤
n−r−1
X
i=0
1
r!(r + i)!(m|zw|)i(m|z|2 + i + r)r(m|w|2 + i + r)r
≤9r
r!
n−r−1
X
i=0
1
(r + i)!(m|zw|)i+2r ≤9r
r! (m|zw|)r En−1(m|zw|).
The Polyanalytic Ginibre Ensembles
15
If we plug in n = q in (3.3), we obtain
(3.4)
q−j−1
X
k=1
j!
(j + k)!

(m¯zw)kLk
j(m|z|2)Lk
j(m|w|2)

 ≤9j
j! (m|zw|)jEq−1(m|zw|).
We may restrict to q ≤n; after, we are considering the limit as n →+∞. As
Eq−1 ≤En−1 on the positive half-axis for q ≤n, an application of (3.3) and (3.4) to
(2.1) gives
(3.5)
|Km,n,q(z, w)| ≤2me9(m|zw|)q−1En−1(m|zw|).
Next, we observe that Polm,n,1 ⊂Polm,n,q (since q ≥1), which implies that
Km,n,q(z, z) ≥Km,n,1(z, z) = mEn−1(m|z|2).
We conclude that the Berezin density may be estimated as follows:
B⟨z⟩
m,n,q(w) ≤4m e18(m|zw|)2q−2 En−1(m|zw|)2
En−1(m|z|2) e−m|w|2.
(3.6)
Finally, we see from Szegö’s asymptotical expansion (2.3) that
Ek(lζ)
elζ
= (2πk)−1/2(l/k)k
ζ
z −k/l(ζe1−lζ/k)k(1 + ϵ2
k(lζ/k)).
(3.7)
k ≤l + O(1), where the convergence ϵ2
k(lζ/k) →0 is uniform if ζ is real with ζ ≥a
for some ﬁxed a > 1. This leads to
En−1(m|zw|)2
En−1(m|z|2) = [2π(n −1)]−1/2[(n −1)/m]n−1en−1|w|2n−2(1 + o(1)),
where the “o” term is uniform in the convergence. As we implement this estimate
in (3.6), and integrate over C \ D(0, ρ), the claim follows.
□
A principal value calculation. We follow the approach of [2], and calculate a
certain principal value integral.
Lemma 3.2. Fix z ∈De. For any l = 0, 1, 2, . . ., we have
pv
Z
C
w−lB⟨z⟩
m,n,q(w)dA(w) →z−l,
as m, n →+∞with n = m + O(1).
Proof. The case q = 1 was treated in [2], so we may from now on assume that
q ≥2. We write
Km,n,q = KI
m,n,q + KII
m,n,q,
where
KI
m,n,q(z, w) := m
q−1
X
r=0
n−r−1
X
i=0
r!
(r + i)!(mz ¯w)iLi
r(m|z|2)Li
r(m|w|2)
and
KII
m,n,q(z, w) := m
q−2
X
j=0
q−j−1
X
k=0
j!
(j + k)!(m¯zw)kLk
j(m|z|2)Lk
j(m|w|2).
It follows that the expression |Km,n,q|2 decomposes accordingly:
(3.8)
|Km,n,q(z, w)|2 = |KI
m,n,q(z, w)|2 + |KII
m,n,q(z, w)|2 + 2 Re[KI
m,n,q(z, w)KII
m,n,q(z, w)].
16
Haimi and Hedenmalm
We ﬁrst consider the following integral involving |KI
m,n,q|2:
(3.9)
pv
Z
C
w−l|KI
m,n,q(z, w)|2e−m|w|2dA(w)
= m2
q−1
X
r1,r2=0
n−r1−1
X
i1=0
n−r2−1
X
i2=0
pv
Z
C
w−l
r1!r2!
(r1 + i1)!(r2 + i2)!(mz ¯w)i1(m¯zw)i2
× Li1
r1(m|z|2)Li1
r1(m|w|2)Li2
r2(m|z|2)Li2
r2(m|w|2)e−m|w|2dA(w)
= m2z−l
q−1
X
r1,r2=0
n−r1−1
X
i1=0
n−r2−1
X
i2=0
mi1+i2r1!r2!
(r1 + i1)!(r2 + i2)!δi2,i1+l |z|2i2Li1
r1(m|z|2)Li2
r2(m|z|2)
×
Z
C
|w|2i1Li1
r1(m|w|2)Li2
r2(m|w|2)e−m|w|2dA(w),
where the delta is understood in Kronecker’s sense. The identity (for p = 1, 2, 3, . . .)
(3.10)
Lα+p
r
(x) =
r
X
s=0
 r −s + p −1
p −1
!
Lα
s (x)
plus the standard orthogonality properties of the Laguerre polynomials gives that
Z +∞
0
ti1Li1
r1(t)Li1+l
r2 (t)e−tdt = (r1 + i1)!(r2 −r1 + l −1)!
r1!(r2 −r1)!(l −1)!
,
where the right-hand side should be interpreted as 0 for r2 < r1. By polar coordi-
nates, then, we have
Z
C
|w|2i1Li1
r1(m|w|2)Li1+l
r2 (m|w|2)e−m|w|2dA(w) = m−i1−1 (r1 + i1)!(r2 −r1 + l −1)!
r1!(r2 −r1)!(l −1)!
,
and (3.9) simpliﬁes to
(3.11)
pv
Z
C
w−l|KI
m,n,q(z, w)|2e−m|w|2dA(w)
= m z−l
q−1
X
r1=0
q−1
X
r2=r1
n−l−r2−1
X
i1=0
r2!(r2 −r1 + l −1)!
(r2 −r1)!(l −1)!(r2 + i1 + l)! (m|z|2)i1+lLi1
r1(m|z|2)Li1+l
r2 (m|z|2),
provided n is so big that q + l ≤n. Next, we apply Lemma 2.3 and (3.2) (using that
z ∈De) to arrive at
(3.12)
n−l−r2−1
X
i1=0
r1!r2!
(r2 + i1 + l)! (m|z|2)i1+l

Li1
r1(m|z|2)Li1+l
r2 (m|z|2)

≤
n−l−r2−1
X
i1=0
1
(r2 + i1 + l)! (m|z|2)i1+l(m|z|2 + i1 + r1)r1(m|z|2 + i1 + l + r2)r2
≤3r1+r2
n−l−r2−1
X
i1=0
1
(r2 + i1 + l)! (m|z|2)r1+r2+i1+l ≤3r1+r2(m|z|2)r1En−1(m|z|2).
The Polyanalytic Ginibre Ensembles
17
On the other hand, by the estimate from below in Lemma 2.3,
(3.13)
Km,n,q(z, z) ≥KI
m,n,q(z, z) = m
q−1
X
r=0
n−r−1
X
i=0
r!
(r + i)!(m|z|2)iLi
r(m|z|2)2
≥m
q−1
X
r=0
n−r−1
X
i=0
1
r!(r + i)!(m|z|2)i[m|z|2 −β(n)]2r
provided that m|z|2 ≥β(n), where
β(n) := n + q −4 + 2
q
1
4 + (q −2)(n −1) = n + O(
√
n).
As we assume z ∈De and n = m + O(1), we must have
m|z|2 −β(n) = m(|z|2 −1) + m −β(n) ≥1
2m(|z|2 −1)
for big enough m, n, and so, by (3.13),
(3.14)
Km,n,q(z, z) ≥KI
m,n,q(z, z) ≥m
q−1
X
r=0
n−r−1
X
i=0
4−r
r!(r + i)!(m|z|2)i+2r
≥41−qm
(q −1)!(m|z|)q−1[En−1(m|z|2) −Eq−2(m|z|2)] ≥
4−qm
(q −1)!(m|z|)q−1En−1(m|z|2).
Here, we used that the En−1(m|z|2) is much bigger than Eq−2(m|z|2) as m, n both
grow. Let us look at the contribution from 0 ≤r1 ≤q −2 in the right-hand side of
(3.11) using the estimate (3.12):
m |z|−l
q−2
X
r1=0
q−1
X
r2=r1
n−l−r2−1
X
i1=0
r2!(r2 −r1 + l −1)!
(r2 −r1)!(l −1)!(r2 + i1 + l)! (m|z|2)i1+l

Li1
r1(m|z|2)Li1+l
r2 (m|z|2)

≤m
|z|−l
(l −1)!
q−2
X
r1=0
q−1
X
r2=r1
(r2 −r1 + l −1)!
r1!(r2 −r1)!
3r1+r2(m|z|2)r1En−1(m|z|2)
≤mC1(q, l)(m|z|2)q−2En−1(m|z|2),
for an appropriate positive constant C1(q, l). As we combine this estimate with
(3.14), we obtain
m
|z|−l
Km,n,q(z, z)
q−2
X
r1=0
q−1
X
r2=r1
n−l−r2−1
X
i1=0
r2!(r2 −r1 + l −1)!
(r2 −r1)!(l −1)!(r2 + i1 + l)!
× (m|z|2)i1+l

Li1
r1(m|z|2)Li1+l
r2 (m|z|2)

 ≤C2(q, l)m−1 = O(m−1) −→0,
as m, n →+∞in the prescribed fashion. So the contribution to (3.11) which comes
from 0 ≤r1 ≤q −2 is negligible from the point of view of the Berezin density. It
remains to consider the contribution from r1 = q −1. The corresponding part of
the sum in the right-hand side of (3.11) equals
m z−l
n−l−q
X
i1=0
(q −1)!
(q + i1 + l −1)! (m|z|2)i1+lLi1
q−1(m|z|2)Li1+l
q−1(m|z|2),
18
Haimi and Hedenmalm
and we now claim that
(3.15)
m
z−l
Km,n,q(z, z)
n−l−q
X
i1=0
(q −1)!
(q + i1 + l −1)! (m|z|2)i1+lLi1
q−1(m|z|2)Li1+l
q−1(m|z|2) −→z−l,
as m, n →+∞in the given fashion. We use the recurrence relation (3.10) to write
(3.16)
Li1
q−1(x) = Li1+l
q−1(x) −
q−2
X
s=0
 q + l −s −2
l −1
!
Li1
s (x).
A straightforward argument allows us to show that as insert this into (3.15), the
sum that is subtracted on the right-hand side of (3.16) makes asymptotically no
contribution to the sum in (3.15). Consequently, (3.15) is equivalent to having
m
z−l
Km,n,q(z, z)
n−l−q
X
i1=0
(q −1)!
(q + i1 + l −1)!(m|z|2)i1+lLi1+l
q−1(m|z|2)2 −→z−l
(3.17)
as m, n →+∞in the given fashion. If we insert the expression (2.1) deﬁning
Km,n,q(z, z), we see that (there is some cancellation of terms)
(3.18)
z−l −m
z−l
Km,n,q(z, z)
n−l−q
X
i1=0
(q −1)!
(q + i1 + l −1)!(m|z|2)i1+lLi1+l
q−1(m|z|2)Li1+l
q−1(m|z|2)
=
z−l
Km,n,q(z, z)
(
m
q−2
X
r=0
n−r−1
X
i=0
r!
(r + i)!(m|z|2)iLi
r(m|z|2)2
+ m
q−2
X
j=1
q−j−1
X
k=1
j!
(j + k)!(m|z|2)kLk
j(m|z|2)2 + m
l−1
X
i1=0
(q −1)!
(q + i −1)!(m|z|2)iLi
q−1(m|z|2)2
)
.
By careful application of Lemma 2.3 to all the Laguerre polynomials in this ex-
pression, while inserting (3.13) to control the denominator, we indeed get (3.17).
So, after a lot of eﬀort, we have obtained that
(3.19)
pv
Z
C
w−l |KI
m,n,q(z, w)|2
Km,n,q(z, z) e−m|w|2dA(w) −→z−l
as m, n →+∞with n = m + O(1). Analogous but slightly easier arguments (left to
the interested reader) show that
pv
Z
C
w−j |KII
m,n,q(z, w)|2
Km,n,q(z, z) e−|w|2dA(w) −→0
and
Z
C
w−j Re
(KI
m,n,q(z, w)KII
m,n,q(z, w)
Km,n,q(z, z)
)
e−|w|2dA(w) −→0,
again as m, n →+∞with n = m + O(1). Finally, we put everything together based
on the decomposition (3.8):
pv
Z
C
w−jB⟨z⟩
m,n,q(w) = pv
Z
C
|Km,n,q(z, w)|2
Km,n,q(z, z)
e−|w|2dA(w) −→z−l,
as m, n →+∞with n = m + O(1). This ends the proof.
□
The Polyanalytic Ginibre Ensembles
19
Convergence to harmonic measure. We now show that even in the principal
value sense, the Berezin density tends to avoid the interior of the unit disk.
Lemma 3.3. Fix a real parameter ρ with 0 < ρ < 1 and a point z ∈De. Then, for
l = 0, 1, 2, . . ., we have the convergence
pv
Z
D(0,ρ)
w−lB⟨z⟩
m,n,q(w)dA(w) −→0,
as m, n →+∞with n = m + O(1).
Proof. In terms of the decomposition (3.8), we will focus on the the term |KI
m,n,q|2
and leave the other two to the reader (the necessary arguments are similar but
slightly easier). The analogue of (3.9) reads
(3.20)
pv
Z
D(0,ρ)
w−l|KI
m,n,q(z, w)|2e−m|w|2dA(w)
= m2z−l
q−1
X
r1,r2=0
min{n−r1−1,n−l−r2−1}
X
i1=0
r1!r2!
(r1 + i1)!(r2 + i1 + l)!m(|z|2)i1+lLi1
r1(m|z|2)Li1+l
r2 (m|z|2)
×
Z
D(0,ρ)
(m|w|2)i1Li1
r1(m|w|2)Li1+l
r2 (m|w|2)e−m|w|2dA(w).
By Lemma 2.3, we have
Z
D(0,ρ)
(m|w|2)i1

Li1
r1(m|w|2)Li1+l
r2 (m|w|2)

e−m|w|2dA(w)
≤
1
r1!r2!
Z
D(0,ρ)
(m|w|2)i1(m|w|2 + i1 + r1)r1(m|w|2 + i1 + l + r2)r2e−m|w|2dA(w)
≤2r1+r2−2
r1!r2!
Z
D(0,ρ)
(m|w|2)i1[(m|w|2)r1 + (i1 + r1)r1][(m|w|2)r2 + (i1 + l + r2)r2]e−m|w|2dA(w)
= 2r1+r2−2
r1!r2!m
( Z mρ2
0
ti1+r1+r2e−tdt + (i1 + r1)r1
Z mρ2
0
ti1+r2e−tdt
+ (i1 + l + r2)r2
Z mρ2
0
ti1+r1e−tdt + (i1 + r1)r1(i1 + l + r2)r2
Z mρ2
0
ti1e−tdt
)
.
In terms of the function
χ(a, b) :=
1
Γ(a + 1)
Z b
0
tae−tdt,
a, b ∈[0, +∞[,
which takes values in the interval [0, 1[, the estimate becomes
Z
D(0,ρ)
(m|w|2)i1

Li1
r1(m|w|2)Li1+l
r2 (m|w|2)

e−m|w|2dA(w)
≤2r1+r2−2
r1!r2!m
(
(i1 + r1 + r2)!χ(i1 + r1 + r2, mρ2) + (i1 + r1)r1(i1 + r2)!χ(i1 + r2, mρ2)
+ (i1 + l + r2)r2(i1 + r1)!χ(i1 + r1, mρ2) + (i1 + r1)r1(i1 + l + r2)r2i1!χ(i1, mρ2)
)
.
20
Haimi and Hedenmalm
and if we use that a 7→χ(a, b) is decreasing for ﬁxed b (a direct calculation involving
derivatives suﬃces to verify this), we get
(3.21)
Z
D(0,ρ)
(m|w|2)i1

Li1
r1(m|w|2)Li1+l
r2 (m|w|2)

e−m|w|2dA(w)
≤2r1+r2−2
r1!r2!m
(
(i1 + r1 + r2)! + (i1 + r1)r1(i1 + r2)!
+ (i1 + l + r2)r2(i1 + r1)! + (i1 + r1)r1(i1 + l + r2)r2i1!
)
χ(i1, mρ2).
Next, since z ∈De, n = m + O(1), and i1 + l ≤n −1, we may use another aspect of
Lemma 2.3 to see that
(3.22)

Li1
r1(m|z|2)Li1+l
r2 (m|z|2)

 ≤
1
r1!r2!(m|z|2)r1+r2,
provided m, n are big enough. As we combine the equality (3.20) with the estimates
(3.21) and (3.22), and use some well-understood comparisons of factorials and
powers, we arrive at
(3.23)

 pv
Z
D(0,ρ)
w−l|KI
m,n,q(z, w)|2e−m|w|2dA(w)

≤m C3(q, l)|z|−l+2q−2
n−l−1
X
i1=0
(m|z|2)i1+l
(i1 + l)! χ(i1, mρ2),
for some appropriate positive constant C3(q, l). The function χ(i1, mρ2) drops oﬀ
exponentially quickly to 0 as i1 exceeds mρ2 by a margin greater than O(m1/2), as
can be seen, e.g., by an application of the Central Limit Theorem (compare with the
next section). This means that eﬀectively we are summing up to m|ρ|2 + O(m1/2)
in the right-hand side expression of (3.23), which does not permit the sum to
compare with the size of Km,n,q(z, z); cf. (3.14). This results in the convergence
pv
Z
D(0,ρ)
w−l |KI
m,n,q(z, w)|2
Km,n,q(z, z)
e−m|w|2dA(w) −→0
as m, n →+∞with n = m + O(1). Together with the estimates which were left as
an exercise to the reader, we get
pv
Z
D(0,ρ)
w−l |Km,n,q(z, w)|2
Km,n,q(z, z)
e−m|w|2dA(w) −→0
as m, n →+∞with n = m+O(1), which amounts to the assertion of the lemma.
□
As in the proof of the Theorem 2.11 in [2], we may now conclude the follow-
ing.
Theorem 3.4. Fix z ∈De and a bounded continuous function g on C. Then
Z
C
g(w)B⟨z⟩
m,n,q(w)dA(w) →
Z
C
g(w)dω(w, z, D∗),
as m, n →+∞with n = m + O(1). Here, dω(w, z, D∗) is harmonic measure with respect
to the point z and the domain De.
The Polyanalytic Ginibre Ensembles
21
