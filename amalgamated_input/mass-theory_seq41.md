<!-- FILE_START: derivation-audit-intro.md -->
We survey the mass and binding energy derivation. We trace the framework from the categorical action down to a numerical evaluation in MeV. The sequence details the derivation steps, the canonical knot identification, and the binding energy analysis.
<!-- FILE_END: derivation-audit-intro.md -->

<!-- FILE_START: pre-archimedean-derivation-chain.md -->
We derive a particle mass from the categorical action of a quantum observable universe. We detail the algorithm behind each step. Every intermediate quantity belongs to $\mathbb{Q}(q)$. No analytic limits or empirical constants enter until the final Archimedean specialisation.

Three weak-sector inputs calibrate the framework: the electron mass $m_e$ fixes the unit, the neutron beta-decay width fixes $q_0$, and the pion mass fixes the orthogonal meson scale. All other observables—nucleon masses, binding energies, decay Q-values—are derived algebraically at $q_0$.

Steps 1–8 construct the categorical trace inside the Iwahori–Hecke algebra. Steps 9–11 extract physical values.

**Step 1: The categorical action**
A quantum observable universe provides a braided category $\mathbf{C}$ acting on a state bundle. This categorical action yields a braid group representation $\rho_n$ where the $R$-matrix generates the strand crossings. This representation drives all subsequent computations.

**Step 2: Holonomy to Hecke relation**
Yekutieli's surface integration maps the braided category to an Iwahori–Hecke algebra $H_n(q)$. The $R$-matrix parallel transport ensures flatness, yielding the Hecke quadratic relation $\sigma_i^2 = (q - q^{-1})\sigma_i + 1$. The eigenvalue split into $\cosh(\ln q)$ and $\sinh(\ln q)$ separates binding from decay.

**Step 3: Knots and the unique trace**
Every hadron corresponds to a knot closure. Jones’s uniqueness theorem guarantees a single Markov trace $\mathrm{tr}_M$ captures the knot invariant unambiguously. Mass, binding, and decay are evaluations of this one algebraic functional.

**Step 4: Operator selection**
The genus-four state space admits exactly six independent crossing operators. The $H_3(q)$ basis in Gröbner–Shirshov normal form supplies them. The Wedderburn summands indexing the mass formula perfectly mirror the curve's automorphism Prym decomposition.

**Step 5: Wedderburn blocks**
Semisimplicity splits $H_n(q)$ into Wedderburn matrix blocks indexed by partitions. This renders the trace a finite sum. Hoefsmit seminormal representations compute the matrix traces. The Wenzl branching rule provides the central weights $y_\lambda(q)$. The full invariant factors block-by-block.

**Step 6: The Frobenius integral and chirality**
The Markov trace is the Frobenius integral on the symmetric algebra $H_n(q)$. The absolute trace evaluates the absolute categorical mass. The Kauffman framing formula supplies the ribbon twist, matching the knot's chirality to its phase.

**Step 7: Normal forms and finite slices**
The Gröbner–Shirshov basis algorithms rewrite braid words to their canonical normal forms. The associated spectral sequence collapses at $E_2$. Computations therefore require only finite jet-order slices, completely avoiding infinite-series divergence.

**Step 8: Jet order**
The slice-traversal matches the jet order. Convergence confirms the finite-slice evaluation remains algebraically consistent with the expected semiclassical limit at $q \to 1$.

**Step 9: Mass evaluation**
The Archimedean functor evaluates the rational trace at $q_0$ and multiplies by the electron scale. This converts the symbolic invariant into a physical mass. The real part of the categorical volume computes the binding energy, while the imaginary part determines the decay Q-value.

**Step 10: Canonical knot identification**
A semidefinite program selects the canonical Hecke element. Minimizing the Frobenius residual over Gröbner–Shirshov normal forms identifies the ground state. The dual shadow prices explicitly recover the binding energy block saturation.

**Step 11: Decay widths and binding**
A flavor-crossing change $\mathfrak{d} \to \mathfrak{u}$ yields the beta-decay Q-value as a simple difference of traces. Binding energy emerges exactly the same way from the free-versus-bound trace interface.
<!-- FILE_END: pre-archimedean-derivation-chain.md -->

<!-- FILE_START: conj-canonical-knot-id-sdp.md -->
**Conjecture (SDP canonical knot identification).**
*Let $\mathfrak{E}_0$ be the hadronic energy scale and $q_0$ the substrate parameter. For $^2\mathrm{H}$, $^3\mathrm{H}$, and $^3\mathrm{He}$, the joint mass-tower confinement SDP uniquely selects the canonical knot.*

*The SDP minimises the Frobenius residual over Gröbner–Shirshov normal forms. The unique global minimizers are $6_2$ for $^2\mathrm{H}$, $8_{11}$ for $^3\mathrm{H}$, and $L_{6a4}$ for $^3\mathrm{He}$. The residuals match AME binding energies to within 0.5%.*

Historical volume matching originally proposed these assignments. Finitude of the normal-form candidate set, rigorous SDP search bounds, and structural identification of the binding operator $K(\mathfrak{H}) \in H_{3A}(q_0)$ are open verification requirements. The R5-minimal verifier confirms the assignments at the constituent level.
<!-- FILE_END: conj-canonical-knot-id-sdp.md -->

<!-- FILE_START: conj-rho-prefactor-structural.md -->
**Conjecture (structural multiplicity $\rho$).**
*The SDP multiplicity $\rho$ for a confined particle $\mathfrak{H}$ equals the nearest integer to the quantum dimension of the dominant Wedderburn block:*

$$
  \rho(\mathfrak{H}) \;\approx\; \dim_q\!\bigl(\lambda^*(T_w)\bigr).
$$

*The dominant partition $\lambda^*$ maximises the Markov trace contribution. The quantum dimension evaluates the $q$-hook-length formula at $q_0$.*

Evaluating the atomic strand count $n_0 = 3A$ resolves the apparent indistinguishability of isobars. The binding operator links constituent nucleons. The conjecture replaces the case-by-case SDP multiplicity read-out with a first-principles categorical assignment.
<!-- FILE_END: conj-rho-prefactor-structural.md -->

<!-- FILE_START: frobenius-cocasimir-refuted-deuteron.md -->
*The Frobenius co-Casimir prescription $\Delta_\lambda = 1/\dim_q(\lambda)$ fails to close the binding energy formula for the deuteron.*

*The signed binding density yields $+0.145 m_e$, missing the target $-4.35 m_e$. The gap vastly exceeds the tolerance. The sign is incorrect.*

This algebraic refutation eliminates the co-Casimir ansatz as a universal correction factor. We strictly enforce the "no empirical fits" policy.
<!-- FILE_END: frobenius-cocasimir-refuted-deuteron.md -->

