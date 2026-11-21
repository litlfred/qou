---
doc_id: arxiv-math-9201302v1
doc_title: "The Quantum G 2 Link Invariant"
section_id: sec-005-24-two-other-polynomial-invariants
section_title: "Two other polynomial invariants"
section_number: 2.4
pages: 9-11
source_pdf: 9201302v1.pdf
source_sha256: 67987dd432f58488
toc_source: inferred
doc_brief: "The Quantum G_2 Link Invariant — We derive an inductive, combinatorial deﬁnition of a polynomial-valued regular isotopy invariant of links and tangled graphs."
---
Two other polynomial invariants
We can repeat the approach of Section 2.3 two more times by changing the notion of a freeway and picking
a new Ansatz. To avoid confusion, let us deﬁne a G2 freeway to be what we previously called a freeway.
The solutions will be polynomial invariants of a single variable. However, for the purpose of a uniform
treatment of all of the invariants, it is desirable in general to make this variable a certain root of a variable
q which will be reused for each of the invariants. Therefore the ﬁnal answers will be elements of the ﬁeld
C(q, q1/2, q1/3, q1/4, . . . ). For every rational number a we distinguish a power qa of the indeterminate q in
such a way that for every integer n, qan = (qa)n.
We deﬁne an A2 freeway to be an oriented planar graph with crossings and junctions that look like this:
We assume the existence of a regular isotopy invariant ⟨·⟩A2 which satisﬁes the 1,0,1,1,2 Ansatz: The acyclic,
crossingless A2 freeways with 0,1,2,3, or 4 endpoints are assumed to be bases for their respective spanning
spaces. This Ansatz, although simpler, comes with some technicalities. In the 2-endpoint case, one endpoint
must be oriented inward and the other outward. In the 4-endpoint case, two endpoints must be oriented
inward and two outward, and we get two diﬀerent bases which diﬀer in the ordering of the endpoints in the
projection:
or
The two possible boundaries are equivalent, but not canonically, so there is no canonical formula for a change
of basis. The endpoints of a 3-endpoint freeway must all be oriented inward or all outward, but in fact the
3-endpoint case of the Ansatz is not needed in the derivation of the invariant. The 1-endpoint case is even
less relevant to the derivation because there are no A2 freeways whatsoever with only 1 endpoint.
By a derivation similar to that of Section 2.3, the only possibilities for ⟨·⟩A2 are the ones described by
Theorem 1.2. As before, the rules given in the theorem suﬃce as an recursive deﬁnition because any trivalent
planar graph must have a face with at most 5 sides, except the situation is simpler because all faces of an
A2 freeway must have an even number of sides. The invariant ⟨·⟩A2 is identically equal to RTA2 if all edges
are colored with the 3-dimensional representation V1,0. The edges are oriented because the representation is
not self-dual. The invariant is a special case of the HOMFLY polynomial with a normalization that makes
it a regular isotopy invariant rather than an isotopy invariant:
q 1/6|
〉A2 − q -1/6|
〉A2 = (q 1/2 − q -1/2)|
〉A2
|
〉A2 = q 4/3|
〉A2
We also deﬁne a C2 freeway to be a planar graph with two kinds of edges, illustrated as double and single
edges, with junctions and crossings that look like this:
The Ansatz for ⟨·⟩C2 has a somewhat diﬀerent form. We ﬁrst assume the existence of a relation which we
call a switching relation:
|
〉C2 − |
〉C2 = k(|
〉C2 − |
〉C2)
Associated to the switching relation is a switching move:
  ⇒  
We deﬁne a switching class of C2 freeways to be an equivalence class under switching moves. We say that a
double edge of a C2 freeway is external if at least one of its vertices is an endpoint of the freeway, otherwise
the edge is internal. Then the Ansatz says that when s+2d < 8, a collection of acyclic, extended C2 freeways
with s single endpoints and d double endpoints and no internal double edges are a basis if the collection has
one representative from each switching class. The caveat about ordering of endpoints applies here just as in
the A2 case.
By a third iteration of Section 2.3, the only possibilities for ⟨·⟩C2 are those of Theorem 1.3. To show that
these rules suﬃce as an inductive deﬁnition, we deﬁne the angles of a (trivalent) junction to be 3π/4, 3π/4,
and π/2, like so:
135
135
We deﬁne the curvature of a face to be 2π minus the sum of the exterior angles. By an Euler characteristic
argument, every crossingless C2 freeway without boundary must have a face with positive curvature, and
such a face can be reduced by the switching move to one for which one of the other moves applies.
Another approach to the C2 bracket is to deﬁne an extended C2 freeway to be one which can also
have tetravalent vertices with no incident double edges. A tetravalent freeway is one with no double edges
whatsoever. We assume the existence of a relation:
|
〉C2 = |
〉C2 − |
〉C2
where the constants α and β are arbitrary except that α must be non-zero to avoid degeneracy. If we interpret
the four angles at a tetravalent vertex to be 90 degrees, we can derive recurrence rules for tetravalent freeways
by reducing faces with positive curvature, namely faces with at most 3 sides. A face with n sides now has 2n
endpoints, and for n = 0, 1, 2, 3 the number of acyclic tetravalent graphs with 2n endpoint is 1,1,3, and 14.
But by the Ansatz for the C2 bracket, these acyclic graphs must be a basis provided that α̸ = 0. Thus we
obtain an example of a linearly recurrent theory for tetravalent graphs; double edges and trivalent vertices
are avoided. (Note that a tetravalent vertex should not be confused with a crossing.) Moreover, some of the
choices of the constants α and β result in a simpler recurrent calculus than others. A particularly fortuitous
choice is α = 1/2 and β = 1/2, whose ﬁrst advantage is a simpler relationship between the trivalent and
tetravalent theories:
|
〉C2 − |
〉C2 = (q -1/2 − q 1/2)(|
〉C2 − |
〉C2)
|
〉C2 = q 5/2|
〉C2
|
〉C2 − |
〉C2 = (q − q -1)(|
〉C2 + |
〉C2)
|
〉C2 = q 4|
〉C2
Its second advantage is that in the recurrence relations, the coeﬃcients of 1 of the acyclic graphs with 4
endpoints and 10 of the acyclic graphs with 6 endpoints vanish. The resulting recurrence relations are those
given in the second half of the statement of Theorem 1.3.
Question 2.3. Currently the tetravalent C2 bracket, for various values of α and β, merely represents exam-
ples of linearly recurrent invariants that satisfy the 1,1,3,14 Ansatz. What are all the invariants of tangled
tetravalent graphs that satisfy this Ansatz?
The C2 bracket constitutes two special cases of the Kauﬀman polynomial, one for plain edges and one
for double edges. The two relations it satisﬁes, both in “Dubrovnik” form, are:
(Figure 27)
