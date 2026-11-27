---
doc_id: vonneumann2015
doc_title: "Von Neumann Algebras"
section_id: sec-029-116-the-normaliser-the-full-group
section_title: "The normaliser-the full group."
section_number: 11.6
pages: 83-85
source_pdf: vonNeumann2015.pdf
source_sha256: 781c6912b7d7b9a4
toc_source: inferred
doc_brief: "Von Neumann Algebras — 70 sections: Front matter; Hilbert Space; The Spectral Theorem"
---
The normaliser-the full group.
How much of G and its action on M can be recovered from M inside M ⋊G
for a free action? One thing that is canonically deﬁned is the normaliser
N(M) = {u unitary in M ⋊G|uMu∗= M} This group obviously contains
the unitary group U(M) as a normal subgroup.
There are two extreme
cases.
(i) If M is a factor. Suppose u = P
g agug is in N(M), then there is an
automorphism β of M so that ux = β(x)u
∀x ∈M. That is
X
g
agαg(x)ug =
X
g
β(x)agug
∀x ∈M
83
. So for each g ∈G we have agαgβ−1(x) = xag. By 11.2.6 there can be only
one g for which ag is diﬀerent from 0 and for that g, ag is unitary. We see
that the quotient N(M)/U(M) is in fact G itself. So we recover G and its
action (up to inner automorphisms) on M.
(ii) If M = L∞(X, µ) the situation is diﬀerent and somewhat richer. As
before, if P
g agαg(x)ug ∈N(M) there is a β such that
X
g
agαg(x)ug =
X
g
β(x)agug
∀x ∈M.
But now freeness is less strong. For a given g we have agαg(x) = β(x)ag for
all x as before. Thus on the support of ag αg(x) = β(x) for all L∞functions
x.
So if the support of ag and ah intersect in a set of non-zero measure
then, arguing as in 11.2.10 the transformations deﬁned by g and h would
agree on that set which is not allowed by freeness.
After throwing away
sets of measure zero we may thus conclude that the supports of the ag’s are
disjoint! Moreover since P
g agαg(x)ug is unitary, P
g aga∗
g = 1 so that the
ag are all characteristic functions of subsets Sg which form a partition of X.
And on Sg, the transformation determined by β agrees with αg.
We thus have the remarkable structure of the transformations of X de-
termined by N(L∞(X)):
there is a partition of X into measurable subsets, on each of which the
transformation agrees with some element of G. It is just as clear from the
above calculation that such a transformation is implemented by a unitary in
N(L∞(X)). Playing freely and easily with sets of measure zero we deﬁne:
Deﬁnition 11.6.1. If G is a discrete group of automorphisms of L∞(X, µ),
the full group of G is the group of all automorphisms T for which there is a
partition X = S
g∈G Cg into disjoint sets with T = g on Cg.
It is perhaps not immediately obvious that the full group contains any
elements besides G itself. But if G acts ergodically then every subset is spread
all over the place so a maximality argument shows that one can extend any
partially deﬁned element to an isomorphism. Note that the elements of the
full group preserve orbits under G. It can be shown that any orbit-preserving
isomorphism of G is in the full group.
84
Chapter 12
