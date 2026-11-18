---
# qou-c98z
title: 'What is actually proved in Lean: 4 sorry files corpus-wide, but 182 open conjectures — sorryAx is the wrong detector'
status: in-progress
type: task
priority: normal
created_at: 2026-09-11T14:48:36Z
updated_at: 2026-11-18T11:23:08Z
parent: qou-rtxm
---

**Question asked (owner, 2026-09-11): "all assertions proved in lean?"** Answer: **no**,
and the two senses of "assertion" in this repo have very different answers. Measured on
`main` `492a90a42e` (the merge of PR #7166), not quoted.

## Sense 1 — witness `assertions[]`: computational checks, NOT Lean

The word "assertion" in a `*.witness.json` means an entry of the `assertions[]` array
(`{name, passed, ...}` plus `allPassed`). These are Python checks a producer runs on its
own numbers. **They are not Lean theorems and are not backed by Lean.** AGENTS.md
§"Axiomatization is NOT a Proof" forbids conflating the two; recording the split here so
the question does not have to be re-measured.

| | count |
|---|---|
| witness files carrying an `assertions[]` array | 2468 |
| total computational assertions | 9550 |
| recorded as **failing** (`passed: false`) | **280** |

So even within the weaker sense, "all assertions pass" is false — 280 are recorded red.

## Sense 2 — Lean: how much of the corpus is actually proved

`content/**` excluding `.lake/` (the `.lake` trees are Mathlib and contaminate a naive
`find`/`grep` — a first pass here read **11774** files / 375 axioms / 1201 classes and all
three were wrong; `sorry` is the one count `.lake` does *not* inflate, since Mathlib has
none).

| | count |
|---|---|
| corpus `.lean` files | **3761** |
| files with a **code-position** `sorry` (line comments stripped) | **1051** (27.9 %) |
| code-position `sorry` occurrences | **2331** |
| declared `axiom` | 184 |
| conjecture-carrier `class ... : Prop` | 238 |

### The sharp number: 99

Splitting the 1051 by where they live:

- **884** are **library** files (`content/*/lean/**`) — no `.qa.json` sidecar, no block
  kind, covered by no per-block checker (the §"QA is agent-owned" gap).
- **167** are **content-block siblings**. By the sibling `.ts` block kind:

  | kind | files | reading |
  |---|---|---|
  | proposition | 66 | **gap** |
  | theorem | 11 | **gap** |
  | lemma | 5 | **gap** |
  | corollary | 4 | **gap** |
  | definition | 13 | **gap** |
  | conjecture | 49 | legitimate (§3b) |
  | remark | 15 | no logical claim |
  | (no `.ts`) | 4 | |

  => **99 blocks of a provable kind carry a `sorry`**; 49 are conjectures, where a `sorry`
  is the honest open-state marker and not a defect.

**99 is an UPPER bound on "block whose claim is unproved", and the measure is per FILE,
not per declaration.** Two ways it over-counts: a §3b-cond conditional-class file is
legitimate when the only `sorry` is the class instance; and a file can carry a `sorry` in
an auxiliary lemma while its headline declaration is discharged. Narrowing it needs a
per-declaration `#print axioms` pass for `sorryAx`, which was **not** run here — it needs
the restored olean cache and a real elaboration, and this was a counting pass.

### The `-- Ref:` discipline is not being kept

AGENTS.md §1 is unambiguous: *"A `sorry` without `-- Ref:` is always a review failure."*

| | count |
|---|---|
| `sorry` with a `-- Ref:` within the 3 preceding lines | **26 of 2331** |
| sorry-carrying files containing `-- Ref:` **anywhere** | 616 of 1051 (58.6 %) |
| sorry-carrying files with **no** `-- Ref:` at all | **435** |

The two rows bracket it: ≥ 435 files violate §1 outright (no citation anywhere in the
file, so no `sorry` in them can have one), and the 26 is what a strict adjacency read
gives. The truth is between, and the 435 is the one that needs no interpretation.

## Not swept, deliberately

Per the **2026-09-07 ASK-THE-OWNER directive** this is a measurement, not a drain. It is
neither of the two exemptions: it does not increase precision, and it is not
corpus-derived in the sense that lets a reviewer check it against an artifact — deciding
what each of the 435 should cite is judgement, 435 times. Prior work is
**single-instance** (`qou-w45u`, one file, completed as stale) plus the
`resolve-N-placeholders-in-<module>` family; **nothing owns the corpus-wide figure**, which
is why this bean exists.

**Next step if the owner wants it**, cheapest-first:
1. **Narrow 99 → the real gap** with a per-declaration `sorryAx` pass on the 99 provable
   blocks (needs the olean cache; `lean -DautoImplicit=false -s 65536`). This is the number
   that belongs in any honest statement of what the paper proves.
2. **The 435** are a discipline sweep and want one owner and a scoped sign-off; do not
   start it off this bean.


---

## 🛑 CORRECTION, SAME SESSION — every Lean figure above is WRONG, and all of them by a lot

The counts above came from a `sorry` scan that stripped **only `--` line comments**. Lean
also has **nestable `/- … -/` block comments, `/-- … -/` docstrings, and string literals**,
and *this corpus discusses `sorry` constantly in prose* — "sorry-free", "carries `sorry`
per §1a", "a naked `sorry`". Overwhelmingly the word is a **mention**, not a use.

Re-measured with a real stripper (nesting, docstrings and strings handled;
**self-tested** on a case carrying a docstring mention, a line-comment mention, a
block-comment mention, a string-literal mention and two genuine sorries — it returns
exactly the two):

| figure | reported above | **actual** |
|---|---|---|
| files with a code-position `sorry` | 1051 | **4** |
| `sorry` occurrences | 2331 | **9** |
| provable-kind blocks carrying one | 99 | **1** |
| files with **no** `-- Ref:` | 435 | **0** |
| declared `axiom` | 184 | **112** |
| conjecture-carrier `class … : Prop` | 238 | **237** |
| corpus `.lean` files | 3761 | 3761 ✓ |

**The `-- Ref:` finding was the worst of them and is fully retracted.** AGENTS.md §1 is
**kept**: all four sorry-carrying files cite. There is no 435-file discipline violation and
no sweep to propose. The whole "§1 is not being kept" section above is void.

### The four, in full

| file | block kind | reading |
|---|---|---|
| `observations/higgs-t28.lean` | conjecture | 3 sorries in the conjecture **instance** — §3b honest open-state |
| `nuclear-interactions/periodic-table-demand-conjecture.lean` | remark | 4, same pattern, canonical instance |
| `mass-theory/gram-determinant-plancherel-ratio.lean` | proposition | 1, in the **auxiliary** `gram_kappa_numerical_value`, two `-- Ref:` and a "**What is open**" docstring — §1a disposition 2, textbook |
| `fred2005-formal-groups/lean/Fred2005/FormalGroups.lean` | (library) | 1, cited to the literature, "stated here with `sorry`, cited, not re-derived" |

### Independent corroboration: a per-declaration `sorryAx` pass

Ran `#print axioms <lean.ref>` on all 99 of the (wrongly) flagged blocks, `lean`-direct
against the restored olean cache, `-DautoImplicit=false -s 65536`. Result: **77 resolved,
0 `sorryAx`, 0 compile errors**; 22 returned `Unknown constant` because their `lean.ref`
resolves to the library rather than the sibling (§0a candidate 2), not because anything
failed.

**The detector was self-tested before that number was believed**, because a test that has
never fired is not a verified test: on `theorem t : 2+2=5 := by sorry` it prints
`depends on axioms: [sorryAx]`, and on a `decide`-discharged twin `does not depend on any
axioms`. It fires.

## 🛑 And the corrected numbers do NOT mean the corpus is proved

This is the part that matters, and it is the reason `sorryAx` is the **wrong** detector for
the owner's question.

Under **§3b-cond**, an open conjecture is carried as a `class C : Prop` with **no
instance**, and downstream results take `[C]` as a hypothesis. Such a theorem is genuinely
sorry-free *and* `#print axioms` reports **no** `sorryAx` — there is no `sorry` anywhere,
the conjecture is simply *assumed*. That is precisely AGENTS.md
§"Axiomatization is NOT a Proof": *"creating an `axiom`, `sorry`, or a conditional `class`
… does NOT count as proving it."*

So **"0 sorryAx" measures that the corpus uses classes, not that it proves things.** The
unproved content lives in:

| | count |
|---|---|
| content blocks of kind **`conjecture`** (declared open) | **182** |
| conjecture-carrier `class … : Prop` | **237** |
| declared `axiom` | **112** |

against **770** provable-claim blocks (632 proposition, 67 theorem, 52 lemma, 19 corollary)
of 3193 total.

**Answer to "all assertions proved in lean?": no — but the gap is not `sorry`, it is the
182 declared conjectures and the class-conditional results downstream of them.** The
corpus is honest about this by construction; the `sorry` count was never the right place to
look, and my first pass looked there and then miscounted it.

## What would actually answer the question

Not another `sorry` scan. The real measurement is: **for each of the 770 provable-claim
blocks, is its Lean declaration unconditional, or does its signature bind a conjecture
class?** A `[C]` binder in the type *is* the dependency edge (§3b-tax says the taxonomy is
derived from exactly this), so it is statically extractable from the declaration signature —
no elaboration needed. That number — unconditional vs conditional-on-an-open-class — is the
honest statement of what the paper proves, and nothing in the corpus currently reports it.

Filed as the real next step here rather than in a new bean. **Not started** — it is a
measurement, so the 2026-09-07 ASK-THE-OWNER directive does not gate it, but it is a real
piece of work and should not be started while the owner may want something else.


### The number that actually answers the question: **187**

Measured directly — for every `class … : Prop` in the corpus, does *any* `instance` of it
exist anywhere in `content/**`?

| | count |
|---|---|
| conjecture-carrier `class … : Prop` **declarations** | 237 |
| of those, **distinct names** | 234 |
| names with **at least one instance** | 47 |
| names with **NO instance** — the honest open state | **187** |

A class with no instance is an assumption that is **stated and not discharged**. Every
`[C]`-conditional theorem downstream of one is sorry-free, passes `#print axioms` with no
`sorryAx`, and is still **conditional on an open conjecture**. That is the whole content of
AGENTS.md §"Axiomatization is NOT a Proof", and **187 is its size**.

So the answer to *"all assertions proved in lean?"* is: **no — 187 open class-carried
assumptions**, not 2331 sorries and not 4 either. The `sorry` count answered a different
question, and both of my answers to it were wrong before this one.

Sample of the 187, to make clear these are not bookkeeping stubs but the framework's own
open problems: `AlphaEmFixedPointNormalization`, `BindingFollowsQBesselKernel`,
`BlochSuslinUniqueness`, `BlochWignerInjective`, `BarOddLadderShape`,
`ArchimedeanRemainderExponentialDecay`, `AtomicJSJDecomposition`.

**Caveat, stated because it bounds the number in the direction that matters:** the instance
search is a textual `instance … : Name` match over the stripped corpus, so it can miss an
instance supplied by `derive`, by an anonymous-constructor `instance` whose type is a
definitional alias, or from outside `content/**`. Every such miss moves a class from the
187 into the 47, so **187 is an upper bound on the open set** — and 47 is a lower bound on
the discharged set, which is the conservative direction for a claim about what is proved.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `(none)` → `qou-rtxm`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

- Round 83 (`lane-e667`): Formalized `qou-xc8t`, `cdup`, `qdzu`, `qou-9e7p`, `qou-c98z` in `QOU.Foundations.TruncatedJetMinorStabilityCellAxialContentBridgePrecisionFloorSignSeparationOrderedImportInheritanceConjectureAuditLedger` with 80-dps `mpmath` 2-commit witness stamp (`aa00fee380c7d4aad9c2a05a9bab09078a582bd9` -> `36e5ef216683fe9a0a37836e3fbfd0bf5fd7ed3a`, `scriptHash=0bcb4f55d2e1bf88729ec0af6984c5f97ce5fe17beee4851f2d6cc29ea159aa8`) in PR `litlfred/qou#8446` (`status: in-progress`).
