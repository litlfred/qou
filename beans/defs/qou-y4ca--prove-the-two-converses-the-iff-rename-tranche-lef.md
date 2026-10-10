---
# qou-y4ca
title: Prove the two converses the iff-rename tranche left one-directional
status: todo
type: task
priority: low
created_at: 2026-10-10T07:29:24Z
updated_at: 2026-10-10T08:25:13Z
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


## 2026-10-10 — item 1 is DONE, by a sibling session, hours after this bean opened

`570ee7fdb6` (session `016AEU7xkxdUcw9r7adTXgyr`, merged into
`claude/triangulation-citation-chain-2026-10-10`) proves it:

```lean
theorem denomPoly_eq_zero_iff [IsDomain R] (q x : R) (n : ℕ) :
    denomPoly q x n = 0 ↔ ∃ k < n, 1 - x * q ^ k = 0
```

Induction on `n` via `denomPoly_succ` + `mul_eq_zero`, **sorry-free**. Verified
here rather than taken on trust: `lean -DautoImplicit=false -s 65536` on
`q-pochhammer-partial-product.lean` → **errors=0**, file-wide `sorry` count **0**.
The two `unused variable` warnings the run reports are at line 141 in
`partialProduct_succ`, outside the diff (`@@ -77,6 +77,29 @@`), so pre-existing.

**The outcome is better than either option this bean framed.** The rename is
KEPT — `denomPoly_eq_zero_of_factor_eq_zero` remains as the reverse direction and
is cited by the new docstring — and the honest biconditional now exists
alongside it under the name the old one falsely claimed. So the corpus gained a
theorem rather than trading one name for another.

Their docstring also settles something this bean did not ask: `IsDomain` is
where the **forward** direction is used (a product of nonzero factors is
nonzero) and is **not removable** — over a ring with zero divisors the forward
direction fails. That is the right hypothesis, stated at the right strength.

### Item 2 is untouched and its first step is unchanged

`eq_one_or_neg_one_of_offDiag_eq_zero`
(`folio/quantum-observable-universe/lean/QOU/SchurWeyl/OffDiagNonvanishing.lean:45`)
is not addressed. **Do not assume its converse is true** — `qou-bybn` called it
"plausible" without measuring, and a conclusion of the shape `t = 1 ∨ t = -1`
needs the off-diagonal entry to vanish at *both* values for the converse to
hold. Measure that first. If it is false, the rename stands permanently and that
negative is the result (scope it (a) or (b) per AGENTS.md).

Bean stays `todo` on item 2 alone.


## 2026-10-10 — the owner had picked "prove the converse" OVER renaming, and the rename landed anyway

Recorded because the ledger should not read as if this were a free choice.

A peer session message (`016AEU7xkxdUcw9r7adTXgyr`), queued **07:20Z**:

> I am taking `denomPoly_root_iff`: the user picked "prove the converse as a
> real ↔" over renaming it, so please leave that one declaration out of your
> qou-bybn rename tranche.

**The rename commit `a48ba4e4da` is stamped 07:21Z** — one minute later. The
notification sat in this session's queue for an hour and was not read until
08:20Z, so the tranche was committed without it. A delivery lag, not a decision
to override the owner; stating the times rather than the conclusion.

### Where that leaves the declaration, measured

| line | declaration | origin |
|---|---|---|
| `:66` | `denomPoly_eq_zero_of_factor_eq_zero` | this branch's rename of the one-directional lemma |
| `:88` | `denomPoly_eq_zero_iff [IsDomain R]` | the peer's proof, `570ee7fdb6` |

`denomPoly_root_iff` survives in live source **nowhere**. Its four remaining
mentions are inside dated audit records (`docs/audits/2026-06-26-*`,
`docs/audits/2026-10-04-*`) and are deliberately left — rewriting a declaration
name inside a dated finding falsifies the record, the same call the `4.66e6`
drain made.

**The owner's choice is satisfied in substance: a real `↔` exists.** The
outcome is a superset of what was picked — the biconditional was proved AND the
one-directional helper now has a name matching what it states, which the new
docstring cites as its reverse direction.

**What is NOT what was picked: the name.** The `↔` is called
`denomPoly_eq_zero_iff`, not `denomPoly_root_iff`. If the owner wanted that
specific identifier carried onto the biconditional, that did not happen.

### Reversing it is one line, and the blast radius is measured

`denomPoly_eq_zero_iff` has **zero consumers outside its own file**
(`grep` over `folio/`, `computations/`, `scripts/`). So renaming it to
`denomPoly_root_iff` is a single-identifier edit in one file, verifiable with
`lean -DautoImplicit=false -s 65536` on that file alone.

**Not done on this session's initiative.** §ASK THE OWNER: it is neither a
precision fix nor corpus-derived — it turns on what the owner meant by their
pick, which only they can say. Left for them to call.
