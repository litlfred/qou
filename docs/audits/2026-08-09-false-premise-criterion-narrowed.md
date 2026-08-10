# `proof-no-false-premise` was 0-for-56 — narrowed at the producer

**Date:** 2026-08-09
**Branch:** `claude/issue-2472-analysis-qgqk7u`
**Scope:** `content/pipeline/lean-vacuity-axiom-audit.ts` (`detectFalsePremise`),
`docs/audits/lean-vacuity-review-ledger.json`

## Result

Every one of the **56** `needs-agent` candidates under
`proof-no-false-premise` / `discharged-impossible-hyp` is **legit**. Combined
with the 8 entries the June sweep had already cleared, the criterion was
**0-for-64** across the corpus: it has never produced a true positive.

The detector fired on the *presence of a contradiction inside a proof*. But
deriving a contradiction is how one proves a **negation** (`¬P`, `a ≠ b`) and
how one eliminates an **impossible branch of a case split** — both idiomatic,
and both saying nothing about whether the theorem's own premises are
satisfiable, which is what the criterion's name actually claims.

The old trigger was any of:

```ts
/\babsurd\b[\s\S]*?\bby\s+(norm_num|decide|simp|omega)\b/
/\bNat\.not_lt_zero\b/
/\(by\s+(norm_num|omega)\)\.elim\b/
```

`absurd … by decide` appears in essentially every negation proof in the tree,
so the criterion was a synonym for "this file proves a negative".

## What the 56 actually were

| Shape | Example | Why legit |
|---|---|---|
| Negation goal | `not_sameRow12_and_sameCol12` — `¬(sameRow12 ∧ sameCol12)` | `rintro` the conjunction, derive `1 = 2`, `absurd`. That *is* the proof of a negation. |
| `interval_cases` branch kill | `interaction_completeness` (BetaDecay) | Exhaustive bash over `r ∈ {2,3,4}`, `s ∈ {3..10}`; `absurd hcop (by decide)` kills the even-`s` non-coprime cases. |
| Empty index set | `jucysMurphy_zero` — `X₀ = 0` | `Nat.not_lt_zero` proves `{j | j < 0} = ∅`; the emptiness *is* the content. |
| Induction base case | `getD_replicate_of_lt`, `qPochDenom_eq_zero_at_pole` | The `zero` branch has `i < 0` in context. Textbook. |
| Term-mode side condition | Coxeter `braid_unconditional`, `far_commute_unconditional`, `isReduced_{ij,iji}_unconditional` | `letI hne := … (fun he => by subst he; exact absurd (M.diagonal i ▸ hm) …)` soundly *derives* `i ≠ j` from `M i j = 3` against `M i i = 1`. The statement is satisfiable for `i ≠ j`, so not vacuous. |
| Boundary case | `mass_eq_holonomy_of_flat` (`hN : M.N = 0`) | Empty-sum case of `mass = holonomy + Σ_{i : Fin N} dilog i`. `N = 0` is satisfiable. |
| Concrete-parity elimination | `crossing_A3` / `crossing_A4` | `he : Even 3` / `ho : Odd 4` are decidably false at the concrete `A`. |

`crossing_A4` and the two `sign_law_*` consumers were read in full precisely
because a vacuous claim there would touch the parity sign law; they are sound.

## The producer fix

`detectFalsePremise` now requires the three things the vacuity claim actually
needs, on top of the (unchanged, plus one widening) discharge pre-gate:

1. **`WHOLE_BODY_DISCHARGE`** — the body *is* the discharge. A nested `absurd`
   (inside a `letI`, a `fun … =>`, a `have`) is a side condition, not the goal.
2. **`LOCAL_CONTEXT_TACTIC` absent** — no `intro`/`rintro`/`rcases`/`cases`/
   `by_contra`/`induction`/`interval_cases`/`refine`/`subst`/`fun`/bullet.
   Any of these means the contradiction is local.
3. **Non-negative conclusion** — a `¬` / `≠` / `False` conclusion is *proved by*
   contradiction; that is content, not vacuity.
4. **The discharged term is one of the statement's own hypotheses** — a
   contradiction built from locally-derived facts is a proof step.

The pre-gate's `.elim` arm was also widened from `\(by norm_num\)\.elim` to
tolerate an inline type ascription (`(by norm_num : ¬P).elim h`) — the tighter
original spelling silently missed a genuinely vacuous shape.

Target shape, unchanged in intent:

```lean
theorem vacuous_claim (n : Nat) (h : n < 0) : n = 99 := absurd h (by omega)
```

## Verification

Synthetic probe (`scratchpad/fptest/Probe.lean`), 4 declarations:

| Decl | Shape | Expected | Got |
|---|---|---|---|
| `vacuous_claim` | unsatisfiable premise, whole goal | FIRE | FIRE |
| `vacuous_elim2` | `.elim` with ascription | FIRE | FIRE |
| `neg_goal` | `a ≠ 2` via `intro` + `absurd` | quiet | quiet |
| `case_branch` | `interval_cases` | quiet | quiet |

Full corpus: **2765 `.lean` scanned, 0 candidates** (was 64).

Ledger: 212 → 148 entries; the 64 `proof-no-false-premise` rows dropped by
`--review-ledger`'s resolved-candidate prune. All 78 `genuine` verdicts intact.
Remaining `needs-agent`: **66**.

> Run the ledger refresh on a **full** scan. With `--only CATEGORY` the
> candidate set is filtered but the prune loop is not, so it deletes every
> other category's entries.

## Why fix the producer rather than stamp the ledger

The June 2026 re-verification swarm already cleared 8 of these with the same
reasoning — `hecke_deg_monic`'s ledger evidence reads *"the discharged premise
is an impossible sub-case … not a vacuous whole-theorem premise"*. The detector
was left as-is, so 56 more accumulated, and every one of them would have gone
stale and demanded re-adjudication on the next touch of its file. A
zero-precision criterion that regenerates its own queue is worse than no
criterion: it trains agents to rubber-stamp the gate that is supposed to make
them look.
