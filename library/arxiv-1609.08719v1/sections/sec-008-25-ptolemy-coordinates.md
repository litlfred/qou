---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-008-25-ptolemy-coordinates
section_title: "Ptolemy coordinates"
section_number: 2.5
pages: 7-8
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
Zickert oﬀer an alternative representation of the information encoded in the gluing
and cusp equations. For our purposes, their principal use is encoding information
about arbitrary representations ρ : π1(M)→ PSL(n, C). We refer the reader to
[GTZ15], [GGZ15], and present a brief overview here, specialized for the particular
case of hyperbolic 3-manifolds.
Deﬁnition 2.8. For a ﬁxed triangulation of a manifold M (with vertices labeled
0, 1, 2, 3), a Ptolemy assignment is an association of variables in C× to each
edge of each simplex satisfying equations 2.8.1 below. We denote the variable of
the ith simplex on the edge between vertices j and k as ci
jk.
If two edges are identiﬁed, their associated variables are the same. This imme-
diately implies, for example, that ci
jk =−ci
kj.
8 GILLES AND HUSTON
The Ptolemy relations are
(2.8.1) ci
03ci
12 +ci
01ci
23 =ci
02ci
13
Proposition 2.9. For a ﬁxed triangulation of a manifold M, and for any Ptolemy
assignment of this triangulation,
(2.9.1) zi =±ci
03ci
12
ci
02ci
13
where the sign is determined by an obstruction class, as described in [GGZ15] and
[GTZ15].
Since in our work we are interested only in zi, we may often assume without loss
of generality that certain ci
jk = 1, where the number of such variables depends on
the number of cusps of the manifold.
In the case ofm032 (the manifold presented above), there are only three distinct
edges, therefore three independent ci
jk variables. The Ptolemy relations are homo-
geneous degree 2 equations in two variables, and taking one of the variables to be
1 makes this a readily solvable system.
