---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-035-7-conclusions
section_title: "Conclusions"
section_number: 7
pages: 58-93
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The past 15 years have seen great progress in our understanding of nuclear forces in terms of low-energy
QCD. Key to this development was the realization that low-energy QCD is equivalent to an eﬀective ﬁeld
theory (EFT) which allows for a perturbative expansion that has become know as chiral perturbation theory
(ChPT). In this framework, two- and many-body forces emerge on an equal footing and the empirical fact
that nuclear many-body forces are substantially weaker than the two-nucleon force is explained naturally.
In this review, we have shown in detail how the two-nucleon force is derived from ChPT and demonstrated
that, at N3LO, the accuracy can be achieved that is necessary and suﬃcient for reliable microscopic nuclear
structure predictions. First calculations applying the N 3LO NN potential [68] in the conventional shell
model [75–77], the ab initio no-core shell model [78, 79], the coupled cluster formalism [80–86], and the
unitary-model-operator approach [87, 88] have produced promising results.
We also discussed nuclear many-body forces based upon chiral EFT. The 3NF at NNLO has been known
for a while [70, 71] and applied in few-nucleon reactions [71, 89–97], structure of light- and medium-mass
nuclei [98–101], and nuclear and neutron matter [102, 103] with some success. However, the famous ‘ Ay
puzzle’ of nucleon-deuteron scattering is not resolved by the 3NF at NNLO. Thus, one important open issue
are the few-nucleon forces beyond NNLO (“sub-leading few-nucleon forces”) which, besides the Ay puzzle,
may also resolve some important outstanding nuclear structure problems. As explained, this may require
going even beyond N 3LO.
Another open question is the convergence of the chiral expansion (of the two- as well as the three-nucleon
potentials) at orders beyond N 3LO, for which the inclusion of ∆-isobar degrees of freedom may be useful.
Furthermore, the non-perturbative renormalizations of the chiral potentials require more work and a better
understanding.
Finally, we note that topics of interest we did not discuss include parity-violating nuclear forces and
consistent electroweak currents.
Having identiﬁed some of the open issues, we hope that this review will be helpful towards future progress.
If the outstanding problems are resolved within the next few years, then, after 80 years of desperate
struggle, we may ﬁnally claim that the nuclear force problem is essentially under control. The greatest
beneﬁciary of such progress will be the ﬁeld of ab initio nuclear structure physics.
Acknowledgement
The work by R. M. was supported in part by the U.S. Department of Energy under Grant No. DE-FG02-
03ER41270. The work of D. R. E. was funded by the Ministerio de Ciencia y Tecnolog´ ıa under Contract
58
No. FPA2007-65748, the Junta de Castilla y Le´ on under Contract No. GR12, and the European Community-
Research Infrastructure Integrating Activity “Study of Strongly Interacting Matter” (HadronPhysics2 Grant
No. 227431).
Appendix A. Notation, conventions, and Feynman rules
Appendix A.1. Notation and conventions
The contravariant space-time four-vector is given by
xµ = (t,⃗ x) (A.1)
and the four-momentum vector reads
pµ = (E,⃗ p). (A.2)
We use units such that ℏ =c = 1.
Greek indices µ,ν , etc. run over the four space-time coordinate labels 0 , 1, 2, 3, with x0 = t the time
coordinate. Latin indices i,j,k , and so on run over the three space coordinate labels 1 , 2, 3. The metric is
diagonal with
gµν =gµν =


1 0
−1
−1
0 −1

 (A.3)
and the covariant versions of the above-mentioned vectors are
xµ =gµνxν = (t,−⃗ x), p µ =gµνpν = (E,−⃗ p), (A.4)
where summation over repeated indices is always understood; also
x2 =xµxµ =t2−⃗ x2. (A.5)
While for an ordinary three-vector we have, in general, ⃗ x= (x1,x 2,x 3), there is caution in place with the
(three-dimensional) nabla operator which is deﬁned to be
⃗∇ = (∇1,∇2,∇3) =
( ∂
∂xi
)
= (∂i) =
(
− ∂
∂xi
)
= (−∂i) (A.6)
The four-momentum operator reads
pµ = i ∂
∂xµ
=i∂µ =
(
i∂0,−i⃗∇
)
=
(
i∂
∂t,⃗ p
)
, (A.7)
pµ = i ∂
∂xµ =i∂µ =
(
i∂0,i⃗∇
)
=
(
i∂
∂t,−⃗ p
)
. (A.8)
The relativistic nucleon ﬁeld satisﬁes the free Dirac equation
(p /−MN) Ψ(x)≡ (γµpµ−MN) Ψ(x) = 0 (A.9)
whereMN denotes the nucleon mass andγµ the Dirac matrices which we apply in Dirac-Pauli representation
γ0 =
( I 0
0 −I
)
γi =
( 0 σi
−σi 0
)
(A.10)
with I the two-dimensional identity matrix and σi the Pauli matrices
σ1 =
(
0 1
1 0
)
σ2 =
( 0 −i
i 0
)
σ3 =
( 1 0
0 −1
)
. (A.11)
59
[
σi,σj]
= σiσj−σjσi = 2iϵijkσk, {σi,σj} =σiσj +σjσi = 2δij, (A.12)
σiσj = iϵijkσk +δij, (A.13)
with
ϵijk =



+1 if ( i,j,k ) even permutation of (1, 2, 3)
−1 if odd permutation
0 otherwise
(A.14)
Following convention, we denote the Pauli matrices byτa (a = 1, 2, 3) when operating in isospin space, with
τaτb =iϵabcτc +δab. (A.15)
Notice that, for isospin components, it does not make sense to distinguish between upper and lower indices
and, therefore, subscripts and superscripts have the same meaning.
The Dirac matrices have the properties
{γµ,γν} = 2gµν, γ 0†
=γ0γ0γ0 =γ0, γ i†
=γ0γiγ0 =−γi. (A.16)
The γ5-matrix is deﬁned by
γ5 =γ5 =iγ0γ1γ2γ3 =
( 0 I
I 0
)
. (A.17)
{γµ,γ 5} = 0, (γ5)2 = 1, γ 5†
=γ5. (A.18)
Commutator of γ matrices:
σµν = i
2 [γµ,γν] , γ µγν =gµν−iσµν, (A.19)
σij =ϵijk
( σk 0
0 σk
)
, σ 0i =i
( 0 σi
σi 0
)
=−σi0 (A.20)
The relativistic Dirac ﬁeld for positive-energy nucleons is
Ψ(x) =
∑
s,t
∫ d3p
(2π)3/2
√
MN
Ep
u(⃗ p,s)ξte−ip·xb(⃗ p,s,t) (A.21)
with the Dirac spinor given by
u(⃗ p,s) =
√
Ep +MN
2MN
(
I
⃗ σ·⃗ p
Ep+MN
)
χs (A.22)
whereEp =p0 =
√
⃗ p2 +M2
N. The Pauli spinors χs andξt describe, respectively, the spin and isospin of the
nucleon. Further,b(⃗ p,s,t) andb†(⃗ p,s,t) are destruction and creation operators for a nucleon with momentum
⃗ p, and spin and isospin quantum numbers s andt, respectively. They satisfy the anti-commutation relations
{
b(⃗ p,s,t),b†(⃗ p′,s′,t′)
}
=δs,s′δt,t′δ3(⃗ p−⃗ p′), (A.23)
{b(⃗ p,s,t),b (⃗ p′,s′,t′)} =
{
b†(⃗ p,s,t),b†(⃗ p′,s′,t′)
}
= 0. (A.24)
¯Ψ≡ Ψ†γ0 (A.25)
In the heavy-baryon formalism, the free ﬁeld equation for nucleons is, in leading order and using vµ =
(1, 0, 0, 0),
i∂0N(x) = 0 (A.26)
60
and the nucleon ﬁeld is
N(x) =
∑
s,t
∫ d3l
(2π)3/2 χsξte−il·xb(⃗l,s,t ) (A.27)
where l0 = 0 at leading order and ⃗l2/2MN at NLO.
¯N≡N†γ0 =N† (A.28)
The pion ﬁelds are in terms of their cartesian components ( i = 1, 2, 3; no distinction between upper and
lower index i)
πi(x) =
∫ d3q
(2π)3/2
1√
2ω
[
e−iq·xai(⃗ q) +eiq·xa†
i(⃗ q)
]
(A.29)
where ω =q0 =
√
⃗ q2 +m2π and ai and a†
i are, respectively, the destruction and creation operators obeying
the commutation relations [
ai(⃗ q),a†
j(⃗ q′)
]
=δijδ3(⃗ q−⃗ q′), (A.30)
[ai(⃗ q),aj(⃗ q′)] =
[
a†
i(⃗ q),a†
j(⃗ q′)
]
= 0. (A.31)
The charged and neutral pion ﬁelds are given by
π+ = 1√
2 (π1 +iπ2) , (A.32)
π− = 1√
2 (π1−iπ2) , (A.33)
π0 = π3. (A.34)
Throughout this article, we state amplitudes in terms of the “potential” V which is deﬁned by
V = iM (A.35)
whereM is the invariant amplitude, calculated according to Feynman rules. The relation of M to the
S-matrix is
⟨p1
′p2
′|S|p1p2⟩ = δ3(⃗ p1−⃗ p1
′)δ3(⃗ p2−⃗ p2
′)
+ (2π)4 δ4(p1 +p2−p1
′−p2
′) 1
(2π)6
( M4
N
E′
1E′
2E1E2
) 1
2
×M (p1
′,p 2
′;p1,p 2). (A.36)
Appendix A.2. Feynman rules
The basic formalism underlying the Feynman rules is the Dyson expansion of the S-matrix [cf. e. g.,
Eq. (6.1.1) of Ref. [225]]. Since we are applying covariant perturbation theory, we assume HI = −LI
(whereHI denotes the interaction Hamiltonian density and LI the interaction Lagrangian density) and
use the usual covariant Feynman propagators. From a procedural point of view, this is acceptable for
the derivative couplings considered here (see, however, Ref. [226] for exceptions). For a discussion of the
diﬀerences between covariant perturbation theory and time-ordered perturbation theory (also known as “old
fashioned” perturbation theory), see the evaluation of the football diagram, Appendix B.2.2 below.
In all one-pion vertices given below,q denotes the four-momentum of an outgoing pion of isospin compo-
nenta. In all two-pion vertices,q1 denotes the four-momentum of an ingoing pion with isospin component a
andq2 the four-momentum of an outgoing pion with isospin componentb. Nucleon momenta are, in general,
denoted by p and p′.
61
Appendix A.2.1. Leading order
The relativistic version of the leading order πN Lagrangian has been given in Eq. (2.41). We consider
the axial-vector (AV) and the Weinberg-Tomozawa (WT) couplings, which involve one and two pion ﬁelds,
respectively. The relativistic AV interaction Lagrangian is given by
LAV =−gA
2fπ
¯Ψγµγ5τ Ψ·∂µπ. (A.37)
For simple Lagrangians like this one, the vertex is just i times the Lagrangian stripped oﬀ the ﬁelds which
generates (q out) gA
2fπ
γµγ5τaqµ. (A.38)
In the heavy baryon formalism, the AV Lagrangian reads [cf. Eq. (2.53)]
ˆLAV =−gA
2fπ
¯Nτ· (⃗ σ·⃗∇)πN (A.39)
with vertex (q out)
− gA
2fπ
τa⃗ σ·⃗ q. (A.40)
The relativistic WT coupling term is
LWT =− 1
4f2π
¯Ψγµτ· (π×∂µπ) Ψ (A.41)
implying the vertex (q1 in, q2 out)
1
4f2π
γµϵabcτc(qµ
1 +qµ
2 ). (A.42)
The Heavy Baryon version is
ˆLWT =− 1
4f2π
¯Nτ· (π×∂0π)N (A.43)
with vertex (q1 in, q2 out)
1
4f2π
ϵabcτc(q0
1 +q0
2). (A.44)
The relativistic nucleon propagator reads [cf. Eq. (A.9)]
i
/ p−MN +iϵ = i(/ p+MN)
p2−M2
N +iϵ (A.45)
and the leading order heavy baryon version of the nucleon propagator is given by [cf. Eq. (A.26)]
i
l0 +iϵ. (A.46)
The pion propagator is [cf. Eq. (2.32)]
iδab
q2−m2π +iϵ. (A.47)
62
Appendix A.2.2. Next-to-leading order
The “ﬁxed” part of the dimension-two HB Lagrangian is given in Eq. (2.56). It leads to a nucleon kinetic
energy correction
−i ⃗ p2
2MN
, (A.48)
and produces the one-pion vertex (q out)
gA
4MNfπ
τa⃗ σ· (⃗ p+⃗ p′)q0 (A.49)
and the two-pion vertex (q1 in, q2 out)
− 1
8MNf2π
ϵabcτc (⃗ p+⃗ p′)· (⃗ q1 +⃗ q2). (A.50)
The vertices Eqs. (A.49) and (A.50) are the ﬁrst relativistic corrections of the vertices Eqs. (A.40) and
(A.44), respectively. These corrections can also be obtained by starting from the corresponding relativistic
vertices Eqs. (A.38) and (A.42), sandwiching them between Dirac spinors, and making a 1 /MN expansion.
The “contact” part of the dimension-two Lagrangian, Eq. (2.57), gives rise to the following two-pion
vertices (q1 in, q2 out):
iδab
f2π
[
−4c1m2
π +
(
2c2− g2
A
4MN
)
q0
1q0
2 + 2c3q1µqµ
2
]
(A.51)
and
− i
f2π
(
c4 + 1
4MN
)
ϵijkϵabcσiτcqj
1qk
2. (A.52)
For more Feynman rules, see appendix A of Ref. [119].
Appendix B. Two-pion exchange contributions to the 2NF at NLO
An overview of the 2PE diagrams that contribute at NLO was shown in Fig. 3. We will now evaluate
the various groups of diagrams one by one.
Appendix B.1. Triangle diagrams
Appendix B.1.1. The triangles in covariant perturbation theory
The triangle diagrams are shown in Fig. B.1. The contributions from diagram (a) and (b) will be denoted
byVa and Vb, respectively. According to relativistic Feynman rules, one obtains
Va = i g2
A
16f4π
∫ d4l
(2π)4 (2lµ +qµ)ϵabcτc
1 ¯u1(⃗ p′)γµu1(⃗ p) i
(l +q)2−m2π +iϵ×
× i
l2−m2π +iϵ ¯u2(−⃗ p′)(−lν)τb
2γνγ5
i(k /N +MN)
k2
N−M2
N +iϵ(lρ +qρ)τa
2γργ5u2(−⃗ p), (B.1)
Vb = i g2
A
16f4π
∫ d4l
(2π)4 (2lµ +qµ)ϵabcτc
2 ¯u2(−⃗ p′)γµu2(−⃗ p) i
(l +q)2−m2π +iϵ×
× i
l2−m2π +iϵ ¯u1(⃗ p′)(−lν−qν)τb
1γνγ5
i(¯k /N +MN)
¯k2
N−M2
N +iϵ(lρ)τa
1γργ5u1(⃗ p), (B.2)
where the momenta are deﬁned in Fig. B.1 and q = (0,⃗ p′−⃗ p). The sum over the isospin operators is
ϵabcτc
iτb
jτa
j =−i 2τi·τj and, for the intermediate nucleon, we haveγνγ5(k /N +MN)γργ5 =γν(k /N−MN)γρ.
63
(a) (b)
kN=
(
Ep−l0,−⃗ p′−⃗l
)
¯kN=
(
Ep−l0, ⃗ p−⃗l
)
l
l+q
b
a
kN µ
ν
ρ
(Ep, ⃗ p) (Ep,−⃗ p)
(Ep, ⃗ p′) (Ep,−⃗ p′)
l+q
b
a
l
¯kNµ
ν
ρ
(Ep, ⃗ p) (Ep,−⃗ p)
(Ep, ⃗ p′) (Ep,−⃗ p′)
Figure B.1: Two-pion exchange triangle diagrams at NLO.
Thus,
Va = −iτ 1·τ 2
g2
A
8f4π
∫ d4l
(2π)4 (2lµ +qµ)¯u1(⃗ p′)γµu1(⃗ p) 1
(l +q)2−m2π +iϵ×
× 1
l2−m2π +iϵ ¯u2(−⃗ p′)(−lν)γν
(k /N−MN)
k2
N−M2
N +iϵ(lρ +qρ)γρu2(−⃗ p), (B.3)
Vb = −iτ 1·τ 2
g2
A
8f4π
∫ d4l
(2π)4 (2lµ +qµ)¯u2(−⃗ p′)γµu2(−⃗ p) 1
(l +q)2−m2π +iϵ×
× 1
l2−m2π +iϵ ¯u1(⃗ p′)(−lν−qν)γν
(¯k /N−MN)
¯k2
N−M2
N +iϵ(lρ)γρu1(⃗ p). (B.4)
At NLO, only the lowest order in the 1 /MN expansion is included. The nucleon mass dependence comes
from the Dirac spinors and the nucleon propagator and performing such an expansion, we ﬁnd at lowest
order
¯uiγµui ≈ δµ0 (B.5)
¯uiγν(k /N−MN)γρui ≈ δνjδρm2MN(δjm +iϵjmnσn
i ) (B.6)
1
k2
N−M2
N +iϵ ≈ 1
2MN
1
−l0 +iϵ (B.7)
In this approximation, the amplitudes are
Va = −iτ 1·τ 2
g2
A
4f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
1
l2−m2π +iϵ×
× (δjm +iϵjmnσn
2 )(lj)(lm +qm) (B.8)
Vb = −iτ 1·τ 2
g2
A
4f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
1
l2−m2π +iϵ×
× (δjm +iϵjmnσn
1 )(lj +qj)(lm) (B.9)
where we used q0 = 0.
64
Alternatively, one can derive the NLO triangle diagram contributions by using the HB formalism from
the outset. Using the Feynman rules for the HB Lagrangians and propagators yields
V HB
a = i g2
A
16f4π
∫ d4l
(2π)4 (2l0)ϵabcτc
1
i
(l +q)2−m2π +iϵ
i
l2−m2π +iϵ×
×τb
2(⃗ σ2·⃗l) i
−l0 +iϵτa
2 (−⃗ σ2· (⃗l +⃗ q)), (B.10)
V HB
b = i g2
A
16f4π
∫ d4l
(2π)4 (2l0)ϵabcτc
2
i
(l +q)2−m2π +iϵ
i
l2−m2π +iϵ×
×τb
1(⃗ σ1· (⃗l +⃗ q)) i
−l0 +iϵτa
1 (−⃗ σ1·⃗l). (B.11)
Performing the isospin sums and using the identity ( ⃗ σ·⃗ a)(⃗ σ·⃗b) =⃗ a·⃗b +i⃗ σ· (⃗ a×⃗b), we obtain
V HB
a = −iτ 1·τ 2
g2
A
4f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
1
l2−m2π +iϵ×
×
[
⃗l· (⃗l +⃗ q) +i⃗ σ2· (⃗l× (⃗l +⃗ q))
]
, (B.12)
V HB
b = −iτ 1·τ 2
g2
A
4f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
1
l2−m2π +iϵ×
×
[
(⃗l +⃗ q)·⃗l +i⃗ σ1· ((⃗l +⃗ q)×⃗l)
]
. (B.13)
The two sets of Eqs. (B.8), (B.9) and (B.12), (B.13) obviously agree—as they should.
Since (⃗l +⃗ q)×⃗l =⃗ q×⃗l and since the integral over a term proportional to ⃗l will yield a result ∝⃗ q, the
spin dependent terms vanish and the sum of both triangles is given by
V =Va +Vb = −iτ 1·τ 2
g2
A
2f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
⃗l2 +⃗l·⃗ q
l2−m2π +iϵ. (B.14)
At this point, it might be of interest to compare with what other authors obtain for the NLO triangle
diagrams. In the work of Ref. [54], time-ordered perturbation theory (TOPT) (also known as old-fashioned
PT) is used in which loop integrals extend only over the three space-dimensions.
Thus, we will perform the integration over the time component in Eq. (B.14) to make a comparison with
TOPT possible. For convenience, we ﬁrst apply the transformation l = 1
2(l′−q), which yields
V = −iτ 1·τ 2
g2
A
8f4π
∫ d4l′
(2π)4
1
(l′ +q)2− 4m2π +iϵ
⃗l′2−⃗ q2
(l′−q)2− 4m2π +iϵ. (B.15)
The poles in the lower half plane are at l′0 =ω±−iϵ with
ω± =
√
(⃗l′±⃗ q)2 + 4m2π (B.16)
and, so, we can write the amplitude as
V = −iτ 1·τ 2
g2
A
8f4π
∫ d4l′
(2π)4
1
(l′0)2−ω2
+ +iϵ
⃗l′2−⃗ q2
(l′0)2−ω2
− +iϵ. (B.17)
Now we perform the integration over l′0 using the residue theorem
V = −τ 1·τ 2
g2
A
8f4π
∫ d3l′
(2π)3 (⃗l′2−⃗ q2)
{ 1
2ω+
1
ω2
+−ω2
−
+ 1
ω2
−−ω2
+
1
2ω−
}
= −τ 1·τ 2
g2
A
8f4π
∫ d3l′
(2π)3 (⃗l′2−⃗ q2)
{ 1
ω2
+−ω2
−
ω−−ω+
2ω+ω−
}
= τ 1·τ 2
g2
A
16f4π
∫ d3l′
(2π)3
⃗l′2−⃗ q2
ω+ω−(ω+ +ω−). (B.18)
65
Except for a typo in Ref. [54] and diﬀerences in notation, this agrees with the second term of Eq. (20) of
Ref. [54] as well as the ﬁrst term of Eq. (4.30) of Ref. [64], which both represent the triangle diagrams.
Appendix B.1.2. Dimensional regularization of the triangles
The integral is divergent and, therefore, requires regularization. In Ref. [54], this is done by introducing a
Gaussian cutoﬀ function exp(−⃗l2/Λ2) which, however, makes the results dependent on the cutoﬀ parameter
Λ. To avoid such cutoﬀ dependence, we will use dimensional regularization which was ﬁrst introduced by ’t
Hooft and Veltman in 1972 [227]. 6
For this it is convenient to go back to Eq. (B.14) and apply a trick discovered by Feynman [230],
1
ab =
∫ 1
0
dx
[b + (a−b)x]2 , (B.19)
which allows to write the product of propagators in terms of a linear combination. Applying Feynman’s
trick in Eq. (B.14) yields
V = τ 1·τ 2
g2
A
2f4π
∫ 1
0
dx
∫ d4l
i(2π)4
⃗l2 +⃗l·⃗ q
[l2 + (2lq +q2)x−m2π +iϵ]2 . (B.20)
The momentum integral is not yet quite ready for dimensional regularization because the integrand mixes
three- and four-dimensional versions of the loop-momentum l. The dimension of the integration variable l
must be consistent throughout the integrand.
Formal (four-dimensional) covariance can be re-covered by re-introducing the four-vectorvµ = (1, 0, 0, 0)
and re-writing the numerator as ⃗l2 +⃗l·⃗ q= (l·v)2−l2−l·q. After a shift of the integration variable
l→l +xq, well-known formulae for the dimensional regularization of covariant integrals can be applied [see,
e.g., Eqs. (10.23) and (10.32)-(10.34) of Ref. [229]].
Alternatively, one may go for consistency in three dimensions and reduce the momentum integral of
Eq. (B.20) to the three space-dimensions—which is what we will do here. This has the advantage that the
integration variable observes an Euclidean metric from the outset (and there is no need for a Wick rotation).
Moreover, the planar box diagram (see below) requires treatment in three dimensions.
The integrand of Eq. (B.20) has two poles as evidenced through
l2 + (2lq +q2)x−m2
π +iϵ =
[
l0 +
√
⃗l2 +m2π + (2⃗l·⃗ q+⃗ q2)x−iϵ
][
l0−
√
⃗l2 +m2π + (2⃗l·⃗ q+⃗ q2)x +iϵ
]
(B.21)
where we used q0 = 0. The pole in the lower half-plane is
l0
1 =
√
⃗l2 +m2π + (2⃗l·⃗ q+⃗ q2)x−iϵ, (B.22)
and, using the residue theorem, one obtains
V = τ 1·τ 2
g2
A
2f4π
∫ 1
0
dx
∫ dl0d3l
i(2π)4
⃗l2 +⃗l·⃗ q
(l0−l0
1)2(l0 +l0
1)2
= τ 1·τ 2
g2
A
2f4π
∫ 1
0
dx
∫ d3l
(2π)3
1
4
⃗l2 +⃗l·⃗ q
(l0
1)3 . (B.23)
To proceed towards dimensional regularization, we now generalize the three-dimensional integral to (D− 1)
dimensions. Moreover, we introduce the renormalization scale λ and multiply the integral by λ4−D such
that the dimension of the amplitude stays the same for any D [228, 231],
V = τ 1·τ 2
g2
A
8f4π
λ4−D
∫ 1
0
dx
∫ dD−1l
(2π)D−1
⃗l2 +⃗l·⃗ q
(l0
1)3 . (B.24)
6Accessible introductions into dimensional regularization can be found in Refs. [228, 229] and a very pedagogical presentation
is provided in appendix A.2 of the Scherer review [113].
66
For convenience, we now divide all dimension-full quantities involved in the integral by λ and denote all
dimensionless quantities (except for the dimensionless momentum ⃗k) by a tilde; for example, ˜ q = ⃗ q/λ.
Furthermore, we shift the integration variable by introducing the new variable ⃗k with λ⃗k =⃗l +x⃗ q, so that
there are no terms linear in the integration variable in the denominator. Thus, we have now
l0
1 = λ
√
⃗k2 + ˜m2π + ˜q2x(1−x)−iϵ, (B.25)
and our integral reads
V = τ 1·τ 2
g2
A
8f4π
λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1
(k−x˜q)2 + (k−x˜q)· ˜q
[k2 + ˜m2π + ˜q2x(1−x)]3/2 . (B.26)
Terms with odd powers of k vanish,
V = τ 1·τ 2
g2
A
8f4π
λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1
k2−x(1−x)˜q2
[k2 + ˜m2π + ˜q2x(1−x)]3/2 . (B.27)
The volume element in (D− 1) dimensions is
dD−1k = kD−2dkd ΩD−1 (B.28)
with
∫
dΩD−1 = 2π(D−1)/2
Γ(D−1
2 ) . (B.29)
Thus,
V = τ 1·τ 2
g2
A
8f4π
2λ2
Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
∫ ∞
0
dk kD−x(1−x)˜q2kD−2
[k2 + ˜m2π + ˜q2x(1−x)]3/2 . (B.30)
Using [cf. for example, Eq. (A.35) of Ref. [113]]
∫ ∞
0
kD−2+n1
(k2 +s)n/2 dk = Γ(D+n1−1
2 )Γ(n+1−D−n1
2 )
2Γ(n
2 )
1
s
n+1−D−n1
2
, (B.31)
we obtain
V = τ 1·τ 2
g2
A
8f4π
λ2
Γ( 3
2)Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
{
Γ(D+1
2 )Γ( 2−D
2 )
[ ˜m2π + ˜q2x(1−x)](2−D)/2
−x(1−x)˜q2 Γ(D−1
2 )Γ( 4−D
2 )
[ ˜m2π + ˜q2x(1−x)](4−D)/2
}
. (B.32)
We choose D = 4−η and then take the limit η→ 0. To prepare for the latter, we expand the various
expressions involved up to ﬁrst order in η:
Γ(D+1
2 )
Γ(D−1
2 ) = D− 1
2 = 3−η
2
Γ
(4−D
2
)
= Γ
(η
2
)
= 2
η−γ +O(η)
Γ
(2−D
2
)
= Γ(η
2 )
η
2− 1 =−2
η +γ− 1 +O(η)
67
1
(4π)
D−1
2
= 1
(4π)
3
2
(4π)
η
2≈ 1
(4π)
3
2
(
1 +η
2 ln(4π)
)
1
( ˜m2π + ˜q2x(1−x))
4−D
2
≈ 1− η
2 ln( ˜m2
π + ˜q2x(1−x))
1
( ˜m2π + ˜q2x(1−x))
2−D
2
≈
[
1− η
2 ln( ˜m2
π + ˜q2x(1−x))
]
( ˜m2
π + ˜q2x(1−x)) (B.33)
Concerning the properties of the Γ-function, see, e.g., Ref. [232]; γ = 0.5772... is Euler’s constant; and we
used aϵ = exp(ϵ lna)≈ 1 +ϵ lna +... .
Hence
V = τ 1·τ 2
g2
A
8f4π
λ2
Γ( 3
2)
1
(4π)
3
2
(
1 +η
2 ln(4π)
)∫ 1
0
dx
{3−η
2
(
−2
η +γ− 1 +O(η)
)[
1− η
2 ln( ˜m2
π + ˜q2x(1−x))
]
( ˜m2
π + ˜q2x(1−x))
−x(1−x)˜q2
(2
η−γ +O(η)
)[
1− η
2 ln( ˜m2
π + ˜q2x(1−x))
]}
(B.34)
and neglecting terms of order η
V = τ 1·τ 2
g2
A
8f4π
λ2
Γ( 3
2)
1
(4π)
3
2
[(
−2
η +γ− 1− ln(4π)
)( 3
2 ˜m2
π + 5
12 ˜q2
)
+ ˜m2
π + 1
3 ˜q2 +
∫ 1
0
dx
(3
2 ˜m2
π + 5
2 ˜q2x(1−x)
)
ln( ˜m2
π + ˜q2x(1−x))
]
. (B.35)
The integral over the logarithmic term is
∫ 1
0
dx
(3
2 ˜m2
π + 5
2 ˜q2x(1−x)
)
ln( ˜m2
π + ˜q2x(1−x)) = −4
3 ˜m2
π− 25
36 ˜q2 +
(
3 ˜m2
π + 5
6 ˜q2
)
ln( ˜mπ)
+1
6(8 ˜m2
π + 5˜q2)L(q), (B.36)
where
L(q)≡ w
q lnw +q
2mπ
, w ≡
√
4m2π +q2, and q =|⃗ q|. (B.37)
Introducing the abbreviation
R ≡ −2
η +γ− 1− ln(4π), (B.38)
the ﬁnal result for the triangle diagrams at NLO in dimensional regularization reads
V = τ 1·τ 2
g2
A
384π2f4π
[
(18m2
π + 5q2)R− 4m2
π− 13
3 q2 + 2(18m2
π + 5q2) ln
(mπ
λ
)
+ (16m2
π + 10q2)L(q)
]
.
(B.39)
Renormalization in a Modiﬁed Minimal Subtraction scheme ( MS -scheme) [228] amounts to omitting the
R-term.
Appendix B.2. Football diagram
Appendix B.2.1. The football in covariant perturbation theory
The football diagram is shown in Fig. B.2. In the HB formalism, one obtains
V = i 1
2
1
16f4π
∫ d4l
(2π)4 (2l0 +q0)ϵabcτc
1
i
(l +q)2−m2π +iϵ
i
l2−m2π +iϵ(2l0 +q0)ϵbadτd
2 , (B.40)
68
l
l + q
b
a
µ ν
(Ep , ⃗ p) ( Ep , −⃗ p)
(Ep , ⃗ p′) ( Ep , −⃗ p′)
Figure B.2: Two-pion exchange football diagram at NLO.
where the factor 1
2 is a combinatoric factor and q = (0,⃗ p′−⃗ p). Using ϵabcτc
1ϵbadτd
2 =−2τ 1·τ 2 andq0 = 0,
V = iτ 1·τ 2
1
4f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
(l0)2
l2−m2π +iϵ. (B.41)
It is again of interest to compare with what other authors obtain for the diagram under consideration. As
discussed in conjunction with the triangle diagrams, in the work of Ref. [54], time-ordered perturbation
theory (TOPT) (also known as old-fashioned PT) is used in which loop integrals extend only over the three
space-dimensions. Therefore, we will perform the integration over the time component in Eq. (B.41) to
make a comparison with TOPT possible. Substituting l = 1
2(l′−q),
V = iτ 1·τ 2
1
16f4π
∫ d4l′
(2π)4
1
(l′ +q)2− 4m2π +iϵ
(l′0)2
(l′−q)2− 4m2π +iϵ
= iτ 1·τ 2
1
16f4π
∫ d4l′
(2π)4
1
(l′0)2−ω2
+ +iϵ
(l′0)2
(l′0)2−ω2
− +iϵ (B.42)
with
ω± =
√
(⃗l′±⃗ q)2 + 4m2π, (B.43)
and applying the residue theorem yields
V = τ 1·τ 2
1
16f4π
∫ d3l′
(2π)3
{ 1
2ω+
ω2
+
ω2
+−ω2
−
+ ω2
−
ω2
−−ω2
+
1
2ω−
}
= τ 1·τ 2
1
32f4π
∫ d3l′
(2π)3
ω+−ω−
ω2
+−ω2
−
= τ 1·τ 2
1
32f4π
∫ d3l′
(2π)3
1
ω+ +ω−
. (B.44)
This amplitude for the football diagram does not agree with Ref. [54], where the result for the football is
given by the ﬁrst term in Eq. (20). In our notation, the result of Ref. [54] and also of Ref. [64] [cf. Eq. (4.30)
therein] is
VORK = −τ 1·τ 2
1
128f4π
∫ d3l′
(2π)3
1
ω+ω−
(ω+−ω−)2
ω+ +ω−
. (B.45)
69
Appendix B.2.2. The proper calculation of the football in time-ordered perturbation theory
We will explain now the reason for the discrepancy between Eqs. (B.44) and (B.45). In covariant PT
theory one assumes for the interaction Hamiltonian densityHI =−LI. This is strictly speaking not correct
for derivative coupling, because in that case one has HI = −LI + additional noncovariant terms . For
relatively simple cases of derivative coupling, the additional terms are of the contact type. Now, in covariant
PT, there are also noncovariant contributions to the propagator, and it has been shown that for certain
interactions with derivative coupling these two groups of additional terms cancel. So, as a procedural matter,
in covariant PT, one can useHI =−LI and the usual covariant Feynman propagators, and everything comes
out right (cf. e. g., Ref. [225], pp. 318-323 therein).
In TOPT the story is diﬀerent. Propagators are just non-covariant energy denominators, which cancel
nothing. Therefore, the full interaction Hamiltonian including all additional terms has to be use to obtain
the same result as in covariant PT. However, in Ref. [54] HI =−LI is assumed in conjunction with TOPT.
Thus, the contributions from the additional contact terms in the Hamiltonian are missing in the calculation
of Ref. [54] and that is the reason for the discrepancy with the covariant calculation, as we will show now.
Using the notation of Ref. [225], the time-component of the current associated with the Lagrangian
density Eq. (A.43) reads
J0
b = 1
4f2π
¯NτcNϵabcπa (B.46)
and the additional term in the interaction Hamiltonian is [cf. Eq. (12) of Ref. [51]]
Hadd
I (t) =
∫
d3x 1
2 (J0
b )(J0
b ) =
∫
d3x 1
2
1
16f4π
¯NτcNϵabcπa ¯Nτc′
Nϵa′bc′
πa′. (B.47)
This generates the following leading contribution to the S-matrix
⟨p′
1p′
2|S|p1p2⟩ = ( −i)
∫
dtH add
I (t) =−i
∫
d4x 1
16f4π
1
2ϵabcϵa′bc′
⟨p′
1p′
2| ¯NτcNπa ¯Nτc′
Nπa′|p1p2⟩
= −i
(2π)6
∫
d4x 2 1
16f4π
1
2ϵabcϵa′bc′
τc
1τc′
2 ei(p′
1+p′
2−p1−p2)x⟨0|πaπa′|0⟩, (B.48)
where the factor of 2 comes from the permutation of the nucleon ﬁelds and the exchange term is left out.
For the pion ﬁelds, we obtain
⟨0|πaπa′|0⟩ = 1
(2π)3
∫
d3kd3k′ 1√4ωkωk′
⟨0|
(
aa(⃗k)e−ikx +a†
a(⃗k)eikx
)(
aa′(⃗k′)e−ik′x +a†
a′(⃗k′)eik′x
)
|0⟩
= 1
(2π)3
∫
d3kd3k′ 1√4ωkωk′
δ3(⃗k−⃗k′)δaa′ =
∫ d3k
(2π)3
1
2ωk
δaa′. (B.49)
Hence,
⟨p′
1p′
2|S|p1p2⟩ = −i
(2π)6
∫
d4x 1
16f4π
ϵabcϵa′bc′
τc
1τc′
2 ei(p′
1+p′
2−p1−p2)x
∫ d3k
(2π)3
1
2ωk
δaa′
= −i(2π)4δ4(p′
1 +p′
2−p1−p2) 1
(2π)6
1
16f4π
ϵabcϵa′bc′
τc
1τc′
2
∫ d3k
(2π)3
1
2ωk
δaa′
= −i(2π)4δ4(p′
1 +p′
2−p1−p2) 1
(2π)6
1
8f4π
τ 1·τ 2
∫ d3k
(2π)3
1
2
√
⃗k2 +m2π
= −i(2π)4δ4(p′
1 +p′
2−p1−p2) 1
(2π)6
1
32f4π
τ 1·τ 2
∫ d3l
(2π)3
1
2
√
⃗l2 + 4m2π
,
(B.50)
70
where⃗k =⃗l/2 and ϵabcϵabc′
τc
1τc′
2 = 2τ 1·τ 2 . From the last equation, one can read oﬀ the contribution to
the T -matrix [cf. Eqs. (A.36) and (A.35)], which is
V add = τ 1·τ 2
1
32f4π
∫ d3l
(2π)3
1
2
√
⃗l2 + 4m2π
(B.51)
Obviously, this additional term doesn’t depend on external momenta, only on mπ.
For the amplitude, calculated in TOPT and including all terms, we now get
V = VORK +V add (B.52)
= VORK + τ 1·τ 2
1
32f4π
∫ d3l
(2π)3
1
2
√
⃗l2 + 4m2π
(B.53)
= VORK + τ 1·τ 2
1
32f4π
∫ d3l′
(2π)3
1
2ω+
(B.54)
= VORK + τ 1·τ 2
1
32f4π
∫ d3l′
(2π)3
{ 1
4ω+
+ 1
4ω−
}
(B.55)
= VORK + τ 1·τ 2
1
32f4π
∫ d3l′
(2π)3
(ω+ +ω−)2
ω+ +ω−
1
4ω+ω−
(B.56)
= τ 1·τ 2
1
32f4π
∫ d3l′
(2π)3
1
ω+ +ω−
(B.57)
where we used the transformations ⃗l =⃗l′ +⃗ qand⃗l′↦→−⃗l′. This result is now identical to the one obtained
using covariant PT, Eq. (B.44), as it should. We note that the term, Eq. (B.51), left out in the calculation
of Ref. [54], is a contact term∝m2
π, which aﬀects the mπ-dependence of the 2PE potential. Such terms are
relevant for the charge-dependence of the nuclear force [188] and for considerations of the chiral limit [129].
If these more subtle aspects are not of interest, then omitting the contact Eq. (B.51) is acceptable, since
contact terms with adjustable parameters are added to the theory anyhow (cf. Section 2.3).
Appendix B.2.3. Dimensional regularization of the football
We start from Eq. (B.41),
V = iτ 1·τ 2
1
4f4π
∫ d4l
(2π)4
1
(l +q)2−m2π +iϵ
(l0)2
l2−m2π +iϵ, (B.58)
and apply the Feynman trick Eq. (B.19),
V =−τ 1·τ 2
1
4f4π
∫ 1
0
dx
∫ d4l
i(2π)4
(l0)2
[l2 + (2lq +q2)x−m2π +iϵ]2 . (B.59)
Using the residue theorem for the l0 integration, we obtain
V = −τ 1·τ 2
1
4f4π
∫ 1
0
dx
∫ dl0d3l
i(2π)4
(l0)2
(l0−l0
1)2(l0 +l0
1)2
= τ 1·τ 2
1
4f4π
∫ 1
0
dx
∫ d3l
(2π)3
1
4
1
l0
1
(B.60)
with l0
1 =
√
⃗l2 +m2π + (2⃗l·⃗ q+⃗ q2)x−iϵ.
We treat this divergent integral by dimensional regularization (cf. Appendix B.1.2). For that purpose,
we extend the integral to ( D− 1) dimensions and shift the integration variable to λ⃗k =⃗l +x⃗ qwith λ the
renormalization scale:
V = τ 1·τ 2
1
16f4π
λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1
1
[⃗k2 + ˜m2π + ˜q2x(1−x)]1/2
, (B.61)
71
where quantities with a tilde are divided by λ and, thus, dimensionless; and⃗k is dimensionless by deﬁnition.
The angular integration yields [cf. Eqs. (B.28) and (B.29)]
V = τ 1·τ 2
1
16f4π
2λ2
Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
∫ ∞
0
dk kD−2
[⃗k2 + ˜m2π + ˜q2x(1−x)]1/2
(B.62)
and applying Eq. (B.31) we obtain
V = τ 1·τ 2
1
16f4π
λ2Γ( 2−D
2 )
Γ( 1
2)(4π)(D−1)/2
∫ 1
0
dx 1
[ ˜m2π + ˜q2x(1−x)](2−D)/2 . (B.63)
Choosing D = 4−η and using relations displayed in Eq. (B.33) results in
V = τ 1·τ 2
1
16f4π
λ2
Γ( 1
2) (4π)
3
2
(
1 +η
2 ln(4π)
)(
−2
η +γ− 1
)
×
×
∫ 1
0
dx
[
1− η
2 ln( ˜m2
π + ˜q2x(1−x))
](
˜m2
π + ˜q2x(1−x)
)
, (B.64)
and, neglecting terms of order η, leads to
V = τ 1·τ 2
1
16f4π
λ2
Γ( 1
2) (4π)
3
2
[(
−2
η +γ− 1− ln(4π)
)(
˜m2
π + 1
6 ˜q2
)
+
∫ 1
0
dx
(
˜m2
π + ˜q2x(1−x)
)
ln( ˜m2
π + ˜q2x(1−x))
]
. (B.65)
The integral over the logarithmic term is
∫ 1
0
dx
(
˜m2
π + ˜q2x(1−x)
)
ln( ˜m2
π + ˜q2x(1−x)) =−4
3 ˜m2
π− 5
18 ˜q2 +
(
2 ˜m2
π + 1
3 ˜q2
)
ln( ˜mπ) + ˜q2 + 4 ˜m2
π
3 L(q)
(B.66)
with L(q) given in Eq. (B.37).
Thus, for the football at NLO , we ﬁnally get
V = τ 1·τ 2
1
384π2f4π
[1
2R (6m2
π +q2)− 4m2
π− 5
6q2 + (6m2
π +q2) ln
(mπ
λ
)
+w2L(q)
]
(B.67)
with R as deﬁned in Eq. (B.38) and w given in Eq. (B.37).
Appendix B.3. Box and crossed box diagrams
The planar box (pb) and crossed box (cb) diagrams together with our notation are shown in Fig. B.3
and the corresponding amplitudes are given by
V pb = i g4
A
16f4π
∫ d4l
(2π)4
i
q2
1−m2π +iϵ
i
q2
2−m2π +iϵ×
×¯u1(⃗ p′)(−qν
2)τb
1γνγ5
i(/ kN1 +MN)
k2
N1−M2
N +iϵqµ
1τa
1γµγ5u1(⃗ p)×
×¯u2(−⃗ p′)qτ
2τb
2γτγ5
i(/ kN2 +MN)
k2
N2−M2
N +iϵ(−qρ
1)τa
2γργ5u2(−⃗ p), (B.68)
V cb = i g4
A
16f4π
∫ d4l
(2π)4
i
q2
1−m2π +iϵ
i
q2
2−m2π +iϵ×
×¯u1(⃗ p′)(−qν
2)τb
1γνγ5
i(/ kN1 +MN)
k2
N1−M2
N +iϵqµ
1τa
1γµγ5u1(⃗ p)×
×¯u2(−⃗ p′)(−qτ
1)τa
2γτγ5
i(/¯kN2 +MN)
¯k2
N2−M2
N +iϵqρ
2τb
2γργ5u2(−⃗ p), (B.69)
72
(a) (b)
kN1 = (Ep − l0 , ⃗l)
kN2 = (Ep + l0 , −⃗l)
kN1 = (Ep − l0 , ⃗l)
¯kN2 = (Ep − l0 , ⃗l − ⃗ p− ⃗ p′)
q2
q1
b
a
kN2kN1
ν
µ
τ
ρ
(Ep, ⃗ p) ( Ep, −⃗ p)
(Ep, ⃗ p′) ( Ep, −⃗ p′)
q2
b
a
q1
kN1
¯kN2
ρ
τν
µ
(Ep , ⃗ p) ( Ep , −⃗ p)
(Ep , ⃗ p′) ( Ep , −⃗ p′)
Figure B.3: Two-pion exchange planar box (a) and crossed box (b) diagrams at NLO.
where we chose the loop momentum such that its time-component is the energy transferred by the pions
and its space-components are the ones of an intermediate nucleon; kN1 = (Ep−l0,⃗l), kN2 = (Ep +l0,−⃗l),
q1 = (l0,⃗ p−⃗l), and q2 = (l0,⃗ p′−⃗l), with Ep =
√
⃗ p2 +M2
N, for the planar box diagram. For the crossed
box, only the momentum of nucleon 2 is diﬀerent, ¯kN2 = (Ep−l0,⃗l−⃗ p−⃗ p′). The poles are located at
l0
1 = Ep∓El±iϵ
l0
2 = −Ep∓El±iϵ
¯l0
2 = Ep∓E¯l±iϵ
l0
3 = ∓ω1±iϵ
l0
4 = ∓ω2±iϵ (B.70)
withω1 =
√
(⃗ p−⃗l)2 +m2π,ω2 =
√
(⃗ p′−⃗l)2 +m2π,El =
√
⃗l 2 +M2
N, andE¯l =
√
(⃗l−⃗ p−⃗ p′)2 +M2
N. The
ﬁrst three lines state the nucleon poles and the last two lines describe the pion poles. l0
2 and ¯l0
2 are the poles
for nucleon 2 in the box and crossed box diagrams, respectively. We apply the Feynman trick Eq. (B.19) to
the pion propagators and obtain
V pb = i g4
A
16f4π
(3− 2τ 1·τ 2)
∫ 1
0
dx
∫ d4l
(2π)4
1
[l02−ω2
1 + (ω2
1−ω2
2)x +iϵ]2×
×¯u1(⃗ p′)qν
2γν
/ kN1−MN
(l0−Ep)2− (l0
1−Ep)2qµ
1γµu1(⃗ p)×
×¯u2(−⃗ p′)qτ
2γτ
/ kN2−MN
(l0 +Ep)2− (l0
2 +Ep)2qρ
1γρu2(−⃗ p), (B.71)
V cb = i g4
A
16f4π
(3 + 2τ 1·τ 2)
∫ 1
0
dx
∫ d4l
(2π)4
1
[l02−ω2
1 + (ω2
1−ω2
2)x +iϵ]2×
×¯u1(⃗ p′)qν
2γν
/ kN1−MN
(l0−Ep)2− (l0
1−Ep)2qµ
1γµu1(⃗ p)×
×¯u2(−⃗ p′)qτ
1γτ
/¯kN2−MN
(l0−Ep)2− (¯l0
2−Ep)2qρ
2γρu2(−⃗ p), (B.72)
73
where we used τb
1τa
1τb
2τa
2 = 3− 2τ 1·τ 2 and τb
1τa
1τa
2τb
2 = 3 + 2τ 1·τ 2. The pion poles are now given by
l0
34 = ∓
√
(1−x)ω2
1 +xω2
2±iϵ. (B.73)
Performing the 1/MN expansion yields
¯u1γν(k /N1−MN)γµu1 ≈ δνiδµj2MN(δij +iϵijrσr
1), (B.74)
¯u2γτ(k /N2−MN)γρu2 ≈ δτmδρn2MN(δmn +iϵmnsσs
2), (B.75)
1
(l0−Ep)2− (l0
1−Ep)2× 1
(l0 +Ep)2− (l0
2 +Ep)2 ≈ 1
4M2
N
1
(−l0 +iζ)(l0 +iζ), (B.76)
1
(l0−Ep)2− (l0
1−Ep)2× 1
(l0−Ep)2− (¯l0
2−Ep)2 ≈ 1
4M2
N
1
(l0−iϵ)2 , (B.77)
where iζ = ⃗ p2−⃗l2
2MN
+iϵ, which avoids the pinch singularity (cf. discussion on p. 7 of Ref. [51]). Hence,
V pb = i g4
A
16f4π
(3− 2τ 1·τ 2)
∫ 1
0
dx
∫ d4l
(2π)4
qi
2qj
1(δij +iϵijrσr
1)qm
2 qn
1 (δmn +iϵmnsσs
2)
(l0−l0
34)2(l0 +l0
34)2(l0 +iζ)(−l0 +iζ) , (B.78)
V cb = i g4
A
16f4π
(3 + 2τ 1·τ 2)
∫ 1
0
dx
∫ d4l
(2π)4
qi
2qj
1(δij +iϵijrσr
1)qm
1 qn
2 (δmn +iϵmnsσs
2)
(l0−l0
34)2(l0 +l0
34)2(l0−iϵ)2 . (B.79)
In both diagrams we have a contribution from the pion poles, but in the box diagram there is also a
contribution from the nucleon poles which is enhanced in the 1 /MN expansion and gives the iterated 1PE.
We work this out by closing the l0 contour integral in the lower half-plane and, collecting the contribution
from the pole at l0 =−iζ, results in
V pb
it = g4
A
16f4π
(3− 2τ 1·τ 2)
∫ 1
0
dx
∫ d3l
(2π)3
qi
2qj
1(δij +iϵijrσr
1)qm
2 qn
1 (δmn +iϵmnsσs
2)
(l0
34)4(2iζ) . (B.80)
Using
∫ 1
0
dx 1
(l0
34)4 =
∫ 1
0
dx 1
[ω2
1− (ω2
1−ω2
2)x]2 = 1
ω2
1ω2
2
, (B.81)
qi
2qj
1(δij +iϵijrσr
1)qm
2 qn
1 (δmn +iϵmnsσs
2) = ⃗ σ1· (⃗ p′−⃗l)⃗ σ1· (⃗ p−⃗l)⃗ σ2· (⃗ p′−⃗l)⃗ σ2· (⃗ p−⃗l), (B.82)
1
2iζ = MN
⃗ p2−⃗l2 +iϵ
, (B.83)
and changing⃗l→−⃗l, we obtain
V pb
it = g4
AMN
16f4π
(3− 2τ 1·τ 2)
∫ d3l
(2π)3
⃗ σ1· (⃗l +⃗ p′)⃗ σ2· (⃗l +⃗ p′)⃗ σ1· (⃗l +⃗ p)⃗ σ2· (⃗l +⃗ p)
(⃗ p2−⃗l2 +iϵ)((⃗l +⃗ p)2 +m2π)((⃗l +⃗ p′)2 +m2π)
(B.84)
which is the LO iterated 1PE.
Notice that the contribution from the nucleon pole in the crossed box diagram is zero.
Next, we calculate the contribution from the pion poles closing the l0 contour integral in the lower
half-plane with the pole of interest located at l0 =l0
34 =
√
(1−x)ω2
1 +xω2
2−iϵ:
V pb = 3g4
A
64f4π
(3− 2τ 1·τ 2)
∫ 1
0
dx
∫ d3l
(2π)3
(⃗ q1·⃗ q2 +i⃗ σ1· (⃗ q2×⃗ q1))(⃗ q1·⃗ q2 +i⃗ σ2· (⃗ q2×⃗ q1))
(l0
34)5 ,
(B.85)
V cb = − 3g4
A
64f4π
(3 + 2τ 1·τ 2)
∫ 1
0
dx
∫ d3l
(2π)3
(⃗ q1·⃗ q2 +i⃗ σ1· (⃗ q2×⃗ q1))(⃗ q1·⃗ q2−i⃗ σ2· (⃗ q2×⃗ q1))
(l0
34)5 .
(B.86)
74
We treat the divergent integrals by dimensional regularization (cf. Appendix B.1.2). For that purpose, we
extend the integrals to (D− 1) dimensions and shift the integration variable to λ⃗k =⃗ p−⃗l +x⃗ qwith λ the
renormalization scale and ⃗ q=⃗ p′−⃗ p:
V pb = 3g4
A
64f4π
(3− 2τ 1·τ 2)λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1
(˜q1· ˜q2 +i⃗ σ1· (˜q2× ˜q1))(˜q1· ˜q2 +i⃗ σ2· (˜q2× ˜q1))
[k2 + ˜m2π + ˜q2x(1−x)]5/2 ,
(B.87)
V cb = − 3g4
A
64f4π
(3 + 2τ 1·τ 2)λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1
(˜q1· ˜q2 +i⃗ σ1· (˜q2× ˜q1))(˜q1· ˜q2−i⃗ σ2· (˜q2× ˜q1))
[k2 + ˜m2π + ˜q2x(1−x)]5/2 ,
(B.88)
where quantities with a tilde are divided by λ and, thus, dimensionless; and⃗k is dimensionless by deﬁnition.
Since
˜q1 = ⃗k−x˜q, (B.89)
˜q2 = ⃗k− (x− 1)˜q, (B.90)
hence
˜q1· ˜q2 = k2 + ˜q2x(x− 1)− (2x− 1)⃗k· ˜q, (B.91)
˜q2× ˜q1 = ˜q×⃗k. (B.92)
Terms in odd powers of ⃗k vanish. Furthermore, because of
∫ dD−1k
(2π)D−1
kikj
[k2 + ˜m2π + ˜q2x(1−x)]5/2 = δij
D− 1
∫ dD−1k
(2π)D−1
k2
[k2 + ˜m2π + ˜q2x(1−x)]5/2 , (B.93)
we have
∫ dD−1k
(2π)D−1
(⃗k· ˜q)2
[k2 + ˜m2π + ˜q2x(1−x)]5/2 = 1
D− 1
∫ dD−1k
(2π)D−1
˜q2k2
[k2 + ˜m2π + ˜q2x(1−x)]5/2 ,
∫ dD−1k
(2π)D−1
(⃗k· ˜q)i⃗ σi· (˜q×⃗k)
[k2 + ˜m2π + ˜q2x(1−x)]5/2 = 0 ,
∫ dD−1k
(2π)D−1
i⃗ σ1· (˜q×⃗k)i⃗ σ2· (˜q×⃗k)
[k2 + ˜m2π + ˜q2x(1−x)]5/2 = 1
D− 1
∫ dD−1k
(2π)D−1
i2(⃗ σ1× ˜q)· (⃗ σ2× ˜q)k2
[k2 + ˜m2π + ˜q2x(1−x)]5/2 .
(B.94)
Whence
V pb = 3g4
A
64f4π
(3− 2τ 1·τ 2)λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1 ×
×
[k2 + ˜q2x(x− 1)]2 + k2
D−1
[
(2x− 1)2˜q2− (⃗ σ1× ˜q)· (⃗ σ2× ˜q)
]
[k2 + ˜m2π + ˜q2x(1−x)]5/2 , (B.95)
V cb = − 3g4
A
64f4π
(3 + 2τ 1·τ 2)λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1 ×
×
[k2 + ˜q2x(x− 1)]2 + k2
D−1
[
(2x− 1)2˜q2 + (⃗ σ1× ˜q)· (⃗ σ2× ˜q)
]
[k2 + ˜m2π + ˜q2x(1−x)]5/2 . (B.96)
Using (⃗ σ1× ˜q)· (⃗ σ2× ˜q) =λ−2[⃗ q2⃗ σ1·⃗ σ2− (⃗ σ1·⃗ q)(⃗ σ2·⃗ q)], the sum of the two diagrams is given by
V pb +V cb = WC(τ 1·τ 2) +VS(⃗ σ1·⃗ σ2) +VT (⃗ σ1·⃗ q)(⃗ σ2·⃗ q) (B.97)
75
with
WC = − 3g4
A
16f4π
λ2
∫ 1
0
dx
∫ dD−1k
(2π)D−1
[k2 + ˜q2x(x− 1)]2 + k2
D−1(2x− 1)2˜q2
[k2 + ˜m2π + ˜q2x(1−x)]5/2 , (B.98)
VT = 9g4
A
32f4π
∫ 1
0
dx
∫ dD−1k
(2π)D−1
k2
D−1
[k2 + ˜m2π + ˜q2x(1−x)]5/2 , (B.99)
VS = −q2VT. (B.100)
Applying the volume element in (D− 1) dimensions, Eqs. (B.28) and (B.29), we ﬁnd
WC = − 3g4
A
16f4π
2λ2
Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
∫ ∞
0
dk ×
×
kD+2 +kD ˜q2
[
2x(x− 1) + (2x−1)2
D−1
]
+kD−2˜q4x2(x− 1)2
[k2 + ˜m2π + ˜q2x(1−x)]5/2 , (B.101)
VT = 9g4
A
32f4π
2
Γ(D−1
2 )(4π)(D−1)/2
1
D− 1
∫ 1
0
dx
∫ ∞
0
dk kD
[k2 + ˜m2π + ˜q2x(1−x)]5/2 , (B.102)
and performing the k-integration with the help of Eq. (B.31), we obtain
WC = − 3g4
A
16f4π
λ2
Γ( 5
2)Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
{
Γ(D+3
2 )Γ( 2−D
2 )
[ ˜m2π + ˜q2x(1−x)](2−D)/2
+
Γ(D+1
2 )Γ( 4−D
2 )˜q2
[
2x(x− 1) + (2x−1)2
D−1
]
[ ˜m2π + ˜q2x(1−x)](4−D)/2 + Γ(D−1
2 )Γ( 6−D
2 )˜q4x2(x− 1)2
[ ˜m2π + ˜q2x(1−x)](6−D)/2


 , (B.103)
VT = 9g4
A
32f4π
1
Γ( 5
2)Γ(D−1
2 )(4π)(D−1)/2
1
D− 1
∫ 1
0
dx Γ(D+1
2 )Γ( 4−D
2 )
[ ˜m2π + ˜q2x(1−x)](4−D)/2 . (B.104)
We chooseD = 4−η and take the limit η→ 0 [cf. Eq. (B.33)],
WC = − g4
A
384π2f4π
λ2
∫ 1
0
dx
{
R
[
45 ˜m2
π + ˜q2(−6 + 105x− 105x2)
]
+ 48 ˜m2
π + 6˜q2(−1 + 22x− 22x2) + 12˜q4x2(x− 1)2
˜m2π + ˜q2x(1−x)
+
[
45 ˜m2
π + ˜q2(−6 + 105x− 105x2)
]
ln( ˜m2
π + ˜q2x(1−x))
}
, (B.105)
VT = − 3g4
A
128π2f4π
∫ 1
0
dx
{
R + 1 + ln( ˜m2
π + ˜q2x(1−x))
}
(B.106)
with R as deﬁned in Eq. (B.38). And performing the x-integration, we ﬁnally get for the planar box plus
crossed box diagrams at NLO
WC = − g4
A
384π2f4π
{[1
2R + ln
(mπ
λ
)]
(90m2
π + 23q2) + 16m2
π + 5
6q2
+
(
20m2
π + 23q2 + 48m4
π
w2
)
L(q)
}
, (B.107)
VT = − 1
q2VS =− 3g4
A
64π2f4π
[1
2R + ln
(mπ
λ
)
− 1
2 +L(q)
]
(B.108)
with w and L(q) given in Eq. (B.37).
76
Appendix B.4. Summary of 2PE contributions at NLO
Adding up all 2PE contributions at NLO, namely, the box and crossed boxes Eqs. (B.107) and (B.108),
the triangles Eq. (B.39), and the football Eq. (B.67), we obtain
WC = − 1
384π2f4π
{[
4m2
π(5g4
A− 4g2
A− 1) +q2(23g4
A− 10g2
A− 1) + 48g4
Am4
π
w2
]
L(q)
+
[
6m2
π(15g4
A− 6g2
A− 1) +q2(23g4
A− 10g2
A− 1)
]
ln
(mπ
λ
)
+4m2
π(4g4
A +g2
A + 1) +q2
6 (5g4
A + 26g2
A + 5)
}
(B.109)
VT = − 1
q2VS =− 3g4
A
64π2f4π
[
L(q) + ln
(mπ
λ
)
− 1
2
]
(B.110)
with w and L(q) given in Eq. (B.37), and where we applied renormalization in a Modiﬁed Minimal Sub-
traction scheme (MS -scheme) [228], i. e., the (inﬁnite) R-terms are subtracted. The results fully agree
with Ref. [55]. If one is not interested in subtle aspects, like charge-dependence [188] or the chiral limit
(mπ→ 0) [129], one may omit the polynomial terms in the above expressions [cf. Eqs. (4.9) and (4.10)],
since contact terms are added anyhow (cf. Section 4.3) which have the same mathematical structure and,
therefore, can absorb the polynomial terms. Thus, the contacts are getting renormalized by the polynomials
that result from dimensional regularization.
Appendix C. Two-pion exchange contributions to the 2NF at NNLO
Two-pion exchange diagrams that contribute at NNLO were shown in Fig. 4. These diagrams diﬀer from
the NLO diagrams, Fig. 3, by one insertion from the dimension-two Lagrangian, the vertices of which are
given in Appendix A.2.2. There are two kinds of second order vertices: The relativistic corrections of the
leading order Lagrangian, which are proportional to 1/MN, Eqs. (A.48)-(A.50), and new contact interactions
proportional to the LECs ci, Eqs. (A.51) and (A.52). Since the shapes of the NNLO diagrams are the same
as in the NLO case, the evaluation is very similar to what we presented in detail in Appendix B for the NLO
diagrams. The results for the irreducible 2PE at third order (NNLO) as derived by the Munich group [55]
were given in Sec. 4.1.2, Eqs. (4.13)–(4.18). Note that the irreducible 2PE depends on what is chosen for
the (reducible) iterated 1PE. For this, the Munich group applies the expression Eq. (4.25). Alternatively,
one may also use the form Eq. (4.26) implied by the BbS scheme [133], which diﬀers in third and higher
orders from the Munich expression. Therefore, when the BbS formalism is used, a (irreducible) correction
term has to be added to the Munich irreducible 2PE in higher orders. In terms of the notation introduced
in Eqs. (4.25) and (4.26), this correction term is given by:
V (KBW)
2π,it −V (EM)
2π,it =
∫ d3p′′
(2π)3
( 1
Ep
− 1
Ep′′
) M2
N
p2−p′′2 +iϵV1π(⃗ p′,⃗ p′′)V1π(⃗ p′′,⃗ p) (C.1)
= −
∫ d3p′′
(2π)3
M2
N
Ep′′Ep(Ep′′ +Ep)V1π(⃗ p′,⃗ p′′)V1π(⃗ p′′,⃗ p) (C.2)
≈ −
∫ d3p′′
(2π)3
1
2MN
V1π(⃗ p′,⃗ p′′)V1π(⃗ p′′,⃗ p), (C.3)
with the last line showing the correction in third order or NNLO, which is what we want to calculate here.
Using Eq. (4.5) and the relation τ 1·τ 2 τ 1·τ 2 = 3− 2τ 1·τ 2, and deﬁning ⃗l =⃗ p−⃗ p′′, yields
V (KBW)
2π,it −V (EM)
2π,it = − g4
A
32f4πMN
(3− 2τ 1·τ 2)
∫ d3l
(2π)3
⃗ σ1· (⃗l +⃗ q)⃗ σ2· (⃗l +⃗ q)
(⃗l +⃗ q)2 +m2π
⃗ σ1·⃗l ⃗ σ2·⃗l
l2 +m2π
(C.4)
= − g4
A
32f4πMN
(3− 2τ 1·τ 2)
∫ 1
0
dx
∫ d3l
(2π)3
⃗ σ1· (⃗l +⃗ q)⃗ σ2· (⃗l +⃗ q)⃗ σ1·⃗l ⃗ σ2·⃗l
[⃗l2 + (2⃗l·⃗ q+⃗ q2)x +m2π]2
,(C.5)
77
where, in the last line, we introduced the Feynman trick. We now extend the integral to (D− 1) dimensions
and make the change of variables λ⃗k =⃗l +x⃗ q(cf. Appendix B.1.2),
V (KBW)
2π,it −V (EM)
2π,it = − g4
A
32f4πMN
(3− 2τ 1·τ 2)λ3
∫ 1
0
dx
∫ dD−1k
(2π)D−1×
× ⃗ σ1· [⃗k + (1−x)˜q]⃗ σ2· [⃗k + (1−x)˜q]⃗ σ1· (⃗k−x˜q)⃗ σ2· (⃗k−x˜q)
[k2 + ˜m2π + ˜q2x(1−x)]2 . (C.6)
Since
⃗ σi· [⃗k + (1−x)˜q]⃗ σi· (⃗k−x˜q) = k2 + ˜q2x(x− 1)− (2x− 1)⃗k· ˜q +i⃗ σi· (˜q×⃗k), (C.7)
we obtain, making use of Eq. (B.94),
V (KBW)
2π,it −V (EM)
2π,it = − g4
A
32f4πMN
(3− 2τ 1·τ 2)λ3
∫ 1
0
dx
∫ dD−1k
(2π)D−1×
×
[k2 + ˜q2x(x− 1)]2 + k2
D−1[(2x− 1)2˜q2− (⃗ σ1× ˜q)(⃗ σ2× ˜q)]
[k2 + ˜m2π + ˜q2x(1−x)]2 . (C.8)
Applying (⃗ σ1× ˜q)(⃗ σ2× ˜q) =λ−2[q2⃗ σ1·⃗ σ2− (⃗ σ1·⃗ q)(⃗ σ2·⃗ q)], leads to
VC = − 3g4
A
32f4πMN
λ3
∫ 1
0
dx
∫ dD−1k
(2π)D−1
[k2 + ˜q2x(x− 1)]2 + k2
D−1(2x− 1)2˜q2
[k2 + ˜m2π + ˜q2x(1−x)]2 (C.9)
WC = −2
3VC (C.10)
VT = − 3g4
A
32f4πMN
λ
∫ 1
0
dx
∫ dD−1k
(2π)D−1
k2
D−1
[k2 + ˜m2π + ˜q2x(1−x)]2 (C.11)
VS = −q2VT (C.12)
WT = −2
3VT (C.13)
WS = −q2WT. (C.14)
Using the volume element in (D− 1) dimensions, Eqs. (B.28) and (B.29), we ﬁnd
VC = − 3g4
A
32f4πMN
2λ3
Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
∫ ∞
0
dk
kD+2 +kD ˜q2
[
2x(x− 1) + (2x−1)2
D−1
]
+kD−2˜q4x2(x− 1)2
[k2 + ˜m2π + ˜q2x(1−x)]2 ,
(C.15)
VT = − 3g4
A
32f4πMN
2λ
Γ(D−1
2 )(4π)(D−1)/2
1
D− 1
∫ 1
0
dx
∫ ∞
0
dk kD
[k2 + ˜m2π + ˜q2x(1−x)]2 . (C.16)
Performing the k-integration yields
VC = − 3g4
A
32f4πMN
λ3
Γ(2)Γ(D−1
2 )(4π)(D−1)/2
∫ 1
0
dx
{
Γ(D+3
2 )Γ( 1−D
2 )
[ ˜m2π + ˜q2x(1−x)](1−D)/2
+
Γ(D+1
2 )Γ( 3−D
2 )˜q2
[
2x(x− 1) + (2x−1)2
D−1
]
( ˜m2π + ˜q2x(1−x))(3−D)/2 + Γ(D−1
2 )Γ( 5−D
2 )˜q4x2(x− 1)2
[ ˜m2π + ˜q2x(1−x)](5−D)/2


 , (C.17)
VT = − 3g4
A
32f4πMN
λ
Γ(2)Γ(D−1
2 )(4π)(D−1)/2
1
D− 1
∫ 1
0
dx Γ(D+1
2 )Γ( 3−D
2 )
[ ˜m2π + ˜q2x(1−x)](3−D)/2 . (C.18)
78
We chooseD = 4−η and take the limit η→ 0,
VC = − 3g4
A
256πf 4πMN
∫ 1
0
5m4
π−m2
πq2(1− 20x + 20x2) +q4x(−1 + 17x− 32x2 + 16x3)√
m2π +q2x(1−x)
, (C.19)
VT = 3g4
A
256πf 4πMN
∫ 1
0
√
m2π +q2x(1−x), (C.20)
and, performing the x-integration, we ﬁnally obtain
VC = − 3g4
A
256πf 4πMN
(mπw2 + ~w4A(q)), (C.21)
VT = 3g4
A
512πf 4πMN
(mπ +w2A(q)). (C.22)
Appendix D. Two-pion exchange contributions to the 2NF at N 3LO
The fourth order 2PE contributions consist of two classes: the one-loop (Fig. 5) and the two-loop
diagrams (Fig. 6).
Appendix D.1. One-loop diagrams
This large pool of diagrams can be analyzed in a systematic way by introducing the following well-deﬁned
subdivisions.
Appendix D.1.1. c2
i contributions.
The only contribution of this kind comes from the football diagram with both vertices proportional to
ci (ﬁrst row of Fig. 5). One obtains [60]:
VC = 3L(q)
16π2f4π
[(c2
6w2 +c3~w2− 4c1m2
π
)2
+ c2
2
45w4
]
, (D.1)
WT = − 1
q2WS = c2
4w2L(q)
96π2f4π
, (D.2)
with L(q) and w deﬁned in Eq. (B.37) and
~w≡
√
2m2π +q2. (D.3)
Appendix D.1.2. ci/MN contributions.
This class consists of diagrams with one vertex proportional to ci and one 1 /MN correction. A few
graphs that are representative for this class are shown in the second row of Fig. 5. Symbols with a large
solid dot and an open circle denote 1/MN corrections of vertices proportional to ci. They are part of ˆL∆=2,
Eq. (2.67). The result for this group of diagrams is [60]:
VC = − g2
AL(q)
32π2MNf4π
[
(c2− 6c3)q4 + 4(6c1 +c2− 3c3)q2m2
π + 6(c2− 2c3)m4
π + 24(2c1 +c3)m6
πw−2]
,
(D.4)
WC = − c4q2L(q)
192π2MNf4π
[
g2
A(8m2
π + 5q2) +w2]
, (D.5)
WT = − 1
q2WS =− c4L(q)
192π2MNf4π
[
g2
A(16m2
π + 7q2)−w2]
, (D.6)
VLS = c2g2
A
8π2MNf4π
w2L(q), (D.7)
WLS = − c4L(q)
48π2MNf4π
[
g2
A(8m2
π + 5q2) +w2]
. (D.8)
79
Appendix D.1.3. 1/M2
N corrections.
These are relativistic 1 /M2
N corrections of the leading order 2 π exchange diagrams. Typical examples
for this large class are shown in row 3–6 of Fig. 5. This time, there is no correction from the iterated 1PE,
Eq. (4.25) or Eq. (4.26), since the expansion of the factor M2
N/Ep does not create a term proportional to
1/M2
N. The total result for this class is [61],
VC = − g4
A
32π2M2
Nf4π
[
L(q)
(
2m8
πw−4 + 8m6
πw−2−q4− 2m4
π
)
+ m6
π
2w2
]
, (D.9)
WC = − 1
768π2M2
Nf4π
{
L(q)
[
8g2
A
(3
2q4 + 3m2
πq2 + 3m4
π− 6m6
πw−2−k2(8m2
π + 5q2)
)
+4g4
A
(
k2(
20m2
π + 7q2− 16m4
πw−2)
+ 16m8
πw−4 + 12m6
πw−2− 4m4
πq2w−2− 5q4− 6m2
πq2− 6m4
π
)
−4k2w2
]
+ 16g4
Am6
π
w2
}
, (D.10)
VT = − 1
q2VS = g4
AL(q)
32π2M2
Nf4π
(
k2 + 5
8q2 +m4
πw−2
)
, (D.11)
WT = − 1
q2WS = L(q)
1536π2M2
Nf4π
[
4g4
A
(
7m2
π + 17
4 q2 + 4m4
πw−2
)
− 32g2
A
(
m2
π + 7
16q2
)
+w2
]
,
(D.12)
VLS = g4
AL(q)
4π2M2
Nf4π
(11
32q2 +m4
πw−2
)
, (D.13)
WLS = L(q)
256π2M2
Nf4π
[
16g2
A
(
m2
π + 3
8q2
)
+ 4
3g4
A
(
4m4
πw−2− 11
4 q2− 9m2
π
)
−w2
]
, (D.14)
VσL = g4
AL(q)
32π2M2
Nf4π
. (D.15)
Appendix D.2. Two-loop contributions.
The two-loop contributions are quite involved. In Fig. 6, we attempt a graphical representation of this
class. The gray disk stands for all one-loop πN graphs which are shown in some detail in the lower part
of the ﬁgure. Not all of the numerous graphs are displayed. Some of the missing ones are obtained by
permutation of the vertices along the nucleon line, others by inverting initial and ﬁnal states. Vertices
denoted by a small dot are from the leading order Lagrangian ˆL∆=0, Eq. (2.65). The solid square represents
vertices proportional to the LECs di introduced inL(3)
πN which is part of ˆL∆=2, Eq. (2.67). The di vertices
occur actually in one-loop NN diagrams, but we list them among the two-loop NN contributions because
they are needed to absorb divergences generated by one-loop πN graphs. Using techniques from dispersion
theory, Kaiser [60] calculated the imaginary parts of the NN amplitudes, Im Vα(iµ) and Im Wα(iµ), which
result from analytic continuation to time-like momentum transfer q = iµ− 0+ with µ≥ 2mπ. From this,
the momentum-space amplitudes Vα(q) and Wα(q) are obtained via the subtracted dispersion relations:
VC,S(q) = −2q6
π
∫ ∞
2mπ
dµ ImVC,S(iµ)
µ5(µ2 +q2), (D.16)
VT (q) = 2q4
π
∫ ∞
2mπ
dµ ImVT (iµ)
µ3(µ2 +q2), (D.17)
and similarly for WC,S,T .
80
In most cases, the dispersion integrals can be solved analytically and the following expressions are
obtained [67]:
VC(q) = 3g4
A~w2A(q)
1024π2f6π
[
(m2
π + 2q2)
(
2mπ + ~w2A(q)
)
+ 4g2
Amπ~w2]
;
(D.18)
WC(q) = W (a)
C (q) +W (b)
C (q), (D.19)
with
W (a)
C (q) = L(q)
18432π4f6π
{
192π2f2
πw2 ¯d3
[
2g2
A~w2− 3
5(g2
A− 1)w2
]
+
[
6g2
A~w2− (g2
A− 1)w2]
[
384π2f2
π
(
~w2( ¯d1 + ¯d2) + 4m2
π ¯d5
)
+L(q)
(
4m2
π(1 + 2g2
A) +q2(1 + 5g2
A)
)
−
(q2
3 (5 + 13g2
A) + 8m2
π(1 + 2g2
A)
)]}
(D.20)
and
W (b)
C (q) = −2q6
π
∫ ∞
2mπ
dµ ImW (b)
C (iµ)
µ5(µ2 +q2) , (D.21)
where
ImW (b)
C (iµ) = − 2κ
3µ(8πf 2π)3
∫ 1
0
dx
[
g2
A(2m2
π−µ2) + 2(g2
A− 1)κ2x2
]
×
{
− 3κ2x2 + 6κx
√
m2π +κ2x2 lnκx +
√
m2π +κ2x2
mπ
+g4
A
(
µ2− 2κ2x2− 2m2
π
)
[
5
6 + m2
π
κ2x2−
(
1 + m2
π
κ2x2
)3/2
lnκx +
√
m2π +κ2x2
mπ
]}
;
(D.22)
VT (q) = V (a)
T (q) +V (b)
T (q)
= − 1
q2VS(q) = − 1
q2
(
V (a)
S (q) +V (b)
S (q)
)
, (D.23)
with
V (a)
T (q) = − 1
q2V (a)
S (q) = −g2
Aw2L(q)
32π2f4π
( ¯d14− ¯d15) (D.24)
and
V (b)
T (q) = − 1
q2V (b)
S (q) = 2q4
π
∫ ∞
2mπ
dµ ImV (b)
T (iµ)
µ3(µ2 +q2), (D.25)
where
ImV (b)
T (iµ) = − 2g6
Aκ3
µ(8πf 2π)3
∫ 1
0
dx(1−x2)
[
−1
6 + m2
π
κ2x2−
(
1 + m2
π
κ2x2
)3/2
lnκx +
√
m2π +κ2x2
mπ
]
;
(D.26)
WT (q) = − 1
q2WS(q) = g4
Aw2A(q)
2048π2f6π
[
w2A(q) + 2mπ(1 + 2g2
A)
]
; (D.27)
81
-5
-4
-3
-2
-1
0
Phase Shift (deg)
0 100 200 300 400
Lab. Energy (MeV)
(1) N2LO 
(2) +c2  
(3) +c/M (4) +1/M2
(5) +2-L 
(6) +d   
 1F3
-3
-2
-1
0
1
2
Phase Shift (deg)
0 100 200 300 400
Lab. Energy (MeV)
(1) N2LO 
(2) +c2  
(3) +c/M 
(4) +1/M2
(5) +2-L 
(6) +d   
 3F3
0
2
4
6
8
Phase Shift (deg)
0 100 200 300 400
Lab. Energy (MeV)
(1) N2LO 
(2) +c2  
(3) +c/M (4) +1/M2
(5) +2-L 
(6) +d   
 3F4
-1
-0.75
-0.5
-0.25
0
0.25
Phase Shift (deg)
0 100 200 300 400
Lab. Energy (MeV)
(1) N2LO 
(2) +c2  
(3) +c/M 
(4) +1/M2
(5) +2-L 
(6) +d   
 3G5
Figure D.1: The eﬀect of individual fourth-order contributions on the neutron-proton phase shifts in some selected peripheral
partial waves. The individual contributions are added up successively in the order given in parentheses next to each curve.
Curve (1) is NNLO (“N2LO”) and curve (6) completes N 3LO. For further explanations, see Appendix D.3. Empirical phase
shifts (solid dots and open circles) as in Fig. 8.
where
A(q)≡ 1
2q arctan q
2mπ
and κ≡
√
µ2/4−m2π. (D.28)
Note that the analytic solutions hold modulo polynomials. We have checked the importance of those
contributions where we could not ﬁnd an analytic solution and where, therefore, the integrations have to be
performed numerically. It turns out that the combined eﬀect on NN phase shifts from W (b)
C ,V (b)
T , and V (b)
S
is smaller than 0.1 deg in F and G waves and smaller than 0.01 deg in H waves, at Tlab = 300 MeV (and
less at lower energies). This renders these contributions negligible. Therefore, we omit W (b)
C ,V (b)
T , and V (b)
S
in the construction of chiral NN potentials at order N 3LO (Section 4.6.3).
In Eqs. (D.20) and (D.24), we use the scale-independent LECs, ¯di, which are obtained by combining the
scale-dependent ones, dr
i (λ), with the chiral logarithm, ln( mπ/λ), or equivalently ¯di = dr
i (mπ). For more
details about this issue, see Ref. [123].
Appendix D.3. Impact of individual N 3LO contributions on peripheral phase shifts
The fourth order is obviously very diverse. Here, we will show how the individual fourth-order con-
tributions impact NN phase shifts in peripheral partial waves. For this purpose, we display in Fig. D.1
phase shifts for four important peripheral partial waves, namely, 1F3, 3F3, 3F4, and 3G5. In each frame, the
following curves are shown:
82
(1) NNLO (“N2LO”).
(2) The previous curve plus the c2
i graph, ﬁrst row of Fig. 5, Eqs. (D.1) and (D.2), denoted by ‘c2’ in the
ﬁgure.
(3) The previous curve plus the ci/MN contributions (denoted by ‘c/M’), second row of Fig. 5, Eqs. (D.4)-
(D.8).
(4) The previous curve plus the 1/M2
N corrections (‘1/M2’), row three to six of Fig. 5, Eqs. (D.9)-(D.15).
(5) The previous curve plus the two-loop contributions without the terms proportional to ¯di (‘2-L’); i.e.
Fig. 6, but without the solid square; Eqs. (D.18)-(D.27), but with all ¯di≡ 0.
(6) The previous curve plus the terms proportional to ¯di (denoted by ‘d’ in the ﬁgure) with the parameters
given in Table 2, column ‘Peripheral perturbative NN ’.
In summary, the various curves add up successively the individual N3LO contributions in the order indicated
in the curve label. The last curve in this series, curve (6), is the full N 3LO result.
Thec2
i graph generates large attraction in all partial waves [cf. diﬀerences between curves (1) and (2) in
Fig. D.1]. This attraction is compensated by repulsion from the ci/MN diagrams, in most partial waves; the
exception is 1F3 where ci/MN adds more attraction [curve (3)]. The 1 /M2
N corrections [diﬀerence between
curves (3) and (4)] are typically small. Finally, the two-loop contributions create substantial repulsion in
1F3 and 3G5 which brings 1F3 into good agreement with the data while causing a discrepancy for 3G5. In
3F3 and 3F4, there are large cancelations between the ‘pure’ two-loop graphs and the ¯di terms, making the
net two-loop contribution rather small.
A pivotal role in the above game is played byWS, Eq. (D.6), from theci/MN group. This attractive term
receives a factor of 9 in 1F3, a factor (−3) in 3G5, and a factor of 1 in 3F3 and 3F4. Thus, this contribution
is very attractive in 1F3 and repulsive in 3G5. The latter is the reason for the overcompensation of the c2
i
graph by the ci/MN contribution in 3G5 which is why the ﬁnal N 3LO result in this partial wave comes out
too repulsive. One can expect that 1/MN corrections that occur at order ﬁve or six will resolve this problem.
Before ﬁnishing this appendix, we like to point out that the problem with the 3G5 is not as dramatic as
it may appear from the phase shift plots—for two reasons. First, the 3G5 phase shifts are about one order of
magnitude smaller than the F and most of the other G phases. Thus, in absolute terms, the discrepancies
seen in 3G5 are small. In a certain sense, we are looking at ‘higher order noise’ under a magnifying glass.
Second, the 3G5 partial wave contributes 0.06 MeV to the energy per nucleon in nuclear matter, the total
of which is−16 MeV. Consequently, small discrepancies in the reproduction of 3G5 by a NN potential will
have negligible inﬂuence on the microscopic nuclear structure predictions obtained with that potential.
Appendix E. Fourth order NN contact potential: Partial wave decomposition
The contact potential of order four, Eq. (4.43), decomposes into partial-waves as follows
V (4)
ct (1S0) = ˆD1S0(p′4 +p4) +D1S0p′2p2
V (4)
ct (3P0) = D3P0(p′3p +p′p3)
V (4)
ct (1P1) = D1P1(p′3p +p′p3)
V (4)
ct (3P1) = D3P1(p′3p +p′p3)
V (4)
ct (3S1) = ˆD3S1(p′4 +p4) +D3S1p′2p2
V (4)
ct (3D1) = D3D1p′2p2
V (4)
ct (3S1−3D1) = ˆD3S1−3D1p4 +D3S1−3D1p′2p2
V (4)
ct (3D1−3S1) = ˆD3S1−3D1p′4 +D3S1−3D1p′2p2
83
V (4)
ct (1D2) = D1D2p′2p2
V (4)
ct (3D2) = D3D2p′2p2
V (4)
ct (3P2) = D3P2(p′3p +p′p3)
V (4)
ct (3P2−3F2) = D3P2−3F2p′p3
V (4)
ct (3F2−3P2) = D3P2−3F2p′3p
V (4)
ct (3D3) = D3D3p′2p2 (E.1)
with the coeﬃcients given by
ˆD1S0 = 4 π
(
D1 + 1
16D2 + 1
4D3− 3D5− 3
16D6− 3
4D7−D11− 1
4D12− 1
4D13− 1
16D14
)
D1S0 = 4 π
( 10
3 D1 + 5
24D2 + 1
6D3 + 2
3D4− 10D5− 5
8D6− 1
2D7− 2D8− 10
3 D11− 1
6D12
− 1
6D13− 5
24D14− 2
3D15
)
D3P0 = 4 π
(
− 4
3D1 + 1
12D2− 4
3D5 + 1
12D6− 2
3D9− 1
6D10 + 8
3D11 + 1
3D12− 1
3D13− 1
6D14
)
D1P1 = 4 π
(
− 4
3D1 + 1
12D2 + 4D5− 1
4D6 + 4
3D11− 1
12D14
)
D3P1 = 4 π
(
− 4
3D1 + 1
12D2− 4
3D5 + 1
12D6− 1
3D9− 1
12D10− 2D11− 1
6D12 + 1
6D13 + 1
8D14
)
ˆD3S1 = 4 π
(
D1 + 1
16D2 + 1
4D3 +D5 + 1
16D6 + 1
4D7 + 1
3D11 + 1
12D12 + 1
12D13 + 1
48D14
)
D3S1 = 4 π
( 10
3 D1 + 5
24D2 + 1
6D3 + 2
3D4 + 10
3 D5 + 5
24D6 + 1
6D7 + 2
3D8 + 10
9 D11 + 1
18D12
+ 1
18D13 + 5
72D14 + 2
9D15
)
D3D1 = 4 π
( 8
15D1 + 1
30D2− 2
15D3− 2
15D4 + 8
15D5 + 1
30D6− 2
15D7− 2
15D8 + 2
5D9− 1
10D10
− 4
9D11 + 1
9D12 + 1
9D13− 1
36D14− 16
45D15
)
ˆD3S1−3D1 = 4 π
(
− 2
√
2
3 D11−
√
2
6 D12−
√
2
6 D13−
√
2
24D14
)
D3S1−3D1 = 4 π
(
− 14
√
2
9 D11 +
√
2
18D12 +
√
2
18D13− 7
√
2
72 D14 + 2
√
2
9 D15
)
D1D2 = 4 π
( 8
15D1 + 1
30D2− 2
15D3− 2
15D4− 8
5D5− 1
10D6 + 2
5D7 + 2
5D8− 8
15D11 + 2
15D12
+ 2
15D13− 1
30D14 + 2
15D15
)
D3D2 = 4 π
( 8
15D1 + 1
30D2− 2
15D3− 2
15D4 + 8
15D5 + 1
30D6− 2
15D7− 2
15D8 + 2
15D9− 1
30D10
+ 4
5D11− 1
5D12− 1
5D13 + 1
20D14 + 4
15D15
)
D3P2 = 4 π
(
− 4
3D1 + 1
12D2− 4
3D5 + 1
12D6 + 1
3D9 + 1
12D10− 2
15D11 + 1
30D12− 1
30D13 + 1
120D14
)
D3P2−3F2 = 4 π
(
4
√
6
15 D11−
√
6
15D12 +
√
6
15D13−
√
6
60D14
)
D3D3 = 4 π
( 8
15D1 + 1
30D2− 2
15D3− 2
15D4 + 8
15D5 + 1
30D6− 2
15D7− 2
15D8− 4
15D9 + 1
15D10− 2
15D15
)
.
(E.2)
84
Table F.1: LECs for two N3LO ﬁts by the Idaho group [68] using Λ = 500 MeV and 600 MeV in the regulator function f(p′,p ),
Eq. (4.63). The CS and CT of the zero-order counterterms given in Eq. (4.38) are in units of 10 4 GeV−2; the Ci, Eq. (4.40),
in 104 GeV−4; and the Di, Eq. (4.43), in 10 4 GeV−6.
LEC Λ = 500 MeV Λ = 600 MeV
Cpp
S -0.009991 -0.009943
Cnn
S -0.010011 -0.009949
Cnp
S -0.010028 -0.009955
Cpp
T 0.000523 0.000695
Cnn
T 0.000543 0.000701
Cnp
T 0.000561 0.000707
C1 0.051949 0.046433
C2 0.163034 0.174354
C3 0.003249 0.006562
C4 -0.048954 -0.050066
C5 -0.075081 -0.086978
C6 -0.013343 -0.013639
C7 -0.225500 -0.214188
D1 -0.016674 -0.004441
D2 2.480231 2.751960
D3 0.915240 0.086650
D4 -0.811591 -0.061000
D5 0.138064 0.126881
D6 1.249801 1.266717
D7 0.148074 0.268796
D8 -0.153405 -0.239967
D9 -0.516607 -0.538043
D10 2.379565 2.429102
D11 -0.125289 -0.132228
D12 0.081807 -0.053835
D13 0.008037 -0.081804
D14 -1.393312 -1.204164
D15 0.164684 -0.005571
Appendix F. Parameters of N 3LO NN potentials
This appendix provides detailed information on parameters involved in the Idaho N 3LO NN poten-
tials [68]. The πN LECs were shown already in Table 2 (column ‘ NN potential’). In Table F.1, the LECs
are listed, which are associated with the contact terms, Eqs. (4.38), (4.40), and (4.43), and, in Table F.2,
the contact LECs are given in terms of partial-wave parameters. Notice that through Eqs. (4.39), (4.42),
and (E.2) there is a one-to-one correspondence between these two representations of the contact LECs. The
partial wave parameters appear one order of magnitude larger, because they are multiplied by (4 π) in the
partial-wave decomposition. The partial-wave contact parameters of the J¨ ulich N 3LO potentials can be
found in Ref. [171]. There are similarities between the parameter sets.
At this point, one may raise the question of the naturalness of the LECs. LECs may be perceived as
natural if they are roughly of the following sizes:
CS,T ∼ 1
f2π
≈ 0.01 104
GeV2 , (F.1)
Ci ∼ 1
f2π Λ2≈ 0.05 104
GeV4 , (F.2)
85
Table F.2: Partial-wave LECs for two N 3LO ﬁts by the Idaho group [68] using Λ = 500 MeV and 600 MeV in the regulator
functionf(p′,p ), Eq. (4.63). The ~Ci of the zero-order partial-wave counterterms given in Eq. (4.39) are in units of 10 4 GeV−2;
the Ci, Eq. (4.41), in 10 4 GeV−4; and the Di, ˆDi, Eq. (E.1), in 10 4 GeV−6. The last column lists the exponent n of the
regulator function, which is applied to the corresponding partial-wave counterterm.
Partial-wave LEC Λ = 500 MeV Λ = 600 MeV n
~Cpp
1S0
-0.145286 -0.151165 3
~Cnn
1S0
-0.146285 -0.151467 3
~Cnp
1S0
-0.147167 -0.151745 3
C1S0 2.380 2.200 2
ˆD1S0 -2.545 -4.890 2
D1S0 -16.00 -5.84 2
C3P0 1.487 1.548 2
D3P0 0.245 -0.215 3
C1P1 0.656 0.790 2
D1P1 5.25 4.40 2
C3P1 -0.630 -0.488 2
D3P1 2.35 3.24 4
~C3S1 -0.118972496 -0.116210 3
C3S1 0.760 0.775 2
ˆD3S1 7.00 4.8004 2
D3S1 6.55 10.8654 2
D3D1 -2.80 -2.35 2
C3S1−3D1 0.826 0.796 2
ˆD3S1−3D1 2.25 2.86 2
D3S1−3D1 6.61 5.58 2
D1D2 -1.770 -1.764 4
D3D2 -1.46 -1.27 2
C3P2 -0.538 -0.548 2
D3P2 2.295 2.554 2
D3P2−3F2 -0.465 -0.525 4
D3D3 5.66 6.26 2, 3 a
a f(p′,p ) = 0.5{exp[−(p′/Λ)4− (p/Λ)4] + exp[−(p′/Λ)6− (p/Λ)6]} is applied.
Di ∼ 1
f2π Λ4≈ 0.2 104
GeV6 , (F.3)
where we used Λ = 0.5 GeV for the numerical estimates. Comparison with Table F.1 reveals that the values
of the contact LECs that result from a ﬁt to the NN data are in general natural, indeed. Exceptions are
D2 and D10 which are an order of magnitude too large.
The charge-dependent LO contact parameters ~Cpp
1S0
, ~Cnn
1S0
, and ~Cnp
1S0
of Table F.2 can be analyzed as
follows. Based upon the isospin-symmetric Lagrangian Eq. (2.61) and the isospin violating ones, Eqs. (4.80)
and (4.81), the charge-dependent non-derivative contact parameters in the 1S0 state are given by
~Cpp = ~Csym + ~CCIB + ~CCSB, (F.4)
~Cnn = ~Csym + ~CCIB− ~CCSB, (F.5)
~Cnp = ~Csym− ~CCIB, (F.6)
where ~Csym is the same as ~C1S0 of Eq. (4.39). The charge-symmetric and the CSB and CIB contributions
86
can then be obtained from
~Csym = 1
2
[1
2
(
~Cpp + ~Cnn
)
+ ~Cnp
]
, (F.7)
~CCSB = 1
2
(
~Cpp− ~Cnn
)
, (F.8)
~CCIB = 1
2
[1
2
(
~Cpp + ~Cnn
)
− ~Cnp
]
. (F.9)
Using the numbers from the Λ = 500 MeV ﬁt listed in Table F.2, the following values are produced:
~Csym = −0.1465 104
GeV2 , (F.10)
~CCSB = 0 .0005 104
GeV2 , (F.11)
~CCIB = 0 .0007 104
GeV2 . (F.12)
Note that these are partial-wave parameters, which carry a factor of (4 π) as compared to the parameters
of, e.g., Eq. (F.1). As discussed in Section 4.6.2, the Idaho N 3LO potential [68] does not include explicitly
the CIB eﬀect from the pion-mass splitting in the NLO 2PE. Thus, the above value for ~CCIB is not the pure
contact contribution since it includes a simulation of this omitted (small) eﬀect (causing ∆ aCIB ≈− 0.5
fm). Moreover, also the CSB eﬀect from nucleon-mass diﬀerence in the NLO 2PE is not calculated explicitly
and, thus, eﬀectively contained in ~CCSB. The exact size of this eﬀect when evaluated in ChPT at NLO is
not known, but could be a large fraction of the total CSB [179].
The regulator function f(p′,p ), Eq. (4.63), has two parameters, namely, the ‘cutoﬀ’ Λ and the power
parametern. Fits were made for Λ = 500 MeV and 600 MeV [denoted by N 3LO(500) and N3LO(600)]. The
parametern has to be chosen such that the higher powers generated by the multiplication with the regulator
[cf. Eq. (4.64)] are beyond the order at which we are working, which is ν = 4. In short, the requirement is
2n +νi > 4, (F.13)
where νi denotes the order of a speciﬁc contribution to the potential. Thus, n≥ 3 for LO contributions,
n≥ 2 for NLO contributions, etc.. In the case of the Idaho N 3LO potentials, n = 4 is used for the 1PE and
n = 2 for all 2PE contributions (which are NLO or higher). For the contact contributions, n is chosen in a
partial-wave dependent way and in accordance with Eq. (F.13), see Table F.2.
Phase shifts ofNN scattering as produced by the Idaho N3LO(500) potential [68] are shown in Tables F.3-
F.6 up to laboratory energies of 300 MeV.
87
Table F.3: pp phase shifts (in degrees) by the Idaho N 3LO(500) potential [68].
Tlab (MeV) 1S0 3P0 3P1 1D2 3P2 3F2 ϵ2 3F3 1G4 3F4
1 32.76 0.13 -0.08 0.00 0.01 0.00 0.00 0.00 0.00 0.00
5 54.71 1.58 -0.90 0.04 0.21 0.00 -0.05 0.00 0.00 0.00
10 55.01 3.73 -2.05 0.17 0.64 0.01 -0.20 -0.03 0.00 0.00
25 48.37 8.57 -4.91 0.70 2.47 0.10 -0.80 -0.23 0.04 0.02
50 38.75 11.47 -8.31 1.70 5.87 0.33 -1.65 -0.69 0.15 0.10
100 25.74 9.30 -13.39 3.68 11.11 0.80 -2.54 -1.48 0.41 0.42
150 16.66 4.34 -17.63 5.28 14.01 1.22 -2.83 -1.96 0.66 0.87
200 8.73 -0.87 -21.48 6.59 15.67 1.56 -2.76 -2.16 0.88 1.37
250 0.51 -5.78 -25.43 7.95 16.85 1.81 -2.35 -2.11 1.05 1.83
300 -8.53 -10.43 -29.54 9.16 17.73 1.94 -1.67 -1.83 1.14 2.17
Table F.4: nn phase shifts (in degrees) by the Idaho N 3LO(500) potential [68].
Tlab (MeV) 1S0 3P0 3P1 1D2 3P2 3F2 ϵ2 3F3 1G4 3F4
1 57.51 0.21 -0.12 0.00 0.02 0.00 0.00 0.00 0.00 0.00
5 60.86 1.85 -1.04 0.05 0.26 0.00 -0.06 -0.01 0.00 0.00
10 57.62 4.10 -2.25 0.18 0.73 0.01 -0.22 -0.04 0.00 0.00
25 48.89 8.92 -5.15 0.73 2.66 0.11 -0.82 -0.24 0.04 0.02
50 38.67 11.60 -8.57 1.76 6.16 0.34 -1.68 -0.71 0.16 0.11
100 25.48 9.16 -13.66 3.75 11.42 0.81 -2.55 -1.50 0.42 0.43
150 16.34 4.08 -17.89 5.33 14.31 1.23 -2.82 -1.98 0.67 0.88
200 8.31 -1.18 -21.69 6.63 15.99 1.58 -2.74 -2.17 0.89 1.39
250 -0.06 -6.11 -25.56 7.97 17.19 1.83 -2.31 -2.11 1.06 1.86
300 -9.24 -10.79 -29.44 9.13 18.07 1.95 -1.63 -1.82 1.15 2.19
Table F.5: I = 1 np phase shifts (in degrees) by the Idaho N 3LO(500) potential [68].
Tlab (MeV) 1S0 3P0 3P1 1D2 3P2 3F2 ϵ2 3F3 1G4 3F4
1 61.95 0.18 -0.11 0.00 0.02 0.00 0.00 0.00 0.00 0.00
5 63.34 1.63 -0.94 0.04 0.25 0.00 -0.05 0.00 0.00 0.00
10 59.55 3.66 -2.06 0.16 0.70 0.01 -0.18 -0.03 0.00 0.00
25 50.28 8.16 -4.86 0.68 2.56 0.09 -0.74 -0.20 0.03 0.02
50 39.82 10.75 -8.25 1.71 5.98 0.30 -1.57 -0.62 0.14 0.09
100 26.51 8.37 -13.35 3.75 11.17 0.75 -2.46 -1.38 0.39 0.39
150 17.35 3.36 -17.58 5.37 14.05 1.15 -2.76 -1.84 0.64 0.84
200 9.29 -1.86 -21.39 6.68 15.72 1.49 -2.70 -2.03 0.87 1.33
250 0.89 -6.76 -25.26 8.04 16.92 1.74 -2.29 -1.98 1.04 1.80
300 -8.31 -11.40 -29.17 9.19 17.81 1.87 -1.63 -1.70 1.14 2.13
88
Table F.6: I = 0 np phase shifts (in degrees) by the Idaho N 3LO(500) potential [68].
Tlab (MeV) 1P1 3S1 3D1 ϵ1 3D2 1F3 3D3 3G3 ϵ3 3G4
1 -0.19 147.76 -0.01 0.11 0.01 0.00 0.00 0.00 0.00 0.00
5 -1.55 118.18 -0.19 0.67 0.22 -0.01 0.00 0.00 0.01 0.00
10 -3.19 102.58 -0.68 1.15 0.85 -0.07 0.00 0.00 0.08 0.01
25 -6.67 80.45 -2.81 1.76 3.72 -0.43 -0.03 -0.05 0.55 0.17
50 -10.03 62.28 -6.41 2.05 8.99 -1.16 0.05 -0.26 1.61 0.72
100 -14.05 42.31 -11.94 2.32 17.56 -2.35 0.89 -0.95 3.50 2.14
150 -17.49 29.79 -15.83 2.67 22.68 -3.22 2.32 -1.77 4.83 3.51
200 -21.43 20.63 -19.01 3.16 24.71 -3.86 3.66 -2.56 5.66 4.62
250 -26.08 13.33 -21.94 3.72 24.29 -4.27 4.51 -3.19 6.02 5.35
300 -31.28 7.24 -24.48 4.02 22.00 -4.41 5.35 -3.53 5.91 5.57
References
[1] H. Yukawa, Proc. Phys. Math. Soc. Japan 17 (1935) 48.
[2] Prog. Theor. Phys. (Kyoto), Supplement 3 (1956).
[3] M. Taketani, S. Machida, and S. Onuma, Prog. Theor. Phys. (Kyoto) 7 (1952) 45.
[4] K. A. Brueckner and K. M. Watson, Phys. Rev. 90 (1953) 699; 92 (1953) 1023.
[5] A. R. Erwin et al., Phys. Rev. Lett. 6 (1961) 628; B. C. Magli´ cet al., ibid. 7 (1961) 178.
[6] Prog. Theor. Phys. (Kyoto), Supplement 39 (1967).
[7] R. A. Bryan and B. L. Scott, Phys. Rev. 135 (1964) B434; 177 (1969) 1435.
[8] K. Erkelenz, Phys. Rep. 13C (1974) 191.
[9] K. Holinde and R. Machleidt, Nucl. Phys. A247 (1975) 495; A256 (1976) 479, 497.
[10] M. M. Nagels, T. A. Rijken, and J. J. de Swart, Phys. Rev. D 17 (1978) 768.
[11] R. Machleidt, Adv. Nucl. Phys. 19 (1989) 189.
[12] V. G. J. Stoks, R. A. M. Klomp, C. P. F. Terheggen, and J. J. de Swart, Phys. Rev. C 49 (1994) 2950.
[13] R. Machleidt, Phys. Rev. C 63 (2001) 024001.
[14] F. Gross and A. Stadler, Phys. Rev. C 78 (2008) 014005.
[15] A. D. Jackson, D. O. Riska, and B. Verwest, Nucl. Phys. A249 (1975) 397.
[16] G. E. Brown and A. D. Jackson, The Nucleon-Nucleon Interaction (North-Holland, Amsterdam, 1976).
[17] R. Vinh Mau, in: Mesons in Nuclei , Vol. I, edited by M. Rho and D. H. Wilkinson (North-Holland, Amsterdam, 1979),
p. 151.
[18] M. Lacombe, B. Loiseau, J. M. Richard, R. Vinh Mau, J. Cˆ ot´ e, P. Pires, and R. de Tourreil, Phys. Rev. C21 (1980) 861.
[19] M. H. Partovi and E. L. Lomon, Phys. Rev. D 2 (1970) 1999; 5 (1972) 1192.
[20] R. Machleidt, K. Holinde, and Ch. Elster, Phys. Rep. 149 (1987) 1.
[21] C. E. de Tar, Nucl. Phys. A335 (1980) 203.
[22] M. Harvey, Nucl. Phys. A352 (1981) 301, 326.
[23] M. Oka and K. Yazaki, Prog. Theor. Phys. 66 (1981) 551, 577.
[24] A. Faessler, F. Fernandez, G. Luebeck, and K. Shimizu, Nucl. Phys. A402 (1983) 555.
[25] A. W. Thomas, Adv. Nucl. Phys. 13 (1983) 1.
[26] F. Myhrer and J. Wroldsen, Rev. Mod. Phys. 60 (1988) 629.
[27] S. Takeuchi, K. Shimizu, and K. Yazaki, Nucl. Phys. A504 (1989) 777.
[28] T. Barnes, S. Capstick, M. D. Kovarik, and E. S. Swanson, Phys. Rev. C 48 (1993) 539.
[29] D. R. Entem, F. Fernandez, and A. Valcarce, Phys. Rev. C 62 (2000) 034002.
[30] G. H. Wu, J. L. Ping, L. J. Teng, F. Wang, and T. Goldman, Nucl. Phys. A673 (2000) 279.
[31] C. Downum, J. Stone, T. Barnes, E. Swanson, and I. Vidana, Nucleon-Nucleon Interactions from the Quark Model ,
arXiv:1001.3320 [nucl-th].
[32] S. Weinberg, Physica 96A (1979) 327.
[33] J. Schwinger, Ann. Phys. (N.Y.) 2 (1957) 407.
[34] M. Gell-Mann and M. Levy, Nuovo Cimento 16 (1960) 705.
[35] T. Ericson and W. Weise, Pions and Nuclei (Clarendon Press, Oxford, 1988).
[36] S. Weinberg, Phys. Rev. Lett. 18 (1967) 188.
[37] S. Weinberg, Phys. Rev. Lett. 17 (1966) 616.
[38] Y. Tomozawa, Nuovo Cimento A 46 (1966) 707.
[39] S. Weinberg, Phys. Rev. 166 (1968) 1568.
[40] S. Coleman, J. Wess, and B. Zumino, Phys. Rev. 177 (1969) 2239; C. G. Callan, S. Coleman, J. Wess, and B. Zumino,
ibid. 177 (1969) 2247.
[41] G. E. Brown, A. M. Green, and W J. Gerace, Nucl. Phys. A115 (1968) 435.
89
[42] G. E. Brown, Comments Nucl. Part. Phys. 4 (1970) 140.
[43] G. E. Brown, in: Mesons in Nuclei , Vol. I, edited by M. Rho and D. H. Wilkinson (North-Holland, Amsterdam, 1979)
p. 330.
[44] J. Fleischer and J. A. Tjon, Phys. Rev. D 21 (1980) 87.
[45] R. Brockmann and R. Machleidt, Phys. Lett. 149B (1984) 283; Phys. Rev. C 42 (1990) 1965.
[46] F. Gross, J. W. van Orden, and K. Holinde, Phys. Rev. C 45 (1992) 2094.
[47] S. Weinberg, Eﬀective Field Theory, Past and Future , arXiv:0908:1964 [hep-th].
[48] J. Gasser and H. Leutwyler, Ann. Phys. 158 (1984) 142; Nucl. Phys. B250 (1985) 465.
[49] J. Gasser, M. E. Sainio, and A. ˇSvarc, Nucl. Phys. B307 (1986) 779.
[50] S. Weinberg, Phys. Lett. B 251 (1990) 288.
[51] S. Weinberg, Nucl. Phys. B363 (1991) 3.
[52] S. Weinberg, Phys. Lett. B 295 (1992) 114.
[53] C. Ord´ o˜ nez, L. Ray, and U. van Kolck, Phys. Rev. Lett.72 (1994) 1982.
[54] C. Ord´ o˜ nez, L. Ray, and U. van Kolck, Phys. Rev. C53 (1996) 2086.
[55] N. Kaiser, R. Brockmann, and W. Weise, Nucl. Phys. A625 (1997) 758.
[56] N. Kaiser, S. Gerstend¨ orfer, and W. Weise, Nucl. Phys. A637 (1998) 395.
[57] N. Kaiser, Phys. Rev. C 61 (2000) 014003.
[58] N. Kaiser, Phys. Rev. C 62 (2000) 024001.
[59] N. Kaiser, Phys. Rev. C 63 (2001) 044010.
[60] N. Kaiser, Phys. Rev. C 64 (2001) 057001.
[61] N. Kaiser, Phys. Rev. C 65 (2002) 017001.
[62] C. A. da Rocha and M. R. Robilotta, Phys. Rev. C 49 (1994) 1818; 52 (1995) 531; M. R. Robilotta, Nucl. Phys. A595
(1995) 171; M. R. Robilotta and C. A. da Rocha, Nucl. Phys. A615 (1997) 391; J.-L. Ballot, C. A. da Rocha, and M. R.
Robilotta, Phys. Rev. C 57 (1998) 1574.
[63] R. Higa and M. R. Robilotta, Phys. Rev. C 68 (2003) 024004.
[64] E. Epelbaum, W. Gl¨ ockle, and U.-G. Meißner, Nucl. Phys. A637 (1998) 107.
[65] E. Epelbaum, W. Gl¨ ockle, and U.-G. Meißner, Nucl. Phys. A671 (2000) 295.
[66] D. R. Entem and R. Machleidt, Phys. Lett. B 524 (2002) 93.
[67] D. R. Entem and R. Machleidt, Phys. Rev. C 66 (2002) 014002.
[68] D. R. Entem and R. Machleidt, Phys. Rev. C 68 (2003) 041001.
[69] R. Machleidt and D. R. Entem, J. Phys. G: Nucl. Phys. 31 (2005) S1235.
[70] U. van Kolck, Phys. Rev. C 49 (1994) 2932.
[71] E. Epelbaum, A. Nogga, W. Gl¨ ockle, H. Kamada, U.-G. Meißner, and H. Witala, Phys. Rev. C 66 (2002) 064001.
[72] S. Ishikawa and M. R. Robilotta, Phys. Rev. C 76 (2007) 014006.
[73] V. Bernard, E. Epelbaum, H. Krebs, and U.-G. Meißner, Phys. Rev. C 77 (2008) 064004.
[74] A. Deltuva and A. C. Fonseca, Phys. Rev. Lett. 98 (2007) 162502; Phys. Rev. C 76, (2007) 021001; arXiv:1005.1308
[nucl-th].
[75] L. Coraggio, A. Covello, A. Gargano, N. Itaco, T. T. S. Kuo, D. R. Entem, and R. Machleidt, Phys. Rev. C 66 (2002)
021303.
[76] L. Coraggio, A. Covello, A. Gargano, N. Itaco, T. T. S. Kuo, and R. Machleidt, Phys. Rev. C 71 (2005) 014307.
[77] L. Coraggio, A. Covello, A. Gargano, and N. Itaco, Phys. Rev. C 81 (2010) 064303.
[78] P. Navr´ atil and E. Caurier, Phys. Rev. C 69 (2004) 014311.
[79] C. Forssen, P. Navratil, W. E. Ormand, and E. Caurier, Phys. Rev. C 71 (2005) 044312.
[80] K. Kowalski, D. J. Dean, M. Hjorth-Jensen, T. Papenbrock, and P. Piecuch, Phys. Rev. Lett. 92 (2004) 132501.
[81] D.J. Dean and M. Hjorth-Jensen, Phys. Rev. C 69 (2004) 054320.
[82] M. Wloch, D. J. Dean, J. R. Gour, M. Hjorth-Jensen, K. Kowalski, T. Papenbrock, and P. Piecuch, Phys. Rev. Lett. 94
(2005) 21250.
[83] D. J. Dean, J. R. Gour, G. Hagen, M. Hjorth-Jensen, K. Kowalski, T. Papenbrock, P. Piecuch, and M. Wloch, Nucl.
Phys. 752 (2005) 299.
[84] J. R. Gour, P. Piecuch, M. Hjorth-Jensen, M. Wloch, D.J. Dean, Phys. Rev. C 74 (2006) 024310.
[85] G. Hagen, T. Papenbrock, D. J. Dean, and M. Hjorth-Jensen, Phys. Rev. Lett. 101 (2008) 092502.
[86] G. Hagen, T. Papenbrock, D. J. Dean, and M. Hjorth-Jensen, Phys. Rev. C 82 (2010) 034330.
[87] S. Fujii, R. Okamoto, and K. Suzuki, Phys. Rev. C 69 (2004) 034328.
[88] S. Fujii, R. Okamoto, and K. Suzuki, Phys. Rev. Lett. 103 (2009) 182501.
[89] K. Ermisch et al., Phys. Rev. C 71 (2005) 064004.
[90] S. Kistryn et al., Phys. Rev. C 72 (2005) 044006.
[91] H. Witala, J. Golak, R. Skibinski, W. Gl¨ ockle, A. Nogga, E. Epelbaum, H. Kamada, A. Kievsky, and M. Viviani, Phys.
Rev. C 73 (2006) 044004.
[92] J. Ley et al., Phys. Rev. C 73 (2006) 064001.
[93] E. Stephan et al., Phys. Rev. C 76 (2007) 057001.
[94] N. Kalantar-Nayestanaki and E. Epelbaum, The three-nucleon system as a laboratory for nuclear physics: the need for
3N forces, Nucl. Phys. News 17 (2007) 22, arXiv:nucl-th/0703089, and references therein.
[95] L. C. Marcucci, A. Kievsky, L. Girlanda, S. Rosati, and M. Viviani, Phys. Rev. C 80 (2009) 034003.
[96] A. Kievsky, M. Viviani, L. Girlanda, and L. E. Marcucci, Phys. Rev. C 81 (2010) 044003.
[97] M. Viviani, L. Giarlanda, A. Kievsky, L. E. Marcucci, and S. Rosati, arXiv:1004.1306 [nucl-th].
90
[98] A. Nogga, P. Navratil, B. R. Barrett, and J. P. Vary, Phys. Rev. C 73 (2006) 064002.
[99] P. Navratil, V. G. Gueorguiev, J. P. Vary, W. E. Ormand, and A. Nogga, Phys. Rev. Lett. 99 (2007) 042501.
[100] G. Hagen, T. Papenbrock, D. J. Dean, A. Schwenk, A. Nogga, M. Wloch, and P. Piecuch, Phys. Rev. C 76 (2007) 034302.
[101] T. Otsuka, T. Susuki, J. D. Holt, A. Schwenk, and Y. Akaishi, Phys. Rev. Lett. 105 (2010) 032501.
[102] S. K. Bogner, A. Schwenk, R. J. Furnstahl, and A. Nogga, Nucl. Phys. A763 (2005) 59; S.K. Bogner, R. J. Furnstahl,
A. Nogga, and A. Schwenk, Nuclear matter from chiral low-momentum interactions , arXiv:0903.3366 [nucl-th].
[103] K. Hebeler and A. Schwenk, Phys. Rev. C 82 (2010) 014314.
[104] R. Machleidt and I. Slaus, J. Phys. G: Nucl. Part. Phys. 27 (2001) R69.
[105] U. van Kolck, Prog. Part. Nucl. Phys. 43 (1999) 337.
[106] P. F. Bedaque and U. van Kolck, Ann. Rev. Nucl. Part. Sci. 52 (2002) 339.
[107] E. Epelbaum, Prog. Part. Nucl. Phys. 57 (2006) 654.
[108] E. Epelbaum, H.-W. Hammer, and U.-G. Meißner, Rev. Mod. Phys. 81 (2009) 1773.
[109] S. R. Beane, P. F. Bedaque, K. Orginos, and M. J. Savage, Phys. Rev. Lett. 97 (2006) 012001.
[110] N Ishii, S. Aoki, and T. Hatsuda, Phys. Rev. Lett. 99 (2007) 022001.
[111] T. Inoue, N. Ishii, S. Aoki, T. Doi, T. Hatsuda, Y. Ikeda, K. Murano, H. Nemura, and K. Sasaki, Baryon-Baryon
Interactions in the Flavor SU (3) Limit from Full QCD Simulations on the Lattice , arXiv:1007.3559 [hep-lat].
[112] A concise and pedagogical introduction into low-energy QCD is contained in: W. Weise, The QCD vacuum and its
hadronic excitations, arXiv:nucl-th/0504087.
[113] S. Scherer, Adv. Nucl. Phys. 27 (2003) 277.
[114] S. Scherer and M. R. Schindler, arXiv:hep-ph/0505265.
[115] K. Nakamura et al. (Particle Data Group), J. Phys. G: Nucl. Part. Phys. 37 (2010) 075021.
[116] J. Goldstone, Nuovo Cim. 19 (1961) 154.
[117] J. Goldstone, A. Salam, and S. Weinberg, Phys. Rev. 127 (1962) 965.
[118] V. Bernard, N. Kaiser, J. Kambor, and U.-G. Meißner, Nucl. Phys. B388 (1992) 315.
[119] V. Bernard, N. Kaiser, and U.-G. Meißner, Int. J. Mod. Phys. E 4 (1995) 193.
[120] E. Jenkins and A. V. Manohar, Phys. Lett. B 255 (1991) 558.
[121] H. Georgi, Phys. Lett B 240 (1990) 447.
[122] N. Fettes, U.-G. Meißner, M. Mojˇ ziˇ s, and S. Steininger, Ann. Phys. (N.Y.)283 (2000) 273; 288 (2001) 249.
[123] N. Fettes, U.-G. Meißner, and S. Steiniger, Nucl. Phys. A640 (1998) 199.
[124] E. Epelbaum, Ph.D. thesis (University of Bochum, 2000), unpublished.
[125] L. Girlanda, S. Pastore, R. Schiavilla, and M. Viviani, Phys. Rev. C 81 (2010) 034005.
[126] J. L. Friar, Few-Body Systems 22 (1997) 161.
[127] S. N. Yang and W. Gl¨ ockle, Phys. Rev. C 33 (1986) 1774.
[128] S. A. Coon and J. L. Friar, Phys. Rev. C 34 (1986) 1060.
[129] E. Epelbaum, U.-G. Meißner, and W. Gl¨ ockle, Nucl. Phys. A714 (2003) 535.
[130] J. Liu al., Phys. Rev. Lett. 105 (2010) 181803.
[131] R. A. Arndt, R. L. Workman, and M. M. Pavan, Phys. Rev. C 49 (1994) 2729.
[132] V. Stoks, R. Timmermans, and J. J. de Swart, Phys. Rev. C 47 (1993) 512.
[133] R. Blankenbecler and R. Sugar, Phys. Rev. 142 (1966) 1051.
[134] K. G. Richardson, Chiral Symmetry and the Nucleon-Nucleon Interaction, Ph.D thesis (University of Manchester, 1999),
arXiv:hep-ph/0008118.
[135] M. C. Birse and J. A. McGovern, Phys. Rev. C 70 (2004) 054002.
[136] R. Higa, arXiv:nucl-th/0411046.
[137] G. Q. Li and R. Machleidt, Phys. Rev. C 58 (1998) 3153.
[138] P. B¨ uttiker and U.-G. Meißner, Nucl. Phys.A668 (2000) 97.
[139] V. G. J. Stoks, R. A. M. Klomp, M. C. M. Rentmeester, and J. J. de Swart, Phys. Rev. C 48 (1993) 792.
[140] R. A. Arndt, I. I. Strakovsky, and R. L. Workman, SAID, Scattering Analysis Interactive Dial-in computer facility, George
Washington University (formerly Virginia Polytechnic Institute), solution SM99 (Summer 1999); for more information
see, e. g., R. A. Arndt, I. I. Strakovsky, and R. L. Workman, Phys. Rev. C 50 (1994) 2731.
[141] In fact, preliminary calculations, which take an important class of diagrams of order ﬁve into account, indicate that the
N4LO contribution may prevailingly be repulsive (N. Kaiser, private communication).
[142] K. Erkelenz, R. Alzetta, and K. Holinde, Nucl. Phys. A176 (1971) 413; note that there is an error in equation (4.22) of
this paper where it should read
−WJ
LS = 2qq′ J− 1
2J− 1
[
AJ−2,(0)
LS −AJ(0)
LS
]
and
+WJ
LS = 2qq′ J + 2
2J + 3
[
AJ+2,(0)
LS −AJ(0)
LS
]
.
[143] E. E. Salpeter and H. A. Bethe, Phys. Rev. 84, 1232 (1951).
[144] R. Machleidt, in: Computational Nuclear Physics 2 – Nuclear Reactions , edited by K. Langanke, J.A. Maruhn, and S.E.
Koonin (Springer, New York, 1993) p. 1.
[145] D. B. Kaplan, M. J. Savage, and M. B. Wise, Nucl. Phys. B478 (1996) 629; Phys. Lett. B 424 (1998) 390; Nucl. Phys.
B534 (1998) 329,
[146] S. Fleming, T. Mehen, and I. W. Stewart, Nucl. Phys. A677 (2000) 313; Phys. Rev. C 61 (2000) 044005.
[147] D. R. Phillips, S. R. Beane, and T. D. Cohen, Ann. Phys. (N.Y.) 263 (1998) 255.
91
[148] T. Frederico, V. S. Timoteo, and L. Tomio, Nucl. Phys. A653 (1999) 209.
[149] M. C. Birse, Phys. Rev. C 74 (2006) 014003; Phys. Rev. C 76 (2007) 034002.
[150] S. R. Beane, P. F. Bedaque, M. J. Savage, and U. van Kolck, Nucl. Phys. A700 (2002) 377.
[151] M. Pavon Valderrama and E. Ruiz Arriola, Phys. Rev. C 72 (2005) 054002.
[152] A. Nogga, R. G. E. Timmermans, and U. van Kolck, Phys. Rev. C 72 (2005) 054006.
[153] M. Pavon Valderrama and E. Ruiz Arriola, Phys. Rev. C 74 (2006) 054001.
[154] M. Pavon Valderrama and E. Ruiz Arriola, Phys. Rev. C 74 (2006) 064004; Erratum: Phys. Rev. C 75 (2007) 059905.
[155] E. Epelbaum and U.-G. Meißner, On the renormalization of the one-pion exchange potential and the consistency of
Weinberg’s power counting, arXiv:nucl-th/0609037.
[156] M. Pavon Valderrama and E. Ruiz Arriola, Ann. Phys. (N.Y.) 323 (2008) 1037.
[157] D. R. Entem, E. Ruiz Arriola, M. Pav´ on Valderrama, and R. Machleidt, Phys. Rev. C 77 (2008) 044006.
[158] C.-J. Yang, Ch. Elster, and D. R. Phillips, Phys. Rev. C 77 (2008) 014002; 80 (2009) 034002, 044002.
[159] B. Long and U. van Kolck, Ann. Phys. (N.Y) 323 (2008) 1304.
[160] S. R. Beane, D. B. Kaplan, and A. Vuorinen, Phys. Rev. C 80 (2009) 011001.
[161] M. Pavon Valderrama, A. Nogga, E. Ruiz Arriola, and D. R. Phillips, Eur. Phys. J. A 36 (2008) 315.
[162] R. Machleidt and D. R. Entem, J. Phys. G: Nucl. Phys. 37 (2010) 064041.
[163] M. P. Valderrama, Phys. Rev. C 83 (2011) 024003.
[164] R. Machleidt, P. Liu, D. R. Entem, and E. Ruiz Arriola, Phys. Rev. C 81 (2010) 024001.
[165] B. H. Brandow, Rev. Mod. Phys. 39 (1967) 771.
[166] B. D. Day, Rev. Mod. Phys. 39 (1967) 719.
[167] H. A. Bethe, Ann. Rev. Nucl. Sci. 21 (1971) 93.
[168] B. D. Day and R. B. Wiringa, Phys. Rev. C 32 (1985) 1057.
[169] E. Epelbaum and J. Gegelia, Eur. Phys. J. A41 (2009) 341.
[170] G. P. Lepage, How to Renormalize the Schr¨ odinger Equation, nucl-th/9706029.
[171] E. Epelbaum, W. Gl¨ ockle, and U.-G. Meißner, Nucl. Phys. A747 (2005) 362.
[172] E. Epelbaum, W. Gl¨ ockle, and U.-G. Meißner, Eur. Phys. J. A19 (2004) 401.
[173] The 1999 NN data base is deﬁned in Ref. [13].
[174] R. B. Wiringa, V. G. J. Stoks, and R. Schiavilla, Phys. Rev. C 51 (1995) 38.
[175] R. Machleidt, F. Sammarruca, and Y. Song, Phys. Rev. C 53 (1996) 1483.
[176] J. R. Bergervoet, P. C. van Campen, W. A. van der Sanden, and J. J. de Swart, Phys. Rev. C 38 (1988) 15.
[177] E. M. Henley and G. A. Miller, in: Mesons in Nuclei , Vol. I, M. Rho and D. H. Wilkinson, eds. (North-Holland,
Amsterdam, 1979) p. 406.
[178] G. A. Miller, M. K. Nefkens, and I. Slaus, Phys. Rep. 194 (1990) 1.
[179] G. Q. Li and R. Machleidt, Phys. Rev. C 58 (1998) 1393.
[180] A. Gardestig, J. Phys. G: Nucl. Part. Phys. 36 (2009) 053001.
[181] D. E. Gonz´ alez Trotteret al., Phys. Rev. C 73 (2006) 034001.
[182] Q. Chen et al., Phys. Rev. C 77 (2008) 054002.
[183] U. L. van Kolck, Soft physics: Applications of eﬀective chiral Lagrangians to nuclear physics and quark models , Ph.D.
thesis (University of Texas, Austin, USA, 1993).
[184] U. van Kolck, Few-Body Systems, Suppl. 9 (1995) 444.
[185] U. van Kolck, J. L. Friar, and T. Goldman, Phys. Lett. B 371 (1996) 169.
[186] E. Epelbaum and U.-G. Meißner, Phys. Rev. C 72 (2005) 044001.
[187] J. Friar and U. van Kolck, Phys. Rev. C 60 (1999) 034006.
[188] M. Walzl, U.-G. Meißner, and E. Epelbaum, Nucl. Phys. A693 (2001) 663.
[189] J. L. Friar, U. van Kolck, G. L. Payne, and S. A. Coon, Phys. Rev. C 68 (2003) 024003; and references to earlier work
therein.
[190] J. L. Friar, U. van Kolck, M. C. M. Rentmeester, and R. G. E. Timmermans, Phys. Rev. C 70 (2004) 044001.
[191] U. van Kolck, M. C. M. Rentmeester, J. L. Friar, T. Goldman, and J. J. de Swart, Phys. Rev. Lett. 80 (1998) 4386.
[192] N. Kaiser, Phys. Rev. C 73 (2006) 044001.
[193] N. Kaiser, Phys. Rev. C 73 (2006) 064003.
[194] N. Kaiser, Phys. Rev. C 74 (2006) 067001.
[195] G. J. M. Austin and J. J. de Swart, Phys. Rev. Lett. 50 (1983) 2039.
[196] W. A. van der Sanden, A. H. Emmen, and J. J. de Swart, Report No. THEF-NYM-83.11, Nijmegen (1983), unpublished;
quoted in Ref. [176].
[197] A. Huber, Th. Udem, B. Gross, J. Reichert, M. Kourogi, K. Pachucki, M. Weitz, and T. W. Hansch, Phys. Rev. Lett.
80 (1998) 468.
[198] W. Gl¨ ockle, H. Witala, D. H¨ uber, H. Kamada, and J. Golak, Phys. Rep.274 (1996) 107.
[199] D. R. Entem, R. Machleidt, and H. Witala, Phys. Rev. C 65 (2002) 064005, and references to earlier work therein.
[200] E. Caurier, P. Navratil, W. E. Ormand, and J. P. Vary, Phys. Rev. C 66 (2002) 024314.
[201] E. Epelbaum, U.-G. Meißner, and J. E. Palomar, Phys. Rev. C 71 (2005) 024001.
[202] J.-I. Fujita and H. Miyazawa, Prog. Theor. Phys. 17 (1957) 360.
[203] S. A. Coon, M. D. Scadron, P. C. McNamee, B. R. Barrett, D. W. E. Blatt. and B. H. J. McKeller, Nucl. Phys. A317
(1979) 242.
[204] H. T. Coelho, T. K. Das, and M. R. Robilotta, Phys. Rev. C 28 (1983) 1812; M. R. Robilotta and H. T. Coelho, Nucl.
Phys. A460 (1986) 645.
92
[205] J. L. Friar, D. H¨ uber, and U. van Kolck, Phys. Rev. C 59 (1999) 53.
[206] S. A. Coon and H. K. Han, Few-Body Syst. 30 (2001) 131.
[207] A. G˚ ardestig and D. R. Philips, Phys. Rev. Lett.96 (2006) 232301.
[208] C. Hanhart, U. van Kolck, and G. A. Miller, Phys. Rev. C 85 (2000) 2905.
[209] D. Gazit, S. Quaglioni, and P. Navr´ atil, Phys. Rev. Lett. 103 (2009) 102502.
[210] S. X. Nakamura, Phys. Rev. C 77 (2008) 054001.
[211] B. M. Fisher, C. R. Brune, H. J. Karwowski, D. S. Leonard, E. J. Ludwig, T. C. Black, M. Viviani, A. Kievsky, and S.
Rosati, Phys. Rev. C 74 (2006) 034001.
[212] M. R. Robilotta, Phys. Rev. C 74 (2006) 044002.
[213] N. Fettes and U.-G. Meißner, Nucl. Phys. A676 (2000) 311.
[214] E. Epelbaum, Eur. Phys. J. A34 (2007) 197.
[215] E. Epelbaum, Phys. Lett. B 639 (2006) 456.
[216] D. Rozpedzik, J. Golak, R. Skibinski, H. Witala, W. Gl¨ ockle, E. Epelbaum, A. Nogga, and H. Kamada, Acta Phys.
Polon. B37 (2006) 2889; arXiv:nucl-th/0606017.
[217] K. Holinde and R. Machleidt, Nucl. Phys. A280 (1977) 429.
[218] T. R. Hemmert, B. R. Holstein, and J. Kambor, J. Phys. G 24 (1998) 1831.
[219] V. Bernard, N. Kaiser, and U.-G. Meißner, Nucl. Phys. A615 (1997) 483.
[220] C. Ord´ o˜ nez and U. van Kolck, Phys. Lett. B291 (1992) 459.
[221] H. Krebs, E. Epelbaum, and U.-G. Meißner, Eur. Phys. J. A32 (2007) 127.
[222] E. Epelbaum, H. Krebs, and U.-G. Meißner, Nucl. Phys. A806 (2008) 65.
[223] N. Fettes and U.-G. Meißner, Nucl. Phys. A679 (2001) 629.
[224] S. C. Pieper, V. R. Pandharipande, R. B. Wiringa, and J. Carlson, Phys. Rev. C 64 (2001) 014001.
[225] S. Weinberg, The Quantum Theory of Fields , Vol. I (Cambridge University Press, Cambridge and New York, 1995).
[226] I. S. Gerstein, R. Jackiw, B. W. Lee, and S. Weinberg, Phys. Rev. D 3 (1971) 2486.
[227] G. ’t Hooft and M. Veltman, Nucl. Phys. B44 (1972) 189.
[228] J. C. Collins, Renormalization (Cambridge University Press, Cambridge, 1984).
[229] F. Mandl and G. Shaw, Quantum Field Theory , Revised Edition (Wiley, New York, 1984).
[230] R. P. Feynman, Phys. Rev. 76 (1949) 769.
[231] G. ’t Hooft, Nucl. Phys. B61 (1973) 455.
[232] M. Abramovitz and I. A. Stegun, Handbook of Mathematical Functions (Dover, New York, 1970).
93
