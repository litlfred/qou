---
doc_id: erlijman-wenzl-pjm-231-2
doc_title: "Subfactors from braided C* tensor categories"
section_id: sec-006-6-examples
section_title: "Examples"
section_number: 6
pages: 36-40
source_pdf: erlijman-wenzl-pjm-231-2.pdf
source_sha256: 1ee590e6f087b681
toc_source: inferred
doc_brief: "Subfactors from braided C* tensor categories — 10 sections: Front matter; Bimodules; Categories"
---
6A. Examples of C∗-tensor categories. (1) The easiest example for our set-up is
the representation category Rep(G) of ﬁnite-dimensional unitary representations
of a ﬁnite group. In order to avoid degenerate trivial cases, we take for X in our
construction an object such that some tensor power of it contains the whole group
ring CG as a subobject. For example, for G a ﬁnite cyclic group, we could take
the direct sum of the trivial and of a faithful one-dimensional representation. For
these examples, the braiding structure is just given by the permutation of tensor
factors, which commutes with the group action. This makes the S-matrix a rank 1
matrix, meaning it is noninvertible unless G is trivial. However, at least in principle,
the dual principal graph can be computed from a general result about ﬁxed point
algebras of a group K and its subgroup H. In our setting, K = Gs and H ∼= G,
which is embedded by g ∈G 7→(g, g, . . . , g) (s times). See [Kosaki et al. 1997]
for details.
In the special case when the subgroup K is normal, we obtain principal and dual
principal graphs of the factor group H/K. This is the case in our setting if G is
abelian.
(2) Let ρ be a II1 factor representation of the inﬁnite braid group B∞such that
the Jones index for the inclusion of factors ρ(B2,∞)′′ ⊂ρ(B∞)′′ is ﬁnite. Let us
deﬁne An = ρ(Bn+1,∞)′ ∩ρ(B∞)′′ (recall that ﬁnite index implies that the relative
commutant is ﬁnite-dimensional). We moreover assume that there exists, for some
k ∈N, a projection p ∈Ak such that pρ(B∞)′′ p = pρ(Bk+1,∞)′′. It is possible to
SUBFACTORS FROM BRAIDED C∗TENSOR CATEGORIES
395
deﬁne from this a C∗-tensor category, with the objects being the projections in An.
Most of this has already been done in [Wenzl 1993], Section 2, without mentioning
categories. We shall not do this here. We just remark that the constructions of this
paper will work in this setting without explicitly exhibiting the category; this has
already been done in [Erlijman 2001]. In particular, this can be applied to the Jones
subfactors as well as to the Hecke algebra and BCD type subfactors.
(3) Let Uqg be the Drinfeld–Jimbo deformation of the universal enveloping algebra
Ug of a semisimple Lie algebra g. It is well-known that the category of its ﬁnite-
dimensional representations has a braiding structure. It can not be unitarized except
for q = 1. If q is a root of unity̸ = 1, one can deﬁne a special class of represen-
tations called tilting modules which again forms a braided tensor category. It can
be shown that the category of tilting modules has a semisimple quotient with only
ﬁnitely many simple modules up to equivalence; this is often referred to as a fusion
category (see [Andersen 1992],[Andersen and Paradowski 1995]). Moreover, for
q being certain roots of unity (usually of the form q = e±2πi/l for suitable integers
l (see [Wenzl 1998] for precise values), this quotient can be unitarized. This yields
a large and important class of C∗tensor categories. Using the one-sided subfactor
construction, one obtains the Jones subfactors for X being the Uqsl2-analog of
the 2-dimensional representation of sl2. Similarly, Hecke algebra subfactors and
BCD type subfactors can be obtained from fusion categories of quantum groups of
classical Lie types.
These C∗-fusion categories can also be obtained by a completely different con-
struction using the category of positive energy representation of a loop group. The
difﬁculty in this construction comes from the fact that one can not use the usual
tensor product for representations; instead one has to deﬁne a new, so-called fusion
tensor product (see [Wassermann 1998]).
(4) Let N ⊂M be an inclusion of II1 factors with ﬁnite index and ﬁnite depth.
Then the category of N–N bimodules obtained as direct sums of summands of the
bimodules
M⊗n = M ⊗N M ⊗N · · · ⊗N M
(n times), n ∈N deﬁnes a C∗-tensor category which may or may not be braided.
One can similarly also deﬁne the C∗-tensor category of M-M bimodules generated
by M⊗n.
If these categories are not braided, one can apply a general construction, called
the categorical quantum double construction to construct from our category of bi-
modules a larger braided C∗tensor category. It was shown that this category is
equivalent to the category of M–M-bimodules for the asymptotic inclusion N ⊂M
derived from N ⊂M; see [M¨uger 2003]. If the original category already was
396
JULIANA ERLIJMAN AND HANS WENZL
braided, the asymptotic inclusion coincides with the 2-sided inclusion constructed
in this paper.
(5) Our constructions of bimodules in this paper are based on certain endomor-
phisms of II1 factors. The approach to categories via endomorphisms has been
used for a long time for type III factors in the framework of algebraic quantum
ﬁeld theory (see [Longo and Roberts 1997; Fredenhagen et al. 1989; Xu 2000], for
example). Here subtleties involving coupling constants do not matter, and objects
are given directly by morphisms.
6B. Examples for our construction. (1) We ﬁrst list examples of C∗-tensor cate-
gories with invertible S-matrix.
(a) The S-matrix for the full fusion tensor categories as constructed in [Andersen
1992],[Andersen and Paradowski 1995] is invertible under the conditions for uni-
tarizability, as stated in [Wenzl 1998]. Hence if we can ﬁnd an object X such that
all irreducible representation of the fusion category appear in some tensor power
of X, we have C′ = C and the dual principal graph is equal to the principal graph.
Such representations can be found in all cases, but usually can not be chosen to be
irreducible. For instance, for Lie type A (the case of Jones subfactors and Hecke
algebra subfactors), one can choose X = 1⊕V , where V is the analog of the vector
representation.
(b) Similarly, the S-matrix for the quantum double of a C∗tensor category is always
invertible (see [M¨uger 2003], for instance). Hence, as soon as we have found an
object X for which all irreducible representations of the double category appear
in some tensor power of X, the dual principal graph of our s-sided inclusion with
respect to X is equal to the principal graph.
(2) It turns out that our construction not only depends on the category C, but also
on the choice of the object X. Even though in the case of the fusion tensor cate-
gories the S-matrix for C is invertible, the S matrix for the category C′ may not
be invertible. For instance, for type A if one takes X = V , the S-matrix for C′ is
invertible only if the degree of the root of unity is coprime to k. If this is not the
case, however, our results for noninvertible S-matrices apply. This will be shown
in more detail in the following subsection at an example.
6C. Subfactors related to Jones subfactors. We illustrate our examples in some
detail for the fusion category C of Uqsl2, with q = e2πi/l. There also exist other,
more elementary methods to construct these categories using the Temperley–Lieb
algebras; see [Turaev 1994], for example. As mentioned before, this is also one
of the cases where the subfactor constructions can be done on the level of braid
representations, as it was carried out in the original paper [Erlijman 2001].
SUBFACTORS FROM BRAIDED C∗TENSOR CATEGORIES
397
We give a brief description of this category. Up to isomorphism, we have exactly
l−1 simple objects in C, which are denoted by [i], 1≤i ≤l−1. The decomposition
of tensor products is given by
(6-1)
[i] ⊗[ j] = [|i−j| + 1] ⊕[|i−j| + 3] ⊕· · · ⊕[m],
where m is the minimum of i + j −1 and 2l −1 −i −j. One sees easily that
[1] corresponds to the trivial object. It follows from the tensor product rules by
induction on n that all simple objects in [2]⊗n are labeled by even numbers if n is
odd, and by odd numbers if n is even. Hence k = 2 and the simple objects of C′ are
labeled by odd numbers. This explicitly describes the principal graph for N ⊂M,
constructed with X = [2], by Theorem 4.6.
Observe that [i] ⊗[l −1] = [l −i] for all 1 ≤i < l. Hence the objects [1] and
[l −1] together with the operation ⊗form a group G which is isomorphic to Z/2Z.
Moreover, the S matrix is well-known to be of the form S = (sin(i jπ/l)), up to a
scalar.
It is very easy to check that if l is even, then sin(i(l −1)π/l) = sin(iπ/l) for
any odd i = 1, 3, . . . ,l −1. Hence the category T contains at least the objects [1]
and [l−1]. It contains no more simple objects as obviously sin(iπ/l) = sin(i jπ/l)
for 1 < j < l only if j = l −1. So the conditions at the beginning of Section 5B
are satisﬁed with |G| = 2 = k. We have shown most of the following
Proposition 6.1. Let N⊂M be the subfactor constructed from the s-sided inclusion
from the Jones subfactor at an l-th root of unity, with l even. Then we have
(a) The even vertices of the principal graph are labeled by all s-tuples of odd
positive numbers less than l and the odd vertices are labeled by all odd pos-
itive numbers less than l. The number of edges between two vertices can be
computed from the tensor product rule stated in (6-1).
(b) Each s-tuple of positive integers less than l whose sum is even and which con-
tains the number l/2 at most once labels an even vertex of the dual principal
graph; the number of edges emanating from such a vertex can be computed as
in (a). The M–M bimodules M⃗λ labeled by an s-tuple⃗λ containing the number
l/2 exactly r > 1 times satisﬁes dim(End(M⃗λ)) = 2r−1.
Proof. Part (a) follows from Theorem 4.6 and our explicit description of the simple
objects of C′. For part (b), we have already checked the conditions stated at the
beginning of Section 5B. It remains to calculate StabGs
1⃗λ for any⃗λ∈3s. Recall that
the action of the nontrivial element of G on our labeling set is given by i 7→l −i.
Obviously, the only ﬁxed point is l/2 for l odd. It is now not hard to show that⃗
λ ∈3s has a nontrivial stabilizer in Gs
1 if and only if r ≥2 of its components
are equal to l/2, and that in this case the stabilizer has exactly 2r−1 elements.
Statement (b) now follows from Theorem 5.9.
□
398
JULIANA ERLIJMAN AND HANS WENZL
Remark 6.2. If s = 3, part (b) of the last proposition completely determines the
number of edges in the dual principal graph except for the decomposition of the
bimodule M⃗λ with⃗λ = (l/2,l/2,l/2), which could decompose into the direct sum
of four nonisomorphic irreducible M–M bimodules or into the direct sum of two
isomorphic irreducible M–M bimodules.
