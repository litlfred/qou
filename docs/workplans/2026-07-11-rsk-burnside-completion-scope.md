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

## Remaining bricks (each a dedicated multi-hour PR)

5. **Column-strictness / shape validity** — the *bumping lemma*: a bumped
   entry lands **strictly below** where it was, so columns of `P(w)` strictly
   increase and the row lengths form a Young-diagram shape. This is the
   hardest structural brick (the crux of RSK correctness). Deliverables:
   `ColsStrict`/`IsTableau` predicate, `insert_colsStrict`, shape-is-partition.
6. **Recording tableau `Q`** — track the *insertion step number* per new cell;
   prove `Q(w)` has the same shape as `P(w)` and is standard (entries `1…n`
   increasing along rows and columns).
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
- **Brick 5 is the bottleneck.** The bumping lemma is where most RSK
  formalisations spend their effort; budget it as its own multi-session sub-goal.

## Recommended next action

**Brick 5 (column-strictness).** Build on the proven `rowInsert`/`insert` +
`insert_content`. Start with the single-row bumping monotonicity
(`rowInsert` on a sorted row bumps an entry `≥` the inserted `x`, and the
bumped entry re-inserts into the next row at a strictly-earlier-or-equal
column), then lift to the cascade. This is a dedicated coding session, not a
tail-of-session task.

_Reconnaissance + scope authored 2026-07-11. Bricks 1–4 pre-existing and
sorry-free; this doc maps the remaining chain so any session can resume at
Brick 5 without re-deriving the state._
