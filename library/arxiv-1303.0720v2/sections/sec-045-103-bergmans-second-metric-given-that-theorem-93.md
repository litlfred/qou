---
doc_id: arxiv-1303.0720v2
doc_title: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS"
section_id: sec-045-103-bergmans-second-metric-given-that-theorem-93
section_title: "Bergman’s second metric. Given that Theorem 9.3 extends to apply to the lifted kernel,"
section_number: 10.3
pages: 39-40
source_pdf: 1303.0720v2.pdf
source_sha256: 389ab465e81a0667
doc_brief: "ASYMPTOTIC EXPANSION OF POLYANALYTIC BERGMAN KERNELS — We consider the q-analytic functions on a given planar domain Ω, square integrable with respect to a weight."
---
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
