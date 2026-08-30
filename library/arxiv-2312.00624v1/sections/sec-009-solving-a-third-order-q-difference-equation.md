---
doc_id: arxiv-2312.00624v1
doc_title: "On the structure of wave functions in complex Chern–Simons theory"
section_id: sec-009-solving-a-third-order-q-difference-equation
section_title: "Solving a third-order q-difference equation"
section_number: null
pages: 20-23
source_pdf: 2312.00624v1.pdf
source_sha256: bda867f7b84f69c3
doc_brief: "On the structure of wave functions in complex Chern–Simons theory — We study the structure of wave functions in complex Chern–Simons theory on the complement of a hyperbolic knot, emphasizing the"
---
We will show how the matrix formalism of Section 3.4.1 can be applied to solve a third-order q-
difference equation in closed form. In particular, let us return to the quantumA-polynomial equation
satisfied by the resummed perturbative wave function χ(α),WKB(u; ℏ) in Eq. (3.51) and assume it is
of order three. As before, after appropriately accounting for the correction due to the exponential
prefactor containing the functions s(α)
0,1 (x) in Eq. (3.49), the q-difference equation takes the form
Ψ(α),WKB(qX;q) +A(X)Ψ(α),WKB(X;q) +B(X)Ψ(α),WKB(q−1X;q) +C(X)Ψ(α),WKB(q−2X;q) = 0,
(3.74)
where A(X),B (X),C (X) are functions of X and q. We can now introduce the function υ(α)(X) as
in Eq. (3.53) and write Eq. (3.74) equivalently as
υ(X)υ(q−1X)υ(q−2X) +A(X)υ(q−1X)υ(q−2X) +B(X)υ(q−2X) +C(X) = 0, (3.75)
where we have dropped the label α from the notation for simplicity. Let us further assume that q is
fixed as in Eq. (3.55) and define the the sequence of functions {υk(X)}, k∈ Z≥0, of X and q by
υk =υ(q−kX). (3.76)
It follows from shifting X intoq−kX in Eq. (3.75) that they satisfy the system of equations
υkυk+1υk+2 +A(q−kX)υk+1υk+2 +B(q−kX)υk+2 +C(q−kX) = 0, 0≤k≤Q− 1. (3.77)
In order to solve the above system recursively, let us define the sequences {a(k)(X)},{b(k)(X)}, and
{c(k)(X)}, k∈ Z≥0, via the relations
a(1)(X) =A(X), (3.78a)
b(1)(X) =B(X), (3.78b)
c(1)(X) =C(X), (3.78c)
υ0υ1··· υk+1 +a(k)(X)υkυk+1 +b(k)(X)υk+1 +c(k)(X) = 0, k> 1. (3.78d)
– 19 –
If we multiply Eq. (3.78d) by υk+2 and apply Eq. (3.77), we obtain a recursion relation which can
be written in matrix form as


a(k+1)(X)
b(k+1)(X)
c(k+1)(X)

 =


−A(q−kX) 1 0
−B(q−kX) 0 1
−C(q−kX) 0 0




a(k)(X)
b(k)(X)
c(k)(X)

 , (3.79)
and it can be solved as 

a(Q)(X)
b(Q)(X)
c(Q)(X)

 =MQ(X)


−1
0
0

 . (3.80)
Here,MQ(X) is the matrix
MQ(X) =
QY
k=1


−A(qkX) 1 0
−B(qkX) 0 1
−C(qkX) 0 0

 =


M11(X)M12(X)M13(X)
M21(X)M22(X)M23(X)
M31(X)M32(X)M33(X)

 , (3.81)
where the product is ordered from left to right as k increases. As before, let us introduce
Πυ =υ0υ1··· υQ−1, (3.82)
which is invariant under q-shifts. Moreover, as it will be useful in the following, we compute the
q-shifted matrix
MQ(q−1X) =


−A(X) 1 0
−B(X) 0 1
−C(X) 0 0

MQ(X)


−A(X) 1 0
−B(X) 0 1
−C(X) 0 0


−1
, (3.83)
and we obtain in this way


−AM12 +M22−AM13 +M23 A
C (M11 +AM12 +BM13)− 1
C (M21 +AM22 +BM23)
−BM12 +M32−BM13 +M33 B
C (M11 +AM12 +BM13)− 1
C (M21 +AM22 +BM23)
−CM12 −CM13 (M11 +AM12 +BM13)

 ,
(3.84)
where we have removed the explicit dependence on X for compactness. Let us now take Eq. (3.78d)
for k =Q, which gives
υ0υ1(Πυ +a(Q)(X)) +b(Q)(X)υ1 +c(Q)(X) = 0. (3.85)
Eq. (3.80) allows us to express the functions a(Q)(X), b(Q)(X), and c(Q)(X) in terms of the entries
of the matrixMQ(X), so that Eq. (3.85) becomes
υ0υ1(Πυ−M 11(X))−M 21(X)υ1−M 31(X) = 0. (3.86)
Shifting X into q−1X, using Eq. (3.77) with k = 0, and applying the dictionary encoded in the
matrix in Eq. (3.84), we find the second equation
υ1(Πυ−M 22(X))−M 32(X)−M 12(X)υ0υ1 = 0. (3.87)
Subsequently shiftingX intoq−1X in the equation above, again using Eqs. (3.77), (3.84), we obtain
the third equation
Πυ−M 33(X)−M 23(X)υ1−M 13(X)υ0υ1 = 0. (3.88)
– 20 –
Eqs. (3.86), (3.87), (3.88) assemble into a cubic system which can be written in matrix form as


M11(X)− Πυ M21(X) M31(X)
M12(X) M22(X)− Πυ M32(X)
M13(X) M23(X) M33(X)− Πυ




υ0υ1
υ1
1

 =


0
0
0

 . (3.89)
We conclude that Πυ is an eigenvalue of the transpose matrixMQ(X)T with eigenvector (υ0υ1,υ 1, 1)T.
The characteristic polynomial is
p(z) = det(zI3−M T
Q) =z3 +d2z2 +d1z +d0, (3.90)
where I3 is the 3x3 identity matrix and
d2 =−M 11−M 22−M 33, (3.91a)
d1 =−M 23M32−M 12M21−M 13M31 +M11M22 +M11M33 +M22M33, (3.91b)
d0 =−M 11M22M33 +M11M23M32 +M22M31M13 +M33M21M12 (3.91c)
−M 21M13M32−M 31M12M23.
The eigenvalues of the matrixMQ(X)T are the roots of p(z), that is,
Πυ =−1
3

d2 + Θ2 + Θ0
Θ2

, (3.92)
where we have
Θ0 =d2
2− 3d1, (3.93a)
Θ1 = 2d3
2− 9d2d1 + 27d0, (3.93b)
Θ2 = emπi
3
2
3
r
Θ1 +
q
Θ4
1− 4Θ3
0, m = 0, 1, 2. (3.93c)
The function υ0 is obtained, for example, by solving the system of Eqs. (3.87), (3.88), yielding
υ0 =M22M33−M 22Πυ−M 23M32−M 33Πυ + (Πυ)2
−M12M33 +M12Πυ +M13M32
, (3.94)
while the functions υk, k∈ Z>0, are computed by successively q-shifting υ0. This gives the solution
to Eq. (3.75) for all rational values of ℏ. As we have done in Section 3.4.1, we can now fix the
ambiguity in Eq. (3.92) and correspondingly in Eq. (3.94), that is, the value of m = 0, 1, 2 in the
definition of Θ2, by imposing the consistency of the solution with the original choice of a non-abelian
classical branch labeled by α. Specifically, we require that Eq. (3.71) holds in the case of P =Q = 1
after accounting for the exponential prefactor in Eq. (3.49). Again, we conclude by observing that
Eqs. (3.53), (3.73) yield
Υ(X) = logυ0, φ Q(X) = 1
Q log Πυ. (3.95)
Note that the procedure described here for a third-order q-difference equation can be generalized to
higher orders.
– 21 –
