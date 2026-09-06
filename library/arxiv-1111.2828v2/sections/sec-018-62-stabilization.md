---
doc_id: arxiv-1111.2828v2
doc_title: "THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS"
section_id: sec-018-62-stabilization
section_title: "Stabilization"
section_number: 6.2
pages: 20-22
source_pdf: 1111.2828v2.pdf
source_sha256: 90e2f5a9b978d403
---
We regard SL(n − 1, C) as a subgroup of SL(n, C) via the standard inclusion adding a 1 as the upper
left entry.
Let π : M (n, C) → M (n−1, C) be the map sending a matrix to the submatrix obtained by remov -
ing the ﬁrst row and last column. The subgroup Dk(SL(n, C)/N) of C gen
k (SL(n, C)/N) generated
by tuples (g0N, . . . , gkN ) such that the upper left entry of each gi is 1 and such that
(6.15) (π(g0)N, . . . , π(gk)N ) ∈ C gen
k (SL(n − 1, C)/N)
THE COMPLEX VOLUME OF SL(n, C)-REPRESENTATIONS OF 3-MANIFOLDS 21
form an SL(n − 1, C)-complex. Consider the SL(n − 1, C)-invariant chain maps
π : D∗(SL(n, C)/N) → P tn−1
∗(6.16)
i : D∗(SL(n, C)/N) → P tn
∗ ,(6.17)
where the ﬁrst map is induced by π and the second is induced by the inclusion D∗(SL(n, C)/N) →
C gen
∗ (SL(n, C)/N. Let Dk = Dk(SL(n, C)/N) ⊗Z[SL(n−1,C)] Z.
Lemma 6.13. The maps λ ◦ π and λ ◦ i from D3 to ˆP(C) agree on cycles.
Proof. Let c ∈ Dk be induced by a tuple (g0N, . . . , gkN ) ∈ Dk(SL(n, C)/N), and let cI be the
collection of Ptolemy coordinates associated to (N, g0N, . . . , gkN ). Since some Ptolemy coordinates
may be zero, cI is not necessarily a Ptolemy assignment. Note, however, tha t cI
α is a Ptolemy
assignment for each (a0, . . . , ak+1) ∈ ∆ k+1
n−2(Z) with a0 = 0. Note also that cI
α ∈ P t2
k+1 only depends
on c. Hence, there is a map
(6.18) P : Dk → P t2
k+1, c ↦→
∑
α∈∆ k+1
n− 2(Z)
a0=0
cI
α.
We wish to prove the following:
(6.19) ∂P (c) + P ∂(c) = J n
k (i(c)) − J n−1
k (π(c)) +
∑
β∈∆ k+1
n− 3(Z)
b0=0
∂β(cI ) ∈ P t2
k+1.
Given this, the result follows immediately from Lemma 6.7.
One easily veriﬁes that
cI
(1,b0,...,bk) = π(c)(b0,...,bk) ∈ P tn−1
k , (b0, . . . , bk) ∈ ∆ k
n−3(Z).(6.20)
cI
(0,a0,...,ak) = i(c)(a0,...,ak), (a0, . . . , ak) ∈ ∆ k
n−2(Z).(6.21)
Using this, one has
(6.22)
∂P (c) + P ∂(c) =
∑
α∈∆ k
n− 2(Z)
i(c)α +
k+1∑
i=1
(−1)i ∑
α∈∆ k+1
n− 2(Z)
a0=0
cI
αi +
k∑
i=0
(−1)i ∑
α∈∆ k+1
n− 2(Z)
a0=0,ai+1=0
cI
αi+1
=
∑
α∈∆ k
n− 2(Z)
i(c)α +
k+1∑
i=1
(−1)i ∑
α∈∆ k+1
n− 2(Z)
a0=0,ai>0
cI
αi
=
∑
α∈∆ k
n− 2(Z)
i(c)α +
∑
β∈∆ k+1
n− 3(Z)
b0=0
k+1∑
i=1
(−1)icI
βi
=
∑
α∈∆ k
n− 2(Z)
i(c)α −
∑
β∈∆ k+1
n− 3(Z)
b0=0
cI
β0 +
∑
β∈∆ k+1
n− 3(Z)
b0=0
∂β(cI )
= J n
k (i(c)) − J n−1
k (π(c)) +
∑
β∈∆ k+1
n− 3(Z)
b0=0
∂β(cI ).
22 STA VROS GAROUF ALIDIS, DYLAN P. THURSTON, AND CHRISTIAN K . ZICKERT
This proves ( 6.19), hence the result. □
Proposition 6.14. The map λ : H3(SL(n, C), N) → ˆB(C) respects stabilization.
Proof. First note that π induces an isomorphism D0(SL(n, C)/N) ∼= C 0(SL(n − 1)/N). Using a
standard cone argument, one easily checks that D∗(SL(n, C)/N) is a free SL(n − 1, C)-resolution of
Ker(D0(SL(n, C)/N) → Z). Hence, D∗ computes H∗(SL(n − 1, C), N), and the result follows from
Lemma 6.13. □
6.3. p SL(n, C)-Ptolemy assignments. When n is even, deﬁne pP tn
∗ to be the complex of Ptolemy
coordinates of generic tuples in p SL(n, C)/N. The Ptolemy coordinates are deﬁned as in ( 5.1), and
take values in C∗/
⟨±1⟩. As in ( 6.1), we have an isomorphism C gen
∗ (p SL(n, C)/N)p SL(n,C) ∼= pP tn
∗ .
For c ∈ C ∗/⟨±1⟩ let~c ∈ C be the image of some ﬁxed set theoretic section of C
exp
− − →C∗ → C∗/⟨±1⟩,
e.g. 1
2 log(x2) (the particular choice is inessential). The map
(6.23) λ : pP t2
3 → Z[ˆCodd], c ↦→(~c03 +~c12 −~c02 −~c13,~c01 +~c23 −~c02 −~c13)
induces a map H3(PSL(2, C), N) → ˆB(C)PSL, which agrees with the map constructed in Zickert [ 30,
Section 3]. By precomposing λ with the map pJ n
3 : pP tn
3 → pP t2
3 deﬁned as in ( 6.2) we obtain a
map
(6.24) λ : H3(p SL(n, C), N) → ˆB(C)PSL,
which commutes with stabilization. This proves that a decor ated boundary-unipotent representation
in p SL(n, C) determines an element in ˆB(C)PSL. The proofs of the above assertions are word by
word identical to their SL(n, C)-analogs.
