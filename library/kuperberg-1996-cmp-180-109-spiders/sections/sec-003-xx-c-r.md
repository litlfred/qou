---
doc_id: kuperberg-1996-cmp-180-109-spiders
doc_title: "Spiders for Rank 2 Lie Algebras"
section_id: sec-003-xx-c-r
section_title: "XX-«'')c<-r"
section_number: null
pages: 40-43
source_pdf: kuperberg-1996-cmp-180-109-spiders.pdf
source_sha256: b6c94630554cc15a
toc_source: inferred
doc_brief: "Spiders for Rank 2 Lie Algebras — A spider is an axiomatization of the representation theory of a group, quantum group, Lie algebra, or other group or group-like object."
---
which leads to an expansion of tangle c:
VA—X
+ q~
m 6
which leads to the evaluation of the entire knot projection:
\A/
-q-
m){q
ι-q+\-q-
λ+ 
q~
2)
Spiders for Rank 2 Lie Algebras
149
Given a knot K and a clasp c in one of the combinatorial spiders presented here,
consider the clasped cabling of K. I.e., replace the strand of K by several strands
tied together with c, for example:
(9)
The value of a web such as the one in Fig. (9) is also a regular isotopy invari-
ant of K; it is the Reshetikhin-Turaev ribbon graph invariant of K colored by an
irreducible representation whose weight is the highest weight of c [17]. By the iso-
morphism between combinatorial and algebraic spiders, clasps are a complete set
in the sense that these clasped invariants yield all of the information about K that
can be obtained from applying the unclasped link invariants to all cablings of K
and all other satellites of K. Moreover, the value of a clasped cabling of K can be
computed more easily than an unclasped cabling, because clasped web spaces are
much smaller vector spaces than their unclasped counterparts.
8.4. Combinatorial consequences. Although Theorems 6.1, 6.9, and 6.10 are prop-
erly results in representation theory, they are also interesting as results in enumera-
tive combinatorics. John Stembridge and Richard Stanley [20] noted that a B2 basis
web w E 5(11... 1) is equivalent to a matching of In cyclically ordered points with
no 6-point star, meaning that among the 2n points, there are no six in cyclic order
no six points p\, p2, pz,q\,qi,qs with each pt matched to qt. On other hand, the
number of such matchings with no 2&-point star is known to be dim Inv( V®
ln),
where V is the defining representation of sp(2& — 2) [21]. Thus, this special case
of Theorem 6.9 was known previously.
It is interesting that ordinary trivalent graphs are related to the exceptional Lie
algebra G2. One corollary of this surprising connection is the following enumerative
result:
Theorem 8.1. For n ^ 3, let an be the number of triangulations of a fixed convex
n-gon such that at least six triangles meet at each internal vertex, and let
A(x)= 
1 +x
2 + 
Σanx
n
n
be a generating function. For n ^ 0, let
for n ^ 0, and let
150 
G Kuperberg
be a generating function. Then
B(x)=A(xB(x)). 
(8)
Proof. (Sketch) By Theorem 6.10, bn may equally well be defined as the number
of G2 basis webs with n endpoints. Each triangulation is dual to a connected basis
web. Equation (8.1) becomes a standard relation between the number of connected
graphs of a certain type and the number of disjoint unions of such graphs. More
precisely, consider n boundary points on a disk with one marked, and consider a
basis web w G B( 11 
1) with this boundary. Then w is given by an ordered tree
whose vertices are its connected components: The root is the component with the
marked vertex, and the children of each component are the adjacent components
other than the parent, if there is one. The children of each component are ordered
going counterclockwise, with the distinguished boundary point separating the first
and last children of the root. Equation (8) is the usual generating function for
ordered trees [3, p. 11-12]. 
D
The sequence {bn} is easy to compute using character theory. Thus, Theorem 8.1
produces a fast algorithm for computing {an}.
It is easy to show that the radius of convergence of B(x) is 1/7. Then by
Theorem 8.1, the radius of convergence of A(x) is at least B(l/Ί)/Ί. Furthermore,
numerical evidence supports the conjecture that it is exactly i?(l/7)/7, i.e., that
Conjecture 8.2. If an and bn are defined as in Theorem 8.1, then
lim ψa~n= 
co 
=6.811... .
Our equinumeration theorems count all basis webs with a fixed boundary. How-
ever, for each n and k, one can also consider the set of Gι basis webs, for example,
with n endpoints of type 1 and k internal vertices. The role of these sets and their
cardinality in representation theory is not known.
Given an A^ basis-web set B(s) for some sign string s, there are various H-maps
corresponding to different adjacent pairs of signs. But if s' is another sign string of
the same weight as s, then any two sequences of H-maps permuting s into s' yield
the same bijection B(s) —» B(s'), provided that the first and the last sign of s are
not considered adjacent. On the other hand, if a sign is moved all the way around
the boundary by H-maps, monodromy arises:
Spiders for Rank 2 Lie Algebras 
151
It would be interesting to compute the cycle structure or establish properties of this
monodromy, which is related to a linear action of the braid group on
S
where the direct sum on the right is taken over all sign strings of length n.
Acknowledgement The author would like to thank Sarah Witherspoon, Bruce Westbury, Igor
Frenkel, and Mikhail Khovanov for their attention to this paper and the work it presents Also, the
T]HX macro package PSTricks [23] was essential for typesetting the equations and figures
