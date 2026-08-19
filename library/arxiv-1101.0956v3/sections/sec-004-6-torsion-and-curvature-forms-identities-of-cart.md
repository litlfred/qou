---
doc_id: arxiv-1101.0956v3
doc_title: "CONSTANTIN M. ARCUS ¸"
section_id: sec-004-6-torsion-and-curvature-forms-identities-of-cart
section_title: "Torsion and curvature forms. Identities of Cartan and Bianchi type"
section_number: 6
pages: 38-44
source_pdf: 1101.0956v3.pdf
source_sha256: 28fffdb404e88501
doc_brief: "CONSTANTIN M. ARCUS ¸ — In this paper we present the category of generalized Lie algebroids ."
---
Bianchi type
Using the theory of linear connections of Eresmann type pres ented in [1] for the diagram:
(6. 1)
E
π
/d15/d15
(
F, [, ]F,h , (ρ, Id N )
)
ν
/d15/d15
M
h /d47/d47N
where ( E, π, M ) ∈ | Bv| and
(
(F, ν, N ) , [, ]F,h , (ρ, Id N )
)
∈ | GLA| , we obtain a linear
ρ-connection ρΓ for the vector bundle ( E, π, M ) by components ρΓ a
bα .
Using the components of this linear ρ-connection, we obtain a linear ρ-connection
ρ ˙Γ for the vector bundle ( E, π, M ) given by the diagram:
(6. 2)
E
(
h∗F, [, ]h∗F ,
( h∗F
ρ , Id M
))
π ↓ ↓ h∗ν
M
Id M− − − − − − − − →M
If (E, π, M ) = ( F, ν, N ) , then, using the components of the same linear ρ-connection
ρΓ , we can consider a linear ρ-connection ρ¨Γ for the vector bundle ( h∗E, h ∗π, M ) given
by the diagram:
(6. 3)
h∗E
(
h∗E, [, ]h∗E ,
( h∗E
ρ , Id M
))
h∗π ↓ ↓ h∗π
M
Id M− − − − − − − − →M
,
Deﬁnition 6.1 If ( E, π, M ) = ( F, ν, N ), then the application
(6. 4) Γ (h∗E, h ∗π, M )2 (ρ,h )T− − − − − →Γ (h∗E, h ∗π, M )
(U, V ) − → ρT (U, V )
deﬁned by:
(6. 5) (ρ, h ) T (U, V ) = ρ ¨DU V − ρ ¨DV U − [U, V ]h∗E ,
23
for any U, V ∈ Γ (h∗E, h ∗π, M ) , will be called ( ρ, h )-torsion associated to linear ρ-
connection ρΓ .
Remark 6.1 In particular, if h = Id M , then we obtain the application
(6. 4′) Γ (E, π, M )2 ρT− − → Γ (E, π, M )
(u, v ) − → ρT (u, v )
deﬁned by:
(6. 5′) ρT (u, v ) = ρDuv − ρDvu − [u, v ]E ,
for any u, v ∈ Γ (E, π, M ) , which will be called ρ-torsion associated to linear ρ-connection
ρΓ .
Moreover, if ρ = Id T M, then we obtain the torsion T associated to linear connec-
tion Γ .
Proposition 6.1 The (ρ, h )-torsion (ρ, h ) T associated to linear ρ-connection ρΓ is
R-bilinear and antisymmetric.
If
(ρ, h ) T (Sa, S b)
put
= ( ρ, h ) Tc
abSc
then
(6. 6) ( ρ, h ) Tc
ab = ρΓ c
ab − ρΓ c
ba − Lc
ab ◦ h.
In particular, if h = Id M and ρT (sa, s b)
put
= ρTc
absc, then
(6. 6′) ρTc
ab = ρΓ c
ab − ρΓ c
ba − Lc
ab.
Moreover, if ρ = Id T M, then the equality (6. 6′) becomes:
(6. 6′′) Ti
jk = Γ i
jk − Γ i
kj .
Deﬁnition 6.2 If ( E, π, M ) = ( F, ν, N ), then the vector valued 2-form
(6. 7) ( ρ, h ) T = ((ρ, h ) Tc
abSc) Sa ∧ Sb
will be called the vector valued form of (ρ, h )-torsion (ρ, h ) T.
In particular, if h = Id M , then the vector valued 2-form
(6. 7′) ρT = (ρTc
absc) sa ∧ sb
will be called the vector form of ρ-torsion ρT.
Moreover, if ρ = Id T M, then the vector valued form (6 . 7′) becomes:
(6. 7′′) T =
(
Ti
jk
∂
∂x i
)
dxj ∧ dxk.
Deﬁnition 6.3 For each c ∈ 1, n we obtain the scalar 2-form of (ρ, h )-torsion
(ρ, h ) T
(6. 8) ( ρ, h ) Tc = (ρ, h ) Tc
abSa ∧ Sb.
24
In particular, if h = Id M , then, for each c ∈ 1, n, we obtain the scalar 2-form of
ρ-torsion ρT
(6. 8′) ρTc = ρTc
absa ∧ sb.
Moreover, if ρ = Id T M, then the scalar 2-form (6 . 9′) becomes:
(6. 8′′) Ti = Ti
jk dxj ∧ dxk.
Deﬁnition 6.4 The application
(6. 9) (Γ (h∗F, h ∗ν, M )2 ×Γ( E, π, M )
(ρ,h )R− − − − − →Γ( E, π, M )
((Z, V ), u ) − → ρR(Z, V )u
deﬁned by
(6. 10) ( ρ, h ) R (Z, V ) u = ρ ˙DZ
(
ρ ˙DV u
)
− ρ ˙DV
(
ρ ˙DZ u
)
− ρ ˙D[Z,V ]h∗F u,
for any Z, V ∈ Γ (h∗F, h ∗ν, M ) , u ∈ Γ (E, π, M ) , will be called ( ρ, h )-curvature associ-
ated to linear ρ-connection ρΓ .
Remark 6.2 In particular, if h = Id M , then we obtain the application
(6. 9′) Γ (F, ν, M )2 ×Γ( E, π, M )
ρR− − → Γ( E, π, M )
((z, v ), u ) − → ρR(z, v )u
deﬁned by
(6. 10′) ρR (z, v ) u = ρDz (ρDvu) − ρDv (ρDzu) − ρD[z,v ]F u,
for any z, v ∈ Γ (F, ν, M ) , u ∈ Γ (E, π, M ) , which will be called ρ-curvature associated
to linear ρ-connection ρΓ .
Moreover, if ρ = Id T M, then we obtain the curvature R associated to linear connec-
tion Γ .
Proposition 6.2 The (ρ, h )-curvature (ρ, h ) R associated to linear ρ-connection ρΓ ,
is R-linear in each argument and antisymmetric in the ﬁrst two ar guments.
If
(ρ, h ) R (Tβ , T α ) sb
put
= ( ρ, h ) Ra
b αβ sa,
then
(6. 11)
(ρ, h ) Ra
b αβ = ρj
β ◦ h ∂ρ Γ a
bα
∂x j + ρΓ a
eβ ρΓ e
bα − ρi
α ◦ h
∂ρ Γ a
bβ
∂x i
−ρΓ a
eα ρΓ e
bβ + ρΓ a
bγ Lγ
αβ ◦ h.
In particular, if h = Id M and ρR (tβ , t α ) sb
put
= ρRa
b αβ sa, then
(6. 11′) ρRa
b αβ = ρj
β
∂ρ Γ a
bα
∂x j + ρΓ a
eβ ρΓ e
bα − ρi
α
∂ρ Γ a
bβ
∂x i − ρΓ a
eα ρΓ e
bβ + ρΓ a
bγ Lγ
αβ .
Moreover, if ρ = Id T M, then equality (6. 11′) becomes:
(6. 11′′) Ra
b hk = ∂ Γ a
bh
∂x k + Γ a
ekΓ e
bh − ∂ Γ a
bk
∂x h − Γ a
ehΓ e
bk.
25
Deﬁnition 6.5 The vector mixed form
(6. 12) ( ρ, h ) R =
((
(ρ, h ) Ra
b αβ sa
)
T α ∧ T β
)
sb
will be called the vector valued form of (ρ, h )-curvature (ρ, h ) R.
In particular, if h = Id M , then the vector mixed form
(6. 12′) ρR =
((
ρRa
b αβ sa
)
tα ∧ tβ
)
sb
will be called the vector valued form of ρ-curvature ρR.
Moreover, if ρ = Id T M, then the vector form (6 . 12′) becomes:
(6, 12′′) R =
(
(Ra
b hk sa) dxh ∧ dxk)
sb.
Deﬁnition 6.6 For each a, b ∈
1, n we obtain the scalar 2-form of (ρ, h )-curvature
(ρ, h ) R
(6. 13) (ρ, h ) Ra
b = (ρ, h ) Ra
b αβ T α ∧ T β .
In particular, if h = Id M , then, for each a, b ∈
1, n, we obtain the scalar 2-form of
ρ-curvature ρR
(6. 13′) ρRa
b = ρRa
b αβ tα ∧ tβ .
Moreover, if ρ = Id T M, then the scalar form (6 . 13′) becomes:
(6. 13′′) Ra
b = Ra
b hk dxh ∧ dxk.
Theorem 6.1 The identities
(C1) ( ρ, h ) Ta = dh∗F Sa + Ω a
b ∧ Sb,
and
(C2) ( ρ, h ) Ra
b = dh∗F Ω a
b + Ω a
c ∧ Ω c
b
hold good. These will be called the ﬁrst respectively the seco nd identity of Cartan type.
Proof. To prove the ﬁrst identity we consider that ( E, π, M ) = ( F, ν, M ) . Therefore,
Ω a
b = ρΓ a
bcSc. Since
dh∗F Sa(U, V )Sa = ((Γ(
h∗F
ρ , Id M )U )Sa(V )
−(Γ(
h∗F
ρ , Id M )V )(Sa(U )) − Sa([U, V ]h∗F ))Sa
= (Γ(
h∗F
ρ , Id M )U )(V a) − (Γ(
h∗F
ρ , Id M )V )(U a) − Sa([U, V ]h∗F )Sa
= ρ ¨DU V − V bρ ¨DU Sb − ρ ¨DV U − U bρ ¨DV Sb − [U, V ]h∗F
= (ρ, h ) T(U, V ) − (ρΓ a
bcV bU c − ρΓ a
bcU bV c)Sa
= ((ρ, h ) Ta(U, V ) − Ω a
b ∧ Sb(U, V ))Sa,
it results the ﬁrst identity.
26
To prove the second identity, we consider that ( E, π, M ) ⁄= (F, ν, M ) . Since
(ρ, h ) Ra
b (Z, W ) sa = (ρ, h ) R ((W, Z ) , s b)
= ρ ˙DZ
(
ρ ˙DW sb
)
− ρ ˙DW
(
ρ ˙DZ sb
)
− ρ ˙D[Z,W ]h∗F sb
= ρ ˙DZ (Ω a
b (W ) sa) − ρ ˙DW (Ω a
b (Z) sa) − Ω a
b ([Z, W ]h∗F ) sa
+ (Ω a
c (Z) Ω c
b (W ) − Ω a
c (W ) Ω c
b (Z)) sa
=
(
dh∗F Ω a
b (Z, W ) + Ω a
c ∧ Ω c
b (Z, W )
)
sa
it results the second identity.
Corollary 6.1 In particular, if h = Id M , then the identities (C1) and (C2) become
(C ′
1) ρTa = dF sa + ω a
b ∧ sb,
and
(C ′
2) ρRa
b = dF ω a
b + ω a
c ∧ ω c
b
respectively.
Moreover, if ρ = Id T M, then the identities (C ′
1) and (C ′
2) become:
(C ′′
1 ) Ti = ddxi + ω i
j ∧ dxj = ω i
j ∧ dxj
and
(C ′′
2 ) Ri
j = dω i
j + ω i
h ∧ ω h
j ,
respectively. q.e.d.
Theorem 6.2 The identities
(B1) dh∗F (ρ, h ) Ta = (ρ, h ) Ra
b ∧ Sb − Ω a
c ∧ (ρ, h ) Tc
and
(B2) dh∗F (ρ, h ) Ra
b = (ρ, h ) Ra
c ∧ Ω c
b − Ω a
c ∧ (ρ, h ) Rc
b,
hold good. We will called these the ﬁrst respectively the sec ond identity of Bianchi type.
If the (ρ, h )-torsion is null, then the ﬁrst identity of Bianchi type beco mes:
( ˜B1) ( ρ, h ) Ra
b ∧ sb = 0.
Proof. We consider ( E, π, M ) = ( F, ν, M ) . Using the ﬁrst identity of Cartan type
and the equality dh∗F ◦ dh∗F = 0, we obtain:
dh∗F (ρ, h ) Ta = dh∗F Ω a
b ∧ Sb − Ω a
c ∧ dh∗F Sc.
Using the second identity of Cartan type and the previous ide ntity, we obtain:
dh∗F (ρ, h ) Ta = ((ρ, h ) Ra
b − Ω a
c ∧ Ω c
b) ∧ Sb − Ω a
c ∧
(
(ρ, h ) Tc − Ω c
b ∧ Sb
)
.
After some calculations, we obtain the ﬁrst identity of Bian chi type.
27
Using the second identity of Cartan type and the equality dh∗F ◦dh∗F = 0, we obtain:
dh∗F Ω a
c ∧ Ω c
b − Ω a
c ∧ dh∗F Ω c
b = dh∗F (ρ, h ) Ra
b .
Using the second of Cartan type and the previous identity, we obtain:
dh∗F (ρ, h ) Ra
b = ((ρ, h ) Ra
c − Ω a
e ∧ Ω e
c) ∧ Ω c
b − Ω a
c ∧ ((ρ, h ) Rc
b − Ω c
e ∧ Ω e
b) .
After some calculations, we obtain the second identity of Bi anchi type. q.e.d.
Corollary 6.2 In particular, if h = Id M , then the identities (B1) and (B2) become
(B′
1) dF ρTa = ρRa
b ∧ sb − ω a
c ∧ ρTc
and
(B′
2) dF ρRa
b = ρRa
c ∧ ω c
b − ω a
c ∧ ρRc
b,
respectively.
Moreover, if ρ = Id T M, then the identities (B′
1) and (B′
2) become:
(B′′
1 ) dTi = Ri
j ∧ dxj − ω i
k ∧ Tk
and
(B′′
2 ) dRi
j = Ri
h ∧ ω h
j − ω i
h ∧ Rh
j ,
respectively.
References
[1] C. M. Arcus, Algebraic constructions in the category of Lie algebroids ,
arXiv:math.DG/1101.0960v3, 20 Jul (2011).
[2] C. M. Arcus, Interior and exterior diﬀerential systems for Lie algebroids ,
arXiv:math-ph/1102.1781v2, 11 May (2011). (to appear)
[3] R.L. Bryant, S.S. Chern, R.B. Gardner, H.L. Goldschmidt , and P.A. Griﬃths, Ex-
terior Diﬀerential Systems, Springer-Verlag, 1991.
[4] J. Grabowski, P. Urbanski, Lie algebroids and Poisson-Nijenhuis structures, Rep.
Math. Phys. 40 (1997), 196-208.
[5] P Griﬃths, Exterior Diﬀerential Systems and the Calculus of Variations , Progr.
Math., No. 25, Birkh¨ auser, Boston, MA, 1983.
[6] T. A. Ivey and J. M. Landsberg, Cartan for Beginners: Diﬀerential Geometry via
Moving Frames and Exterior Diﬀerential Systems, Graduate Texts in Mathematics,
American Mathematical Society, 2003.
[7] N. Kamran, An elementary introduction to exterior diﬀerential system s, In “Geo-
metric approaches to diﬀerential equations (Canberra, 1995 )”, volume 15 of Austral.
Math. Soc. Lect. Ser., Cambridge Univ. Press, Cambridge, (2 000), pages 100–115.
28
[8] K. Mackenzie, Lie Grupoids and Lie Algebroids in Diﬀerential Geometry, London
Math. Soc. Lecture Notes Series 124 Cambridge Univ. Press, C ambridge, (1987).
[9] C.M. Marle, Lie algebroids and Lie pseudoalgebras , arxiv:math DG/0806.0919v2,
(2008).
29
