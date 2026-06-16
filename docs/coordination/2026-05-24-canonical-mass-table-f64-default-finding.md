# Coordination — canonical_mass_table_extended.py default precision (RETRACTED)

**Date:** 2026-05-24
**Status:** ⚠️ **RETRACTED** — initial claim that `laurent_q_rust` default uses f64 was incorrect. The actual dispatcher path enforces MPFR-50dps. See §Correction below.
**Original trigger:** PR #1064 (mass-table regen via pyhecke-native v0.9.0) tripped the witness-pipeline drift detector.

## ⚠️ Correction (2026-05-24, post Copilot review on #1064)

The original doc claimed the `laurent_q_rust` default in `compute_tr_m_canonical()` dispatches through the f64 pyhecke-native surface and regresses the L1 50-dps floor. **This is wrong.**

The actual code at `computations/canonical_mass_table_extended.py:147`:

```python
if method == "laurent_q_rust":
    from markov_peel_rust_bridge import tr_M_atomic_rust_full
    effective_dps = max(int(dps), 50)  # ← enforces 50-dps floor
    tr_mp = tr_M_atomic_rust_full(Z, N, dps=effective_dps)
```

`tr_M_atomic_rust_full` routes through pyhecke-native's `tr_m_atomic_mpfr` (MPFR surface), not the f64 surface. The compute IS at 50 dps.

### What actually caused the "drift" the detector caught

The drift the witness-pipeline detector flagged was a **precision improvement, not a regression**:

- **Prior `markov_peel` baseline** (the value the detector compared against): used `sp.Float(str(Q_FLOAT), 50)` where `Q_FLOAT` is a Python float (f64) — so `str(Q_FLOAT)` is ~17 digits. The sympy `Float` got created with 50 dps allocation but f64-precision INPUT. Effective substrate precision: ~17 dps.

- **New `laurent_q_rust` path**: uses `Q_50_DIGIT_STR` directly (a 50-digit string literal). Effective substrate precision: 50 dps.

`tr_M(β_p, q_0)` differs at digit 17 because the OLD path was f64-substrate-precision; the NEW path is genuine 50-dps. The new value is MORE accurate.

### Misleading witness metadata (the REAL bug)

What IS broken: the witness emitter's metadata fields don't reflect the dispatched path:
- `parameters.precision: "f64"` (should be `"mpfr"`)
- `parameters.dps: 0` (should be `50`)
- `description` field still says "Rust hecke-canonical-chi (f64)" (should say pyhecke-native v0.9.0 tr_m_atomic_mpfr)

These are stale script-header strings, not compute regressions.

### Genuine open finding (separate from this retraction)

`knot_operators` metadata in the witness drops the `sigma_inv` sign marker for indices 1, 4, 7, 9, 12 in ⁵Li/⁶Li/⁷Li records (per Gemini review on #1064). The `braid_word_canonical` field has the correct signs; `knot_operators` was built from a separate codepath that strips the sign. This is a data-integrity bug worth a focused fix. **Not the f64 regression originally claimed in this doc.**

## What this retraction does

1. Marks the original claim wrong + explains why
2. Identifies the actual bug class (witness metadata staleness, not precision regression)
3. Points to the active follow-up PR fixing the metadata fields and the knot_operators sign

## Related work

- PR #1064 (merged) — the regen that surfaced this; sound numerical data
- PR #1069 — original (incorrect) coord doc — superseded by this retraction
- Follow-up fix PR — `canonical_mass_table_extended.py` metadata fields + `knot_operators` sign restoration
- `docs/audits/2026-05-22-rust-laurent-q-reduce-results.md` — original Tier 1.A results (confirms MPFR cross-check at 1e-50)

## Lesson

When a drift detector fires on a witness regen, FIRST verify which path actually computes the value (via the dispatcher logic), not just the metadata field labels. The witness's `parameters.precision` field is built by the script's header, not introspected from the runtime dispatch — it can lie.
