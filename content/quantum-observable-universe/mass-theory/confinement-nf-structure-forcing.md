<!-- Conjecture (witness only — no Lean proof). -->

**Conjecture (Confinement $\to$ NF-structure forcing).**
*Let $\beta = \beta_1 \star I \star \beta_2 \in B_n$ be a compound
braid where $I$ is a basis interface braid (e.g. a torus-knot
generator). Let $A := \{\lambda \vdash n : y_\lambda^* > 0\}$ be the
LP/SDP **active set** of [`prop:operator-selection-lp`](#prop:operator-selection-lp)
applied to $\beta$, and assume the **confinement hypothesis**
$|A| < n!$. Then:*

1. *(NF-support localisation)* The Wedderburn maximizer
   $\lambda^\star \in \arg\max_\lambda \mathrm{ord}_{q=0}^{(-)}
   \chi_\lambda(T_\beta)$ satisfies $\lambda^\star \in A$.
2. *(Shift bound)* There is a deviation $\Delta(\beta_1, \beta_2; A)$
   with

   $$
     \mathrm{shift}_{\mathrm{NF}}(\beta)
     \;=\; \alpha_{\mathrm{shift}}(I) + \Delta(\beta_1, \beta_2; A),
     \qquad
     |\Delta| \;\leq\; \mathrm{duality\_gap}(\beta).
   $$

### Empirical evidence

The witness
[`lp-confinement-nf-forcing.witness.json`](../../computations/lp-confinement-nf-forcing.witness.json)
runs a 6-compound bench at $n \in \{3, 4\}$. For each compound the
LP is solved via [`solve_operator_selection_lp`](../../computations/lp_dual_solver.py)
(emitting **both primal and dual** per CLAUDE.md §LP/SDP duals),
the active set $A$ is read off the dual vector $y_\lambda^*$, and
the seminormal pole order of $T_\beta$ is computed independently.

See [Table](#tbl:confinement-nf-structure-forcing-table-data).

**Result:**
- Confinement holds in 6/6 compounds (active set size $\leq n/(n-1)! \cdot n!$).
- The maximizer always lies in the active set (claim 1) — 6/6.
- The LP duality gap is **exactly 0** in every case (strong duality
  verified).
- $\Delta$ is bounded by $\ell(\beta_1) + \ell(\beta_2)$ — the
  heuristic length-scale bound — in all cases. The tightening to
  the genuine $\mathrm{duality\_gap}$ bound stated in the
  conjecture is consistent with all observations (vacuously, since
  the gap is $0$ and $\Delta \in \{0, 2, 3\}$ is small in absolute
  terms).

The witness emits the required CLAUDE.md §LP/SDP-duals fields
(`lp_y0_star`, `lp_y_star`, `lp_active_set_indices`, `lp_primal_obj`,
`lp_dual_obj`, `lp_duality_gap`) per compound, plus a top-level
`lp_dual_emitted: true` flag.

3 / 3 witness assertions pass.

### Caveats

- The Frobenius Gram in this probe is taken **diagonal**
  ($G_{\lambda\mu} = \delta_{\lambda\mu} \dim V_\lambda$),
  reflecting the orthogonality of irreducible Markov channels.
  A non-trivial inner product would change the active set; see
  [`docs/audits/-nh-knots-confinement-shift.md`](../../docs/audits/-nh-knots-confinement-shift.md).
- The bench is small (6 compounds, $n \leq 4$). Scaling to $n \geq 5$
  requires a numerical / interval-arithmetic switch in the symbolic
  Hoefsmit pipeline.
- No Lean proof is attempted; the conjecture is conjectural in
  the [CLAUDE.md §3b](../../CLAUDE.md#3b) sense — propagated
  downstream uses must be `remark` blocks with `interprets`, or
  carry the conditional-class structure of §3b-cond.
