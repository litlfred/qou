---
doc_id: celebratio-mathematica-neumann-hyperbolic-3-manifolds
doc_title: "Jump to Bibliography by Stavros Garoufalidis and Don Zagier Published: 2023"
section_id: sec-003-4-symplectic-properties
section_title: "Symplectic properties"
section_number: 4
pages: 12-13
source_pdf: Celebratio Mathematica — Neumann — Hyperbolic 3-Manifolds.pdf
source_sha256: 9e541693c60cbd3f
toc_source: inferred
doc_brief: "Garoufalidis & Zagier, Hyperbolic 3-manifolds, the Bloch group, and the work of Walter Neumann — survey of gluing equations, volumes, the extended Bloch group, symplectic properties and quantization."
duplicate_of: "arxiv-2304.12545v1"
---
In retrospect, the symplectic properties as described in equation (3) and the fol‐
lowing text, and their refinement from 
 to  as given in the follow-up paper [2],
turned out to be the most important aspects of these papers. They are responsible
both for the existence of the potential function and for all of the applications to
quantization that we will describe in the next section, as well as many of the con‐
nections to number theory described in Section 6.
Define an 
 matrix 
 whose rows form a -basis for the lattice
spanned by the edge equations  (1) together with one “peripheral” equation (a
coprime linear combination of the meridian and longitude equations in  (2)) at
each cusp. Then the above cited results in [1] imply that 
 is symmetric and
that 
 has rank 
, meaning that its 
 columns generate 
. Together, these
two statements are equivalent to saying that 
 can be extended to a 
matrix
in 
, meaning that
But in fact the 
 columns of 
 span the lattice 
, which is equivalent to saying
that 
 can be completed to a 
 symplectic matrix over  . (We will call
such a matrix half-symplectic.) This follows from the chain complex defined by
Walter in [2]. Explicitly, for any simplex 
, let 
 be the abelian group generated
by 
 (corresponding to the pairs of opposite edges) subject to the relation
. This is a free abelian group of rank 2, with a canonical nonsin‐
gular, skew-symmetric bilinear form given by ([2], Section 4)
The Neumann chain complex associated to an ideal triangulation is then defined
by
⇧
Here 
 and 
 are the free abelian groups on the unoriented 0- and 1-simplices
(cusps and edges), respectively, and
(sum over the 3-simplices or tetrahedra), while  maps any cusp to the sum of its
incident edges, the 
-component of  of any edge is the sum of the edges of 
that are identified with it, and 
 and 
 are the duals of  and  with respect to
the obvious scalar products on 
 and the symplectic form on  . Walter shows
([2], Theorem 4.1) that the sequence (12) is a chain complex and, at least after
tensoring with 
, is exact except in the middle, where the homology is the
sum of  rank-2 modules isomorphic to 
 
. Note that the
map  is given precisely by the matrix 
 as defined in (1) if we choose
the obvious basis for 
 and the basis of  given by choosing the basis 
 for
every 
. The rest of the proof that 
 is half-symplectic follows easily from the
theorem just quoted and will be left to the reader.
We make two remarks about this. The first is that both the construction of the
chain complex and the statement about its homology were done in [2] also for 3-
manifolds with boundary components of arbitrary genus (so the vertices of 
need not be cusps), and of course also do not require any hyperbolic structure.
The other is that the gluing equations of [1] and the symplectic results of [2] were
extended to arbitrary 
-representations in [e29].
Half-symplectic matrices occur in other contexts, e.g., in connection with Nahm’s
conjecture on the modularity of certain -hypergeometric series, and also lead to a
new description of the Bloch group. Both topics will be discussed in more detail in
Section 6.
