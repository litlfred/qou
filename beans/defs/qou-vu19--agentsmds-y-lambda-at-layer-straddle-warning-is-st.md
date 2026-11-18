---
# qou-vu19
title: AGENTS.md's y_lambda_at layer-straddle warning is stale — the cache path is dead
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-23T21:40:25Z
updated_at: 2026-10-04T15:16:18Z
parent: qou-5vkl
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


---

## Item 2 ANSWERED — zero live instances (2026-08-23)

`computations/audits/cached_accessor_shape_audit.py` answers the durable half of
the AGENTS.md warning: *"audit any other cached-witness accessor with the same
shape."*

**Result: 2 hits, both the same dead function** —
`_y_lambda_at_convention_C_HISTORICAL` in `computations/`, and its copy in the
generated `qou-mass/_internal/` mirror. **No live instance exists.** The general
warning is sound; it currently has no target.

### Three detector versions, and the two that were wrong

Recorded because "a clean detector run is not evidence the surface is clear" is
the standing lesson, and it applied twice here.

| v | keyed on | result | why it was wrong |
|---|---|---|---|
| 1 | tolerance literal + `".witness.json"` string, same function | 1 | that one hit is the **inverse** shape — `cross_check_trM_1ppb` reads the pin and **raises** if the runtime constant disagrees. A guard. |
| 2 | `if` test mentions a q-constant **name** (`Q`, `Q_MP`, `Q_50_DIGIT_STR`, …) | **0** | missed the known positive, which compares against `_Y_LAMBDA_AT_Q0_WITNESS_Q0` — a module-private name no list would guess. Keying on **spelling** is the failure mode the convention-C blindness taxonomy catalogues. |
| 3 | **provenance** — a name assigned from a file/JSON read, at module level or inside a loader that declares it `global` | 2 | — |

v3 needed two further discriminators, each measured:

- **The gate must involve a caller argument.** Without it: 34 hits, and the
  great majority are plain memoisation (`if _CACHE is not None: return _CACHE`)
  or an existence check (`if PATH.exists(): return load(PATH)`). Those are
  benign — they hand back the same data to everyone, claiming nothing about the
  caller's q. What makes the shape dangerous is that the cache is served **on
  the strength of a comparison against something the caller passed**, which a
  caller passing the package constant satisfies trivially.
- **A leading `-`/`.` means a suffix pattern, not a path.**
  `AUDIT_SUFFIXES = ("-audit.witness.json", …)` read as cache-derived, so every
  `if name.endswith(suf)` over it looked like the shape. That was 2 of the last
  4.

**The known positive is asserted, not hoped for:** `--selftest` exits 1 unless
`_y_lambda_at_convention_C_HISTORICAL` is among the hits. A future edit that
narrows the detector past it fails loudly.

## Found on the way — vendor mirror drift from my own earlier work

`scripts/sync-qou-mass-vendor.py --check` reported two files drifted, both mine
from this session:

```
ame-2020-binding-energies.witness.json                  (the AME producer fix)
data/m-p-borromean-verification-50dps.witness.json      (the #5593 re-stamp)
```

Regenerated with `--apply` (42 modules), never hand-edited. `--check` **does**
exit 1 on drift, so it can gate — it simply is not wired into
`precision-gates.sh` or `staleness-gates.sh`, which is why two merged PRs left
the mirror behind without anything objecting.
