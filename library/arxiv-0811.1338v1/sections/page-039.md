---
doc_id: arxiv-0811.1338v1
doc_title: "Modern Theory of Nuclear Forces"
section_id: page-039
section_title: "Page 39"
section_number: null
pages: 39-39
source_pdf: 0811.1338v1.pdf
source_sha256: 9a57cb6e014d3ead
toc_source: undetermined
doc_brief: "Modern Theory of Nuclear Forces — 52 sections: Page 1; Page 2; Page 3"
---
0.01
0.1
1
10
(Mπ
crit-Mπ) [MeV]
-2000
0
2000
a
1/2
nd [fm]
FIG. 35 Doublet neutron-deuteron scattering length a1/2
nd in
the critical region computed in the pionless EFT. The solid
line gives the LO result, while the crosses and circles show the
NLO and N2LO results. The dotted lines indicate the pion
masses at which a1/2
nd diverges.
doublet scattering length a1/2
nd in the critical region. The
solid line gives the LO result, while the crosses and cir-
cles show the NLO and N2LO results. The dotted lines
indicate the pion masses at which a1/2
nd diverges because
the second and third excited states of the triton appear
at the neutron-deuteron threshold. These singularities in
a1/2
nd (Mπ) are a clear signature that the limit cycle is ap-
proached in the critical region. Considering the speciﬁc
case of the doublet scattering length at Mπ = 190 MeV,
we have
a1/2
nd (Mπ = 190 MeV) = (93.18+0.80+0.14) fm . (2.72)
At this pion mass we are fairly far away from any singular
points in the function a1/2
nd (Mπ). Consequently, the pion-
less results follow a natural convergence pattern with the
expansion parameter γr0, which is ≈0.08 at this value
of Mπ. For three-body scattering observables in the crit-
ical region no calculation in chiral EFT is available. The
above example shows that both approaches complement
each other. If the pion mass dependence of one three-
body observable is known, the pionless theory can be
used to predict all other observables with high precision
and less computational eﬀort. Figure 35 demonstrates
clearly that the pionless theory converges rapidly in the
critical region.
A ﬁnal answer on the question of whether an infrared
limit cycle can be realized in QCD can only be given by
solving QCD directly.
In particular, it would be very
interesting to know whether this can be achieved by ap-
proriately tuning the quark masses in a Lattice QCD
simulation (396). Finally, we note that the dependence
of nuclear binding on hadronic mass variation has also
been studied based on the Argonne potential (397).
III. TOWARDS A MANY-BODY EFT FOR NUCLEI
The EFT approach to the nuclear many-body problem
is much less established than the one for the forces and
few-nucleon systems. This is, on one hand, related to the
apperance of new scales like the Fermi momentum or in-
duced by collective excitations, and on the other hand to
the computational problems related to solve the many-
body problem. Thus, a variety of pathways are being ex-
plored and here we can only give a brief overview about
the existing attempts and their status. For a pedagog-
ical review on the application of EFTs to ﬁnite density
systems, we refer to Furnstahl et al. (398).
A. In-medium chiral perturbation theory
Early attempts to formulate in-medium chiral per-
turbation theory where mostly triggered by the pio-
neering paper of Kaplan and Nelson on kaon condensa-
tion (399). Most of these calculations were based on chi-
ral Lagrangians at most bilinear in the nucleon ﬁelds and
performed in the mean-ﬁeld approximation,
¯NDN →
ρpTrD11 + ρnTrD22 with ρp(ρn) the proton (neutron)
density, D represents a generic diﬀerential operator in-
cluding the coupling to pions and external sources, the
trace runs over spinor indices and the subscripts run in
ﬂavor space.
Proceeding in this way, one keeps track
about the vacuum CHPT Lagrangians, but the chiral
counting in the medium is lost, as e.g. nucleon corre-
lations are not considered. The most elegant formulation
of this approach based on the path-integral formulation is
due to Wirzba and collaboraotrs, see e.g. (400; 401; 402).
To go beyond the mean-ﬁeld approximation, the in-
medium genrating functional for pions coupled to nucle-
ons and external sources was developed in Refs. (403;
404). Leaving out multi-nucleon interactions, as system-
atic in-medium CHPT can be developed by expanding
around the nuclear matter ground state at asymptotic
times and intergrating out the nucleon ﬁelds in the path
integral representation, giving rise to the in-medium gen-
erating functional (for the detailed derivation, we refer to
Ref. (403))
ei ˜
Z[v,a,s,p] =
Z
[dU] exp
(
i
Z
dx Lππ−i
Z
d⃗p
(2π)32E(p)
×
Z
dx dy eip(x−y) Tr
 
A[I4 −D−1
0 A]−1|(x,y)(̸p +m) n(p)
!
+ 1
2
Z
d⃗p
(2π)32E(p)
Z
d⃗q
(2π)32E(q)
Z
dx dx′ dy dy′ eip(x−y)
×e−iq(x′−y′) Tr
 
A[I4 −D−1
0 A]−1|(x,x′) (̸q +m)n(q)
×A[I4 −D−1
0 A]−1|(y′,y)(̸p +m) n(p)
!
+ . . .
)
