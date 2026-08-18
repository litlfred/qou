---
# qou-jtbo
title: pyhecke.gram.h is a Python float -- a float64 entry point every consumer silently inherits
status: todo
type: task
priority: normal
created_at: 2026-08-18T16:09:37Z
updated_at: 2026-08-18T16:11:22Z
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
