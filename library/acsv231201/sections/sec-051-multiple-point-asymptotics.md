---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-051-multiple-point-asymptotics
section_title: "Multiple point asymptotics"
section_number: null
pages: 309-311
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
Multiple point asymptotics
The asymptotic behavior of the coeﬃcients ar of a convergent Laurent expan-
sion F(z) = P
r∈Zd arzr in a domain D ⊂Cd is determined by certain con-
tributing points of the singular set V of F. In Chapter 9 we derived asymptotics
in the presence of smooth contributing points, where V is locally a manifold.
In this chapter we derive asymptotics for the simplest non-smooth geometry,
where V locally decomposes as a union of smooth sets (see Figure 10.1).
Deﬁnition 10.1 (multiple points). A point p ∈V is said to be a multiple point
of V (or F) if there exist complex manifolds V1, . . . , Vn such that
U ∩V = (U ∩V1) ∪· · · ∪(U ∩Vn)
for every suﬃciently small neighborhood U of p in Cd.
A taxonomy of multiple points, with examples, is described in Section 10.1
below. Combinatorial applications of generating functions whose asymptotics
are controlled by multiple points include multi-server queues (Example 10.28),
lattice points in polytopes (Example 12.28), binomial sums (Examples 10.11
Figure 10.1 A singular variety containing multiple points.
291
292
Multiple point asymptotics
and 10.69), discrete probability (Example 12.25), and lattice paths (Exam-
ple 12.26).
Exercise 10.1. Prove directly from the deﬁnition that the origin is not a multi-
ple point of V(z2 −x2 −y2).
Recall from Chapter 7 that every complex algebraic variety (respectively,
its complement) has a Whitney stratiﬁcation and is locally the product of a
stratum with its normal space (respectively, its normal link). Throughout this
chapter we use n for the number of manifolds, also called divisors, intersecting
at a multiple point p, and k for the codimension of the stratum containing p.
Every smooth point is a multiple point with n = 1. Mirroring Deﬁnition C.14 in
Appendix C, when n ≤d we call p a transverse multiple point if the normals
to the divisors vanishing at p are linearly independent, and say the divisors
are transverse or intersect transversely if they are transverse at every point
where they intersect. Thus, n divisors intersecting transversely necessarily have
codimension k = n. No point with n > d is considered a transverse multiple
point. A complete intersection in dimension d is a stratum of codimension d,
which necessarily consists of isolated points.
One important simpliﬁcation throughout most of the chapter is the assump-
tion that the direction ˆr does not lie on a boundary between two regions of
coeﬃcient behavior.
Deﬁnition 10.2 (generic directions). Let {S α : α ∈A} be a Whitney stratiﬁca-
tion of the variety V. We call ˆr a generic direction if each critical point for h ˆr
in the closure S α of a stratum S α lies in S α rather than in a proper substratum
S β ⊂S α.
Non-generic directions occur when a critical point in a stratum “disappears”
because it enters a substratum, leading to non-uniform behavior around non-
generic directions. If a direction is generic, then Condition (2) of Deﬁnition
D.12 of a stratiﬁed Morse function will be satisﬁed because the negation of
Condition (2) implies that p is a critical point in direction h ˆr for the stratum Sβ
but it lies in the proper substratum Sα. As our naming suggests, most directions
are generic.
Exercise 10.2. Let V be the variety deﬁned by the vanishing of Q(x, y) =

1 −2
3 x −1
3y
 
1 −1
3 x −2
3y

. Give a stratiﬁcation of V and ﬁnd all non-generic
directions ˆr for this stratiﬁcation.
The results of Section 7.3 imply that (under mild conditions, such as having
