---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Few-body systems in lattice effective field theory"
section_id: sec-024-the-pionless-theory
section_title: "The pionless theory"
section_number: null
pages: 49-51
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-body systems in lattice effective field theory — 58 sections: Introduction and Motivation; The standard model of particle phy; Lattice QCD"
---
93]
EB(L)− E∞
B =−24|A|2 exp
(
−
√
−2µE∞
B L
)
2µL , (4.15)
p cotδ0(p) = 1
πL S (η), η =
( Lp
2π
)2
, (4.16)
with A the normalization constant of the wave function for large distances andµ = mpmn/(mp + mn) the
reduced mass. The energy eigenvalues of the system are linked to the momentum squared byE = p2/(2µ)
and S (η) is the zeta function. Its expansion for smallη is given by
S (η) =−1
η + S 0 + S 1η1 + S 2η2 + S 3η3 +... (4.17)
and the coeﬃcients S i can be found in Chapt. 3.4.1. We do calculations at volumes large enough that
Lüscher’s ﬁnite volume formulas are suﬃcient for inﬁnite volume extraction with negligible residual
ﬁnite volume dependence so we can entirely focus on the remaining dependence on the lattice spacing.
For the scattering state calculations, the ﬁnite volume corrections are of size exp(−L/R), where L is the
box length and R is the range of the interactions [84]. For the bound state calculations, the ﬁnite-volume
formula in Eq. (4.15) captures the leadingexp(−
√
−2µE∞
B L), but there are also smaller corrections of size
exp(−
√
2
√
−2µE∞
B L) [93]. For S-waves, the eﬀective range expansion is p cotδ0(p)≈− 1/as + (re/2)p2
with as the scattering length and re the eﬀective range. Hence, we match our ﬁnite volume results to
the inﬁnite volume eﬀective range parameters and the deuteron binding energy, a 1S 0
=−23.76(1) fm,
r 1S 0
= 2.75(5) fm, and Eb =−2.224575(9) MeV .
In the ﬁts, diﬀerent lattice volumes are used to produce enough data points to make the respective ﬁt
using Eqs. (4.15,4.16) and predict r 3S 1
as well as a 3S 1
. Finally, one can compare the prediction to the
experimental values given by a 3S 1
= 5.424(4) fm and r 3S 1
= 1.759(5) fm. In the following we will repeat
this procedure for lattice spacings between a−1 = 100 MeV and a−1 = 400 MeV , respectively, that is
approximately between 2 fm and 0.5 fm in the pionless theory and for a between 0.3 and 2.0 fm the EFT
with pions.
4.3 The pionless theory
a−1 [MeV] a [fm] C3S 1
[MeV] C1S 0
[MeV] b [MeV−2] a 3S 1
[fm] r 3S 1
[fm]
100 1.97 −46.66 −28.18 3.83· 10−5 5.611(1) 2.029(1)
130 1.52 −50.71 −30.16 3.93· 10−5 5.630(1) 2.047(1)
160 1.23 −50.26 −29.84 4.04· 10−5 5.624(1) 2.034(1)
200 0.99 −49.89 −29.70 4.13· 10−5 5.614(1) 2.017(1)
240 0.82 −50.17 −29.92 4.19· 10−5 5.607(1) 2.008(1)
300 0.66 −50.63 −30.24 4.23· 10−5 5.602(1) 2.005(1)
350 0.56 −50.85 −30.38 4.25· 10−5 5.601(1) 2.008(1)
400 0.49 −50.91 −30.43 4.27· 10−5 5.605(1) 2.015(1)
Table 4.2: Fit results in the Gaussian-smeared pionless EFT case for L = 34, 36, 38 and N = 3.5. The values for
a 3S 1
and r 3S 1
are predictions (modulo the consistency condition Eq. (4.20)).
43
Chapter 4 Regularization Methods for Nuclear Lattice E ﬀective Field Theory
Initially, we consider the pionless case which works well for very low energies and is described by the
eﬀective Hamiltonian
H = Hfree + Hcont. (4.18)
It was shown in Ref. [111] that for any lattice spacing the non-smeared contact interaction cannot
reproduce the eﬀective range correctly. Hence, we introduce a smearing according to Eq. (4.11). The
calculation is performed for N = 0 and N = 3.5 to estimate the inﬂuence of the stretching factor in
the improved action. As we only have to consider the S-wave projection, we use the appropriate linear
combinations
C = 1
4
(
3C1S 0
+ C3S 1
)
CI = 1
4
(
C1S 0
+ C3S 1
)
. (4.19)
The results for two stretching factors N = 0 and N = 3.5 are shown in Fig. 4.1. For N = 3.5, the
explicit values of the ﬁtted parameters and the predictions are listed in Tab. 4.2. The lattice size of
L = 34, 36, 38 is motivated by the corresponding physical lattice length of Lphys = 16.66, 17.64, 18.62 fm
for a minimal lattice spacing of a = 0.49 fm. This should be still large enough so that higher order terms
to Eqs. (4.15,4.16) and in the eﬀective range expansion are negligible. The LECs in the respective table
and plot are obtained after rescaling C3S 1/1S 0
→ C3S 1/1S 0
/a3 so as to account for the diﬀerent volumes.
−54
−52
−50
−48
−46
−44
−33
−32
−31
−30
−29
−28
3.6
3.8
4
4.2
4.4
4.6
4.8
5
0 0 .5 1 1 .5 2
C3S1[MeV]C1S0[MeV]b[MeV−2]
a [fm]
L=34,36,38; N=3.5L=34,36,38; N=0.0
Figure 4.1: Low-energy coupling constants and the smearing parameter b in the pionless EFT for a lattice size of
L = 34, 36, 38 and two diﬀerent stretching factors.
First, we see the parameters belonging to N = 0 and N = 3.5 have similar values and they approach a
constant value when the lattice spacing is minimized. But there is a preference for N = 3.5 case because
for this case, the variation of the LECs is signiﬁcantly decreased for various lattice spacings than in the
44
