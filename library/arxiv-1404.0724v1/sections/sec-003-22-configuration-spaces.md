---
doc_id: arxiv-1404.0724v1
doc_title: "Introduction to representations of braid groups"
section_id: sec-003-22-configuration-spaces
section_title: "Configuration spaces"
section_number: 2.2
pages: 4-4
source_pdf: 1404.0724v1.pdf
source_sha256: ea40edaad77c1617
toc_source: outline
doc_brief: "Introduction to representations of braid groups — These are lecture notes prepared for a minicourse given at the Cimpa Research School Algebraic and geometric aspects of representation the- ory, held"
duplicate_of: "ariasabad2015-revcolmat"
---
Conﬁguration spaces
The group Bn can also be described as the fundamental group of the conﬁguration space of
points in the plane. We will now brieﬂy recall some deﬁnitions regarding conﬁguration spaces.
Let M be a smooth manifold. The conﬁguration space of n ordered points in M, denoted ˆCn(M)
is the manifold:
ˆCn(M) := {(x1, . . . , xn) ∈Mn : xi̸ = xj if i̸ = j}.
There is a natural action of the symmetric group Σn on the space ˆCn(M), given by permuting
the coordinates. The conﬁguration space of n unordered points in M is the quotient space:
Cn(M) := ˆCn(M)/Σn.
Theorem 2.4 (Fox-Neuwirth [13], Fadell-van Buskirk [11]). There is a natural isomorphism
between the braid group in n strands and the fundamental group of the conﬁguration space of n
unordered points in the plane:
Bn ∼= π1(Cn(C), p).
Here p = {1, 2, . . . , n} ∈Cn(C).
The isomorphism above is deﬁned as follows: a braid can be thought of as a path in the
conﬁguration space ˆCn(C). However, seen as a path in this conﬁguration space it is not closed,
since the endpoint of a strand may be diﬀerent from its starting point. By composing with
the quotient map to the unordered conﬁguration space, this path becomes a closed path, and
therefore deﬁnes an element of the fundamental group.
