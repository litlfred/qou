---
# qou-gzs0
title: 'Downstream: can the ribbon axioms close mass/binding derivation gaps'
status: in-progress
type: task
priority: normal
created_at: 2026-08-17T01:45:48Z
updated_at: 2026-08-17T17:40:29Z
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


## 2026-08-17 — HANDOFF: RibbonCategory landed; hSpherical is the next proof, NOT started

`RibbonFromBalanced.lean` (PR #5262, `244f3cf8`) has `RibbonCategory =
BalancedCategory + twist_dual`, stated **and inhabited** (`ribbonOfSymmetric`,
lean-direct exit 0).

### What remains, precisely

`KeystonePivotalSpherical` needs `hSpherical : leftQDim X = qDimObj X`. The two
differ in exactly one factor:

```lean
qDimObj  X = η_ X Xᘁ ≫ (β_ X Xᘁ).hom ≫ ε_ X Xᘁ
leftQDim X = η_ X Xᘁ ≫ (β_ Xᘁ X).inv ≫ ε_ X Xᘁ
```

so the goal reduces to relating `(β_ X Xᘁ).hom` and `(β_ Xᘁ X).inv` *under the
coevaluation/evaluation sandwich*. In the **symmetric** case they are equal
outright (`braiding_inv_eq_hom_of_symmetric`, already proved) — which is why
proving only the symmetric case would be **zero progress**: it needs no ribbon
structure at all.

The braided case is the real theorem (ribbon ⇒ spherical, Deligne/Yetter,
Bakalov–Kirillov ch. 2). It is a string-diagram argument in which the twist
mediates: `twist_dual` is what lets `θ` be pushed across the dual so the two
sandwiches become comparable. It needs several intermediate lemmas — at
minimum a `twist`-vs-`ev`/`coev` compatibility and a slide lemma — and is a
session of work, not a tactic call.

### Do not

- Prove the symmetric case and report it as progress. It was already provable.
- Add `leftQDim_eq` as a *field* of `RibbonCategory`. That is the §3b-cond
  rule-5 self-assuming projection: the class would carry the conclusion and the
  "theorem" would be `ctx.leftQDim_eq`. `SphericalStructure` already exists as
  the honest place for the hypothesis; the job is to *derive* it.

### Two method notes, because the same error happened twice this session

1. **B1** — I claimed Mathlib lacked `LeftRigidCategory (FGModuleCat K)` having
   grepped for the declaration. `inferInstance` proved it derivable in one step.
2. **The diamond** — I committed that the `KeystonePivotalSpherical` dodge "does
   not transfer". A 10-line probe showed it transfers exactly.

Both were "X is not available / does not work" judgements reached by reasoning
about the elaborator instead of asking it. **Test first.** The probe is seconds;
the retraction costs a commit and the reader's trust.

### Scope reminder for whoever continues

This whole arc is **derivation correctness**, not accuracy. `qDim_conj` is an
unproved input the Gram-inverse derivation leans on; closing it does not move
`m_p`, `Δ_λ`, or any `c_k`. The owner's actual question — mass and binding
accuracy — is still untouched and lives in the `Δ_λ` magnitude and the `c_k`
ladder, neither of which this arc reaches.
