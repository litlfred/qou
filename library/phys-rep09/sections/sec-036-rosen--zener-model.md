---
doc_id: phys-rep09
doc_title: "The Magnus expansion and some of its applications"
section_id: sec-036-rosen--zener-model
section_title: "Rosen--Zener model"
section_number: null
pages: 44-45
source_pdf: phys-rep09.pdf
source_sha256: cd345d3df9358efc
toc_source: outline
doc_brief: "The Magnus expansion and some of its applications — Article history: Accepted 13 November 2008 Available online 25 November 2008 editor: D.L."
---
Following [122] we will deal with the Rosen-Zener model (see Section 4.1.2 and [15]) since it allows a clear illustration
of the adiabatic regime.

The preliminary linear transformation G(s) defined in (94) for the Hamiltonian (202) is given by G(s) = b- o, where the
unit vectorb points in the direction b = atk (k = unit vector along the z-axis). Remember that s = t/T is the dimensionless
time-variable. The evolution operator then gets factorized as

Ug(s) = G'(s)U(8)G(s0), (205)
which, according to (90), satisfies the equation
dUg -
—— = He(s)Uc. (206)
ds

Here Hg = —iHg/h is given by
He(s) ra 2 (207)
= —do3 — 1-02,
G ih 3 2 2
with a? = E2 + V2/ cosh? s and cot @ = (Ep/Vo) coshs.
Next, in analogy to (203), we introduce the Adiabatic Interaction Picture which allows us to integrate the diagonal piece
of H¢(s). The time-evolution operator gets eventually factorized as

foe) 0
Uc(s) = exp (ir7m i] a aon) UL) (s) exp (a/m il a a(s)os) . (208)
0 00
where U2 (s) obeys the equation
du.
z _ Ayu”, (209)
with
AL? (8) = -i(6'/2)[oy sin A(s) + 02 cos A(s)], (210)
and
2T f* 1 2 2
A(s) = +f ds’ a(s’) = 5 in Tey £” arctan oY 5, (211)
h Jo 2 1-p Sa me
We have introduced the definition
p= {1—[1 + (#6 /2y)] sin’ 9)", (212)

in terms of the dimensionless strength parameter y = VoT/h and @. Using the ME to first order in the adiabatic basis
(which coincides with the fixed one at s = +00), one finds the spin-flip approximate (first order) transition probability

00
adp) = sin? Lf do sin ats) . (213)
0
In Fig. 8 we compare the numerical results given by the new approximation (213) with the exact formula P., in (204). For
the sake of illustration, we also plot the results in the usual Interaction Picture to first order in ME (see Pp in (204)). The
gain achieved when using the adiabatic ME in the intermediate regime (i.e., moderate values of ) is of note, although only
the first order is considered. Here, the adiabatic regime corresponds to large values of € = 2ET/h(e = 1/T < 1).
It should also be noted that, for the Hamiltonian (210) one has

se 1 1
i] HQ (si)llods1 = =10(s) — 0(50)| < 520 =
so 2 2
and thus the convergence condition given by Theorem 9 is always satisfied. In other words, for this example the Magnus

expansion is always convergent in the Adiabatic Interaction Picture.
More involved illustrative examples of ME in the Adiabatic Picture may be found in [120,123].
S. Blanes et al. / Physics Reports 470 (2009) 151-238 195

ae

Exact
— O— Magnus-1 (Adiab.)
—4A— T.Pert.-1  (Adiab.)

0.84

1)

% WW — ©@— Magnus-1 (Dirac)
2 oe- \\ —A—TPert-1 (Dirac)
3 A,
2Q
g ‘\
= at
§ 04-4 A
3 ~
5 Wa,

0.24

0.0 : T

0.0 05 1.0 1.6
§

Fig. 8. Rosen-Zener model: Transition probability as a function of €, with y = 1. The solid line stands for the exact result in (204). The remaining lines
stand for first order computations with ME (circles) and perturbation theory (triangles). Open symbols are for the Adiabatic Picture and solid symbols for
the Interaction Picture.
