**Observation.**  At the cost-coincidence loci of the operator-selection
LP/SDP ([operator selection LP](#prop:operator-selection-lp)) — points
$q^* > 0$ where two cost coefficients $t_i(q)$ and $t_j(q)$ become equal
— the strict-complementarity condition fails and the SDP is
**degenerate**.  These loci coincide exactly with the metallic-ratio
ladder $\{\delta_n : n \in \mathbb{N}^+\}$.

**The mechanism.**  For the n=2 LP with basis $\{\gamma, \sigma_0\}$ of
$H_2(q)$ the cost coefficients are

$$
  t_1(q) \;=\; 2(q + q^{-1}),
  \qquad
  t_2(q) \;=\; q^2 - q^{-2}.
$$

A direct algebraic calculation (Lean-proved sorry-free in
`QOU.AlgebraicSubstrate.MetallicLPIdentities.silver_lp_coincidence`) gives

$$
  t_1(q) \;=\; t_2(q)
  \quad\Longleftrightarrow\quad
  q - q^{-1} \;=\; 2
  \quad\Longleftrightarrow\quad
  q \;=\; \delta_{\rm silver} \;=\; 1 + \sqrt{2}.
$$

At this q, the LP optimum is not a vertex but a **face** of the
feasible polytope: any feasible $x$ satisfying $x_1 + x_2 = n_{\rm target}$
achieves the same primal cost $t_1 x_1 + t_2 x_2 = t_1 \cdot n_{\rm target}$.
The dual shadow prices $y_i^*$ become non-unique (multiple optimal
$(y_0^*, y^*)$ values), strict complementarity fails, and the active set
$\mathcal{A} = \{i : y_i^* > 0\}$ is empty.  This is exactly the
**SDP-degeneracy** signature one would observe by running an
interior-point solver: rapid loss of conditioning, ambiguous
identification of binding constraints, multiple optimal solutions
returned.

**Empirical verification.**  The n=2 LP active-set sweep
(`folio-assistant/computations/two_quark_active_set_mahler_sweep.py`)
observed exactly this signature: below silver the active set was
$\{0\}$ (row 1 tight), AT silver it was $\emptyset$ (degenerate),
above silver it was $\{1\}$ (row 2 tight).  The degeneracy at silver
is the **first non-null result** in a series of five prior numerical
probes that all returned smooth observables.

**Exact-Gram refinement ($n = 3, 4$).**  Replacing the rank-1 Gram
approximation with the exact word-basis Gram
$G_{ij} = \mathrm{tr}_M(b_i b_j)$ on the canonical $T_w$ bases of
$H_3(q)$ and $H_4(q)$ (native Hoefsmit characters; witness
`metallic-q-s4-exact-lp-sweep.witness.json`) sharpens the picture in
two directions.  The cost-coincidence mechanism survives exactly: the
pair $t_\gamma(q) = t_{\sigma_1}(q)$ crosses at $q = \delta_{\rm silver}$
at every strand count tested, with $40$-digit residuals below
$10^{-37}$, and no other metallic ratio appears among the coincidence
loci — so $S(2) = S(3) = S(4) = \{\delta_{\rm silver}\}$ at the
coincidence level.  The active-set transition, however, does not
survive: with the exact Gram the LP active set is constant across the
entire sweep at $n \geq 3$, so the richer active-set flip reported by
the approximate $n=3$ probe was an artifact of the Gram approximation;
only the $n=2$ active-set transition (where the Gram is exact) stands.
The coincidences are also convention-anchored: they appear in the
$q$-Plancherel weight family $y_\lambda = H_q(\lambda)^2/[n]_q!$ of the
proved $n=2$ statement, and disappear under the Markov-normalized
canonical weights.

**Why this matters structurally.**  The metallic-ratio ladder
(see [`docs/audits/2026-06-08-metallic-q-hierarchy-proof.md`](../../../docs/audits/2026-06-08-metallic-q-hierarchy-proof.md)
and Lean module `QOU.AlgebraicSubstrate.MetallicHierarchy`)
sits on the algebraic side: $q = \delta_n$ is exactly where the Hecke scalar
$q - q^{-1}$ takes the integer value $n$, making $\sigma$ satisfy the
integer-coefficient quadratic $\sigma^2 = n \sigma + 1$.  Smooth
observables (Wenzl weights, Jones polynomial signs, n=3 per-block
character signs) do not see this discrete arithmetic structure because
they are rational functions of $q$ with no discontinuities.  The
**LP-vertex combinatorics** does see it: cost-coefficient coincidences
are algebraic events that translate the arithmetic of $q - q^{-1}$ into
a topological change of the optimum's face dimension.

**Physical interpretation.**  Identifying the silver coincidence with
the CFL phase transition of dense quark matter
([color superconductivity Borromean](#conj:color-superconductivity-borromean))
gives the empirical handle on this otherwise abstract algebraic
phenomenon: the CFL transition density $\rho_c$ is the physical
realization of the silver-coincidence point, and the SDP degeneracy
there IS the order-parameter discontinuity of the first-order CFL
transition.  Multiple metallic ratios on the ladder should correspond
to multiple phase transitions; the bar-mirror $\varphi^2 \approx 2.618$
of the deconfinement boundary $q_{\rm gold} = 1/\varphi^2$ is a
candidate for the CFL $\to$ gCFL (gapless / crystalline color
superconductor) boundary observed in dense-QCD phenomenology.

**Generalisation (conditional).**  For the strand-$n$ LP with basis
size $d_n = n!$, the cost coefficients $t_i(q)$ are rational functions
of $q$.  The pairwise coincidence equations $t_i(q) = t_j(q)$ have
rational-function solutions; those solutions that lie on the metallic
ladder constitute the set $S(n) \subseteq \{\delta_k : k \le n\}$ of
LP-degeneracy points for n strands.  For n=2 we have proven $S(2) = \{2\}$
(silver only).  For n=3 and n=4 the exact-Gram probe returns
$\{\delta_{\rm silver}\}$ at the coincidence level ($q$-Plancherel
convention; see the exact-Gram refinement above); the full
higher-strand characterisation is the content of the conditional class
`SDPDegeneracyDetectsMetallic` in `MetallicLPIdentities.lean`.

**Falsifiability handle.**  This remark predicts that running an
SDP solver on the canonical operator-selection problem at q-values
near each metallic ratio should reveal **measurable** signs of
degeneracy: rising condition-number of the KKT system, multiple
optimal solutions reported by the solver, $y_i^*$ values dropping to
tolerance for all $i$ simultaneously.  Each such observation is a
direct test of the algebraic identification.
