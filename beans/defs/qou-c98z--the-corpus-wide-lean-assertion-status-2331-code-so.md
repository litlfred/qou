---
# qou-c98z
title: 'The corpus-wide Lean assertion status: 2331 code sorries, 435 files with no -- Ref: anywhere'
status: todo
type: task
priority: normal
created_at: 2026-09-11T14:48:36Z
updated_at: 2026-09-11T14:50:01Z
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
