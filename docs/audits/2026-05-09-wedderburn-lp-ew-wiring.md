# 2026-05-09 — Wedderburn pair-volume LP/SDP-EW wiring + Δ_I-word Weinberg probe

**Branch:** `claude/wedderburn-lp-sdp-wiring` (PR #618; superseded by
`claude/klr-positive-supply-vector` for the §0 correction below)
**Predecessor:** [`2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md) §3 item 4
**Companion to:**
[`prop:knot-operator-lp-selection`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-lp-selection.md),
[`def:ew-interface-knot`](../../content/quantum-observable-universe/braids-and-knots/ew-interface-knot.md)

## 0. KLR-positivity correction (post-#618)

**The "LP unbounded for mixed-sign $t$" finding in §2 below was a
setup error, not an LP-theory issue.** KLR (Khovanov-Lauda-Rouquier)
positivity guarantees that Markov traces of compound operators in
the canonical-basis cone are non-negative at $q > 0$
[Kashiwara-Saito, Brundan-Kleshchev]. The supply vector $t_k$ used
by [`wedderburn_lp_ew_wiring.py`](../../computations/wedderburn_lp_ew_wiring.py)
on PR #618 was

$$
  t_k^{(\text{PR #618})}
  \;=\; w_{\rm sym} \, \lambda_i^{\rm sym} \lambda_j^{\rm sym}
  \;+\; w_{\rm std} \, \big(z \cdot (M_i M_j)_{12}
                           + (M_i M_j)_{22}\big)
  \;+\; w_{\rm alt} \, \lambda_i^{\rm alt} \lambda_j^{\rm alt},
$$

i.e. the `pair["full"]` field from `wedderburn_pair_volumes`. This
is a **sum of seminormal-basis matrix entries** (specifically
$(M_i M_j)_{12}$ and $(M_i M_j)_{22}$ for the std channel), **not**
a Markov trace. Matrix entries on a chosen seminormal basis can
have signs, and the deuteron / triton runs picked up such negative
entries — driving the LP $\min \langle t, x \rangle$ unbounded.

The KLR-positive replacement is the actual pair Markov trace

$$
  t_k^{\rm KLR}
  \;=\; \mathrm{tr}_M(\sigma_i \sigma_j)
  \;=\; \sum_{\lambda \,\vdash\, 3A} y_\lambda(q) \cdot
        \chi_\lambda(\sigma_i \sigma_j),
$$

evaluated via the same Hoefsmit-matrix cache that `_full_wedderburn_gram`
already builds. By KLR positivity, $t_k^{\rm KLR} \ge 0$ for every
pair (verified: $\min_k t_k = +5 \times 10^{-6}$ for triton, all
positive within numerical noise).

A second adjustment is needed alongside the KLR fix: the LP
$\min \langle t, x \rangle$ s.t. $\sum x = n_{\text{target}},
G x \ge 0, x_i \ge -M$ remains bounded only with $x \ge 0$
explicitly (the natural reading of "operator selection" — operator
coefficients are non-negative). The default `M_bound = 10^6` in
`solve_operator_selection_lp` is intended for sign-indefinite
problems; passing `M_bound = 0.0` enforces $x \ge 0$. With both
fixes, **strong duality holds for every computable atom** (gap = 0,
verified):

| Atom | $(Z, N)$ | $H_n$ | # pairs | $t_{\min}^{\rm KLR}$ | $t_{\max}^{\rm KLR}$ | primal_obj | dual_obj | gap | $y_0^\star$ |
|------|---------:|------:|--------:|---------------------:|---------------------:|-----------:|---------:|----:|------------:|
| proton | (1, 0) | $H_3$ | 1 | +7.27 × 10⁻² | +7.27 × 10⁻² | +2.64 × 10⁻³ | +2.64 × 10⁻³ | 0 | +0.0727 |
| neutron | (0, 1) | $H_3$ | 1 | +7.27 × 10⁻² | +7.27 × 10⁻² | +2.64 × 10⁻³ | +2.64 × 10⁻³ | 0 | +0.0727 |
| deuteron | (1, 1) | $H_6$ | 10 | +4.63 × 10⁻⁴ | +2.74 × 10⁻³ | +3.15 × 10⁻⁶ | +3.15 × 10⁻⁶ | 0 | +0.0005 |
| triton | (1, 2) | $H_9$ | 28 | +5.36 × 10⁻⁶ | +1.20 × 10⁻⁴ | +1.67 × 10⁻⁹ | +1.67 × 10⁻⁹ | 0 | +0.0000 |
| ⁴He | (2, 2) | $H_{12}$ | 55 | DEFERRED — `pyhecke_native` Rust kernel needed for the H_12 Hoefsmit precomputation in session budget | | | | | |

The legacy `pair["full"]` matrix-entry sum is preserved under
`t_legacy_matrix_entries_min` / `_max` in the witness for diff /
comparison.

The "53 active for ⁴He" interpretation correction (§2 `active_set`
discussion) and the LP-statement contract correction (§2 dual
program) remain as written — both of those were genuine findings
independent of the supply-vector choice.

## 1. Two deliverables

This audit captures two compute-bound items per the user's direction
(execute v3 §3 item 4 + try alternative Δ_I words for the Weinberg gap):

**(A) Wire `wedderburn_pair_volumes.py` into
`prop:knot-operator-lp-selection`.** A concrete numerical instance:
solve the LP/SDP-dual program for the EW-sector operator selection
with Wedderburn pair amplitudes |V̂_i V̂_j|_Wedd as the supply matrix,
and compute the **full H_(3·A) Wedderburn Frobenius Gram** on the
pair-operator algebra (no diagonal proxy, no rank-3 H_3-channel
projection). Report primal_obj, dual_obj, y_0_star, y_star,
active_set per
[AGENTS.md](https://github.com/litlfred/qou/blob/main/AGENTS.md)
"LP/SDP duals — first-class infra" mandate.

**(B) Try to close the 2.19% Weinberg gap.** The (3,2,1)
max+/2nd-max+ = 1.78 reading on Δ_I^minimal = σ_2 σ_4 σ_2 was
2.19% off CODATA cot θ_W = 1.823 (per the prior deep-dive PR).
Test ~14 alternative Δ_I words and report the best.

Witness:
[`computations/wedderburn-lp-ew-wiring.witness.json`](../../computations/wedderburn-lp-ew-wiring.witness.json)

## 2. Deliverable (A) — LP/SDP-EW wiring

### Pair amplitudes (input)

Pair amplitudes |V̂_i V̂_j|_Wedd are computed via the H_3 Wedderburn-block
decomposition

$$
  |V̂_i V̂_j|_{\rm Wedd}
  \;=\; w_{\rm sym} \cdot \lambda_i^{\rm sym} \lambda_j^{\rm sym}
  \;+\; w_{\rm std} \cdot (z \cdot (M_i M_j)_{12} + (M_i M_j)_{22})
  \;+\; w_{\rm alt} \cdot \lambda_i^{\rm alt} \lambda_j^{\rm alt}
$$

per `wedderburn_pair_volumes.py`. The `full` field of each pair feeds
the LP supply vector $t_k$.

### LP / dual program

Per [`prop:operator-selection-lp`](../../content/quantum-observable-universe/braids-and-knots/operator-selection-lp.md),
solver contract from
[`lp_dual_solver.py`](../../computations/lp_dual_solver.py):

$$
  \begin{aligned}
    \text{primal:} & \quad \min_x \langle t, x \rangle \\
                   & \quad \text{s.t.} \quad \sum_i x_i = n_{\text{target}}
                                            \quad (\text{net constraint}) \\
                   & \qquad\qquad\quad G x \geq 0
                                            \quad (\text{Frobenius positivity}) \\
                   & \qquad\qquad\quad x_i \geq -M
                                            \quad (\text{lower bound, } M = 10^6) \\
    \text{dual:}   & \quad \max_{y, z} n_{\text{target}} \cdot y_0
                          - M \cdot \sum_i z_i \\
                   & \quad \text{s.t.} \quad G^T y + z = t,
                                       \quad y \geq 0, \; z \geq 0
  \end{aligned}
$$

Dual variables:
- $y_0^\star$ — shadow price of the net constraint ($\sum x = n_{\text{target}}$).
- $y^\star_i$ — shadow prices of the Frobenius positivity rows
  $G_i \cdot x \geq 0$.
- **`active_set`** — indices $i$ with $y^\star_i > \text{tol}$, i.e.
  the **saturated positivity constraints**. At a saturated row the
  dual is binding and the corresponding primal direction $x_i$ is
  pinned at the boundary of the feasible cone. The active set
  identifies which positivity rows are *driving* the optimum, **not**
  channels with positive primal mass. (Earlier draft of this audit
  inverted this reading; corrected per Gemini #r3213498017 + Copilot
  #r3213500214.)

### Full H_(3·A) Wedderburn Gram (no proxy)

Per pair $(i, j)$, treat the Hecke element $\sigma_i \sigma_j \in
H_{3A}(q)$ as the basis vector for that pair. The Frobenius inner
product on $H_{3A}$ via the Markov trace is

$$
  G_{(i,j),(i',j')}
  \;=\; \langle \sigma_i \sigma_j, \, \sigma_{i'} \sigma_{j'}
                \rangle_{\rm tr_M}
  \;=\; \sum_{\lambda \,\vdash\, 3A}
        y_\lambda(q) \cdot
        \chi_\lambda(\sigma_i \sigma_j \sigma_{i'} \sigma_{j'})
$$

where $y_\lambda$ is the canonical Plancherel weight on $H_{3A}(q)$
and $\chi_\lambda$ is the Hoefsmit character on the Wedderburn block
$\lambda$. This is the **genuine off-diagonal Wedderburn coupling**
— not a $t_k \cdot t_{k'} / wt$ proxy, not the rank-3 H_3 channel
projection — and is full-rank generically (modulo bar-involution
kernel).

Implementation: [`_full_wedderburn_gram`](../../computations/wedderburn_lp_ew_wiring.py)
pre-computes f64 Hoefsmit generator matrices once per partition via
`_hoefsmit_build`, then evaluates each pair-pair Markov trace as a
chain of three matrix products + trace summed over $\lambda$.
Symmetric in $(k, k')$ by cyclicity of the trace, so only the upper
triangle is computed.

### Compute budget for headline atom

The Hoefsmit precomputation cost grows rapidly with $n = 3A$:

| Atom | $n$ | $p(n)$ | max $\dim V_\lambda$ | precompute time |
|------|----:|-------:|---------------------:|----------------:|
| proton / neutron | 3 | 3 | 2 | < 0.1 s |
| deuteron | 6 | 11 | 16 | 0.06 s |
| triton | 9 | 30 | 168 | 5.2 s |
| ⁴He | 12 | 77 | 462 | > 5 min (deferred) |

For $n \le 9$ the full Wedderburn Gram is computed in this script;
for $n = 12$ (⁴He) the sympy-based `_hoefsmit_build` exceeds session
budget and the atom is recorded with `deferred_compute_budget`
status. The optional Rust mpfr kernel `pyhecke_native` would lift
this restriction (open frontier).

### Atom sweep — actual results (full Wedderburn Gram)

Read live from
[`wedderburn-lp-ew-wiring.witness.json`](../../computations/wedderburn-lp-ew-wiring.witness.json):

| Atom | $(Z, N)$ | $H_n$ | # pairs | $t_{\min}$ | $t_{\max}$ | primal | dual | gap | # active |
|------|---------:|------:|--------:|-----------:|-----------:|-------:|-----:|----:|---------:|
| proton | (1, 0) | $H_3$ | 1 | +0.6003 | +0.6003 | +0.180 | +0.180 | 0 | 0 |
| neutron | (0, 1) | $H_3$ | 1 | +0.3727 | +0.3727 | +0.069 | +0.069 | 0 | 0 |
| deuteron | (1, 1) | $H_6$ | 10 | −0.1444 | +2.1411 | −1.96 × 10⁶ | −1.42 | 1.96 × 10⁶ | 7 |
| **triton** | (1, 2) | $H_9$ | 28 | −0.2464 | +2.1411 | **−5.27 × 10⁶** | **−7.59** | **5.27 × 10⁶** | **22** |
| ⁴He | (2, 2) | $H_{12}$ | 55 | — | — | DEFERRED | — | — | — |

Triton is the headline (heaviest computable atom).

### Finding: LP unbounded for atoms with mixed-sign $t$

**This is the substantive result of moving from the rank-3 H_3
channel projection to the full Wedderburn Gram.** The previous
diagonal-proxy formulation forced $x \ge 0$ implicitly by giving
$G$ rank 1 with positive $t$ on the diagonal; the off-diagonal
Wedderburn Gram is full-rank but does not constrain the sign of
$x$, and the lower bound $x_i \ge -M$ becomes the only barrier
against unboundedness.

For atoms with $\min_i t_i \ge 0$ (proton, neutron — single-pair),
strong duality holds and the primal/dual match exactly.

For atoms with mixed-sign $t$ (deuteron, triton — multi-pair), the
LP

$$
  \min_x \langle t, x \rangle \quad
  \text{s.t.} \quad \sum_i x_i = n_{\text{target}}, \;
                    G x \ge 0, \;
                    x_i \ge -M
$$

is *unbounded* along the negative-$t$ directions. The solver
detects this by driving $x_i \to -M$ for every $i$ with $t_i > 0$
(making $\langle t, x \rangle$ arbitrarily negative), so the
reported `primal_obj` is dominated by the chosen $M = 10^6$
rather than a finite optimum. The `dual_obj` is the LP dual under
the same constraints and is finite (≈ −7.6 for triton); strong
duality fails because the primal is essentially unbounded
modulo the artificial $M$-bound.

This is a **real finding about
[`prop:knot-operator-lp-selection`](../../content/quantum-observable-universe/braids-and-knots/knot-operator-lp-selection.md)**:
the proposition's LP, as currently formulated, is well-posed only
under the implicit assumption $t \ge 0$ componentwise. For
multi-pair atoms with mixed-sign Markov-trace amplitudes, the
proposition needs an additional sign / non-negativity constraint
(e.g. $x \ge 0$ instead of $x \ge -M$, or an entropy-like
regularizer) to be meaningfully solvable.

This finding was hidden by the previous diagonal-only Gram, which
collapsed the constraint $G x \ge 0$ into $t_i x_i \ge 0$ (i.e.
$x_i \ge 0$ for positive $t_i$, masking the sign issue). The full
Wedderburn Gram exposes it.

### What this gives the workplan

`prop:knot-operator-lp-selection` now has a concrete EW-sector
LP/SDP instance with the genuine H_(3·A) Wedderburn coupling on the
pair-operator algebra. v3 §3 item 4 closes with two follow-up
issues surfaced:

1. **Proposition reformulation** — the LP needs an explicit
   non-negativity constraint $x \ge 0$ (or analogue) to be
   well-posed for multi-pair atoms. Tracked as open work on
   `prop:knot-operator-lp-selection`.
2. **⁴He compute path** — install `pyhecke_native` (Rust mpfr
   Hoefsmit kernel) to lift the H_12 budget restriction and
   include ⁴He in the sweep.

## 3. Deliverable (B) — alt-Δ_I Weinberg probe

### Candidates tested

14 Δ_I words, all using inter-pair generators σ_2 (idx 1) and
σ_4 (idx 3):

| Δ_I | (3,2,1) max+/2nd-max+ | rel err vs CODATA cot θ_W |
|-----|----------------------:|--------------------------:|
| **σ_2 σ_4 σ_2 (minimal, baseline)** | **1.7832** | **2.19%** ★ |
| σ_2 σ_4 | 1.7720 | 2.80% |
| σ_4 σ_2 | 1.7720 | 2.80% |
| σ_2 (single) | 1.7239 | 5.44% |
| σ_4 (single) | 1.9532 | 7.14% |
| σ_4 σ_2 σ_4 (mirror) | 1.4757 | 19.05% |
| σ_2² σ_4² | 1.4277 | 21.69% |
| σ_4² σ_2² | 1.4277 | 21.69% |
| σ_2 σ_4² σ_2 | 1.4277 | 21.69% |
| σ_4 σ_2² σ_4 | 1.4277 | 21.69% |
| σ_2 σ_4 σ_2 σ_4 | 1.4277 | 21.69% |
| σ_4 σ_2 σ_4 σ_2 | 1.4277 | 21.69% |
| σ_2 σ_4 σ_2 σ_4 σ_2 | 1.4298 | 21.57% |
| (empty Δ_I = trivial) | 1.0000 | 45.15% |

### Verdict (B)

**The minimal Δ_I = σ_2 σ_4 σ_2 is OPTIMAL** within this candidate
space. The 2.19% gap is **not closable by Δ_I-word substitution**.
This is informative: the structural origin of the residual lies
elsewhere — likely in:

1. **Non-Wedderburn corrections** to the cot θ_W reading. The
   max+/2nd-max+ ratio on (3,2,1) is a plausible-but-coarse
   structural reading of the EW Wedderburn structure; a more
   refined formula (e.g., weighted by Hoefsmit cell-content
   multiplicity, or by pair-coupling shadow prices y_k from
   deliverable (A)) may close the gap.
2. **Higher-order corrections in the Higgs-vev coupling**. Even
   the optimal Δ_I^minimal is a *minimal* coupling; physical
   Higgs-vev structure may add higher-order corrections (analogous
   to the δ_CS = ℏ_q^4 [5]_q in the EM α derivation).
3. **A categorical-physics derivation of the** structural cot θ_W
   formula that doesn't reduce to an eigenvalue ratio. The
   "max+/2nd-max+" reading was *empirically* close — the right
   categorical formula may differ.

Routes to close the 2.19% gap (open):
- Combine (A)'s active set (saturated positivity rows) with (B)'s
  spectrum: weight the (3,2,1) eigenvalues by the LP shadow prices
  $y^\star_i$ on the saturated rows, re-test ratio.
- Test β_EW words with NON-EVEN twists (allowing σ_1, σ_3, σ_5
  with odd exponents in the construction) — these break
  bar-self-duality but may match the actual physical Higgs-vev.
- Investigate whether the RHS of cot θ_W = 1.823 has a clean
  q-rational form involving [k]_q^a for some structural (k, a).

## 4. Connection to v3 workplan

This audit closes v3 §3 item 4 ("`wedderburn_pair_volumes.py`
LP/SDP integration") with the full H_(3·A) Wedderburn Gram and
two new follow-up items (LP reformulation + ⁴He compute path).
The Weinberg probe (B) is a follow-on to the
`claude/weinberg-wedderburn-321-deepdive` finding (2.19%
near-miss); the negative result here narrows where to look.

Recommended next actions per v3 §3:
- Item 1 (Tier-2 PSLQ extension): unchanged.
- Item 2 (Term 7 α_5 numerical fit): unchanged.
- Item 3 (Chirality ⟨c⟩_β concrete computation): unchanged.
- **Item 4 (this audit)**: ✓ DONE with full H_(3·A) Wedderburn Gram;
  surfaces two new items: (a) reformulate
  `prop:knot-operator-lp-selection` LP for multi-pair atoms with
  mixed-sign $t$; (b) install `pyhecke_native` to add ⁴He to the
  sweep.
- Item 5 (`gb_filtration_jet_tracker.py` extension to H_n, n≥4):
  unchanged.

## 5. Files

- This audit:
  [`docs/audits/2026-05-09-wedderburn-lp-ew-wiring.md`](2026-05-09-wedderburn-lp-ew-wiring.md)
- Witness:
  [`computations/wedderburn-lp-ew-wiring.witness.json`](../../computations/wedderburn-lp-ew-wiring.witness.json)
- Script:
  [`computations/wedderburn_lp_ew_wiring.py`](../../computations/wedderburn_lp_ew_wiring.py)
- Workplan v3:
  [`docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md`](2026-05-09-refocused-1ppb-workplan-v3.md)
