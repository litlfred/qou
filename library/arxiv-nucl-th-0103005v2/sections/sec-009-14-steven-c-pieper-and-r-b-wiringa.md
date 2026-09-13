---
doc_id: arxiv-nucl-th-0103005v2
doc_title: "Quantum Monte Carlo Calculations of Light Nuclei"
section_id: sec-009-14-steven-c-pieper-and-r-b-wiringa
section_title: "Steven C. Pieper and R. B. Wiringa"
section_number: 14
pages: 14-15
source_pdf: 0103005v2.pdf
source_sha256: c2aaa21b51d7bc10
doc_brief: "Quantum Monte Carlo Calculations of Light Nuclei — Accurate quantum Monte Carlo calculations of ground and low-lying excited states of light p-shell nuclei are now possible for realistic nuclear"
---
expensive to evaluate in this basis, but the overall savings in computation is still
large. Furthermore, if for even- A nuclei the M = 0 state is computed, only half the
spin components need to be evaluated; the other ones can be fo und by time-reversal
invariance.
Expectation values of the kinetic energy and spin-orbit pot ential require the com-
putation of ﬁrst derivatives and diagonal second derivativ es of the wave function.
These are obtained by evaluating the wave function at 6 A slightly shifted positions
of the coordinates R and taking ﬁnite diﬀerences, as discussed in Ref. (10). Poten -
tial terms quadratic in L require mixed second derivatives, which can be obtained
by additional wave function evaluations and ﬁnite diﬀerence s.
The rapid growth in the size of Ψ as A increases is the chief limitation, both
in computer time and memory requirements, on extending the c urrent method
to larger nuclei. The cost of an energy calculation for a give n conﬁguration also
increases as the number of pairs, P = 1
2A(A − 1), because of the number of pair
operations required to construct Ψ, and roughly as the numbe r of particles, A, due
to the number of wave function evaluations required to compu te the kinetic energy
by ﬁnite diﬀerences. These factors are shown in Table 2 for a nu mber of nuclei,
with a ﬁnal overall product showing the cost relative to that for an 8Be calculation.
Some initial A = 9, 10 calculations have been made, but are at the limit of curren t
computer resources, so while 12C should be reached in a few years, it may be the
practical limit for this approach. Calculations of nuclei l ike 16O or 40Ca, will require
other methods such as auxiliary-ﬁeld diﬀusion Monte Carlo, w hich samples the spin
and isospin components of the wave function by introducing a uxiliary ﬁelds, as the
plain Monte Carlo samples the spatial part. Also shown in the table is the cost for
several pure neutron problems, such as an eight-body drop (w ith external conﬁning
potential) or 14 or 38 neutrons in a box (with periodic bounda ry conditions) as
neutron matter simulations. The 8n drop has been calculated (39,40) by VMC and
GFMC, and initial box simulations have been done for 14 neutr ons by GFMC (41)
and up to 54 neutrons by AFDMC (20).
A major problem arises in minimizing the variational energy for p-shell nuclei
using the above wave functions: there is no variational mini mum that gives reason-
able rms radii. For example, the variational energy for 6Li is slightly more bound
than for 4He, but is not more bound than for separated 4He and 2H nuclei, so the
wave function is not stable against breakup into α +d subclusters. Consequently,
the energy can be lowered toward the sum of 4He and 2H energies by making the
wave function more and more diﬀuse. Such a diﬀuse wave function would not be
useful for computing other nuclear properties, or as a start ing point for the GFMC
calculation, so the search for variational parameters is co nstrained by requiring the
resulting point proton rms radius, rp, to be close to the experimental values for 6Li
and 7Li ground states. For other A = 6–8 ground states, and all the excited states,
the trial functions contain minimal changes to the 6Li and 7Li wave functions, with
the added requirement that excited states should not have sm aller radii than the
ground states. The ﬁnal step is always the diagonalization o f the Hamiltonian in
Exact Calculations of Light Nuclei 15
Table 2: Approximate scaling of VMC and GFMC calculations wi th system size.
The number of pairs is P , the state-vector size is the product of the number of
spin states and number of isospin states, I(A,T ); as is discussed in the text, these
numbers may be halved for even-A nuclei. The last column is the relative diﬃculty
scaled to 8Be, assuming M = 0 states are computed for even- A nuclei.
A P 2A ×I(A,T ) ∏ / ∏ (8Be)
3H 3 3 8 ×2 0.0004
4He 4 6 16 ×2 0.001
5He 5 10 32 ×5 0.020
6Li 6 15 64 ×5 0.036
7Li 7 21 128 ×14 0.66
8Be 8 28 256 ×14 1.
9Be 9 36 512 ×42 17.
10B 10 45 1024 ×42 24.
12C 12 66 4096 ×132 530.
16O 16 120 65536 ×1430 2 × 105
40Ca 40 780 7 ×1021 3 × 1020
8n 8 28 256 ×1 0.071
14n 14 91 16384 ×1 26.
38n 38 703 3 ×1011 9 × 109
the βLS[n] mixing parameters.
