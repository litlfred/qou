---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-014-effective-theory-on-the-lattice
section_title: "Effective theory on the lattice"
section_number: null
pages: 27-30
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
As already mentioned, we have to discretize all operators so that they are deﬁned on the lattice and the
explicit form of discretization for any operator will be given explicitly in the subsequent chapters. Here
we want to examine some speciﬁc problems, namely the smearing of nucleon-nucleon contact interactions
and the discretization of the one-pion-exchange potential, which puts the link between lattice spacing,
discretization and the validity of eﬀective ﬁeld theory in a focus. We start with the smearing of the contact
interactions. From an eﬀective ﬁeld theory point of view we can construct only momentum-independent
zero-range interactions at leading order. However, such a contribution leads to a clustering instability and
a strongly overbound 4He state. These eﬀects are reduced by a Gaussian smearing in momentum space
[32]. For example the simplest contact interaction for a two-body system without spin is smeared as
Vint =
∑
⃗n
: a† (⃗n) a(⃗n) a† (⃗n) a(⃗n) :−→
∑
⃗n,⃗n′
f
(
⃗n−⃗n′)
: a† (⃗n) a(⃗n) a† (
⃗n′)
a
(
⃗n′)
:, (3.1)
where : : means normal ordering of the creation and annihilation operators. The smearing function
f (⃗n−⃗n′) is deﬁned as
f
(
⃗n−⃗n′)
= 1
L3 f0
∑
⃗q
exp
−b⃗q 2n
2
 exp
[
i⃗q·
(
⃗n−⃗n′)]
, (3.2)
with normalization constant f0,
f0 = 1
L3
∑
⃗q
exp
−b⃗q 2n
2
. (3.3)
21
Chapter 3 Nuclear Lattice E ﬀective Field Theory
b is a smearing parameter and n is chosen such that the smearing starts contributing atO(q2n), which
is the truncation order of the eﬀective theory. A similar smearing takes place in QCD where it is used
to reduce ﬂuctuations and to improve the signal of correlation functions [2]. Furthermore, it is used in
continuum eﬀective ﬁeld theory to render ultraviolet divergences ﬁnite [22, 53, 74]. The smearing of
the contact interaction via local regulators increases the description of some partial waves, but it may
decrease the prediciton in other channels. The reason is that the antisymmetry argument for the reduction
of possible interaction terms does not hold anymore and as such one must use the local regularization
carefully [75]. E.g., the contact interaction in Eq. (2.17) does not act on P waves due to the antisymmetry
of P waves but a smeared contact interaction according to Eq. (3.1) contributes to the P waves. Hence,
the smearing operators should be implemented such that it only projects on S waves.
Beside the contact interaction, we have also long-range interactions at leading order. Before the modern
formulation of an eﬀective ﬁeld theory, one already assumed the one-pion exchange as a central part of
the theory going back to Yukawa [76]. Obviously, a cutoﬀ is necessary due to the singular structure at the
origin which was diﬃcult to explain before the full understanding of eﬀective ﬁeld theories. An early
work on the one-pion exchange, the cutoﬀ dependence and deuteron observables can be found in [77].
We consider the one-pion-exchange potential in its continuum form,
VOPEP
(⃗q) =− g2
A
4F2
π
⃗σ1·⃗q⃗σ2·⃗q
⃗q2 + M2
π
⃗τ1·⃗τ2. (3.4)
For example, projected on the 1S 0 channel in position space, the potential reads
V
1S 0
OPEP(r) = M2
π
12π
g2
A
4F2
π
(−3)
[exp(−Mπr)
r − 4π
3 δ(⃗r)]
. (3.5)
Here, r =|⃗r| is the radial distance between the two particles. Obviously, such a potential is divergent
at the origin making a regulator necessary. Moreover, the short-range physics should be completely
described by short-range terms and their respective low-energy coupling constants constructed according
to the rules of EFT. A standard smearing in momentum space would produce oscillations in the potential
for very large momenta. These oscillations can be avoided by more complicated momentum space
smearing functions [78] or by using position space regulators. Such a regulator is
flong−range(r) =
1− exp
− r2
R2


n
, (3.6)
where R is a coordinate-cutoﬀ parameter reﬂecting the distinction between short- and long-range physics.
The exponent n should be chosen such that the singularity vanishes and the ﬁts are robust. In Fig. 3.1 we
show a continuum-regularized potential for R = 0.8,..., 1.2 fm and n = 6 in the 1S 0 channel. Such a
scheme regularizes the OPEP to zero in the origin, and hence, the whole interaction is described by the
short-range potential terms. On the lattice we ﬁrstly have an inherent natural hard regulator in momentum
space by the lattice spacing as Λ =π/a which is chosen as a = 1.97 fm, a = 1.32 fm and a = 0.98 fm in
this subsection. Secondly, the discretization scheme itself may serve as a regulator as the momentum can
be discretized in diﬀerent schemes. We show the OPEP for for three diﬀerent schemes. The ﬁrst scheme
uses a very basic discretization using trigonometric functions in momentum space. In the second scheme
we improve it by using a superposition of trigonometric functions whereby in the last scheme we use the
exact momentum on the lattice. For example, the lattice momentum componentν(pl) in the numerator
is discretized as ν(pl) = sin(pl), ν(pl) = 4/3 sin(pl)− 1/6 sin(2pl), and ν(pl) = mod(pl +π, 2π)−π,
22
3.2 The reduced symmetry of SO (3, Z)
respectively. As we see in Fig. 3.1 the continuum result and the continuum-regularized one are both
attractive albeit the latter one vanishes for small lattice spacings. This is in line with eﬀective ﬁeld theory,
where all short-range physics is absorbed in contact interaction terms. All lattice realizations show a very
good agreement for distances larger than 3.5 fm, while the trigonometric ones show a repulsive behavior
between 0 fm and 3 fm. This is partially compensated by some contributions which are very negative, e.g.
at a distance of 2 fm for a lattice spacing of 0.98 fm. The exact discretization results are in a very good
agreement with the continuum calculation. We see of course that for lattice spacings smaller than 1.0 fm,
the exact discretization solution is far oﬀ from the continuum-regularized solution. This means that we
can use the one-pion-exchange potential without extra regulator only in systems with lattice spacings
larger than∼1 fm. Otherwise, the contact interaction contributions become unnaturally large, and may
not be able to compensate the OPE contribution.
−10
−8
−6
−4
−2
0
2
4
0 1 2 3 4 5
V
1S0
OPEP[MeV]
r [fm]
V
1S0
OPEP(r)
V
1S0
OPEP(r)· flong−range(r)
a = 1.97 fm, impr.0a = 1.97 fm, impr.1a = 1.97 fm, exacta = 1.32 fm, impr.0a = 1.32 fm, impr.1a = 1.32 fm, exacta = 0.98 fm, impr.0a = 0.98 fm, impr.1a = 0.98 fm, exact
Figure 3.1: 1S 0 one-pion-exchange potential for various lattice discretization schemes and continuum solutions
with and without position space regularization.
3.2 The reduced symmetry of SO (3, Z)
As argued in Subsec. 2.2.1, the continuum SO(3) symmetry has an inﬁnite number of irreducible
representations and each irreducible representation is identiﬁed with the angular momentumj. This makes
the identiﬁcation straightforward, as each partial wave is directly linked to an irreducible representation
with quantum number j. In fact, this is not possible anymore in a cubic ﬁnite volume. Due to the cubic
symmetry, rotations are only allowed for a discrete and ﬁnite number of values, namely multiplicities of
π/2. E. g., the π/2 rotation around the z-axes is given by the operator,
Rˆz
(π
2
)
= exp
(
−iπ
2 jz
)
. (3.7)
Rotations around the x- and y-axes are deﬁned accordingly with respect to jx, jy. From Eq. (3.7) it is
clear that also the quantum number jz is not a good quantum number anymore, but only jz modulo 4.
23
Chapter 3 Nuclear Lattice E ﬀective Field Theory
The reduced symmetry group is SO(3, Z), which is a ﬁnite group consisting of the representations A1, T1,
E, T2, and A2 [79]. The properties of the representation are summarized in Tab. 3.1.
Rep dimensionality jz Example
A1 1 0 mod 4 Y0,0
T1 3 0,1,3 mod 4 {Y1,1, Y1,0, Y1,−1}
E 2 0,2 mod 4 {Y2,0,
Y2,−2+Y2,2√
2 }
T2 3 1,2,3 mod 4 {Y2,1,
Y2,−2+Y2,2√
2 , Y2,−1}
A2 1 2 mod 4
Y3,2−Y3,−2√
2
Table 3.1: Spherical harmonics for various representations [79].
j irrep
0 A1
1 T1
2 E⊕ T2
3 A2⊕ T1⊕ T2
4 A1⊕ E⊕ T1⊕ T2
5 E⊕ T1⊕ T1⊕ T2
6 A1⊕ A2⊕ E⊕ T1⊕ T2⊕ T2
Table 3.2: Irreducible representations for angular momentum j≤ 6 [79].
The mapping from SO(3) irreducible representations according to their angular momentum j to the
irreducible representations of SO(3, Z) is shown in Tab. 3.2. There is a one-to-one mapping for systems
with angular momenta zero and one. The situation becomes diﬃcult by including higher angular momenta
and as such higher partial waves. Firstly, the partial waves begin to decompose into parts belonging
to diﬀerent representations. Hence, a formalism must be used that puts together the diﬀerent pieces of
diﬀerent representations to restore the rotational invariant state where the angular momentum is a good
quantum number, see for example in [80, 81]. Additionaly, a representation like theT1 exist for j = 1 and
j = 3, linking the coupled channels 3S 1−3 D1 and 3D3−3 G3. Such a mixing is unphysical and should
be removed from the data. This eﬀect has been investigated in Refs. [82, 83] and it is removed by adding
all possible rotational symmetry breaking operators in the theory.
