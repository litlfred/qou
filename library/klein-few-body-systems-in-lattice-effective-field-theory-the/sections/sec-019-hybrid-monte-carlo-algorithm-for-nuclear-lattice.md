---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-019-hybrid-monte-carlo-algorithm-for-nuclear-lattice
section_title: "Hybrid Monte Carlo algorithm for Nuclear Lattice Effective Field Theory"
section_number: null
pages: 39-42
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
3.7 Hybrid Monte Carlo algorithm for Nuclear Lattice Effective Field
Theory
While there are a lot of diﬀerent algorithms to calculate Eq. (3.41), we choose the Hybrid Monte Carlo
(HMC) algorithm in this thesis [102]. In this algorithm we update the whole ﬁeld and auxiliary ﬁeld
conﬁguration at the same time making it very e ﬃcient and exact. In the following we give a detailed
description of the method. Starting point is the path integral with auxiliary ﬁelds according to Eq. (3.49),
where the path integral over the Grassmann ﬁelds is substituted by the transfer matrix formulation,
Z(t) =
∫
DπI Ds DsS DsI DsS I exp[−Sππ− S ss
]⟨Ψ| MLt (πI, s, sS, sI, sS I
)|Ψ⟩. (3.56)
Here,|Ψ⟩ is the trial wave function and M(nt)(πI, s, sI) is the transfer matrix including all auxiliary
ﬁeld-nucleon interactions,
M(nt) (πI, s, sS, sI, sS I
) =: exp
−Hfreeαt− gAαt
2Fπ
∑
S,I
∆SπI
(⃗ns, nt
)ρS,I
(⃗ns
)
+√−c00αt
∑
⃗n
s(⃗n,⃗n)ρ(⃗n) +√−cssαt
∑
S
∑
⃗n
sS
(⃗n, nt
)ρS
(⃗n)
+√−ciiαt
∑
I
∑
⃗n
sI
(⃗n, nt
)ρI
(⃗n) +√−csiαt
∑
S,I
∑
⃗n
sS I
(⃗n, nt
)ρS I
(⃗n)
 : .
(3.57)
The free Hamiltonian is used in the discretized version of the upper line of Eq. (3.44), while the density
operators are deﬁned in App. B. The auxiliary ﬁelds s, sS, sI and sS I correspond to the respective contact
interaction. The pion and auxiliary ﬁeld actions read
Sππ =αt

m2
π
2 + 3

∑
I
∑
⃗n
πI
(⃗n)πI
(⃗n)−αt
∑
I
∑
⃗n,ˆl
πI
(⃗n)πI
(
⃗n + ˆl
)
, (3.58)
S ss =1
2
∑
⃗n,⃗n′,nt
s(⃗n, nt
) f−1 (
⃗n−⃗n′)
s
(
⃗n′)
+ 1
2
∑
⃗n,⃗n′,nt,S
sS
(⃗n, nt
) f−1 (
⃗n−⃗n′)
sS
(
⃗n′)
+ 1
2
∑
⃗n,⃗n′,nt,I
sI
(⃗n, nt
) f−1 (
⃗n−⃗n′)
sI
(
⃗n′)
+ 1
2
∑
⃗n,⃗n′,nt,S,I
sS I
(⃗n, nt
) f−1 (
⃗n−⃗n′)
sS I
(
⃗n′)
,
(3.59)
with f−1(⃗n−⃗n′) is the inverse smearing function,
f−1 (
⃗n−⃗n′)
= 1
L3
∑
⃗q
1
f (⃗q) exp
[
−i⃗q
(
⃗n−⃗n′)]
. (3.60)
A natural choice for the trial wave function is an antiymmetric combination of plane single-nucleon
wave functions,|Ψfree⟩. As a time evolution of such a state through the complete LO transfer matrix is
too expensive, we split the calculation into two parts. Firstly, we evolve this conﬁguration through an
SU(4) symmetric Hamiltonian Lto times. Such a simpliﬁed Hamiltonian does not suﬀer from the sign
problem and it is already a good approximation to the full Hamiltonian [33, 103, 104]. Then the trial
33
Chapter 3 Nuclear Lattice E ﬀective Field Theory
wave function reads
|Ψ⟩ =
Lto∏
nt=1
: exp
−Hfreeαt− 1
2
∑
⃗n,⃗n′,nt
sSU(4)
(⃗n, nt
) f−1
SU(4)
(
⃗n−⃗n′)
sSU(4)
(
⃗n′, nt
)
+
√
−CSU(4)αt
∑
⃗n
sSU(4)
(⃗n, nt
)ρ(⃗n)
 :
⏐⏐⏐⏐Ψfree⟩
.
(3.61)
Once the trial wave function is constructed, we can use the full Hamiltonian to calculate the amplitude,
ZLO (t) =⟨Ψ| M
Lti
LO|Ψ⟩, (3.62)
with t = 2Lto + Lti and where we have suppressed all auxiliary ﬁeld notations in the expression. Now the
ground state energy is given as
ELO
(
t− αt
2
)
=− 1
αt
log ZLO (t)
ZLO
(t−αt
). (3.63)
Over and above the LO transient energy, we will measure higher-order operators ˆO perturbatively. We
insert them in the center of our amplitude calculation,
Z ˆO (t) =⟨Ψ|(MLO
)Lti/2 M ˆO
(MLO
)Lti/2|Ψ⟩, (3.64)
with an energy contribution
E ˆO = 1
αt
(
1− Z ˆO
ZLO
+...
)
. (3.65)
The time evolution for the di ﬀerent time steps is shown schematically in Fig. 3.4. Note that for the
evaluation of the transient energy and perturbative insertions, one normaly evaluates the amplitude
between neighboring time slices. Additionally, one could also take next-to-neighboring time slices and so
on to get energies for times between to and ti. However, it has been shown earlier that the data becomes
poorly decorrelated quickly. In the following calculations, we will take neighboring and – if possible –
partially next-to-neighboring time slices only. The operator M ˆO is constructed from an extended auxiliary
ﬁeld transfer matrix M(πI, s, sS, sI, sS I,ϵ ) which includes all necessary operator structures in the form of
external currents. In the following we give an explicit example for a simple two-body contact interaction
without any spin, isospin or momentum dependence while all other interaction operators are calculated
analogous after including the respective current structure in the transfer matrix. Hence, the transfer
matrix is deﬁned as
M
(
πI, s, sS, sI, sS I,ϵρ
)
= M (πI, s, sS, sI, sS I
) exp

∑
⃗n
ϵρ
(⃗n, nt
)ρ(⃗n)
. (3.66)
Then the perturbative insertion reads
∆Mρ∝−αt
∑
⃗n
δ
δϵρ
(⃗n, nt
) δ
δϵρ
(⃗n, nt
) M(πI, s, sS, sI, sS I,ϵρ). (3.67)
Now the amplitude is deﬁned in terms of the auxiliary ﬁelds and we can use the HMC method to
34
3.7 Hybrid Monte Carlo algorithm for Nuclear Lattice E ﬀective Field Theory
OΨ free Ψ free
02Lto+ Lti
SU(4) π
Lto+ Lti/2 LtoLto+ Lti
full LO full LO SU(4) π
operator insertion for
expectation value
Z,N Z,N
Figure 3.4: Schematic time steps for time evolution. Figure taken from [33].
determine the ground state energy. The procedure is as follows:
1. Initialization
Firstly, we create a random conﬁguration of auxiliary ﬁelds sX, where sX is an abbreviation for all
auxiliary ﬁelds of the theory used in Eqs. (3.56), (3.57), and (3.61).
2. Molecular dynamics
Corresponding to the initial conﬁguration we create the conjugate momenta randomly according to
a Gaussian distribution,
P
[
psX
(⃗n, nt
)]
∝ exp
{
−1
2
[
psX
(⃗n, nt
)]}
. (3.68)
The weight exp[−V(s)] and has the explicit form
|Z (Lt
)| exp
(
−S sX
)
, (3.69)
and it is used for the Hamiltonian dynamics of the auxiliary ﬁelds according to
˙psX
(τ) =−∂HHMC
∂sX
, (3.70)
˙sX (τ) = psX, (3.71)
whereas HHMC is
HHMC = 1
2 p2
sX + V (sX
). (3.72)
3. Exploring the phase space
With the previous equations we can explore the phase space of the process using the discretized
equations. Therefore, we use the leapfrog method, which is a simple and phase space area
preserving discretization scheme. We start with a half step departing from the initial conﬁguration,
p′
sX(0) = psX(0)− ϵHMC
2 ˙psX(0). (3.73)
Afterward we explore the phase space with full step size,
sX (τ + 1) = sX (τ) +ϵHMC p′
sX
(τ), (3.74)
p′
sX
(τ + 1) = psX
(τ) +ϵHMC ˙p′
sX
(τ), (3.75)
35
Chapter 3 Nuclear Lattice E ﬀective Field Theory
and add an additional half step in the end,
psX
(Nτ
) = p′
sX
(Nτ
) + ϵHMC
2 ˙p′
sX
(Nτ
). (3.76)
The evaluation of momenta between two full steps pushes the error toO(ϵ3
HMC) instead ofO(ϵ2
HMC)
in the case of evaluating the ﬁeld and the conjugate momenta at the same time point. For an
eﬃcient algorithm, it is necessary to choose the number of time steps Nτ and the step lengthϵHMC
such that the ﬁnal acceptance rate is large enough to get enough statistics but also that the phase
space is explored rapidly enough.
4. Metropolis test - accept or reject
At the end of the molecular dynamics evolution, one has a new conﬁguration of auxiliary ﬁelds
and their momenta, sX(Nτ), psX(Nτ)., The accept/ reject criterion reads
u< min
{
1, exp
{
−HHMC
[
sX
(Nτ
), psX
(Nτ
)]
+ HHMC
[
sX (0), psX
(0)
]}}
, (3.77)
where u is a random number between 0 and 1. The new conﬁguration is accepted if Eq. (3.77) is
fulﬁlled. This accept/reject criterion is called Metropolis test and it fulﬁlls the detailed balance, a
necessary condition for the reversibility of the system in equilibrium.
5. Measuring observables
If the system is already in equilibrium and the state is accepted, we take statistics of all observables
according to Eqs. (3.63) and (3.65).
6. Continue from step 2
We repeat this procedure for Ntrial times, but we use the new conﬁguration sX(Nτ) as a starting
point if it has been accepted or we use the old conﬁguration sX(0) if it has been rejected.
