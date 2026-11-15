---
doc_id: arxiv-0905.1873v2
doc_title: "Evolution of Nuclear Many-Body Forces with the Similarity Renormalization Group"
section_id: page-001
section_title: "Page 1"
section_number: null
pages: 1-1
source_pdf: 0905.1873v2.pdf
source_sha256: d4f785469fafdce6
toc_source: undetermined
doc_brief: "Evolution of Nuclear Many-Body Forces with the Similarity Renormalization Group — 4 sections: Page 1; Page 2; Page 3"
---
arXiv:0905.1873v2  [nucl-th]  17 Aug 2009
Evolution of Nuclear Many-Body Forces
with the Similarity Renormalization Group
E.D. Jurgenson,1 P. Navr´atil,2 and R.J. Furnstahl1
1Department of Physics, The Ohio State University, Columbus, OH 43210, USA
2Lawrence Livermore National Laboratory, P.O. Box 808, L-414, Livermore, CA 94551, USA
The ﬁrst practical method to evolve many-body nuclear forces to softened form using the Similarity
Renormalization Group (SRG) in a harmonic oscillator basis is demonstrated. When applied to 4He
calculations, the two- and three-body oscillator matrix elements yield rapid convergence of the
ground-state energy with a small net contribution of the induced four-body force.
PACS numbers: 21.30.-x,05.10.Cc,13.75.Cs
A major goal of nuclear structure theory is to make
quantitative calculations of low-energy nuclear observ-
ables starting from microscopic internucleon forces. Chi-
ral eﬀective ﬁeld theory (χEFT) provides a systematic
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
hierarchy of χEFT and the improved convergence prop-
erties are preserved.
The SRG is a series of unitary transformations of the
free-space Hamiltonian (H ≡Hλ=∞),
Hλ = UλHλ=∞U †
λ ,
(1)
labeled by a momentum parameter λ that runs from ∞
toward zero, which keeps track of the sequence of Hamil-
tonians (s = 1/λ4 has been used elsewhere [7, 8]). These
transformations are implemented as a ﬂow equation in λ
(in units where ℏ2/M = 1),
dHλ
dλ = −4
λ5 [[T, Hλ], Hλ] ,
(2)
whose form guarantees that the Hλ’s are unitarily equiv-
alent [6, 7].
The appearance of the nucleon kinetic energy T in
Eq. (2) leads to high- and low-momentum parts of Hλ
being decoupled, which means softer and more conver-
gent potentials [9]. This is evident in a partial-wave mo-
mentum basis, where matrix elements ⟨k|Hλ|k′⟩connect-
ing states with (kinetic) energies diﬀering by more than
λ2 are suppressed by e−(k2−k′2)2/λ4 factors and there-
fore the states decouple as λ decreases. (Decoupling also
results from replacing T in Eq. (2) with other genera-
tors [6, 7, 10, 11].) The optimal range for λ is not yet
established and also depends on the system, but experi-
ence with SRG and other low-momentum potentials sug-
gest that running to about λ = 2.0 fm−1 is a good com-
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
λ
⟩a†a†aa + ⟨V (3)
λ
⟩a†a†a†aaa + · · · ,
(3)
where a†, a are creation and destruction operators with
respect to the vacuum in some (coupled) single-particle
basis.
This deﬁnes ⟨T ⟩, ⟨V (2)
λ
⟩, ⟨V (3)
λ
⟩, . . . as the one-
body, two-body, three-body, . . . matrix elements at each
λ. Upon evaluating the commutators in Eq. (2) using
Hλ from Eq. (3), we see that even if initially there are
only two-body potentials, higher-body potentials are gen-
erated with each step in λ. Thus, when applied in an
A-body subspace, the SRG will “induce” A-body forces.
But we also see that ⟨T ⟩is ﬁxed, ⟨V (2)
λ
⟩is determined
only in the A = 2 subspace with no dependence on ⟨V (3)
λ
⟩,
⟨V (3)
λ
⟩is determined in A = 3 given ⟨V (2)
λ
⟩, and so on.
Since only the Hamiltonian enters the SRG evolution
equations, there are no diﬃculties from having to solve
T matrices in all channels for diﬀerent A-body systems.
However, in a momentum basis the presence of spectator
nucleons requires solving separate equations for each set
of ⟨V (n)
λ
⟩matrix elements. In Refs. [12, 13], a diagram-
matic approach is introduced to handle this decomposi-
tion. But while it is natural to solve Eq. (2) in momentum
representation, it is an operator equation so we can use
any convenient basis. Here we evolve in a discrete basis,
where spectators are handled without a decomposition
and induced many-body forces can be directly identiﬁed.
Having chosen such a basis, we obtain coupled ﬁrst-order
diﬀerential equations for the matrix elements of the ﬂow-
ing Hamiltonian Hλ, where the right side of Eq. (2) is
evaluated using simple matrix multiplications.
