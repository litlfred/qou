---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-008-32-results-for-finite-volume-corrections-to-the
section_title: "Results for finite-volume corrections to the pole mass and consequences for the various QED formulations"
section_number: 3.2
pages: 21-23
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Results for ﬁnite-volume corrections to the pole mass and consequences for the
various QED formulations
In this subsection we combine the results of the previous subsection to obtain the FV corrections to the pole
masses of point spinor and scalar particles for two versions of FV QED of interest for lattice calculations:
• QEDL on T4, which is the formulation used in the present study;
• QEDTL on T4, which is the formulation used in previous lattice studies of isospin breaking effects.
While some of the details of the results obtained in this section are speciﬁc to point particles, the general
conclusions also carry over to the case of composite particles, which is discussed in Sec. 5.
Finite-volume corrections in QEDL on T4
QEDL on T4 is the formulation used in the present study of isospin breaking effects. Combining the results of
Eqs. (S15) and (S19) and putting everything together, we ﬁnd that the mass of a point-like fermion of spin 1/2,
of charge q in units of e, on the four-torus T4 of dimensions T × L3 in QEDL, is at one-loop, in terms of its
inﬁnite-volume mass m:
m 1
2(T, L)
∼
T,L→+∞m

1 −q2α

κ
2mL

1 +
2
mL

−
3π
(mL)3

,
(S22)
up to terms which are exponentially suppressed in mL and terms which fall faster than any power in 1/(mT),
with κ given in Eq. (S16). Similarly, the FV corrections to the mass of a point-like boson of spin 0 are, in terms
of its inﬁnite-volume mass m:
m2
0(T, L)
∼
T,L→+∞m2

1 −q2α
 κ
mL

1 +
2
mL

.
(S23)
Four important comments are in order. The ﬁrst is that the ﬁnite-volume pole masses in both cases have
a well deﬁned T, L →∞limit and converge onto their inﬁnite-volume counterparts. The second is that the
coefﬁcient of the leading 1/L and 1/L2 corrections to the mass m of a particle of charge qe is the same for
spin-1/2 fermions and spin-0 bosons at O(α). In Sec. 5 we show that these coefﬁcients are always the same,
independent of the spin and point-like nature of the particle: they are ﬁxed by QED Ward-Takahashi identities.
Moreover, as suggested in (38) and worked out explicitly in (32), the leading 1/L term is the FV correction
to the classical, electrostatic potential of a point charge on T3, with the spatial zero-modes removed from
Gauss’ law. The third comment is that the dimensionless, relative FV corrections must be functions of the only
dimensionless parameter, mL, in the two theories considered. This will no longer be the case when we consider
physical mesons and baryons, as these particles are not point-like and therefore have relevant scales other than
their mass. The ﬁnal remark is that we ﬁnd a coefﬁcient for the 1/(mL)3 term in Eq. (S22) which is twice the
one found in (32), when the result for composite fermions in that paper is reduced to the point-like case. As
shown in Sec. 4, this factor of 2 is conﬁrmed by direct simulation of QEDL on T4.
Finite-volume corrections in QEDTL on T4
The setup considered in this section, QEDTL on the four-torus T4 of dimensions L3 × T, is the one used in all
previous studies which include QED corrections to hadronic observables in lattice QCD (7,8,10–13,35,38,45).
As discussed in Sec. 2.1, it violates reﬂection positivity. Here we show that it has another problem: it does not
have a well deﬁned T →∞limit for ﬁxed L. It is these reasons which have led us to choose to simulate QEDL
instead of QEDTL for the precision computation presented in the present paper.
The ﬁnite-volume corrections to the masses of point particles in QEDTL on T4 are obtained by adding, to
those in QEDL on T4 (Eqs. (S22) and (S23)), the corrections on the self-energy components determined in
Eq. (S21). This yields the following result for the mass of a spin J = 1/2 point-particle, of charge q in units of
e, in QEDTL on the four-torus of dimensions T × L3, in terms of its inﬁnite-volume counterpart, m:
m 1
2(T, L)
∼
T,L→+∞
m

1 −q2α

κ
2mL

1 +
2
mL

1 −π
2κ
T
L

−
3π
(mL)3

1 −coth(mT)
2

−
3π
2(mL)4
L
T

,
(S24)
up to terms which are exponentially suppressed in mL and terms which fall faster than any power in 1/(mT),
with κ given in Eq. (S16). Similarly, the FV corrections to a point-like boson of spin 0 are, in terms of the
inﬁnite-volume mass m:
m2
0(T, L)
∼
T,L→+∞
m2

1 −q2α
 κ
mL

1 +
2
mL

1 −π
2κ
T
L

.
(S25)
A number of important remarks about these results deserve to be made. We begin by considering T/L as
being O(1), as it is usually in lattice simulations. The ﬁrst remark is that the leading 1/L and 1/L2 contribution
are identical for both spins, as was the case in QEDL. However, only the 1/L terms here are equal with those
found in QEDL. The reinstatement of the spatially-uniform photon modes for k0̸ = 0 reduces the coefﬁcient
of the subleading 1/L2 contributions for T ∼L, compared to what it is in QEDL.
It should also be noted that both masses acquire new T-dependent, 1/L3 and 1/L4 contributions, which
remain under control even when T ≫L. And, as in the case of QEDL, the dimensionless, relative, FV mass
corrections of Eqs. (S24) and (S25) can be written in terms only of dimensionless quantities. However, while
in QEDL there is only one dimensionless variable, mL, here there is another, the aspect ratio of T4, ξ = T/L.
This will no longer be the case when we consider physical mesons and baryons, as these particles are not
point-like and therefore have relevant scales other than their mass.
The problem in QEDTL on the four-torus arises if one considers the limit T →∞for ﬁxed L. In that case
the 1/L2 corrections blow up linearly in T/L. In particular, this means that the conventional mass extraction
procedure, which relies on examining the asymptotic time behavior of Euclidean propagators, is not well-
deﬁned at ﬁnite L. This justiﬁes, for the precision study presented in this paper, our choice of working with
QEDL instead of QEDTL that was used in previous studies. It should be noted, however, that this problem only
arises at O(1/L2) and remains mild for typical T/L used in lattice computations. Thus, for lower precision
studies with T/L ∼1 such as in (10), where no sensitivity to terms of higher order than a ﬁtted 1/L was found,
the effect of using QEDTL will not signiﬁcantly distort results.
