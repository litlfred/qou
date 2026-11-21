---
doc_id: physrevd111094513
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-006-iv-discretization-artifacts
section_title: "IV. DISCRETIZATION ARTIFACTS"
section_number: null
pages: 5-6
source_pdf: PhysRevD.111.094513.pdf
source_sha256: c05dfaef1f1c2f98
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Lattice QCD calculation of the Com; I. INTRODUCTION; II. BACKGROUND"
---
As with all lattice calculations, it is necessary to take into
account, and correct for, discretization artifacts present in
the results. The subtraction function, more so than other
quantities, suffers from such artifacts to a large degree. This
is analogous to short-distance artifacts studied in the case of
the hadronic vacuum polarization [47,48].
TABLE I.
Lattice parameters and other relevant quantities of the gauge ensembles used in this work [41], including mp [43], ZV [44],
gS [45], and hxi [46].
N3
L × NT
a½fm
β
κl; κs
amp
am0
mπ½MeV
mπL
ZV
gu
S
gd
S
hxiu
hxid
323 × 64
0.074
5.50
0.120900
0.4646(43)
0.00674(7)
470
5.6
0.85
4.26(10)
2.77(7)
…
…
483 × 96
0.068
5.65
0.122005
0.3860(44)
0.00545(15)
410
6.8
0.86
4.83(23)
3.15(14)
0.403(1)
0.173(5)
483 × 96
0.058
5.80
0.122810
0.3552(27)
0.00574(5)
430
6.1
0.88
4.47(28)
2.90(17)
…
…
TABLE II.
Momentum transfers of the external current.
κ ¼ 0.120900
κ ¼ 0.122005
κ ¼ 0.122810
β ¼ 5.50
β ¼ 5.65
β ¼ 5.80
q
Q2
q
Q2
q
Q2
½2π=L
[GeV2]
½2π=L
[GeV2]
½2π=L
[GeV2]
(2,0,0)
1.10
(3,1,0)
1.44
(4,3,0)
4.96
(2,1,0)
1.37
(3,2,0)
1.88
(5,3,0)
6.74
(3,1,0)
2.74
(4,2,0)
2.89
(7,1,0)
9.92
(3,2,0)
3.56
(5,3,0)
4.91
(4,0,0)
4.39
(7,1,0)
7.21
(4,1,0)
4.66
(7,4,0)
9.38
(4,2,0)
5.48
(4,3,0)
6.85
(5,1,0)
7.13
(6,3,0)
12.3
(7,3,0)
15.9
FIG. 3.
The lattice subtraction function as determined from
Feynman-Hellmann. Results are labeled according to which
quark flavor the currents couple to: u for both (top), d for both
(middle), and one on each (bottom).
To correct these artifacts, we perform a lattice operator
product expansion (LOPE) of the Compton amplitude for
Wilson fermions. This calculation is essentially a tree-level
OPE, where the intermediate quark propagators are taken to
be Wilson fermions. This section is inspired by, and builds
upon, a previous LOPE by some of us in 2006 of the lattice
Compton amplitude for the conserved current [49]. In
contrast to this prior result, our current LOPE is specifically
for the local current Vμ ¼ ZV ¯ψγμψ in order to match the
Feynman-Hellmann calculation. Furthermore, we improve
on the 2006 result by retaining the bare quark mass.
A succinct outline of the method we use to perform this
LOPE is as follows (see Appendix A for further details):
first, we expand and discretize the forward Compton
amplitude (Tμν →TLμν), then insert the Wilson form of
the fermion propagators. Next, we begin the OPE by
performing a Taylor expansion in small sinðapμÞ (the
lattice equivalent of apμ in the continuum) and substitute
this expansion into the Compton amplitude (TLμν →TLOPE
μν
).
Unlike the standard OPE, which uses a hard scale Q2 →∞,
we use a soft scale with sinðapμÞ much smaller than the
momentum transfer q. After much simplification, we
associate the sinðapμÞ terms with the covariant derivative
before concluding by writing the relevant terms as sym-
metric and traceless operators.
In our full calculation in the Appendix A, we restrict
ourselves to terms up to first order in the covariant
derivative. Then, to isolate the contribution to the sub-
traction function, we select the μ ¼ ν ¼ 3 component with
the constraint q3 ¼ 0 and p3 ¼ 0, which follows from the
lattice sink momentum p ¼ 0. Recalling the form of
Eq. (3), this unique selection (with ω ¼ 0, since q4 ¼ 0
and p ¼ 0) ensures that TLOPE
33
is, in fact, the LOPE of the
lattice Compton subtraction function. After removing all
terms present in the continuum, we are finally left with a
“correction term,” ΔS1, which quantifies—to leading order
—the discretization artifact present in our lattice calculation
of the subtraction function. That is, ΔS1 ¼ Sfull
1
−Scont
1
,
where Sfull
1
is the leading order LOPE result, and Scont
1
is the
leading order continuum component of the LOPE, leaving
only the discretization contribution. This result is as follows
[see Eq. (A24)]:
ΔS1 ¼ CWðq; m0ÞZ2
Vhpj ¯ψψjpi;
ð16Þ
where CWðq; m0Þ is the Wilson coefficient of the form,
CWðq; m0Þ ¼
2rP
ρ½1 −cosðaqρÞ
P
ρsin2ðaqρÞ þ a2M2ðq; m0Þ ;
ð17Þ
with Mðk; m0Þ ¼ m0 þ r
a
P
τ½1 −cosðakτÞ and r denoting
the scalar Wilson coefficient. This scalar coefficient is
typically set to r ¼ 1 in lattice simulations, but we keep it
explicit in our LOPE expressions in order to keep track of
OðaÞ terms arising from the Wilson term in the fermion
action. Unlike standard Wilson coefficients, we also keep
the bare quark mass explicit.
The correction term in Eq. (16) is comparable to the
corresponding expression in Ref. [50]. Under the same
kinematic conditions, the 2006 result [49] (ignoring the
seagull term) is in agreement with Eq. (16) in the limit
m0 →0, as anticipated. This expression in Eq. (16) is also
purely unphysical, as Taylor expanding in a yields terms of
order OðaÞ, which vanish in the continuum. Furthermore,
the expression in Eq. (16) is specifically a Wilson discre-
tization artifact, ΔS1 ∝r, and thus there is an additional
necessity for the term to vanish in the continuum [51].
We intend to further investigate the correction in light
of clover fermions [50], and for Ginsparg-Wilson fermions,
for which OðaÞ contributions have already been deter-
mined [52]. The matrix element is given by hpj ¯ψψjpi ¼
2ampgbare
S
, where gbare
S
is the unrenormalized scalar charge.
Since amp ≈0.4 in our calculations, we note that these
artifacts will be relatively large, even at somewhat fine
lattice spacings.
Taking our lattice calculations of the subtraction func-
tion, SL
1ðQ2Þ, we can now remove the leading order
discretization artifact, ΔS1, to produced an improved result,
Simp
1 ðQ2Þ ¼ SL
1ðQ2Þ þ ΔS1:
ð18Þ
Since the OðaÞ term of our LOPE arises from the quark
propagator connecting the two current insertions (type I in
Fig. 2), this correction only affects the uu and dd flavor
combinations, but not the ud combination. This quantita-
tively explains the behavior of the results in Fig. 3, which
appears reasonable in the ud case, but has completely
anomalous asymptotes in the uu and dd plots.
