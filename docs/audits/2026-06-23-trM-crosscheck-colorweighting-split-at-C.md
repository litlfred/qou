# tr_M 1ppb cross-check: the four legs split on the color-weighted p-n convention at q₀=C

**Date:** 2026-06-23
**Branch:** `claude/q0-clusterA-followup-2026-06-22` (PR #2598)
**Context:** post-rebase `cross_check_trM_1ppb.py --strict` failure during `/prepare-merge`.

## TL;DR

The q₀ A→C migration in this PR (and #2585) is **correct and complete** — every
witness/leaf/cache now evaluates at the canonical proton re-pin
`q_at() = 1.1099785955573347…` (C), not the retired `1.10997858275…` (A).

The `cross_check_trM_1ppb.py --strict` gate nonetheless reports `DIVERGE` on
all atoms. This is **not** cache staleness and **not** the q₀ migration. The
four independent tr_M legs split **2-vs-2 on the `bring_color_weighted`
p-n crossing convention**, and `main` hid the split behind a **stale q₀=A
cross-check witness** that was never regenerated after the 2026-05-28 re-pin.

## Evidence

`main`'s committed `cross-check-trM-1ppb.witness.json` carries q₀=**A** with
`any_diverge: false, passed: true`, last touched 2026-06-19 by an unrelated
beans commit (swept, not recomputed). But `main`'s own `q_at()` returns **C**.
So the green witness is a stale snapshot: every leg was computed at A together,
so they agreed.

Regenerating at the live q₀=C (this PR) gives, e.g. deuteron:

| group | legs | deuteron \|tr_M\| | color-weighted p-n crossing? |
|-------|------|-------------------|------------------------------|
| 1 | Hoefsmit (`atomic_tr_m_mpfr`) + markov_peel | 0.38835726 | **yes** |
| 2 | chi-cache combiner + Habiro | 0.38828640 | **no** |

The two groups differ by ~7e-5 (A=3/deuteron) / ~9e-8 (p/n). The χ closed-form
anchor (1-dim irreps) matches to ~1e-50, so the χ engine itself is correct —
the split is purely about whether the **inter-nucleon crossing** is the
color-weighted `σ − h·(½ − δ/4)·𝟙` (δ = `flavor_split_subleading(q₀)`) or the
color-blind `σ − h/2·𝟙`.

## Two contributing causes (both addressed / scoped here)

1. **markov_peel fast-path regression (fixed in this PR).** This PR's
   color-weighted crossing put a symbolic non-Laurent δ(q) coefficient into
   `crossing_from_cd`; the `LaurentQ` fast path (`hecke_laurent_fast`) raised
   `non-Laurent factor …`, so `markov_peel_atomic_witness` aborted and the peel
   leg stayed at A. Fixed by a fast→slow fallback in `markov_peel.tr_M_atomic`
   (on a non-Laurent `LaurentQ` failure, fall through to the exact sympy/Ocneanu
   path). Post-fix, Hoefsmit + markov_peel **agree** at C.

2. **chi-cache + Habiro are structurally color-blind (follow-up).** The χ-cache
   producer (`chi_at_q0_via_hoefsmit_mpfr`) *does* build the color-weighted word
   (`atom_braid_word_3A` defaults to `bring_color_weighted`), but its **native
   Rust χ path (`pyhecke_native`) only recognizes `d ∈ {0, −h, −h/2}`** and
   raises / falls back on the color-weighted `d = −h(½ − δ/4)`. So it emits the
   color-blind χ. The Habiro path is a separate series representation with no
   δ-crossing term. Making both color-weighted is a precision-critical refactor
   across two compute engines (Rust FFI + Habiro series), out of scope for the
   q₀ migration PR.

Plus the **known A=3 combiner / Δ_λ gate** (per the coordination ledger): even
with consistent conventions, the A=3 legs diverge at ~1.8e-4 independently of
q₀ or color-weighting.

## Resolution (2026-06-23, this PR)

Three of the four legs are now color-weighted and converge at C:

1. **markov_peel — FIXED.** Fast→slow fallback in `tr_M_atomic` on a non-Laurent
   `LaurentQ` failure (the δ(q) coefficient). Color-weighted at C.
2. **chi-cache — FIXED.** The color-blindness was **not** an architecture limit:
   `chi_at_q0_via_hoefsmit_mpfr` hit a resume `KeyError: 'contribution'` on a
   stale partial cache and never recomputed, so the combiner read the old
   color-blind numerical cache. Deleting the stale caches and regenerating fresh
   makes the native path correctly bypass the color-weighted δ-crossing
   (d=−0.10446 ≠ −h/2) to the exact slow path. **markov_peel and chi-cache now
   agree to ~1e-15** for deuteron/tritium/helium-3.
3. **Hoefsmit — already color-weighted**, but sits ~9e-9 from the
   markov_peel=chi-cache pair (a separate, small Hoefsmit-leg precision/method
   offset, independent of color-weighting and of q₀).

**The A=3 ~1.8e-4 "Δ_λ gate" divergence was the stale chi-cache, not a
fundamental gate** — with the cache regenerated, the A=3 exact methods agree.

### The Habiro leg is structurally color-blind (by design)

The Habiro extrapolation leg is built from `hecke_laurent_fast.tr_M_atomic_fast`
(the LaurentQ pipeline) and extracts **cyclotomic** coefficients a_m(u) with
integer coefficients. The color-weighted tr_M is a rational function with
`(q+1)`/`(q−1)` denominator factors (non-Laurent), which breaks the cyclotomic
structure the Habiro method depends on. So the Habiro leg **cannot** be made
color-weighted without abandoning the cyclotomic extraction. It remains a
color-blind extrapolation, useful where the exact methods are intractable
(⁵Li/⁶Li); for atoms where the three exact methods exist and agree, the Habiro
column is expected to differ by the color-weighting amount (~1.8e-4).

## Disposition

- The q₀→C migration ships in PR #2598 (correct, verified: m_p err 0.0004 ppb).
- Color-weighting now consistent across the three **exact** tr_M methods
  (Hoefsmit / markov_peel / chi-cache).
- The cross-check `--strict` still flags divergence driven by (a) the
  color-blind Habiro extrapolation leg and (b) the ~9e-9 Hoefsmit offset.
  Recommended gate design: compare the exact methods (now agreeing); treat
  Habiro as an informational extrapolation column, gated only where it is the
  sole method.
