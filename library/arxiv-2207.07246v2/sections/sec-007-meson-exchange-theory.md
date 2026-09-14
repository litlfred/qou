---
doc_id: arxiv-2207.07246v2
doc_title: "Path Integral Quantum Monte Carlo Method for Light Nuclei"
section_id: sec-007-meson-exchange-theory
section_title: "Meson exchange theory"
section_number: null
pages: 12-15
source_pdf: 2207.07246v2.pdf
source_sha256: 91e70e5fe39e07a5
doc_brief: "Path Integral Quantum Monte Carlo Method for Light Nuclei — 58 sections: Front matter; ABSTRACT; LIST OF TABLES"
---
The earliest version of nucleon-nucleon (NN) interaction is the Yukawa potential
(Yukawa (1935)) which isVYukawa(r) =−g2 e−mr
r where g is the coupling constant, m
2
is the mass of the meson and r is the distance between two nucleons. Yukawa theory
was pioneering in the 1930s because it ﬁrst predicted that the interactions between
nucleons are made by exchanging a new particle called a meson. The interaction range
r between nucleons, which is about 1 fm, can determine the mass of the meson by the
uncertainty principler≈ 1/m so m≈ 200 MeV. And such a meson called the pion
with mass about 140 MeV was discovered in 1947 (Lattes et al. (1947)). Since then,
nuclear and high energy physics has entered a golden age, and there was time where a
discovery of a new particle meant a Nobel Prize.
Over the decades, we have more understanding of what the interaction between
nucleons looks like. We at least know that the interactions between nucleons should
have momentum dependence. The simplest interaction with momentum dependence
is the spin-orbit interaction which is nonlocal, and in fact a realistic nucleon-nucleon
interaction cannot be built without it. Also, there are not only two-nucleon forces
(2NF), but also three-nucleon forces (3NF), and even four-nucleon forces (4NF), and
even more. Since the 1990s, several high-precision NN interactions (Machleidt and
Slaus (2001)) mostly based on meson exchange theory have been developed. Among
them, the Nijmegen potentials (Stoks et al. (1994)), the CD-Bonn potential (Machleidt
et al. (1996)), the Argonne series (Wiringa et al. (1995); Wiringa and Pieper (2002);
Veerasamy and Polyzou (2011)) of interactions together with Tucson-Melbourne (Coon
and Gl ¨ockle (1981)) and Urbana and the modern Illinois series of 3NF (Carlson
et al. (1983); Wiringa and Pieper (2002)) are widely used. These meson-exchange
based models have achieved great success in explaining the experimental data. In
these potentials, the 2NF includes one-pion exchange (OPE) as well as heavier meson
exchange and the 3NF contains terms from two and/or more pion exchange. However,
the parameters in the 3NF models need be adjusted for the chosen 2NF model to
ﬁt the binding energy for A≥ 3 nuclei (Nogga et al. (2000)). This situation raises a
3
simple question, how do we choose the 2NF and 3NF? Apparently these models are
lacking a fundamental theory which can guide us to ﬁnd or choose the form of 2NF
and 3NF within a consistent framework. From today’s point of view, we know that
those models are lacking the guidance of the (broken) symmetry from QCD, the chiral
symmetry.
Chiral eﬀective ﬁeld theory
Since the 1990s, the importance of NN interactions derived from chiral eﬀective ﬁeld
theory (ChEFT) has been realized by more and more people. The idea of ChEFT was
proposed in 1979 by Steven Weinberg (Weinberg (1979)) and after his proposal about
how to treat the nuclear interaction at the chiral limit (Weinberg (1990, 1991)) ChEFT
has been rapidly developed in nuclear physics (Epelbaum et al. (2009); Machleidt and
Entem (2011)). The nuclear interactions derived from ChEFT are connected with the
fundamental theory of QCD by the broken chiral symmetry. This is an example of
‘symmetry dictates interaction’ (Yang (1980)). To derive the nuclear interaction from
ChEFT, one has to identify the relevant symmetries of low-energy QCD ﬁrst. Then,
one needs to construct the most general Lagrangian including those symmetries and
symmetry breakings. After that, one needs to do a low momentum expansion and
design the scheme to collect the important contributions. The scheme is called chiral
perturbation theory (ChPT). Finally, one calculates those Feynman diagrams of the
important contributions order by order, in terms of an expansion in the small external
momenta over the large scale, ( Q
Λχ
)ν. Here Q means the nucleon three-momentum
or pion four-momentum or a pion mass which is around 140 MeV, Λχ is the chiral
symmetry breaking scale (hadronic scale) which is about 1 GeV, ν is the power of the
order. Determining the power ν is called power counting. ν = 0 terms are the called
the leading order (LO) which contributes the most to the nuclear interaction. There
4
are no ν = 1 terms due to parity and time-reversal invariance, so the next-to-leading
order (NLO) terms are for ν = 2. The next-to-next-to-leading order (N 2LO) terms are
for ν = 3, and this is where a nonvanishing 3NF occurs (van Kolck (1994); Epelbaum
et al. (2002)). The next-to-next-to-next-to-leading order (N 3LO) are for ν = 3 and
that is where a 4NF occurs. Note that ( Q
Λχ
)< 1, and the 2NF occurs at ν = 0, the
3NF occurs at ν = 3, and the 4NF occurs at ν = 4. ( Q
Λχ
)0≫ ( Q
Λχ
)3≫ ( Q
Λχ
)4, therefore
ChPT explains the hierarchy of nuclear force 2NF ≫ 3NF ≫ 4NF which we knew
empirically before. Because the Chiral interaction are based on momentum expansion
( Q
Λχ
)ν, it naturally carries the momentum dependence. It is worth mentioning that
(Gezerlis et al. (2013)) up to N 2LO (beginning from N 3LO, non-local operators cannot
be avoided however their eﬀects should be negligible and can be treated perturbatively),
one can write down a mostly local version of the chiral interaction 1 . The local chiral
interaction will be particularly useful for any quantum Monte Carlo (QMC) method
in continuous space which includes the method used in this work.
