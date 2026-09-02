---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables"
section_id: sec-044-multiple-point-asymptotics
section_title: "Multiple point asymptotics"
section_number: null
pages: 309-311
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
---
The asymptotic behavior of the coeﬃcients ar of a convergent Laurent expan-
sion F(z) = ∑
r∈Zd arzr in a domainD⊂ Cd is determined by certain con-
tributing points of the singular setV of F. In Chapter 9 we derived asymptotics
in the presence of smooth contributing points, whereV is locally a manifold.
In this chapter we derive asymptotics for the simplest non-smooth geometry,
whereV locally decomposes as a union of smooth sets (see Figure 10.1).
Deﬁnition 10.1 (multiple points). A pointp∈V is said to be a multiple point
ofV (or F) if there exist complex manifoldsV1,..., Vn such that
U∩V = (U∩V 1)∪···∪ (U∩V n)
for every suﬃciently small neighborhood U ofp inCd.
A taxonomy of multiple points, with examples, is described in Section 10.1
below. Combinatorial applications of generating functions whose asymptotics
are controlled by multiple points include multi-server queues (Example 10.28),
lattice points in polytopes (Example 12.28), binomial sums (Examples 10.11
Figure 10.1 A singular variety containing multiple points.
291
292 Multiple point asymptotics
and 10.69), discrete probability (Example 12.25), and lattice paths (Exam-
ple 12.26).
Exercise 10.1. Prove directly from the deﬁnition that the origin is not a multi-
ple point ofV(z2− x2− y2).
Recall from Chapter 7 that every complex algebraic variety (respectively,
its complement) has a Whitney stratiﬁcation and is locally the product of a
stratum with its normal space (respectively, its normal link). Throughout this
chapter we use n for the number of manifolds, also calleddivisors, intersecting
at a multiple point p, and k for the codimension of the stratum containing p.
Every smooth point is a multiple point withn = 1. Mirroring Deﬁnition C.14 in
Appendix C, when n≤ d we callp a transverse multiple point if the normals
to the divisors vanishing at p are linearly independent, and say the divisors
are transverse or intersect transversely if they are transverse at every point
where they intersect. Thus,n divisors intersecting transversely necessarily have
codimension k = n. No point with n > d is considered a transverse multiple
point. A complete intersection in dimension d is a stratum of codimension d,
which necessarily consists of isolated points.
One important simpliﬁcation throughout most of the chapter is the assump-
tion that the direction ˆr does not lie on a boundary between two regions of
coeﬃcient behavior.
Deﬁnition 10.2 (generic directions). Let{Sα :α∈ A} be a Whitney stratiﬁca-
tion of the varietyV. We call ˆr a generic direction if each critical point for h ˆr
in the closure Sα of a stratum Sα lies in Sα rather than in a proper substratum
Sβ⊂ Sα.
Non-generic directions occur when a critical point in a stratum “disappears”
because it enters a substratum, leading to non-uniform behavior around non-
generic directions. If a direction is generic, then Condition (2) of Deﬁnition
D.12 of a stratiﬁed Morse function will be satisﬁed because the negation of
Condition (2) implies thatp is a critical point in directionh ˆr for the stratumSβ
but it lies in the proper substratumSα. As our naming suggests, most directions
are generic.
Exercise 10.2. LetV be the variety deﬁned by the vanishing of Q(x, y) =(
1− 2
3 x− 1
3y
)(
1− 1
3 x− 2
3y
)
. Give a stratiﬁcation ofV and ﬁnd all non-generic
directions ˆr for this stratiﬁcation.
The results of Section 7.3 imply that (under mild conditions, such as having
