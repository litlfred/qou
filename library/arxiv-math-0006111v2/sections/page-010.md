---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: page-010
section_title: "Page 10"
section_number: null
pages: 10-10
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
toc_source: undetermined
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of symmet- ric groups."
---
10
PHILIPPE BIANE
is
R(z) =
∞
X
n=1
zncn−1 =
z
1 −cz
thus
K(z) = 1
z + R(z) = 1
z +
z
1 −cz
Inverting the function K gives the Cauchy transform
G(z) = z + c −
p
(z −c)2 −4
2(1 + cz)
=
2
z + c +
p
(z −c)2 −4
where the branch of the square root on C \ [0, +∞[ is chosen to have positive
imaginary part. We now compute the Rayleigh measure τ according to the formula
∂
∂z log G(z) = −
Z
R
τ(du)
z −u
One has
−∂
∂z log G(z) =
1 +
z−c
√
(z−c)2−4
z + c +
p
(z −c)2 −4
=
1
2
p
(z −c)2 −4
 
2 + cz −c2 + c
p
(z −c)2 −4
1 + cz
!
Let
k(c, u) =
2 + cu −c2
2π(1 + cu)
p
4 −(u −c)2
for −2 + c < u < 2 + c.
Using Stieltjes inversion formula we get
(3.1.2)
τc(du) =





k(c, u)1[c−2,c+2](u) du
if 0 ≤c < 1
1
2δ−1(du) +
du
2π√
(x+1)(3−x)1]−1,3[(u)
if c = 1
δ−1
c (du) + k(c, u)1[c−2,c+2] du
if c > 1
From the Rayleigh measure τc we can recover the diagram by the formula
Pc(u) =
Z +∞
−∞
|u −x| τc(dx)
A lenghty but straightforward computation using (3.1.2) gives formula (3.1.1).
□
3.2 Generalization to other tensor states. Let H = H0⊕H1, be a Z/2-graded
Hilbert space with grading operator ∆. Endow B(H⊗q) = B(H)⊗q with a tensor
state τ ⊗q where τ is a state on B(H), of the form τ(X) = Tr(TX), with T a positive
trace class operator, with trace 1, commuting with the grading. Denote by t1,0 ≥
t2,0 ≥. . . ≥tk,0 ≥. . . ≥0 and t1,1 ≥t2,1 ≥. . . ≥tk,1 ≥. . . ≥0 the eigenvalues of
T on H0 and H1 respectively, and let pn = Tr(∆(∆T)n) = P∞
j=1 tn
j,0 −(−tj,1)n for
n ≥1
