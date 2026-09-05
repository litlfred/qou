---
doc_id: arxiv-math-9805116v3
doc_title: "Weak Hopf Algebras"
section_id: sec-022-41-first-consequences-of-the-c--structure
section_title: "First consequences of the C ∗-structure"
section_number: 4.1
pages: 31-33
source_pdf: 9805116v3.pdf
source_sha256: 65ce47d232d61de4
doc_brief: "Weak Hopf Algebras — We give an introduction to the theory of weak Hopf algebras pr oposed recently as a coassociative alternative of weak quasi-Hopf algebras."
---
Deﬁnition 4.1 We deﬁne a ∗-WHA as a WHA (A, 1, ∆ ,ε,S ) over the complex numbers |C
together with an antilinear involution ∗ such that
i) (A, ∗) is a ∗-algebra,
ii) ∆ is a ∗-algebra map, i.e. (x∗)(1) ⊗ (x∗)(2) = (x(1))∗ ⊗ (x(2))∗ for all x ∈A.
By uniqueness of the unit, counit, and the antipode (see Lemm a 2.8) we have the following
additional relations in a ∗-WHA.
1∗ = 1, ε (x∗) = ε(x), S (x∗)∗ =S−1(x). (4.1)
Now it is easy to check that the projections ⊓L and ⊓R satisfy
⊓L (x)∗ = ⊓L(S(x)∗), ⊓R(x)∗ = ⊓R(S(x)∗) (4.2)
therefore AL and AR are ∗-subalgebras of A. As an elementary exercise we obtain selfduality
of the ∗-WHA:
Scholium 4.2 LetA be a ∗-WHA and deﬁne a star operation on its dual as follows
⟨ϕ∗,x ⟩ =: ⟨ϕ,S (x)∗⟩. (4.3)
Then ˆA with this star operation becomes a ∗-WHA.
31
For a ∗-WHA A the canonical isomorphisms κL
A:AL → ˆAR and κR
A:AR → ˆAL of Lemma
2.6 become ∗-algebra isomorphisms.
We omit the discussion of further properties of ∗-WHAs and turn to the most important
case of C ∗-WHAs.
Deﬁnition 4.3 A ∗-WHA A possessing a faithful ∗-representation is called a C ∗-weak Hopf
algebra, or C ∗-WHA for short.
Being a ﬁnite dimensional C ∗-algebra any C ∗-WHA can be uniquely characterized, as an al-
gebra, by the dimensions nr ∈ IN of its blocks where r is running over the ﬁnite set SecA of
equivalence classes of irreducible representations (i.e. the sectors) of A.
A ∼=
⨁
r∈SecA
Mnr , M nr = Mat(nr, |C) . (4.4)
AL andAR are unital ∗-subalgebras therefore they are C ∗-algebras as well and we have natural
numbersna,a ∈ SecAL andnb,b ∈ SecAR characterizing the type of AL andAR, respectively.
Ac ∼=
⨁
a∈SecAc
Mna , c =L,R . (4.5)
The antiisomorphism S:AL → AR establishes a bijection a ↦→¯a of the blocks of AL to the
blocks of AR such that n¯a =na. (We consider SecAL, SecAR, and SecA as disjoint sets which
allows to use one function n.)
The following elementary but important Proposition will be the basic ingredient in proving
both the existence of Haar measures and rigidity of the repre sentation category of C ∗-WHAs.
Proposition 4.4 LetA be a ﬁnite dimensional C ∗-algebra and S:A →Aop an algebra isomor-
phism such that ( ∗ ◦S)2 = idA. Then there exists g ∈A× such that
i) g ≥ 0
ii) gxg−1 = S2(x), x ∈A
iii) trr(g) = trr(g−1), r ∈ SecA
iv) S(g) = g−1
where tr r denotes trace in the irreducible representation Dr. An element g ∈A satisfying only
the ﬁrst three properties is already unique.
Proof: The restriction S|CenterA is an algebra automorphism therefore acts on the minimal
central idempotents er asS(er) = e¯r wherer ↦→¯r is a permutation of SecA. Since e∗
r =er and
∗ ◦S is an involution, r ↦→¯r is an involution.
Choose matrix units {eαβ
r } for theC ∗-algebraA and deﬁne the antiautomorphism S0:A →A
byS0(eαβ
r ) := eβα
¯r . Then S2
0 = idA and ∗ ◦S0 =S0 ◦ ∗. Since S ◦S0 is an automorphism of A
that acts as the identity on the centre, there exists C ∈A invertible such that S = AdC ◦S0..
It follows that
∗ ◦S(x) = C −1∗S0(x∗)C ∗, (∗◦S)2(x) = C −1∗S0(C −1)xS0(C)C ∗ =x, (4.6)
therefore S0(C)C ∗ is central and so is its adjoint K :=CS 0(C ∗) = S(C ∗)C.
S2(x) = CS 0(CS 0(x)C −1)C −1 =CS 0(C −1)xS0(C)C −1, x ∈A (4.7)
32
henceT :=CS 0(C −1) = CC ∗[S0(C)C ∗]−1 =CC ∗K −1∗ implementsS2 and its polar decompo-
sition takes the form
T =ug′, u =K −1∗(K ∗K)1/2, g ′ =C(K ∗K)−1/2C ∗ . (4.8)
Using centrality of the unitary part and the computations S(T ) = S(C)S2(C −1) =
S(C)TC −1T −1 = T −1 and S(K) = S0(K) = C ∗S0(C) = S0(C)C ∗ = K ∗ we obtain that
g′ is positive invertible, implements S2, and satisﬁes S(g′) = g′−1. These latter three proper-
ties, however, do not ﬁx g completely. If c is positive, central, and satisﬁes S(c) = c−1 then
g =g′c will also satisfy the above three properties. Now deﬁning
g :=g′c where c =
∑
r
er
(
trr(g′−1)
trr(g′)
)1/2
(4.9)
it is easy to verify that g obeys (i–iv) of the Proposition. If f ∈A satisﬁes only (i), (ii), and
(iii) then f = gc where c is positive invertible, central, and satisﬁes Dr(c) = Dr(c)−1 for all
irrep Dr. Hence c = 1, proving uniqueness of g. Q.e.d.
