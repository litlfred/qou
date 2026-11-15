---
doc_id: arxiv-0811.1338v1
doc_title: "Modern Theory of Nuclear Forces"
section_id: page-035
section_title: "Page 35"
section_number: null
pages: 35-35
source_pdf: 0811.1338v1.pdf
source_sha256: 9a57cb6e014d3ead
toc_source: undetermined
doc_brief: "Modern Theory of Nuclear Forces — 52 sections: Page 1; Page 2; Page 3"
---
The transfer matrix for nt-th step has, besides the free
part, two important contributions:
M (nt) = : exp

−Hfreeαt
−gAαt
2Fπ
X
S,I
X⃗
ns
∇SπI(⃗ns, nt)ρa†,a
S,I (⃗ns)
+
p
−Cαt
X⃗
ns
[s(⃗ns, nt)ρa†,a(⃗ns)
+ i
p
CIαt
X
I
sI(⃗ns, nt)ρa†,a
I
(⃗ns)]

: .(2.64)
Here :: denotes normal ordering.
The ﬁrst long-range
contribution ∼
gA includes the instantaneous pion-
nucleon interaction and describes the one-pion-exchange
in the leading-order eﬀective potential. The second short-
range contribution corresponds to the NN contact in-
teractions.
The low-energy constants C = CS −2CT
and CI = −CT (cf.
sec. II.B) have diﬀerent signs,
C < 0, CI > 0. With these signs the pion-less theory
can be shown to have no sign-oscillations if the number
of protons and neutrons are equal and they stay pair-wise
in isospin-singlet states. In this case the multiplication
with τ2 of the single-nucleon matrix elements M from left
and right is well deﬁned and gives τ2Mτ2 = M∗. For this
reason, the determinant of M is real, det M∗= det M.
Since τ2 is antisymmetric, the eigenvalues of M are dou-
bly degenerate. This leads to a positive Slater determi-
nant (382; 383)
det M ≥0.
(2.65)
The introduction of pions causes small sign oscillations
which, however, are not severe and appear to be sup-
pressed.
To perform simulations in a most eﬃcient way one ex-
ploits the approximate SU(4)-Wigner (384) symmetry in
the NN system. The symmetry transformation is given
by independent rotations of the spin and isospin degrees
of freedom.
δN = αµνσµτ νN
with
σµ = (1,⃗σ) ,
τµ = (1,⃗τ).
(2.66)
One can show that in the limit where the NN S-wave scat-
tering lengths approach inﬁnity the two-nucleon system
becomes invariant under the SU(4)-transformation (385).
The SU(4)-breaking corrections come from the ﬁnite
the scattering length and higher order terms in the
chiral expansion, these are of order O((1/a(3S1) −
1/a(1S0)), q/Λχ).
Since the NN scattering lengths are
very large, the SU(4)-breaking corrections appear to be
small. This fact can be used to improve the performance
of the lattice simulations. The SU(4) symmetric transfer
matrix is given by
M (nt) = : exp

−Hfreeαt
+
p
−Cαt
X⃗
ns
s(⃗ns, nt)ρa†,a(⃗ns)

: . (2.67)
O
Ψ free
Ψ free
0
2Lto+ Lti
SU(4) π
Lto+ Lti/2
Lto
Lto+ Lti
full LO
full LO
SU(4) π
operator insertion for
expectation value
Z,N
Z,N
FIG. 29 Overview of the various pieces of the transfer matrix
calculation.
In this case there are no sign oscillations for an even
number of nucleons (386) and one only has one auxiliary
ﬁeld such that the simulations become much cheaper.
Although there is no positivity theorem for odd numbers
of nucleons, sign oscillations seem to be suppressed also
in systems with odd number of nucleons because it is
only one particle away from an even system with no sign
oscillations. Since the ﬁnal result is close to the one pro-
duced by a SU(4)-symmetric simulation it pays to divide
a simulations into three parts. To simulate the expecta-
tion value of some observable one uses SU(4)-symmetric
transfer matrices in the ﬁrst and the last Lt0 steps in
order to ﬁlter the low-energy signal. After this ﬁltering,
one starts the simulation with the complete (realistic)
transfer matrices. A schematic overview of the transfer
matrix calculation is shown in Fig. 29. Having set up
the transfer matrix, one utilizes the hybrid Monte-Carlo
(HMC) method (387) to update the ﬁeld conﬁgurations.
More speciﬁcally, one introduces the conjugate ﬁelds pπI,
ps, psI and uses molecular dynamics trajectories to gen-
erate new conﬁgurations for the ﬁelds pπI, ps, psI, πI, s,
sI which keep the HMC Hamiltonian
HHMC = 1
2
X⃗
n
X
I

p2
πI(⃗n) + p2
sI(⃗n)

+ p2
s(⃗n)

+ V (πI, s, sI),
(2.68)
constant, where the HMC potential is deﬁned by
V (πI, s, sI) = Sππ + Sss −log | det M|.
(2.69)
Upon completion of each molecular dynamics trajec-
tory, an Metropolis accept or reject step for the new
conﬁguration according to the probability distribution
exp(−HHMC) is applied. This process of molecular dy-
namics trajectory and Metropolis step is repeated many
times.
Already at LO promising results for binding energies,
radii and density correlations for the deuteron, triton and
4He are obtained (381). On a 53 lattice, the triton bind-
ing energy agrees with experiment within 5% and the
triton root-mean-square radius is accurate to 30%. The
binding energy for 4He is within 25% of the experimen-
tal value while the root-mean-square radius agrees within
10%. Note, however, that one has to overcome a zero-
range clustering instability that appears for 4 (or more
