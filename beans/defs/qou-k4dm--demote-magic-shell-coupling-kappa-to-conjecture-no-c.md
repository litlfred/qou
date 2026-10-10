---
# qou-k4dm
title: 'Demote prop:magic-shell-coupling-kappa to conjecture — there is no CAL-4'
status: completed
type: task
created_at: 2026-08-10T02:30:00Z
updated_at: 2026-08-10T02:30:00Z
---

Opened retroactively. The work was done in PR #4885 before a bean existed —
recording it as unclaimed rather than leaving `.beans/` saying it did not happen.

## What was wrong

`magic-shell-coupling-kappa.qa.json` carried `[critical]
canonical-cal4-acknowledged`, offering *"demote to conjecture or add CAL-4
banner"*. **There is no CAL-4.** The three-calibration discipline admits `m_e`,
`𝔇_β`, `𝔇_π` and nothing else, so the banner branch would have left a provable
block kind carrying an acknowledgement that its own content was fitted.

Both factors of `κ = −E₀·log(1/h) / ([2]_q[3]_q)` were read off the (2,2)
doubly-magic anchor. Structural motivation attached afterwards does not convert
an anchor-identified expression into a derived one.

## Done

- `prop:` → `conj:` across `.ts` / `.md` / `.lean`, the table's `uses[]`, and the
  definition index. Validation clean; the `[critical]` finding cleared.
- **Nothing unwired** — checked, not assumed. Producer already removed, all three
  κ witnesses under `computations/_deprecated/`. The `KAPPA` in
  `pyhecke/constants.py` is a different object (the binding scale `m_e`).
- **The Lean was worse than the block kind.** The superseded class carried the
  observed slope as a *field*, so `⟨q, m_e, kappaClosed q m_e, rfl⟩` discharged
  it and the projecting theorem asserted nothing — the §3b-cond rule-5
  self-assuming projection. Replaced by a primary conjecture class over an
  `opaque` measured datum, no instance.
- Stated with a relative `tol`, not exact equality: the residual at `q₀` is
  `3.4·10⁻⁴`, so an exact-equality conjecture would have been contradicted by
  the data offered in its support.

## Left standing

The proved content about the *expression* is untouched and remains valid — the
bracket's tie to canonical `qIntBal`, positivity of `E₀` and `h`, the forced
sign. Only the identification with the *observed* slope is conjectural.

Follow-up: `qou-o16k`.
