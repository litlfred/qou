---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives H.-W. Hammer∗ Institut f¨ ur Kernphysik, Technische Universit¨ at Darmstadt, 64289 Darmstadt, Germany ExtreMe Matter Institute"
section_id: sec-022-2-renormalization-of-singular-potentials
section_title: "Renormalization of singular potentials"
section_number: 2
pages: 48-49
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives H.-W. Hammer∗ Institut für Kernphysik, Technische Universität Darmstadt, 64289 Darmstadt, Germany ExtreMe Matter Institute EMMI — 34 sections: C"
---
The regulator dependence of Weinberg’s prescription
has been understood for a long time. Historically the
ﬁrst observation was that the potential (75) can be solved
semi-analytically in the 1S0 channel: ifp (p′) denotes the
relative incoming (outgoing) momentum in the center-of-
mass frame andk2/mN the energy, the LO amplitude can
be written (Kaplan et al., 1996; Gegelia, 1999b; Eiras and
Soto, 2003; Long and Yang, 2012b)
T (0)(p′,p;k) =TY(p′,p;k) + χ(p′;k)χ(p;k)
C−1
0s (Λ)−I(Λ;k), (78)
where TY is the amplitude for a pure Yukawa potential
and
χ(p;k) = 1 +mN
∫ d3l
(2π)3
TY(l,p;k)
k2−l2 + iϵ, (79)
I(Λ;k) =mN
∫ d3l
(2π)3
χ2(l;k)
k2−l2 + iϵ, (80)
where we keep the regularization implicit. WhenTY = 0,
I(Λ;k) reduces to the I0(Λ;k) of Eq. (22), and Eq. (78)
to Eq. (13). While TY andχ have no non-negative-power
dependence on Λ, I(Λ;k) has two types of inadmissible
cutoﬀ dependence: ∝ Λ and ∝ (m2
π/MNN) ln(Λ/MNN).
The former is the same cutoﬀ dependence one sees in Pi-
onless EFT (Sec. II), and can be absorbed in C0s. The
latter cutoﬀ dependence, which appears despite the fact
that the Yukawa interaction is regular by itself and is for-
mally the same as the logarithmic divergence generated
by the Coulomb interaction (see Sec. II.B.7), comes from
the interference between contact interaction and OPE.
It does not appear in other singlet channels (Eiras and
Soto, 2003; Nogga et al., 2005), but it cannot be absorbed
inC0s, which is the LEC of a chiral-invariant interaction
and thus is not linear in m2
π. Instead, one has to modify
the LO potential (75) by (Kaplan et al., 1996)
C0s→C0s +m2
πD2s =O
( 4π
mNMNN
)
. (81)
Even though NDA estimates D2s = O(C0s/M2
QCD),
renormalization requires D2s =O(C0s/M2
lo). Because of
the diﬀerent transformation properties under chiral sym-
metry, the two operators with LECS C0s and D2s diﬀer
in their pion interactions, see Eq. (70c). Of course, one
cannot see this problem numerically in the 2 N system
unless one varies mπ, which is not done in most nuclear
work, and even then the divergence is only logarithmic.
The additional pion interactions fromD2s should have ef-
fects on other processes, such as pion-nucleus scattering,
but only when there is a signiﬁcant contribution from the
1S0 2N partial wave. Regardless of its phenomenologi-
cal (ir)relevance, this is the simplest example where the
renormalization of observables in Chiral EFT is not guar-
anteed by NDA. This result has been conﬁrmed in many
other studies (Beane et al., 2002; Pav´ on Valderrama and
Ruiz Arriola, 2004, 2006a).
A similar but more dramatic renormalization eﬀect
concerns the momentum dependence of OPE. The ten-
sor potential is singular, behaving at short distances as
−α/rn with n = 3 and, in some channels, α >0. It is
well known (Frank et al., 1971) that such potentials need
to be treated carefully because both solutions of the ra-
dial Schr¨ odinger equation are irregular at r = 0. For
two particles of reduced mass µ, the zero-energy S-wave
radial wavefunction behaves at short distances as 13
ψ(r) =rn/4−1 cos
(√2µαr 1−n/2
n/2− 1 +φn
)
+··· , (82)
where φn is a phase related to the scattering length
and, more generally, the phase shifts. In EFT, the
phase is determined by a contact interaction, the LEC
of which displays an oscillatory dependence on the cut-
oﬀ (Beane et al., 2001a; Bawin and Coon, 2003; Braaten
and Phillips, 2004; Alberg et al. , 2005; Hammer and
Swingle, 2006; Bouaziz and Bawin, 2014; Odell et al. ,
2019), characteristic of a limit cycle or more complicated
attractor. For RG analyses and reviews of limit cycles,
see (Barford and Birse, 2003, 2005; Pav´ on Valderrama
and Ruiz Arriola, 2008), and (Hammer and Platter, 2011;
Bulycheva and Gorsky, 2014), respectively. Without the
13 Particularly interesting is n = 2, which is equivalent (Eﬁmov,
1971) to the three-boson system at unitarity (Sec. II). In this
case√2µαr 1−n/2/(n/2− 1)→
√
2µα− 1/4 ln(r/r0), with r0
an arbitrary dimensionful parameter, and φ2 = φ2(r0). This is
an example of an anomaly (Camblong and Ord´ o˜ nez, 2003, 2005)
where the scale invariance of the classical system is broken by
renormalization to discrete scale invariance.
49
contact interaction, the increasing attraction of the sin-
gular potential leads to the repeated appearance of low-
energy bound states as the momentum cutoﬀ increases.
With the contact interaction, not only the two-, but also
the three-body system is renormalized properly (Odell
et al., 2019), at least for n = 3.
The argument can be generalized to the tensor force
(Beane et al. , 2002; Birse, 2006), which is attractive in
some uncoupled channels and has one attractive eigen-
value in coupled channels. In 3S1-3D1, the C0t interac-
tion in Eq. (75) is suﬃcient to absorb the cutoﬀ depen-
dence and ﬁx the low-energy phase shifts (Fredericoet al.,
1999; Beane et al., 2002; Pav´ on Valderrama and Ruiz Ar-
riola, 2005, 2006a; Yang et al. , 2008), as suggested by
NDA. However, in higher partial waves the eﬀects of C0t
are cutoﬀ artifacts that disappear at large cutoﬀs. As
the cutoﬀ increases, bound states accrue in the higher
partial waves where the tensor OPE is attractive ( 3P0,
3P2-3F2, 3D2, 3D3-3G3, etc.), leading to wild variation in
the corresponding low-energy phase shifts (Nogga et al.,
2005; Pav´ on Valderrama and Ruiz Arriola, 2006b). This
problem can be cured (Nogga et al. , 2005) by a short-
range interaction in each such wave, e.g., including a
termC′
2t(p′·p)Pt in Eq. (75). As primordial counterterm,
C′
2t =O(C0s/M2
QCD) appears only atO(Q2/M2
QCD), and
similarly for the counterterms in other attractive, singu-
lar waves. The absence in Weinberg’s prescription of the
appropriate counterterms explains the need for a “phys-
ical cutoﬀ” Λ phys <∼ 1 GeV, where 3P0 would develop a
bound state (Nogga et al., 2005). In other waves, bound
states cross threshold at higher cutoﬀs. In triplet waves
where OPE is repulsive there is no need for such countert-
erms at LO (Eiras and Soto, 2003; Nogga et al., 2005).
Renormalization problems have been re-
ported (Pav´ on Valderrama and Ruiz Arriola, 2006a,b;
Entem et al. , 2008; Yang et al. , 2009a,b; Zeoli et al. ,
2013) within Weinberg’s prescription also for higher-
order potentials, which are increasingly singular and
attractive in other waves as well. In contrast, a pertur-
bative treatment of more-singular corrections to singular
potentials can be properly renormalized (Long and
van Kolck, 2008) with counterterms containing more
derivatives, as expected from NDA. Renormalization of
chiral potentials seems to demand that at least some
parts of the potential be treated in perturbation theory,
just like in Pionless EFT. 14
14 The simple toy model of a regular long-range potential plus a
short-range interaction that yields a natural two-body scattering
length nicely illustrates how treating the subleading EFT contact
interaction nonperturbatively, similar to the “peratization” of
Fermi theory (Feinberg and Pais, 1963, 1964), prevents a large
cutoﬀ (Epelbaum and Gegelia, 2009).
