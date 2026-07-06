# QA backlog proof drain — braids-and-knots (phase-1 pilot)

Following #1939, this is the phase-1 pilot of the proof-axis QA backlog
drain (AGENTS.md skill `local/integration-backlog`). One chapter = one PR.

## 4 critical proof-statement-integrity fixes

1. **q-casimir-unique** — md claims uniqueness up-to-scalar; Lean stated
   `Subsingleton (QCasimirData qs)` (literal uniqueness of the *parameter
   bundle*, the wrong proposition) propped by a wrong-proposition axiom.
2. **r-matrix-braiding-structure** — `lean.ref` had no matching decl; the
   YBE / braid-rep claims lived only in the docstring; malformed
   `hecke_relation` field.
3. **figure-eight-reeb-rotation** — `lean.ref` pointed at a vacuous
   tautology `(-1)^4 = 1 ∧ 2 = 2`.
4. **habiro-precision-ladder-equivalence** — the 3 propositions had type
   `True` / `∃ M, True` (placeholder tautologies); md's integrality /
   finiteness claim absent.

## Re-rate
Re-run proof-rater criteria over the chapter after fixes.
