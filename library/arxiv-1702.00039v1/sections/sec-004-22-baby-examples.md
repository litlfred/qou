---
doc_id: arxiv-1702.00039v1
doc_title: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY"
section_id: sec-004-22-baby-examples
section_title: "Baby examples"
section_number: 2.2
pages: 3-7
source_pdf: 1702.00039v1.pdf
source_sha256: b47ca7d1cf7b44be
doc_brief: "Gentle introduction to Soergel bimodules I: The basics NICOLAS LIBEDINSKY — This paper is the ﬁrst of a series of introductory papers on the fascinating world of Soergel bimodules."
---
We start with two baby examples of Coxeter systems. In these two cases (as
well as in examples (C) and (D)) we will calculate explicitly the two key ob-
jects in the theory, namely the Kazhdan-Lusztig basis and the indecomposable
Soergel bimodules.
3
(A) The group Symm(∆) of symmetries of an equilateral triangle is isomor-
phic to the group with 6 elements
⟨s,r|s2 =r2 =e, srs=rsr⟩.
One possible isomorphism is given by the map
(B) The group Symm(□) of symmetries of a square is isomorphic to the group
with 8 elements
⟨s,r|s2 =r2 =e, srsr=rsrs⟩.
One isomorphism between these groups is given by
2.3 Generalizing the baby examples: (inﬁnite) regular polygons
One natural way to generalize the baby examples is to consider the symmetries
of a regularn-sided polygon. This is also a ﬁnite Coxeter group denotedI2(n)
(the subindex 2 in this notation denotes the rank of the Coxeter system, as
deﬁned in Section 2.1). A presentation of this group is given by
(C) I2(n) =⟨s,r|s2 =r2 =e, (sr)n =e⟩,
4
so Symm(∆)∼=I2(3) and Symm(□)∼=I2(4). Again, one isomorphism here is
given by sending s to some reﬂection and r to any of the “closest reﬂections
to it”
Figure 1: Example with n = 8
What is the Inﬁnite regular polygon , the “limit” in n of the groups I2(n)? A
reasonable way to search for a geometric limit of the sequence of n−sided
regular polygons, is to picture this sequence having “the same size” as in the
ﬁgure
Figure 2: The incorrect mental image
If we do so, the (pointwise) limit is a circle. On the other hand, the limit when
n goes to inﬁnity of I2(n) is algebraically clear if we consider the presentation
given in Example (C). It is the inﬁnite group
U2 =⟨s,r|s2 =r2 =e⟩.
But the geometric and algebraic descriptions given here do not coincide! The
group Symm(©) of symmetries of the circle (usually called the orthogonal
group O(2)) is not even ﬁnitely generated. We have passed to a continuous
group! The best we can do is to seeU2 as a dense subgroup of Symm(©) (just
considers andr to be two ”random” reﬂections of the circle).
5
There is a beautiful way to solve this problem: there is a discrete geometric
limit of the sequence of n−sided regular polygons. Let us picture this se-
quence with one ﬁxed side (in the ﬁgure, the darker one). Let us suppose that
the ﬁxed side has vertices in the points (0, 0) and (0, 1) of the plane.
Figure 3: A new sequence
Then, if we make a “close up” around the darker side, and we put all the
polygons together, we see
Figure 4: The ﬁgure opens like ﬂower
The (pointwise) limit isR with the vertices converging to the setZ. The sym-
metries of this geometric object (that we call (R,Z)) is isomorphic to U2! One
isomorphism is given by sendings to the reﬂection through 0 andr to the re-
ﬂection through 1/2 (again “the closest reﬂection”). Now our geometric limit
and the algebraic limit coincide and we can regain our lost calm.
For our fourth example, we just just raise the rank ofU2.
(D) The Universal Coxeter system of rankn is the group
Un =⟨s1,s 2,...,s n|s2
1 =s2
2 =··· =s2
n =e⟩
This is the most complicated family of groups in which one can still compute
all of the Kazhdan-Lusztig theory explicitly.
6
