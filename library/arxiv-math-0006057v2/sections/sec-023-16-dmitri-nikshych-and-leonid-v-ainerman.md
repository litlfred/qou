---
doc_id: arxiv-math-0006057v2
doc_title: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS"
section_id: sec-023-16-dmitri-nikshych-and-leonid-v-ainerman
section_title: "DMITRI NIKSHYCH AND LEONID V AINERMAN"
section_number: 16
pages: 16-18
source_pdf: 0006057v2.pdf
source_sha256: c881434fe9f4b04f
doc_brief: "FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS — W e give a survey of the theory of ﬁnite quantum groupoids (wea k Hopf algebras), including foundations of the theory and app lications to ﬁnite"
---
take ∑
j φj ⊗vj ∈V ∗ ⊗V,z ∈Ht. Using the isomorphisms lV and rV identifying
Ht ⊗V , V ⊗Ht and V , for all v ∈V and φ ∈V ∗ we have:
(idV ⊗dV )(bV ⊗ idV )(v) = (id V ⊗dV )(bV (1(1) · 1) ⊗ 1(2) ·v)
= (id V ⊗dV )(bV (1(2)) ⊗S−1(1(1)) ·v)
=
∑
i
(idV ⊗dV )(1(2) ·gi ⊗ 1(3) ·γi ⊗S−1(1(1)) ·v)
=
∑
i
1(2) ·gi ⊗ (1(3) ·γi)(1′
(1)S−1(1(1)) ·v)1′
(2)
= 1 (2)S(1(3))1′
(1)S−1(1(1)) ·v ⊗ 1′
(2) =v,
(dV ⊗ idV ∗ )(idV ∗ ⊗bV )(φ) = ( dV ⊗ idV ∗ )(1(1) ·φ ⊗bV (1(2)))
=
∑
i
(dV ⊗ idV ∗ )(1(1) ·φ ⊗ 1(2) ·gi ⊗ 1(3) ·γi)
=
∑
i
(1(1) ·φ)(1′
(1)1(2) ·gi)1′
(2) ⊗ 1(3) ·γi
= 1 ′
(2) ⊗ 1(3)1(1)S(1′
(1)1(2)) ·φ =φ,
which completes the proof.
5.2. Quasitriangular quantum groupoids.
Deﬁnition 5.2.1. A quasitriangular quantum groupoid is a pair ( H, R) where
H is a quantum groupoid and R ∈ ∆ op(1)(H ⊗kH)∆(1) satisfying the following
conditions :
∆ op(h)R = R∆( h),(28)
for all h ∈H, where ∆ op denotes the comultiplication opposite to ∆,
(id ⊗ ∆) R = R13R12,(29)
(∆ ⊗ id)R = R13R23,(30)
where R12 = R ⊗ 1, R23 = 1 ⊗ R , etc. as usual, and such that there exists
¯R ∈ ∆(1)( H ⊗kH)∆ op(1) with
R ¯R = ∆ op(1), ¯RR = ∆(1) .(31)
Note that ¯R is uniquely determined by R: if ¯R and ¯R′ are two elements of
∆(1)( H ⊗kH)∆ op(1) satisfying the previous equation, then
¯R = ¯R∆ op(1) = ¯RR ¯R′ = ∆(1) ¯R′ = ¯R′.
For any two objects V and W of Rep(H) deﬁne cV,W : V ⊗W → W ⊗V as the
action of R21 :
cV,W (x) = R(2) ·x(2) ⊗R(1) ·x(1),(32)
where x =x(1) ⊗x(2) ∈V ⊗W and R = R(1) ⊗ R(2).
Proposition 5.2.2. The family of homomorphisms {cV,W }V,W deﬁnes a braiding
in Rep (H). Conversely, if Rep (H) is braided, then there exists R, satisfying the
properties of Deﬁnition 5.2.1 and inducing the given braidi ng.
FINITE QUANTUM GROUPOIDS AND THEIR APPLICA TIONS 17
Proof. Note that cV,W is well-deﬁned, since R21 = ∆(1) R21. To prove the H-
linearity of cV,W we observe that
cV,W (h ·x) = R(2)h(2) ·x(2) ⊗ R(1)h(1) ·x(1)
= h(1)R(2) ·x(2) ⊗h(2)R(1) ·x(1) =h · (cV,W (x)).
The inverse of cV,W is given by
c−1
V,W (y) = ¯R(1) ·y(2) ⊗ ¯R(2) ·y(1), where y =y(1) ⊗y(2) ∈W ⊗V,
therefore cV,W is is an isomorphism. Finally, we check the braiding identities. Let
x =x(1) ⊗x(2) ⊗x(3) ∈U ⊗V ⊗W , then
(idV ⊗cU,W )(cU,V ⊗ idW )(x) =
= (id V ⊗cU,W )(R(2) ·x(2) ⊗ R(1) ·x(1) ⊗x(3)
= R(2) ·x(2) ⊗ R′(2) ·x(3) ⊗ R′(1)R(1) ·x(1)
= R(2)
(1) ·x(2) ⊗ R(2)
(2) ·x(3) ⊗ R(1) ·x(1) =cU,V ⊗W (x).
Similarly, we have (cU,W ⊗ idV )(idU ⊗cV,W ) = cU⊗V,W .
The third equality of this computation shows that the relations of De ﬁnition 5.2.1
are equivalent to the braiding identities.
Lemma 5.2.3. Let (H, R) be a quasitriangular quantum groupoid. Then R satis-
ﬁes the quantum Yang-Baxter equation :
R12R13R23 = R23R13R12.
Proof. It follows from the ﬁrst two relations of Deﬁnition 5.2.1, that
R12R13R23 = (id ⊗ ∆ op)(R)R23 = R23(id ⊗ ∆)( R) = R23R13R12.
Remark 5.2.4. Let us deﬁne two linear maps R1, R2 : ˆH →H by
R1(φ) = (id ⊗φ)(R), R2(φ) = (φ ⊗ id)(R), for all φ ∈ ˆH.
Then condition (29) of Deﬁnition 5.2.1 is equivalent to R1 being a coalgebra ho-
momorphism and algebra anti-homomorphism and condition (30) is equ ivalent to
R2 being an algebra homomorphism and coalgebra anti-homomorphism. I n other
words, R1 : ˆH → H op and R2 : ˆH → H cop are homomorphisms of quantum
groupoids.
Proposition 5.2.5. For any quasitriangular quantum groupoid (H, R), we have:
(εs ⊗ id)(R) = ∆(1) , (id ⊗εs)(R) = (S ⊗ id)∆ op(1),
(εt ⊗ id)(R) = ∆ op(1), (id ⊗εt)(R) = (S ⊗ id)∆(1) ,
(S ⊗ id)(R) = ( id ⊗S−1)(R) = ¯R, (S ⊗S)(R) = R.
Proof. The proof is essentially the same as ([Ma], 2.1.5).
