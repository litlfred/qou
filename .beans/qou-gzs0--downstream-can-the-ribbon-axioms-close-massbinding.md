---
# qou-gzs0
title: 'Downstream: can the ribbon axioms close mass/binding derivation gaps'
status: todo
type: task
priority: normal
created_at: 2026-08-17T01:45:48Z
updated_at: 2026-08-17T01:59:29Z
---

## 2026-08-17 — first pass: the twist reaches the mass chain, but is ONE AXIOM SHORT

Traced whether the newly-landed `BalancedCategory` twist can close a recorded
mass/binding gap. It touches a real one, and falls exactly one axiom short of
closing it. Measured, not argued.

### The chain

```
twist θ (landed)
  → [MISSING: dual compatibility θ_{X∨} = (θ_X)∨]
  → sphericality on all of C
  → qDim_conj : qDimObj(X∨) = qDimObj(X)          -- bean rtqd, OPEN
  → dim_q(λ) consistency
  → G⁻¹_{λμ} = δ·[n]_q!/(dim_q(λ)·dim(λ))          -- gram-matrix-spectral-connection
  → the mass chain
```

### The measurement

`KeystoneBalancedRibbon.lean` carries `twist`, `twist_isIso`, `twist_unit`,
`twist_naturality`, `twist_tensor` — and **no dual-compatibility field**. Grep
for `twist_dual`: empty. So what landed is **balanced, not ribbon**.

`KeystonePivotalSpherical.lean` factors `rtqd` into two named inputs:
`hTransport` (pivotal transport) and `hSpherical` (sphericality). Its only
unconditional proof of the second is `leftQDim_eq_qDimObj_of_symmetric` — the
**symmetric** case, which the framework calls the classical limit.

Ribbon = balanced **+** dual compatibility, and sphericality follows from
*ribbon*, not from balanced alone. So the twist as merged does not supply
`hSpherical` in the braided case.

### Why this is the useful answer rather than a disappointment

`rtrb`'s own note already names the missing piece: *"Next: the dual-
compatibility ribbon axiom (theta_{X*}=(theta_X)*) + connect to qDimObj
conjugation symmetry."* That was written 2026-08-02 and is precisely the field
this trace independently arrives at from the mass side.

So the gap is **one identified axiom**, not an open research question, and
closing it has a traced consumer: `dim_q` feeds `G⁻¹` feeds the mass chain.
That makes it the highest-value next Lean item on this surface.

### Scope (a) — what this does NOT claim

It does **not** claim that closing `rtqd` improves any *number*. The chain above
is a **correctness/consistency** dependency: `qDim_conj` is currently an
unproved input that the Gram-inverse formula's derivation leans on. Improving
`m_p` or the `Δ_λ` binding magnitude is a separate question, and nothing here
touches the six failed `Δ_λ` ansätze or the `c_k` ladder.

Distinguish these carefully: *"the twist closes a proof gap in the mass chain's
derivation"* is what the evidence supports. *"the twist improves mass accuracy"*
is **not**, and would be exactly the over-claim the framework's own anti-
laundering rules exist to catch.

### Next

1. Add `twist_dual` to `BalancedCategory`, promoting it to a genuine
   `RibbonCategory`.
2. Derive `hSpherical` from it in the braided case.
3. Discharge `rtqd`'s `qDim_conj` — which then no longer needs `hTransport` as
   a bare hypothesis either, if the pivotal transport also follows.

Coordinate with `rtrb` (in-progress since 2026-08-02, stale) before starting.
