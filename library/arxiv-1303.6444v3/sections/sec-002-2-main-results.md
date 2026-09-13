---
doc_id: arxiv-1303.6444v3
doc_title: "VIRIAL EXPANSION BOUNDS"
section_id: sec-002-2-main-results
section_title: "Main Results"
section_number: 2
pages: 2-4
source_pdf: 1303.6444v3.pdf
source_sha256: 4f12ace2197f70ca
doc_brief: "VIRIAL EXPANSION BOUNDS — In the 1960s, the technique of using cluster expansion bounds in order to achieve bounds on the virial expansion was developed by Lebowitz and Penrose (1964) and Ruelle"
---
The main results of this paper rely on the particle model of the classical gas. The main
parameters in the model are: the inverse temperature β = 1
kT , where k is Boltzmann’s
constant and T is the temperature; the fugacity z; the pressure P ; and the density ρ.
We start with the Grand Canonical Partition function for a classical gas:
Ξ(z) =
∞∑
N=0
ZNzn (2.1)
Where ZN is the N-particle conﬁguration integral:
ZN = 1
N!
N∏
i=1
(∫
Rd
ddxi
)
e
−β ∑
1≤i<j≤N
Φ(xi,xj)
(2.2)
We have the relationship βP = ln Ξ, which gives us an expansion for pressure. The power
series for pressure in terms of fugacity z, may be written as:
βP =
∑
n≥1
bnzn (2.3)
Using the formula ρ =z ∂
∂z (βP ), we have the corresponding fugacity expansion for density:
ρ =
∑
n≥1
nbnzn (2.4)
We see that the power series expansion for ρ has a zero constant term and non zero z
term, where we have that b1⁄= 0 and usually we set it to 1. It is usual to have a non zero
z coeﬃcient in the cluster expansion. This means that it is possible to invert the ρ−z
relationship, in order to obtain an expansion for z(ρ). This can be substituted into (2.3) in
order to get a power series for P in terms of ρ:
P =
∑
n≥1
cnρn (2.5)
The assumptions for the initial cluster expansion bounds used in this article are:
Assumption 1 (Potential). The N-particle interaction potential: UN(x1,··· ,xN) may be
written as the sum of pair-potentials:
UN(x1,··· ,xN) =
∑
1≤i<j≤N
Φ(xi,xj) (2.6)
Furthermore, we assume that the pair potentials Φ(xi,xj) are central, that is, they only
depend on the distance from xi to xj.
Assumption 2 (Stability). The potential energy is assumed to be stable, that is, there is a
B >0, such that for every N and (x1,··· ,xN)∈ RNd, we have:
U(x1,··· ,xN) =
∑
1≤i<j≤N
Φ(xi,xj)≥−BN (2.7)
whered is the dimension of our system.
Deﬁnition 1 (C(β) and R(β) - ‘temperedness’). We have two main functions of β, which
play an important rˆ ole in the cluster expansion bounds:
C(β) :=
∫
Rd
⏐⏐⏐e−βΦ(0,x)− 1
⏐⏐⏐ ddx (2.8)
VIRIAL EXPANSION BOUNDS 3
R(β) :=

|B|rd +β
∫
|y|>r
|Φ(0,y )|ddy

 (2.9)
If the expression (2.8) is ﬁnite then the potential Φ is called ‘tempered’, which we assume
for bounds involving C(β)
The r in (2.9) represents the radius of the hard-core interaction. |B| is the surface area
of a d-dimensional sphere.
We writeRVir for the radius of convergence of the virial expansion.
Deﬁnition 2 (Lambert W-function). We denote by W (z), the Lambert W-function with
domain R+ :={x∈ R|x≥ 0} and range R+. It is the solution to:
W (z)eW(z) =z (2.10)
Further notes on the Lambert W-function can be found in [Cor97]
Theorem 2.1 (General Virial Bounds). Assuming cluster coeﬃcient bounds of the form:
|nbn|≤ ann−1
n! bn (2.11)
wherea and b are non-negative functions of inverse temperature β, we have the virial coef-
ﬁcient bounds:
|cn|≤ β−1
n

a−1
W
(
eab
1+ab
)
(
W
(
eab
1+ab
)
− 1
)2


n−1
(2.12)
which gives the lower bound on the radius of convergence as:
RVir≥a
(
W
(
eab
1+ab
)
− 1
)2
W
(
eab
1+ab
) (2.13)
If we apply this general theorem, which is derived in Section 4, to two speciﬁc bounds we
have for cluster expansions, we achieve:
Corollary 2.2 (Improved Lebowitz-Penrose). The cluster expansion bounds:
|nbn|≤ nn−1
n! e2βB(n−1)C(β)n−1 (2.14)
give the bound for virial coeﬃcients:
|cn|≤ β−1
n

C(β)e4βB
W
(
e
1+e2βB
)
(
W
(
e
1+e2βB
)
− 1
)2


n−1
(2.15)
and the bound for the radius of convergence:
RVir≥C(β)−1e−4βB
(
W
(
e
1+e2βB
)
− 1
)2
W
(
e
1+e2βB
) (2.16)
4 S. J. TATE
This is shown in Section 5
For purely hard-core interactions B = 0 and the radius of convergence satisﬁes:
RVir≥C(β)−1
(
W
(e
2
)
− 1
)2
W
(e
2
) (2.17)
This is precisely the same as what is obtained by Lebowitz-Penrose.
Corollary 2.3 (Alternative Bounds). For cluster expansion bounds:
|nbn|≤ nn−1
n! R(β)n−1enβB (2.18)
we have the bound for virial coeﬃcients as:
|cn|≤ β−1
n R(β)n−1


W
(
eβB+1
1+eβB
)
(
W
(
eβB+1
1+eβB
)
− 1
)2


n−1
(2.19)
Thus giving the radius of convergence as:
RVir≥R(β)−1
(
W
(
eβB+1
1+eβB
)
− 1
)2
W
(
eβB+1
1+eβB
) (2.20)
Remark 1. The bounds for the cluster coeﬃcients used in Corollary 2.2 are obtained in
[Rue69] and [Leb64]. The bounds for the cluster coeﬃcients used in Corollary 2.3 are ob-
tained in [Pog09].
Having a new separate bound is only a good idea, if it is an improvement in certain cases.
In Section 7 we understand how the two diﬀerent bounds compare and conclude:
Proposition 2.4 (Comparison of Bounds). The bound in Corollary 2.3 is better than that
in Corollary 2.2, precisely when
1.6R(β)<C (β) (2.21)
This is likely to happen at low temperatures (large β) and for potentials with a hard
core and attractive tail. The attractive element of the potential is important, since the
improvements are made corresponding to the stability parameter B.
