---
doc_id: arxiv-math-0604094v1
doc_title: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant"
section_id: sec-003-once-punctured-torus-bundles-over-the-circle
section_title: "Once-Punctured Torus Bundles over the Circle"
section_number: null
pages: 19-26
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
doc_brief: "Generalized volume conjecture and the A-polynomials: the Neumann-Zagier potential function as a classical limit of quantum invariant — We study quantum invariant Zγ(M) for cusped hyperbolic"
---
One of beneﬁts of the quantum invariant Zγ(M) is that we can compute it explicitly for a
once-punctured torus bundle over S 1. A once-punctured torus bundle over S 1, which we denote
M(ϕ), is described by F × [0, 1]/(x, 0) ∼ (ϕ(x), 1) where a monodromy matrix ϕ ∈ S L(2, Z) is
a homeomorphism from the punctured torus F = T2 \ {0} to itself. Thurston’s hyperbolization
theorem indicates that M(ϕ) admits a complete hyperbolic metric with a ﬁnite volume whe n
ϕ has 2 distinct real eigenvalues. In this case, the monodromy matrix ϕ can be written up to
conjugation as
ϕ = Ls1 Rt1 · · ·LsnRtn (4.20)
where
L =
(
1 1
0 1
)
R =
(
1 0
1 1
)
with n > 0, and s j and t j are positive integers. Note that the complement of the ﬁgure-eight knot
studied in Sec. 4.1 corresponds to ϕ = L R =
(
2 1
1 1
)
.
It is known that we can triangulate the manifold Mϕ with ∑n
k=1(sk + tk) ideal tetrahedra [15],
and we have the quantum invariant as
Zγ (Mu(ϕ)) =
/iiiintegdisplay
R
da db dc dd δC(a, b, c, d; u) δG(a, b, c, d)
×
n∏
k=1








sk−1∏
i=0
⟨
dk,i, ck,i+1|S −1|dk,i+1, ck,i
⟩tk−1∏
j=0
⟨
bk, j, ak, j+1|S |bk, j+1, ak, j
⟩






 (4.21)
where gluing condition δG(a, b, c, d) means







bk,0 = ck+1,0
ak,0 = dk+1,0
for k = 1, 2, . . . ,n − 1







bn,0 = c1,0
an,0 = d1,0







bk,tk = ck,sk
ak,tk = dk,sk
for k = 1, 2, . . . ,n
20 K. HIKAMI
When we set the modulus of each oriented tetrahedra as
zk, j = eak, j−ak, j+1 wk, j = eck, j−ck, j+1
the developing map is drawn schematically as Fig. 6. We can th en read a condition
δC(a, b, c, d; u) for meridian as
u = 1
2
n∑
k=1
( ck,0 − ck,sk − ak,0 + ak,tk
) (4.22)
With these conditions, we have the quantum invariant Zγ (Mu(ϕ)), and the Neumann–Zagier
potential function can be given by taking a classical limit γ → 0. As far as we know, the A-
polynomial-type invariant for the once-punctured torus bundle over S 1 is not studied, but we can
obtain such polynomials from the Neumann–Zagier function.
Below we give a few examples for concreteness.
4.4.1 L2 R
We set ϕ = L2 R =
(
3 2
1 1
)
. The hyperbolic Dehn surgery of this manifold is studied in R ef. 4.
The invariant (4.21) is rewritten as
Zγ
(
Mu(L2 R)
)
=
∫
R
dp δC(p; u)
⟨
p1, p5|S −1|p6, p3
⟩ ⟨
p6, p4|S −1|p2, p5
⟩
⟨p3, p2|S |p4, p1⟩ (4.23)
When we set the modulus of tetrahedra as w0 = ep3−p5, w1 = ep5−p4, and z0 = ep1−p2, the develop-
ing map M(L2 R) can be depicted as Fig. 7. Then the meridian is read as
p3 − p4 − p1 + p2 = 2 u (4.24)
In the classical limit, we have
Zγ
(
Mu(L2 R)
)
∼
/iintegdisplay
dx dy exp
( 1
2 iγ VM(L2R)(ex, ey; eu)
)
(4.25)
where the potential function is computed as
VM(L2R)(x, y; m) = Li2
( 1
m2 x
)
− Li2
( 1
m2 x y2
)
− Li2
(
m2 x2 y2)
− log
(
m2)
log
(
m2 x2 y4)
− 2( log (x y)) 2 + π2
6 (4.26)
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 21
Figure 6. Schematic developing map for M(ϕ). Top vertex of tetrahedron with
modulus z1,0 is ﬁlled gray. Gray straight line denotes meridian.
The saddle point conditions (3.11), which correspond to thehyperbolic consistency condition,
reduce to (
−1 + m2 x
) (
−1 + m2 x2 y2
) 2
m4 x4 y2 ( −1 + m2 x y2) = 1
(
−1 + m2 x2 y2
)
m2 x ( −1 + m2 x y2) = 1
(4.27)
22 K. HIKAMI
Figure 7. Developing map of M(L2 R). Gray ﬁlled triangle is top vertex of the
tetrahedron with modulus z0. Gray curve is meridian.
and, as (3.12), the longitude is deﬁned by
ℓ = −(−1 + m2 x) (−1 + m2 x2 y2)
m4 x2 y2 (−1 + m2 x y2) (4.28)
In the case of complete casem = 1, we ﬁnd that (x, y2) =
( 1±
√
7 i
4 , −1±
√
7 i
2
)
solves the consistency
condition (4.27). Among these, we can check numerically that the largest value of the imaginary
part of the potential function at the saddle points
Im VM(L2R)(x, y; m = 1) = D
( 1
x
)
− D
( 1
x y2
)
− D
(
x2 y2)
coincides with the hyperbolic volume V ol
(
M(L2 R)
)
= 2.66674 · · ·.
The A-polynomial is now given by eliminating x and y from the set of equations, (4.27)
and (4.28), and we obtain the algebraic curve AM(L2R)(ℓ, m) = 0 whose Newton polygon is given
by














0 −1 0
0 2 1
1 2 0
0 −1 0














GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 23
4.4.2 L R3
We take another example ϕ = L R3 =
(
4 1
3 1
)
. In this case, the invariant (4.21) becomes
Zγ(Mu(L R3)) =
∫
R
dp δC(p; u) ⟨p1, p4|S |p3, p2⟩ ⟨p3, p6|S |p5, p4⟩
× ⟨p5, p8|S |p7, p6⟩
⟨
p2, p7|S −1|p8, p1
⟩
(4.29)
We set the modulus of each tetrahedron as
z0 = ep2−p4 z1 = ep4−p6
z2 = ep6−p8 w0 = ep1−p7
The developing map is depicted in Fig. 8, and the meridian is r ead as w0
z0 z1 z2
. We thus have a
condition of δC(p; u) as
p1 − p7 − p2 + p8 = 2 u (4.30)
Figure 8. Developing map of M(L R3).
In the classical limit, we obtain
Zγ(Mu(L R3)) ∼
/iiintegdisplay
dx dy dz exp
( 1
2 iγ VM(LR3)(ex, ey, ez; eu)
)
(4.31)
where the potential function is computed as
VM(LR3)(x, y, z; m) = − Li2
( 1
m4 y
)
+ Li2
( 1
m2 x y z2
)
+ Li2
(
m2 x2 z
)
+ Li2
( m2 y2 z
x
)
−
(
log
(
m2)) 2
+ 2 log
( x
m2
)
log
( x
y
)
+ 2 logy log(y z) + 2 logz log(x z m2) − π2
3 (4.32)
24 K. HIKAMI
In the case of complete case m = 1, we can check numerically that among algebraic solutions
of (3.11) the maximum of the imaginary part of VM(LR3)(x, y, z; m = 1),
Im VM(LR3)(x, y, z; 1) = −D
( 1
y
)
+ D
( 1
x y z2
)
+ D
(
x2 z
)
+ D
( y2 z
x
)
coincides with the hyperbolic volume V ol(M(L R3)) = 2.98912 · · ·. See Ref. 16 where algebraic
solutions of consistency equations are investigated in detail.
Correspondingly we obtain the A-polynomial for M(L R3) by eliminating x, y, and z from a
set of equations. Explicitly the polynomial AM(LR3)(ℓ, m) is given in the form of Newton polygon
as follows;





























0 0 0 1 0 0
0 0 0 −3 0 0
−1 −2 −3 −1 −2 0
0 −3 −2 2 3 0
0 2 1 3 2 1
0 0 3 0 0 0
0 0 −1 0 0 0





























5. C onclusion and Discussion
We have constructed quantum invariant Zγ(M) for cusped hyperbolic 3-manifolds M by as-
signing the Faddeev quantum dilogarithm function to oriented ideal tetrahedra. Once the triangu-
lation of cusped 3-manifold M is given, it is rather straightforward to deﬁne the invariant Zγ(M)
in an integral form. In the classical limit, the Faddeev inte gral reduces to the dilogarithm func-
tion, which denotes the hyperbolic volume of ideal tetrahed ron. Remarkable is that the saddle
point conditions coincide with the hyperbolic consistencyconditions around edges [19]. We have
discussed as a variant of the volume conjecture that the invariant Zγ(M), which can be regarded
as a generalization of the Kashaev invariant (speciﬁc value of the colored Jones polynomial), is
dominated by the hyperbolic volume in the classical limit γ → 0.
We have shown that the invariant can be deﬁned for a one-param eter deformation of mani-
fold Mu (not complete), and that the Neumann–Zagier potential function can be given by taking
a classical limit γ → 0. Correspondingly the A-polynomial can be computed from th e poten-
tial function (3.14). This supports the generalized volume conjecture. We have demonstrated by
taking examples that our method recovers previously known A-polynomial when M is a comple-
ment of hyperbolic knots. We have further applied our method in the case of the once-punctured
torus bundle over the circle. It seems that the A-polynomial -type invariant is not known for this
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 25
3-manifold, and it will be interesting to study a relationsh ip with the boundary slope. To con-
clude, our results indicate that the S -operator (2.13) denotes the quantum Bloch invariant for
oriented ideal tetrahedron.
The A-polynomial may give an interesting insight for mathematical physics. For example, the
Mahler measure of the A-polynomial is expected to coincide with the hyperbolic volume of knot.
On the other hand, the Mahler measure of the determinant of the Kasteleyn matrix has appeared
as the free energy of the dimer problem. From the viewpoint of our combinatorial construction
of the quantum invariant, the quantum invariants based on or iented ideal triangulation may be
interpreted as a matching of in-states and out-states, and i t might be interesting to investigate a
Kasteleyn matrix interpretation of the A-polynomial.
Acknowledgments
We have used computer programs, SnapPea [52], Knotscape [24], and Snap [11], in studying
triangulation of manifolds. We have also used Mathematica and Pari/GP. Pictures of knots in
this paper are drawn using KnotPlot [47]. This work is suppor ted in part by Grant-in-Aid for
Young Scientists from the Ministry of Education, Culture, S ports, Science and Technology of
Japan.
A. M ore Examples
We shall study the quantum invariant for other cusped manifolds. We give
• the quantum invariant Zγ(M) in terms of the S -operators,
• developing map when the number of the ideal tetrahedron is less than four,
• the condition δC(p; u), where u is a deformation parameter from the completeness u = 0,
• the Neumann–Zagier potential function VM(x; m), which follows from Zγ(M) by taking
the classical limit γ → 0,
• a solution of the saddle point equations in the complete case u = 0, which is checked
that the hyperbolic volume coincides with a maximal value of the imaginary part of the
potential function at this saddle point,
• the A-polynomial, which is given from the potential functio n VM(x; m) by eliminating
parameters x.
In the ﬁrst part A.1, we collect results for hyperbolic knots up to 7 crossings. Though the
A-polynomial is given in Ref. 9, we give an explicit form for s elf-completeness. In the second
26 K. HIKAMI
part A.2, we consider simple hyperbolic knots K xy from Ref. 6. Pictures of knot may be compli-
cated, but the triangulation of the complement is relativel y simple in these cases. We note that,
though the number of the ideal tetrahedra of the complement o f knot K xy is x in the case of the
canonical triangulation [52], our triangulations are diﬀerent.
