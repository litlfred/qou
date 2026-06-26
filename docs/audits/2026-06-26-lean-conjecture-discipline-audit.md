# Lean conjecture-discipline audit — 2026-06-26

New checks added to `content/pipeline/lean-vacuity-axiom-audit.ts` to close a
structural blind spot: a conjecture axiomatised as a Lean `class`/`structure`
can be **sorry-free, axiom-free, and compile cleanly while asserting nothing**.
The existing proof-anti-pattern detectors all miss this because there is no
proof term, no `sorry`, and no `axiom` to inspect — the defect lives in the
*carrier*, not in a proof.

See AGENTS.md **§3b-tax** for the taxonomy (primary vs dependent conjecture),
the `@conjecture: primary|dependent` annotation, and the criteria definitions.

## New criteria

| Criterion | Severity | Fires on |
|---|---|---|
| `proof-no-empty-prop-carrier` | critical | a `class`/`structure : Prop` with zero fields (no `extends`); opt out an opaque tag with `@marker` |
| `proof-claims-unencoded` | major | a carrier whose docstring enumerates ≥2 named properties not encoded as Prop fields |
| `proof-conjecture-unclassified` | major | a conjecture carrier with no `@conjecture: primary\|dependent` annotation |
| `proof-dependent-conjecture-not-conditional` | critical | a `@conjecture: dependent` class not stated conditionally on its primary |

## Run

```
bun run content/pipeline/lean-vacuity-axiom-audit.ts content \
  --json docs/audits/2026-06-26-lean-conjecture-discipline-audit.json
```

Scope: 1770 `.lean` (library trees + content-block siblings).

## Findings

### `proof-no-empty-prop-carrier` (critical) — empty marker carriers

Three genuine empty-`Prop` carriers remain after fixing `ReebEpsilon`
(the motivating case). Each asserts nothing; a downstream `[C]`-conditional
result built on it is vacuous. **Flagged for follow-up — not fixed here**
(out of scope for this change):

- `QOU/AlgebraicSubstrate/PvsNPQou.lean:56` — `class PvsNPQou : Prop`
  (P-vs-NP; docstring admits "will become explicit `Prop` fields once …").
  Sidecar fail written to `appendix-surreals/p-vs-np-conjecture.qa.json`.
- `QOU/Interactions/QIntegerMassFormula.lean:137` —
  `class IsAMEValue (Z N : ℕ) (B_AME : ℝ) : Prop` (library-only; witness-recorded).
- `QOU/BraidKnot/ShellNeutrality.lean:252` —
  `class Saturated (lam : YoungDiagram) : Prop` — pattern `empty-prop-class`
  (no conjecture signal); likely an opaque predicate tag. Either add the
  `@marker` opt-out or give it content; **agent review required**.

### `proof-conjecture-unclassified` (major) — taxonomy backlog: 335

Every existing conjecture carrier predates the `@conjecture:` annotation, so
335 are flagged as unclassified. This is the **adoption backlog**, not 335
distinct bugs — each needs a one-line `@conjecture: primary` or
`@conjecture: dependent on conj:<label>` tag (and, if dependent, confirmation
that it is stated conditionally). Top areas:

| Count | Area |
|---|---|
| 164 | `lean/` library tree |
| 70 | `mass-theory/` |
| 20 | `particle-interactions/` |
| 17 | `mass-endomorphism/` |
| 13 | `predicted-spectra/` |
| 12 | `appendix-surreals/` |

Full machine-readable list: `2026-06-26-lean-conjecture-discipline-audit.json`.

To avoid flooding 335 sidecars in one pass, only the critical
`proof-no-empty-prop-carrier` fails were written to sidecars. The unclassified
backlog should be drained incrementally (one chapter at a time, agent-confirmed).

### Resolved in this change

- `ReebEpsilon.lean` (+ `stochastic-mechanics/reeb-epsilon.lean`):
  `ArchimedeanInfinitesimal` empty marker → content-bearing
  `ReebPositive` + `ArchimedeanInfinitesimal` primary-conjecture classes,
  classified `@conjecture: primary`. Sidecar updated with the finding +
  resolution (`reeb-epsilon.qa.json`).
