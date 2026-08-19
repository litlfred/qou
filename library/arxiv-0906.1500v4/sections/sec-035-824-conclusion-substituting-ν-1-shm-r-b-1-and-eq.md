---
doc_id: arxiv-0906.1500v4
doc_title: "TWISTED ALEXANDER INV ARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS"
section_id: sec-035-824-conclusion-substituting-ν-1-shm-r-b-1-and-eq
section_title: "Conclusion. Substituting ν = 1, s(H∗(M ; R)) = b + 1 and Equation (37) into"
section_number: 8.2.4
pages: 25-28
source_pdf: 0906.1500v4.pdf
source_sha256: 9a586f6d134ca47f
doc_brief: "TWISTED ALEXANDER INVARIANT AND NON–ABELIAN REIDEMEISTER TORSION FOR HYPERBOLIC THREE–DIMENSIONAL MANIFOLDS WITH CUSPS — W e study a computational method of the hyperbolic Reidemeister torsion (also"
---
Equation (34) we obtain that
(38) ∆ ϕ⊗Ad◦ρ
M (t) = ǫ(−1)b∆ ϕ⊗Ad◦ρ
∂M (t)∆
ϕ⊗Ad◦ρ
M (t).
Finally, using Equation (35), we can see that Equation (38) turns int o
∆ ϕ⊗Ad◦ρ
M (t) = ǫ(−1)b+b(b−1)/2∆ ϕ⊗Ad◦ρ
M (t) = ǫ(−1)b(b+1)/2∆ ϕ⊗Ad◦ρ
M (t)
which achieves the proof of Theorem 14. □
Appendix A. A natural homology orientation for link exterior
In this section, we exhibit a natural, and in a sense compatible, homolo gy orientation
in the case where M is the exterior EL = S3 \ N (L) of a link L in S3. Here N (L)
denotes a tubular neighborhood of L. Observe that the boundary ∂M of M consists in
the disjoint union of b tori T 2
1 , . . . , T2
b . For more details on homology orientations the
reader is invited to refer to Turaev’s monograph [Tur02].
The deﬁnition of the homology orientation needs some orientation co nventions. We
suppose that S3 and L are oriented. Thus EL = S3 \ N (L) and each torus T 2
ℓ inherits
the orientation induced by the one of S3. Moreover each torus T 2
ℓ is given together with
its peripheral-system ( λℓ, µℓ), where λℓ, the longitude, and µℓ, the meridian, generates
H1(T 2
ℓ ; Z) ≃ Z ⊕ Z. These two curves are oriented using the following rules: µℓ is
oriented using the convention ℓk (µℓ, L) = +1, and λℓ is oriented using the convention
int(µℓ, λℓ) = +1.
In what follows, we construct natural homology orientations for t he link exterior EL,
for its boundary ∂EL = ⋃ b
ℓ=1 T 2
ℓ and for the pair ( EL, ∂EL).
A.1. Homology groups and homology orientations. We begin our investigations
by describing in details the homology groups of the link exterior EL, of its boundary
∂EL = ⋃ b
ℓ=1 T 2
ℓ and of the pair ( EL, ∂EL).
The homology groups of the torus T 2
ℓ are given as follows:
H2(T 2
ℓ ; R) = R [ [T 2
ℓ ] ], H 1(T 2
ℓ ; R) = R [ [λℓ] ]⊕ R [ [µℓ] ], H 0(T 2
ℓ ; R) = R [ [pℓ] ].
Here [ [T 2
ℓ ] ] is the fundamental class induced by the orientation of T 2
ℓ , [ [µℓ] ] and [ [λℓ] ] are
given by the oriented meridian and the oriented longitude (see above ) and [ [pℓ] ] is the
homology class of the base point.
An application of Mayer-Vietoris sequence associated to the followin g decomposition
of the three–sphere: S3 = EL ∪ (⋃ b
ℓ=1 S1 × D2
ℓ ) gives us the following generators for the
homology groups of EL:
H2(EL; R) =
b−1⨁
ℓ=1
R [ [T 2
ℓ ] ], H 1(EL; R) =
b⨁
ℓ=1
R [ [µℓ] ], H 0(EL; R) = R [ [pb] ].
To describe the homology groups of the pair ( EL, ∂EL) we use Poincar´ e duality and
get the following generators:
H3(EL, ∂EL; R) = R [ [EL, ∂EL] ],
H2(EL, ∂EL; R) = R [ [S1] ]⊕ · · · ⊕ R [ [Sb] ],
H1(EL, ∂EL; R) = R [ [γ1] ]⊕ · · · ⊕ R [ [γb−1] ].
25
Here [ [EL, ∂EL] ] = [ [pb] ]∗ is the fundamental class induced by orientations. If Sℓ denotes
the restriction of a Seifert surface of the component Kℓ in L to EL, then its class [ [Sℓ] ] =
[ [µℓ] ]∗. And ﬁnally, if γℓ denotes a path connecting the point pℓ to pb, then its class
[ [γℓ] ] = [ [T 2
ℓ ] ]∗.
The homology orientations we ﬁx on ∂EL, EL and (EL, ∂EL) are respectively induced
by the following ordered bases:
H∗(∂EL; R) =
⟨
[ [T 2
1 ] ], . . . ,[ [T 2
b ] ], [ [λ1] ], [ [µ1] ], . . . ,[ [λb] ], [ [µb] ], [ [p1] ], . . . ,[ [pb] ]
⟩
R ,
H∗(EL; R) =
⟨
[ [T 2
1 ] ], . . . ,[ [T 2
b−1] ], [ [µ1] ], . . . ,[ [µb] ], [ [pb] ]
⟩
R ,(39)
H∗(EL, ∂EL; R) = ⟨[ [EL, ∂EL] ], [ [S1] ], . . . ,[ [Sb] ], [ [γ1] ], . . . ,[ [γb−1] ]⟩R .
A.2. A sign term. This combination of bases for the pair ( EL, ∂EL) are natural in
the sense that they are given by Poincar´ e duality. In the case of lin k exteriors, using
such homology orientations we will ﬁx numbers of sign indeterminacy in our formulas.
However, to be exhaustive it remains to us to explicitly compute the R eidemeister torsion
of the long exact sequence in homology associated to the pair ( EL, ∂EL). This torsion is
a new sign term, given in the following proposition, which will give us the s ign–term in
the symmetry formula for the polynomial torsion (see Section 8, in p articular Theorem 14
and Equation (32)).
Proposition 16. The torsion of the long exact sequence in homology associate d to the
pair (EL, ∂EL), in which homology groups are endowed with the distinguishe d bases given
in Equation (39), is equal to (−1)b(b−1)/2.
Proof. Let H∗ denotes the long exact sequence in homology associated to the pair
(EL, ∂EL). Counting dimensions, it is easy to observe that H∗ is decomposed into the
following three short exact sequences:
(40) H(i)
∗ : 0 → Hi+1(EL, ∂EL; R)
δ(i)
− − →Hi(∂EL; R)
−j(i)
∗
− − − →Hi(EL; R) → 0
for i = 0, 1, 2. Here δ(i) denotes the connecting homomorphism and j(i)
∗ is induced by the
usual inclusion ∂EL֒→EL. Thus, the torsion of H∗ is equal to the alternative product
of the three torsions of the above short exact sequences (40).
The torsions are computed with respect to the bases given in Equat ion (39) and we
have:
Claim 17. The Reidemeister torsions of the short exact sequences H(i)
∗ are given by:
Tor(H(2)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅) = ( −1)b−1,
Tor(H(1)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅) = ( −1)b(b−1)/2,
Tor(H(0)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅) = ( −1)b−1.
Proof of the claim. Each torsion of the short exact sequences H(i)
∗ can be calculated as
follows.
• Computation of Tor(H(2)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅).
The connecting homomorphism δ(2) maps [ [EL, ∂EL] ] to [ [T 2
1 ] ] +· · · + [ [T 2
b ] ].
Moreover one has
j(2)
∗ ([ [T 2
ℓ ] ]) = [ [T 2
ℓ ] ] for ℓ = 1, . . . , b− 1.
Thus the set {[ [T 2
1 ] ], . . . ,[ [T 2
b−1] ]} of vectors in H2(∂EL; R) can be chosen as lifts of
the distinguished basis of H2(EL; R). As a result, the torsion of this short exact
26
sequence H(2)
∗ is given by the following base change determinant:
Tor(H(2)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅)
=
[
{δ([ [EL, ∂EL] ]), [ [T 2
1 ] ], . . . ,[ [T 2
b−1] ]}/{[ [T 2
1 ] ], [ [T 2
2 ] ], . . . ,[ [T 2
b ] ]}
]
=
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
1 1
.
.
. . . .
1 1
1
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
⏐
= (−1)b−1.
• Computation of Tor(H(1)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅).
The connecting homomorphism δ(1) maps [ [Sℓ] ] to [ [λℓ] ] +∑
k⁄=ℓ ℓk(Kℓ, Kk)[ [µk] ]
where ℓk denotes the linking number. Moreover, j(1)
∗ ([ [µℓ] ]) = [ [µℓ] ], for ℓ =
1, . . . , b. Thus, the set {[ [µ1] ], . . . ,[ [µb] ]} of vectors in H1(∂EL; R) can be chosen
as lifts of the distinguished basis of H1(EL; R). It follows that the torsion of the
short exact sequence H(1)
∗ is given by the ratio of the following two determinants
of bases change matrices:
Tor(H(1)
∗ , {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅)
= [{δ([ [S1] ]), . . . , δ([ [Sb] ]), [ [µ1] ], . . . ,[ [µb] ]}/{[ [λ1] ], [ [µ1] ], . . . ,[ [λb] ], [ [µb] ]}] .(41)
Observe that the determinant in the right-hand side of Equation (4 1) can be
written again as the product of the following two base change deter minants:
D1 = [{δ([ [S1] ]), . . . , δ([ [Sb] ]), [ [µ1] ], . . . ,[ [µb] ]}/{[ [λb] ], . . . ,[ [λ1] ], [ [µ1] ], . . . ,[ [µb] ]}] ,
D2 = [{[ [λb] ], . . . ,[ [λ1] ], [ [µ1] ], . . . ,[ [µb] ]}/{[ [λ1] ], [ [µ1] ], . . . ,[ [λb] ], [ [µb] ]}] .
It is easy to observe that
D1 = [{[ [λ1] ], . . . ,[ [λb] ], [ [µ1] ]. . . ,[ [µb] ]}/{[ [λb] ], . . . ,[ [λ1] ], [ [µ1] ], . . . ,[ [µb] ]}]
=
⏐
⏐
⏐
⏐
⏐
⏐
⏐
0 · · · 1
.
.
.
. . . .
.
.
1 · · · 0
⏐
⏐
⏐
⏐
⏐
⏐
⏐
= (−1)b(b−1)/2,
and that D2 = 1, because it is the signature of a product of even permutations.
As a conclusion, we have that
Tor(H(1)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅) = ( −1)b(b−1)/2.
• Computation of Tor(H(0)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅).
The connecting homomorphism δ(0) maps [ [γℓ] ] to [ [pb] ]− [ [pℓ] ], for all ℓ =
1, . . . , b− 1. Also observe that j(0)
∗ ([ [pb] ]) = [ [pb] ]. Thus, the torsion of the short
exact sequence H(0)
∗ is given by the following base change determinant:
Tor(H(0)
∗ , {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) = [ {δ([ [γ1] ]), . . . , δ([ [γb−1] ]), [ [p1] ]}/{[ [p1] ], . . . ,[ [pb] ]}]
=





−1
.
.
. . . .
−1
1 · · · 1 1




 = (−1)b−1.
□
Using this result, we conclude that the torsion Tor( H∗, {h∗
EL, h∗
∂EL, h∗
(EL,∂EL)}, ∅) of
H∗ is given by ∏ 2
i=0 Tor(H(i)
∗ , {h∗
EL, h∗
∂EL , h∗
(EL,∂EL)}, ∅)
(−1)i
= (−1)b(b−1)/2. □
27
