# b0vf He4 χ "regen drift" is a q₀-pin difference, not an engine/version issue

**Date:** 2026-06-29
**Beans:** `b0vf` (He4 H₁₂ χ), cross-ref `tnjb` / `z5vu` (q₀-convention witness staleness)
**Follows:** [`2026-06-28-pyhecke-native-buildable-clarabel-egress-proxy.md`](2026-06-28-pyhecke-native-buildable-clarabel-egress-proxy.md)
(established `pyhecke_native` builds via the egress proxy).

## Question chased

After `pyhecke_native` was made buildable, re-running `chi_4he_via_rust_lossless.py` reproduced the
full 77/77 He4 χ cache in ~3 s but with `tr_M(q₀)` differing **~1e-7** from the committed
`chi-helium-4-h12-at-q0-50dps-matrix-m.witness.json` (generated 2026-06-10). "Chase the canonical
`pyhecke-native` version" — is the committed witness stale, or is my build non-canonical?

## Finding — it is the q₀ pin (input), not the engine

1. **Drift is 100% engine-output-side, 0% data-weights:** all 77 `chi_lambda` differ; all 77
   `y_lambda` identical.
2. **Both engine builds agree:** `pyhecke-native` built with the clarabel-default features **and**
   with `--no-default-features` give the *same* new value (`tr_M = 0.885616920128525`,
   `chi[12] = 134.82995572…`). So the engine is internally consistent; the 2026-06-28 clarabel-default
   change (`05bba46f`) is **not** the cause (it was the initial suspect).
3. **The committed witness used a different q₀:**
   - committed `q_0_50dps = 1.1099785827513808…`
   - current `q_parameter.Q_50_DIGIT_STR = 1.1099785955573347…` (the muon value)
   - Δ ≈ 1.3e-8 relative — exactly the **muon↔proton ~11.5 ppb** spread (AGENTS.md §q₀ anchor
     convention). χ(q₀) is high-degree in q, amplifying Δq₀ ~1.3e-8 → Δχ ~1e-7.

So the engine is canonical and consistent; the committed He4 χ witness simply sits at a **different q₀
pin** than the current `Q_50_DIGIT_STR`.

## Consequence for b0vf

- **b0vf is NOT engine-blocked** (the #3039 "out-of-scope, not fixable" claim was already corrected;
  the engine builds and is canonical).
- "Completing" the He4 χ cache is a **q₀-convention witness refresh**, which lands squarely in the
  STRICT, owner-gated q₀ tangle (`tnjb` recurring silent-q₀-flip bug; `z5vu` "~840 muon-q₀ witnesses,
  owner-gated"). Regenerating this one witness to the other pin in isolation is exactly the silent-flip
  hazard those beans guard against.
- Therefore: **do not unilaterally regenerate.** The proper fix is a q₀-convention decision (which pin
  is canonical for the χ-cache layer) applied consistently — owner-gated. No regen committed; all
  test runs were reverted (working tree clean).

## Net

The b0vf investigation chain closes cleanly: tooling block dissolved (engine builds, both feature sets
agree, canonical); the residual χ "drift" is a q₀-pin difference, not staleness of the engine; and the
remaining work is an owner-gated q₀-convention refresh tracked under `tnjb`/`z5vu`, not a standalone
b0vf compute.
