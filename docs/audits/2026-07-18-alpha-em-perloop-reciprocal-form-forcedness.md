# α_EM per-loop 1/(8π): not naive-mode-countable — the arithmetic joint is subsumed into the magnitude leg

**Date:** 2026-07-18 · **Axis:** α_EM 2-loop / 1ppQ (#3612) · **Tier:** numerical
(scope-(a) forcedness/anti-laundering) · **Discipline:** no fit (nothing tuned to
CODATA), no c_k, nothing wired, no tier change.

## Question

With the two α_EM ingredients now settled — the 2-D heat-kernel per-mode constant
`1/(4π)` (#3909) and the homological index `b₁ = 2g = 8` (#3896) — is the per-loop
measure `1/(π·b₁) = 1/(8π)` (the reciprocal-form `1/b₁` and the `8π = 2·4π`
multiplicity) **forced** by naive mode-counting bookkeeping, or does it require the
genuine polarized-Jacobian theta-factor computation (#3911)?

## Result — 6 combinations hit 1/(8π); not naive-mode-countable

[`alpha_em_perloop_reciprocal_form_forcedness_probe.py`](../../computations/alpha_em_perloop_reciprocal_form_forcedness_probe.py)
enumerates the natural dimensionless combinations of the fixed data
`{1/(4π), b₁=8, g=4, P=2}`. **Six** distinct combinations land exactly on
`1/(8π)` (e.g. `(1/4π)/P`, `(1/4π)/(b₁/g)`, `(1/8π)·1`, `2·(1/4π)/g`,
`2·(1/4π)/(b₁/P)`, …). No forcing principle singles any one out.

**Conclusion (scope-(a), anti-laundering):** the coefficient is **not
naive-mode-countable**. The reciprocal-form and the `8π = 2·4π` multiplicity do
**not** separate from the magnitude, so `8π` cannot be honestly derived by
arithmetic bookkeeping — it must come from the genuine **polarized-Jacobian
genus-4 theta-factor** computation (#3911). This forecloses reverse-engineering
`8π` from a hand-picked combination (the trap the merged forcedness audit named:
"the working 1/(8π) must be FORCED, never reverse-engineered").

## Correction to the 2026-07-18 action plan

The action plan listed "the α_EM reciprocal-form / `8π = 2·4π` multiplicity joint"
as the *last unowned separable arithmetic piece* (move 1). **That framing is
wrong.** This probe shows the arithmetic does **not** separate: the reciprocal-form
coefficient is one object with the polarized-Jacobian magnitude, already owned by
#3911. There is **no separate unowned arithmetic piece** — the whole α_EM
coefficient wall is the #3911 theta-factor. Move 1 is subsumed, not open.

## Honest scope

A scope-(a) *negative* that corrects the ownership map — it does not derive
`1/(8π)`; it proves the coefficient cannot be *arithmetically* derived from the
settled count + π-power alone. No fit; no c_k; nothing wired; no tier change.

## Cross-references

- Action plan (corrected): [`2026-07-18-1ppq-action-plan.md`](2026-07-18-1ppq-action-plan.md)
- Settled ingredients: [`2026-07-18-alpha-em-pi-origin-adjudication.md`](2026-07-18-alpha-em-pi-origin-adjudication.md) (#3909), the b₁ index (#3896)
- Magnitude leg (owner): #3911 (polarized Epstein det′Δ / theta-factor)
- My front-3 continuum-exclusion: [`2026-07-17-alpha-em-bring-jacobian-zeta-determinant.md`](2026-07-17-alpha-em-bring-jacobian-zeta-determinant.md)
