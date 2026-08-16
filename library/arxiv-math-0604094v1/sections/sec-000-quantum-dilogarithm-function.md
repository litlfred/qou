---
doc_id: arxiv-math-0604094v1
doc_title: "GENERALIZED VOLUME CONJECTURE AND THE A-POLYNOMIALS: THE NEUMANN–ZAGIER POTENTIAL FUNCTION AS A CLASSICAL LIMIT OF QUANTUM INV ARIANT KAZUHIRO HIKAMI"
section_id: sec-000-quantum-dilogarithm-function
section_title: "Quantum Dilogarithm Function"
section_number: null
pages: 2-12
source_pdf: 0604094v1.pdf
source_sha256: f0c4c36ab0acf537
doc_brief: "GENERALIZED VOLUME CONJECTURE AND THE A-POLYNOMIALS: THE NEUMANN–ZAGIER POTENTIAL FUNCTION AS A CLASSICAL LIMIT OF QUANTUM INVARIANT KAZUHIRO HIKAMI — We study quantum invariant Zγ(M) for cusped"
---
introduced his invariant JK
(
N; e2πi/N
)
for triangulated 3-manifolds, although the R-matrix con-
struction is developed subsequently [28]. He studied Fadde ev’s quantum dilogarithm function
when q is a root of unity [13, 26] (see also Ref. 2), and assigning the quantum dilogarithm func-
tion to ideal tetrahedron he deﬁned invariant [27, 28]. In th is sense, our invariant Zγ(M) for
M with complete hyperbolic structure can be regarded as a non- compact Uq(sl(2; R)) analogue
of the Kashaev invariant, and an asymptotic behavior of Zγ(S 3 \ K ) in the limit γ → 0 should
coincide with that of the Kashaev invariant JK
(
N; e2πi/N
)
in the limit N → ∞.
This paper is organized as follows. In Section 2 we recall deﬁ nitions of quantum dilogarithm
function, and we discuss properties of this function. In Sec tion 3, we shall reveal that the three-
dimensional hyperbolic geometry naturally arises from the quantum dilogarithm function in the
classical limit γ → 0 as was clariﬁed in Ref. 19. Then we deﬁne the quantum invaria nt Zγ(Mu)
for a deformation of complete hyperbolic cusped 3-manifold M. Based on a triangulation of
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 3
M, we construct the invariant by assigning quantum dilogarithm function to oriented ideal tetra-
hedron. We discuss that the Neumann–Zagier potential funct ion appears in a classical limit of
Zγ(M). In Section 4, we take several examples of cusped hyperbolic manifolds such as comple-
ments of hyperbolic knots and punctured torus bundle over th e circle, and explain our assertion
in detail. We shall also give a list for other manifolds in Appendix. The last section is devoted to
conclusions and discussions.
2. Q uantum Dilogarithm Function
We deﬁne a function Φγ(ϕ) by an integral form following Ref. 12. We set γ ∈ R, and for
| Im ϕ| < π, we deﬁne
Φγ(ϕ) = exp










∫
R+i 0
e−i ϕ x
4 sinh(γ x) sinh(π x)
dx
x









 (2.1)
The Faddeev integral (2.1), which we call the quantum diloga rithm function, is also related to
the double sine function [31, 34, 48], the hyperbolic gamma f unction [1, 46] and the quantum
exponential function [54]. We see that the integral Φγ(ϕ) has a duality,
Φπ2
γ
(ϕ) = Φγ
( γ
π ϕ
)
(2.2)
and that it satisﬁes the inversion relation,
Φγ(ϕ) · Φγ(−ϕ) = exp
(
− 1
2 iγ
( ϕ2
2 + π2 + γ2
6
) )
(2.3)
The Faddeev integral satisﬁes the diﬀerence equations;
Φγ(ϕ + i γ)
Φγ(ϕ − i γ) = 1
1 + eϕ (2.4a)
Φγ(ϕ + i π)
Φγ(ϕ − i π) = 1
1 + e
π
γ ϕ (2.4b)
Due to these relations, the integral Φγ(ϕ) deﬁned in (2.1) is analytically continued to ϕ ∈ C, and
we see that
zeros of ( Φγ(ϕ)) ±1 =
{
ϕ = ∓i( (2 m + 1) γ + (2 n + 1) π) ⏐
⏐
⏐m, n ∈ Z≥0
}
(2.5)
The most important properties of the Faddeev integral is tha t it fulﬁlls the pentagon iden-
tity [12, 13]
Φγ( ˆp) Φγ(ˆq) = Φγ(ˆq) Φγ( ˆp + ˆq) Φγ( ˆp) (2.6)
4 K. HIKAMI
where ˆp and ˆq are the canonically conjugate operators satisfying the Hei senberg commutation
relation,
[ ˆp , ˆq] = ˆp ˆq − ˆq ˆp = −2 iγ (2.7)
By this commuting relation, we call a limit γ → 0 a classical limit.
We use V as the momentum space |p⟩with p ∈ R which is an eigenstate of the momentum
operator;
ˆp |p⟩= p |p⟩. (2.8)
A reason of the quantum dilogarithm function reveals when we take a classical limit γ → 0.
In this limit, the Faddeev integral reduces to
Φγ(ϕ) ∼ exp
( 1
2 iγ Li2(−eϕ)
)
(2.9)
where Li2(x) denotes the Euler dilogarithm function deﬁned by (see, e.g., Refs. 32, 36)
Li2(x) =
∞∑
n=1
xn
n2 (2.10)
where |x| ≤ 1. For x ∈ C, we use the integral form
Li2(x) = −
∫ x
0
log(1 − s) ds
s
where the branch of log(1 − s) is on C \ [1, ∞) for which log(1 − 0) = 0. See that the inversion
relation (2.3) of the quantum dilogarithm function Φγ(ϕ) gives that of the Euler dilogarithm
function as
Li2(−ex) + Li2(−e−x) + x2
2 + π2
6 = 0
We note that the Fourier transformation of the Faddeev integral can be computed as follows [5,
14, 31, 54];
1√
4 π γ
∫
R
dy Φγ(y) e
1
2 iγ x y = Φγ(−x + iπ + iγ) e
1
2 iγ
(
x2
2 − 1
2 πγ− π2+γ2
6
)
(2.11)
1√
4 π γ
∫
R
dy 1
Φγ(y) e
1
2 iγ x y = 1
Φγ(x − i π − i γ) e
− 1
2 iγ
(
x2
2 − 1
2 πγ− π2 +γ2
6
)
(2.12)
To see a relationship between the integral Φγ(ϕ) with geometry, we deﬁne the S -operator
acting on V ⊗ V by
S 1,2 = e
1
2 iγ ˆq1 ˆp2 Φγ( ˆp1 + ˆq2 − ˆp2) (2.13)
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 5
Here the Heisenberg operators ˆp j and ˆq j act on the j-th vector space of V ⊗ V, i.e. ˆp1 = ˆp ⊗ 1,
ˆp2 = 1 ⊗ ˆp, and so on. Then the pentagon identity (2.6) can be rewritten in a compact form;
S 2,3 S 1,2 = S 1,2 S 1,3 S 2,3 (2.14)
where S j,k acts on the j- and k-th spaces of V ⊗ V ⊗ V. Matrix elements can be computed by use
of (2.11) and (2.12);
⟨p1, p2 | S 1,2 | p′
1, p′
2⟩
= 1
√
4 π γ
δ(p1 + p2 − p′
1) · Φγ(p′
2 − p2 + i π + i γ) e
1
2 iγ
(
− π2+γ2
6 − γ π
2 +p1 (p′
2−p2)
)
(2.15a)
⟨p1, p2 | S −1
1,2 | p′
1, p′
2⟩
= 1
√
4 π γ
δ(p1 − p′
1 − p′
2) 1
Φγ(p2 − p′
2 − i π − i γ) e
1
2iγ
(
π2+γ2
6 + γ π
2 −p′
1(p2−p′
2)
)
(2.15b)
In the classical limit γ → 0, we ﬁnd by use of (2.9) that the S -operators (2.15) reduce to
⟨p1, p2 | S 1,2 | p′
1, p′
2⟩ ∼δ(p1 + p2 − p′
1) · exp
(
− 1
2 iγ V(p′
2 − p2, p1)
)
(2.16a)
⟨p1, p2 | S −1
1,2 | p′
1, p′
2⟩ ∼δ(p1 − p′
1 − p′
2) · exp
( 1
2 iγ V(p2 − p′
2, p′
1)
)
(2.16b)
where we have deﬁned the function V(x, y) by
V(x, y) = π2
6 − Li2(ex) − x y. (2.17)
We see that the function V(x, y) satisﬁes partial diﬀerential equations;
V(x, y) = L(1 − ex) + 1
2
(
x ∂V(x, y)
∂x + y ∂V(x, y)
∂y
)
(2.18)
Im V(x, y) = D(1 − ex) + log |ex| · Im
( ∂
∂xV(x, y)
)
+ log |ey| · Im
( ∂
∂yV(x, y)
)
(2.19)
Here the Rogers dilogarithm L(z) and the Bloch–Wigner function D(z) are respectively deﬁned
in terms of the Euler dilogarithm function (2.10) by
L(z) = Li2(z) + 1
2 log z log(1 − z) (2.20)
D(z) = Im Li 2(z) + arg(1 − z) · log |z| (2.21)
6 K. HIKAMI
both of which fulﬁll the pentagon identity (see, e.g., Ref. 36);
L(z) − L(w) + L
( w
z
)
− L
( 1 − z−1
1 − w−1
)
+ L
( 1 − z
1 − w
)
= π2
6 (2.22)
D(z) − D(w) + D
( w
z
)
− D
( 1 − z−1
1 − w−1
)
+ D
( 1 − z
1 − w
)
= 0 (2.23)
3. Q uantum Inv ariant andPotential Function
The result that theS -operator satisﬁes the pentagon identity (2.14) indicatesthat we can assign
(oriented) tetrahedron to each S -operator. See Refs. 7, 30 (also Ref. 8) for another interpretation
as a quantization of the Teichm¨ uller theory. In the classical limit γ → 0, imaginary part of the
S -operator gives the Bloch–Wigner function D(z) which denotes the hyperbolic volume of the
ideal tetrahedron ∆(z) with totally geodesic faces which has a modulusz (see, e.g., Refs. 3,38,50).
Extra terms in (2.19) including partial diﬀerentials of V(x, y) can be neglected when we assume a
saddle point condition as will be discussed later, and we can assign the oriented hyperbolic ideal
tetrahedra to these S -operators as follows [19];
⟨a, b | S | c, d⟩= = (3.1)
⟨
a, b | S −1 | c, d
⟩
= = (3.2)
Namely in the momentum space representation we assign four momentum parameters {a, b, c, d}
to faces of tetrahedron. This di ﬀers from the (quantum) 6 j symbol as a solution of the pentagon
identity [33, 45], which was used to deﬁne the topological (quantum) gravity.
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 7
Figure 1. Triangle with vertices 0, 1, and z in C. Here we set z[1] = z, z[2] = 1− 1
z ,
and z[3] = 1
1−z.
Here both ideal tetrahedra have the modulus z = ed−b, and we mean that the dihedral angles
are given by
z[1] = z = ed−b
z[2] = 1 − 1
z
z[3] = 1
1 − z
The cross sections by the horosphere is similar to the triang le in C with vertices 0, 1, and z (see
Fig. 1), and we have z[1] z[2] z[3] = −1. See that the opposite edges of tetrahedra have the same
dihedral angles. Then the hyperbolic volume of the ideal tet rahedron ∆(z) with modulus z is
given by [50]
V ol(∆(z)) = D(z)
= L
( arg(z[1])) + L
( arg(z[2])) + L
( arg(z[3])) (3.3)
where L(θ) is the Lobachevsky function deﬁned by
L(θ) = 1
2
∞∑
n=1
sin(2 n θ)
n2 (3.4)
Any hyperbolic cusped 3-manifold M (for simplicity we assume that the manifold M has one
cusp in this paper) can be ideally triangulated, and it is con structed from ﬁnite number of the
oriented ideal tetrahedra in (3.1) and (3.2). Other types of oriented ideal tetrahedra, such as one
that has a face with loop, are prohibited. So our triangulation sometimes diﬀer from the canonical
triangulation used in computer programs, such as SnapPea [52], Knotscape [24], and Snap [11].
To construct 3-manifolds from these ideal tetrahedra, we glue each face to match orientations
of edges. Every faces have no loops, so there is no ambiguity i n gluing faces together once
two faces to be glued are ﬁxed. Furthermore, one ﬁnds that in- state |p⟩can glue only with
8 K. HIKAMI
Figure 2. Pentagon identity (2.14) is interpreted as the Pachner mo ve.
out-states ⟨p|, and that we cannot glue two in-states or out-states togethe r. As suggested by the
momentum representation of the pentagon identity, gluing t wo faces, which have same label p,
can be formulated by an integration with respect to p,
∫
R
dp |p⟩ ⟨p|.
By these identiﬁcations of the S -operators as the oriented ideal tetrahedra, the pentagon iden-
tity (2.14) is identiﬁed with the Pachner move as is depicted in Fig. 2; oriented polytope with 5
vertices can be decomposed into 2 tetrahedra with a face in co mmon, or into 3 tetrahedra with
an edge in common. In case of decomposing into 3 tetrahedra, we need a hyperbolic consistency
condition around the common edge. This condition coincides with a saddle point condition of
the right hand side of (2.14) after substituting (2.15) and t aking a classical limit γ → 0. One
can see a coincidence for any other type of gluings such as oth er choices of orientations in the
Pachner move between the hyperbolic consistency conditionand the saddle point equations [19].
Once triangulation is given and we know how to glue faces toge ther, we can naturally deﬁne
the quantum invariant for hyperbolic cusped 3-manifold M based on the S -operator by
Zγ(M) =
∫
R
dp δC(p) δG(p)
M∏
i=1
⟨
p(−)
2i−1, p(−)
2i | S εi | p(+)
2i−1, p(+)
2i
⟩
(3.5)
where p denotes a set of variables (p(±)
1 , p(±)
2 , . . . ,p(±)
2M), and εi = ±1 depending on an orientation
of tetrahedron. We set M as the number of ideal tetrahedra. The condition δG(p) determines
how to glue faces together (“G” stands for “gluing”). Every faces with same momentum mean to
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 9
be glued together, and the fact that in-states can be glued on ly with out-states indicates that the
gluing condition δG(p) is a product of δ
(
p(−)
j − p(+)
k
)
We need another geometrical condition δC(p) to deﬁne invariant besides a way how to glue
faces (“C” stands for “completeness”) [21]. We can draw a developing map from an ideal trian-
gulation of 3-manifold, and we need to read oﬀa hyperbolic complete condition. This condition
can be written as a constraint for p by identiﬁcations (3.1) and (3.2). By construction, the par ti-
tion function Zγ(M) is invariant under the Pachner move (Fig. 2), and it is essentially the invariant
constructed in Ref. 19.
As was studied by Thurston [51], deformation of the hyperbolic structure on the manifold
M can be holomorphically parametrized by a parameter u in a neighborhood of completeness
condition u = 0. The parameter u is the logarithm of the eigenvalue of the meridian by the
holonomy representation, and we set
m = eu (3.6)
Correspondingly we call such manifold Mu which is no more complete, and deﬁne the invariant
by
Zγ(Mu) =
∫
R
dp δC(p; u) δG(p)
M∏
i=1
⟨
p(−)
2i−1, p(−)
2i | S εi | p(+)
2i−1, p(+)
2i
⟩
(3.7)
Here the condition δC(p; u) follows from that the meridian has a holonomy (3.6). The inv ari-
ant (3.5) for M with complete hyperbolic structure follows from (3.7) by assuming a complete-
ness u = 0 of the hyperbolic structure of Mu;
Zγ(M) = Zγ (Mu=0) (3.8)
because
δC(p) = δC(p; u = 0) (3.9)
We now study a classical limit of our quantum invariantZγ(Mu). When we take a limit γ → 0
by use of (2.16), the quantum invariant deﬁned by (3.7) becomes
Zγ (Mu) ∼
∫
R
dp δC(p; u) δG(p)







M∏
i=1
δ
(
p(εi)
2i−1 − p(−εi)
2i−1 − p(−εi)
2i
) 






× exp







i
2 γ
M∑
i=1
εi V
(
p(εi)
2i − p(−εi)
2i , p(−εi)
2i−1
) 






=
∫
R
dx exp
( 1
2 iγ ΦM(x; u)
)
(3.10)
10 K. HIKAMI
Here in the last equality for our convention we have re-param etrized variables p with x =
(x1, x2, . . . ,xM−1) after incorporating constraints written in terms of delta functions.
The integral (3.10) could be evaluated by the saddle point method as we have taken a classical
limit γ → 0. The saddle point condition for variables x is
∂
∂xi
ΦM(x; u) = 0 (3.11)
As was extensively studied in Ref. 19, these conditions coin cide with hyperbolic consistency
conditions around edges when we glue oriented tetrahedra together. By construction the variable
u denotes the meridian of cusp in this classical limit, and the complete hyperbolic structure is
realized by setting u = 0. To conclude, the function ΦM(x; u) deﬁned by a classical limit (3.10)
of the quantum invariant Zγ(Mu) is nothing but the Neumann–Zagier potential function [44,55].
As a result, di ﬀerential of the potential function with respect to the defor mation parameter u
gives
∂
∂u ΦM(x; u) = 2 v (3.12)
where v is related to the eigenvalue of the longitude by the holonomy representation
ℓ = ev (3.13)
Variables xi can be solved from the hyperbolic consistency equation (3.1 1) as a function of u,
and we can regard the potential function ΦM(x; u) as a function of u; ΦM(u) = ΦM(x; u)|(3.11).
Then we can rewrite (3.12) by
d
du lim
γ→0
i γ log Zγ (Mu) = v (3.14)
We note that our variables ( u, v) diﬀers from those in Ref. 44; when we denote their variables
(uNZ, vNZ), we have
(u, v) =
( uNZ
2 , vNZ
2 + π i
)
(3.15)
Hereafter we also use the function VM(x; m) deﬁned by
VM(x1, x2, . . .; m) = ΦM(log x1, log x2, . . .; u = log m) (3.16)
As seen from (2.18) and (2.19), the potential function ΦM(x; u) under saddle point condi-
tions (3.11) becomes a sum of the Rogers dilogarithm functio ns. We recall here the Bloch in-
variant studied in Refs. 42, 43. The Bloch invariantβ(M) is deﬁned for ﬁnite volume hyperbolic
3-manifold M as
β(M) =
M∑
i=1
[zi] (3.17)
GENERALIZED VOLUME CONJECTURE & THE A-POLYNOMIALS 11
where [z] satisﬁes the Bloch group
[z] − [w] +
[ w
z
]
−
[ 1 − z−1
1 − w−1
]
+
[ 1 − z
1 − w
]
= 0 (3.18)
The Bloch regulator map ρ gives [43]
ρ (β(M)) = V ol(M) + i CS(M) (3.19)
where CS denotes the Chern–Simons invariant (see Ref. 37 for deﬁnition of the Chern–Simons
invariant for a case of cusped manifolds). As identities (2. 18)– (2.19) show that the S -operator
reduces to the Rogers dilogarithm function (or the Bloch–Wi gner function) in the saddle point,
and that they satisfy the pentagon identities (2.22) and (2. 23), we can interpret our invariant
Zγ(M) as a quantization of the Bloch invariant.
Generally we have many saddle points as algebraic solutions of a set of equations (3.11).
Among them, a solution which has the largest absolute value d ominates an asymptotics of the
quantum invariant Zγ(M). Combining this with a fact that our quantum invariant Zγ(M) may be
regarded as a quantization of the Bloch invariant, we should have
lim
γ→0
2 γ log
(
Zγ(M)
)
= V ol(M) + i CS(M) (3.20)
as a variant of the volume conjecture [19]. Although, there s till remains an ambiguity of branch
in complex plane in an actual computation.
The Neumann–Zagier potential function ΦM(x; u) has much information on geometry of man-
ifold. One of the properties is a relationship with the A-pol ynomial deﬁned in Ref. 9. When the
manifold M is a complement of knot S 3 \ K , the A-polynomial AK(ℓ, m) of K as an algebraic
equation of ℓ and m can be given by using the Gr¨ obner base or resultant theory to eliminate xi
from a set of equations, (3.11) and (3.12). So the pair (ℓ, m) = (ev, eu) deﬁned from (3.14) is a zero
locus of the A-polynomial AK(ℓ, m). This result should be comparable with a conjecture (1.2),
and the invariant Zγ(Mu) is a non-compact generalization of the Jones–Witten invariant.
The A-polynomial has following properties [9, 10];
• Polynomial AK(ℓ, m) is an integer polynomial, and it contains only even powers of m.
• Up to powers of ℓ and m, we have
AK(ℓ, m) = AK(1/ℓ, 1/m) (3.21)
• If K and K ′ are mirror images, then
AK(ℓ, m) = AK ′(1/ℓ, m) (3.22)
12 K. HIKAMI
• With additional property that every closed incompressiblesurface embedded in S 3 \ K is
parallel to the boundary torus, we have
AK(ℓ, ±1) = n (ℓ + 1)α+ (ℓ − 1)α− ℓβ (3.23)
with non-zero integer n.
• Slopes of edges of the Newton polygon of AK(ℓ, m) are boundary slopes of K.
• Coeﬃcients of terms in the corners of the Newton polygons of AK(ℓ, m) are ±1.
Another property of the Neumann–Zagier potential functionΦM(u) associated to cusped man-
ifold M is the volume of the Dehn surgered manifold. The (p, q)-hyperbolic Dehn surgery of M,
where (p, q) is a pair of coprime integers, is performed by gluing back a solid torus with cusp of
M, where the surgery data satisfy [50]
p u + q v = π i (3.24)
Then for the core c of solid torus, we have
Length(c) + i Torsion(c) = −2 (r u + s v) mod 2 π i (3.25)
where
(
p r
q s
)
∈ S L(2, Z). We have
Im (u ¯v) = −π
2 Length(c) (3.26)
According to Refs. 44, 55, we have for the hyperbolic (p, q)-Dehn surgered manifold M(p,q) as
(
V ol
(
M(p,q)
)
+ i CS
(
M(p,q)
))
− (V ol(M) + i CS(M))
= − i
4 (ΦM(u) − 4 u v) − π
2
( Length(c) + i Torsion(c)) (3.27)
which follows from
Zγ
(
M(p,q)
)
∼
∫
du e
1
2iγ
( p
q u2+ 2(π+γ)i
q u
)
Zγ(Mu) (3.28)
4. E xamples
