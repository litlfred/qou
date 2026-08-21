---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-024-2-hyperbolic-elements
section_title: "Hyperbolic elements"
section_number: 2
pages: 32-33
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
doc_brief: "Reidemeister torsion on character varieties — 78 sections: Introduction; (−1)i+1; ByH∗(M, Ad◦ρ) (respectivelyH∗(M,ρ"
---
If l(g) > 0, then g is called hyperbolic; Ag ={s∈ T | d(s,g·s) = l(g)}
is an inﬁnite, globally ﬁxed, axis on whichg acts by translation, and any
basis ofV such that the standard latticeO2
v∈Ag provides the matrix form
g =
(
tl(g)/2 0
0 t−l(g)/2
)
.
We prove the following lemma from [SB77, Corollaire 3, p.90].
Lemma 1.3.7. Let G be a subgroup ofSL(V ) acting on the Bass-Serre treeT. If
every element g∈ G ﬁxes a vertex ofT, then the whole group has a ﬁxed vertex,
that is the action is trivial.
Proof. — First we prove that every two elements have a common ﬁxed point.
Letg1,g 2∈ Γ which have no common ﬁxed point, take two verticess1 ands2,
such that they realize the minimal distancel between the ﬁxed subtreesT1
and T2. Then the segment[s1,s 2] has no other point thans1 ﬁxed byg1, so
it’s image byg1 is [s1,g 1·s2]. In the same way, it’s image byg−1
2 is [g−1
2 ·s1,s 2].
Consider the action of the elementg1g2∈ Γ.
31
s1 s2
g1·s2
g−1
2 ·s1
g2·s1g1g2·s1
ll
l
l
We prove that it acts on the pictured axis by translation of length2l : by the
minimality ofl,g−1
2 ·s1 ands1 are at distance2l. It clear thats1 andg1g2·s1
are at distance at most2l. Now ifd(s1,g 1g2·s1) < 2l, there exists an other
vertex thang1·s2 in the intersection[s1,g 1·s2]∩ [g1·s2,g 1g2·s1]. Denote it
bys. Theng−1
1 ·s∈ [s1,s 2]∩ [s2,g 2·s1]\{s2}, hence it is ﬁxed byg2, what
contradicts the minimality ofl.
Iterating this process, we see thatg1g2 ﬁxes acts as an hyperbolic element,
and thus has no ﬁxpoint, which is a contradiction.
— Write{g1,...gn} a system of generators ofΓ. Assume thatg1,...,g k have a
common ﬁxed points, and takes′ a ﬁxed point ofgk+1 as near as possible
of s. So one of thegi’s,i = 1...k, do not ﬁx any other point of[ss′] than
s; applying the same argument as above gives thatgk+1 ﬁxess too, and
concludes the proof.
