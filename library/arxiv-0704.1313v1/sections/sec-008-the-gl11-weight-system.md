---
doc_id: arxiv-0704.1313v1
doc_title: "Mutant knots and intersection graphs"
section_id: sec-008-the-gl11-weight-system
section_title: "The gl(1|1) weight system"
section_number: null
pages: 11-13
source_pdf: 0704.1313v1.pdf
source_sha256: a75bb39c60ec9b15
toc_source: outline
doc_brief: "Mutant knots and intersection graphs — We prove that if a ﬁnite order knot invariant does not disting uish mutant knots, then the corresponding weight system depends on the interse ction graph of a"
---
Deﬁne the (unframed) Conway graph invariant with values in the ring of polynomi-
als C[y] in one variable y in the following way. We set it equal to ( −y)n/2 on graphs
with n vertices if the adjacency matrix of the graph is nondegenerate, a nd 0 otherwise.
Recall that the adjacency matrix AG of a graph G with n vertices is an n × n-matrix
with entries in Z2 obtained as follows. We choose an arbitrary numbering of the
vertices of the graph, and the entry aij is 1 provided the i th and the j th vertices
are adjacent and 0 otherwise (diagonal elements aii are 0). Note that for odd n, the
adjacency matrix cannot be nondegenerate, hence the values ind eed are in the ring of
polynomials. The Conway graph invariant is multiplicative: its value on th e disjoint
union of graphs is the product of its values on the factors.
Clearly, the Conway graph invariant is a 4-invariant. Moreover, it sa tisﬁes the 2-
term relation, which is more restrictive than the 4-term one: its valu es on the graphs G
and ~GAB coincide for any graph G and any pair of ordered vertices A, B in it. Indeed,
consider the graph as a symmetric bilinear form on the Z2-vector space whose basis is
the set of vertices of the graph, the adjacency matrix being the m atrix of the bilinear
form in this basis. In these terms, the transformation G ↦→~GAB preserves the vector
space and the bilinear form, but changes the basis A, B, C, · · · → A + B, B, C, . . . .
Thus, it preserves the nondegeneracy property of the adjacen cy matrix.
The subspace F1 is spanned by the graph p1 with a single vertex (whence no
edges), which is a primitive element. Since F is the polynomial ring in its primitive
elements, each homogeneous space Fn admits a decomposition into the direct sum of
two subspaces, one of which is the subspace of polynomials in primitive elements of
degree greater than 1, and the other one is the space of polynomia ls divisible by p1.
We deﬁne the framed Conway graph invariant as the only multiplicative 4-invariant
with values in the polynomial ring C[c, y ] whose value on p1 is c, and on the projection
of any graph to the subspace of p1-independent polynomials along the subspace of
p1-divisible polynomials coincides with the Conway graph invariant of the g raph.
The values of the framed Conway graph invariant can be computed r ecursively.
Take a graph G and consider its projection to the subspace of graphs divisible by p1.
On this projection, the framed Conway graph invariant can be comp uted because of
its multiplicativity. Now add to the result the value of the (unframed) Conway graph
invariant on the graph. Now we can reﬁne the statement of theore m 5.
11
Theorem 6 The gl(1|1) universal weight system is the pullback of the framed Conway
graph invariant to chord diagrams under the homomorphism γ.
Proof. The proof follows from two statements in [10]. Theorem 3.6 there st ates
that setting c = 0 in the value of the gl(1|1) universal weight system on a chord
diagram we obtain the result of deframing this weight system. Theor em 4.4 asserts
that this value is exactly the Conway invariant of the chord diagram. The latter
coincides with the Conway graph invariant of the intersection graph of the chord
diagrams deﬁned above. Since the deframing for chord diagrams is a pullback of the
deframing for graphs, we are done. □
References
[1] The knot Atlas , http://katlas.math.toronto.edu/wiki/Main_Page
[2] D. Bar-Natan, On Vassiliev knot invariants , Topology, 34, 423–472 (1995)
[3] A. Bouchet Reducing prime graphs and recognizing circle graphs , Combinatorica,
7, no. 3, 243–254 (1987)
[4] A. Bouchet Circle graph obstructions , J. Combin. Theory Ser. B 60, no. 1, 107–
144 (1994)
[5] S. V. Chmutov, S. V. Duzhin, S. K. Lando Vassiliev knot invariants I. Introduc-
tion, Advances in Soviet Mathematics, vol. 21, 117-126 (1994)
[6] S. Chmutov, S. Duzhin, J. Mostovoy, CDBooK. Introduction to Vassiliev Knot
invariants. (a preliminary draft version of a book about Chord Diagrams.)
http://www.math.ohio-state.edu/~chmutov/preprints/
[7] S. V. Chmutov, A. N. Varchenko, Remarks on the Vassiliev knot invariants com-
ing from sl2, Topology 36, no. 1, 153–178 (1997)
[8] B. Courcelle Circle graphs and Monadic Second-order logic , Preprint, June 2005,
http://www.labri.fr/perso/courcell/ArticlesEnCours/CircleGraphsSubmitted.pdf
[9] W. H. Cunningham, Decomposition of directed graphs , SlAM J. Algor. Discrete
Math.,3, no. 2, 214–228 (1982)
[10] J. M. Figueroa-O’Farrill, T. Kimura, A. Vaintrob, The universal Vassiliev in-
variant for the Lie superalgebra gl(1|1), Comm. Math. Phys. 185, no. 1, 93–
127 (1997)
[11] C. P. Gabor, K. J. Supowit, W.-L. Hsu, Recognizing circle graphs in polynomial
time, Journal of the ACM (JACM) (3), 36, no. 3, 435–473 (1989)
[12] M. Kontsevich, Vassiliev’s knot invariants, Adv. Soviet Math., 16, Part 2, AMS,
Providence RI, 137–150 (1993)
12
[13] S. K. Lando, On a Hopf algebra in graph theory, J. Comb. Theor y Series B, 80,
no. 1, 104–121 (2000)
[14] S. K. Lando, A. K. Zvonkin, Graphs on surfaces and their applications , Springer
(2004)
[15] B. Mellor, Intersection graphs for string links , J. Knot Theory Ramif. 15, no. 1,
53-72 (2006).
[16] H. R. Morton, P. R. Cromwell, Distinguishing mutants by knot polynomials , J.
Knot Theory Ramif. 5 225–238 (1996)
[17] J. Murakami, Finite type invariants detecting the mutant knots , Knot Thoery.
A volume dedicated to Professor Kunio Murasugi for his 70th birthd ay. Edi-
tors: M. Sakuma et al., Osaka University, March 2000. Preprint is av ailable at
http://www.f.waseda.jp/murakami/papers/finitetype.pdf
[18] A. Vaintrob, Vassiliev knot invariants and Lie S-algebras, Math. Res. Lett. 1,
no. 5, 579–595 (1994)
[19] D. J. A. Welsh, Matroid theory, Academic Press, London (1976)
13
