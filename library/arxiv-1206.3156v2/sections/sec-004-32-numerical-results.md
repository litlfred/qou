---
doc_id: arxiv-1206.3156v2
doc_title: "Isospin breaking in octet baryon mass splittings"
section_id: sec-004-32-numerical-results
section_title: "Numerical results"
section_number: 3.2
pages: 9-11
source_pdf: 1206.3156v2.pdf
source_sha256: 384b83fa69f21305
toc_source: outline
doc_brief: "Isospin breaking in octet baryon mass splittings — Using an SU(3) ﬂavour symmetry breaking expansion in the quark mass, we determine the QCD component of the nucleon, Sigma and Xi mass splittings of"
---
Numerical results
Simulations have been performed using Nf = 2+1 O(a) improved clover fermions
[19] at β = 5.50 and on 323 × 64 lattice sizes, as described in more detail in
[13]. Errors given here are statistical (using ∼O(1500) conﬁgurations); possible
systematic errors are discussed in Appendix A and incorporated into the ﬁnal
results in section 7.
A particular starting value for the degenerate sea quark mass, m0, is chosen
on the SU(3) ﬂavour symmetric line, and the subsequent sea quark mass points
ml, ms have then been arranged in the various simulations to have constant m
(= m0). This ensures that the expansion coeﬃcients do not change. It was found
in [13] that a linear ﬁt provides a good description of the numerical data over
the relatively short distance from the symmetric point down to the physical pion
mass. This helped us in choosing the initial point on the SU(3) ﬂavour symmetric
line to give a path that hits (or is very close to) the physical point.
In a little more detail, the bare quark masses in lattice units are deﬁned as
mq = 1
2
 1
κq
−
1
κ0;c

with
q ∈{l, s, 0} ,
(25)
(together with eq. (5) for δmq) with the index q = 0 denoting the common mass
degenerate quarks along the SU(3) ﬂavour symmetric line, and where vanishing
of the quark mass along this line determines κ0;c. Keeping m = constant ≡m0
gives
κs =
1
3
κ0 −2
κl
.
(26)
So once we decide on a κl this then determines κs. Note that κ0;c drops out of
eq. (26), so we do not need its explicit value. The initial SU(3) ﬂavour symmetric
κ0 value chosen here, namely κ0 = 0.12090, [13] is very close to a point on the
path that leads to the physical point. The constancy of ﬂavour singlet quantities
over the range from the SU(3) ﬂavour symmetric line down to the physical point
[13], leads directly from Xπ to an estimate for the pion mass of ∼411 MeV (i.e.
eq. (47)) and similarly from XN a value of the lattice spacing of a ∼0.079 fm.
While, as discussed earlier, simulations between the SU(3) ﬂavour symmetric
point and the physical point are in principle enough to determine the linear and
quadratic expansion coeﬃcients, in practice the range is not suﬃciently large
to reliably determine the quadratic terms. In order to determine the quadratic
coeﬃcients more precisely, additional PQ simulations have been performed on the
set of gauge conﬁgurations that have all three sea quark masses equal, i.e. at the
SU(3) ﬂavour symmetric point κ0 = 0.12090. For these particular simulations
δml = 0 = δms automatically.
µq is deﬁned identically to mq, eq (25), by
replacing mq →µq with q ∈{a, b, . . . , } together with eq. (19) for δµq so that
δµq = µq −m ,
µq = 1
2
 1
κq
−
1
κ0;c

.
(27)
We have chosen a wide range of PQ masses starting from a slightly heavier mass
than m0 (to avoid any possibility of so-called ‘exceptional conﬁgurations’) and
reaching up to masses ∼mcharm. The values are given in Appendix B in Table 4.
A direct ﬁt is made to these PQ masses, the unitary masses of [13], which all
have the same ﬁxed m, and additionally three PQ masses, which we call MNs ≡
M(sss) again with the same ﬁxed m. (This is analogous to the pseudoscalar ηs
considered later.) These values are also given in Appendix B in Table 5. Using
the ﬁt function of eq. (20) and ignoring the ˜C1 and ˜C2 terms as discussed in
section 3.1 gives the results in Table 1, together with the NNLO coeﬃcient values
˜A1
˜A2
˜B1
˜B2
˜B3
10.15(12)
1.828(157)
13.51(126)
-10.29(139)
-14.90(144)
Table 1: Results for the baryon octet expansion coeﬃcients.
of ˜C3 = −4.60(115), ˜C4 = −17.5(26), ˜C5 = −1.88(310) and ˜C6 = −3.65(184).
We note that in comparison to the NLO coeﬃcients, the NNLO coeﬃcients are
poorly determined. The bootstrap (MINUIT) ﬁt used gave χ2/dof ∼0.4.
We now compare these results to a plot for illustration.
The simplest to
consider is setting δµa = δµb, i.e. degenerate valence quark masses. For simplicity,
but slightly inaccurately, we shall in the following simply say b = a. (Of course
we still need two diﬀerent quark ﬂavours.) With δml = 0, eq. (23) then becomes
˜
M2(aaa) −1
3δµa
=
˜A1 + ˜B1δµa + 8
3 ˜C3δµ2
a .
(28)
In Fig. 3 we plot ( ˜
M2(aaa) −1)/(3δµa) against δµa for the PQ data (together
with the cubic ﬁt coeﬃcients from Table 1) which due to the denominator is a
sensitive plot. There is good agreement. (We postpone the comparison to the
unitary data, ‘fan’ plots, until section 6.)
