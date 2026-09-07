---
doc_id: arxiv-0905.1873v2
doc_title: "Evolution of Nuclear Many-Body Forces with the Similarity Renormalization Group"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-3
source_pdf: 0905.1873v2.pdf
source_sha256: d4f785469fafdce6
---
arXiv:0905.1873v2  [nucl-th]  17 Aug 2009
Evolution of Nuclear Many-Body Forces
with the Similarity Renormalization Group
E.D. Jurgenson, 1 P. Navr´ atil,2 and R.J. Furnstahl 1
1Department of Physics, The Ohio State University, Columbus , OH 43210, USA
2Lawrence Livermore National Laboratory, P.O. Box 808, L-41 4, Livermore, CA 94551, USA
The ﬁrst practical method to evolve many-body nuclear force s to softened form using the Similarity
Renormalization Group (SRG) in a harmonic oscillator basis is demonstrated. When applied to 4He
calculations, the two- and three-body oscillator matrix el ements yield rapid convergence of the
ground-state energy with a small net contribution of the ind uced four-body force.
PACS numbers: 21.30.-x,05.10.Cc,13.75.Cs
A major goal of nuclear structure theory is to make
quantitative calculations of low-energy nuclear observ-
ables starting from microscopic internucleon forces. Chi-
ral eﬀective ﬁeld theory ( χ EFT) provides a systematic
construction of these forces, including a hierarchy of
many-body forces of decreasing strength [1]. Renormal-
ization group (RG) methods can be used to soften the
short-range repulsion and short-range tensor components
of the initial chiral interactions so that convergence of nu-
clear structure calculations is greatly accelerated [2, 3].
The diﬃculty is that these transformations (or any other
softening transformations) change the short-range many-
body forces. To account for these changes, we present
in this letter the ﬁrst consistent evolution of three-body
forces by using the Similarity Renormalization Group
(SRG) [4, 5, 6, 7, 8], which oﬀers a technically simpler
approach to evolving many-body forces than other RG
formulations. Our results show that both the many-body
hierarchy of χ EFT and the improved convergence prop-
erties are preserved.
The SRG is a series of unitary transformations of the
free-space Hamiltonian ( H ≡ Hλ =∞),
Hλ = Uλ Hλ =∞U †
λ , (1)
labeled by a momentum parameter λ that runs from ∞
toward zero, which keeps track of the sequence of Hamil-
tonians ( s = 1/λ 4 has been used elsewhere [7, 8]). These
transformations are implemented as a ﬂow equation in λ
(in units where ℏ2/M = 1),
dHλ
dλ = − 4
λ 5 [[T, H λ ], H λ ] , (2)
whose form guarantees that the Hλ ’s are unitarily equiv-
alent [6, 7].
The appearance of the nucleon kinetic energy T in
Eq. (2) leads to high- and low-momentum parts of Hλ
being decoupled, which means softer and more conver-
gent potentials [9]. This is evident in a partial-wave mo-
mentum basis, where matrix elements ⟨k|Hλ |k′⟩ connect-
ing states with (kinetic) energies diﬀering by more than
λ 2 are suppressed by e−(k2−k′ 2)2/λ 4
factors and there-
fore the states decouple as λ decreases. (Decoupling also
results from replacing T in Eq. (2) with other genera-
tors [6, 7, 10, 11].) The optimal range for λ is not yet
established and also depends on the system, but experi-
ence with SRG and other low-momentum potentials sug-
gest that running to about λ = 2 . 0 fm−1 is a good com-
promise between improved convergence from decoupling
and the growth of induced many-body interactions [9].
(Also, diﬀerences between using T and the diagonal of
Hλ in Eq. (2), which can be very important in some sit-
uations [10], are negligible in this λ range.)
To see how the two-, three-, and higher-body potentials
are identiﬁed, it is useful to decompose Hλ in second-
quantized form. Schematically (suppressing indices and
sums),
Hλ = ⟨T ⟩a†a + ⟨V (2)
λ ⟩a†a†aa + ⟨V (3)
λ ⟩a†a†a†aaa + · · · ,
(3)
where a†, a are creation and destruction operators with
respect to the vacuum in some (coupled) single-particle
basis. This deﬁnes ⟨T ⟩, ⟨V (2)
λ ⟩, ⟨V (3)
λ ⟩, . . . as the one-
body, two-body, three-body, . . . matrix elements at each
λ. Upon evaluating the commutators in Eq. (2) using
Hλ from Eq. (3), we see that even if initially there are
only two-body potentials, higher-body potentials are gen-
erated with each step in λ. Thus, when applied in an
A-body subspace, the SRG will “induce” A-body forces.
But we also see that ⟨T ⟩ is ﬁxed, ⟨V (2)
λ ⟩ is determined
only in the A = 2 subspace with no dependence on ⟨V (3)
λ ⟩,
⟨V (3)
λ ⟩ is determined in A = 3 given ⟨V (2)
λ ⟩, and so on.
Since only the Hamiltonian enters the SRG evolution
equations, there are no diﬃculties from having to solve
T matrices in all channels for diﬀerent A-body systems.
However, in a momentum basis the presence of spectator
nucleons requires solving separate equations for each set
of ⟨V (n)
λ ⟩ matrix elements. In Refs. [12, 13], a diagram-
matic approach is introduced to handle this decomposi-
tion. But while it is natural to solve Eq. (2) in momentum
representation, it is an operator equation so we can use
any convenient basis. Here we evolve in a discrete basis,
where spectators are handled without a decomposition
and induced many-body forces can be directly identiﬁed.
Having chosen such a basis, we obtain coupled ﬁrst-order
diﬀerential equations for the matrix elements of the ﬂow-
ing Hamiltonian Hλ , where the right side of Eq. (2) is
evaluated using simple matrix multiplications.
2
Our calculations are performed in the Jacobi coordi-
nate harmonic oscillator (HO) basis of the No-Core Shell
Model (NCSM) [14]. This is a translationally invariant,
anti-symmetric basis for each A, with a complete set of
states up to a maximum excitation of NmaxℏΩ above the
minimum energy conﬁguration, where Ω is the harmonic
oscillator parameter. The procedures used here build di-
rectly on Ref. [13], which presents a one-dimensional im-
plementation of our approach along with a general anal-
ysis of the evolving many-body hierarchy.
We start by evolving Hλ in the A = 2 subsystem, which
completely ﬁxes the two-body matrix elements ⟨V (2)
λ ⟩.
Next, by evolving Hλ in the A = 3 subsystem we deter-
mine the combined two-plus-three-body matrix elements.
We can isolate the three-body matrix elements by sub-
tracting the evolved ⟨V (2)
λ ⟩ elements in the A = 3 ba-
sis [13]. Having obtained the separate NN and NNN
matrix elements, we can apply them unchanged to any
nucleus. We are also free to include any initial three-
nucleon force in the initial Hamiltonian without chang-
ing the procedure. If applied to A ≥ 4, four-body (and
higher) forces will not be included and so the transforma-
tions will be only approximately unitary. The questions
to be addressed are whether the decreasing hierarchy of
many-body forces is maintained and whether the induced
four-body contribution is unnaturally large. We summa-
rize in Table I the diﬀerent calculations to be made for
3H and 4He to confront these questions.
The initial ( λ = ∞) NN potential used here is the
500 MeV N 3LO interaction from Ref. [15]. The initial
NNN potential is the N 2LO interaction [16] in the local
form of Ref. [17] with constants ﬁt to the average of tri-
ton and 3He binding energies and to triton beta decay
according to Ref. [18]. We expect similar results from
other initial interactions because the SRG drives them
toward near universal form; a survey will be given in
Ref. [19]. NCSM calculations with these initial interac-
tions and the parameter set in Table I of Ref. [18] yield
energies of −8. 473(4) MeV for 3H and −28. 50(2) MeV for
4He compared with −8. 482 MeV and −28. 296 MeV from
experiment, respectively. So there is a 20 keV uncertainty
in the calculation of 4He from incomplete convergence
and a 200 keV discrepancy with experiment. The latter
is consistent with the omission of three- and four-body
chiral interactions at N 3LO. These provide a scale for
assessing whether induced four-body contributions are
important compared to other uncertainties.
In Fig. 1, the ground-state energy of the triton is plot-
ted as a function of the ﬂow parameter λ. Evolution is
from λ = ∞, which is the initial (or “bare”) interaction,
toward λ = 0. We use Nmax = 36 and ℏΩ = 28 MeV, for
which all energies are converged to better than 10 keV.
We ﬁrst consider an NN interaction with no initial NNN
(“NN-only”). If Hλ is evolved only in an A = 2 sys-
tem, higher-body induced pieces are lost. The resulting
energy calculations will only be approximately unitary
for A > 2 and the ground-state energy will vary with λ
(squares). Keeping the induced NNN yields a ﬂat line
1 2 3 4 5 6 7 10 20
λ [fm
−1
]
−8.6
−8.4
−8.2
−8.0
−7.8
−7.6
−7.4Ground-State Energy [MeV]
NN-only
NN + NNN-induced
NN + NNN
3
H
Expt.
N
3
LO (500 MeV)
FIG. 1: (Color online) Ground-state energy of 3H as a func-
tion of the SRG evolution parameter, λ . See Table I for the
nomenclature of the curves.
1 2 3 4 5 10 20
λ [fm
−1
]
−29
−28
−27
−26
−25
−24Ground-State Energy [MeV]
NN-only
NN+NNN-induced
+NNN-initial
4
He N
3
LO (500 MeV)
Expt.
FIG. 2: (Color online) Ground-state energy of 4He as a func-
tion of the SRG evolution parameter, λ . See Table I for the
nomenclature of the curves.
(circles), which implies an exactly unitary transforma-
tion; the line is equally ﬂat if an initial NNN is included
(diamonds). Note that the net induced three-body is
comparable to the initial NNN contribution and thus is
of natural size.
In Fig. 2, we examine the SRG evolution in λ for 4He
with ℏΩ = 36 MeV. The ⟨V (2)
λ ⟩ and ⟨V (3)
λ ⟩ matrix ele-
ments were evolved in A = 2 and A = 3 with Nmax = 28
and then truncated to Nmax = 18 at each λ to diagonal-
ize 4He. The NN-only curve has a similar shape as for
the triton. In fact, this pattern of variation has been ob-
3
TABLE I: Deﬁnitions of the various calculations.
NN-only No initial NNN interaction and do not keep NNN-induc ed interaction.
NN + NNN-induced No initial NNN interaction but keep the SRG- induced NNN interaction.
NN + NNN Include an initial NNN interaction and keep the SRG-induced NNN interaction.
served in all SRG calculations of light nuclei [3]. When
the induced NNN is included, the evolution is close to
unitary and the pattern only depends slightly on an ini-
tial NNN interaction. In both cases the dotted line rep-
resents the converged value for the initial Hamiltonian.
At large λ, the discrepancy is due to a lack of conver-
gence at Nmax = 18, but at λ < 3 fm−1 SRG decoupling
takes over and the discrepancy is due to short-range in-
duced four-body forces, which therefore contribute about
50 keV net at λ = 2 fm−1. This is small compared to the
rough estimate in Ref. [20] that the contribution from
the long-ranged part of the N 3LO four-nucleon force to
4He binding is of order a few hundred keV. If needed,
we could evolve 4-body matrix elements in A = 4 and
will do so when nuclear structure codes can accomodate
them.
4 8 12 16 20 24 28
Nmax
−8.5
−8.0
−7.5
−7.0
−6.5
−6.0E [MeV]
bare (28)
L-S (28)
SRG (2.0/20)
3
HN
3
LO (500 MeV)
NN + NNN
NN (+ NNN-
induced)
FIG. 3: (Color online) Ground-state energy of 3H as a func-
tion of the basis size Nmax for an N 3LO NN interaction [15]
with and without an initial NNN interaction [1, 18]. Un-
evolved (“bare”) and Lee-Suzuki (L-S) results with ℏΩ =
