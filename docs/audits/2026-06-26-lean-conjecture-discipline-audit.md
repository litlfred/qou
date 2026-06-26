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

**All resolved (0 remaining).** The three carriers the first pass surfaced are
now fixed:

- `QOU/AlgebraicSubstrate/PvsNPQou.lean` — empty marker → two content fields
  `strict_separation` (`P ⊊ BQP_q` for every ε>0) + `noncompressible`
  (separation survives ε→0). Block sidecar `p-vs-np-conjecture.qa.json` flipped
  fail → pass.
- `QOU/Interactions/QIntegerMassFormula.lean` — `IsAMEValue` empty predicate →
  two physical-invariant fields (`has_nucleon : 1 ≤ Z+N`, `binding_nonneg : 0 ≤ B_AME`),
  so `[IsAMEValue …]` is a genuine restriction.
- `QOU/BraidKnot/ShellNeutrality.lean` — `Saturated` is a genuine structural
  predicate whose full content awaits the `H_n(q)` Hecke import (parallel to
  `fullTwistTrivial`); given the documented `@marker` opt-out (intentional opaque
  tag, not accidental vacuity) rather than faked content.

### Resolved in this change

- `ReebEpsilon.lean` (+ `stochastic-mechanics/reeb-epsilon.lean`):
  `ArchimedeanInfinitesimal` empty marker → content-bearing `ReebPositive` +
  `ArchimedeanInfinitesimal` classes encoding positivity + archimedean smallness
  as real-parameter fields. Both derived as **primary** (roots). Finding +
  resolution recorded in `reeb-epsilon.qa.json`.
