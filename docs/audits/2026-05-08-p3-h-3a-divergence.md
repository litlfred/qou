# P3 (1 ppb workplan): H_3 → H_{3A} Jones-Markov weight divergence

**Date:** 2026-05-08
**Branch:** `claude/hecke-nf-followups` (PR #572)
**Scope:** Quantify the divergence between the legacy **H_3
shortcut** and the **H_{3A} Jones-Markov formulation** required by
`prop:atomic-mass-gb-nf`. P3 in the [1 ppb workplan](../coordination/1ppb.md).

**Author note (2026-05-08, post-review correction):** the first
draft of this audit used `hecke_3a_weights.wedderburn_weights_3a`
which returns the **symmetric Plancherel** weight
$w_\lambda = d_q(\lambda)^2 / [n]_q!$. Per
[`markov_weights_symbolic.py:18-23`](../../computations/markov/markov_weights_symbolic.py),
that is **NOT** the correct Jones-Markov weight $y_\lambda(q)$
for $q \neq 1$; they coincide only at the classical Plancherel
point $q = 1$. The QOU paper at $q = q_0 \approx 1.1098$
**requires** $y_\lambda$ via Wenzl's Schur principal
specialization. This audit now uses the correct $y_\lambda$.

**Witness:** [`h-3a-vs-h-3-divergence.witness.json`](../../computations/h-3a-vs-h-3-divergence.witness.json)
— 9 / 9 assertions pass.

## Methodology

Each $y_\lambda(q)$ computed via
[`markov_weights_symbolic.schur_principal_symbolic`](../../computations/markov/markov_weights_symbolic.py)
with **numerical-q-from-start** — substitutes $q = q_0$ before
the symbolic `sp.cancel` step that was the bottleneck in naive
`solve_y_lambda(n)`. Timings:

| n | partitions | time (numerical-q-from-start) | (symbolic-throughout, comparison) |
|---:|---:|---:|---:|
| 3 | 3 | 0.18 s | < 1 s |
| 6 | 11 | 3.80 s | > 60 s |
| 9 | 30 | 62.98 s | infeasible |
| 12 | 77 | (~150–300 s, deferred) | infeasible |

The "symbolic Wenzl is too slow" framing in this audit's earlier
draft was a 30-s-timeout artefact, not algorithmic. With
numerical-q-from-start, n = 3, 6, 9 all complete in-session;
n = 12 is borderline (deferred to follow-up).

## Result: Σ y_λ(q_0) per atom

| Atom | $A$ | $n = 3A$ | $p(n)$ partitions | $\sum_\lambda y_\lambda(q_0)$ | Divergence vs H_3 |
|---|---:|---:|---:|---:|---:|
| p, n | 1 | 3 | 3 | **0.7191** | (anchor) |
| D | 2 | 6 | 11 | **0.1898** | **−73.60%** |
| T, ³He | 3 | 9 | 30 | **0.0318** | **−95.58%** |
| ⁴He | 4 | 12 | 77 | (deferred — ~150–300 s) | (extrapolate) |

The Jones-Markov $\sum y_\lambda$ **collapses fast with $n$** because
the normalisation involves $[n]_q!$ which grows super-exponentially.
This is structurally correct — the H_3 shortcut overstates each
atom's weight by an order of magnitude or more.

**The legacy H_3 shortcut is therefore wrong for D by 73.6%, for
T / ³He by 95.6%, and growing for heavier atoms.**

## Top y_λ(q_0) at each n

**H_3 (n = 3):**

| λ | y_λ(q_0) |
|---|---:|
| (3) | 0.4156 |
| (2, 1) | 0.2809 |
| (1, 1, 1) | 0.0227 |

**H_6 (n = 6):** dominant partition shifts to mid-shape (per the
`h_6_jones_markov_table_at_q0` field in the witness). The
column-rich (1^6) sign rep is now severely suppressed — consistent
with the audit's Step 5 prediction (column-pole maximizer for the
*pole order* claim, but column λ has tiny $y_\lambda$ at $q_0$).

## Audit-side finding: same wrong-weight pattern elsewhere

The user flagged "are you using proper weights? not symmetric see
paper". Surveying `computations/`:

| File | Function | Formula | Verdict |
|---|---|---|---|
| `markov_weights_symbolic.py` | `solve_y_lambda(n)` | Wenzl/Jones-Markov via Schur principal specialization | ✅ **canonical y_λ** |
| `hecke_3a_weights.py` | `wedderburn_weight(shape)` | $d_q(\lambda)^2 / [n]_q!$ | ❌ **symmetric Plancherel — wrong for q ≠ 1** |
| `paper_six_term_shadow_price_sweep.py` | `w_lambda(shape, q, n)` | $d_q(\lambda)^2 / [n]_q!$ | ❌ same — symmetric Plancherel |
| `schur_weyl_symbolic.py` | `schur_weyl_weight(partition, q)` | $s_\lambda(q, q^{-1}) / H_q(\lambda)$ | ❌ **2-variable Schur — vanishes for ≥ 3-row partitions** |
| `light_isotope_sweep.py` | `convention="wenzl-schur"` | reads cached `y_λ` from witness | ✅ **correct (when convention is set)** |
| `light_isotope_sweep.py` | `convention="plancherel"` | symmetric Plancherel | ⚠️ **opt-in to wrong** |

### Critical consumer impact

`crt_markov.py` (still imported by live mass-table code) calls
`schur_weyl_symbolic.global_wedderburn_sum_symbolic`, which uses
`schur_weyl_weight` — the **2-variable Schur** formula that
vanishes for partitions with > 2 rows. This is **worse than just
the symmetric-Plancherel substitution** because it actively drops
contributions from $(1, 1, 1)$, $(2, 1, 1)$, etc. — including the
sign-rep $(1^p)$ that `prop:alpha-shift-torus-knot` identifies as
the **maximizer of the pole order**.

`atomic_braid_mass_table.py` is **not** affected by this — it
uses `markov_trace_recursive.markov_trace_of_word` directly
(Markov-axiom recursive ascent), which produces correct $\mathrm{tr}_M$
without going through the partition-sum formula. The wiring path
`atomic_braid_mass_table.py → markov_trace_recursive` is correct.

The wiring path `crt_markov.py → schur_weyl_symbolic → schur_weyl_weight`
is the one that needs fixing.

## Implications for `atomic_mass_via_rho_k.py`

Per the [ρ_K mass-table audit](2026-05-08-rho-k-mass-table-audit.md),
the rho-k path achieves 0.23% MAE on D / T / ³He using
`markov_trace_recursive` (correct path). The 0.23% is therefore
**unaffected by the wrong-weight bug** documented here. P3 wiring
to fix `crt_markov.py` would not improve `atomic_mass_via_rho_k.py`
directly; instead it would fix the legacy `crt_markov.py` consumers
that haven't migrated to the rho-k path.

## Cross-check finding (2026-05-08, post-wiring): residual gap is q=1 character limit

After wiring `crt_markov.py` to use `wedderburn_jones_markov.global_wedderburn_sum_jones_markov`
(commit [`ac7880c5`](https://github.com/litlfred/qou/pull/572/commits/ac7880c5)),
ran [`tr_m_jones_markov_cross_check.py`](../../computations/tr_m_jones_markov_cross_check.py)
against the canonical reducer (`markov_trace_recursive` →
`atomic-tr-m-mpfr-50dps.witness.json`):

| Atom | canonical |tr_M| | Jones-Markov sum | rel err |
|---|---:|---:|---:|
| proton | 1.0653 | 0.4154 | 61% |
| neutron | 0.9232 | 0.4154 | 55% |
| deuteron | 0.3883 | 0.0733 | 81% |

**The new path is closer to the legacy 2-var-Schur path than to
the canonical reducer.** Diagnosis: this is **not** a y_λ bug. The
remaining discrepancy is the **q=1 classical-character limit**
baked into `specht_character_atomic` (used by both legacy and new
partition-sum paths). Per `schur_weyl_symbolic.py:182-186`, the
file is explicit:

> "The q=1 limit of the Hecke character is still implicit;
> full q-deformation is a separate refinement (q-ribbon-tableau
> weights)."

The partition-sum formula

$$
  \mathrm{tr}_M(\beta) \;=\; \sum_\lambda y_\lambda(q)\,\chi^\lambda_q(\beta)
$$

requires the **q-deformed Hecke character** $\chi^\lambda_q$. The
current `specht_character_atomic` returns the **classical
Murnaghan–Nakayama** character $\chi^\lambda_{\mathrm{MN}}(\pi(\beta))$,
which is the q=1 limit. The y_λ weight fix removes the 2-var-Schur
drop-out (≥3-row partitions); the residual is the character.

**Implication for the wiring fix:** the y_λ correction is *necessary
but not sufficient* — without q-Hecke characters, both legacy and
new paths give a Σ that approximates tr_M only at q=1. For the
QOU paper at q=q_0, the canonical-reducer route
(`markov_trace_recursive`) remains the correct integration path.

**Status of partition-sum path consumers:**

- `crt_markov.py` — wired to new path; produces y_λ-corrected sum, but
  remains q=1-character-limited until a follow-up refinement.
- `gb_residue_tower.py`, `canonical_tr_m_three_path_comparison.py` —
  reference but don't actively call.
- `habiro_residue_symbolic.py` — wired to new path (commit on this PR).

**Status of canonical-reducer consumers (unaffected):**

- `atomic_braid_mass_table.py` → `markov_trace_recursive` — correct path; 0.23% MAE on D/T/³He stands.
- `atomic_mass_via_rho_k.py` (PR #564) → `markov_trace_recursive` — same.

The fix in this PR therefore:
- ✅ removes the weight bug (`schur_weyl_weight` 2-var-Schur drop-out)
- ❌ does NOT close the partition-sum path's q=1 character gap
- ✅ documents the gap explicitly so future consumers don't re-stumble

The character refinement is **research-grade follow-up** (q-ribbon-tableau weights, or direct seminormal-Hoefsmit character evaluation at q_0).

## What this PR does NOT do

- **Does NOT modify** `crt_markov.py` — the wiring fix belongs in
  a follow-up that migrates `crt_markov.py` from
  `schur_weyl_weight` (wrong, 2-var Schur) to
  `markov_weights_symbolic.solve_y_lambda` (correct, Jones-Markov).
- **Does NOT modify** `paper_six_term_shadow_price_sweep.py` —
  same fix, separate consumer.
- **Does NOT modify** `hecke_3a_weights.py` — the symmetric
  Plancherel formula it implements is correct *as the symmetric
  Plancherel weight*; the issue is callers using it for
  Markov-trace assembly. A docstring warning would help; the
  function itself is fine.
- **Does NOT extend** the witness to A = 4 (⁴He, n = 12, 77
  partitions, ~150–300 s). Feasible via numerical-q-from-start but
  too long for interactive session.

## What this PR DOES do

- ✅ Computes correct Jones-Markov $y_\lambda(q_0)$ for $n \in \{3, 6, 9\}$
  via numerical-q-from-start (resolves the "Wenzl too slow" framing).
- ✅ Quantifies the H_3 → H_{3A} divergence: −73.6% at D, −95.6% at
  T / ³He.
- ✅ Audits compute infra: identifies three wrong-weight
  formulas in active use (`hecke_3a_weights`, `paper_six_term_*`,
  `schur_weyl_symbolic`).
- ✅ Identifies the **most critical consumer** (`crt_markov.py` →
  `schur_weyl_weight`, which truncates to 2-row partitions and
  drops the sign-rep contribution).

## Recommended owner

**#564** — owns the `crt_markov.py` consumer side. Recommended
follow-up:

1. In `crt_markov.py`, replace
   `from schur_weyl_symbolic import global_wedderburn_sum_symbolic`
   with a call to a **new** `wedderburn_sum_jones_markov(A, q, char_kind, ...)`
   that uses `markov_weights_symbolic.solve_y_lambda(3*A)` for
   weights.
2. Add a numerical-q-from-start path for n ≥ 6 to keep CI fast.
3. Re-run `atomic_mass_via_rho_k.py` (no change expected since it
   doesn't use this path) and any other downstream consumers.
4. Add docstring warnings to `hecke_3a_weights.wedderburn_weight`
   and `paper_six_term_shadow_price_sweep.w_lambda` flagging that
   they are **symmetric Plancherel only**, NOT Markov-trace
   weights.

## Cross-references

- [`prop:atomic-mass-gb-nf`](../../content/quantum-observable-universe/braids-and-knots/atomic-mass-gb-nf.md) — defines the H_{3A} mass formula
- [`prop:per-nucleon-shift-additive-linearity`](../../content/quantum-observable-universe/braids-and-knots/per-nucleon-shift-additive-linearity.md)
- [`docs/audits/2026-05-08-rho-k-mass-table-audit.md`](2026-05-08-rho-k-mass-table-audit.md) — pre-P3 baseline (0.23% MAE)
- [`computations/markov/markov_weights_symbolic.py`](../../computations/markov/markov_weights_symbolic.py) — canonical y_λ
- [`computations/schur_weyl_symbolic.py`](../../computations/schur_weyl_symbolic.py) — wrong-weight site
- [`docs/coordination/1ppb.md`](../coordination/1ppb.md) — P3 in workplan
