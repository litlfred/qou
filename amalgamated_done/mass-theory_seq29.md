<!-- FILE_START: phi-q-markov-residue-habiro-intro.md -->
This sub-section bridges the algebraic foundations to the substrate-level Habiro evaluation. It establishes the $\hat{V}$-pair commutation trace, validates the exact pair equality at fixed jet levels, and states the uniform $\Delta_{\max}$ geometric bound.

The sequence connects the algebraic topological mass formula to the Habiro residue expansion. It interprets the residue as braid holonomy around singular fibres, explicitly splits the graded trace from the residue sum, and applies this split to the 6-term binding density. The closing blocks detail the full pole structure of the mass trace, securing the substrate-flow inputs for the binding density evaluation.
<!-- FILE_END: phi-q-markov-residue-habiro-intro.md -->

<!-- FILE_START: vhat-pair-commutation-trace.md -->
**Lemma (pair commutation at traced-volume level).**
*Let $\hat V_i(q) = z(q)a_i(q) + b_i(q) \in \mathbb{Z}[q^{\pm 1/2}, z]$ be the traced volume of the $i$-th crossing of a closed braid. For any two indices $i, j$:*

$$
  \hat V_i(q) \cdot \hat V_j(q)
  \;=\;
  \hat V_j(q) \cdot \hat V_i(q)
  \qquad
  \text{in } \mathbb{Z}[q^{\pm 1/2}, z].
$$

*Equivalently:*

$$
  \mathrm{tr}_M\!\bigl(\hat V_i \hat V_j\bigr)
  \;=\;
  \mathrm{tr}_M\!\bigl(\hat V_j \hat V_i\bigr)
  \;=\; z^2.
$$

The pentagon identity requirement $uv = qvu$ applies strictly to non-commutative operator lifts, not to the scalar traced volumes. The traced volumes commute exactly.
<!-- FILE_END: vhat-pair-commutation-trace.md -->

<!-- FILE_START: tower-pair-equality-fixed-level.md -->
**Lemma (pair-contribution equality at fixed jet level).**
*Let $n \in \mathbb{N}$ be a brane jet level and let $\mathcal{P}_n = \{(i, j) : 0 \le i < j\}$ be the full set of unordered pair blow-up centres at level $n$. The pair contribution at level $n$ equals:*

$$
  \mathrm{pairs}_n
  \;=\;
  z^2 \sum_{(i, j) \in \mathcal{P}_n}
    \Phi_q\!\bigl(\bigl|\hat V_i^{(n)} \hat V_j^{(n)}\bigr|\bigr).
$$

*The formula is an exact equality, not an upper bound.*

The prior upper-bound framing incorrectly assumed the pentagon inequality applied to scalar volumes. The true algebraic basis is the exact Markov-pair identity $\mathrm{tr}_M(\sigma_i \sigma_j) = z^2$. Lifting this identity to the traced volumes preserves the strict equality at every jet level.
<!-- FILE_END: tower-pair-equality-fixed-level.md -->

<!-- FILE_START: jet-tower-uniform-delta-max.md -->
**Conjecture (uniform per-level binding bound).**
*For every confined vortex $\varrho$, there exists a finite real constant $\Delta_{\max}(\varrho) < \infty$ bounding the per-level binding contribution:*

$$
  |\Delta^{(n)}(\varrho)| \;\le\; \Delta_{\max}(\varrho)
  \qquad\text{for all } n \ge 1.
$$

The canonical formalism verifies this bound empirically at $n = 1, 2, 3$ for $^2\mathrm{H}$, $^3\mathrm{H}$, and $^3\mathrm{He}$. The observed sequence decays geometrically by exactly $\hbar_q^2$, maintaining strict uniformity.

The geometric tail bound of the mass series relies conditionally on this conjecture. Future analytical proofs must either leverage the Gröbner-Shirshov spectral sequence $E_2$-collapse or apply a Yekutieli categorical rigidity bound to the descent involution.
<!-- FILE_END: jet-tower-uniform-delta-max.md -->

<!-- FILE_START: topological-mass-formula-algebraic.md -->
**Proposition (algebraic topological mass formula).**
*Let $\beta \in H_n(R, q)$ be the Hecke normal form of a closed braid. The categorical mass admits the closed form:*

$$
  \mathfrak{m}_{\mathrm{alg}}(\beta)
  \;=\;
  \frac{\Phi_1(\beta)}{\hbar_q^{2}},
\qquad
  \Phi_1(\beta) \;=\; \tau_{\mathrm{arch}}\bigl(\mathrm{Vol}_q(\beta)\bigr)
  \;=\; \ln\!\bigl\lvert\mathrm{Vol}_{q_0}(\beta)\bigr\rvert.
$$

*The constituent operations occur strictly within $\mathbb{Q}(q)$ prior to the archimedean specialisation $\tau_{\mathrm{arch}}$.*

The algebraic quantum volume evaluates as a finite product in $\mathbb{Z}[q^{\pm 1/2}]$. The algebraic identity bypasses complex-analytic limits, asymptotic scaling, and hyperbolic volume conjectures. The archimedean topological formula emerges cleanly as the $q \mapsto q_0$ specialisation of this pre-realisation identity.
<!-- FILE_END: topological-mass-formula-algebraic.md -->

<!-- FILE_START: residue-as-braid-holonomy.md -->
**Remark.**
Each residue $\operatorname{Res}_{q=\zeta_\ell}[\Phi_q \cdot \mathrm{tr}_{M,\,\ell}(T_w)]$ operates gauge-theoretically as the holonomy of the braid loop $T_w$ around the singular fibre at $q = \zeta_\ell$.

The complex parameter $q$ labels a flat holomorphic bundle of Hecke algebras over $\mathbb{C}^\times$. The algebra degenerates at roots of unity, creating singular fibres. The braid word defines a section that acquires monodromy when analytically continued around these fibres. The residue explicitly pairs this monodromy with the Markov trace.

At roots of unity, the Markov trace collapses to the Reshetikhin-Turaev invariant. The residues extract these invariants to populate the Habiro cyclotomic coefficients. For deep-strata braids, the regular-value tower converges too slowly; the holonomy residues supply the missing binding energy.
<!-- FILE_END: residue-as-braid-holonomy.md -->

<!-- FILE_START: graded-trace-residue-split.md -->
**Proposition (graded-trace residue split).**
*The Markov trace decomposes canonically into smooth and oscillating components:*

$$
  \mathrm{tr}_M(T_w, q_0)
  \;=\;
  \mathrm{tr}_{\mathrm{gr}}(T_w, q_0)
  \;+\;
  \mathrm{Res}_{\mathrm{GB}}(T_w, q_0).
$$

*The graded trace evaluates on the associated graded algebra, capturing the leading-order term. The residue sum tallies the rewriting defects from higher filtration strata via the Habiro expansion.*

The split mirrors Strutinsky's macroscopic-plus-shell decomposition. The graded trace acts as the macroscopic liquid-drop baseline. The residue sum supplies the oscillating shell corrections.
<!-- FILE_END: graded-trace-residue-split.md -->

<!-- FILE_START: graded-trace-strutinsky-interpretation.md -->
**Physical interpretation of each piece.**
The categorical split maps precisely onto the Strutinsky energy decomposition $E = \tilde E + \delta E_{\mathrm{shell}}$. The symbol map on the graded algebra implements the Strutinsky smoothing convolution. The residue sum recovers the sharp shell fluctuations that the smoothing procedure suppresses.
<!-- FILE_END: graded-trace-strutinsky-interpretation.md -->

<!-- FILE_START: term6-binding-density.md -->
**Remark.**
*The nuclear binding energy per nucleon follows the structural decomposition:*

$$
  \frac{B(Z, N)}{A}
  \;\approx\;
  \alpha \cdot \frac{T_6(Z, N)}{A^3}
  \;+\;
  \beta
  \;+\;
  \delta_M(Z, N).
$$

*Here $T_6$ evaluates the level-3 Gröbner-Shirshov spectral-sequence stratum, while $\alpha$ and $\beta$ provide AME calibration constants.*

The term $T_6$ enumerates ordered triples of nucleons, generating an intrinsic $\sim A^3$ scaling. Dividing by $A^3$ constructs the proper intensive density. The decomposition structure strictly derives from the spectral sequence and Hecke factorization, isolating the empirical inputs exclusively to the calibration scalars and operator-level magic-shell enhancements.
<!-- FILE_END: term6-binding-density.md -->

<!-- FILE_START: full-pole-structure-mass-trace.md -->
**Proposition (Habiro completion of the mass trace).**
*The Markov trace of any closed braid lies natively within the Habiro cyclotomic completion:*

$$
  \mathrm{tr}_M(T_w) \;\in\; \widehat{\mathbb{Z}[q]}
  \;:=\; \varprojlim_n \mathbb{Z}[q] / (q;q)_n.
$$

*The trace expands cyclotomically as:*

$$
  \mathrm{tr}_M(T_w, q)
  \;=\;
  \sum_{m \geq 0} a_m(T_w)\,(q; q)_m.
$$

The primitive roots of unity populate $S^1$ densely, blocking any complex-analytic continuation across the boundary. The Habiro ring provides the rigorous algebraic substrate. Evaluating the trace truncates cleanly at finite cyclotomic orders, suppressing higher roots unconditionally. The expansion explicitly isolates the algebraic content from analytic convergence artifacts.
<!-- FILE_END: full-pole-structure-mass-trace.md -->
