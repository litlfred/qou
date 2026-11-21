---
doc_id: arxiv-2501.08619v2
doc_title: "Lattice QCD calculation of the Compton amplitude subtraction function"
section_id: sec-006-discretisation-artefacts
section_title: "Discretisation artefacts"
section_number: null
pages: 5-7
source_pdf: 2501.08619v2.pdf
source_sha256: 29ce7af1791830fb
toc_source: outline
doc_brief: "Lattice QCD calculation of the Compton amplitude subtraction function — 16 sections: Front matter; Lattice QCD calculation of the Com; Introduction"
---
converge somewhat slowly.
−3
−2
−1
0
Suu
1 (Q2)
323 × 64, a = 0.074 fm
483 × 96, a = 0.068 fm
483 × 96, a = 0.058 fm
−2
−1
0
Sdd
1 (Q2)
2.5
5.0
7.5
10.0
12.5
15.0
Q2 [GeV2]
−2
−1
0
Sud
1 (Q2)
Figure 3.
The lattice subtraction function as determined
from Feynman-Hellmann. Results are labelled according to
which quark flavour the currents couple to: u for both (top),
d for both (middle), and one on each (bottom).
IV.
DISCRETISATION ARTEFACTS
As with all lattice calculations, it is necessary to take
into account, and correct for, discretisation artefacts
present in the results. The subtraction function, more
so than other quantities, suffers from such artefacts to
a large degree. This is analogous to short-distance arte-
facts studied in the case of the hadronic vacuum polar-
isation [47, 48].
To correct these artefacts, we perform a lattice oper-
ator product expansion (LOPE) of the Compton ampli-
tude for Wilson fermions. This calculation is essentially
a tree-level OPE, where the intermediate quark prop-
6
agators are taken to be Wilson fermions. This section
is inspired by, and builds upon, a previous LOPE by
some of us in 2006 of the lattice Compton amplitude
for the conserved current [49]. In contrast to this prior
result, our current LOPE is specifically for the local
current Vµ = ZV ¯ψγµψ in order to match the Feynman-
Hellmann calculation. Furthermore, we improve on the
2006 result by retaining the bare quark mass.
A succinct outline of the method we use to perform
this LOPE is as follows (see Appendix A for further
details): first, we expand and discretise the forward
Compton amplitude (Tµν →T L
µν), then insert the Wil-
son form of the fermion propagators. Next, we begin
the OPE by performing a Taylor expansion in small
sin(apµ) (the lattice equivalent of apµ in the contin-
uum) and substitute this expansion into the Comp-
ton amplitude (T L
µν →T LOPE
µν
). Unlike the standard
OPE, which uses a hard scale Q2 →∞, we use a soft
scale with sin(apµ) much smaller than the momentum
transfer q. After much simplification, we associate the
sin(apµ) terms with the covariant derivative before con-
cluding by writing the relevant terms as symmetric and
traceless operators.
In our full calculation in Appendix A, we restrict our-
selves to terms up to first order in the covariant deriva-
tive. Then, to isolate the contribution to the subtrac-
tion function, we select the µ = ν = 3 component with
the constraint q3 = 0 and p3 = 0, which follows from
the lattice sink momentum p = 0. Recalling the form of
Eq. (3), this unique selection (with ω = 0, since q4 = 0
and p = 0) ensures that T LOPE
33
is, in fact, the LOPE of
the lattice Compton subtraction function. After remov-
ing all terms present in the continuum, we are finally
left with a ‘correction term’, ∆S1, which quantifies—to
leading order—the discretisation artefact present in our
lattice calculation of the subtraction function. That is,
∆S1 = Sfull
1
−Scont.
1
, where Sfull
1
is the leading order
LOPE result, and Scont.
1
is the leading order continuum
component of the LOPE, leaving only the discretisation
contribution. This result is as follows (see Eq. (A24)):
∆S1 = CW (q, m0)Z2
V ⟨p| ¯ψψ|p⟩,
(16)
where CW (q, m0) is the Wilson coefficient of the form
CW (q, m0) =
2r P
ρ [1 −cos(aqρ)]
P
ρ sin2(aqρ) + a2M 2(q, m0).
(17)
with M(k, m0) = m0+ r
a
P
τ

1−cos(akτ)

and r denot-
ing the scalar Wilson coefficient. This scalar coefficient
is typically set to r = 1 in lattice simulations, but we
keep it explicit in our LOPE expressions in order to keep
track of O(a) terms arising from the Wilson term in the
fermion action. Unlike standard Wilson coefficients, we
also keep the bare quark mass explicit.
The correction term in Eq. (16) is comparable to the
corresponding expression in Ref. [50]. Under the same
0.0
0.1
0.2
0.3
0.4
0.5
am0
−0.4
−0.3
−0.2
−0.1
0.0
−∆S(ﬀ)
1
−∆S(ﬀ)
1
(2006 QCDSF)
SL (ﬀ)
1
(FH)
Figure 4.
Comparison of our 2006 LOPE [49], our lat-
tice OPE, ∆S(ff)
1
, in Eq. (20), and the Feynman-Hellmann
results, SL (ff)
1
.
Results are for free fermions and q =
2π
L (5, 1, 0).
kinematic conditions, the 2006 result [49] (ignoring the
seagull term) is in agreement with Eq (16) in the limit
m0 →0, as anticipated. This expression in Eq. (16) is
also purely unphysical, as Taylor expanding in a yields
terms of order O(a), which vanish in the continuum.
Furthermore, the expression in Eq. (16) is specifically
a Wilson discretisation artefact, ∆S1 ∝r, and thus
there is an additional necessity for the term to vanish
in the continuum [51].
We intend to further investi-
gate the correction in light of clover fermions [50], and
for Ginsparg-Wilson fermions, for which O(a) contri-
butions have already been determined [52]. The matrix
element is given by ⟨p| ¯ψψ|p⟩= 2ampgbare
S
, where gbare
S
is the unrenormalised scalar charge. Since amp ≈0.4
in our calculations, we note that these artefacts will be
relatively large, even at somewhat fine lattice spacings.
Taking our lattice calculations of the subtraction
function, SL
1 (Q2), we can now remove the leading order
discretisation artefact, ∆S1, to produced an improved
result
Simp
1
(Q2) = SL
1 (Q2) + ∆S1.
(18)
Since the O(a) term of our LOPE arises from the
quark propagator connecting the two current insertions
(Type I in Fig. 2), this correction only affects the uu and
dd flavour combinations, but not the ud combination.
This quantitatively explains the behaviour of the results
in Fig. 3, which appears reasonable in the ud case, but
has completely anomalous asymptotes in the uu and dd
plots.
7
10
15
20
25
30
35
(L/2π)2q2
−0.14
−0.12
−0.10
−0.08
−0.06
−0.04
−0.02
0.00
SL (ﬀ)
1
SL (ﬀ)
1
SL (ﬀ)
1
−∆S(ﬀ)
1
(κ = 0.1248)
−∆S(ﬀ)
1
(κ = 0.1239)
−∆S(ﬀ)
1
(κ = 0.1225)
Figure 5. Comparison of the LOPE corection, ∆S(ff)
1
, and
