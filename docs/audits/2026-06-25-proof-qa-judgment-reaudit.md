# Proof-QA judgment + rater re-audit (follow-up to PR #2775)

**Date:** 2026-06-25
**Branch:** `claude/proof-qa-judgment-reaudit-2026-06-25`
**Predecessor:** [PR #2775](https://github.com/litlfred/qou/pull/2775) (merged `db52522`)
drained the deterministic proof-QA false positives and **invalidated** the
1,680 unreliable judgment + rater verdicts from the 2026-06-22 `qa-agent-drain`
batch → `n/a` *pending canonical re-sweep*.

## This pass

The canonical `qa-sweep` (folio-assistant) is out of session scope (403), so
this performs the per-block agent re-audit directly: for each of the **360
blocks** whose 4 judgment + 3 rater criteria were invalidated, a sub-agent reads
the `.md` claim + the resolved Lean (sibling or `lean.ref` library decl) and
records a considered verdict, superseding the `n/a` placeholder.

Unlike the 2026-06-22 batch (templated — e.g. "contains sorryAx" notes on
sorry-free files), each verdict here cites block-specific evidence.

### Criteria + rubric

| criterion | PASS | FAIL |
|---|---|---|
| `proof-statement-integrity` | Lean statement faithfully encodes the `.md` claim; no `sorry`/`admit`/`native_decide` masking; no degenerate weakening | Lean proves a weaker/different claim (`Nonempty` via trivial instance, `: True`, self-projection); or unexpected axioms / `sorryAx` |
| `proof-no-self-assuming-projection` | proof derives the conclusion | proof just returns a hypothesis/structure field that *is* the conclusion (`:= ctx.foo`) |
| `proof-no-unused-hypotheses` | every binder is used | a hypothesis/instance binder is never referenced in the body |
| `proof-no-false-premise` | premises are satisfiable | a premise is contradictory ⇒ vacuously true |
| `proof-rater-goal-plausibility` | score ∈ [0,1] — is the goal well-posed and substantive? | (`< 0.66` = open) |
| `proof-rater-strategy-clarity` | score — is there a clear proof strategy? | (`< 0.66` = open) |
| `proof-rater-novelty` | score — does it add something beyond a restatement? | (`< 0.66` = open) |

`n/a` when no Lean resolves (6 blocks).

Tool: [`scripts/reaudit_verdict.py`](../../scripts/reaudit_verdict.py) (append a
fresh agent verdict; disjoint batches → parallel-safe).

## Caveat

A fresh Opus agent re-audit is **not more authoritative** than the canonical
checker; this is a best-effort interim re-audit until `folio-assistant`'s
`qa-sweep` can run. Verdicts are evidence-cited and reversible via git.
