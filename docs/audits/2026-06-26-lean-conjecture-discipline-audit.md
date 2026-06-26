# Lean conjecture-discipline audit — 2026-06-26

New checks in `content/pipeline/lean-vacuity-axiom-audit.ts` close a structural
blind spot: a conjecture axiomatised as a Lean `class`/`structure` can be
**sorry-free, axiom-free, and compile cleanly while asserting nothing**. The
existing proof-anti-pattern detectors all miss this — there is no proof term,
no `sorry`, and no `axiom` to inspect; the defect is in the *carrier*.

See AGENTS.md **§3b-tax** for the taxonomy and criteria definitions.

## Two content criteria (high-recall, agent-confirmed)

| Criterion | Severity | Fires on |
|---|---|---|
| `proof-no-empty-prop-carrier` | critical | a `class`/`structure : Prop` with zero fields (no `extends`); `@marker` opts out an opaque tag |
| `proof-claims-unencoded` | major | a carrier whose docstring enumerates ≥2 named properties not encoded as Prop fields |
| `proof-dependent-conjecture-not-conditional` | critical | doc explicitly claims conditionality on `conj:Y` while the type binds no such class (derived) |

## Primary/dependent is DERIVED, not tagged

A dependent conjecture takes its primary as an `[Instance]` hypothesis (§3b-cond)
— that edge is already in the Lean type. So the primary-vs-dependent split is a
graph computation over instance binders (`classifyConjectures`), **not** a hand
annotation. There is no "tagging backlog" to drain; the graph is recomputed each
run and recorded in the witness as `conjecture_graph`.

```
bun run content/pipeline/lean-vacuity-axiom-audit.ts content \
  --json docs/audits/2026-06-26-lean-conjecture-discipline-audit.json
```

Scope: 1770 `.lean` (library trees + content-block siblings).

## Findings

### Conjecture dependency graph (derived)

- **211** conjecture carriers total.
- **206 primary** (roots — bind no other conjecture class).
- **5 dependent**, with edges read directly from `[Instance]` binders:
  - `OmegaOrder → SurrealField`
  - `JonesBirthday → SurrealField`
  - `CrystalRMatrixSubLemma → CrystalGraphRealization`
  - `SaturatedShellConjecture → FullTwistContentFormula`
  - `WKBGreensFunction → ArchimedeanLimit`
- **0** `proof-dependent-conjecture-not-conditional` defects (no prose-claims-conditional-without-binder mismatches).

Full machine-readable graph + per-file flags: the `conjecture_graph` and
`flagged` keys of `2026-06-26-lean-conjecture-discipline-audit.json`.

### `proof-no-empty-prop-carrier` (critical) — empty marker carriers

Three genuine empty-`Prop` carriers remain after fixing `ReebEpsilon` (the
motivating case). Each asserts nothing; a downstream `[C]`-conditional result
built on it is vacuous. **Flagged for follow-up — not fixed here:**

- `QOU/AlgebraicSubstrate/PvsNPQou.lean:56` — `class PvsNPQou : Prop` (P-vs-NP;
  docstring admits "will become explicit `Prop` fields once …"). Sidecar fail
  written to `appendix-surreals/p-vs-np-conjecture.qa.json`.
- `QOU/Interactions/QIntegerMassFormula.lean:137` —
  `class IsAMEValue (Z N : ℕ) (B_AME : ℝ) : Prop` (library-only; witness-recorded).
- `QOU/BraidKnot/ShellNeutrality.lean:252` —
  `class Saturated (lam : YoungDiagram) : Prop` (no conjecture signal; likely an
  opaque predicate tag — add the `@marker` opt-out or give it content).

### Resolved in this change

- `ReebEpsilon.lean` (+ `stochastic-mechanics/reeb-epsilon.lean`):
  `ArchimedeanInfinitesimal` empty marker → content-bearing `ReebPositive` +
  `ArchimedeanInfinitesimal` classes encoding positivity + archimedean smallness
  as real-parameter fields. Both derived as **primary** (roots). Finding +
  resolution recorded in `reeb-epsilon.qa.json`.
