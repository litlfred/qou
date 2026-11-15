---
doc_id: arxiv-hep-th-9212088v1
doc_title: "arXiv:hep-th/9212088v1 14 Dec 1992"
section_id: sec-003-3-calculation-of-the-partition-function
section_title: "Calculation of the partition function"
section_number: 3
pages: 6-9
source_pdf: 9212088v1.pdf
source_sha256: ecb2c02ec6fe11bd
toc_source: inferred
doc_brief: "arXiv:hep-th/9212088v1 14 Dec 1992 — We construct a random matrix model that, in the large N limit, reduces to the low energy limit of the QCD partition function put forward by Leutwyler and Smilga."
---
In order to evaluate the partition function (2.2) the determinant is written as an
integral over Grassmann variables
Y
f
det
 
mf
iT
iT †
mf
!
=
Z Y
f
DψfDφf exp
X
f
 
ψf∗
φf∗
! 
mf
iT
iT †
mf
! 
ψf
φf
!
,
(3.1)
where the measure of the Grassmann integration is as usual
Dψf =
Y
i
dψf
i dψf∗
i ,
(3.2)
and the conjugation ∗is the conjugation of the second kind (i.e., ψ∗∗= −ψ) [9]. The
integral over T is gaussian and can be performed easily. In the partition function this
results in the factor
exp 2λ2
N ψf∗
i ψg
i φg∗
j φf
j ,
(3.3)
which represents a 4-fermion interaction.
The quartic term can be written as a sum of two squares
ψf∗
i ψg
i φg∗
j φf
j = 1
4(ψf∗
i ψg
i + φf∗
i φg
i )(ψg∗
j ψf
j + φg∗
j φf
j ) −1
4(ψf∗
i ψg
i −φf∗
i φg
i )(ψg∗
j ψf
j −φg∗
j φf
j ).
(3.4)
Each of the two squares can be linearized with the help of a Hubbard-Stratonovich trans-
formation [9]. This allows us to perform the Grassmann integrations at the expense of
the introduction of the new real valued integration variables σfg and ¯σfg, respectively.
Apart from an irrelevant overall constant, the partition function reduces to
Z =
X
N
µ(N)
X
N+
 
N
N+
!
eiθ(N+−N−)
Z
DσD¯σ
detN+(σ + i¯σ + m)detN−(σ −i¯σ + m)
×
exp −N
2λ2Tr(σ + i¯σ)(σ −i¯σ).
(3.5)
As always, the measure of the integral over the matrices σ and ¯σ is the Haar measure.
The diagonal mass matrix is denoted by m.
The complex matrix σ + i¯σ can be decomposed in ’polar coordinates’ as [19]
σ + i¯σ = UΛV −1,
(3.6)
where U and V are unitary matrices and Λ is a diagonal real positive deﬁnite matrix. Since
the r.h.s has Nf more degrees of freedom than the l.h.s., one has to impose constraints
on the new integration variables. This can be achieved [19] by restricting U to the coset
U(Nf)/U(1)Nf, where U(1)Nf is the diagonal subgroup of U(Nf). In terms of the new
variables the partition function reads
Z
=
X
N
µ(N)
X
N+
 
N
N+
! Z
J(Λ)DΛDUDV
×
detN+(UΛV −1 + meiθ/Nf )detN−(V ΛU−1 + me−iθ/Nf ) exp(−N
2λ2TrΛ2), (3.7)
where the integral over U is over U(Nf)/U(1)Nf and the integral over V is over U(Nf).
A phase factor exp(−iθNf) has been absorbed in the integration over V .
For Nf ﬂavors we have Nf condensates which break down the symmetry of the action
to U(Nf)/U(1)Nf leaving us with N2
f −1 Goldstone modes for N+̸ = N−. When the total
topological charge is zero the phase of the determinant also cancels which provides us
with an additional zero mode.
The term proportional to m plays the role of a small symmetry breaking term. The
integrals over the nonzero modes will be performed by a saddle point integration at
m = 0, whereas the integrals over the soft modes will be accounted for exactly at a ﬁxed
value of mN. There are two types of nonzero modes, the phase exp iα of the determinant
det V U−1 for N+̸ = N−, and the eigenvalues Λ. The partition function at m = 0 factorizes
accordingly,
Z(m = 0) =
X
N
µ(N)
Z
dα(exp(iα) + exp(−iα))N
Z
J(Λ)dΛdetNΛ exp(−N
2λ2TrΛ2).
(3.8)
The leading order contribution in 1/N of the integral over Λ can be obtained by a saddle
point approximation. The saddle point equations for the Λ integrals read
Λi = ±λ.
(3.9)
The negative solution is not inside the integration manifold and can be omitted.
The integral over α, which ranges from 0 until 2π , can be executed either before or
after the summation over N+. In the ﬁrst case we ﬁnd zero for odd values of N while for
even values of N only the term N+ = N−= N/2 contributes in which case the α integral
becomes soft. However, in the second case the interference between contributions of all
diﬀerent topologies results in the integrand (2 cos α)N which allows us to perform the
integral by a saddle point approximation in order to obtain the leading order contribution
in 1/N. The saddle points are located at α = 0 and α = π. It is at this point that the
distribution function µ(N) plays a role: the contribution of the latter saddle point, (−1)N,
can be ignored after the summation over N, whereas the contribution at α = 0 yields
a overall factor µ(N) that does not contribute to the m dependent part of the partition
function to be discussed below.
At the saddle points in Λ and α, the U−dependence can be absorbed into V . The the
U−integration yields a ﬁnite irrelevant constant. Since the phase exp iα has already been
extracted the remaining integral over V is over SU(Nf) instead of U(Nf). We treat m
as a small parameter and expand the determinants up to ﬁrst order in m. At the saddle
point α = 0 the result for m dependent part of the partition function is
Z(m, θ)
Z(m = 0, θ) =
Z
det V =1 DV exp( N
2λTr(mV −1 exp(−iθ/Nf) + mV exp(iθ/Nf)),
(3.10)
which coincides with the result derived by Smilga and Leutwyler [2] for the QCD partition
function using chiral perturbation theory.
The value of Σ at θ = 0 can be obtained from eq. (2.4)
Σ(θ = 0) = lim
m→0 lim
N→∞
1
2λ
1
Nf
< Tr(V + V −1) >Z(θ=0) .
(3.11)
For Nf = 1 the integral over V is absent, and the sign of the quark condensate is inde-
pendent of the sign of m. For more than one ﬂavor the order of the limits allows us to
perform the V integral by a saddle point approximation. In the case of equal positive
masses the saddle point for θ = 0 is at V = 1 which allows us to identify the parameter
λ as
λ =
1
Σ(θ = 0),
(3.12)
which completes the calculation of the partition function.
As observed in [2], for more than one ﬂavor the value of the condensate depends on
the sign of the quark mass. For example, in the case of two ﬂavors with equal negative
masses and θ = 0, the saddle point is at V = −1.
It is also possible to introduce a complex mass in eq. (2.2) with the mass in the lower
block equal to the complex conjugate of the mass in the upper block of the overlap matrix.
In this case the ﬁnal result for the partition function depends only on the combination
meiθ and its complex conjugate which makes it possible [2] to derive relations between
the m and the θ derivatives of the partition function.
