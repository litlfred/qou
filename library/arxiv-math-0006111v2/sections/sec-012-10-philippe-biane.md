---
doc_id: arxiv-math-0006111v2
doc_title: "Approximate factorization and concentration for characters of symmetric groups"
section_id: sec-012-10-philippe-biane
section_title: "PHILIPPE BIANE"
section_number: 10
pages: 10-10
source_pdf: 0006111v2.pdf
source_sha256: cd99f45d686eb6e2
doc_brief: "Approximate factorization and concentration for characters of symmetric groups — We prove a factorization-concentration result for characters of s ymmet- ric groups."
---
is
R(z) =
∞∑
n=1
zncn−1 = z
1 −cz
thus
K(z) = 1
z +R(z) = 1
z + z
1 −cz
Inverting the function K gives the Cauchy transform
G(z) = z +c −
√
(z −c)2 − 4
2(1 +cz) = 2
z +c +
√
(z −c)2 − 4
where the branch of the square root on C \ [0, +∞[ is chosen to have positive
imaginary part. We now compute the Rayleigh measure τ according to the formula
∂
∂z logG(z) = −
∫
R
τ(du)
z −u
One has
− ∂
∂z logG(z) =
1 + z−c√
(z−c)2−4
z +c +
√
(z −c)2 − 4
= 1
2
√
(z −c)2 − 4
(
2 +cz −c2 +c
√
(z −c)2 − 4
1 +cz
)
Let
k(c,u ) = 2 +cu −c2
2π (1 +cu)
√
4 − (u −c)2 for −2 +c<u< 2 +c.
Using Stieltjes inversion formula we get
(3.1.2) τc(du) =





k(c,u )1[c−2,c +2](u)du if 0 ≤c< 1
1
2δ−1(du) + du
2π
√
(x+1)(3−x)
1]−1, 3[(u) if c = 1
δ− 1
c
(du) +k(c,u )1[c−2,c +2]du if c> 1
From the Rayleigh measure τc we can recover the diagram by the formula
Pc(u) =
∫ +∞
−∞
|u −x|τc(dx)
A lenghty but straightforward computation using (3.1.2) gi ves formula (3.1.1). □
