---
doc_id: reshetikhin-turaev
doc_title: "Ribbon graphs and their invariants derived from quantum groups"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: Reshetikhin_Turaev.pdf
source_sha256: 7ead97555a25d357
toc_source: inferred
doc_brief: "Ribbon graphs and their invariants derived from quantum groups — The generalization of Jones polynomial of links to the case of graphs in R 3 is presented."
---
The present paper is intended to generalize the Jones polynomial of links and the 
related Jones-Conway and Kauffman polynomials to the case of graphs in R 3. 
Originally the Jones polynomial was defined for links of circles in R 3 via an 
astonishing use of yon Neumann algebras (see [Jo]). Later on it was understood 
that this and related polynomials may be constructed using the quantum 
R-matrices (see, for instance, [Tul]). This approach enables one to construct 
similar invariants for coloured links, i.e. links each of whose components is 
provided with a module over a fixed algebra (see IRes], where the role of the 
algebra is played by the quantized universal enveloping algebra Uq(G) of a 
semisimple Lie algebra G). 
The Jones polynomial has been also generalized in another direction: in 
generalization of links of circles one considers the so-called tangles which are links 
of circles and segments in the 3-ball, where it is assumed that ends of segments lie 
on the boundary of the ball. Technically it is convenient to replace the ball by the 
strip R 2 x [0, 1], which enables one to distinguish the top and bottom endpoints of 
the tangle. The corresponding "Jones polynomial" of a coloured tanlge is a linear 
operator VI|174174174 
e where V1,...,V k (respectively VIQ...| 
~) 
are the modules associated with the segments incident to bottom (respectively top) 
endpoints of the tangle. Here the language of categories turns out to be very 
fruitful. The tangles considered up to isotopy are treated as morphisms of the 
"category of tangles." The generalized Jones polynomial is a covariant functor 
from this category to the category of modules (see [Tuz, Re2] ). 
Definitions of Jones-type polynomials for embedded graphs in R 3 have been 
given by several authors [KV, Ye] but the subject still remains open. It was clear 
from the very beginning that the graph should be provided with thickening, i.e. 
2 
N. Yu. Reshetikhin and V. G. Turaev 
with a surface containing the graph and contracting to it (cf. Sect. 4). Another 
related problem is what should be understood by colours of the vertices. 
The theory of the Jones-type polynomials has proved to be closely related to 
the conformal field theories [KT, Wi]. In this connection one should mention 
Witten's paper [Wi], where it is shown that the Jones polynomial and its 
generalizations are related to the topological Chern-Simons action. 
In the present paper we introduce the so-called coloured ribbon graphs in 
R 2 x [0, 1] and define for them Jones-type isotopy invariants. Ribboness means 
that the role of vertices of graphs is played by small plane squares with two 
distinguished opposite bases, the role of edges is played by thin strips (or bands) 
whose short bases are glued either to distinguished bases of the squares or to 
8(R 2 x [0, 1])=R 2 x {0, 1}. 
Our approach to colouring is based on the Drinfel'd notion of a quasitrian- 
gular Hopf algebra (see [Dr, RS, R%]). For each quasitriangular Hopf algebra A 
we define A-coloured (ribbon) graphs. The colour of an edge is an A-module. The 
colour of a vertex is an A-linear homomorphism intertwining the modules which 
correspond to edges incident to this vertex. The category of an A-coloured ribbon 
graph happens to be a compact braided strict monoidal category in the sense of 
[JS]. 
If A satisfies a minor additional condition, then we construct a canonical 
covariant functor from the category of A-coloured ribbon graphs into the category 
of A-modules. In the case A = Uq(sl2) this functor generalizes the Jones polynomial 
of links. 
We would like to emphasize that coloured ribbon graphs are not merely 
topological objects but rather mixed objects of topology and representation 
theory. For some algebras a purely combinatorial description of A-modules and 
A-homomorphisms is available (via Young tableaux, Young diagrams, etc.). Note 
also that for 3-valent graphs the colours of vertices are nothing else but the 
Clebsch-Gordan projectors and their linear combinations (cf. Sect. 7.2). 
Plan of the Paper. In Sect. 2 we recall the notion of a braided monoidal category 
and related notions. In Sect. 3 we discuss quasitriangular and ribbon Hopf 
algebras. In Sect. 4 we introduce A-coloured ribbon graphs. In Sect. 5 we state and 
prove our main theorem on the functor from the category of graphs in the category 
of modules. In Sect. 6 we collect some applications and variations of the theorem. 
Section 7 is concerned with examples and further comments on the theorem.
