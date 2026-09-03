---
doc_id: arxiv-1907.03683v4
doc_title: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND"
section_id: sec-012-31-on-the-plancherel-measure-on-partitions-the-p
section_title: "On the Plancherel measure on partitions. The Plancherel measure is a probability"
section_number: 3.1
pages: 11-12
source_pdf: 1907.03683v4.pdf
source_sha256: eb8cc2ddfc8c0739
doc_brief: "EXPLICIT DESCRIPTION OF CHRISTOFFEL DEFORMATIONS AND — Christoﬀel deformation of a measure on the real line consists of multipying this measure by a squared polynomial having its roots in R."
---
measure Pln on the set of Young diagrams of ﬁxed size n, Yn = {λ ∈Y, |λ| = n}. It is given
by
Pln(λ) = dim(λ)2
n!
,
λ ∈Yn,
where dim(λ) is the dimension of the irreducible representation of the n-th symmetric group
parametrized by λ, or equivalentely, the number of stantard Young tableaux of shape λ
(see [28] or [31]). It is well known that the poissonization of the Plancherel measure is a
determinantal point process. More precisely, let α > 0 be a positive parameter and form
the poissonized Plancherel measure Pα on Y by imposing n to have the Poisson distribution
with parameter α:
Pα(λ) = e−αα|λ|
dim(λ)
|λ|!
2
,
λ ∈Y.
For λ ∈Y, we set
S0(λ) := {λi −i, i = 1, 2, ...} ∈Conf(Z).
Then the pushforward of Pα under the map S0, which we call the discrete Bessel point
process, is a determinantal point process with the discrete Bessel kernel
(4)
Kα(x, y) = √αJx(2√α)Jy+1(2√α) −Jy(2√α)Jx+1(2√α)
x −y
,
where the Bessel functions Jx(2√α), x ∈Z are deﬁned via their generating Laurent series
([1]):
(5)
e
√α(z−z−1) =
X
x∈Z
Jx(2√α)zx.
This deﬁnition leads to the expression
Jx(2√α) =
+∞
X
m=0
(−1)m
m!Γ(m + x + 1)αm+x/2
that can be analytically continuated for all values of the indices x ∈C. We can thus introduce
the derivatives of the Bessel functions with respect to their index
d
dxJx(2√α) =: Lx(2√α).
11
