---
# vrfw
title: 'GAP (fixed): ⟨…, rfl⟩ witnesses were invisible to proof-no-unused-hypothesis-rfl — the gate could not see what the standalone audit flags'
status: completed
type: bug
priority: high
tags:
    - lean
    - vacuity
created_at: 2026-08-08T16:20:00Z
updated_at: 2026-09-26T11:03:15Z
---

Claimed and finished on `claude/vacuity-anon-rfl-witness-2026-08-08`.

## The gap

`scripts/lean-vacuous-existential-audit.py` flags ten `rfl-witness`
declarations, and `docs/audits/2026-08-07-lean-vacuous-existential-audit.json`
records them. The **live detector** — `content/pipeline/lean-vacuity-axiom-audit.ts`,
the one CI runs and the QA sidecars derive from — flagged **none of the ten**.

Verified by running it, not by grepping the audit docs (the method note in
`qou-z3k1` is right, and it is why that check was done this way).

The mechanism is one regex. `detectUnusedHypothesisRfl` opens with

    if (!RFL_BODY.test(body)) return undefined;

and `RFL_BODY` matches only a body that *is* `rfl` — `rfl`, `by rfl`,
`by unfold …; rfl`. These proofs are anonymous constructors:

    theorem nuclear_knot_classification (Z N : ℕ) (hA : Z + N ≥ 4) :
        ∃ K : NuclearKnotType, K = .borromean := by exact ⟨.borromean, rfl⟩

`⟨.borromean, rfl⟩` consults `hA` exactly as little as a bare `rfl` does — the
witness is handed over and `rfl` closes the equation — but the body is an
anonymous constructor, so the detector returned before looking at a single
binder. A statement could bind any number of decorative hypotheses and stay
invisible.

## The fix

`ANON_RFL_BODY` alongside `RFL_BODY`, matched against a whitespace-collapsed
body so the `by`-block form is covered by the same pattern.

One tightening was **required**, not cosmetic: a bare `rfl` mentions nothing,
but an anonymous constructor supplies a witness that can be built from a
hypothesis (`⟨h.choose, rfl⟩`), and then the binder is load-bearing. The
detector now also skips a binder whose name occurs in the **body**. That check
is a no-op for the `rfl` shapes and necessary for this one.

New witness patterns `rfl-witness-with-unused-hypothesis` /
`rfl-witness-with-underscored-hypothesis`, so the two shapes stay
distinguishable in the ledger.

## Measured — exactly four, nothing lost

The committed audit JSON is badly stale (see `vaud`), so the delta was measured
against a **freshly regenerated baseline** rather than the committed file:

| | hits | defects |
|---|---|---|
| fresh baseline, unmodified detector | 203 | 122 |
| with this change | 207 | 126 |

Set-diff on `(file, line, category, decl)`: **4 added, 0 removed.**

| declaration | binds | proof |
|---|---|---|
| `nuclear_knot_classification` | `hA : Z + N ≥ 4` | `by exact ⟨.borromean, rfl⟩` |
| `spectral_decomposition_qvalue` | `hq`, `hp`, `hd`, `hm…` | `⟨bareQValue …, rfl⟩` |
| `wenzl_annihilator` | `_h : 4 ≤ firstCol` | `⟨0, rfl⟩` |
| `universal_habiro_closure` | `hq : 0 < q` | `by exact ⟨rfl, rfl⟩` |

All four read and confirmed genuine. `universal_habiro_closure` is **not** in
the ten the Python audit found — its conclusion is a conjunction of definitional
equalities, not `∃ x, x = e`, so the widened rule reaches a shape that audit
does not.

`wenzl_annihilator` is worth singling out: its docstring is candid — *"Stated as
a structural target; a full proof needs the Wenzl projector machinery not yet in
Mathlib"* — while the statement `∃ chi, chi = 0` proved `⟨0, rfl⟩` says only
that `0` exists. Honest prose, vacuous declaration, and nothing that gates could
see it.

## Not closed by this, and deliberately

`knot_factor_amphicheiral` stays invisible, for two pre-existing reasons this
change does not touch:

- its binder type `Amphicheiral β β_mirror altPartition` carries no relational
  token, so `PROP_SHAPED` reads it as data — the documented precision trade-off;
- `_off_block_norm`'s type nests parentheses two deep, and the binder regex
  handles one level.

Both are real limits of the existing rule. Widening either changes the
false-positive profile and wants its own measurement.

## CI impact — none for this PR, correct for future ones

The two gates in `.github/workflows/lean-content-siblings.yml` are diff-scoped:
`--fail-on proof-no-trivial-type-mismatch,lean-import-after-content` (this
category is not in it) and `--check-ledger`, which fails only when a `.lean`
file **the PR changes** carries a candidate lacking a fresh verdict. This PR
changes no `.lean` files. Future PRs touching those four will now need ledger
verdicts — which is the point.

Draining the four is separate work: `wenzl_annihilator` needs Wenzl projector
machinery, and the others are content claims, not detector bugs.
