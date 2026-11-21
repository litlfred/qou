# Float64 engine refactor plan (2026-11-21)

Epic N4, precision and calibration. Branch `claude/f64-cast-batch1-2026-11-21`,
PR #8856, issue #8855.

## Where things stand

`computations/f64_into_mpmath_audit.py --tier F64_CAST`, run on this branch:

| | before (main) | after (this branch) |
|---|---|---|
| files | 98 | **86** |
| sites | 180 | **162** |

Fixed so far (each one re-run, with the digits that moved reported in its commit):
nine producers in batch 1, the ³He combiner check, the T₂/T₃ brane tower, and
two symbolic producers that used a 16-digit truncation of q₀.

The ³He combiner (`wenzl_a3_combiner_end_to_end.py`) was not only a precision
issue. Its "true" side used the colour-blind interface σ₅ − h/2, while the
combiner uses the colour-weighted σ₅ − h(1/2 − δ/4). Every checked partition
missed by 3e-5 to 3e-4, and the script exited 1 while its docstring said the
check passed. With the interface read from the word itself, the worst residual is
4.8e-50 on all 8 partitions of dimension ≤ 28 that the script can reach, and it
exits 0 (full run, 24 min). The other 22 partitions are still out of reach in
Python, so the full tr_M(³He) assembly is still not done.

## What the remaining 86 files are made of

Each file is counted once per engine it imports, so the columns overlap.

| engine | files | is there a full-precision twin? |
|---|---|---|
| numpy (dense float arrays) | 57 | yes, `mp.matrix` (slow above dim ~100) |
| scipy / cvxpy (LP, SDP, sparse) | 30 | partly: `lp_dual_solver` (Clarabel is float64 by nature) |
| float seminormal rep (`build_seminormal_matrices`, `chi_lambda_of_word`) | 18 | **yes**: `a_operator_categorical.exact_seminormal_matrices` (MPFR) |
| `pyhecke.gram` (float by design, bit-stable) | 15 | **yes**: `h_mp`, `z_mp`, `tr_m_mp`, `gram_matrix_mp` |
| `pyhecke_native` float entry | 10 | **yes**: the `_mpfr` entry points, 10-30× slower |
| `BlockCache` | 9 | no |
| `hecke_core` float constants `h`, `z` | 9 | yes: compute `z_D = q³/(q²+1)` from `Q_MP` |
| no engine at all | 19 | n/a: classifiers, display-only metadata, retired routes |

Of the 19 with no engine, most are not defects: `atom_nf_symbolic_D` and
`tr_m_algebraic_q:126` use the float only to classify a letter as 0, −h/2 or −h.
`q_beta_substrate_prediction` and the `qbeta_*` Stokes probe are on retired Q_β
routes. The ones worth a look are `laurent_q_trace` (a self-test at float q),
`mirror_isospin_coulomb_split`, `crystal_alpha_shift_pole_orders`,
`aufbau_eigenvalue_channel` and `derive_b2`.

## Proposed tranches, cheapest and most useful first

**T1. Float seminormal rep → MPFR twin (18 files).** This is the same move that
just worked for the brane tower: replace `build_seminormal_matrices` +
`chi_lambda_of_word` with `exact_seminormal_matrices` + an mpf product.
- Cost: about one file an hour including the re-run. Small irreps (n ≤ 9) stay
  fast. At A = 4 the largest irrep has dimension 4158, and dense mpf there is
  hours per word, so those files need the Rust MPFR character instead.
- Risk: numbers move at the 1e-15 level. A larger move means the old float path
  was hiding something, as with ³He, and each one would be reported.
- Commits to: nothing upstream. The float kernel stays for the callers that are
  float by design.

**T2. The two producers whose output feeds another producer.** The audit's
`F64_ENGINE_ENTRY` tier names `all_nuclides_wedderburn_spectral_v2` and
`fr_pullback_cosh_h_test`. These matter more than end-of-line probes, because
they carry the float64 floor into someone else's numbers.
- The audit's "half-fix" warning is out of date. `hecke_characters.dim_q` and
  `qfac` already return mpf when given an mpf q (checked today), so passing
  `Q_MP` instead of the float proton q is enough. It no longer needs a new helper.
- But `fr_pullback_cosh_h_test` reads its characters from the
  `atom-chi-rust-*.witness.json` files, which were themselves made at float
  precision. So the fix chain is two producers deep.

**T3. `hecke_core.h`, `hecke_core.z` → mpf at the import (9 files).** Mechanical,
and the value is already convention D. Risk is low. One caution: the float `z` is
also how some numpy code keeps a float dtype, so a site that mixes it into
`np.eye` would turn into a slow object-dtype array (the trap documented in
`canonical_braid_crossings.d_for_ctype`).

**T4. numpy and scipy (57 + 30 files). Leave these alone by default.** Most use
an LP or SDP solver (Clarabel, cvxpy, scipy) that is float64 by construction. For
those, the honest fix is to report results at the solver's precision, not to
widen the arithmetic around it. Only the ones that serialise 50 digits from a
float solve are defects, and the `F64_ENGINE_ENTRY` tier already lists those
(9 terminal probes).

**T5. `pyhecke.gram` (15 files). Do not change the engine.** Its own comments say
its float `q0/qi/h` are kept bit-stable on purpose, and full-precision twins
already exist next to them. Each caller that needs digits should switch to
`*_mp` individually, which belongs inside T1 or T3, not a separate sweep.

## Findings that are not precision, recorded so they are not lost

1. **³He combiner check** (fixed, above).
2. **`hecke-character-symbolic.witness.json` is stale.** Re-running its producer
   moves the (2,1) characters of p and n by up to 7×, and their symbolic forms
   change. The q₀ edit cannot do that (the symbolic form does not depend on q₀),
   so it comes from earlier word changes on main. The witness was not refreshed,
   because whether to refresh it is the owner's call.
3. **`canonical_brane_tower_decomposition.py` raised `ValueError`** on its own
   header line (`{'Δ':>+12}`). Fixed in passing.
4. **The colour-blind `-h/2` appears hardcoded in 9 more places** (grep
   `, -h / 2, `). They sit in quark-level and probe code, not at the p-n
   interface, so they were not changed. Each one is a question about which
   crossing that line models, not a mechanical fix.

## Recommendation (judgement, not a finding)

Do T1 next, then T2, then T3. They are where a float64 floor actually reaches a
published number, and the ³He case shows that each re-run can also surface a
real bug. T4 and T5 should be per-file decisions taken during those tranches, not
sweeps.

If the owner says nothing: the branch stays at its current 15 fixed files, and the 86
files keep reporting in the audit.

## Outcome of T1 → T3 (same day, owner chose "T1, then T2 and T3")

Audit after the tranches: **F64_CAST 81 files / 157 sites** (from 86 / 162), and
`F64_ENGINE_ENTRY` has **0 propagating** producers (from 2). Nine terminal
probes are left in that tier.

**New shared helper.** `mass_at_3A_proper.chi_lambda_of_word_mpfr(shape, word, q)`
is the full-precision twin of the float `chi_lambda_of_word`. It takes the same
`(c, d, gen)` word and runs `pyhecke_native.chi_q_atomic_mpfr`. It refuses a
float q. On the deuteron word it agrees with the float kernel to 3e-15–5e-15.
Any remaining T1 caller can switch with a one-line change.

**T1, converted:**
- `iterative_lp_dual_h6_deuteron`: χ^λ(β_D) moves by up to 4.1e-14. Its own
  tr_M cross-check was at 0.736 in the committed witness (stale); the re-run
  gives 1.18e-8 and passes.
- `paper_six_term_shadow_price_sweep`: only the recorded q₀ was 16 digits.

**T1, not converted, with reasons.**
- `markov_trace_3A` (the only `chi_lambda_of_word` call in `mass_at_3A_proper`) is
  deprecated, as is the `qbeta_perlambda_collapse` probe that reads it.
- These need the matrix itself, not its trace, so they are numpy by design:
  - `binding_k_solver` (determinants and eigenvalues, plus an LP);
  - `A_operator_extract_general` (lstsq fit; the mpmath combiner supersedes it);
  - `gram_*` probes, `alpha_k_jones_markov_h3/h4`, `atom_level_wedderburn_tower`
    (marked not_production).

**T2, both converted.**
- `all_nuclides_wedderburn_spectral_v2`: its native cross-check now uses the MPFR
  entry. The deviation is 2.1e-40, where before it could only show ~1e-16. No
  data field moves.
- `fr_pullback_cosh_h_test`: MPFR characters, and `dim_q`/`qfac` at the mpf proton
  pin. Its inputs (`atom-chi-rust-*`) were already MPFR. My change moves results
  by ≤ 3.9e-14. **The witness was not refreshed**, because re-running the
  *unmodified* producer today already moves the deuteron B by ~110%. That flips its
  verdict from "cosh(h) injection NEUTRAL, best variance 1.54" to "HELPS at
  v5, +1.1%, best variance 2.33". That movement is staleness from upstream word
  changes, and refreshing it is an owner decision.

**T3: no clean wins.** Of the nine `hecke_core` importers:
- `markov_peel_rust_bridge` uses h only to classify a crossing's sign.
- `canonical_tr_m_via_branching` and `wenzl_a3_cross_check` are numpy/complex128
  pipelines whose mpmath sibling is the combiner itself.
- `k_versus_selected_operator_probe` is a numpy solve over the float `TR_M` table.
- The rest are legacy or `not_production`.

None is a substitution that adds digits to a published number.

**Stale witnesses, refreshed on owner instruction ("Refresh both", commit `744ca678f7b`):**
1. `hecke-character-symbolic.witness.json`: the (2,1) characters change
   symbolic form and sign at q₀ (p 1.8077 → −0.2806, n 1.7009 → −0.3720).
2. `fr-pullback-cosh-h.witness.json`: the verdict now reads "HELPS at
   v5_alpha_2_div_cosh_h, +1.1%", where it read "NEUTRAL" before.
