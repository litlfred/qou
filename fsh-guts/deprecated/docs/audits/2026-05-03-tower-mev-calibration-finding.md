> **DEPRECATED on 2026-05-24.** Workplan / status snapshot / investigation result / closure-attempt that has been integrated into main or superseded by a later resolution. Original audit preserved here for historical record. See [`docs/audits/INDEX.md`](../INDEX.md) for the tranche rationale.

# 2026-05-03 — Tower-Term MeV Calibration: Finding the Blocker

## Context

Per `2026-05-03-t6-calibration-and-gs-reducer-perf.md`, the T6 → MeV
calibration question is blocked by an upstream issue: the
binding_full pipeline's `tower_MeV` column reports values in the
GeV-to-TeV range for atoms whose experimental binding energy is
single-digit MeV.  This audit identifies the structural source of
that miscalibration.

## Numerical evidence (D, kahler_order=0)

```
canonical (via ω): |tr_atom|=0.388286, |tr_free|=0.983526, B_canon=0.466 MeV
V̂ (free) = [0.665, 1.046, 0.991, 0.547, 1.079]
V̂ (atom) = [0.665, 1.046, 0.000, 0.547, 1.079]
tower_level_1_delta_cat = 3.7536e+06
tower_MeV               = 28 828.85
```

For deuteron the expected B(D) is **2.224 MeV**.  The pipeline's
`B_pred = canonical_MeV + tower_MeV ≈ 28 829 MeV` overshoots by
**13 000×**.

## Root cause — pinpointed

`canonical_plus_multibrane.tower_mass_level(V̂)` computes:

```
desc   = ∏ |V_i|                                                  (product)
single = Σ Φ_q(|V_i|)                                             (single-tower)
cross  = z² · Σ_{i<j} Φ_q(|V_i V_j|)                              (pair-tower)
return desc + single + cross
```

with the calibration

```
tower_MeV = E_0 · ℏ_q² · (m_free − m_atom)
        = 0.782 · 0.00982 · Δ
        = 7.68 × 10⁻³ × Δ MeV per cat unit
```

For D:
- V̂ values 1.046, 1.079 are **above 1** — Φ_q(x) diverges as |x| → 1.
- `phi_q_safe(x, cap_frac=0.98)` caps to 0.98 to avoid divergence.
- Φ_q(0.98) ≈ 10³–10⁴ at q₀.
- `cross` sums (5 choose 2) = 10 pair-Φ_q terms × z² ≈ huge accumulation.
- Net `Δ ≈ 3.75 × 10⁶`, multiplied by 7.7 × 10⁻³ MeV/cat → 28 829 MeV.

The docstring at `canonical_plus_multibrane.py:243` says
"tower_1 ≈ 141 MeV (D)" — this expected magnitude is the calibration
target, but the formula as implemented produces 200× more.

## ⚡ Convergent finding from `claude/categorical-mass-divergence-audit`

While this audit was being written, the parallel branch
`claude/categorical-mass-divergence-audit` (commit `49fe17928`,
"Kashaev integration probe: identity NOT Φ_q AND NOT α·ln|V| — it's
q-dilogarithm") landed a numerical probe that **directly identifies
the wrong function**:

The integration identity claimed in `prop:mass-endomorphism-tower`
(line 117-130) was

  ∫_0^V (ln_q(1+t)/t) dt  ?=  Φ_q(V)

The probe at q₀ = 1.10998, V ∈ (0.1, 0.989), shows:

  V       integral    Φ_q(V)        ratio
  0.10    +0.098      2.54          0.038
  0.50    +0.449      189           0.002
  0.85    +0.717      33 347        2 × 10⁻⁵
  0.989   +0.815      671 093       1 × 10⁻⁶

The integral is **bounded** in [0.1, 0.82] for V ∈ (0, 1) (it's a
q-dilogarithm `Li₂_q(V)`).  Φ_q(V) is unbounded as V → 1.  The
identity is **off by ~10⁶** at the high end and the relationship
isn't even monotonic.

This independently confirms — and pinpoints — Fix C below: the
tower formula's `Φ_q` is the wrong analytic function.  The right
function is `Li₂_q`, which is bounded and so won't drive tower_MeV
into the GeV regime.

Witness: `computations/kashaev-integration-identity.witness.json`
(on `claude/categorical-mass-divergence-audit`, not yet on `main`).

### Follow-up commit (`841cab890`, same audit branch)

The reconciliation across the codebase's existing α·ln|V| formula
and the new Li₂_q identity:

  ∫_0^V (ln_q(1+t)/t) dt  =  -Li_2^q(-V)            ✓ correct
                          ≠  Φ_q(V)                 ✗ wrong by 10⁶

  α · Σ ln|V_i|  is the leading-order expansion of  -Σ Li_2^q(-V_i)

Empirical fit vs AME via `li2q_six_term_probe.py`:

  | atom |  α·Σ ln|V|  |  -Σ Li_2^q(-V)  |
  |------|-----------:|----------------:|
  | p    |    -0.016% |      -0.645%    |
  | n    |    -0.073% |      -0.608%    |
  | D    |    -0.192% |      -0.558%    |
  | T    |    -0.174% |      -0.374%    |
  | ³He  |    -0.071% |      -0.438%    |
  | ⁴He  |    +0.296% |      +0.053%    | ← Li_2^q wins
  | mean |     0.18%  |      0.29%      |

α·ln formula is better on light atoms; Li_2^q is better on ⁴He.
Trend: Li_2^q is expected to win on ⁵Li, ⁶Li (heavier atoms with
|V_i| closer to 1).

### Integration opportunity for this branch

Combining the two findings:
  - **This branch (LaurentQ fast Markov-peel)** → makes ⁵Li, ⁶Li
    symbolic peels tractable for the first time.
  - **The audit branch (Li₂_q identity)** → gives the bounded MeV
    formula that actually predicts B_AME.

The natural cross-product is: run `binding_full` on ⁵Li, ⁶Li using
the Li₂_q formula instead of `tower_mass_level`'s Φ_q chain.  Would
produce the first sub-percent binding-energy predictions for A ≥ 5.

Pending the audit branch's merge into `main`, this branch's wide-
spectrum binding sweep (`binding-full-A5-sweep.witness.json`)
records the *uncalibrated* tower_MeV column, which is empirically
useless.  Recipe for the post-merge follow-up:

  1. Wait for `claude/categorical-mass-divergence-audit` → `main`.
  2. Replace `tower_mass_level`'s Φ_q chain with the Li₂_q sum.
  3. Re-run `binding_full_pipeline.__main__` over A ≤ 6.
  4. Report sub-percent binding-energy table.

## Three candidate fixes (each requires theoretical work)

### Fix A — different summation convention

The current code sums every pair `(i, j)` indiscriminately (`pair_mode = "full"`).
The 2026-04-20 commit changed the default from `"adjacent"` to `"full"`
based on `rem:mass-endomorphism-jet-tower` and
`thm:markov-trace-factorization`, which prescribe *all* pairs at every
level.  But maybe the correct formulation is a different combinatorial
weighting (e.g., per-nucleon-cluster, or per-Wedderburn-block) so the
sum doesn't quadratically explode in atom size.

### Fix B — different calibration constant

If the formula is structurally correct and just needs rescaling,
the right calibration constant is ~10⁻⁹ MeV/cat (rather than
7.7 × 10⁻³).  This would make ΔV̂ × ℏ_q² · α ≈ B (with α set to
match D, then test on T, ³He, ⁴He).  Empirically:

  D:  ΔV̂ = 3.75 × 10⁶,  B_AME = 2.22 MeV → α_D ≈ 5.93 × 10⁻⁷
  
For internal consistency we'd need α_T ≈ α_He3 ≈ α_He4 too, which
the current data doesn't support — see the calibration audit's
"residual/T6" column.  So Fix B alone is insufficient unless coupled
with Fix A.

### Fix C — alternative tower formula

The `desc` (`∏ V_i`) term is suspicious: it's a multiplicative
product of trace values, growing exponentially in atom size.  The
existing prop derivation may not actually require this term; the
docstring at line 113 says "Single-level prop:mass-endomorphism-tower
formula on aggregated V̂" without specifying that `desc` is part
of it.  Try `tower = single + cross` (drop `desc`) and re-measure.

## Recommended next step

1. **Verify the prop:** read `prop:mass-endomorphism-tower` and
   `rem:mass-endomorphism-jet-tower` to determine whether `desc`,
   `single`, and `cross` are each prescribed, or whether the formula
   has been over-specified.
2. **Empirical sweep with Fix C:** drop `desc` from `tower_mass_level`,
   re-run the binding_full sweep on A ≤ 5, see if magnitudes align
   with B_AME.
3. **Resolve the docstring drift:** the "tower_1 ≈ 141 MeV (D)"
   comment in the codebase clearly predates the current state.  Find
   the commit that introduced the discrepancy and reconcile.

## Why this matters for T6

T6 calibration has been "open theoretical work" for a while (per
`six_term_consumer.assemble_ame_comparison`).  This audit shows the
**T6 question is downstream of the tower question**: until the
tower's MeV calibration is correct, the residual `B_AME − B_pred`
is dominated by tower miscalibration, not by genuine T6 contribution.

Once the tower is calibrated, T6 → MeV becomes empirically
determinable from the `B_AME − (canonical + tower)` residual sweep
across atoms.

## Files

This audit is documentation only — no code changes.  The data
points are reproducible via:

```bash
python3 computations/binding_full_pipeline.py \
  > binding_sweep.log 2>&1
```

(takes ~30-90 min for the full kahler_order ∈ {0, 1, 2} × A ≤ 4
spectrum on a single core; ~5-15 min for kahler_order = 0 alone).

A=5,6 atoms now structurally tractable post-LaurentQ (see
`docs/audits/2026-05-03-t6-calibration-and-gs-reducer-perf.md`).
