---
doc_id: arxiv-2407.04744v2
doc_title: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S"
section_id: sec-005-magnetic-form-factors-and-moments
section_title: "Magnetic form factors and moments"
section_number: null
pages: 5-5
source_pdf: 2407.04744v2.pdf
source_sha256: fc6fda3138296fb1
doc_brief: "Magnetic structure of A≤ 10 nuclei using the Norfolk nuclear models with quantum Monte Carlo methods G. Chambers-Wall 1,∗ A. Gnech 2,3,† G. B. King 1,‡ S — 21 sections: Front matter; Theory; Introduct"
---
The magnetic form factors are extracted from elas-
tic electron scattering differential cross section data (see
Ref. [63] for a review). For this work we use the definition
given in Ref. [63], i.e.,
F 2
M(q) = 1
2J + 1
∞X
L=1
|⟨J||ML(q)||J⟩|2 , (15)
where we express the magnetic form factor as a function
of the reduced matrix elements (RMEs) of the magnetic
multipole operators (ML), andJ is the total angular mo-
mentum of the nucleus.
The calculation of the magnetic multipole expansion is
carried out using standard techniques [64] implemented
to expand the current operator j(q). As the reference
frame, we adopt the one where ˆz is the spin-quantization
axis of the nucleus, and the direction of ˆq is defined by
the angles θ and ϕ, the polar and azimuthal angles with
respect to this axis, respectively. In what follows, we
define q =|q|. The current, in terms of the magnetic
and electric multipoles, MLML and ELML, reads
jλ(q) =
Z
dxeiq·xˆeλ· j(x)
=−
X
L≥1,ML
p
2π(2L + 1)iLDL
ML,λ(−ϕ,−θ,ϕ )
× [λMLML(q) +ELML(q)],
(16)
where λ =±1, and DL
ML,λ are the Wigner rotation ma-
trices [65]. The unit vector ˆeqλ indicates the linear com-
bination
ˆeλ=±1 =∓ˆe1± ˆe2√
2 , (17)
where ˆe3 = ˆq, ˆe2 = ˆz×ˆq, and ˆe1 = ˆe2×ˆe3. Note that, for
elastic scattering, the electric multipole operators ( EL)
vanish because of time reversal invariance [66], and the
sum over L runs only on odd values because of parity
conservation.
As observed in Ref. [67], in VMC and GFMC calcula-
tions, it is more efficient to compute the matrix elements
of j(q) between states of a specific spin configuration MJ
(usually MJ = J) and then adjust the direction of ˆq to
isolate the single RME contributions. In our case, it is
very convenient to select q to be in the x−z plane. This
makesϕ = 0, and ˆe2 = ˆy. Leveraging this selection and
Jπ Nuclei Multipoles
1/2+ 3 He,3H M1
1+ 6 Li M1
3/2− 7Li, 7Be M1, M3
2+ 8 Li, 8B M1, M3
3/2− 9Li, 9C, 9Be, 9B M1, M3
3+ 10 B M1, M3, M5
TABLE I: Multipole contributions to the magnetic form
factors for the nuclei considered in this work.
making use of the Wigner-Eckart theorem in Eq. (16),
the matrix element reduces to [67]
⟨JJ|jy(q)|JJ⟩ =
√
4π
X
L≥1
iL+1⟨JJ,J −J|L0⟩p
L(L + 1)
×P 1
L(cosθ)⟨J||ML(q)∥J⟩ .
(18)
The various multipole contribution to the magnetic
form factor for the nuclei considered in this work are sum-
marized in Table I. The number of independent matrix
elements with different directions of q (i.e., of different
θ’s) that have to be computed is equal to the number of
multipoles allowed. Clearly, any independent choice of
the directions are equivalent; in Appendix B we present
the explicit formulas obtained for our specific choices.
From the smallq behaviour of the magnetic form factor
it is possible to extract the magnetic (dipole) moment of
the nucleus. Starting from the definition of the magnetic
moment, it is possible to show that [67]
⟨J||M1(q)||J⟩≃ i√
2π⟨JJ,J −J|10⟩
q
2mN
µ. (19)
Therefore, considering that the higher-order multipoles
have a negligible contribution to the magnetic moment
at smallq we can select the matrix element computed for
θ = π/2 (any choice is equivalent) and so the magnetic
moment becomes
µ = lim
q→0
−i2mN
q ⟨JJ|jy(q ˆx)|JJ⟩ . (20)
To extract µ, we evaluate ⟨JJ|jy(qˆ x)|JJ⟩ for q ∈
[0.00, 0.25] fm−1 and fit the results to a polynomial, sim-
ilarly to what was done for the multipole analysis of the
6Heβ-decay spectrum in Ref. [35]. The linear coefficient
is then used to determine the quantity of interest.
