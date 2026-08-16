# Colour level (r = 2 vs r = 3) and the `TL_n` compute move

**Status: IN PROGRESS** — stub committed to open the PR; findings land as
commits on this branch.

Two tasks, both opened by PR #5234 and PR #5229.

## Task 1 — the 8-fold / colour question

PR #5234 measured that production colour runs `z_D` (level r = 2) and that
colour enters as a δ-perturbation on the p–n bond factor rather than as a
change of fibre, and on that basis dropped the eightfold line. The owner
asked for the question to be investigated rather than closed on one
measurement.

1. Independent re-verification of the per-file colour level, read from the
   code path (not from a registry row): solve `z_r = q^r/[r]_q = z` for `r`.
2. The question #5234 did not ask: *should* colour be at r = 3?
   `FibreDimensionForcesTL.lean:68-71` states colour needs a three-row block,
   hence a 3-dimensional fibre. Characterise the code-vs-Lean tension.
3. What fibre/level `bring_color_weighted` (canonical per owner ruling R3)
   implies, if any.
4. Numerology discipline: "level 3 is SU(3) and colour is SU(3)" is **not**
   evidence. State what would count as evidence.

## Task 2 — the `TL_n` compute move

`dim TL_n = Catalan(n)` vs `dim H_n = n!` (132 vs 720 at n = 6; 1430 vs 40320
at n = 8). Binding runs at `n = 3A`. Survey production consumers, separate
speed from correctness honestly, implement where clean and low-risk.

Existing bean: `qou-ondw` (high, TL_n compute move, PR #5230) — extended, not
duplicated.
