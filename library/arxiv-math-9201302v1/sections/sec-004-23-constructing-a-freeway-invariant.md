---
doc_id: arxiv-math-9201302v1
doc_title: "The Quantum G 2 Link Invariant"
section_id: sec-004-23-constructing-a-freeway-invariant
section_title: "Constructing a freeway invariant"
section_number: 2.3
pages: 6-9
source_pdf: 9201302v1.pdf
source_sha256: 67987dd432f58488
toc_source: inferred
doc_brief: "The Quantum G_2 Link Invariant — We derive an inductive, combinatorial deﬁnition of a polynomial-valued regular isotopy invariant of links and tangled graphs."
---
Constructing a freeway invariant
We assume that there is a scalar freeway invariant ⟨·⟩G2 whose corresponding vector invariant is | ·⟩G2 and
which satisﬁes the following condition: For n < 6, the bracket of the acyclic, crossingless freeways with n
endpoints are linearly independent vectors, and that the bracket of a freeway which consists of a face with
n sides is a linear combination of these acyclic freeways. These freeways are precisely the ones listed in the
statement of Theorem 1.1. Thus, we assume the existence of coeﬃcients a, b, c, d1, d2, e1, and e2 as given
in the statement of Theorem 1.1 (but we do not yet assume the formulas given for those coeﬃcients).
We call this assumption the 1,0,1,1,4,10 Ansatz because there are 1,0,1,1,4, and 10 acyclic freeways with
0,1,2,3,4, and 5 endpoints, respectively. Note that by symmetry there can only be two distinct coeﬃcients
for the relation for a square and pentagon, for otherwise the bracket of a square or a pentagon would satisfy
more than one linear relation, which would violate the linear independence assumption.
Theorem 2.1. Every freeway invariant which satisﬁes the 1,0,1,1,4,10 Ansatz is equal to the invariant
deﬁned in Theorem 1.1 for some value of q.
We will proceed by proving Theorem 2.1. Along the way all of the conditions for the existence of the
invariant will be met, thereby proving Theorem 1.1.
The following lemma shows that the coeﬃcients a,. . . ,e2 completely determine ⟨·⟩G2 for crossingless
freeways, provided that the coeﬃcients are chosen so that the bracket exists, up to a choice of global
normalization. As in the case of the Kauﬀman bracket, we choose for the sake of convention ⟨∅⟩G2 = 1.
Lemma 2.2. Let Z be a non-empty crossingless freeway. The graph Z has at least one simply-connected
face with ﬁve or fewer sides which does not share an edge with itself.
Proof. If we allot each face one third of each of its vertices and one half of each of its edges, then the Euler
characteristic of a simply-connected face with n sides is 1 −n/6 and the Euler characteristic of a multiply-
connected face is negative or zero. If no face shares an edge with itself, then since the Euler characteristic
of the sphere is 2, we must have at least one face with positive Euler characteristic.
Suppose instead that at least one face does share an edge with itself. Then we may draw a circle which
is inside this face except at one point:
If we draw a circle for each such face, then at least one of the circles must be innermost, i.e. it must bound
a region containing no such faces. The total Euler characteristic of the faces in this region is at least 5/6, so
once again there must be a face in the region with the desired property.
A variation of the proof of this lemma yields a self-justiﬁcation for the 1,0,1,1,4,10 Ansatz: If a crossingless
freeway has n endpoints, then either the freeway is acyclic or the total Euler characteristic of its faces is at
least 1 −n/6. If n < 6, then any freeway with n endpoints is a linear combination of acyclic freeways. The
Ansatz implies that the acyclic freeways are bases for the ﬁrst six spanning spaces of the bracket.
We now derive the values for the coeﬃcients a, b, c, di, and ei which are consistent for the values of
the bracket on all crossingless freeways. Let P be a minimal crossingless freeway projection for which the
recursive deﬁnition contradicts itself. Suppose that the projection P has two faces A and B with ﬁve or
fewer sides which are not adjacent. Then reducing the face A must yield the same result as reducing the
face B, because after we reduce A we are still free to reduce B, and vice versa. Thus, the only possibility of
a contradiction arises when P has two adjacent faces with at most ﬁve sides.
Suppose, for example, that P has a triangle next to a pentagon; it suﬃces to consider the case when P
is a triangle next to a pentagon and nothing more, like so:
We can in this case reduce either the pentagon or the triangle:
|
〉G2 = c|
〉G2 = cd1(|
〉G2 + |
〉G2) + cd2(|
〉G2 + |
〉G2)
 = e1(|
〉G2 + |
〉G2 + |
〉G2 + |
〉G2 + |
〉G2)
 + e2(|
〉G2 + |
〉G2 + |
〉G2 + |
〉G2 + |
〉G2)
By the linear independence assumptions, we obtain the scalar equations:
cd1
=
e1d1 + e1c + e1b + e2
cd2
=
e1d2 + e2b
We can perform this procedure for all cases of a face with n sides adjacent to a face with m sides except
n = m = 5. We obtain the equations:
b2
=
bd1 + d2 + ad2
(1)
c2
=
bd1 + cd1 + d2
bc
=
2e1b + 2e2 + ae2 + e1c
cd1
=
d1e1 + ce1 + be1 + e2
(2)
cd2
=
d2e1 + be2
d1e1 + d2
=
e2
1
(3)
d1e1 + d2
1
=
e2
1 + ce1 + d1e1
(4)
d1e1
=
e2
1 + d1e1 + e2
(5)
d1e2 + d2c
=
e1e2 + be2 + 2d2e1
d1e2
=
e1e2 + d2e1
d1e2 + d1d2
=
e1e2 + e2c
Since we have not made any linear independence assumptions for freeways with six endpoints, we do not
obtain any equations which the coeﬃcients must satisfy a priori in the case of two neighboring pentagons.
Nevertheless, we must check the equations anyway, since the relevant freeways might be linearly independent.
Here are the equations which result:
e2d1
=
e1d2 + e1e2
e2
=
e2
1
The only remaining possibility is that there are two faces with ﬁve or fewer sides which have two or more
edges as their common border. This case is inconsequential and the reason is left as an exercise to the reader.
Undeterred by the sprawl of these equations and by the fact that there are more constraints than un-
knowns, we can proceed by reducing them to a sequence of relatively simple relations. First, we note that
one solution can be varied in an uninteresting way to obtain another: We can multiply b, c, d1, and e1 by a
constant and d2 and e2 by the square of that constant. To eliminate this degree of freedom, we normalize
by declaring that e1 = 1. (The case e1 = 0 produces only trivial solutions.) Then we can eliminate variables
by using some of the equations to simplify the algebra: We ﬁnd that e2 = −1 by equation (5), then express
d2 in terms of d1 by equation (3), then c in terms of d1 by equation (4), then we ﬁnd b by equation (2), and
ﬁnally a by equation (1). In the process we see that the other equations are satisﬁed automatically, and we
are left with a second free parameter. We make the useful reparameterization d1 = −q −q−1, with q an
indeterminate, to obtain the solutions given in the statement of Theorem 1.1.
To extend the invariant to links and to freeways with crossings, we further assume that a crossing is a
linear combination of the four acyclic, crossingless freeways with four endpoints. To ﬁnd the four coeﬃcients
f1, f2, g1, and g2 for this linear dependence, we must investigate the behavior of the bracket under the
regular isotopy moves. We ﬁrst reduce the “before” and “after” pictures of the ﬁrst regular move:
|
〉G2 = f1g1|
〉G2 + f1 2|
〉G2 + f1g2|
〉G2 + f1f2|
〉G2
 + g1 2|
〉G2 + g1f1|
〉G2 + g1g2|
〉G2 + g1f2|
〉G2
 + f2g1|
〉G2 + f2f1|
〉G2 + f2g2|
〉G2 + f2 2|
〉G2
 + g2g1|
〉G2 + g2f1|
〉G2 + g2 2|
〉G2 + g2f2|
〉G2
This yields the equations:
f1g1d1 + f 2
1 c + g2
1c + f1g1b + g1g2 + f1f2
=
0
f1g1d1 + f1g2 + f2g1
=
0
f1g1d2 + f1f2b + f 2
2 + g1g2b + g2
2 + f2g2a
=
0
f1g1d2 + f2g2
=
1
(6)
the third and fourth moves result in the equations:
f 2
1 d1 + f1g1c + g1f1e1g2
1d1
=
0
g1f1e1 + g1f2
=
f1
g1f1e1 + g2f1
=
g1
g1f1e1 + g2
1d1 + g2g1
=
0
f 2
1 d1 + f1f2 + g1f1e1
=
0
g1f1e2 + g2f2
=
0
(7)
f 2
1 d2 + f1g2b + g1f1e2 + g1g2c + g2
2
=
0
g1f1e2 + g2
1d2 + f2g1b + f2f1c + f 2
2
=
0
f 2
1 d2 + g1f1e2
=
f2
(8)
g1f1e2 + g2
1d2
=
g2
(9)
Comparing equations (6) and (7), we obtain:
f1g1 = f2g2 =
1
1 + d2
=
1
q + 2 + q−1
Multiplying equations (8) and (9) and substituting the formula (2.3), we obtain:
f 2
1 + g2
1 =
q + q−1
q + 2 + q−1
Since we now know the sum and the product of f 2
1 and g2
1, we obtain a quadratic equation. The result is
the solutions given in the statement of Theorem 1.1.
It remains to check the second regular isotopy move. As in the case of two adjacent pentagons, we do
not obtain any equations which the coeﬃcients must satisfy a priori, but we must check the move anyway.
In this case the ubiquitous trick which was left as an exercise to the reader in the case of the Kauﬀman
bracket appears again. If we have invariance under the other moves, and if a crossing is a linear combination
of crossingless freeways, then the second regular isotopy move is automatically satisﬁed.
In solving the quadratic equation we must break a Galois symmetry which maps the parameter q to q−1.
A rationale for making the choice presented here, as well as for choosing the parameter q in the ﬁrst place,
will be presented in the second part of the paper.
