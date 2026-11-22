---
doc_id: s10955-022-02992-6
doc_title: "Cluster Expansions: Necessary and Sufficient Convergence Conditions"
section_id: sec-006-23-hard-core-systems-in-the-continuum
section_title: "Hard-Core Systems in the Continuum"
section_number: 2.3
pages: 11-12
source_pdf: s10955-022-02992-6.pdf
source_sha256: aa73d797a89eaf06
toc_source: outline
doc_brief: "Cluster Expansions: Necessary and Sufficient Convergence Conditions — We prove a new convergence condition for the activity expansion of correlation functions in equilibrium statistical mechanics"
---
Let K ′ be the collection of non-empty compact subsets of Rd, equipped with the Hausdorff
distance and Borel σ-algebra [19, Chapter I-4], and X ⊂K ′ a non-empty measurable subset.
Here we want to additionally assume that X consists of bounded convex sets that are non-
empty and regular closed, i.e., that are equal to the closure of its non-empty interior. Notice
that such sets are compact and have ﬁnite positive Lebesgue measure that is equal to the
Lebesgue measure of their interior. In practice X will consist of easily described subsets. For
example, when dealing with closed balls Br(x) ⊂Rd we may identify X with Rd × R+.
Consider the hard-core interactions given by the potential v(X, Y) := ∞1l{X∩Y̸ =∅}, Mayer’s
f function then is
f (X, Y) = −1l{X∩Y̸ =∅}.
Clearly the function is well-deﬁned for general subsets X, Y ⊂Rd that are not necessarily
in X, the domains of deﬁnition of the functions ϕT
n and ψn,n+k extend accordingly.
For D ⊂Rd and a measure λz on X deﬁned as in (2.3), consider the formal series
T (D; z) := 1 +
∞

k=1
1
k!

Xk ϕT
1+k(D, Y1, . . . , Yk)λk
z(dY).
(2.14)
As is well-known [6, Eq. (3.12)]
T (D; z) = exp

−
∞

k=1
1
k!

Xk 1l{∃i: Yi∩D̸=∅}ϕT
k(Y1, . . . , Yk)λk
z(dY)

(2.15)
on the level of formal power series.
Moreover, if the domain D can be written as a ﬁnite union of disjoint objects Xi ∈X, say
D = X1 ∪. . . ∪Xn for n ∈N, then the identity
1 +
∞

k=1
1
k!

Xk ϕT
1+k(D, Y1, . . . , Yk)λk
z(dY)
=
∞

k=0
1
k!

Xk ψn,n+k(X1, . . . , Xn, Y1, . . . , Yk)λk
z(dY)
holds by Lemma 3.8 below and we recognize that the series T (D, z) provide expansions for
the reduced correlation functions in the sense that
ρn(X1, . . . , Xn; z) = z(X1) · · · z(Xn)1l{X1,...,Xn disjoint} T (X1 ∪· · · ∪Xn; z).
The absolute convergence of the expansions ρ(z) for the correlation functions is implied by
the absolute convergence of T (D; z), i.e., by the pointwise convergence
1 +
∞

k=1
1
k!

Xk |ϕT
1+k(D, Y1, . . . , Yk)|λk
z(dY) < ∞,
for all domains D that are unions of ﬁnitely many objects Xi ∈X.
Assume we are given a systematic way to chop up the objects X ∈X into smaller bits
and pieces, called snippets (think: analogous to representing a polymer as a collection of
33
Page 12 of 47
S. Jansen, L. Kolesnikov
