---
# qou-jtbo
title: pyhecke.gram.h is a Python float -- a float64 entry point every consumer silently inherits
status: completed
type: task
priority: normal
created_at: 2026-08-18T16:09:37Z
updated_at: 2026-08-18T21:10:08Z
---

Found while draining the NO-FLOAT64-in-probes directive (AGENTS.md 2026-08-18).

**The defect.** `pyhecke.gram.h` is a Python `float`:

    tools/pyhecke/python/pyhecke/gram.py:40
        from q_parameter import Q as q0, Q_INV as qi, HA as h

`q_parameter.HA` is the float64 convenience sibling of the exact
`Q_50_DIGIT_STR` route. Measured: `G.h` = 0.20906029879563937 against
`q - 1/q` at 50 dps = 0.20906029879563931543084621313 — **off by 5.5e-17**.

**Why it matters more than the size suggests.** It is an *entry point*. A
consumer writing `hf = float(G.h)` — or even just using `G.h` in mpmath
arithmetic — silently pins the whole downstream computation to float64, with no
signal that a precision boundary was crossed. That is exactly how the Coulomb
charge probe ended up computing its headline offset in float64 (fixed by
deriving `h = q - 1/q` locally at 50 dps).

**The same file already has the exact value.** Line 421:

    _H_FRAC = _Q_FRAC - _QI_FRAC  # h = q - 1/q (exact rational)

So gram.py computes h exactly for internal use and exports only the float.

**Blast radius: 10 files** reference `G.h` / `gram.h` (excluding _deprecated):
f64_into_mpmath_audit.py, coulomb_charge_is_linear_in_z_probe.py,
h6_deuteron_free_word_chi_lambda_probe.py, qbeta_lorentzian_gram_offset_probe.py,
framing_derivation_attempt_probe.py, all_nuclides_sdp_admissibility.py,
mass_at_3A_proper.py, qbeta_crossing_weight_hecke_probe.py, plus gram.py and
atom.py themselves and the test.

**NOT fixed here, deliberately.** This is shared library code with 10 consumers
across compute and probes; changing the type of an exported constant could shift
numbers in producers that emit witnesses. That needs its own scoped change with
a witness-diff, not a drive-by edit from a probe branch.

**Options for whoever takes it:**
1. Export `h_exact` (mpf or Fraction from the existing `_H_FRAC`) alongside `h`,
   and migrate consumers — additive, no number moves until a consumer opts in.
2. Make `h` itself exact and audit all 10 consumers' witnesses for drift.
3. Leave `h` float but add a module docstring warning naming it a float64 entry
   point — cheapest, does not stop the next agent from inheriting it silently.

I would take (1). Note `framing_derivation_attempt_probe.py` and
`mass_at_3A_proper.py` are on the L2 binding path, so option (2) would need
the binding witnesses re-checked.


## 2026-08-18 — RESOLVED, and the bean's own premise was wrong twice

**Correction 1: the exact accessor ALREADY EXISTED.** This bean said gram.py
'exports only the float' and proposed three options for adding an exact one.
Wrong — `gram.py:729` has had `h_mp(dps=50)` all along, docstring: *'h = q_0 -
q_0^-1 at 50-dps mpmath — the mpf counterpart of the float module constant h'*.
It is in `__all__` alongside `z_mp`, `tr_m_mp`, `gram_matrix_mp`. Verified:
`h_mp()` agrees with q-1/q to 1.3e-51 at 50 dps.

I found this only because my redundant re-export collided with the existing
name. A corpus-grep of the module before writing the bean would have caught it —
the third time this session that skipping that check cost me.

**Correction 2: `_H_FRAC` is NOT the exact h.** The bean cited
`gram.py:421 _H_FRAC = _Q_FRAC - _QI_FRAC` as 'the exact value already in the
file'. It is h at `q = 111/100` (`_Q_FRAC = Fraction(111,100)`), a rational
*approximation* used for the exact-in-Q H_3 Gram path — not h at the substrate
q0 = 1.1099785827513808. Different quantity.

**Correction 3: the muon/proton worry was unfounded.** I checked whether
`q_parameter.HA_MP` (shim, commented 'muon base') differs from
`qou_substrate.constants.HA_MP` (proton). They are **identical** — f64 equal,
mpf difference exactly 0.0. No layer straddle from this path.

## What was actually done

The defect was never 'no exact option exists'; it was that the float constant
carried no pointer to the exact one, so a consumer reached for `h` and got
float64 silently.

1. **`gram.py`** — documented `q0`/`qi`/`h` as the float64 path, stating that
   they are deliberately bit-stable (constants.py: 'Don't change them'), that
   `h` is off by 5.0e-17, and naming the existing mpf counterparts
   (`h_mp`, `z_mp`, `tr_m_mp`, `gram_matrix_mp`). **No value changed.**
2. **`framing_derivation_attempt_probe.py`** — the only `G.h` consumer emitting
   no witness — migrated from `hf = float(G.h)` to `hf = G.h_mp()` with mpmath
   arithmetic. Conclusions unchanged: writhes still p +3, n +1, pp +7,
   pn +4.0006879, nn +1; interface-only still exactly +1 / ~0 / -1.

## Deliberately NOT done

The four remaining `G.h` consumers **emit witnesses** —
`mass_at_3A_proper.py` (1), `all_nuclides_sdp_admissibility.py` (4),
`h6_deuteron_free_word_chi_lambda_probe.py` (3),
`qbeta_lorentzian_gram_offset_probe.py` (3). Migrating them to `h_mp()` moves
numbers in the low digits and requires witness regeneration plus a diff review.
That is its own scoped change, not a drive-by from a probe branch. Filed as the
follow-up below.
