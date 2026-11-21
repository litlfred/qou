---
doc_id: arxiv-2111.13842v1
doc_title: "Signatures of linear Breit-Wheeler pair production in polarized γγ collisions"
section_id: page-002
section_title: "Page 2"
section_number: null
pages: 2-2
source_pdf: 2111.13842.pdf
source_sha256: 3b1f744b3cd51020
toc_source: undetermined
doc_brief: "Signatures of linear Breit-Wheeler pair production in polarized γγ collisions — 7 sections: Page 1; Page 2; Page 3"
---
FIG. 1. Scenario of the LBW pair production in a colliding setup of
polarized γ-photon beams in x −z plane in the laboratory frame. The
pair spectra are presented in the plane of polar angle θ and kinematic
energy Ek. The lower sketches show the helicity transfer of the
LBW process in the center of mass (c.m.) frame, and Λγ is the total
helicity of two-photon system in the direction of photon momentum ˆnk.
The scattered pair carries the mean total helicity Λe in the direction
of electron momentum ˆne, |±⟩represent the positive and negative
helicity states, corresponding to the right-hand and left-hand spirals,
respectively, and γ(1)/(2)
R/L
denote right-hand circular polarization (RCP)
or left-hand circular polarization (LCP) photon in beam (1) and beam
(2), respectively.
of pair momenta. In addition, the impact of energy distribu-
tion of γ-photon beam on the LBW pair yield is analyzed in
a semi-analytical model [31]. However, considering realistic
polarization and energy distribution into laser-driven γ-photon
beams, the spin-associated momentum and polarization char-
acteristics of the LBW process have not been uncovered and
are still great challenges.
In this Letter, we investigate the complete polarization ef-
fects in the LBW process by virtue of our ﬁrst developed
spin-resolved Monte Carlo (MC) simulation method, which is
applicable for general binary collisions of leptons and photons
(see the interaction scenario in Fig. 1). We ﬁnd that the circular
polarization of γ-photons can modify the kinematics of scat-
tering particles and induces a correlated energy-angle shift of
the LBW pairs (see the upper panel in Fig. 1 and more details
in Fig. 2), and the polarization characteristic of the LBW pairs
depends on the helicity conﬁgures of scattering particles (see
lower panel in Fig. 1 and more details in Fig. 3). Our method
conﬁrms that the polarized γγ collider with an asymmetric
setup can be performed with currently achievable laser facil-
ities (see Tab. I), and the considered polarization eﬀects may
have signiﬁcant applications in high-energy astrophysics.
Let us ﬁrst summarize our simulation method for calculating
the production and polarization of the LBW pairs. Employing
the standard treatment of particle density matrixes in the scat-
tering amplitude of incoherent binary collisions [42–47], the
polarized LBW cross section is obtained as
dσ
dΩ= σ0
F +
3
X
i=1
(G+
i ζ+
i + G−
i ζ−
i ) +
3
X
i,j=1
Hi, jζ+
i ζ−
j
,
(1)
where σ0 = r2
em2
e|pe|/16ε3, Ωis the solid angle, pe the c.m.
momentum of electron, ε the c.m. energy of photon, electron
and positron (they are equal in the c.m. frame), me and re
the electron mass and classical radius, respectively, ζ±
i the
spin components of electron (“−”) and positron (“+”), and the
factors F, G±
i and Hi, j include the photon Stokes parameters ξi
[43] and are given in [48]. Summing over ζ±
i and integrating
over Ω, one obtains
σtot = r2
em4
eπ
4ε4
r
s −4
s

−s −4 + 2ξ(1)
1 ξ(2)
1 + 3sξ(1)
2 ξ(2)
2
−2ξ(1)
3 ξ(2)
3

+ 16π
s
tanh−1
r
s −4
s

2s2 + 8s −16
+ 8ξ(1)
1 ξ(2)
1 −2s2ξ(1)
2 ξ(2)
2 −8ξ(1)
3 ξ(2)
3

,
(2)
where s = 4ε2/m2
e. Relativistic units with c = ℏ= 1 are used
throughout.
The event probabilities are given by σtot and the pair pro-
duction is determined by a rejection method.
The collid-
ing photons in each 3-dimensional cell are paired in the lab-
oratory frame using the no-time-counter method [49]. By
Lorentz boost along the c.m. frame velocity βcm [50–52],
the 4-momenta of paired photons are transformed into the
c.m. frame to calculate pe, which is determined by the prob-
abilistic scattering angle θs. Here θs is calculated by solving
σθ/σtot = R1 ∈(−1, 1), where R1 is an uniform random num-
ber and σθ = √s(s −4)/4
R | cos θs|
−| cos θs| dσ. Moreover, the energy
and momenta of e± in the laboratory frame are obtained by the
inverse Lorentz boost acting on ε and pe.
The mean spin polarization vectors of electron and positron
ζ± are determined by the deﬁned 3-vector basis [44, 48]
and their components can be analytically calculated via
ζ±i = G±
i /F [43]. The corresponding mean helicities are
λ± = ∓ζ±pe/2|pe|. In our MC method, the projections of
ζ± onto the deﬁned spin states D± (unit vectors) of a detec-
tor are calculated with transition probabilities, and the latter
determine the sign of components D±
i
= ζ±i/|ζ±|. Conse-
quently, the total beam polarization is calculated by Ptot =
q
(D±
1)2 + (D±
2)2 + (D±
3)2, where D±
i = PN
n=1 D±,n
i
/N with the
particle number N [53]. Aligning D± to the parallel or per-
pendicular direction of the momenta can further obtain the
longitudinal polarization PL or transverse polarization PT for
e± beams. More details of our simulation method are clariﬁed
in the Supplementary Materials [48].
Impact of the γ-photon polarization on the energy and polar
angle distributions of the LBW pairs is shown in Fig. 2. σtot
of the γ(1)
R γ(2)
R case increases about 33% at the peak energy
and narrows the spectrum, compared with that of the nonpo-
larized case [see Fig. 2(a)], while the linear polarization only
modiﬁes the amplitude because it has no impact on θs [48].
