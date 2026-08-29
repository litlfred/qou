---
# qou-llew
title: 'q_ns_wellposedness: prose denies the self-assuming projection it contains'
status: todo
type: task
priority: normal
created_at: 2026-08-29T16:40:02Z
updated_at: 2026-08-29T16:40:43Z
---

`lean/QOU/FluidDynamics/q_ns_wellposedness.lean` carries a "Disposition
(integrity)" section asserting the self-assuming encoding was removed. Measured
against `main` today, its three claims are all false:

- "is `sorry`'d" — the file has **no** `sorry`;
- "Nothing in `QNsWellposednessContext` assumes any part of this conclusion" —
  the class field `wellposedness_holds` is **verbatim the theorem's conclusion**,
  and its own docstring says `Missing input: global regularity of the q-NS system`;
- the proof is `ctx.wellposedness_holds`, a bare projection.

The defect is already adjudicated — `lean-vacuity-review-ledger.json` records this
declaration under `proof-no-self-assuming-projection`, verdict `genuine`. What is
new is that **the file's prose denies it**, and that both tracking beans
(`qou-t28w`, `qou-7aj0`) describe a `sorry` at line 109 that no longer exists. An
agent triaging from the beans expects the honest §1 disposition and meets the
§3b-cond item-5 one.

Shallow clone here, so which encoding came first is **not established** and is not
claimed.

Scope: fix the docstring to describe the file, and re-title/close the two stale
beans. Whether to convert the projection back to a cited `sorry` is the author's
call — it is a Millennium-adjacent claim either way (`qou-t28w` tier B,
infra-blocked).
