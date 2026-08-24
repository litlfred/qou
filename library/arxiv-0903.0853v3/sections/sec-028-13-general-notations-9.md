---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-028-13-general-notations-9
section_title: "GENERAL NOTATIONS 9"
section_number: 1.3
pages: 15-16
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
forms of them.
In chapter 5, we shall use:
(1.2) θ(z;q) :=
∑
n∈Z
q−n(n−1)/2zn =
∏
n∈N
(1−q−n−1)(1 +q−nz)(1 +q−n−1/z).
The second equality is Jacobi’s celebrated triple product f ormula. When ob-
vious, the dependency in q will be omitted and we shall write θ(z) instead of
θ(z;q). One has:
θ(qz) =q z θ(z) and θ(z) =θ(1/qz).
In chapter 6, we shall rather use:
(1.3) θq(z) :=
∑
n∈Z
q−n(n+1)/2zn =
∏
n∈N
(1−q−n−1)(1 +q−n−1z)(1 +q−n/z).
One has of course θq(z) =θ(q−1z;q) and:
θq(qz) =zθq(z) =θq(1/z).
Both functions are analytic over the whole of C∗ and vanish on the discrete
q-spiral−qZ with simple zeroes.
In chapter 7, we shall use in alternance both forms, accordin g to which ﬁts
better the needs of the computation. Indeed, in section 7.4, we shall even use
the “classical” forms θi,j, i,j ∈{ 0, 1} to be found in the standard theory of
special functions.
1.3.2. q-Gevrey levels. — As in [7],[36], we introduce the space of formal
series of q-Gevrey order s:
C[[z]]q;s :=
{∑
anzn∈ C[[z]]|∃ A> 0 : an =O
(
Anqsn2/2
)}
.
We also say that f ∈ C[[z]]q;s is of q-Gevrey level 1/s. It understood that
C[[z]]q;0 = C{z} and C[[z]]q;∞ = C[[z]]. Note however that it is not true that⋂
s>0
C[[z]]q;s = C{z}, as shows the example of the classical Euler series∑ n!zn,
which belongs to the former but not to the later (and the same i s true for any
divergent series having a ﬁnite Gevrey level in the sense of the classical theory
of ordinary diﬀerential equations); nor that ⋃
s>0
C[[z]]q;s = C[[z]], as shows the
example of∑ nnzn, which belongs to the latter but not to the former.
