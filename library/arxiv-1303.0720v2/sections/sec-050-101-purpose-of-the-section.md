---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-050-101-purpose-of-the-section
section_title: "Purpose of the section"
section_number: 10.1
pages: 37-40
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
toc_source: outline
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
Sections 7 (see especially Remark 7.6) and 9 to form asymptotic expressions for Bergman’s ﬁrst
and second metric (see Section 3) in the context of ω = e−2mQ. We will generally assume that
the assumptions of Theorem 9.3 are fulﬁlled, so that the local analysis of Section 7 gives the
global weighted bianalytic Bergman kernel with high precision.
38
ANTTI HAIMI AND HAAKAN HEDENMALM
10.2. Bergman’s ﬁrst metric. Our starting point is the abschnitt b⟨2,k⟩with k = 0:
(10.2.1)
b⟨2,0⟩= m2b2
0 + mb2
1 = −4m2
π |z −w|2[λ(z, w)]2 + m
 4
πλ(z, w) −2
π(¯z −¯w) ¯∂wλ(z, w)
+ 2
π(z −w)∂zλ(z, w) −3
π|z −w|2∂z ¯∂wλ(z, w) + 2
π|z −w|2 [∂zλ(z, w)][ ¯∂wλ(z, w)]
λ(z, w)

,
where we used the formulae (7.9.7) and (7.9.21), and recall the notational convention λ(z, w) =
∂z ¯∂wQ(z, w). The lift of the abschnitt is easily obtained by inspection of (10.2.1):
(10.2.2)
E⊗2[b⟨2,0⟩](z, z′; w, w′) = −4m2
π (z −w′)(¯z′ −¯w)[λ(z, w)]2
+ m
 4
πλ(z, w) −2
π(¯z′ −¯w) ¯∂wλ(z, w) + 2
π(z −w′)∂zλ(z, w)
−3
π(z −w′)(¯z′ −¯w)∂z ¯∂wλ(z, w) + 2
π(z −w′)(¯z′ −¯w)[∂zλ(z, w)][ ¯∂wλ(z, w)]
λ(z, w)

,
The double diagonal restriction to z = w and z′ = w′ is then (since λ(z, z) = ∆Q(z))
(10.2.3)
E⊗2[b⟨2,0⟩](z, z′; z, z′) = 4m2
π |z −z′|2[∆Q(z)]2 + m
 4
π∆Q(z) + 4
π Re[(z −z′)∂∆Q(z)]
+ 3
π|z −z′|2∆2Q(z) −2
π|z −z′|2 | ¯∂∆Q(z)|2
∆Q(z)

.
As K⟨k⟩
2,m(z, w) = b⟨2,k⟩(z, w)e2mQ(z,w), it follows that
(10.2.4)
E⊗2[K⟨0⟩
2,m](z, z′; z, z′) = e2mQ(z)E⊗2[b⟨2,0⟩](z, z′; z, z′).
We conclude that
(10.2.5)
e−2mQ(z)E⊗2[K⟨0⟩
2,m](z, z + ǫ; z, z + ǫ) = E⊗2[b⟨2,0⟩](z, z + ǫ; z, z + ǫ)
= 4m2
π |ǫ|2[∆Q(z)]2 + m
 4
π∆Q(z) −4
π Re[ǫ∂∆Q(z)] + 3
π|ǫ|2∆2Q(z) −2
π|ǫ|2| ¯∂∆Q(z)|2
∆Q(z)

.
Next, we rescale the parameter ǫ to ﬁt the typical local size m−1/2:
(10.2.6)
ǫ =
ǫ′
[2m∆Q(z)]1/2.
Then, in view of (10.2.5),
(10.2.7)
e−2mQ(z)E⊗2[K⟨0⟩
2,m](z, z + ǫ; z, z + ǫ) = 2m
π (2 + |ǫ′|2)∆Q(z) + O(m1/2).
It is possible to extend the assertion of Theorem 9.3 to the lift E⊗2[K2,m] in place of the kernel
itself; this requires a nontrivial argument.
Basically, what is needed is to know that the
expressions ¯∂zK2,m(z, w), ∂wK2,m(z, w), and ¯∂z∂wK2,m(z, w) are all suitably approximated by the
corresponding expression where the kernel K2,m(z, w) is replaced by the approximate kernel
K⟨0⟩
2,m(z, w). We should say some words on how this may be achieved. First, we observe that
(9.3.6) and (9.6.2) say that the three functions
K⟨k⟩
2,m(·, w)χ0,
P2,m[K⟨k⟩
2,m(·, w)χ0],
K2,m(·, w),
ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS
39
are all close to one another in L2(Ω, e−2mQ) for w ∈D(z0, 1
3r). Furthermore, the associated error
terms may be written out explicitly, and it is possible to check that the ∂w-derivatives of the
above three kernels remain close to one another. In particular,
∂wK⟨k⟩
2,m(·, w)χ0
and
∂wK2,m(·, w)
are close to one another for w ∈D(z0, 1
3r):

∂w[K⟨k⟩
2,m(·, w)χ0 −K2,m(·, w)]

m = O(m−k−1
2 emQ(w)),
w ∈D(z0, 1
3r).
Next, we observe that
I⟨k⟩
2,m[K2,m(·, z)](w) = P2,m
h
K⟨k⟩
2,m(·, w)χ0
i
(z) =
D
K⟨k⟩
2,m(·, w)χ0, K2,m(·, z)
E
m;
the analogue of (9.2.3) then reads
(10.2.8)

 ¯∂z∂wK2,m(z, w) −¯∂z∂wK⟨k⟩
2,m(z, w)

 ≤

D
∂zK2,m(·, z), ∂w[K⟨k⟩
2,m(·, w)χ0 −K2,m(·, w)]
E
m

+

 ¯∂zP⊥
2,m[∂wK⟨k⟩
2,m(·, w)χ0](z)

,
for z, w ∈D(z0, 1
3r). Here, P⊥
2,m := I −P2,m is the projection onto the orthogonal complement.
It is clear how to handle the ﬁrst term on the right-hand side of (10.2.8) by using the above-
mentioned estimate combined with Proposition 8.2 (which lets us to control ∥∂zK2,m(·, z)∥m). The
last term is easily controlled by applying (9.6.2) together with Proposition 8.2, as the function
P⊥
2,m[∂wK⟨k⟩
2,m(·, w)χ0]
is bianalytic in D(z0, 2
3r) (for ﬁxed w). In conclusion, (10.2.8) leads to
¯∂z∂wK2,m(z, w) = ¯∂z∂wK⟨k⟩
2,m(z, w) + O(m−kemQ(z)+mQ(w)),
z, w ∈D(z0, 1
3r),
as desired. The remaining approximate identities – for ¯∂zK2,m(z, w) and ∂wK2,m(z, w) – are more
straightforward, and therefore left to the reader.
It then follows that in the context of Theorem 9.3, we have from (10.2.5) that
(10.2.9)
e−2mQ(z)E⊗2[K2,m](z, z + ǫ; z, z + ǫ) = 2m
π (2 + |ǫ′|2)∆Q(z) + O(m1/2),
for z ∈D(z0, 1
3r), and Bergman’s ﬁrst metric, suitably rescaled, becomes asymptotically (with
ω = e−2mQ)
(10.2.10)
ds③
2,ω,ǫ(z)2
2m∆Q(z) = e−2mQ(z)E⊗2[K2,m](z, z+ǫ; z, z+ǫ)
|dz|2
2m∆Q(z) =
n
π−1(2+|ǫ′|2)+O(m−1/2)
o
|dz|2;
cf. (3.3.4). In matrix form (see (3.3.5)), this corresponds to a diagonal matrix with entries 2/π
and 1/π. Since Q is a rather general potential, this is a sort of universality.
10.3. Bergman’s second metric. Given that Theorem 9.3 extends to apply to the lifted kernel,
we see from (10.2.3) and (10.2.4) that
(10.3.1)
L(z, z′) = log E⊗2[K2,m](z, z′; z, z′) = 2mQ(z) + log 4m∆Q(z)
π
+ log

1 + m|z −z′|2∆Q(z) + Re[(z −z′)∂log ∆Q(z)] + |z −z′|2
3∆2Q(z)
4∆Q(z) −| ¯∂∆Q(z)|2
2[∆Q(z)]2

+ O(m−1/2).
40
ANTTI HAIMI AND HAAKAN HEDENMALM
Applying the Laplacian ∆z to (10.3.1), we should expect to obtain
(10.3.2)
∆zL(z, z′) = 2m∆Q(z) +
m∆Q(z)
[1 + m|z −z′|2∆Q(z)]2 + O(m1/2),
provided that |z −z′| = O(m−1/2) is assumed. Applying instead ∆z′ results in
(10.3.3)
∆z′L(z, z′) =
m∆Q(z)
[1 + m|z −z′|2∆Q(z)]2 + O(m1/2),
provided that |z −z′| = O(m−1/2). If instead of the Laplacian we apply ∂z∂z′, we should get that
(10.3.4)
∂z∂z′L(z, z′) =
m2(¯z −¯z′)2[∆Q(z)]2
[1 + m|z −z′|2∆Q(z)]2 + O(m1/2),
again provided |z −z′| = O(m−1/2). We conclude that Bergman’s second metric (3.4.2), suitably
rescaled, should be asymptotically given by (with ω = e−2mQ)
(10.3.5)
ds④
2,ω,ǫ(z)2
2m∆Q(z) =

1 +
4
(2 + |ǫ′|2)2 + O(m−1/2)

|dz|2 + 2 Re

[ǫ′]2
(2 + |ǫ′|2)2 + O(m−1/2)

(dz)2

,
where z′ = z + ǫ and ǫ′ is the rescaled parameter in accordance with (10.2.6).
provided
|z −z′| = O(m−1/2). As Q is a rather general potential, this appearance of the metric

1 +
4
(2 + |ǫ′|2)2

|dz|2 + 2 Re

[ǫ′]2
(2 + |ǫ′|2)2 (dz)2

in the limit may be interpreted as a kind of universality.
