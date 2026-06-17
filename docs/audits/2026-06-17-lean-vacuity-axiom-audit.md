# Lean vacuity + provable-axiom audit

**Date:** 2026-06-17
**Branch:** `claude/sleepy-darwin-bokth1`
**Skill:** [`lean-proof-vacuity-audit`](../../.claude/skills/local/lean-proof-vacuity-audit.md)
**Scanner:** [`content/pipeline/lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
**Witness:** [`2026-06-17-lean-vacuity-axiom-audit.json`](2026-06-17-lean-vacuity-axiom-audit.json)

## Scope

Extends the `lean-proof-vacuity-audit` from an agent-only / grep-heuristic
checklist to a **runnable, repeatable scanner** over every `.lean` (library
trees + content-block siblings), and adds a **new category** requested by the
owner: an `axiom` that is a **candidate to prove**.

Categories (criterion ids — the first two mirror the skill; `proof-no-provable-axiom`
is new):

| criterion | what it flags | severity |
|---|---|---|
| `proof-no-trivial-true` | conclusion is `True` / a reflexive tautology (`x = x`) | major |
| `proof-no-self-assuming-projection` | body returns a conclusion-typed structure field verbatim (`:= d.claim`, `:= ⟨d.f1, d.f2⟩`) | critical |
| `proof-no-false-premise` | a hypothesis is impossible — vacuously true | major |
| `proof-no-decide-masking` | closed by `native_decide` (adds `Lean.ofReduceBool` to the axiom set) | critical |
| `proof-no-provable-axiom` **(new)** | an `axiom` with no `-- Ref:` / citation — should be proved or cited | major |

The scanner strips comments/docstrings before detection, and **exempts**:
- **sibling-resolution / docstub shadows** — a `: True := trivial` sibling whose
  real formalisation resolves elsewhere (the block's `lean.ref` or a docstring
  Lake-tree pointer maps to a real library decl). A `: True` stub with **no**
  resolvable real decl is a *genuine placeholder* and **is** flagged
  (`placeholder-true`).
- **field compositions that derive** (`Iff.intro`, `.trans`, `linarith`,
  `obtain …`) — not bare projections (the legit §3b-cond shape).

A `fail` is a **candidate**, not a verdict: detection is heuristic and
agent-confirmed per the skill's legit-vs-anti discriminator.

## Repository-state finding (why this audit is self-contained)

On `origin/main` (= this branch) the QA TypeScript pipeline — `qa-sweep.ts`,
`qa-criteria-registry.ts`, `qa-utils.ts`, `qa-checkers-*.ts`, and the schema
files `folio-assistant/schemas/{block-qa,lean-packages}.ts` — has been
**removed** (an in-progress migration). Only `content/pipeline/qa-agent-drain-queue.ts`
survives, and its `./qa-utils` / `./qa-criteria-registry` imports dangle. The
2323 `*.qa.json` sidecars remain as committed data, but their producing scripts
and the commit SHAs they cite are not on this line of history.

Consequently the documented `bun run content/pipeline/qa-sweep.ts … --only …`
workflow **cannot run here**. Rather than resurrect the whole removed pipeline
(which would fight the migration), this audit is delivered as a **self-contained
scanner** depending only on node builtins. The `block-qa/v1` sidecar types are
**inlined** in the scanner (the canonical schema home
`folio-assistant/schemas/block-qa.ts` is gitignored on this branch, so an import
from there would dangle on a fresh checkout). It emits the witness above and,
with `--write-sidecars`, upserts `reviewer.kind="script"` candidate entries into
the owning blocks' `.qa.json`.

## Run results (2026-06-17)

Scanned **1754** `.lean`; **197** defect candidates across **178** files; **39**
exempt shadows.

| criterion | candidates |
|---|---|
| `proof-no-trivial-true` | 130 (73 `conclusion-True`, 48 `placeholder-true`, 9 `reflexive-tautology`) |
| `proof-no-self-assuming-projection` | 22 (13 field-projection, 9 tuple-projection) |
| `proof-no-false-premise` | 9 |
| `proof-no-decide-masking` (`native_decide`) | 31 |
| `proof-no-provable-axiom` | 5 |

### `proof-no-provable-axiom` — all 5 (the actionable new category)

All in [`lean/QOU/BraidsKnots/LinearJSJVolume.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsKnots/LinearJSJVolume.lean):

- `AtomicKnot (Z N : ℕ) : Type` (l.10)
- `Vol (K : Type) : ℝ` (l.16)
- `Vol_p : ℝ`, `Vol_n : ℝ` (l.21–22)
- `JSJ_volume_additivity (Z N : ℕ) : …` (l.31)

`Vol(K)` is the hyperbolic volume in the canonical mass formula
`m(K) = m_e · Vol(K) · ρ(K) / ℏ_q²`. These uncited axioms are prime
prove-or-cite candidates — addressed in this PR.

### `proof-no-self-assuming-projection` — triage required

Many carry `[ctx : …Context]` / `[h : Class]` binders — the §3b-cond
conditional-class shape, which is **legit when the proof derives** and a
**defect when it bare-projects the conclusion field** (§3b-cond item 5,
non-degeneracy). Known prior verdicts to respect:
`MostowRigidity.mass_rigidity_of_mostow` and `MassGap.yangMillsMassGap_construction`
were assessed false-positive / ∃-repackaging (CLAUDE.md §7d U4) — confirm before
touching. The remainder (`q-beta-*`, `he4-*`, `SubstrateEWHypotheses`,
`r-matrix-braiding-structure`, …) need the per-decl discriminator.

## Drain plan (priority order)

1. **`proof-no-provable-axiom` (this PR).** Prove or cite the 5 `LinearJSJVolume`
   axioms.
2. **`self-assuming-projection` agent triage.** Per-decl legit-vs-anti; recipe-1
   genuine proof where vacuous; respect prior false-positive verdicts.
3. **`placeholder-true` (48).** Genuine `: True` gaps: honest fix is state the
   real proposition with `sorry` + `-- Ref:`, or **demote `theorem → conjecture`**
   — a **claim change requiring owner sign-off** (do NOT auto-commit).
4. **`native_decide` (31).** Advisory: replace with `decide` where it terminates
   to drop `Lean.ofReduceBool`; otherwise accept with a note.

Claim-changes (theorem→conjecture demotions, axiom removals that cannot be
proved) are surfaced for owner sign-off rather than auto-committed, per the
skill's recipe-4.
