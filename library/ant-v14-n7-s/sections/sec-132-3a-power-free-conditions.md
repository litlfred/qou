---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-132-3a-power-free-conditions
section_title: "3A. Power-free conditions"
section_number: null
pages: 255-256
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
ducible factor of F over Z (or equivalently over Q, by Gauss’s lemma) appears with multiplicity strictly
less than d. In general, given a ﬁeld k, we say that F∈ k[x1,..., xn] is d-th power-free over k when
F= cF a1
1 Fa2
2 ··· Fa𝓁
𝓁 with c∈ k×, all ai< d and all Fi∈ k[x1,..., xn] are irreducible and pairwise non-
associate. (We say G, G′∈ k[x1,..., xn] are nonassociate if there is no c∈ k× such that G= cG′.) (Note
that a constant may be regarded as a d-th power-free polynomial. In lemmas or theorems which assume a
polynomial is d-th power-free, other hypotheses will rule out the case of the polynomial being a constant.)
To be precise, we recall that the property of being d-th power-free may be speciﬁed equivalently over
a ﬁeld k or the separable closure of k:
Lemma 3.1. Let k be a ﬁeld and ks its separable algebraic closure, so ks= k if k is perfect, and in
particular if k is ﬁnite. Then for any F∈ k[x1,..., xn], F is a perfect d-th power over k (up to a nonzero
multiplicative constant) if and only if F is a perfect d-th power over ks. Similarly, F is d-th power-free
over k if and only if F is d-th power-free over k s.
Proof. We begin with the second claim. Certainly if F is d-th power-free over ks then it is over k. For the
other direction, write F= cF a1
1 Fa2
2 ··· Fa𝓁
𝓁 with c∈ k×, all ai< d and all Fi∈ k[x1,..., xn] irreducible
and pairwise nonassociate. For each such Fi, we recall from [Xu 2018, Lemma 3.15 (2)] that the fact
that Fi is irreducible over k implies that Fi is square-free as a polynomial in ks[x1,..., xn]. Thus upon
factoring Fi over ks we have Fi= Gi,1Gi,2··· Gi,bi in which each Gi, j is irreducible in ks and as j varies
the Gi, j are pairwise nonassociate. Thus the factorization of F over ks is
c(Ga1
1,1Ga1
1,2··· Ga1
1,b1)(Ga2
2,1Ga2
2,2··· Ga2
2,b2)··· (Ga𝓁
𝓁,1Ga𝓁
𝓁,2··· Ga𝓁
𝓁,b𝓁).
Next we recall from [Xu 2018, Lemma 3.15 (3)] that ifFi, Fi′∈ k[x1,..., xn] are nonassociate irreducible
polynomials, then Fi and Fi′ have no common factors in ks[x1,..., xn]. From this we conclude that
1922 Lillian B. Pierce and Junyan Xu
Gi, j and Gi′, j′ are nonassociate when (i, j)⁄=(i′, j′). Thus as i and j vary the Gi, j are all pairwise
nonassociate over ks, so that F remains d-th power-free over ks.
Finally, if F is a perfect d-th power over k then it also is over ks. In the other direction, if F is a perfect
d-th power over ks, then in the factorization above, all ai must be multiples of d, so that F factors over k
as F= cG d with G= Fa1/d
1 ··· Fa𝓁/d
𝓁 . □
