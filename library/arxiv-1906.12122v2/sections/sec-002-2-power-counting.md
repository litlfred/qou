---
doc_id: arxiv-1906.12122v2
doc_title: "Nuclear eﬀective ﬁeld theory: status and perspectives H.-W. Hammer∗ Institut f¨ ur Kernphysik, Technische Universit¨ at Darmstadt, 64289 Darmstadt, Germany ExtreMe Matter Institute"
section_id: sec-002-2-power-counting
section_title: "Power counting"
section_number: 2
pages: 9-11
source_pdf: 1906.12122v2.pdf
source_sha256: 955e3eda48672e28
doc_brief: "Nuclear effective field theory: status and perspectives H.-W. Hammer∗ Institut für Kernphysik, Technische Universität Darmstadt, 64289 Darmstadt, Germany ExtreMe Matter Institute EMMI — 34 sections: C"
---
form (3) whereMhi is expected to be set by the pion mass
mπ, since pion exchange has been integrated out. In par-
ticular, we want to reproduce the ERE (Bethe, 1949) for
the on-shell NN scattering amplitude:
T (k, cosθ) =− 4π
mN
∑
l
(2l + 1)Pl(cosθ)
k cotδl(k)− ik , (12a)
k2l+1 cotδl(k) =− 1
al
+ rl
2k2 +O(k4), (12b)
with a Legendre polynomial Pl, the scattering angle θ
and energyE =k2/mN in the center-of-mass frame, and
whereδl(k) is the scattering phase shift in thel-th partial
wave, whileal andrl denote the corresponding scattering
length and eﬀective range, respectively. Here, we focus
on S waves with l = 0. Higher partial waves will be
discussed below.
In a “natural” scenario, the LECs C2n in Eq. (11)
would scale with inverse powers of their mass dimension,
e.g.,C0∝M−1
hi . (Note that an overall scaling with 1/mN
from the nonrelativistic framework is shared by all terms
in the eﬀective Lagrangian.) In this case, to lowest or-
derT would simply be given by the tree-level C0 vertex,
and we could identifyC0 = 4πa0/mN. However, the low-
energy NN system is not natural. From the above rela-
tion for C0 it is immediately clear what this means here:
= + + · · ·
Figure 3 Bubble chain for a generic S-wave NN scattering
amplitude at LO from the C0 interaction (solid circle).
the actual NN scattering lengths (a1S0≃− 23.7 fm and
a3S1≃ 5.4 fm) are large compared to the pion Compton
wavelengthm−1
π ≃ 1.4 fm, so C0 = 4πa0/mN is incom-
patible withC0∝M−1
hi if one assumes Mhi∼mπ. Turn-
ing the argument around, the perturbative expansion in
C0 has a breakdown scale set by 1 /a0≪ mπ, rendering
it useful only for the description of extremely low-energy
NN scattering.
The physical reason for the rapid breakdown of the per-
turbative expansion is that the largeNN S-wave scatter-
ing lengths correspond to low-energy (“shallow”) bound
states (virtual, in the case of the 1S0 channel). For exam-
ple, it is well known that the deuteron binding momen-
tum γd =
√
mNBd≃ 45.7 MeV is given to about 30%
accuracy by 1/a3S1. These states directly correspond to
poles of the amplitude T (located on the imaginary axis
of the complex k plane, or on the negative energy axis
in the ﬁrst or second Riemann sheet). It is clear that a
(Taylor) expansion ofT ink2 will only converge up to the
nearest pole in any direction in the complex plane . Thus,
the presence of the shallow NN bound states limits the
range for a perturbative description of NN scattering.
A nonperturbative treatment is necessary to generate
poles in T , since a ﬁnite sum of polynomials can never
have a pole. As pointed out by Weinberg (1991), this can
be achieved by “resumming” the C0 interaction, i.e., by
writing the LO amplitude as the tree-level C0 diagram
plus any number of C0 vertices with intermediate prop-
agation, as shown in Fig. 3 (see also a related analysis
by Luke and Manohar (1997)). The result for a single
generic NN channel is
T (0) =C0 +C0I0(k)C0 +C0I0(k)C0I0(k)C0 +···
=
[
C−1
0 −I0(k)
]−1
, (13)
where I0 is the two-body “bubble integral,” discussed in
more detail below. Having C0 now in the denominator
means that it can be adjusted to give a pole at the desired
position.
2. Power counting
Of course, the power counting of the theory should be
such that it actually mandates this procedure. The small
inverse NN scattering lengths introduce a genuine new
low-momentum scale Mlo (or large length M−1
lo ). Typ-
ically, this is referred to as “ﬁne tuning” because the
existence of this scale—at odds with the perfectly natu-
10
ral assumption that pion exchange should set the lowest
energy scale—implies that diﬀerent contributions from
quarks and gluons have to combine in just the right way
to produce this scenario (see Sec. V.A).
Equation (13) is nothing but Eq. (6) for a two-body po-
tentialC0, which, from the discussion above, is enhanced
by a factor M−1
lo . The loops connecting two insertions
of the potential contain nucleon propagators, which from
Eq. (11) we read oﬀ to be
iDN(p0, p) = i
(
p0− p2
2mN
+··· + iε
)−1
. (14)
Here, p0 and p are the energy and momentum associ-
ated with a nucleon line in Fig. 3. If a total momentum
k∼Q runs through the diagram, we see that, after regu-
larization eﬀects have been removed by renormalization,
the dominant contribution in a loop integral d q0d3q will
come from the region where q∼ Q. Hence, keeping in
mind thatq0 is a nonrelativistic kinetic energy∼q2/mN,
we count
nucleon propagator∼mNQ−2, (15a)
(reducible) loop integral∼ (4πmN)−1Q5. (15b)
Equations (15a) and (15b) lead directly to the esti-
mate (8) and imply that the one-loop contribution in
Fig. 3 scales like the tree-level one times a factor Q/Mlo.
In fact, each additional dressing by one loop with a C0
vertex contributes such a factor. Hence, in the regime
where Q∼Mlo≪Mhi each such diagram is equally im-
portant, and they all have to be summed up to get the
LO amplitude nonperturbatively. On the other hand, for
Q≪ Mlo one can still use a perturbative approach, so
the counting here is able to capture both scenarios.
Operators with derivatives in the eﬀective Lagrangian
must contain inverse powers of Mhi in order not to in-
troduce additional low-energy poles in the LO T matrix.
They provide corrections to the 2N potential,
V2N(p′, p) =C0 +C2
(
p′2 + p2)
+··· . (16)
Being suppressed, higher orders can be calculated in per-
turbation theory and matched to an expansion of Eq.
(12a),
T = 4π
mN
1
1/a0 + ik
(
1 + r0k2/2
1/a0 + ik +···
)
. (17)
The speciﬁc scaling with Mhi can be inferred from this
and from regulator eﬀects considered below.
For example, the NLO amplitude T (1) is the result
from inserting a single C2 vertex into each combination
that can be formed with the LO amplitude (Bedaque
and van Kolck, 1998; van Kolck, 1997; Kaplan et al. ,
1998a,b; Bedaque et al. , 1998; van Kolck, 1999b), as
shown in Fig. 4. Matching to thek2 coeﬃcient in Eq. (17)
Figure 4 NLO correction to the NN scattering amplitude
from the C2 interaction (circled circle).
shows that the C2 contributions are related to the eﬀec-
tive ranges. Since the values of the NN S waves are
r3S1≃ 1.75 fm and r1S0≃ 2.7 fm, and thus of the order
m−1
π ∼M−1
hi , we conclude C2 is indeed an NLO eﬀect,
C2Q2
C0
∼ Q2
MloMhi
. (18)
For comparison, given that the C0 term is a dimension-
6 operator whereas the one with C2 is dimension-8, the
na¨ ıve (natural) scaling isC2Q2/C0 ∼ (Q/Mhi)2. The
additional low-energy enhancement Mlo also occurs in
the scaling of the C2 parameters.
This procedure can be generalized to higher orders and
other operators. At N 2LO we must consider two inser-
tions of C2 and one insertion of C4; the latter is deter-
mined entirely in terms ofr2
0, the shape parameter emerg-
ing at N3LO (Kaplan et al., 1998a,b; van Kolck, 1999b).
Generally, enhancements depend on the partial waves in-
volved. The interactions contributing to such waves are
operators in the “··· ” of Eq. (11) that make T depen-
dent on the scattering angle. There is no enhancement
for operators that contribute only to higher waves, as
long as there are no other low-energy poles as is the case
inNN scattering. Thus, for example, a P -wave operator
leading to a term∝ k′· k appears ﬁrst at N3LO. The en-
hancement is only partial for operators that connect an
S wave to other waves. The short-range tensor force that
connectsS andD waves is present at N2LO because it is
enhanced by one power ofM−1
lo (Chen et al., 1999a). The
lowest orders in the potential are shown schematically in
Fig. 5.
Summarizing, the 2N potential (16) is a particularly
simple form of Eq. (7) where there are no non-analytic
functions and
µ =d/2 (s2 = 2) , µ =d + 1−s2 (s2 = 0, 1), (19)
˜N =O
(
(4π)A−1m−1
N M5−3A
lo
)
, (20)
with A = 2, d the number of derivatives, and s2 = 0, 1, 2
the number of S waves connected by the operator (Be-
daque and van Kolck, 1998; van Kolck, 1997; Kaplan
et al., 1998a,b; Bedaque et al., 1998; van Kolck, 1999b).
Using the standard graph equalities to eliminate the
number of internal linesI and loopsL,I =∑
iVi +L−1
and I = −A +∑
ifiVi/2, where Vi is the number of
11
Figure 5 Diagrams representing the AN nuclear potential in
Pionless EFT. The order of the contributions is indicated as
O(Qµ/Mµ
hi), µ≥ 0, where Q∼ Mlo and Mhi∼ mπ, so that
circles around the central solid circle denotes inverse powers
of Mhi.
vertices with fi nucleon lines, we obtain Eq. (3) for the
amplitude with
ν =
∑
i
Viµi , N =O
(
(4π)A−1m−1
N M5−3A
lo
)
. (21)
Assuming Mlo∼ γd, a rough estimate of the expansion
parameter is Mlo/Mhi∼γd/mπ∼ 1/3.
