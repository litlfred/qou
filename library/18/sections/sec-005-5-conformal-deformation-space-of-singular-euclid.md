---
doc_id: 18
doc_title: "Combinatorial scalar curvature and rigidity of ball packings"
section_id: sec-005-5-conformal-deformation-space-of-singular-euclid
section_title: "Conformal deformation space of singular Euclidean metrics"
section_number: 5
pages: 7-8
source_pdf: 18.pdf
source_sha256: 0b7bf055085cb04b
toc_source: inferred
doc_brief: "Combinatorial scalar curvature and rigidity of ball packings — 11 sections: Front matter; Introduction; Conformal simplices"
---
Consider a closed three-dimensional manifold M 3, together with a topo-
logical triangulation T . If we equip all of the simplices of T with metrics,
so that they are isometric to geodesic simplices in E3, and, furthermore,
these metrics are compatible (which is to say that all of the gluing maps
are Euclidean isometries), M 3 acquires a metric, which is ﬂat on the com-
plement of the 1-skeleton of T . We deﬁne the solid angle Sv of (M 3, T ) at
a vertex v to be the sum of the solid angles of the simplices of T incident
to v at the vertex identiﬁed to v. The quantity 4π −Sv is a combinatorial
analogue of scalar curvature, in that it measures the diﬀerence in, on the
1According to the translator’s note in the English translation of Kovalev’s paper,
Theorem 4.3 was already known to Coxeter in the thirties.
58
DARYL COOPER AND IGOR RIVIN
one hand, the growth rate of a small ball centered at v in M 3 and, on the
other hand, the growth rate of the volume of an Euclidean ball of the same
radius.
Just as in the previous section we use the notation eij for the edge joining
adjacent vertices vi and vj of T , lij for the length of that edge, and αij for
the total cone angle at that edge.
We say that a singular Euclidean structure on (M 3, T ) is conformal, if
there exists a function r : V (T ) →R+, such that (denoting r(vi) by ri),
lij = ri + rj. Note that a conformal structure always exists, since we can
make all simplices regular and of the same size. The term “conformal”
can be justiﬁed – we think of a general conformal structure as obtained by
rescaling the “metric” of this regular one.
Let C ⊂R|V (T )| be the set of those r which correspond to all the simplices
of T being geometric and non-degenerate – it’s clear that C is an open set
in R|V (T )|. As before, we will think of geometric invariants of (M 3, T ) as
functions on C.
Let S = 
v∈V (T ) Svrv. It is clear that S = 
T ∈T ST , where ST is the
function deﬁned in section 1. It is then immediate that S is weakly concave
on C, and if in addition we restrict our attention to the slice C1 of C given
by the condition
(5.1)

ri = 1,
then ST is strictly concave.
Now, the proof of Theorem 1.4 goes through unchanged to show
Theorem 5.1. A conformal structure on (M 3, T ) cannot be deformed (ex-
cept by rescaling) while keeping the solid angles at the vertices of T ﬁxed;
that is, the set of conformal structures with prescribed solid angles is a
discrete subset of C1.
Note. The proof actually shows something a bit stronger than Theorem 5.1
– we need only keep the diﬀerences between the solid angles ﬁxed.
Remark 5.2. By the results in section 3 everything in this section, with the
exception of the preceding Note, translates essentially verbatim to the case
of hyperbolic conformal structures on M 3 (those where the simplices of T
are hyperbolic confromal simplices).
