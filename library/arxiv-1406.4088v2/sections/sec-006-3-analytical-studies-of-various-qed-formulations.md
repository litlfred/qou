---
doc_id: arxiv-1406.4088v2
doc_title: "Ab initio calculation of the neutron-proton mass difference"
section_id: sec-006-3-analytical-studies-of-various-qed-formulations
section_title: "Analytical studies of various QED formulations in finite volume"
section_number: 3
pages: 17-19
source_pdf: 1406.4088v2.pdf
source_sha256: d8f2ff1efb5bea30
toc_source: outline
doc_brief: "Ab initio calculation of the neutron-proton mass difference — 27 sections: Front matter; 1; Outline"
---
Analytical studies of various QED formulations in ﬁnite volume
In this section we derive a number of important results concerning the properties of the pole mass of a charged
particle in various formulations of QED on a ﬁnite spacetime volume. We focus here on point particles, because
the main features are already present in this simpler situation. For the formulation of QED that we use in our
simulations, in Sec. 5 we investigate the modiﬁcations to these calculations which result from the fact that
mesons and baryons have internal structure.
It is important to have a solid analytical handle on QED ﬁnite-volume (FV) corrections, because they are
expected to be large due to the long-range nature of the electromagnetic interaction. Unlike QCD, QED has no
gap and the photon remains massless even in the presence of interactions. While the gap in QCD guarantees
that FV corrections fall off exponentially in LMπ for sufﬁciently large LMπ (42), in the presence of QED,
quantities are much more sensitive to the volume and topology of spacetime. It is the main characteristics of
this sensitivity which concerns us in this section. We use the computed analytical expressions in two important
ways. The ﬁrst is to decide on the ﬁnite-volume formulation of QED to use in our numerical work. The second
is to test our implementation of QED and the corresponding codes.
The work presented in this paper is concerned with spin-1/2 baryons and spin-0 pseudoscalar mesons. Thus
we compute the FV corrections in spinor and scalar QED. Our photon ﬁeld has periodic boundary conditions,
while the quark ﬁelds are periodic in space and antiperiodic in time. Therefore, baryon ﬁelds are antiperiodic
in time and periodic in space, while meson ﬁelds are periodic in all directions. As a result, the topology of
our spacetime is the four-torus, T4, up to a twist for baryons in the time direction. Note that for corrections in
inverse powers of the torus size, only the photon boundary conditions are relevant.
As discussed in Sec. 2.1, we consider two different versions of FV QED:
• the ﬁrst where only the four-momentum zero-mode of the photon ﬁeld is eliminated, i.e. Aµ(k = 0) ≡0,
which we denote QEDTL;
• the second where all three-momentum zero-modes of the photon ﬁeld are eliminated, i.e. Aµ(k0,⃗k =⃗
0) ≡0 for all k0, which we denote QEDL.
Power-like FV corrections arise from the exchange of a photon around the torus. They are obtained by
comparing results obtained in FV with those of our target theory, QED in inﬁnite volume (IV), that is in R4.
Here we are interested in the FV corrections to a charged particle’s pole mass. This is the physical mass of the
particle, as obtained by studying the Euclidean time-dependence of a relevant, zero three-momentum, two-point
correlation function. This mass is gauge invariant and we use this freedom to work in the simpler Feynman
gauge.
The FV corrections to the mass m of a point particle of spin J and of charge q in units of e, on a torus of
dimensions T ×L3, is given by the difference of the FV self energy, ΣJ(p, T, L), and its IV counterpart, ΣJ(p),
on shell:
∆mnJ
J (T, L) ≡mnJ
J (T, L) −mnJ
=
(qe)2∆ΣJ(p = im, T, L)
≡
(qe)2 [ΣJ(p = im, T, L) −ΣJ(p = im)] ,
(S7)
where nJ = 1 (resp. nJ = 2) for spin J = 1/2 fermions (resp. spin J = 0 bosons) and p = im is a shorthand
for p = (im,⃗0) (with /p →im for spin-1/2 fermions). Here and below, quantities without the arguments L and
T are inﬁnite spacetime-volume quantities.
Because we only work in a regime where electromagnetic effects are linear in the ﬁne structure constant α,
we evaluate the self-energy difference in Eq. (S7) at one loop. At this order, we generically write differences
of self energies or of contributions to self energies as
∆Σ(p, T, L) =
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
σ(k, p) ,
(S8)
where k is the momentum of the photon in the loop and σ(k, p) is the appropriate, IV self-energy integrand, a
number of which are deﬁned below. The individual FV and IV terms in Eq. (S8) are generally UV and possibly
IR divergent. Thus, individually they should be regularized, e.g. with dimensional regularization. However,
on shell the IV integral is IR ﬁnite and in ﬁnite volume, the sums are IR ﬁnite because the FV formulations of
QED that we consider are regulated by the space or spacetime volume. Moreover, for large k2, the functions
k3σ(k, p) that arise in Eq. (S8) are strictly monotonic. Therefore, the proof of Cauchy’s integral criterion (43)
guarantees that the difference of the FV sums and IV integrals is also UV ﬁnite. Thus, to compute the FV
corrections at one loop, no explicit regularization is required.
In Eq. (S8), the information about the topology of the ﬁnite volume and the speciﬁc formulation of QED
is contained in the deﬁnition of
PR ′
k. In addition to the case of T4 already discussed, we will also consider
the four-cylinder R × T3. This is a useful intermediate step computationally, because it allows single particle
propagators to develop a pole at the particle’s energy.
For the cases of interest here, we have the following deﬁnitions for
PR ′
k:
• QEDL on R × T3:
′
X
Z
k
≡
Z +∞
−∞
dk0
2π
1
L3
X⃗
k∈BZ3∗
L
,
(S9)
with BZ3∗
L ≡2π
L Z3∗and the star, as usual, indicates the removal of the zero element;
• QEDL on T4:
′
X
Z
k
≡
1
TL3
X
k0∈BZT
X⃗
k∈BZ3∗
L
,
(S10)
with BZT ≡2π
T Z;
• QEDTL on T4:
′
X
Z
k
≡
1
TL3
X
kµ∈BZ4∗
T L
,
(S11)
where BZ4∗
TL ≡[2π
T Z × 2π
L Z3]∗.
The last ingredient of a general nature, needed to study the FV corrections in the three cases of interest, is
the integrand of the self-energy σJ(k, p) for fermions (J = 1/2) and bosons (J = 0). These are obtained from
the usual one-loop spinor and scalar self-energy Feynman diagrams, yielding the following expressions:
σ 1
2(k, p)
=
(2i/p + 4m)σS1(k, p) + 2i/σS2(k, p)
(S12)
σ0(k, p)
=
4σT(k) −σS0(k, p) −4p2σS1(k, p) −4pµσS2,µ(k, p) ,
(S13)
with,
σT(k) =
1
k2 ,
σS0(k, p) =
1
[(p+k)2+m2] ,
σS1(k, p) =
1
k2[(p+k)2+m2] ,
σS2,µ(k, p) =
kµ
k2[(p+k)2+m2] .
(S14)
In the following subsection we provide a brief description of the methods used to obtain the FV corrections
in inverse powers of the volume for the three formulations of FV QED described above. We summarize the
results and discuss their consequences in Sec. 3.2.
