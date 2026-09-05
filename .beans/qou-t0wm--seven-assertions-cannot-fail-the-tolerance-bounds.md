---
# qou-t0wm
title: 'Seven assertions cannot fail: the tolerance bounds its own residual, in six producers'
status: in-progress
type: task
priority: normal
created_at: 2026-09-05T06:21:10Z
updated_at: 2026-09-05T06:21:49Z
---

Found 2026-09-05 while closing out the `qou-tol0` root cause. That bean's own
instance (`atom_mass_derived`, ten assertions under `tolerance=max(abs(r.delta_MeV)*2, 50)`)
was fixed in `7f95ad5962`; the SHAPE was never made detectable, so nothing had
looked for it elsewhere.

Detector: [`computations/audits/tolerance_from_residual_audit.py`](../computations/audits/tolerance_from_residual_audit.py).
Full analysis: [`docs/audits/2026-09-05-tolerance-that-bounds-its-own-residual.md`](../docs/audits/2026-09-05-tolerance-that-bounds-its-own-residual.md).

## The seven, each verified by hand

| producer:line | assertion | why it cannot fail |
|---|---|---|
| `mass-from-q-symbolic.py:568` | `𝔪(𝔅₃) Borromean topological mass` | `borromean_mass_ratio` IS `VOL_BORROMEAN / HBAR_Q_SQ0` (line 246); `expected` restates it |
| `mass-from-q-symbolic.py:577` | `𝔪(𝔅₃) in MeV` | both sides expand identically; the witness records residual **0.0 exactly** |
| `confined_knot_binding.py:289` | `W_sym equals W_alt` | `W_SYM` and `W_ALT` are the same expression, character for character (lines 42, 44) |
| `confined_knot_binding.py:308` | `V_pn = W_std*(z+d_pn)` | `expected` restates `V_pn_exact`'s definition (line 251) |
| `yekutieli_borromean_h2_extraction.py:216` | `kappa_computed` | tolerance `2*max(\|c\|,\|e\|)`; unfalsifiable by the triangle inequality |
| `compute_atom_chi_rust.py:164` | `rust_kernel_loaded` | `float(x)` vs `x`, same subscript |
| `channel_asymmetry_crossing_budget_bound_probe.py:204` | `budget_is_s_squared` | `c_inter = s * s` (line 134); `expected` is `s * s` |

## The two worth reading twice

**`W_sym equals W_alt`** carries `source="Wedderburn-Artin: dim_q((3))=dim_q((1,1,1))=1"`,
advertising a check of a representation-theoretic fact. It checks nothing — the
two constants are one expression written twice. **If the Wedderburn–Artin fact
were false, the assertion would still pass.** The `source` field is doing all
the epistemic work and none of it is tested.

**`kappa_computed`** is the one with a live wrong number. Recorded:
computed `0.1875`, expected `-0.915965594177219…`, tolerance `1.8319…`,
`passed: true`. Opposite signs; residual **1.1035**, a 121 % miss.

## What would close this, per assertion

Fix at the producer, and expect one to go RED — that is the honest outcome:

1. `mass-from-q-symbolic` ×2, `confined_knot_binding` ×2 — need an INDEPENDENT
   expected (a literal from the source each `source` field already names), or
   the assertion deleted. Restating a definition is not a check. Witness
   regeneration required; attribute any value movement against an unmodified
   run first.
2. `yekutieli_borromean_h2_extraction:216` — needs a real tolerance, and will
   then **fail** at 121 %. AGENTS.md asks for the honest negative explicitly.
   Whether κ = 0.1875 or the expected `-Vol/…` is the wrong side is a separate
   question this bean does not settle.
3. `compute_atom_chi_rust:164`, `channel_asymmetry…:204` — self-reports, the
   benign class `always_vacuous_assertion_scan` documents. Renaming suffices.

## Not to be confused with three neighbouring beans

- `qou-tol0` — the same root cause, its own instance already fixed. This is the
  corpus-wide sweep of the shape.
- `qou-26f2` — 266 assertions where `computed` and `expected` are the same AST.
  This audit deliberately **excludes** raw-identical arguments; only the case
  needing an indirection to see is new here.
- `qou-ploj` — `add_assertion(name, X, X)`, same exclusion.

## Do NOT widen anything

The audit exits 1 on any blocking hit. The fix is always at the assertion.
