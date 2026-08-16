---
doc_id: arxiv-1112.5179v1
doc_title: "Prepared for submission to JHEP 3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA "
section_id: sec-009-42-the-bipyramid
section_title: "The bipyramid"
section_number: 4.2
pages: 25-28
source_pdf: 1112.5179v1.pdf
source_sha256: b58af08336c40994
doc_brief: "3-Manifolds and 3d Indices Tudor Dimofte1,2 Davide Gaiotto 1 Sergei Gukov 3,4 1Institute for Advanced Study, Einstein Dr., Princeton, NJ 08540, USA 2Trinity College, Cambridge CB2 1TQ, UK — We"
---
As a simple but crucial example of a nontrivial 3-manifold, let us takeM to be the bipyramid,
shown in the center of Figure 3. The bipyramid can be decomposed into either 2 or 3
tetrahedra, leading to two diﬀerent UV descriptions of the theory TM. It was shown in
[19] that, with an appropriate polarization, the gluing of two tetrahedra produces Nf = 1
SQED, while the gluing of three tetrahedra produces the so-called XYZ model, a theory of
three chiral multiplets coupled by a cubic superpotential. The fact that these theories are
mirror symmetric [5] formed the basis of the argument that the construction ofTM for general
3-manifolds is triangulation independent (see also [34]).
z
z￿z￿￿
z
z￿
z￿￿
w
w￿
w￿￿
w
w￿
w￿￿
y
y￿
y￿￿
y
y￿
y￿￿
r
r￿
r￿￿
r
r￿
r￿￿
s
s￿
s￿￿
s
s￿ s￿￿ x1 x2
p1
p2
Figure 3. The bipyramid, in its two triangulations. The equatorial polarization Π = ( X1,X 2;P1,P 2)
has positions X1 and X2 corresponding to the two equatorial edges in the front.
Here we calculate the index IM for the bipyramid. The boundary phase space P∂M is
four-dimensional, with two position coordinates corresponding to the U(1)2 ﬂavor symmetry
of eitherNf = 1 SQED or the XYZ model. Let us choose an equatorial polarization for P∂M ,
with position coordinates x1,2 = exp(X1,2) and momentum coordinates p1,2 = exp(P1,2)
associated to the external edges shown in Figure 3.
– 24 –
For the decomposition into two tetrahedra ∆ R and ∆S, we ﬁrst form the product index
I{∆R,∆S},{ΠR,ΠS}(mR,mS,eR,eS) = I∆(mR,eR)I∆(mS,eS). (We continue to suppress the
dependence of indices on the parameter q.) Then observe that


X1
X2
P1
P2

 =


R +S′′
R′′ +S
R′′
S′′

 =


1 0 0 1
0 1 1 0
0 0 1 0
0 0 0 1




R
S
R′′
S′′

 . (4.7)
Therefore, Π = ~Π =gSp· (ΠR× ΠS), where gSp is the symplectic matrix on the right side of
(4.7). There is no aﬃne shift. Correspondingly, the index transforms as
IM,Π(m1,m 2,e 1,e 2) =
(
−q
1
2
)⟨0,(m,e)⟩I{∆R,∆S},{ΠR,ΠS}
(
g−1
Sp (m1,m 2,e 1,e 2)
)
=I∆(m1−e2,e 1)I∆(m2−e1,e 2). (4.8)
Since there are no internal edges, this is automatically the index of the bipyramid theory.
Physically, (4.8) counts states in Nf = 1 SQED on S2×S1. To be very explicit, this
theory starts out with a ﬂat-space Lagrangian 12
LM,Π = 1
4π
∫
d4θ
(
Σ1V2 + (Σ1 + 2V2)V
)
+
∫
d4θ
(
φ†
ReV + 1
2V1φR +φ†
S′′e−V + 1
2V1φS′′
)
, (4.9)
whereV is dynamical, V1 is a background vector multiplet for the axial U(1) symmetry, and
V2 is a background vector multiplet for a slightly modiﬁed topological U(1) symmetry. Some
additional background Chern-Simons couplings are turned on, and one can also work out
the appropriate R-charges and fermions numbers chosen for putting the theory on S2×S1
(corresponding to our equatorial polarization Π). Then
IM,Π(m1,m 2;q,ζ 1,ζ 2) = TrHm1,m2(−1)Fq
R
2 +j3ζe1
1 ζe2
2 =
∑
e1,e2∈Z
IM,Π(m1,m 2,e 1,e 2;q)ζe1
1 ζe2
2 ,
(4.10)
where e1 and e2 count axial and topological charges, and m1 and m2 specify the amount of
axial and topological ﬂux, respectively, through S2.
For the triangulation into three tetrahedra ∆ Z, ∆W, ∆Y , we again start with a product
indexI{∆i},{Πi}(m,e ) = I∆(mZ,eZ)I∆(mW,eW )I∆(mY,eY ). Now, however, the product
phase spaceP∂∆Z×P∂∆W×P ∆Y is six-dimensional, and there is an internal edge. We choose
an intermediate polarization ~Π = (X1,X 2,C ;P1,P 2, Γ) on the product phase space that is
compatible with Π and also includes C = Z +W +Y , the internal edge parameter, as a
position coordinate. Here Γ = −Y′ (say) is a conjugate momentum to C that commutes with
12This particular Lagrangian is found after doing an σeST rotation (a mirror symmetry) of the ∆S tetrahe-
dron; see Section 4.2 of [19].
– 25 –
the external edges. Then


X1
X2
C
P1
P2
Γ


=


Z
W
Z +W +Y
Z′′ +Y′
W′′ +Y′
−Y′


=


1 0 0 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0−1 1 0 −1
0 0−1 0 1 −1
0 0 1 0 0 1




Z
W
Y
Z′′
W′′
Y′′


+


0
0
0
iπ + ℏ
2
iπ + ℏ
2
−iπ− ℏ
2


, (4.11)
so the aﬃne symplectic transformation from {Πi} to ~Π is σ(α)gSp with gSp the matrix
appearing in (4.11) and a shift vector α = (0, 0, 0, 1, 1,−1). Correspondingly,
I{∆i},˜Π(m,e ) =
(
−q
1
2
)⟨α,(m,e)⟩I{∆i},{Πi}
(
g−1
Sp (m,e )
)
=
(
−q
1
2
)m1+m2−m3
I∆(m1,e 1 +e3)I∆(m2,e 2 +e3)I∆(m3−m1−m2,e 3 +m1 +m2−m3).
Finally, to obtain the index of the bipyramid theory, we sum over the electric charge e3
corresponding to the internal edge, and set m3 = 0 :
IM,Π(m,e ) =
∑
e3∈Z
(
−q
1
2
)2e3+m1+m2
I∆(m1,e 1 +e3)I∆(m2,e 2 +e3)I∆(−m1−m2,e 3 +m1 +m2)
=
∑
e3∈Z
qe3I∆(m1,e 1 +e3)I∆(m2,e 2 +e3)I∆(m1 +m2,e 3) (4.12)
(the last simpliﬁcation follows by parity symmetry (3.9)). It is not too hard to see that (4.12)
is a reasonable index for the XYZ model, with the cubic superpotential breaking a diagonal
U(1) ﬂavor symmetry and leading to a sum over its charge sectors.
The equivalence of (4.8) and (4.12) can be proven using diﬀerence equations, much in
the same way that we demonstrateσeST –invariance of the tetrahedron index in Appendix A.
Of course, these two expressions must be equal on physical grounds, because they are indices
for mirror symmetric theories. Computationally, it is very easy to check equivalence at any
ﬁxed charge γ = (m,e ), order by order in q. For example, both expressions give
IM,Π(0, 0, 0, 0) = 1− 2q− 3q2 + 4q4 + 12q5 + 14q6 + 6q8 +... ,
IM,Π(1, 3, 2, 4) =−q6− 2q7− 4q8− 6q9− 8q10− 9q11− 8q12 +... ,
etc. Only a ﬁnite number of terms in the sum (4.12) is needed at any given order. In [16, 17]
the match was also proven at special values of m = (m1,m 2) using diﬀerent methods.
The equivalence of (4.8) and (4.12) and theσeST -invariance ofI∆ are the basic nontrivial
ingredients in a combinatorial argument that IM,Π is a topological invariant of ( M, Π) —
independent of triangulation or any other choices. Again, this must be the case physically as
long as TM is well deﬁned, but it us useful to have a more bottom-up understanding. The
σeST -invariance shows that it does not matter how one labels edge parameters of individual
tetrahedra in a triangulation, as long as their cyclic ordering (induced by the orientation of
– 26 –
M) is preserved. The 2-3 invariance of the bipyramid index is then enough to show that the
index of any triangulated 3-manifold is independent of triangulation. In particular, the 2-3
invariance must work for any boundary polarization of the bipyramid (it is trivial to show
this), and seems to commute with the operation of gluing the bipyramid into a larger 3-
manifold — as long as the larger triangulation has no univalent edges. 13 Then, conjecturally,
the set of triangulations of M with no univalent edges is fully connected by 2–3 moves, and
triangulation invariance follows.
It would be useful to have a more rigorous understanding of convergence, its relation to
combinatorics of triangulations, and how 2–3 moves act to connect restricted sets of trian-
gulations — such as those without univalent edges. Mathematically, this is still uncharted
territory.
