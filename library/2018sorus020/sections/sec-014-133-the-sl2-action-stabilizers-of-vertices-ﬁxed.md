---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-014-133-the-sl2-action-stabilizers-of-vertices-ﬁxed
section_title: "The SL2 action : stabilizers of vertices, ﬁxed points and trans- lation length"
section_number: 1.3.3
pages: 31-33
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The SL2 action : stabilizers of vertices, ﬁxed points and
translation length
There is a natural isometric and transitive action of GL(V ) on T, induced by the
action of GL(V ) on V .
Deﬁnition 1.3.1. The action of a subgroup G ⊂GL(V ) on T will be said trivial if
a vertex is ﬁxed by the whole group.
Lemma 1.3.2. For any g ∈GL2(K), [L] ∈T, ﬁx a basis {e, f} of L ∈[L], and
n, m ∈Z such that {tne, tmf} is a basis of g · L. Then v(det(g)) = n + m.
Proof. In this basis, L ≃O2
v, and g can be written as the matrix A ( tn
0
0 tm ) B with
A, B ∈GL2(Ov). The result follows.
Now we restrict to the SL(V ) action. We say that an element g ∈SL(V ) stabilizes
a vertex [L] ∈T if for any representative L we have g · L = xL for some x ∈K∗.
Lemma 1.3.3. An element g ∈SL(V ) stabilizes a vertex [L] iﬀfor any representa-
tive g · L = L.
30
Proof. Assume that g · L = xL, then by Lemma 1.3.2, v(det(g)) = 2v(x) = 0 hence
x ∈O∗and xL = L.
Furthermore, as SL2(Ov) is the stabilizer of the standard lattice O2
v, we deduce the
proposition.
Proposition 1.3.4. The stabilizer in SL2(K) of any vertex of the tree T is a GL2-
conjugate of SL2(Ov).
Remark 1.3.5. Since for any g ∈SL(V ), v(det(g)) = 0, we know that the distance
d([L], g · [L]) = |n −m| is even, in particular SL(V ) acts without inversion on T,
that is it can not ﬁx an edge and exchange its end points.
Deﬁnition 1.3.6. Given g ∈SL(V ), we deﬁne the translation lenght of g to be
equal to l(g) = min
[L]∈T d([L], g · [L]).
There are two ways for g ∈SL(V ) acting on the tree :
1. Elliptic elements
If g has some ﬁxed points, or alternatively l(g) = 0, then it will be called
elliptic. In this case, there is a basis of V such that O2
v is ﬁxed and g is an
element of SL2(Ov). The set of ﬁxed points Tg is a subtree of T.
2. Hyperbolic elements
If l(g) > 0, then g is called hyperbolic ; Ag = {s ∈T | d(s, g · s) = l(g)}
is an inﬁnite, globally ﬁxed, axis on which g acts by translation, and any
basis of V such that the standard lattice O2
v ∈Ag provides the matrix form
g =

tl(g)/2
0
0
t−l(g)/2

.
We prove the following lemma from [SB77, Corollaire 3, p.90].
Lemma 1.3.7. Let G be a subgroup of SL(V ) acting on the Bass-Serre tree T. If
every element g ∈G ﬁxes a vertex of T, then the whole group has a ﬁxed vertex,
that is the action is trivial.
Proof.
— First we prove that every two elements have a common ﬁxed point.
Let g1, g2 ∈Γ which have no common ﬁxed point, take two vertices s1 and s2,
such that they realize the minimal distance l between the ﬁxed subtrees T1
and T2. Then the segment [s1, s2] has no other point than s1 ﬁxed by g1, so
it’s image by g1 is [s1, g1·s2]. In the same way, it’s image by g−1
2
is [g−1
2 ·s1, s2].
Consider the action of the element g1g2 ∈Γ.
31
s1
s2
g1 · s2
g−1
2
· s1
g2 · s1
g1g2 · s1
l
l
l
l
We prove that it acts on the pictured axis by translation of length 2l : by the
minimality of l, g−1
2 · s1 and s1 are at distance 2l. It clear that s1 and g1g2 · s1
are at distance at most 2l. Now if d(s1, g1g2 · s1) < 2l, there exists an other
vertex than g1 · s2 in the intersection [s1, g1 · s2] ∩[g1 · s2, g1g2 · s1]. Denote it
by s. Then g−1
1
· s ∈[s1, s2] ∩[s2, g2 · s1] \ {s2}, hence it is ﬁxed by g2, what
contradicts the minimality of l.
Iterating this process, we see that g1g2 ﬁxes acts as an hyperbolic element,
and thus has no ﬁxpoint, which is a contradiction.
— Write {g1, ...gn} a system of generators of Γ. Assume that g1, ..., gk have a
common ﬁxed point s, and take s′ a ﬁxed point of gk+1 as near as possible
of s. So one of the gi’s, i = 1...k, do not ﬁx any other point of [ss′] than
s ; applying the same argument as above gives that gk+1 ﬁxes s too, and
concludes the proof.
