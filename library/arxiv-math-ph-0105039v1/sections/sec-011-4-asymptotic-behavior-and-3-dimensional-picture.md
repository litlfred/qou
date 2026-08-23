---
doc_id: arxiv-math-ph-0105039v1
doc_title: "Hyperbolic Structure Arising from a Knot Invariant"
section_id: sec-011-4-asymptotic-behavior-and-3-dimensional-picture
section_title: "Asymptotic Behavior and 3-dimensional Picture"
section_number: 4
pages: 11-14
source_pdf: 0105039v1.pdf
source_sha256: 850e6a00721e38d0
doc_brief: "Hyperbolic Structure Arising from a Knot Invariant — We study the knot invariant based on the quantum dilogarithm function."
---
We shall reveal the 3-dimensional picture of the knot invari ant τ1(K) by studying an asymptotic
behavior in a limit γ → 0. Using eq. (2.12), we ﬁnd that the S-operator (2.26) is represented by
⟨p1, p2 | S1, 2 | p′
1, p′
2⟩ ∼ δ(p1 + p2 − p′
1) · exp
(
− 1
2 i γ V (p′
2 − p2, p1)
)
, (4.1a)
⟨p1, p2 | S−1
1, 2 | p′
1, p′
2⟩ ∼ δ(p1 − p′
1 − p′
2) · exp
( 1
2 i γ V (p2 − p′
2, p′
1)
)
, (4.1b)
where we have deﬁned the function V (x, y) by
V (x, y) = π2
6 − Li2(ex) − x y. (4.2)
We see that the function V (x, y) is associated with each S-operator, and that the function V (x, y)
has an interesting property for our purpose to relate with th e 3-dimensional hyperbolic geometry;
when we suppose an analytic continuation x, y ∈ C, we have
V (x, y) = L(1 − ex) + 1
2
(
x ∂V (x, y)
∂x + y ∂V (x, y)
∂y
)
, (4.3a)
Im V (x, y) = D(1 − ex) + log |ex| · Im
( ∂
∂x V (x, y)
)
+ log |ey| · Im
( ∂
∂y V (x, y)
)
. (4.3b)
11
Here L(z) is the Rogers dilogarithm (2.2), and the function D(z) is the Bloch–Wigner func-
tion (2.9) which gives the hyperbolic volume of the ideal tet rahedron. This indicates that the
classical limit of the S-operator describes the ideal tetrahedron at the critical p oint. By these
observations we can associate the ideal tetrahedron for the S-operators ⟨p1, p2 | S±1 | p′
1, p′
2⟩ as
Fig. 3. Due to sign of the function V (x, y) in eqs. (4.1) these tetrahedra are mirror images each
other. Therein the modulus of the ideal tetrahedron is given by ep′
2−p2 and each face has a momen-
tum; we regard pi and p′
i as the outgoing and incoming states respectively,i.e., each triangular face
is assigned a transverse orientation. See that the dihedral angles of opposite edges are equal, and
we have
z1 z2 z3 = −1, 1 − z1 + z1 z2 = 0.
⟨p1, p2 | S | p′
1, p′
2⟩ :
PSfrag replacements
p1
p2
p′
1
p′
2
z1
z1
z2
z2
z3
z3
⟨p1, p2 | S−1 | p′
1, p′
2⟩ :
PSfrag replacements
p1
p2
p′
1
p
′
2
z1
z1
z2
z2
z3
z3
Figure 3: Both operators ⟨p1, p2 | S | p′
1, p′
2⟩ and ⟨p1, p2 | S−1 | p′
1, p′
2⟩ are represented by the
oriented tetrahedra, which become the ideal tetrahedra in t he classical limit γ → 0. In this limit
they have the modulus ep′
2−p2, and each edge is associated by z1 = e p′
2−p2, z2 = 1 − z −1
1 , and
z3 = (1 − z1)−1. These modulus denote the dihedral angle.
Our identiﬁcation of the modulus and dihedral angles can be j ustiﬁed from the 3-dimensional
picture of the pentagon identity as follows. The pentagon id entity (2.21) is depicted as the 2-3
Pachner move (Fig. 4) once we represent the S-operators by the oriented tetrahedra as in Fig. 3.
The matrix element of the right hand side of eq. (2.21) is written as
∫ ∫ ∫
dy dz dw ⟨p1, p2 | S | y, z⟩ ⟨y, p3 | S | p′
1, w⟩ ⟨z, w | S | p′
2, p′
3⟩. (4.4)
After substituting the asymptotic form (4.1) into this integral, we get immediately
y = p1 + p2, w = p′
2 − z,
12
and the integral reduces to
δ(p1 + p2 + p3 − p′
1) ·
∫
dz exp 1
2 i γ
(
−π2
2 + Li2(ez−p2) + Li2(ep′
2−p3−z) + Li2(ep′
3−p′
2+z)
+ z (−p2 + p′
3 − p′
2 + z) − p1 p2 + (p′
2 − p3) (p1 + p2)
)
.
As we study a limit γ → 0, the integral is evaluated by the saddle point method, whose saddle
point condition is given by
(1 − ew−p3)−1 · (1 − ep2−z) · (1 − ew−p′
3) = 1 . (4.5)
This condition exactly coincides with the hyperbolicity eq uation around an axis which penetrates
2 adjacent tetrahedra in the right hand side of Fig. 4, once we regard the S-operator as the ideal
tetrahedron whose dihedral angles are written in Fig. 3. See that by substituting a solution of
eq. (4.5) into eq. (4.4) we recover the left hand side of eq. (2 .21) after using Schaeffer’s pentagon
identity (2.7).
Figure 4: Pachner move 2 ↔ 3.
This coincidence between the saddle point equation and the h yperbolicity consistency con-
dition can be seen for other pentagon identities, such as S2, 3 S1, 2 S −1
2, 3 = S1, 2 S1, 3, S −1
1, 2 S2, 3 =
S1, 3 S2, 3 S −1
1, 2 , and the trivial identities S1, 2 S −1
1, 2 = 1 . This fact supports a validity that at the crit-
ical point the classical limit of the S-operator represents the (oriented) ideal tetrahedron who se
dihedral angles are ﬁxed as in Fig. 3.
13
5 3-Dimensional Picture of the Invariant
