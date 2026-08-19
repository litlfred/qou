---
doc_id: klein-few-body-systems-in-lattice-effective-field-theory-the
doc_title: "Bonn, November 2018"
section_id: sec-028-introduction
section_title: "Introduction"
section_number: null
pages: 55-57
source_pdf: klein-few-body-systems-in-lattice-effective-field-theory-thesis.pdf
source_sha256: 7ecafdd08255d5c6
doc_brief: "Few-Body Systems in Lattice Effective Field Theory Dissertation Erlangung des Doktorgrades (Dr. rer. nat.) Mathematisch-Naturwissenschaftlichen Fakultät Rheinischen Friedrich-Wilhelms-Universität Bonn"
---
Nuclear Lattice Eﬀective Field Theory (NLEFT) has become a powerful tool in the last years to study the
formation of nuclei from nucleons in an ab initio way. Using this method it was possible to calculate
the binding energies of medium mass nuclei with good accuracy [108, 115] and postdict the Hoyle
state [34, 35], which is an excited state in carbon-12 indispensable for nucleosynthesis in stars. Besides
binding energies, also scattering processes like nucleon-nucleon [61, 116] or alpha-alpha-scattering [36]
were investigated. NLEFT combines two powerful concepts. First, we have chiral nuclear e ﬀective
ﬁeld theory [39, 52], which gives a systematic description of low-energy hadron physics based on
the symmetries (and their breaking) of the underlying gauge ﬁeld theory, Quantum Chromodynamics.
This continuum approach can be combined with well established many-body continuum schemes to go
beyond light nuclei, such as the shell model, the no-core-shell model, coupled cluster theory, variational
Monte Carlo methods, and so on, see e.g. Refs. [117–127]. Second, we discretize Euclidean space
time with spatial lattice spacing a and temporal lattice spacing at, and use Monte Carlo methods for
the numerical evaluation of few- and many-body problems. While many interesting and precise results
could be obtained in this scheme, a problem due to the discretization of space had never been resolved
in a satisfactory fashion. In Ref. [115] an overbinding of the ground state of 4He was observed which
was traced back to the appearance of implicit multi-particle interactions which have signiﬁcant eﬀect on
few-body physics on coarse lattices. In Ref. [128], this eﬀect was demonstrated explicitly for an N-boson
system in two dimensions with short-range interaction. This eﬀect becomes even stronger in larger nuclei.
In Ref. [108] this discretization artefact was cured by adding an eﬀective four-nucleon force (4NF), that,
however, is not related to the chiral expansion. Here, we want to reconsider this issue and prove the
conjecture of the appearance of the implicit multi-particle interactions, and show that with decreasing
lattice spacing their eﬀect is diminished more and more. Consequently, the eﬀective 4NF is not necessary
any more once the lattice spacing is chosen small enough, and one should also conﬁrm the correlation
between 3N and 4N systems, known as the Tjon band [24, 72]. Note that historically, this correlation was
called the Tjon line, but as theory has an inherent uncertainty, it really is a band as stressed in Ref. [72].
While the aforementioned overbinding of 4He on coarse lattices results in correlation points relatively far
oﬀ the Tjon band, the binding energies for triton and helium-4 should get closer to this band or already
be on top of it once the lattice spacing is chosen small enough. Furthermore, note that one also has to
⋆ The following chapter has been published in [114].
49
Chapter 5 The Tjon band in Nuclear Lattice E ﬀective Field Theory
be aware of an additional eﬀect that needs proper treatment. The conﬁgurations with four nucleons on
one lattice site require smearing to prevent a strong overbinding [32]. In the chiral EFT action used for
most investigations, this smearing was adjusted to get the proper neutron-proton eﬀective range. This
procedure might, however, not be suﬃcient in larger systems, as evidenced by the highly successful
non-locally smeared leading order action proposed in Ref. [129].
Diﬀerent to lattice QCD, we do not consider the continuum limit a→ 0. This is related to the fact that
we are dealing with an eﬀective ﬁeld theory (EFT) that is only valid for a certain energy range. In fact,
π/a serves as the ultraviolet cut-oﬀ of this EFT. Letting a tend to zero would generate large momenta that
probe the inner structure of the nucleons, which is outside the realm of the EFT considered. Therefore, a
must be chosen between 1 and 2 fm. This was explained e.g. in Ref. [82].
The EFT provides a counting scheme for the expansion of the eﬀective potential [14] systematically up
to any given orderO(Q/Λ), where Q is a small expansion parameter with respect to the nuclear hard scale
Λ≈ 500 MeV . Note that this hard scale is smaller than the usual chiral perturbation theory scale because
of the non-perturbative nature of the nuclear interactions. For a detailed discussion, see e.g. Ref. [22].
The pertinent small expansion parameter in our case is the nucleon momentum p or the pion mass Mπ or
the electromagnetic charge e∝ Mπ/Λ. Within this counting scheme, the two-body contact interactions
start at leading order (LO),O[(Q/Λ)0], while momentum-dependent and electromagnetic interactions
are at next-to-leading order (NLO),O[(Q/Λ)2] and do not have any additional contribution at N2LO,
O[(Q/Λ)3]. Additional contact terms would arise at N3LO,O[(Q/Λ)4], which is beyond the accuracy of
our calculations in the three- and four-body sector performed here. The two-pion-exchange potential
(TPEP) has contributions at NLO and N2LO. A detailed analysis of the lattice spacing dependence of
the two-body sector can be found in Ref. [116], where higher-order corrections were included both
perturbatively and non-perturbatively. In the following we will include and extend the two-body analysis,
but we will focus on the perturbative approach as we want to be in agreement with former three- and four-
body calculations in which all corrections beyond LO have been included perturbatively. In the three-body
sector, 3NF corrections only start at N2LO as NLO contributions only consist of reducible topologies
which do not produce any non-vanishing contributions. Concerning the 4NF, it was conjectured that they
are not necessary due to the same argument of vanishing contributions for 3NF. However, it was shown
by Ref. [130] that these forces matter at N3LO and a rough estimation of some of their contribution
gives to the binding energy of 4He is about 100 keV [131]. Hence, since they are beyond the order we
include in our analysis and their actual contribution is beyond the accuracy of our work as well, we can
safely neglect them. We remark that these chiral 4NFs are not the eﬀective 4NFs that were included in
Ref. [108].
The chapter is organized as follows. In Sec. 5.2 we introduce the method of NLEFT with an emphasis
on the two-body sector. We calculate phase shifts up to N2LO for neutron-proton scattering, and we
consider electromagnetic corrections for neutron-neutron and proton-proton scattering. Then in Sec. 5.3,
we extend the method to three-body systems and calculate the properties of triton at each order in the
framework of NLEFT. When describing the four-body system in Sec. 5.4, we also give a brief introduction
into Monte Carlo method which is necessary for the calculation of the4He properties. All calculations are
done for lattice spacings of a = 1.97 fm, a = 1.64 fm and a = 1.32 fm, which means that the respective
cutoﬀ Λa =π/a remains below the breakdown scale of the theory. The respective temporal lattice spacing
is chosen as at = 1.32 fm, at = 0.91 fm and at = 0.59 fm, such that the ratio a2/at is kept ﬁxed. Finally,
we investigate the 3H-4He correlation in Sec. 5.5. In Sec. 5.6 we conclude and give an outlook on further
improvements.
50
