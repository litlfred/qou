---
# qou-vu19
title: AGENTS.md's y_lambda_at layer-straddle warning is stale — the cache path is dead
status: todo
type: task
priority: normal
created_at: 2026-08-23T21:40:25Z
updated_at: 2026-08-23T21:41:05Z
---

## What AGENTS.md says

Under §"q₀ anchor convention", as a **STRICT** rule with its own worked example:

> **The specific trap that caused it (check your call sites).**
> `wedderburn_jones_markov.y_lambda_at(n, q)` returns the cached
> **muon-built** `y-lambda-at-q0.witness.json` whenever
> `|q − q_parameter.Q| < 1e-12` — a gate satisfied **trivially** when the
> caller passes `q_parameter.Q` itself. So the ideal-layer cache reaches an
> experimental-layer caller with **no signal that a layer boundary was
> crossed.** For experimental-anchor compute call
> `schur_principal_mpmath.y_lambda_at_q0_mpmath(n, q)` (live closed form)
> instead.

## It is out of date — read the body, not the docstring

The live `y_lambda_at` in `computations/wedderburn_jones_markov.py` is:

```python
from y_lambda_su_n import y_lambda_su_n as _y_su_n
import mpmath as _mp
if q_val is not None:
    _y = _y_su_n(n, _mp.mpf(str(q_val)), 2)          # the CALLER's q
    return {sh: sp.Float(_mp.nstr(v, 30), 30) for sh, v in _y.items()}
from y_lambda_su_n import y_lambda_su_n_symbolic as _y_su_n_sym
return _y_su_n_sym(n, Q_SYM, 2)                       # symbolic, anchor-free
```

**No cache read on any path.** The `|q − Q| < 1e-12` gate and the
`y-lambda-at-q0.witness.json` load now live in
`_y_lambda_at_convention_C_HISTORICAL`, which is dead — convention C, excised
2026-08-09, and the function's own docstring says so:

> THE THREE C FAST PATHS BELOW ARE NOW DEAD … the D result returns before any
> of them is reached. In particular `y-lambda-at-q0.witness.json` holds C
> weights and must **NOT** be served.

So the convention-D wiring **closed the straddle at the function**, and the
AGENTS.md paragraph now describes behaviour that no longer exists.

## Why this is worth fixing rather than leaving

It is not a harmless stale note. It names a specific function as a trap, so an
agent following it will either avoid `y_lambda_at` for experimental-anchor
compute when it is now the correct anchor-neutral call, or go "fix" call sites
that are not broken. **Measured, that second failure mode is 56 files:**
promoting `y_lambda_at` to a classifier identifier check — which is exactly
what the AGENTS.md wording invites — reclassified 56 producers from `proton` to
`BOTH`. `BOTH` shields a producer from triage as a possible deliberate
comparison, so acting on the stale guidance would have hidden 56 clean files
behind a muon association that no longer exists.

I nearly shipped that. The correction came from reading the function body after
a spot-check, not from the docstring and not from AGENTS.md.

## Scope note — the rest of that section stands

The **layer-straddle rule itself is unaffected and still STRICT**: never mix an
ideal-layer input with an experimental-layer one inside a single computed
quantity, and the μ₃ Fréchet worked example (11.54 ppb, `y_λ` from the
muon-built cache while `χ_λ` evaluated at the proton `q₀`) is a real measured
incident. What has changed is only that **`y_lambda_at` is no longer the
mechanism**. The general instruction that follows it — *"Audit any other cached-
witness accessor with the same 'matches the package constant ⇒ serve the cache'
shape"* — is the durable part and should survive the edit.

## Done here (PR on `claude/q0-classifier-prose-evidence-2026-08-23`)

`y_lambda_at` removed from the classifier's `MUON_ARTIFACTS`, with this
reasoning recorded at the constant so the next reader does not re-add it.

## Next

1. Rewrite the AGENTS.md paragraph: keep the straddle rule and the μ₃ example,
   replace the `y_lambda_at` mechanism with a note that it was closed by the
   convention-D wiring on 2026-08-09, and keep the "audit any other cached-
   witness accessor" instruction.
2. Check whether any **other** accessor still has the
   "matches the package constant ⇒ serve the cache" shape — that is the part of
   the warning that may still have live instances, and nobody has measured it.
