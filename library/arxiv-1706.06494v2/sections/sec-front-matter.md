---
doc_id: arxiv-1706.06494v2
doc_title: "Sampling General N-Body Interactions with Auxiliary Fields"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-5
source_pdf: 1706.06494v2.pdf
source_sha256: 3745319210df19bd
doc_brief: "Sampling General N-Body Interactions with Auxiliary Fields — 2 sections: Front matter; Acknowledgements"
---
Sampling General N-Body Interactions with Auxiliary Fields
Christopher Körber,1,∗ Evan Berkowitz,1,† and Thomas Luu1,‡
1Institut für Kernphysik and Institute for Advanced Simulation
Forschungszentrum Jülich
52425 Jülich Germany
(Dated: October 14, 2018)
We present a general auxiliary ﬁeld transformation which generates eﬀective interactions con-
taining all possible N-body contact terms. The strength of the induced terms can analytically be
described in terms of general coeﬃcients associated with the transformation and thus are control-
lable. This transformation provides a novel way for sampling 3- and 4-body (and higher) contact
interactions non-perturbatively in lattice quantum monte-carlo simulations. We show that our
method reproduces the exact solution for a two-site quantum mechanical problem.
PACS numbers: pacs
The introduction of auxiliary ﬁelds, e.g. via the
Hubbard-Stratonovitch (HS) transformation [1, 2], as a
means of linearizing the interaction term of the Hamil-
tonian in terms of its density operator is common prac-
tice in many areas of theoretical physics, and is particu-
larly prevalent in condensed matter and nuclear physics
[3, 4]. Upon linearization of the theory, the problem be-
comes that of many particles undergoing one-body inter-
actions with the ﬂuctuating background auxiliary ﬁeld.
In occupation number formalism, the problem becomes
very similar to that ofnon-interacting (amongst them-
selves)particles, whichinsomecasescanbeevaluatedvia
steepest-descent methods (e.g. 1-D Ising model). At the
very least, the transformation greatly facilitates numeri-
cal treatment of the many-body problem [5–8]. In path
integral formalisms that involve Grassmann ﬁelds, the
transformation is essential as it reduces the Lagrangian
to terms bilinear in fermionic ﬁelds, which can subse-
quently be integrated out exactly via Grassmann gaus-
sian integration (e.g. bosonization of fermionic theories
[9]). The HS transformation is ideal for theories that ini-
tially have 2-body interactions (i.e. terms quadratic in
the density operator). In principle many-body interac-
tions can be linearized through recursive application of
the HS transformation, but at the cost of introducing nu-
merous auxiliary ﬁelds. A transformation that naturally
includes 3-body interactions, for example, would be ben-
eﬁcial for studying ultra-cold gases of polar molecules,
where 3-body (and higher) interactions can be tuned to
become dominant [10, 11].
In this Letter we detail a generalization of the HS
transformation that includes two-body and all possible
higher contact interactions that involves only one auxil-
iaryﬁeld. ThestandardHStransformationcanbeviewed
as a particular limit of this general transformation. Our
transformation, in principle, induces all possiblen-body
interactionsλ(n) ˆρn where ˆρ is the density operator. The
coeﬃcientsλ(n) are analytically determined and control-
lable through a set of accompanying coeﬃcientscj that
control the coupling of the density operator with thejth
power of the auxiliary ﬁeld in the linearized theory. The
numerical implementation of this transformation is triv-
ial as the sampling of the ﬁelds can be obtained from
known distributions. For 2-ﬂavor fermionic systems (e.g.
nucleons), this transformation allows for complete con-
trol of contact interactions up to 4-body in nature.
Formalism. Consider the following integral which is
intended to correspond to the interacting part of a par-
tition function at a single space-time point
Zc,N≡
∞∫
−∞
dφPN(φ) exp


−
2N−1∑
j=1
cjφj ˆρ


 , (1)
where PN(φ) is the normalized probability distribution
PN(φ) = N
Γ
( 1
2N
)e−φ2N
. (2)
Here,φisanauxiliaryﬁeldwhichcouplestothefermionic
density operator ˆρ = ∑
f
¯ψfψf, where f runs over the
diﬀerent fermion species at a given site. Because the
density operators at diﬀerent spacetime points commute,
we present only the derivation for a single point.
The argument of the exponential in (1) describes inter-
action vertices with an incoming and outgoing fermionic
ﬁeld (the density operator) and from one up to2N− 1
auxiliary ﬁelds associated with interaction strengthcj.
Theintegralisnormalizedsuchthat Zc,N→ 1forcj→ 0.
The result of the integration over the largest exponent of
φ times another polynomial inφ is given by
∞∫
−∞
dφe−φ2N
φ2k = Γ
( 1+2k
2N
)
N
N→∞
−→ 2
1 + 2k, ∀k∈ N0,N ∈ N.
(3)
It is suﬃcient to only consider polynomials in even pow-
ers ofφ because of the symmetry of the integration – odd
powers vanish. Also, in order for the integral to converge,
the leading exponent is not allowed to be odd inφ.
In this work we identify the integralZc,N with an eﬀec-
arXiv:1706.06494v2  [nucl-th]  29 Jun 2017
2
tiveactionconsistingofgeneral 2k-fermionicﬁeldvertices
Zλ≡ exp
{
−
∞∑
k=1
λ(k) ˆρk
}
. (4)
We expandZc,N andZλ in powers of the density oper-
ator ˆρ and systematically match order-by-order, relating
the auxiliary ﬁeld interactions to the induced many-body
forces. Using Faà di Bruno’s formula [12] we ﬁnd that
Zc,N =
∞∑
M =0
Z (M )
c,N ˆρM, (5)
Z (M )
c,N =
⌊(2N−1)M/2⌋∑
k=⌈M/2⌉
Γ
( 1+2k
2N
)
Γ
( 1
2N
)
∑
⃗ m∈M(2k)
N M
2k∏
j=1
[(−cj)mj
mj!
]
(6)
where the sum runs over the set
M(2k)
NM =
{
⃗ m∈ N 2k
0
⏐⏐⏐⏐⏐
( 2k∑
j=1
jmj = 2k
)
∧
( 2k∑
j=1
mj =M
)
∧ (j≥ 2N⇒mj = 0)
}
, (7)
and
Zλ =
∞∑
M =0
Z (M )
λ ˆρM, Z (M )
λ =
∑
⃗ m∈M(M )
M∏
k=1


(
−λ(k)
)mk
mk!

 (8)
where the sum inZ (M )
λ is over the set
M(M ) =
{
⃗ m∈ N M
0
⏐⏐⏐⏐⏐
M∑
k=1
kmk =M
}
. (9)
As the highest coeﬃcientλ(k) (in terms ofk) in (8) is
given byλ(M ) and is also linear in exactly this coeﬃcient
(because ifmM = 1 thenmj⁄=M = 0), one can recursively
determine all coeﬃcientsλ(M ) for M >0 by
Z (M )
λ =−λ(M ) +Z (M )
λ
⏐⏐
λ(M )→0 =Z (M )
c,N , Z (1)
λ
⏐⏐
λ(1)→0 = 0.
(10)
Note that one can prove by induction that each coef-
ﬁcientλ(M ) is proportional to a sum where each term
is a products of M fermion auxiliary-ﬁeld coeﬃcients:
λ(M )∝cj1··· cjM [13]. In Tab. I we show the coeﬃcients
of the induced forces up to the order of four-body forces
(M = 4) for three diﬀerent choices ofN.
Numerical Results. To demonstrate the eﬃcacy of
our transformation, we consider a system of 3 diﬀerent
fermion speciesf interacting on a two-site model (with
sites{0, 1}) with the following Hamiltonian,
ˆH =κ

−3
3∑
f =1
∑
⟨i,j⟩
ˆaf,iˆa†
f,j +λ(2) ∑
i∈{0,1}
ˆρ2
i +λ(3) ∑
i∈{0,1}
ˆρ3
i

 ,
(11)
where ˆa†
f,i (ˆaf,i) is a creation (annihilation) operator
for a fermion of speciesf at sitei and ˆρi =∑
f ˆa†
f,iˆaf,i
is the number operator at site i. Here the sum over
⟨i,j⟩ ∈ {(0, 1), (1, 0)} represents nearest neighbor hop-
pings between the two sites, andκ is a dimensionful pa-
rameter that sets the dynamical scale of our problem. As
is evident in (11),λ(2) andλ(3) represent the size of two-
and three-body interactions (relative toκ), respectively,
and are dimensionless. A positive (negative) value ofλ(i)
indicates a repulsive (attractive) interaction. We quote
results in units ofκ. The two-site model can be diag-
onalized and its spectrum directly determined from its
eigenvalues. We use the transfer matrix formalism [5] to
obtain this spectrum 1. With the spectrum in hand, we
comparetheseresultswiththoseobtainedfromastochas-
tic lattice projection calculation [5] where the introduc-
tion of auxiliary ﬁelds via our transformation is needed.
A detailed description of these calculations is in prepara-
tion [13]. In what follows, we give a succinct description.
The projection method extracts the lowest energy level
E in the spectrum of the system via
E =− lim
τ→∞
∂τ logZ[τ, ΨT ] , (12)
where Z is given by
Z[τ, ΨT ]≡⟨ ΨT|e−τ : ˆH:|ΨT⟩
=
∫ (∏
x
dφxPN(φx)
)
K[τ,⃗φ,cj, ΨT ], (13)
ΨT is an initial trial wavefunction, and⃗φ indicates the
collection of allφ overx, all space (both sites) and time
from 0 toτ.
Inthelaststepofthe(13)wehaveappliedourtransfor-
mation with its associated probability distributionPN(φ)
ateachspacetimepointandintroduced Kwhichisafunc-
tional ofφ and depends explicitly on the coeﬃcientscj,
the trial wavefunction ΨT, and the time separation τ.
The form ofPN(φ) depends on the orderN of the trans-
formation that is applied. For the work presented here,
1 We compare the spectrum obtained from the transfer matrix
(instead of direct diagonalization of the Hamiltonian) since it
incorporates lattice discretization eﬀects. This enables a direct
comparison with our lattice projection calculations.
3
N = 1 N = 2 N =∞, cj>3 = 0
λ(1) 0 γ3,1c2 1
3c2
λ(2) − 1
4c2
1 −
(
1
8−
γ2
3,1
2
)
c2
2− 1
4c1c3− 1
2γ3,1c2
1− 3
8γ3,1c2
3 − 1
6c2
1− 2
45c2
2− 1
5c1c3− 1
14c2
3
λ(3) 0
(
1
8−
γ2
3,1
2
)
c2
1c2 +
(
5
32−
3γ2
3,1
8
)
c2c2
3
2
45c2
1c2 + 8
2835c3
2 + 8
105c1c2c3 + 2
63c2c2
3
+ 1
2γ3,1c1c2c3 + 1
3γ3
3,1c3
2
λ(4) 0
(
γ2
3,1
8 − 1
96
)
c4
1−
γ3
3,1
2 c2
1c2
2−
(
3
64−
3γ2
3,1
16
)
c2
1c2
3
1
180c4
1 + 4
14175c4
2 + 1
105c3
1c3− 52
10395c2
2c2
3− 5
7644c4
3
−
γ3,1
8 c1c3
3−
(
1
8−
γ2
3,1
2
)
c1c2
2c3−
γ3,1+3γ3
3,1
8 c2
2c2
3 − 4
945c2
1c2
2 + 13
3150c2
1c2
3− 16
1575c1c2
2c3− 1
1155c1c3
3
−
(
1
192−
γ4
3,1
4
)
c4
2−
(
15
512−
9γ2
3,1
128
)
c4
3
Table I: We show the results of the matching for N = 1, N = 2, and N =∞ with all cj>3 = 0. The ﬁrst column is
the Hubbard-Stratonovich case, which produces only a two-body interaction. We repeatedly usedΓ(x) = (x− 1)Γ(x− 1) to
simplify manyN = 2 coeﬃcients, and use the shorthandγ3,1 = Γ(3/4)/Γ(1/4). We provide aMathematica notebook useful for
generating theλ(M ) for a givenN in the Supplementary Material.
we consider the two extreme cases
N = 1 P1(φ) = 1√π exp
(
−φ2)
(14)
N =∞ P∞(φ) =
{
1/2 |φ|< 1
0 otherwise (15)
The case N = 1 corresponds to the gaussian distribu-
tion of the original Hubbard-Stratonovich transformation
(and thus onlyλ(2) is nonzero), whereas forN =∞ we
have uniform sampling and in principle all allowed many-
body contact interactions. In theN =∞ case, there are
in principle an inﬁnite number ofcj—we set them all to
zero forj >3.
As our trial wavefunction for multifermion systems
|ΨT⟩ we pick a direct product state of single-particle
ground state wavefunctions,|ψf⟩ = 1√
2[a†
f,0−a†
f,1]|0⟩ for
each ﬂavorf. The direct product structure allows us to
write the functionalK in (13) as
K[τ,⃗φ,cj, ΨT ] =
(
K−1[τ;⃗φ,cj]
)α
(16)
where α is the number of fermion types and
K−1[τ;⃗φ,cj] = 1
2
(
K−1[0,τ ; 0, 0;⃗φ,cj]−K−1[0,τ ; 1, 0;⃗φ,cj]
−K−1[1,τ ; 0, 0;⃗φ,cj] +K−1[1,τ ; 1, 0;⃗φ,cj]
)
,
(17)
After introducing a time discretizationτ = aτt, theK
matrix is given by
K[i,t ;i′,t′;⃗φ,cj]≡δi,i′δt,t′ +aτδ⟨i,i′⟩δt,t′+1
+δi,i′δt,t′+1
(
c1φi,t +c2φ2
i,t +c3φ3
i,t− 1
)
. (18)
Here we have used the fact that we letcj = 0 for j >3.
We attach the indicesi and t on the auxiliary ﬁeld to
indicate that there exists auxiliary ﬁelds for each spatial
and temporal point.
Because we work with discretized time, we analyze the
discretized version of eq. (12),
E(τ)≡− 1
aτ
log
(Z[τ +aτ, ΨT ]
Z[τ, ΨT ]
)
(19)
and search for constant plateaus at long times to numer-
ically determine theτ→∞ limit.
In Fig. 1 we show the numerical results of E(τ)/κ
for combinations ofλ(M ) where λ(2)∈{± 1.74, 0.0} and
λ(3)∈{± 0.245, 0.0} for two and three-fermion systems.
For calculations withλ(3) = 0.0, φ was sampled accord-
ing to the HS distributionP1 and all other calculations
sampled according toP∞. Note that the coeﬃcientscj
can be complex. The solid lines correspond to the exact
answers from diagonalization of the transfer matrix, and
the dashed lines correspond to non-interacting energies.
Wenotethatforalltwo-fermioncalculations, both N = 1
and N =∞ calculations agree with each other, regard-
less of the value ofλ(3), since the 3-body interaction plays
no role. Furthermore, withλ(2) = 0.0 but nonzeroλ(3),
the two-fermion system reproduces the non-interacting
result. In the three-fermion system, the eﬀects ofλ(3)
are apparent and agree well with exact diagonalization.
A quantitative analysis will be given in [13], as well as
an analysis of signal-to-noise behavior for the diﬀerent
systems.
Discussion. The Hubbard-Stratonovitch transforma-
tion has been a useful tool for making analytic and nu-
merical progress in problems of physical interest, and is a
special case of the transformation described in this work.
Our transformation, which uses a self-interacting auxil-
4
4.55
4.50
4.45
4.40
4.35
4.30
4.25
λ(2) = + 1.74
E/
Two Flavors
5.0
4.8
4.6
4.4
4.2
4.0
3.8
3.6
Three Flavors
5.90
5.85
5.80
5.75
5.70
5.65
5.60
λ(2) = 0
E/
9.2
9.0
8.8
8.6
8.4
8.2
8.0
7.8
0.0 0.1 0.2 0.3 0.4 0.5
τ×
7.35
7.30
7.25
7.20
7.15
λ(2) = − 1.74
E/
P∞ (φ);        λ(3) = + 0.245
P1(φ);        λ(3) = 0
P∞ (φ);        λ(3) = − 0.245
0.0 0.1 0.2 0.3 0.4 0.5
τ×
14.0
13.5
13.0
12.5
Figure 1: E(τ)/κ for diﬀerent systems. All systems were studied with2× 108 measurements. Some systems show a signal-
to-noise problem and others yield an easy extraction of a constant plateau in the long-time-limit. The left panels all show
two-fermion systems and the corresponding right panels show the three-fermion systems with the same parameters. In the top
(middle) [bottom] two panels we show a system with repulsive (absent) [attractive] two-body forces. In the top four panels
red (blue) [green] points correspond to repulsive (absent) [attractive] three body forces, where the blue points were sampled
according to the HS distributionP1 and the other points according toP∞. The data in the mid two panels were generated
with P∞ and cj < 4 coeﬃcients tuned to exactly cancel the two-body force, and we show dashed lines for the corresponding
non-interacting energies.
iary ﬁeld, allows for the direct inclusion of controllable
many-body forces into numerical calculations.
Choosing a degree of auxiliary ﬁeld self-interaction
ﬁxes the sampling distribution and limits the types of
fermion/auxiliary-ﬁeld interaction vertices. These inter-
actions in turn generate a slew ofn-body forces. Sam-
pling a gaussian distribution for the auxiliary ﬁeld recov-
ers the original HS transformation, while uniform sam-
pling in principle allows for the independent control of all
possible n-body forces, while intermediate distributions
yield correlated forces.
We have demonstrated that on a two-site model, dif-
ferent sampling techniques reproduce the exact results in
a variety of cases, correctly handling all combinations of
attractive, repulsive, and absent two-body forces with at-
tractive and repulsive three-body forces. While even the
agreement of the one-body energies found with the diﬀer-
ent methods is nontrivial, the agreement of the two-body
systems between methods and agreement of three-body
systems with exact results indicate a reliable understand-
ing and deﬁnite control over many-fermion interactions.
One drawback of our method is that some combina-
tions of strengths of many-body forces are only achiev-
able with complex cj, opening the possibility of intro-
ducing a numerical sign problem [14]. Because the c
coeﬃcients appear nonlinearly in the higher-bodyλ co-
5
eﬃcients, there is not a unique set of cs that yield a
particular set ofλs.
It would be interesting to consider sampling by more
generic functions such as PN(φ) = exp( −∑
nα(n)φn)
with multiple tuneable φ self-interactions. For ﬁeld-
theoretic applications, it may prove fruitful to under-
stand how the renormalization of diﬀerentλ(M ) control
renormalization of the parameterscj.
We expect our transformation to be useful in a va-
riety of physical systems where many-body interactions
are important. Numerical applications may include den-
sity functional theory approaches to nuclear physics [15],
the nonperturbative inclusion of multinucleon forces into
NLEFT which might unlock precision characterizations
of halo nuclei, the study of systems near the Eﬁmov
threshold such as cold atoms (see Refs. [16, 17] and ref-
erences therein), systems at high density, and any other
system where contact interactions need stochastic imple-
mentation.
