---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-010-5-finite-volume-effects-for-composite-particles
section_title: "Finite-volume effects for composite particles"
section_number: 5
pages: 24-27
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Finite-volume effects for composite particles
As discussed in Sec. 3, ﬁnite-volume (FV) effects are particularly important, because of the presence of the
massless photon. While in that section we computed these effects for point-like scalar and spinor particles,
here we generalize the discussion to composite particles, which can be hadrons, nuclei, etc. We consider only
the QED formulation that was actually used in our numerical work, namely QEDL on the four-torus T4 of
dimensions T × L3 and use the fact that it differs from QEDL on R × T3 by corrections in T which fall of
faster than any power in 1/T (see Sec. 3).
As shown in Sec. 3 (Eqs. (S22) and (S23)), the leading and next-to-leading FV corrections to the mass of a
point particle of charge qe in scalar and fermion QED are identical at O(α):
m(T, L)
∼
T,L→+∞m

1 −q2α
κ
2mL

1 +
2
mL

+ O
 α
L3

,
(S26)
with κ given in Eq. (S16). Here we show that both corrections remain unchanged for composite particles. This
result follows from the QED Ward-Takahashi identities (WTIs) and from the assumptions that the photon is the
only massless asymptotic state, and that the charged particle considered is stable and non-degenerate in mass
with any other particle which shares its quantum numbers.
3 Since we work in the quenched approximation in this section, the triviality issue is absent. This is because the renormalized
coupling equals the bare coupling and it can be kept ﬁxed for arbitrary small lattice spacings.
While the project described in the present paper was being ﬁnalized, a determination of FV corrections
to the masses of composite particles was presented in (32), up to O (1/L4). In that paper, the authors use
an elegant approach based on heavy-hadron effective ﬁeld theories. Nevertheless, because of the importance
of the inﬁnite-volume (IV) extrapolation in studies involving QED and because the precision of our results
depends critically on knowing the value of the coefﬁcients of the 1/L and 1/L2 corrections, we have chosen to
outline our independent derivation of Eq. (S26) in the present section. Although we work out the corrections
only up to O (1/L2), our approach can be considered more general, as it is based on general ﬁeld theoretical
considerations and not on a speciﬁc effective theory.
Note that Eq. (S26) implies that, to O (1/L2) at least, composite, neutral particles receive no FV corrections.
According to (32), these only appear at O (1/L4) for such particles.
Here we consider a scalar particle of mass m and charge qe. The fermionic case is entirely analogous, but
is technically more involved because of spin. As in the point-particle case, power-like FV corrections to the
mass of composite particles arise from the exchange of a massless photon around the spacetime torus. The
modiﬁcation in the case of composite particles comes from the fact that the photons couple to a state which
has internal structure. The coupling, that enters in the self-energy calculation, is described by the connected
scalar-scalar-photon-photon vertex G(k′; p, k), with the momentum of the outgoing scalar equal to p + k −k′.
At O (α) it can be decomposed as shown in Fig. S5. D(p) is the full, re-summed scalar propagator. Γµ(p, k) is
the one-particle irreducible (1PI) scalar-scalar-photon, three-point vertex function, with the momentum of the
outgoing scalar equal to p + k. ˜Γµν(k′; p, k) is the 1PI scalar-scalar-photon-photon, four-point vertex function,
with the momentum of the outgoing scalar equal to p + k −k′. These functions contain no photon lines and
they are O (α0). They are all inﬁnite-volume, renormalized quantities. They satisfy the following WTIs:
kµΓµ(p, k)/q
=
D−1(p + k) −D−1(p)
(S27)
−kµkν˜Γνµ(k; p, k)/q2
=
D−1(p + k) + D−1(p −k) ,
(S28)
where again q is the charge of the particle in units of e.
The FV corrections to the mass are obtained by taking the difference of the particle’s on-shell self-energy
in ﬁnite and inﬁnite volumes. For a scalar particle at O (α), this yields:
∆m2(T, L) ≡m2(T, L) −m2 = −e2
2


′
X
Z
k
−
Z
d4k
(2π)4

1
k2G(k; p = im, k) =
(S29)
= −e2
2


′
X
Z
k
−
Z
d4k
(2π)4

1
k2{2Γµ(p + k, −k)D(p + k)Γµ(p, k) + ˜Γµµ(k; p, k)}p=im,
where the sum is the one deﬁned by Eq. (S9). Since the contributions to the pole mass are gauge independent,
we work in the simpler Feynman gauge.
In Eq. (S29) an important step has already been taken: the propagator D and the vertices Γµ and ˜Γµν have
been replaced by their IV counterparts. This is because, for the kinetics of the self-energy diagrams these
functions differ only by terms that fall off exponentially with the size of the box. For the propagator of a
stable particle with an inﬂowing energy smaller than that of any possible on-shell, multi-particle state, this was
shown by L¨uscher (42). In the same paper the analiticity of the three-point and four-point 1PI vertex functions
and the associated Feynman-integrands is proven (Theorem 2.3), assuming again, that the inﬂowing energy is
smaller than that of any possible multi-particle states. The FV vertices are obtained by replacing the momentum
integrals, which appear in the loop expansions of their IV counterparts, by momentum sums. The analyticity
proof applies also in FV. Combined with the well known properties of Fourier transforms, this guarantees that
the FV corrections to the vertex functions, computed using Poisson’s formula, fall off faster than any inverse
power of size of the box. The same arguments apply to the 1PI vertices Γµ and ˜Γµν considered here.
No regularization is required in Eq. (S29), because as we now argue, the ultraviolet divergences cancel
in the difference of the sum and the integral. First, if we replaced the momentum sum by the one, which
corresponds to QEDTL, the difference must be ﬁnite. This is because in QEDTL only the single k = 0 mode
is removed from the momentum sums, and these sums deﬁne the integral in the L, T →∞limit. Furthermore
the difference between QEDL and QEDTL one loop self-energies is a one-dimensional integral over k0 with⃗
k = 0, which is ultraviolet convergent in the point-like case, because of the 1/k2
0 suppression from the photon
propagator. Since the form factors, which arise in the vertex functions of composite particles are expected to
suppress ultraviolet modes, this integral will be ultraviolet convergent also for composite particles. From this
reasonable assumption it follows that the difference of the one-loop self-energies in IV QED and QEDL in
Eq. (S29) is free of ultraviolet divergences.
To obtain the desired asymptotic expansion of ∆m2(T, L) in powers of 1/L, we apply the same Poisson
formula as the one used in Eq. (S15). Power-law volume corrections result from infrared singularities in the
integrand. We saw that (p2 + m2)D(p), Γµ(p, k) and ˜Γνµ(k′; p, k) are analytic functions of their arguments in
the domain of integration of Eq. (S29). Thus, the only singularities that can arise are those corresponding to
the poles of the free photon propagator, 1/k2, and of the free scalar propagator, D0(p + k) = 1/(2k·p + k2),
for p2 = −m2. These singularities show up in the limit⃗k →0. It should be noted that there is an additional
source of power-law corrections in Eq. (S29): the subtraction of the⃗k = 0 contribution in the sum over photon
momenta.
Dimensional arguments suggest that corrections up to and including 1/L2 can be obtained by expanding
the numerator of the Γµ · D · Γµ term in Eq. (S29) to O(kµ) and that of the ˜Γµµ term to O(k0
µ). Setting
p2 = −m2, we perform this expansion around the on-shell point k2 = 0 and (p + k)2 + m2 = P·k = 0,
with P ≡2p + k, considering only terms up to the desired order in kµ at the end of the calculation. This
expansion can be performed because these functions are analytic in the domain of integration of Eq. (S29). For
the derivation, it is actually convenient to push the expansion to one order higher in kµ, as it allows to include
the full point-particle contribution. Note that we are expanding here the IV functions, and can therefore use all
of the properties of these functions in inﬁnite volume, including Lorentz covariance.
We begin with the propagator
D(p + k)
=
1
P·k [1 −(P·k)δD(P·k)]−1 ,
(S30)
where δD(P·k) is the full self-energy of the composite scalar at e = 0. It can be expanded as
D(p + k) =
1
P·k + δD(0) + (P·k){δD(0)2 + δD′(0)} + O
 (P·k)2
.
(S31)
The two vertex functions are then decomposed into linear combinations of invariant functions using Lorentz
covariance and the properties of these functions under discrete spacetime symmetry transformations. Substi-
tuting the invariant decompositions into the WTIs of Eqs. (S27) and (S28), expanding the resulting equations
to the desired order in kµ and matching order by order yields:
Γµ(p, k)/q
=
Pµ

F(k2) −δD(0)(P·k) −δD′(0)(P·k)2
−kµF ′(0)(P·k) + O(k3) ,
(S32)
˜Γνµ(k; p, k)/q2
=
−2δµν + 8pµpνδD(0) + O(k) ,
(S33)
where F(k2) is the on-shell electromagnetic form-factor of the scalar. Its ﬁrst derivative gives the electromag-
netic radius ⟨r2⟩= −6F ′(0). Then, replacing the propagator and vertex functions in Eq. (S29) by the above
expansions, one ﬁnds that the terms in δD(0) and δD′(0) cancel and one obtains the point-particle result of
Eq. (S26) plus a ﬁnite term proportional to ⟨r2⟩/L3 and a residual
∆m2
res(T, L) = −


′
X
Z
k
−
Z
d4k
(2π)4


1
m2k2
k2(p·k)f1 + (p·k)3f2/m2
2k·p + k2
+ k2f3 + (p.k)2f4/m2

.
(S34)
In this expression, the dimensionless, nonperturbative functions fi = fi(p·k, k2), i = 1, · · · , 4 must fall off fast
enough as |kµ| →∞for this residual to be ﬁnite. Indeed, as discussed above, ∆m2(T, L) is ﬁnite. Moreover,
the terms already computed in the 1/L expansion are also ﬁnite and by deﬁnition these functions are such that
fi(p·k, k2) −→
kµ→0 constant. Note that we have used crossing symmetry to guarantee that contributions from
˜Γµµ(k; p, k) in the brackets begin at O(k2).
Now, performing the change of variables⃗k = 2π⃗n/L,⃗n ∈Z3, and taking the IV limit, we ﬁnd:
∆m2
res(T, L)
∼
T,L→+∞
1
m2L3
Z dk0
2π
 m g1(k0)
k0 + 2im + g2(k0)

×
" X⃗
n∈Z3∗
−
Z
d3n
#
1 ,
(S35)
where the dimensionless, nonperturbative functions gi(k0), i = 1, 2, are derived from the fj(p·k, k2), j = 1,
· · · , 4, with⃗k = 0. These functions have a ﬁnite limit as k0 →0 and they fall off fast enough at large k0 to
guarantee that the integral over k0 is a ﬁnite number. Moreover, the difference between the sum and integral of
1 over⃗n is −1. Therefore ∆m2
res is O (1/L3).
The spinor case proceeds in an entirely analogous way. The end result is that the ﬁrst two FV corrections
to the mass of a composite particle are identical for spin-0 and 1/2 particles, and are equal to those of point
particles, as given in Eq. (S26). We use this result throughout our numerical analysis of mass splittings.
In addition, in performing the expansions in Eqs. (S32) and (S33), it is clear that the next terms leading to
corrections of order 1/L3 or higher depend on the structure and spin of the particles. This conﬁrms the picture
obtained in (32).
