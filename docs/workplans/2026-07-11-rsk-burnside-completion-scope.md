# RSK → Burnside `Σ_λ (f^λ)² = n!` — completion scope

**Goal.** Discharge Identity-I axiom (i), the Burnside/RSK cardinality identity
`Σ_{λ ⊢ n} (f^λ)² = n!` (`f^λ = #SYT(λ)`), for **general `n`** — currently the
last standing axiom/`sorry` blocking the `Sₙ`-representation infrastructure.
Two in-repo encodings target it:

| Encoding | File | Partition type | Status |
|---|---|---|---|
| `RSKBurnsideHolds n` | `QOU/Mathlib/RSKBurnsideTarget.lean` | Mathlib `Nat.Partition n` + `numStandardYoungTableaux` | canonical; **n ≤ 12 proved** (`rskBurnsideHolds_le12`), general axiomatised (`RSKBridge.RSK_substrate_axiom`) |
| `burnside n …` | `QOU/BraidKnot/DeltaLambdaSignRule.lean` | repo list-based `Partition`, `dimIrrep = n!/∏hooks` | general `sorry`; **n ≤ 5 finite `decide` checks** (`burnside_check_1…_5`, 2026-07-11) |

Both reduce to the same mathematics; the canonical target is `RSKBurnsideHolds`.
A future bridge lemma `burnside ↔ RSKBurnsideHolds` would let the
`DeltaLambdaSignRule.burnside` sorry inherit the RSK discharge (deferred; the
two use different `Partition` encodings).

## The reduction already in place (do not rebuild)

- `RSKBurnsideTarget.dimSYT p = numStandardYoungTableaux (partitionShape p)` —
  genuine SYT count via Mathlib `YoungDiagram`.
- `IdentityIHLFBridge`: `dimSYT p = dimHLF (toList p)` (Frame–Robinson–Thrall
  hook-length formula) **proved**, so `RSKBurnsideHolds n` is equivalent to a
  **computable** `dimHLF` sum (`rskBurnsideHolds_iff_dimHLF`).
- `PartitionsOfBridge.rskBurnsideHolds_le12` — the identity **proved for
  n ≤ 12** via `decide` through that equivalence.
- `RSKBridge`: the `RSKBijection` class + `RSK_substrate_axiom n :
  RSKBurnsideHolds n` (the one honest axiom), plus `BurnsideFromRSK` deriving
  the identity from any genuine instance.

**So the ONLY missing piece for general `n` is the Robinson–Schensted
bijection `Sym n ≃ Σ_{λ⊢n} SYT(λ) × SYT(λ)` and its cardinality count.**
Pinned Mathlib has `Mathlib.Combinatorics.RSK` (partial) but not the
cardinality consequence; the repo builds it brick by brick.

## Brick status — `QOU/Mathlib/SchenstedInsertion.lean` (**0 sorry**)

| Brick | Content | Status |
|---|---|---|
| 1 | `rowInsert` (single-row Schensted bump) + `mem_rowInsert`, `rowInsert_length_{none,some}`, `rowInsert_sorted` | ✅ proved |
| 2 | `insert` (bumping cascade), `insertWord` (P-tableau), `RowsSorted`, `insert_rowsSorted`, `insertWord_rowsSorted` | ✅ proved |
| 3 | `totalCells`, `insert_totalCells`, `insertWord_totalCells` (`|P(w)| = |w|`) | ✅ proved |
| 4 | `bumpMs`, `content`, `rowInsert_content`, `insert_content`, `insertWord_content` (`content(P(w)) = ↑w`) | ✅ proved |
| 5 | **bumping lemma** — `StrictBelow`/`ColStrict`, `bump_findIdx_mono`, `strictBelow_bump_step`, `insert_colStrict`, `insertWord_colStrict` (`P(w)` columns strictly increase ⇒ `P(w)` is semistandard) | ✅ proved (building blocks PR #3535; cascade PR #3565) |
| 6a | **recording tableau `Q` — shape** — `insertRec`, `tableauShape`, `insertRec_fst_eq_insert`, `insertRec_shape`, `insertWordRec_shape_eq_P` (`Q(w)` has the same shape as `P(w)`) | ✅ proved (seed, PR #3565) |

## Remaining bricks (each a dedicated multi-hour PR)

6b. **Recording tableau `Q` — standardness** — prove `Q(w)` is *standard*:
   entries `1…n` (each step index used once, in cell-creation order) strictly
   increasing along rows and columns. Builds on the shape match (`6a`) plus
   `insertWord_colStrict`. The step index only ever appends at a row end and is
   monotone increasing, so rows/columns of `Q` inherit strictness structurally.
7. **RSK map** — `w ↦ (P(w), Q(w))` as a function `Sym n → Σ_λ SYT(λ)²`
   (restricting to permutation words / two-line arrays for the `Sₙ` count).
8. **Inverse (reverse bumping)** — reconstruct `w` from `(P, Q)`; prove it is a
   two-sided inverse of Brick 7.
9. **Bijection** — assemble Bricks 7–8 into `Equiv (Sym n) (Σ_λ SYT(λ)²)`.
10. **Cardinality** — `Fintype.card_congr` + `Fintype.card_sigma` +
    `Fintype.card_prod` ⟹ `n! = Σ_λ (#SYT λ)²`, discharging
    `RSK_substrate_axiom` / `RSKBurnsideHolds` and closing `burnside`.

## Risks / dependencies

- **Mathlib SYT count API.** `numStandardYoungTableaux` is a `Nat.card` over a
  `Finite` SYT type; Brick 10 must match the repo's `partitionShape`/`dimSYT`
  to Mathlib's `YoungDiagram` SYT count exactly (the `partitionShape` glue is
  in place).
- **`Nat.Partition n` Fintype API** is upstream-dependent (noted in
  `RSKBridge`); the cohort/`List` route (`CohortRSKWitness`) is the fallback if
  the sigma-over-`Nat.Partition` count fights Mathlib.
- **Brick 5 (the bottleneck) is now closed.** The bumping lemma
  (`strictBelow_bump_step` + `insert_colStrict`) is where most RSK
  formalisations spend their effort; it is proved sorry-free. The next
  bottleneck is Brick 8 (reverse bumping / inverse), the second-hardest.

## Recommended next action

**Brick 6b (recording-tableau standardness).** The shape foundation (6a) is in
place: `insertRec` threads `Q` alongside `P`, `insertRec_fst_eq_insert` shows
the P-component is untouched, and `insertWordRec_shape_eq_P` gives `Q(w)` the
same shape as `P(w)`. What remains is proving `Q(w)` **standard**: the step
index `s` is strictly increasing and each new cell (an append at a row end, per
the `insertRec` none/new-row branches) receives the current `s`, so rows and
columns of `Q` are strictly increasing by construction. Reuse
`insertWord_totalCells` (each step adds one cell ⇒ entries are exactly `0…n−1`)
and mirror the `insertRec_shape` induction to track the per-row `Q` monotonicity.

_Reconnaissance + scope authored 2026-07-11. Bricks 1–5 sorry-free
(Brick 5 completed 2026-07-11, PRs #3535 + #3565); Brick 6a (Q shape) seeded
2026-07-11 (PR #3565). This doc maps the remaining chain so any session can
resume at Brick 6b without re-deriving the state._
