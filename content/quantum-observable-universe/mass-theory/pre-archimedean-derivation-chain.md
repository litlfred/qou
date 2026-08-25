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
The genus-four state space admits exactly six independent crossing operators. The $H_3(q)$ basis in Gröbner–Shirshov normal form supplies them. The Wedderburn summands indexing the mass formula mirror the curve's automorphism Prym decomposition.

**Step 5: Wedderburn blocks**
Semisimplicity splits $H_n(q)$ into Wedderburn matrix blocks indexed by partitions. This renders the trace a finite sum. Hoefsmit seminormal representations compute the matrix traces. The Wenzl branching rule provides the central weights $y_\lambda(q)$. The full invariant factors block-by-block.

**Step 6: The Frobenius integral and chirality**
The Markov trace is the Frobenius integral on the symmetric algebra $H_n(q)$. The absolute trace evaluates the absolute categorical mass. The Kauffman framing formula supplies the ribbon twist, matching the knot's chirality to its phase.

**Step 7: Normal forms and finite slices**
The Gröbner–Shirshov basis algorithms rewrite braid words to their canonical normal forms. The associated spectral sequence collapses at $E_2$. Computations therefore require only finite jet-order slices, avoiding infinite-series divergence.

**Step 8: Jet order**
The slice-traversal matches the jet order. Convergence confirms the finite-slice evaluation remains algebraically consistent with the expected semiclassical limit at $q \to 1$.

**Step 9: Mass evaluation**
The Archimedean realisation evaluates the rational trace at $q_0$ and multiplies by the electron scale. This converts the symbolic invariant into a physical mass. The real part of the categorical volume computes the binding energy, while the imaginary part determines the decay Q-value.

**Step 10: Canonical knot identification**
A semidefinite program selects the canonical Hecke element. Minimizing the Frobenius residual over Gröbner–Shirshov normal forms identifies the ground state. The dual shadow prices explicitly recover the binding energy block saturation.

**Step 11: Decay widths and binding**
A flavor-crossing change $\mathfrak{d} \to \mathfrak{u}$ yields the beta-decay Q-value as a simple difference of traces. Binding energy emerges exactly the same way from the free-versus-bound trace interface.
