---
doc_id: invariant-eigendistributions-2
doc_title: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups"
section_id: sec-004-31-lemma
section_title: "Lemma."
section_number: 3.1
pages: 4-6
source_pdf: Invariant_eigendistributions_2.pdf
source_sha256: ee43c3ebeff95265
toc_source: inferred
doc_brief: "Invariant eigendistributions on a semisimple Lie algebra and homology classes on the conormal variety II: representations of Weyl groups — 18 sections: Front matter; Contents; Introduction."
---
Lemma.
The inclusion Bν →B induces a W-map H∗(Bν) →H∗(B). This map factors
through the projection H∗(Bν) →H∗(Bν)A(ν) onto the A(ν)-invariants.
REPRESENTATIONS OF WEYL GROUPS
5
Proof.
It suﬃces to show that the homotopy equivalence of Bν constuct above has a representative
Bν →Bν, denoted aν(w), so that the inclusion i : Bν →B satisﬁes
i ◦aν(w) ∼a(w) ◦i.
Choose a neighbourhood V of Bν for which the inclusion k : Bν →V has a homotopy inverse q : V →Bν:
q ◦k ∼1 on Bν,
k ◦q ∼1 on V.
Let U = {(b, ν′) : b ∈V, |ν′| ≤R} for some ﬁxed R > |ν|. Deﬁne maps
j : Bν →U, j(b) = (k(b), ν) = (b, ν),
p : V →Bν, p(b, ν′) = q(b).
We show that
p ◦j ∼1 on Bν,
j ◦p ∼1 on U.
(1)
The ﬁrst relation is clear since
p ◦j(b) = q ◦k(b) and q ◦k ∼1 on Bν.
To see the second relation, use k ◦q ∼1 to choose a homotopy qs : V →V, 0 ≤s ≤1, from q0 = 1V to
q1 = k ◦q. Perform successively the following homotopies of maps U →U :
(1) (b, ν′) →(b, sν′), s going from 1 to 0,
(2) (b, ν′) →(qs(b), 0), s going from 0 to 1,
(3) (b, ν′) →(k ◦q(b), sν), s going from 0 to 1.
This gives a homotopy from the identity 1U : (b, ν′) →(b, ν′) to p ◦j : (b, ν′) →(k ◦q(b), ν) as required.
For λ close to 0, aλ(w)j(Bν) stays in the neighbourhood U of j(Bν). The relation (1) shows that the
p, j can take the place of the p, i in the deﬁnition (2.7) of aν(w). For such λ the map p◦aλ(w)◦j : Bν →Bν
therefore represents the homotopy class aν(w):
aν(w) ∼p ◦aλ(w) ◦j : Bν →Bν.
(2)
For 0 ≤s ≤1, deﬁne of maps
js : Bν →U, js(b) = (b, sν),
ps : U →V, ps(b, ν′) = qs(b)
with qs as above. Consider the homotopy of maps
ps ◦aλ(w) ◦js : Bν →V,
0 ≤s ≤1.
(3)
For s = 0 we get
po ◦aλ(w) ◦jo(b) = qo ◦aλ(w)(b, 0) = a(w)b
because aλ(w) and a(w) coincide on B considered as the zero section in B∗: this is clear from the deﬁnition
of aλ(w). So for s = 0, (3) reduces to a(w) ◦i. On the other hand, for s = 1 we get
p1 ◦aλ(w) ◦j1(b) = p ◦aλ(w)(b, ν)) = p ◦aλ(w) ◦j(b)) = aν(b)b
by (2). So for s = 1, (3) reduces to aν(w)◦i. Hence (3) provides the desired homotopy i◦aν(w) ∼a(w)◦i.
REPRESENTATIONS OF WEYL GROUPS
6
To see the second assertion of the lemma one only has to note that the action of the stabilizer of
ν in U, which induces the action of A(ν) in H∗(Bν), becomes trivial in H∗(B) as U is connected. This
proves the lemma.
3.2 Corollary. In top dimension the W-map
H2e(ν)(Bν)A(ν) →H2e(ν)(B),
e(ν) = dimCBν,
is an isomorphism onto its image.
Proof. This is because the representation of W on H2e(ν)(Bν)A(ν) is irreducible, as we shall see in (4.1).
