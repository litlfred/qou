# Surreal re-scope execution — ledger rows + finite-page settle

**Date:** 2026-06-09 · **Branch:** `claude/surreal-rescope-ledger-rows-2026-06-09`
**Follows:** #1995 (merged) — the keep-and-re-scope verdict + narrowing ledger.

Picks up the two open checkboxes left on #1995:

## Task 1 — convert speculative `*-surreal-bound` blocks → ledger rows

The 5 millennium-problem blocks are currently `rem:` "bounds":
`rem:bsd-surreal-bound`, `rem:rh-surreal-bound`, `rem:yang-mills-surreal-bound`,
`rem:p-vs-np-surreal-bound`, `rem:collatz-surreal-bound`. Only `kashaev` from the
millennium set is a ledger row so far.

**Action:** add one narrowing-ledger row per block (narrowing + named residue +
L/E? tag), realizing the owner's "wherever appropriate" directive. The blocks
themselves stay (they are the worked statements); the ledger row is the
re-scoped index entry that replaces the "speculative bound" framing.

- [ ] BSD row
- [ ] RH row
- [ ] Yang–Mills row
- [ ] P-vs-NP row (already known **conditional** — the one conditional column)
- [ ] Collatz row

## Task 2 — settle finite-page vs perpetual-`ε^ω`

The rank-2 necessity question. The ledger §"essential candidate — RESOLVED to
language" already gives the two-tower reading (mass tower → E₁ collapse →
surreal-free; volume tower → perpetual but Mostow-convergent → L). Remaining:
make the finite-page side rigorous.

- [ ] Audit current state of `spectral-sequence-collapse` (mass-theory) +
      `motivic-perpetual-obstruction` / `perpetual-obstruction-depth-omega`
- [ ] Decide: is the E₁-collapse already formalized, or does it need a Lean
      lemma / rigorous writeup?
- [ ] Record the settled verdict (L) with its rigorous backing
