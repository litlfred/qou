---
doc_id: black-samson-phd2010sp
doc_title: "REPRESENTATIONS OF HECKE"
section_id: sec-001-ill-links-and-braids
section_title: "ILL Links and Braids"
section_number: null
pages: 14-17
source_pdf: Black_Samson_phd2010sp.pdf
source_sha256: c16799b0bd54ff29
toc_source: inferred
doc_brief: "REPRESENTATIONS OF HECKE — 16 sections: Front matter; INTRODUCTION; ILL Links and Braids"
---
Links and Braids
II.l.l.
Links
We recall some standard notions and establish some conventions (see [25, chapter 2] or [10,
chapter 1] for details). A link is a smooth embedding SI u· .. U SI
----> S3. Whenever it is convenient
and does not cause confusion, we also refer to the image of the embedding as the link. All links
are oriented. A link with one component is called a knot. An isotopy of links is a smooth path in
the space of embeddings, or equivalently a smooth embedding (SI U ... U SI) x I
----> S3. Isotopy
forms an equivalence relation whose equivalence classes are called link types. For our purposes, a
link invariant is a function on link types taking values in a ring.
A link diagram is a four-valent graph embedded in S2 along with the choice of over- and
under-crossing strands at each vertex. An isotopy of link diagrams is an isotopy of the underlying
graphs that preserves the crossing data. By compactness, we may assume that the diagram embeds
into a disk in lR?2 (which is how links are usually drawn), but we allow for isotopies of link diagrams
that utilize the connectivity of the sphere S2. A link diagram specifies a link type in a natural way:
compose the planar embedding of the link diagram with the standard embedding lR?2
'----> lR?3 and
locally perturb the two strands at each crossing in opposite directions normal to the plane. Thus,
we have a well-defined surjective map called realization V
----> 12, where V is the set of link diagrams
up to planar isotopy and £ is the set of link types. Using standard transversality arguments, there
exist generic projections JR3
----> II, where II is a plane, under which the image of a link is a link
diagram (there are only finitely many transverse double points). Thus, we have sections £ ---->V of
the realization map. The fibers of the realization map are described by Reidemeister's theorem.
Theorem 11.1.1.
Two link diagrams realize isotopic links if and only if they are related by a
7
sequence of planar isotopies and the following three local moves:
(R I) P "
"110
(R II)
(R III)
II. 1. 2.
Braids
There are many equivalent ways to define braids (see, e.g.
[7] or [25, chapter 1]).
A
geometric braid with d strands is a smooth embedding of of d disjoint arcs in ]R2 x [0, 1] such
that the endpoints of each strand have coordinates (i, 0, 0) and (7l"(i), 0,1) for some permutation
7l" E Sd and the height function (projecting onto the third coordinate) has no critical points. Bya
geometric braid isotopy, we mean an isotopy of the ambient Euclidean space keeping the endpoints
of the strands fixed. When we speak of a braid, we mean an isotopy class of geometric braids. Let
Bd denote collection of braids on d strands.
By analogy with link diagrams, we consider geometric braid diagrams consisting of im-
mersed arcs in the strip ]R x [0, 1] connecting points (i, 0) to (7l"(i), 1) for i = 1, ... , d satisfying
the conditions that projection onto the second coordinate has no critical points and that self-
intersections are transverse. Each transverse double point in a geometric braid diagram is called a
cTOssing and carries with it the data of which strand passes over and which strand passes under.
There is an appropriate notion of isotopy of geometric braid diagrams that allows one to speak
simply of braid diagrams, meaning isotopy classes.
Braids naturally carry the structure of a group whose operation is given by placing dia-
grams on top of one another. We now define the braid group abstractly, following Artin [3]. Fix
d :::: 1. Let I:d = {erl, ... , erd-l} be the set of braid generators, and let I:;; denote the set of words
in the symbols I:d U I:dl. Then, Bd is the braid group on d strands, that is, the quotient of the
8
free group on ~d by the relations
O"jO"i when Ii - jl > 1.
For each d, there is a canonical map
~d
---» Bd .
The map e : Bd
---> Z,
O"i
f-+ 1 induces an
isomorphism of groups Bd/[Bd,Bd] ---> Z. The image of 0 under Bd ---> Z is called the exponent sum
of o. Also there is a map Bd ---> .c, 0
f-+ 0, defined by closing a braid into a link by connecting the
top of strand i to the bottom of strand i for each i (see Figure II.1.2).
Figure 11.1: A diagram of the braid 0 = 0"2 10"i and its closure o.
Alexander showed in [2] that this map is surjective by giving an algorithm that transforms a
link diagram, using the Reidemeister moves, into an equivalent diagram that is evidently the closure
of a braid. We call two braids (not necessarily on the same number of strands) link equivalent if
they form isotopic links after closure. In [31], Markov made the following characterization of this
equivalence relation on Ud21 Bd' although the first published proof was due to Birman ([6]).
Theorem 11.1.2. Link of equivalence of braids is generated by the following two local moves.
(M I)
(M II)
(30,
where i
: Bd '---+ Bd+l is the natural inclusion defined on generators by O"i f-+ O"i.
II
....I.
II
....I..
9
(3
<-------->ITL
Figure II.2: The cyclic Markov move.
J
J1
1 ...
l~
Cl'
<-------->
Cl'
T
"If
1'-,
Figure IL3: The stabilization Markov move.
