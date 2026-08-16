---
doc_id: arxiv-1105.2919v1
doc_title: "Chiral effective field theory and nuclear forces"
section_id: sec-017-43-nn-contact-terms
section_title: "NN contact terms"
section_number: 4.3
pages: 31-32
source_pdf: 1105.2919v1.pdf
source_sha256: 6d94496f2093ddd0
doc_brief: "Chiral effective field theory and nuclear forces — We review how nuclear forces emerge from low-energy QCD via chiral eﬀective ﬁeld theory. The presentation is accessible to the non-specialist."
---
The successful test of the chiral pion-exchange contributions in peripheral partial waves in the previous
section has shown that we got the long- and intermediate-range parts of the nuclear force right. However, for
a “complete” nuclear force, we have to describe correctly all partial waves, including the lower ones. In fact,
in calculations of NN observables at low energies (cross sections, analyzing powers, etc.), the lower partial
waves with L≤ 2 are the most important ones, generating the largest contributions. The same is true for
microscopic nuclear structure calculations. These lower partial waves are dominated by the dynamics at
short distances. Therefore, we need to look now into the short-range part of the NN potential.
In conventional meson theory, the short-range nuclear force is described by the exchange of heavy mesons,
notably the ω(782). Qualitatively, the short-distance behavior of the NN potential is obtained by Fourier
transform of the propagator of a heavy meson,
∫
d3q ei⃗ q·⃗ r
m2ω +⃗ q2 ∼ e−mωr
r . (4.32)
ChPT is an expansion in small momentaQ, too small to resolve structures like aρ(770) orω(782) meson,
because Q≪ Λχ≈mρ,ω. But the latter relation allows us to expand the propagator of a heavy meson into
a power series,
1
m2ω +Q2≈ 1
m2ω
(
1− Q2
m2ω
+ Q4
m4ω
− +...
)
, (4.33)
31
where the ω is representative for any heavy meson of interest. The above expansion suggests that it should
be possible to describe the short distance part of the nuclear force simply in terms of powers ofQ/mω, which
ﬁts in well with our over-all power expansion since Q/mω≈Q/Λχ.
A second purpose of contact terms is renormalization. Dimensional regularization of the loop integrals
that occur in multi-pion exchange diagrams typically generates polynomial terms with coeﬃcients that are,
in part, inﬁnite or scale dependent (cf. Appendix B). Contact terms pick up inﬁnities and remove scale
dependences, which is why they are also known as counter terms.
The partial-wave decomposition of a power Qν has an interesting property. First note that Q can only
be either the momentum transfer between the two interacting nucleons q or the average momentum k [cf.
Eq. (4.8) for their deﬁnitions]. In any case, for even ν,
Qν =fν
2 (cosθ), (4.34)
where fm stands for a polynomial of degree m and θ is the CMS scattering angle. The partial-wave
decomposition of Qν for a state of orbital-angular momentum L involves the integral
I(ν)
L =
∫ +1
−1
QνPL(cosθ)d cosθ =
∫ +1
−1
fν
2 (cosθ)PL(cosθ)d cosθ, (4.35)
where PL is a Legendre polynomial. Due to the orthogonality of the PL,
I(ν)
L = 0 for L> ν
2. (4.36)
Consequently, contact terms of order zero contribute only in S-waves, while order-two terms contribute up
to P -waves, order-four terms up to D-waves, etc..
Due to parity, only even powers ofQ are allowed. Thus, the expansion of the contact potential is formally
given by
Vct =V (0)
ct +V (2)
ct +V (4)
ct +... , (4.37)
where the superscript denotes the power or order.
We will now present, one by one, the various orders of NN contact terms which result from the contact
Lagrangians presented in Section 2.3.
