---
# sp09
title: 'D [independent]: numSYT_mul_hookProduct (StandardYoungTableau.lean:113) — FRT hook-length'
status: completed
type: task
priority: low
created_at: 2026-07-05T16:30:00Z
updated_at: 2026-08-08T07:43:03Z
parent: sp00
---

Frame-Robinson-Thrall: numSYT(lam).prod(hooks)=n!. Needs NPS hook-walk (probability layer) or RSK. Famous, absent.

Parent: sp00.

## Precise bridge scope (2026-08-01, from PieceA general-n completion)

`numSYT_mul_hookProduct` (`QOU.BraidKnot`, StandardYoungTableau.lean) is NOT a
from-scratch HLF: the FRT formula is ALREADY sorry-free at
`QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct`
(HookLengthFormula.lean). Closing sp09 = two bridges:

  (1) hookProduct μ = QOU.Mathlib.hookLengthProduct μ  [TRACTABLE, ~40 lines]
      per-cell: StandardYoungTableau.hookLength (filter-arm-card + filter-leg-card
      + 1) = HookLengthFormula.hookLength (rowLen i - j - 1)+(colLen j - i - 1)+1,
      on cells. This is exactly PieceA.armZ_eq_card / legZ_eq_card (ℕ form) —
      filter-arm-card = rowLen i - j - 1. Product over μ.cells ⇒ cell-agreement
      suffices.

  (2) numSYT μ = QOU.Mathlib.numStandardYoungTableaux μ  [MODERATE, ~120-150 lines]
      Nat.card equality between two SYT encodings:
      - QOU.BraidKnot.StandardYoungTableau: standalone, entries 0-based {0..n-1},
        explicit inj_on/row_strict/col_strict.
      - QOU.Mathlib.StandardYoungTableau: 1-based {1..n}, wraps Mathlib
        SemistandardYoungTableau (toSsyt) + injOn_cells/mapsTo_cells.
      Build Equiv both directions (entry shift ±1; derive SSYT weak-row from
      strict, and strict from SSYT-weak+injOn). Then Nat.card_congr.

  Then numSYT_mul_hookProduct := numStandardYoungTableaux_mul_hookLengthProduct
  transported by (1)+(2). Part (2) is the real work; part (1) reuses PieceA.

## Grind findings 2026-08-01 (part 1 correct, but ARCHITECTURE blocks in-place)

Attempted to discharge numSYT_mul_hookProduct in StandardYoungTableau.lean by
importing QOU.Mathlib.HookLengthFormula → **IMPORT CYCLE**: HookLengthFormula's
cone transitively imports the custom QOU.BraidKnot.StandardYoungTableau (via
SpechtClassification/Syt* chain), so StandardYoungTableau.lean is UPSTREAM of
HookLengthFormula and cannot import it (Lean: "X already declared"). Reverted.

Consequences for the plan:
- The bridge theorem must live DOWNSTREAM of both StandardYoungTableau AND
  HookLengthFormula (a new file, or SytMathlibBridge.lean extended). The sorried
  `QOU.BraidKnot.numSYT_mul_hookProduct` in StandardYoungTableau.lean can stay as
  the honest cited sorry; prove the real bridged identity downstream.
- Part 1 (hookProduct = hookLengthProduct) is CORRECT — the two filter-card
  helpers (armFilter_card/legFilter_card, = my PieceA.armZ_eq_card in ℕ) + a
  prod_congr close it. Just place it downstream (needs HookLengthFormula's
  YoungDiagram.hookLength/hookLengthProduct). ~40 lines, ready-to-write.
- Part 2 (numSYT = numStandardYoungTableaux) is PARTIALLY DONE: SytMathlibBridge.lean
  already has `QOU.Mathlib.StandardYoungTableau.toBraidKnot` (Mathlib→custom
  direction) with 1 sorry. Finish the reverse (custom→Mathlib, entry +1 shift +
  SSYT row_weak/col_strict/zeros + BijOn onto Icc 1 n), then Equiv + Nat.card_congr.
  Build ON SytMathlibBridge, don't restart.

Next-session recipe: extend SytMathlibBridge.lean (imports custom SYT already):
add `import QOU.Mathlib.HookLengthFormula` there (check it's not in HLF's cone —
likely fine, it's a leaf bridge), prove part 1 + finish part 2's equiv, then the
downstream `numSYT_mul_hookProduct_bridged`.

## PART 2 DONE 2026-08-01 (the hard half) — SYT equiv sorry-free

`QOU.BraidKnot.numSYT_eq_numStandardYoungTableaux` LANDED (SytMathlibBridge.lean,
lean-direct exit 0, commit 45c351bbc1):
  numSYT μ = numStandardYoungTableaux μ
via row_mono/col_mono + toMathlib (BraidKnot→Mathlib SSYT+BijOn) +
toBraidKnot_toMathlib/toMathlib_toBraidKnot round-trips + mathlibSYT_ext +
Nat.card_congr. This closes the SYT-encoding bridge — the piece I'd flagged as
the real work.

REMAINING (mechanical, ~1 short session):
1. Part 1: hookProduct μ = YoungDiagram.hookLengthProduct μ. Exact proof (from my
   reverted StandardYoungTableau attempt, reuses PieceA idea):
     armFilter_card / legFilter_card (filter = image of Finset.Ioo; my
     PieceA.armZ_eq_card in ℕ) + Finset.prod_congr on cells. ~40 lines.
2. Final assembly (DOWNSTREAM file, e.g. new QOU/BraidKnot/NumSYTHookBridge.lean
   importing SytMathlibBridge + QOU.Mathlib.HookLengthFormula — leaf, no cycle):
     numSYT_mul_hookProduct_bridged μ : numSYT μ * hookProduct μ = μ.card.factorial
     := by rw [numSYT_eq_numStandardYoungTableaux, hookProduct_eq_hookLengthProduct,
             show μ.card = μ.cells.card from rfl];
        exact QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct μ
   (the sorried QOU.BraidKnot.numSYT_mul_hookProduct in StandardYoungTableau.lean
    stays as the honest cited sorry, OR is re-pointed once the downstream lands.)
   Needs the full HookLengthFormula cone built to verify (~40 modules).

## Summary of Changes — RESOLVED 2026-08-08

`QOU.BraidKnot.numSYT_mul_hookProduct` is **proved and axiom-clean**
(`#print axioms` → propext / Classical.choice / Quot.sound, no `sorryAx`).
`StandardYoungTableau.lean` now has **zero** sorries; full `lake build`
green at 4323 jobs.

Exactly the two bridges this bean specified, and the architecture note was
right: both had to live downstream of `StandardYoungTableau` AND
`HookLengthFormula`.

**Bridge (1)** — `hookProduct_eq_hookLengthProduct`, in
`QOU/BraidKnot/HookProductBridge.lean`. Sized here at ~40 lines; came in at
about 8, because the per-cell hook agreement was already available from
`qou-xevq`'s `hookLength_eq_rowLen_add_colLen`. Both sides reduce to
`(rowLen i − j) + (colLen j − i) − 1` on a genuine cell.

**Bridge (2)** — `numSYT_eq_numStandardYoungTableaux`, in the new
`QOU/BraidKnot/SytCountBridge.lean`.

`SYTEncodingBridge.lean` already had the 1-indexed ⟶ 0-indexed direction
(`toBraidKnot`) and the `≤` inequality, and its header named what was
missing: "the pigeonhole … together with weak-row monotonicity from
adjacent strictness; it is the remaining half of the bridge." That half is
what this adds:

- `entry_row_lt` / `entry_col_lt` (in `StandardYoungTableau.lean`) —
  strictness for arbitrary `j1 < j2`, since the structure fields only give
  adjacent steps.
- `toSsyt` — row-strictness weakened to the SSYT's `row_weak'`.
- `toSsyt_bijOn` — the pigeonhole: `SurjOn` from `InjOn` plus equal finite
  cardinality, via `Finset.surjOn_of_injOn_of_card_le`.
- `mathlibSyt_ext` — the 1-indexed structure carries no `@[ext]`.
- `sytEquiv` — the equivalence, reusing `SYTEncodingBridge.toBraidKnot`
  rather than redefining it.

**The theorem** transports
`QOU.Mathlib.numStandardYoungTableaux_mul_hookLengthProduct` (already
sorry-free) across both bridges. The sorry'd declaration was removed from
`StandardYoungTableau.lean` — it cannot be stated there, since
`HookLengthFormula`'s cone transitively imports that file — and replaced
by a section comment pointing downstream. Nothing referenced it in code;
all mentions were in prose.

### Snags worth recording

`omega` treats definitionally-equal terms as distinct atoms three separate
times: `μ.card` vs `μ.cells.card` (a reducible abbrev), `S.entry` vs
`S.toSsyt.entry`, and `j.succ` vs `j + 1`. Each needed the `rfl` equation
or `Nat.succ_eq_add_one` stated explicitly.
