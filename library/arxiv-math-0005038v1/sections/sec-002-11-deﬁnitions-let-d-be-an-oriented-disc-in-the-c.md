---
doc_id: arxiv-math-0005038v1
doc_title: "Braid groups are linear"
section_id: sec-002-11-deﬁnitions-let-d-be-an-oriented-disc-in-the-c
section_title: "Deﬁnitions. Let D be an oriented disc in the complex plane. Fix a set"
section_number: 1.1
pages: 1-2
source_pdf: 0005038v1.pdf
source_sha256: db0b9b7a8534f161
doc_brief: "Braid groups are linear — The braid groups Bn can be deﬁned as the mapping class group of the n-punctured disc."
---
P ⊂ D consisting of n distinct points p1, . . . , pn in the interior of D. Let H(D, P )
be the group of all homeomorphisms h : D → D such that h(P ) = P and h ﬁxes
∂D pointwise. Let I(D, P ) be the group of all such homeomorphisms which are
isotopic to the identity relative to P ∪ ∂D. We deﬁne the braid group Bn to be
the group H(D, P )/I(D, P ). See [Bir74] for other equivalent deﬁnitions of these
groups and a good introduction to their basic properties.
Let C denote the space of all unordered pairs of distinct points in D \ P . In
other words,
C = ((D \ P ) × (D \ P )) \ {(x, x)}
(x, y) ∼ (y, x) .
Let d1 and d2 be distinct points in ∂D. Let c0 = {d1, d2} be a basepoint for C.
We now deﬁne a map φ from π1(C, c0) to the free Abelian group with basis {q, t}.
Let α be a closed curve in C based at c0 representing an element [ α] of π1(C, c0).
We can write α in the form
α(s) = {α1(s), α2(s)}
1991 Mathematics Subject Classiﬁcation. Primary 20F36; Secondary 57M07, 20C15.
Key words and phrases. Braid group, representation .
1
2 STEPHEN J. BIGELOW
for some arcs α1 and α2 in D \ P . Let
a = 1
2πi
n∑
j=1
( ∫
α 1
dz
z − pj
+
∫
α 2
dz
z − pj
)
.
Let
b = 1
πi
∫
α 1−α 2
dz
z .
Let φ([α]) = qatb.
This deﬁnition requires some explanation. If α1 and α2 are closed loops then a is
the sum of the winding numbers of α1 and α2 around each of the puncture points,
and b is twice the winding number of α1 and α2 around each other. However α1 and
α2 are not necessarily closed loops, but may “switch places”. In this ca se, a is the
sum of the winding numbers of the closed loop α1α2 around each of the puncture
points, and α1 − α2 satisﬁes
(α1 − α2)(1) = −(α1 − α2)(0),
which implies that b is an odd integer.
Let ˜C be the covering space of C whose fundamental group is the kernel of φ.
Choose a lift ˜ c0 of c0 to ˜C. Let Λ denote the ring Z[q±1, t±1]. The homology
group H2( ˜C) can be considered as a Λ-module, where q and t act by covering
transformations.
Let σ ∈ Bn. There is an induced action of σ on C. Let ˜σ be the lift of σ to a
map from ˜C to itself which ﬁxes ˜c0. This induces a Λ-module automorphism ˜ σ∗ of
H2( ˜C). The Lawrence-Krammer representation is the map from Bn to GL(H2( ˜C))
taking [ σ] to ˜σ∗.
