---
doc_id: arxiv-0806.2317v1
doc_title: "Bounds for codes and designs in complex subspaces Aidan Roy ∗"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: 0806.2317v1.pdf
source_sha256: c54e80d460413a5e
doc_brief: "Bounds for codes and designs in complex subspaces Aidan Roy ∗ — We introduce the concepts of complex Grassmannian codes and designs."
---
In this paper, we introduce the concept of complex Grassmann ian codes and
designs: codes and designs in the collection of ﬁxed-rank su bspaces of a complex
vector space.
In the 1970’s, Delsarte [10] developed a series of excellent bounds for certain
error-correcting codes by treating codewords as points in a n association scheme
and then applying linear programming. Shortly thereafter, Delsarte, Goethals
and Seidel [11] showed that the same technique could also be u sed on systems
of points on the real or complex unit sphere, which they calle d spherical codes
∗ email:aroy@qis.ucalgary.ca
1
and spherical designs; this resulted in important contribu tions to problems in
sphere-packing [9, Chapter 9]. This linear programming tec hnique, which is
now known as “Delsarte LP theory”, has proved surprisingly p ortable. Re-
cently, Bachoc, Coulangeon and Nebe [3] generalized the res ults of Delsarte,
Goethals and Seidel to real Grassmannian spaces, and Bachoc [2] pointed out
that “the same game” can be played over the complex numbers. I n this paper,
we investigate more closely the case of complex Grassmannia n codes.
The motivation for studying complex Grassmannians comes fr om the the-
ory of quantum measurements. Roughly speaking, any complex Grassmannian
1-design deﬁnes a projective measurement in the theory of qu antum mechanics.
It has recently been discovered that complex projective 2-d esigns correspond
to quantum measurements that are optimal for the purposes of nonadaptive
quantum state tomography [21]. In fact, this is also true in t he more gen-
eral Grassmannian setting: complex Grassmannian 2-design s are the optimal
choices of measurements for nonadaptive quantum state tomo graphy when the
observer only has access to measurements with a restricted n umber of outcomes.
More details will appear in a paper by Godsil, R¨ otteler, and the author [13].
Complex Grassmannians also play a role in certain wireless c ommunication
protocols [1].
Deﬁne Gm,n to be the set of m-dimensional subspaces of an n-dimensional
complex vector space. Without loss of generality, we will al ways assume m ≤
n/ 2. Usually, we will represent a subspace a by its n × n projection matrix Pa.
The inner product on Gm,n is the trace inner product for projection matrices:
⟨a, b ⟩ := tr(P ∗
a Pb)
= tr(PaPb).
Since ⟨a, b ⟩ = ⟨b, a ⟩, the inner product is real. This is a measure of separation,
or distance, between two subspaces—note that is not a distan ce metric per se:
the inner product of Pa with itself is maximal rather than minimal. However,
the chordal distance [8], deﬁned by
dc(Pa, P b) :=
√
m − tr(PaPb),
is a monotonic function of the inner product. Given a ﬁnite se t of inner product
values A, an A-code is a subset S of Gm,n such that
A = {tr(PaPb) : a, b ∈ S, a ⁄= b}.
An s-distance set is an A-code with |A| = s. This generalizes the concept of
an s-distance set on the complex unit sphere: if u and v are unit vectors, then
2
their separation distance on the unit sphere is a function of
|u∗v|2 = tr(uu∗vv∗).
We are interested in codes of maximal size for a ﬁxed A or s, and bounds on
their size based on zonal polynomials. Table 1 in Section 6 gi ves a summary of
the bounds for small |A|.
The outline of this paper is as follows. In Section 2, we descr ibe the orbits
of pairs of subspaces in Gm,n under the action of U (n): these orbits play a
signiﬁcant role in the bounds derived later on. In Sections 3 , 4 and 5, we develop
the necessary representation theory background needed for our LP bounds.
In particular, we discuss the decomposition of the square-i ntegrable functions
on Gm,n into irreducible representations of U (d), and the zonal polynomials
for these representations. The results in this section are a ll known, and the
development is quite similar to that of Bachoc, Coulangeon a nd Nebe for real
Grassmannians. In fact, the complex case is actually easier than the real case,
because representations of the unitary group U (n) are easier to describe than
representations of the orthogonal group O(n). In Section 6, we develop absolute
and relative bounds for codes, and show how these bounds for Gm,n reduce to
known bounds for complex spherical codes when m = 1. These bounds are
compared to some other known bounds for subspaces in Section 7. In Section 9,
we consider Grassmanian designs. Grassmannian codes enjoy a form of duality
with complex Grassmannian designs, very similar to real Gra ssmannian codes
or spherical codes. In Section 8, we give examples in which th e bounds are
tight. In many cases codes of maximal size or designs of minim al size have the
structure of an association scheme, which we describe in Sec tion 10.
