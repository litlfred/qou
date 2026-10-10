---
# qou-y4ca
title: Prove the two converses the iff-rename tranche left one-directional
status: todo
type: task
priority: low
created_at: 2026-10-10T07:29:24Z
updated_at: 2026-10-10T07:29:24Z
parent: b9cj
---

Spun out of `qou-bybn` on 2026-10-10 (PR #7546). That bean's own recommendation
was **option 2** — *prove* the missing direction where the converse is true —
for two of its thirteen members, and **option 1** (rename) for the rest. What
landed was option 1 for all ten renamed members, so these two converses are
still unproved and the honest `_iff_` name is still unavailable.

This is strictly additive content work, not a defect. Nothing is wrong in the
corpus today: both declarations now state exactly what they prove.

## The two

### 1. `denomPoly_eq_zero_of_factor_eq_zero`

`folio/quantum-observable-universe/mass-theory/q-pochhammer-partial-product.lean:66`
(renamed from `denomPoly_root_iff` in `a48ba4e4da`).

Proves one direction: `1 - x q^k = 0 -> denomPoly q x n = 0`.

The converse is **true over a domain** — a finite product vanishes iff one of
its factors does, which is `Finset.prod_eq_zero_iff` in Mathlib. So the full
biconditional is reachable and cheap, and proving it would let the name go back
to `denomPoly_eq_zero_iff` honestly.

Worth doing because of the arc this sits in: `qou-mfdq` documents the
corpus-grep trap where an agent asking *"is X <-> Y established?"* finds a
sorry-free `X_iff_Y` and stops. Supplying the real iff is the version of that
fix that leaves the useful name in place.

### 2. `eq_one_or_neg_one_of_offDiag_eq_zero`

`folio/quantum-observable-universe/lean/QOU/SchurWeyl/OffDiagNonvanishing.lean:45`
(renamed from `offDiag_eq_zero_iff`).

Also one direction. `qou-bybn` called this "the plausible one" for a converse
but did not measure it — so the first step here is to **decide whether the
converse is actually true**, not to assume it. A conclusion of the shape
`t = 1 or t = -1` has a converse that needs the off-diagonal entry to vanish at
*both* values, and that has not been checked.

**If it is false, that is the result**: record the scope-(a) negative and the
rename stands permanently.

## Cost / risk

Both are file-local; `qou-bybn` measured **zero consumers** for all thirteen
members, re-verified across `.ts`/`.md`/`.json`/`.py` (a `*.lean`-only grep
cannot see a `lean.ref` in a `.ts` manifest -- that was the first sweep's blind
spot). So neither proof can break a downstream reader, and neither rename-back
needs a consumer update.

Verify with `lean -DautoImplicit=false -s 65536 <file>`, never bare `lean` --
bare `lean` does not read the lakefile, so `autoImplicit` reverts to `true` and
an unbound identifier auto-binds instead of erroring.

## Default if nobody picks this up

Nothing changes and nothing is wrong. Both declarations keep their accurate
`_of_` names and the audit stays quiet. The only cost is that a true
biconditional the corpus could state remains unstated.
