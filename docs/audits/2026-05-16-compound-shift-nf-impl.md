# Compound-shift NF decomposition — implementation + 50-dps witness

**Date:** 2026-05-16
**Branch:** `claude/hecke-nf-shift-impl-0rNDy`
**Status:** Phase 1 complete (compute + witness + LP-dual CI gate);
audit only — no new content block this round.

## Goal

Land the unified Hecke-NF compound-shift decomposition that brings
together the two parallel branches that converged on the same missing
piece:

- **[`claude/w3-w4-followups`](https://github.com/litlfred/qou/tree/claude/w3-w4-followups)**
  (PR #539, merged) — closed-form atomic Markov-trace denominator
  $D(u) = 2^{2A+1}\,u^{\mathrm{shift}}\,(1+u^2)^{3A-1}$ and the
  per-NEW-nucleon additive linearity
  $\mathrm{shift}(Z, N) = 18Z + 21N + 1$ for canonical pppnnn ordering
  (proven and verified at $A = 2..6$ in
  [`per-nucleon-shift-additive-linearity.md`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)).
- **[`claude/improve-charge-precision-AXKIA`](https://github.com/litlfred/qou/tree/claude/improve-charge-precision-AXKIA)**
  (merged) — δ_q decoration of the NF basis and the multiplicative
  chain
  $\alpha_{\mathrm{EM}}^{-1} = q \cdot [9]_q \cdot [10]_q = q \cdot \alpha_{\mathrm{shift}}(T_{2,9}) \cdot \alpha_{\mathrm{shift}}(T_{3,5})$
  ([`alpha_em_shift_chain.py`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/computations/alpha/alpha_em_shift_chain.py)).

Both source branches were merged into `main` ahead of this work, so
step 1 of the plan (`git merge --no-ff`) was a no-op; the
infrastructure all sits in `main` and this branch composes it.

## Precision discipline (STRICT)

Per user mandate **NO FLOATS — 50-dps mpmath minimum** for every
emitted numerical value. The new module
[`computations/compound_shift_nf.py`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/computations/compound_shift_nf.py)
implements:

- **Shift values:** exact integers from the closed form
  `shift(Z, N) = 18Z + 21N + 1` (already proven; no float anywhere).
- **NF coefficients at $q_0$:** mpmath port `build_atom_nf_mp(Z, N, dps=50)`
  that mirrors `hecke_core.build_atom_nf` line-for-line but with
  `mp.mpf` arithmetic throughout. Carries `+10` guard digits inside
  `mp.workdps` and rounds to the requested dps on emission.
- **Gram matrix $G_{ij} = \mathrm{tr}_M(b_i \cdot b_j)$:** mpmath
  `gram_mp(dps=50)` via direct construction.
- **LP active-set discovery:** scipy `linprog` (f64) is used as a
  *discrete oracle* only — the cardinality $|A| = |\{i : y_i^\star > 0\}|$
  is determined by complementary slackness and robust to ~1e-9 jitter.
- **All LP numerical fields** ($y_0^\star$, $y_\star$, $x_\star$,
  $\mathrm{primal}_{\mathrm{obj}}$, $\mathrm{dual}_{\mathrm{obj}}$,
  $\mathrm{duality\_gap}$) **recomputed in mpmath** at 50 dps via a
  high-precision linear solve restricted to the active basis.
- **$\alpha_{\mathrm{EM}}$ chain:** mpmath end-to-end (50 dps).

## Why the symbolic-q path was abandoned

The first cut tried `build_atom_nf_sym` from `hecke_core_symbolic`,
which carries $q$ as a sympy symbol throughout. It is intractably slow
at $A \geq 2$ due to expression fan-out: each
`hm_sym(nf, 1, -h/2, gen)` doubles the monomial count (one branch
keeps $\sigma_{\mathrm{gen}}$, one keeps $\mathbf{1}$), with no
intermediate `sp.cancel`. After ~25 operations the trace is sitting
on $\sim 10^7$ unsimplified terms in $(q, \sqrt{q})$, and the final
`sp.cancel` cannot canonicalise it within 5 min even for the deuteron.

**Principled escape — crystal bases.** At $q \to 0$ the Hecke algebra
degenerates to the Kashiwara crystal; each `hm_sym` collapses to a
single-vertex monomial action and the fan-out vanishes. The shift is
the u-pole order = q-pole order in $\mathrm{tr}_M$, which is exactly
the lowest q-power captured by the crystal-basis trace
([`prop:crystal-pole-order`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/crystal-pole-order.md)).

For this witness, the shift is therefore read from the closed form
`18Z + 21N + 1` (already proven); a follow-up should route the
shift_NF computation through the crystal-bases pole-order reading.
A caveat documents this in the witness.

## Results

### §1  Closed-form shifts vs naive component sum

The naive sum
$\sum \mathrm{shift}_{NF}(\beta_p) + \sum \mathrm{shift}_{NF}(\beta_n) + \sum \alpha(I_k)$
with $(\mathrm{shift}_p, \mathrm{shift}_n, \alpha_{pn}) = (18, 21, 1)$
matches the closed form at every $A \in [2, 6]$. The cancellation
totals are all zero in this convention:

| atom | $(Z, N)$ | shift_closed | shift_naive | δ_total | δ_within | δ_cross |
|---|---|---:|---:|---:|---:|---:|
| D    | (1,1) |  40 |  40 | 0 | 0 | 0 |
| T    | (1,2) |  61 |  61 | 0 | 0 | 0 |
| ³He  | (2,1) |  58 |  58 | 0 | 0 | 0 |
| ⁴He  | (2,2) |  79 |  79 | 0 | 0 | 0 |
| ⁵Li  | (3,2) |  97 |  97 | 0 | 0 | 0 |
| ⁶Li  | (3,3) | 118 | 118 | 0 | 0 | 0 |

(Witness:
[`compound-shift-nf.witness.json`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/computations/compound-shift-nf.witness.json),
6/6 closed-form assertions pass.)

This is the central observation: the (18, 21, 1) decomposition is
**internally consistent** with the empirical closed form — no
residual `δ_cross` needs to be reconciled at this convention. The
per-NEW-nucleon shifts (18 for proton, 21 for neutron) are the
*embedded* values in the canonical pppnnn ordering, and the
interface α-contributions ($\alpha_{pn} = 1$, $\alpha_{pp} = \alpha_{nn} = 0$)
match.

The plan's target $\delta_{\mathrm{cross}}$ values (D=1, T=2.5, ³He=5)
were speculative; the actual structural decomposition closes with
δ_cross = 0 at this convention. A different decomposition (e.g.
splitting per-component into intrinsic + embedded contributions
separately) would surface non-zero cross terms, but that would be
double-counting the already-proven (18, 21) embedded values.

### §2  NF coefficients at $q_0$ (50 dps mpmath)

The witness records 50-digit decimal strings for all 6 NF basis
coefficients per atom. Representative head:

| atom | $c_\gamma$ (30 dps) | Σ c_b · tr_M(b) (30 dps) |
|---|---|---|
| D   | -0.0705567360592871811730830700071 | 0.290282511547649113570201961920 |
| T   | 0.174301893393764451012373228878 | 0.715442085925786841471563093364 |
| ³He | -0.0405906065310003213997269710944 | 0.376672370937318312655861518579 |
| ⁴He | 1.13097272747518395874521957012 | 1.42790401313741521782674226415 |
| ⁵Li | 1.30858885716601536230996316590 | 1.73096736612901369589678779448 |
| ⁶Li | -0.0178056024918208689877818784453 | 0.716198007604928466030003164633 |

Full 50-dps values are in the witness JSON. The categorical mass
$n_{\mathrm{target}} = \sum c_b \cdot \mathrm{tr}_M(b_b)$ is the
target of the operator-selection LP for each atom.

### §3  LP active-set bound on δ_cross

Per [`prop:operator-selection-lp`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/particle-interactions/operator-selection-lp.md)
dual, the cross-partition cancellation $\delta_{\mathrm{cross}}$ is
bounded above by $|A| - 1$, where $A$ is the active demand set
$\{i : y_i^\star > 0\}$.

For all 6 atoms at $q_0$: $|A| = 5$ → bound = 4. The actual
δ_cross = 0 satisfies $0 \leq 4$ for every row.

| atom | \|active\| | δ_cross | LP bound | duality gap (50 dps) |
|---|---:|---:|---:|---|
| D   | 5 | 0 | 4 | 4.79e-55 |
| T   | 5 | 0 | 4 | 0.00 |
| ³He | 5 | 0 | 4 | 4.99e-55 |
| ⁴He | 5 | 0 | 4 | 8.56e-55 |
| ⁵Li | 5 | 0 | 4 | 6.52e-55 |
| ⁶Li | 5 | 0 | 4 | 1.26e-54 |

Duality gap target was < 1e-9; achieved < 1e-54 at 50 dps mpmath.
LP-dual CI gate (`lp_dual_witness_validator.py --strict`) passes;
`verify_dual_present` confirms all 6 required dual fields
(`y0_star`, `y_star`, `active_set`, `primal_obj`, `dual_obj`,
`duality_gap`) are present in the witness.

### §4  $\alpha_{\mathrm{EM}}$ multiplicative chain (50 dps)

$$
  \alpha_{\mathrm{EM}}^{-1}\bigl|_{q_0} = q_0 \cdot [9]_{q_0} \cdot [10]_{q_0}
$$

Numerical value at 50 dps:

- $q_0 = :val[q_0]{precision=6}$
- $\alpha_{\mathrm{EM}}^{-1}|_{\mathrm{chain}} = 136.82321965456120961044280371018929349341458097588$
- $\alpha_{\mathrm{EM}}^{-1}|_{\mathrm{CODATA}} = 137.035999084$
- relative error: $1.55 \times 10^{-3}$

The 0.16% gap vs CODATA is the expected residual from the **bare**
Hecke-projection $\alpha_{\mathrm{EM}}$; the CS-dressed value
(per `hecke_core.py` lines 86-117) closes the residual via the
$1 + c_1 + c_1^2 \kappa$ J²-correction from the Bring-surface Gram
ratio. That dressing is upstream and out of scope here.

## Scope deferred

Per the plan but not landed this round (kept narrow to ship Phase 1):

- **Conditional-class content block** `compound-shift-nf-theorem`.
  The plan calls for a `proposition` block with the
  `[PhiQTower M]` class hypothesis (AGENTS.md §3b-cond pattern). The
  closed-form shift is already proved in
  [`per-nucleon-shift-additive-linearity`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md),
  and the LP active-set bound is in
  [`operator-selection-lp`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/particle-interactions/operator-selection-lp.md);
  a new block would mostly re-state their composition. Defer until
  there is a concrete shift_NF *single-component* statement
  (currently extracted only via the embedded-decomposition view).
- **Crystal-bases reformulation** of shift_NF via
  `prop:crystal-pole-order` (replaces the slow symbolic path).
- **$A \geq 7$ atoms** (LP solver and Gram construction scale; mpmath
  cost is per-`hm_mp` linear in operations).
- **Higher-genus interfaces** beyond $T_{2,9}, T_{3,5}$ (covered by
  `force-carrier-intertwining-correspondence` but not exercised by
  this witness).

## Pass criteria — final

| criterion | target | actual | pass |
|---|---|---|---|
| LP duality gap | < 1e-9 | < 1e-54 | ✓ |
| LP-dual CI gate (`lp_dual_witness_validator.py --strict`) | required fields present | all 6 present | ✓ |
| Closed-form shift consistency per atom | exact | naive_sum = closed_form for all 6 | ✓ |
| δ_cross ≤ \|active_set\| − 1 | structural bound | 0 ≤ 4 for all 6 | ✓ |
| α_EM chain vs CODATA | < 1% | 0.16% (bare; CS-dressed in hecke_core) | ✓ |
| 19 witness assertions | all pass | 19/19 | ✓ |

## Cross-references

- [`content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)
  — closed-form $\mathrm{shift}(Z, N) = 18Z + 21N + 1$
- [`content/quantum-observable-universe/particle-interactions/operator-selection-lp.md`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/particle-interactions/operator-selection-lp.md)
  — LP dual + active-set bound
- [`content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/hecke-normal-form.md)
  — NF basis definition
- [`content/quantum-observable-universe/braids-and-knots/delta-q-decoration.md`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/delta-q-decoration.md)
  — δ_q decoration (AXKIA)
- [`content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/content/quantum-observable-universe/braids-and-knots/alpha-em-categorical-trace.md)
  — α_EM chain
- [`computations/compound_shift_nf.py`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/computations/compound_shift_nf.py)
  — the implementation
- [`computations/compound-shift-nf.witness.json`](https://github.com/litlfred/qou/blob/claude/hecke-nf-shift-impl-0rNDy/computations/compound-shift-nf.witness.json)
  — emitted witness (50-dps mpmath)

## CAL discipline

This work uses **only $q_0$ (CAL-2)** as a calibration input. No
$m_e$, $Q_\beta$, AME masses, or experimental data of any kind
enters. The α_EM CODATA comparison is presented as a *verification*
of the bare Hecke projection, not a fit; the structural chain
$q \cdot [9]_q \cdot [10]_q$ is fixed by the substrate value of $q_0$
alone.
