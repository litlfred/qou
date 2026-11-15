---
doc_id: 2018sorus020
doc_title: "Reidemeister torsion on character varieties"
section_id: sec-018-137-the-non-split-case
section_title: "The non-split case"
section_number: 1.3.7
pages: 37-39
source_pdf: 2018SORUS020.pdf
source_sha256: c3f929e5195983ce
toc_source: inferred
doc_brief: "Reidemeister torsion on character varieties — 52 sections: Front matter; Introduction; Character varieties and Reidemeist"
---
The non-split case
Let S be an incompressible surface associated to an ideal point v ∈ˆX which is,
again, union of n parallel copies S = S1 ∪. . . ∪Sn, and we assume now that M \ Si
is connected. Hence [Si] = 0 ∈H2(M; ∂M), and in particular ∂Si is a homological
longitude. We say that Si is a Seifert surface in M. Let V (Si) be a neighborhood of
36
Si in M, and E(Si) = M \ V (Si). It is a classical fact (see [Oza01, Proposition 2])
that E(Si) is a handlebody if and only if π1(E(Si)) is free. In this case we say that
the surface Si is free. It is the case, for instance, as soon as M is small (does not
contain any closed incompressible surfaces), and a necessary and suﬃcient condition
for a knot to contain non-free Seifert surfaces is given in [Oza00].
In the sequel we assume that the Seifert surface Si is free, say of genus g, and we
denote by H = E(Si) the genus 2g handlebody complement of Si. We assume that
∂V (S) = S1 ∪Sn. We have M = V (S) ∪S1∪Sn H, hence the HNN decomposition
π1(M) = π1(H)∗α, where we ﬁx the basepoint p ∈S1, and α : π1(S1) →π1(Sn)
an isomorphism between those subgroups of π1(M). This means that we have the
presentation π1(M) = ⟨π1(H), v | vγv−1 = α(γ), ∀γ ∈π1(S1)⟩.
Lemma 1.3.16. One can chose a conjugate of the tautological representation ρ :
π1(M) →SL2(k(X)) such that the restrictions ρH : π1(H) →SL2(k(X)) and ρ1 :
π1(S1) →SL2(k(X)) are convergent. Moreover, ρ(v) = Vn with Vn =

0
tn/2
−t−n/2
0

,
in particular n is an even integer, and the restriction ρn : π1(Sn) →SL2(k(X)) is
equal to Vnρ1V −1
n . Finally, the residual restricted representation ¯ρ1 is reducible, with
Tr(¯ρ1(∂Si)) = 2.
Proof. We ﬁx a vertex s in the Bass-Serre tree T, that corresponds to the lattice O2
v
and is ﬁxed by π1(H), hence ρH is convergent. We denote by e1 the edge in the tree
T incident to s that is ﬁxed by π1(S1), and the parallel copies of S1 stabilize a series
of edges ei that form a segment in T, which has Un · s1 as an end point, as depicted
below.
s1
...
Un · s1
e1
e2
en
In particular, the representation ¯ρ1 is reducible by the same argument that in the
proof of Lemma 1.3.15. Now the element v ∈π1(M) acts on the tree T in the
following way : it sends the vertex s1 to Un · s1, but it sends the incident edge e1 to
en. Since it acts by isometries, the only possibility is to act as a central rotation with
center the mid-point of the segment [s1Un · s1]. But the fundamental group π1(M)
acts without inversion, hence n is even, and ρ(v) is of the form U n
2 RπU −1
n
2
= Vn,
where Rπ = (
0 1
−1 0 ).
The last statement follows from [CCG+94], where it is proven that the eigenvalues of
the matrix ¯ρ1(∂Σ1) are roots of unity, of order that divides the number of boundary
37
components of any surface Σi, hence those eigenvalues are equal to 1, and it achieves
the proof.
