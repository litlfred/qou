---
# qou-nrex
title: 'EPIC: RSK inverse — reverse bumping to the Robinson-Schensted bijection (taken over from the Schensted programme)'
status: todo
type: milestone
created_at: 2026-08-16T02:46:29Z
updated_at: 2026-08-16T02:46:29Z
---


## Why this epic exists, and what it is NOT for

The Schensted programme in `QOU/Mathlib/Schensted*.lean` is further along than its own brick-1
docstring says: the forward map is built through **brick 11**,
`SchenstedPairingMap.rskPair : Equiv.Perm (Fin n) → Σ_λ SYT(λ) × SYT(λ)`. Taking it over means
continuing from there, not restarting.

**Do not spend a session proving `rskPair` injective.** That yields `n! ≤ Σ_λ (f^λ)²`, and that
inequality is *already proved by an unrelated route*:
`BraidKnot.SpechtActionInjective.factorial_le_sum_sq` (injectivity of the Specht action map,
merged as PR #5189). Both programmes deliver the same direction. The non-redundant content is the
**inverse map** — reverse bumping — which is what gives surjectivity and hence the identity.

## Bricks

1. **DONE** — `SchenstedReverseRow.lean`: `rowUninsert` (reverse row insertion), the inversion
   law `rowUninsert_rowInsert`, plus `_length` / `_sorted` invariants and the three helper
   lemmas (`mem_rowUninsert`, `forall_le_of_rowUninsert_none`,
   `exists_lt_of_rowUninsert_some`). Sorry-free; `#print axioms` reports **`propext` alone** —
   no `Classical.choice`, no `Quot.sound`. Pure constructive combinatorics.
2. the cascade: undo `insertRec` across rows, driven by the recording tableau's largest timestamp;
3. recover the word: iterate the cascade to invert `insertWordRec`;
4. `rskPair` is bijective;
5. the cardinality count: `RSKBurnsideHolds n` for general `n`.

## What lands when brick 5 does

`BraidKnot.SpechtWedderburnCriterion.spechtEquiv_of_sum_sq` turns it straight into the general
Wedderburn split `k[S_n] ≃ₐ[k] ∏_μ End_k(S^μ)`, which is `sn_isotypic_specht_split` — the last
open gap of the OV cone, and hence the `sorryAx` on `RSKBurnsideHolds`'s two downstream keystones.
The `n ≤ 12` case of that split is already unconditional (PR #5197) via
`PartitionsOfBridge.rskBurnsideHolds_le12`, which uses **no** RSK at all.

Also note `RSKBridge.RSK_substrate_axiom` is a real `axiom` asserting brick 5's statement. Closing
brick 5 lets it be deleted; until then, check `#print axioms` on anything claiming the identity.

## Brick 2 DONE — the reverse cascade

`QOU/Mathlib/SchenstedReverseCascade.lean`, sorry-free (`uninsert_insert` axioms: `propext`,
`Quot.sound`; the two helpers: `propext` alone):

- `newRowIndex T x` — which row `insert T x` appends to, by the same recursion `insert` uses, so
  it records rather than searches;
- `uninsert T i` — remove the last cell of row `i`, push the displaced value up through rows
  `i-1 … 0` by `rowUninsert`;
- **`uninsert_insert`** — `uninsert (insert T x) (newRowIndex T x) = (T, some x)`.

**Two side conditions, both needed and both preserved.** `RowsSorted` is what brick 1's
`rowUninsert_rowInsert` consumes on each undone row. `NoEmptyRows` is what lets `uninsert` decide
at the target row between *shortening* a row and *deleting* it — a row that had one cell and loses
it must go, or the tableau grows a spurious empty row and shapes stop matching. `insert` preserves
both (`insert_rowsSorted` upstream; `insert_noEmptyRows` added here), so the cascade composes and
brick 3 can iterate it without re-establishing them.

Also proved on the way: `rowInsert_eq_append_of_none` — a no-bump insertion is literally
`r ++ [x]`, which is what makes `dropLast`/`getLast?` the right inverse at the target row.

**Next (brick 3):** iterate `uninsert` to invert `insertWordRec`. The row index to undo at is not
free — it is where the *largest* recording timestamp sits, and `SchenstedRecording`'s
`insertWordRec_snd_content` (content is exactly `range |w|`, each timestamp once) is what makes
"the largest" well-defined. Expect the work to be locating that cell, not the undoing.
