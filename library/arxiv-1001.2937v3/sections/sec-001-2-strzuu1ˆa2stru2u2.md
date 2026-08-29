---
doc_id: arxiv-1001.2937v3
doc_title: "Microscopic Spectrum of the Wilson Dirac Operator"
section_id: sec-001-2-strzuu1ˆa2stru2u2
section_title: "Str(Z[U+U−1])+ˆa2Str(U2+U−2)"
section_number: 2
pages: 2-3
source_pdf: 1001.2937v3.pdf
source_sha256: ab44349bc21634ff
doc_brief: "Microscopic Spectrum of the Wilson Dirac Operator — 4 sections: Str(M[U−U−1])+i 1; Str(Z[U+U−1])+ˆa2Str(U2+U−2); Str(M[U+U−1])+ 1"
---
where M ≡diag( ˆm1 . . . ˆmk+l) and Z ≡diag(ˆz1 . . . ˆzk+l).
This graded partition function diﬀers in a subtle way
from the one introduced in [12]. As discussed in [6], the
0
2
4
6
8
10
x
0
0.5
1
1.5
ρ5
ν(x)
FIG. 1:
The microscopic spectrum of D5 for ˆm = 3, ν = 0
and ˆa = 0, 0.03, and 0.250. The ν = 0 spectrum is reﬂection
symmetric about ˆx = 0.
integration manifold for non-perturbative computations
is non-compact for the bosonic sector. While the action
(5) and the action introduced in [12] break the ﬂavor
symmetries in exactly the same way, only the former one
is consistent with the convergence requirements of the
graded integral for W8 > 0. For perturbative calcula-
tions the convergence requirements are immaterial. Here
and below we focus mainly on the quenched case, corre-
sponding to integration manifold Gl(1|1)/U(1). The gen-
eralization to an arbitrary number of ﬂavors is straight-
forward, and we expect that the underlying integrability
structure will lead to a full analytical solution just as in
the a = 0 case [17].
The Microscopic Spectrum of D5. For a = 0, the micro-
scopic spectral density of D5 follows from the expression
for the microscopic spectral density of D through
ρν
5(ˆx > ˆm, ˆm; ˆa = 0) =
ˆx
√
ˆx2 −ˆm2 ρν(
p
ˆx2 −ˆm2) . (6)
To obtain the spectral density of D5 for a̸ = 0, we eval-
uate the resolvent
Gν(ˆz, ˆm; ˆa) ≡
lim
ˆz′→ˆz
d
dˆz Zν
1|1( ˆm, ˆm, ˆz, ˆz′; ˆa)
(7)
and ﬁnd
Gν(ˆz, ˆm; ˆa) =
Z ∞
−∞
ds
Z π
−π
dθ
2π
i
2 cos(θ)eSf +Sbe(iθ−s)ν
× (−ˆm sin(θ) + i ˆm sinh(s) + iˆz cos(θ) + iˆz cosh(s) (8)
+4ˆa2[cos(2θ) + cosh(2s) + (eiθ+s + e−iθ−s)] + 1

.
Here Sf = −ˆm sin(θ) + iˆz cos(θ) + 2ˆa2 cos(2θ) and Sb =
−i ˆm sinh(s)−iˆz cosh(s)−2ˆa2 cosh(2s). As is well known,
the resolvent is deﬁned only up to ultraviolet subtrac-
tions in the underlying theory. The microscopic quenched
spectral density,
ρν
5(ˆx, ˆm; ˆa) = 1
π Im[Gν(ˆx, ˆm; ˆa))],
(9)
3
-16
-12
-8
-4
0
4
8
12
16
x
0
0.5
1
1.5
ρ5(x)
a=0.125, m=3, ν=2
a=0.250, m=3, ν=2
a=0.500, m=3, ν=2
FIG. 2:
The microscopic spectrum of D5 for ˆm = 3, ν = 2
and ˆa = 0.125, ˆa = 0.250 and ˆa = 0.500 respectively.
is, however, uncontaminated by these ultraviolet pieces.
Plots of ρν
5 are shown in Fig. 1 for ν = 0, and in Fig. 2 for
ν = 2. The eigenvalues that converge towards the end-
points of the spectrum at sign(ν)m in the a →0 limit are
clearly visible. The sum over ν of the spectral density,
for which the continuum limit has been established rig-
orously [18], can be evaluated in a straightforward way.
Random Matrix Theory. An eﬃcient alternative way to
extend the above results to all spectral correlation func-
tions and individual eigenvalue distributions is to con-
struct a chiral Random Matrix Theory that is equiva-
lent to the chiral Lagrangian in the same scaling regime.
This the case if the chiral Random Matrix Theory has
the same global symmetries and transformation proper-
ties as the QCD partition function with the Wilson Dirac
operator. The chiral Random Matrix Theory is
˜Zν
Nf =
Z
d ˜Ad ˜Bd ˜W detNf ( ˜DW + ˜m + ˜z˜γ5) P( ˜DW ),(10)
where ˜DW is of the same block form as (1) and the inte-
gration is over the real and imaginary parts of the matrix
elements of the Hermitian n×n matrix, ˜A, the Hermitian
(n + ν) × (n + ν) matrix ˜B and the complex n × (n + ν)
matrix ˜W. This ˜DW has |ν| real eigenvalues. We have
added tildes to stress that this is a zero-dimensional ma-
trix integral with parameters ˜m and ˜z instead of m and
z. In the universal scaling limit there is a one-to-one cor-
respondence between the two pairs, just as in the a = 0
case. The precise form of the distribution of the matrix
elements P( ˜DW ) is not important on account of univer-
sality. The partition function (3) (with W6 = W7 = 0) is
recovered in the microscopic scaling limit. For a Gaus-
sian distribution, this can be shown by a simple explicit
calculation. It also follows that W8 > 0. This is a con-
sequence of the γ5-Hermiticity: Changing the sign of W8
is equivalent to a →ia, violating γ5-Hermiticity of ˜DW .
This suggests that the Hermiticity properties of the Dirac
operator can restrict the coeﬃcients of the eﬀective La-
grangian. In fact, with W8 < 0 the integrals in (5) are
divergent. However, the graded partition function
¯Zν
1|1(M, Z; ˆa) =
Z
dU Sdet(U)ν
(11)
×e
1
