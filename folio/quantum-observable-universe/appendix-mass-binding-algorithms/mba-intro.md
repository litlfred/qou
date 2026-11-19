**Purpose.**
This appendix gives a self-contained mathematical specification of the algorithms that map the categorical data $(\mathbf{C}, A, \tau)$ and the balancing twist parameter $q_0 > 1$ to dimensionless particle mass ratios, electromagnetic and weak decay observables, and nuclear binding energies. Every procedure is stated purely in terms of its algebraic, topological, or variational inputs, its terminating transformation rules, its asymptotic complexity, and the theorems in the main text that establish well-definedness.

**Four arithmetic regimes.**
Each step of the evaluation chain executes in one of four exact or enclosure-certified regimes:

1. **Exact Laurent and rational algebra over $\mathbb{Z}[q, q^{-1}]$ and $\mathbb{Q}(q)$.** Braid-group actions, Gröbner–Shirshov normal-form reduction, $2 \times 2$ Hecke transfer-matrix recurrences, Specht characters, Convention-D Markov traces ($z_D = q^3/(q^2 + 1)$), and Geer–Patureau-Mirand–Turaev (GPMT) modified-dimension renormalizations are evaluated without rounding in polynomial or rational function rings.
2. **Exact combinatorial and simplicial topology over $\mathbb{Z}$.** Standard Young tableau dimensions, content sums, 3D compact-ball triangulations $(f_0, f_1, f_2, f_3)$ satisfying Dehn–Sommerville elimination, and $(2j + 1)$ spin–orbit subshell capacities are computed in exact integer arithmetic.
3. **Convex primal–dual conic optimization.** Confinement operator selection solves a primal–dual linear or semidefinite program over the Frobenius Gram cone $G_{ij} = \mathrm{tr}_M(b_i b_j) \succeq 0$, recovering both the minimal-trace primal state $x^*$ and the active dual shadow-price support $\{i : y_i^* > 0\}$.
4. **Arbitrary-precision real ball evaluation ($\geq 80$ decimal digits).** Transcendental constants such as the figure-eight hyperbolic volume $\mathrm{Vol}(4_1) = 2\,\mathrm{Cl}_2(\pi/3)$, the Form-B Bring–Schwinger cubic fixed-point coupling $\alpha_{\mathrm{EM}}^{\mathrm{corr}}(q)$, and partial products of the Convention-D $\beta$-decay generating function $\mathcal{G}_D(u; q)$ are evaluated in arbitrary-precision interval arithmetic with explicit analytic truncation bounds.

**Epistemic classification.**
Each step carries one of four structural status designations matching the main derivation tables: *proved* (unconditional theorem of the categorical axioms), *derived* (parameter-free consequence of the categorical chain at $(q_0, m_e)$), *conditional* (resting on an explicitly stated geometric or representation-theoretic hypothesis), or *open* (where a specific coarse-graining or deformation constant awaits first-principles derivation).

**Organisation.**
The summary table in the next section records the input-to-output signature and arithmetic complexity of all twelve canonical steps, followed by individual algorithm specifications in dependency order and five auxiliary blocks covering per-partition Springer/Donaldson–Thomas weights, three-body/four-body correlation bounds, mirror-nucleus baseline cancellation, conditional chiral isovector residues, and all-order Convention-D cumulant extraction.
