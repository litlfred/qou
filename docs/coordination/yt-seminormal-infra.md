# Coordination ledger — YT seminormal-sum Mathlib-gap infra

**Goal.** Build the "not in Mathlib" standard-tableau seminormal-character
apparatus so the corpus's `χ_λ(σ) = c_λ·h` walls (`symbolic_character_table`,
`QHeckeSeminormalCharacterClosure`) can be discharged. Mathlib carries only
`YoungDiagram` + `SemistandardTableau`.

**Lead PR.** [#3777](https://github.com/litlfred/qou/pull/3777)
(`claude/askey-derivation-gap-canonical-xaf8h7`). Beans: milestone `qou-cxkc`
+ Infra tasks `qou-ujfg`/`qou-mcbf`/`qou-vg1u`/`qou-9vvr`/`qou-tqab`.

## Scope map (2026-07-13)

| PR | Relationship | Action |
|----|--------------|--------|
| #3777 (this) | seminormal character (`χ_λ`) Lean infra | — |
| #3719 (cyclotomic/Specht `dim_q`) | **overlap** — shared standard-YT + partition base; complementary invariant (`dim_q` vs `χ_λ`) | intent + capstone update posted; no file overlap yet |
| #3432 (Hoefsmit Stage-B probe) | weak — `Hoefsmit.content` = my `content`; compute probe not the Lean file | reuse note in `TableauContent.lean` (consolidation direction: extract the pair primitive to the light module) |
| #3773 / #3780 / #3779 (Φ_b, binding-frontier) | thematic (mass/binding) only; no seminormal-character file overlap | none |

## Verified results on #3777 (all sorry-free, lean-direct exit 0)

- `SeminormalWeight.lean`: `reducedWeight`, `seminormalWeight`,
  `seminormalWeight_eq_h_mul` (`a_ρ = h·g_ρ`), `reducedWeight_add_neg`
  (`g_ρ + g_{−ρ} = 1`), `characterSum_eq_h_mul` (`χ = h·Σg`),
  `reducedSum_pair` / `characterSum_pair` (base case `c_λ=1`),
  **`two_mul_reducedSum_eq_card`** (`2·Σg = |S|`, integer content),
  **`two_mul_characterSum_eq`** (`2·χ = |S|·h` — general `χ = c_λ·h`).
- `TableauContent.lean`: `content`, `axialDistance`, `axialDistance_antisymm`,
  `reducedWeight_pair`.
- `JonesNuclearQuotient.lean`: `jonesHopfLink_eq_jonesHopf` (rpow bridge).

## Concrete construction (bean `qou-tqab`, PRs #3791/#3794/#3798/#3799)

The algebraic core is done. Remaining to *discharge* `symbolic_character_table`:
the concrete standard-YT type + seminormal-action model per partition supplying
the `τ` (`i↔i+1` swap) and `ρ` (axial distance) the general theorem consumes,
then the wire into the abstract `chiSigma`. This is the shared standard-YT base
with #3719 — coordinate before building it in either branch.

## 2026-07-18 — base-tableau brick complete (#3843)

`QOU/BraidKnot/SytRowSuperstandard.lean` (new, sorry-free) — the OV
base-tableau existence brick, complementary to this ledger's χ_λ thread:

- `rowSuperstandardSsyt` (row-reading SSYT), `card_eq_sum_rowLen`
  (`|μ.cells| = ∑_{i<colLen 0} rowLen i` via `cells = ⨆ rows`), the full
  `BijOn` (MapsTo/InjOn/SurjOn), `rowSuperstandardStd : StandardYoungTableau μ`,
  and `instNonemptyStandardYoungTableau`.
- Also on #3843: `syt_adjacentSwap_connected` proved sorry-free via
  `adjacentSwapStep_symm` (swap-symmetry de-abstraction), reducing the
  `JucysMurphy.lean` OV debt to the one-directional `syt_all_connect_to_some`.
- No file overlap with the `SeminormalCharacterConnector`/`SeminormalWeight`
  χ_λ work; `seminormalVector_base_exists` left for that thread's `g_ρ` machinery.
- Remaining for `syt_all_connect_to_some`: inversion measure + exchange step
  (walk any SYT to `rowSuperstandardStd`).

## 2026-07-18 — two more exchange-argument bricks (#3843, sorry-free)

Two isolated, sorry-free, pushed bricks that de-risk the remaining
`syt_all_connect_to_some` walk:

- `QOU/BraidKnot/SytMathlibBridge.lean` — `Mathlib.SYT → BraidKnot.SYT`
  one-down conversion (`entry i j - 1`; off-diagram `0` stays `0`, the BijOn
  bound `1 ≤ entry ≤ |μ|` makes truncated subtraction faithful). Yields
  `rowSuperstandardBraidKnot` + `Nonempty (QOU.BraidKnot.StandardYoungTableau μ)`
  — the base tableau `T₀` **in the exact type** `syt_all_connect_to_some`
  consumes (the JM machinery uses the bespoke entry-based `BraidKnot.SYT`, not
  the `bijOn`-based `Mathlib.SYT` the base brick built).
- `QOU/BraidKnot/SytAdjacentSwap.lean` — `swapCellsSYT`, the consecutive-label
  cell-swap constructor: given cells `p,q` holding labels `a,a+1` in different
  rows **and** columns, exchanging their entries is again a `BraidKnot.SYT`.
  Clean design via the value-level involution `swapSucc a` (swap the integers
  `a,a+1`): it reverses order only on the pair `(a,a+1)`, and the
  different-row/col hypotheses (via `inj_on`) guarantee no row/col-adjacent
  pair carries those values, so strictness transfers with no cell geometry.

### Decomposition of the residual `syt_all_connect_to_some` (for the next session)

The two combinatorial edge/base objects now exist in the right type. What
remains is best done **inside `JucysMurphy.lean`** (it already has `cellLabel`,
`tableauCellEquiv`, `entry_tableauCellEquiv`, `row_eq_offset_add_count`), which
would then `import QOU.BraidKnot.SytAdjacentSwap`:

1. **Realization** `AdjacentSwapStep μ T (swapCellsSYT T p q …)` for
   `p = tableauCellEquiv T a`, `q = tableauCellEquiv T (a+1)` when their contents
   differ by `≥ 2` (⟺ different row & col, automatic for consecutive labels in a
   genuine SYT — same row ⟺ gap `+1`, same col ⟺ gap `−1`, gap `0` impossible).
   In `T' = swapCellsSYT`, label `a` sits at `q`, label `a+1` at `p`
   (`swapSucc a a = a+1`, `swapSucc a (a+1) = a`); compute `tableauCellEquiv T'`
   via `cellLabel T' q = ⟨a,_⟩` + `tableauCellEquiv_cellLabel`. The gap
   conditions `d≠0`, `d²≠1` are then automatic from the `≥2` separation.
2. **Measure** `inv(π_T)` with `π_T = cellLabel (rowSuperstandardBraidKnot μ) ∘
   tableauCellEquiv T` (a permutation of `Fin n`, `= id` at `T₀`). An admissible
   step right-multiplies `π_T` by the adjacent transposition `(a, a+1)`, changing
   `inv` by `±1`.
3. **Exchange lemma** — if `T ≠ T₀` then some adjacent descent `π_T(a) >
   π_T(a+1)` corresponds to a **valid** (different-row/col) swap, so `inv`
   strictly decreases. The one obstruction to rule out: an adjacent descent whose
   labels are row/col-adjacent (gap `±1`); handle by choosing the descent
   position carefully (Yamanouchi/last-letter order) — the crux, and the only
   genuinely non-mechanical remaining step.
4. **WF induction** on `inv(π_T)` closes `syt_all_connect_to_some` with
   `T₀ = rowSuperstandardBraidKnot μ`.

## 2026-07-18 — post-#3843 tranche (PR #3893): `SytEntryMono.lean`

#3843 merged (base tableau + bridge + swap constructor + swap-symmetry). New
PR #3893 opens the tranche that closes `syt_all_connect_to_some`:

- **`SytEntryMono.lean`** (new, sorry-free) — `content_ne_of_succ`: consecutive
  labels never share a diagonal (`d ≠ 0`). Row trichotomy on `p` vs `q`: same
  row ⇒ same cell (contra); `q` above `p` ⇒ diagonal-mono contradiction
  (`a+1 < a`); `p` above `q` ⇒ reduces to `p` = `q`'s diagonal predecessor, then
  the between-cell `(p₁, p₂+1)` carries an entry strictly between `a` and `a+1`.
  Also lifts `entryLtDiagSucc` / `entryLtOfDiagRowLt` to public lemmas.
- **Strategic insight (recorded above, step 3):** every descent of `inv(π_T)` is
  admissible for *any* `T₀` — same-row/col pairs map to ascents under
  `cellLabel_{T₀}`. This removes the last-letter/Yamanouchi complication.
- Remaining bricks on #3893: `d² ≠ 1` (same-row ⟺ gap +1 / same-col ⟺ gap −1),
  the realization, the `inv` measure, and the WF induction.
- **Lean gotcha logged:** `entryLtOfDiagRowLt` applied with `x := (a,b)` returns
  a pair-projection conclusion `T.entry (a,b).1 (a,b).2` that `omega` treats as
  an atom distinct from `T.entry a b`; ascribe the result to a clean-typed
  `have` (defeq) before feeding `omega`.

## 2026-07-18 — post-#3904 tranche (PR #3910): realization scaffolding

#3893 + #3904 merged (both admissibility halves: `d ≠ 0`, `d² ≠ 1`). PR #3910
adds the `swapCellsSYT` **entry-computation helpers** in `SytAdjacentSwap.lean`
(sorry-free): `swapSucc_self`, `swapSucc_succ`, and
`swapCellsSYT_entry_{mem,at_p,at_q,other}`. These let `JucysMurphy.lean` evaluate
`cellLabel T'` on the swapped tableau `T' = swapCellsSYT T p q …` (label `a`
moves to cell `q`, label `a+1` to cell `p`).

### Realization proof — fully worked, ready to type into `JucysMurphy.lean`

Add `import QOU.BraidKnot.SytAdjacentSwap` + `import QOU.BraidKnot.SytEntryMono`.
Then, with `p := tableauCellEquiv μ T a`, `q := tableauCellEquiv μ T b`,
`T' := swapCellsSYT T ↑p ↑q (tableauCellEquiv_mem T a) (tableauCellEquiv_mem T b)
(by rw [entry_tableauCellEquiv, entry_tableauCellEquiv]; omega) hrow hcol`:

```
theorem adjacentSwapStep_swapCells (T) (a b : Fin (nOf μ)) (hab : ↑a+1 = ↑b)
    (hrow : (↑p).1 ≠ (↑q).1) (hcol : (↑p).2 ≠ (↑q).2) :
    AdjacentSwapStep μ T T' := by
  refine ⟨a, b, hab, ?_, ?_, ?_, ?_, ?_⟩
```
The five goals reduce to three cell-identities (each: `cellLabel T' c = ℓ` via
`Fin.ext` + a `swapCellsSYT_entry_*` rewrite + `entry_tableauCellEquiv`, then
`tableauCellEquiv_cellLabel` to invert):

- `tableauCellEquiv μ T' a = tableauCellEquiv μ T b` — via
  `cellLabel T' q = a` (`swapCellsSYT_entry_at_q` → `T.entry p = a`).
- `tableauCellEquiv μ T' b = tableauCellEquiv μ T a` — via
  `cellLabel T' p = b` (`swapCellsSYT_entry_at_p` → `T.entry q = b`).
- `∀ s ≠ a, ≠ b, tableauCellEquiv μ T' s = tableauCellEquiv μ T s` — via
  `swapCellsSYT_entry_other` (the `≠ ↑p/↑q` side-goals from
  `(tableauCellEquiv μ T).injective`).

The two content gap conditions (`d ≠ 0`, `d² ≠ 1`) come from `content_ne_of_succ`
and `sq_content_gap_ne_one` applied at `↑p, ↑q` (rewrite cellContent → the
explicit `(·.2 − ·.1)` form). **Coercion caution:** `swapCellsSYT_entry_other`
and the `cellLabel` unfolds cross `μ.cells ↔ ℕ×ℕ`; wrap membership/`≠` args with
`Prod.mk.eta` to convert `↑cell` ↔ `((↑cell).1, (↑cell).2)`.

### Then: measure + WF induction (to close the 887 sorry — needs a small reorg)

The private `tableauCellEquiv`/`cellLabel` lemmas (JucysMurphy L1120–1144) sit
*after* `syt_all_connect_to_some` (L887); closing the sorry in place needs them
earlier. Move L1120–1144 (they depend only on `tableauCellEquiv` + imports, not
on the entry-mono lemmas) to before L826, then: define
`π_T := (cellLabel rowSuperstandardBraidKnot) ∘ tableauCellEquiv T` (an `Equiv`,
`= id` at `T₀`); a step right-multiplies `π_T` by `Equiv.swap a b`; `inv` drops
by 1 on a descent; **every descent is admissible** (same-row/col ⇒ ascent under
`cellLabel_{T₀}`; consecutive labels never share a diagonal), so WF-recurse on
`inv(π_T)` to `T₀ = rowSuperstandardBraidKnot μ`.

## 2026-07-18 — measure kernel merged-track (PR #3922): `PermInversion.lean`

**All hard lemmas for closing `syt_all_connect_to_some` are now proven.** The
realization `adjacentSwapStep_swapCells` is merged; the WF measure kernel
[`QOU/Mathlib/PermInversion.lean`](../../content/quantum-observable-universe/lean/QOU/Mathlib/PermInversion.lean)
(PR #3922, sorry-free) supplies:

- `invCount` + `invCount_mul_swap_lt` (adjacent-descent swap strictly lowers the
  inversion count — the only reversed pair is `(a, a+1)`);
- `eq_one_of_invCount_eq_zero` (WF base: 0 inversions ⇒ identity);
- `exists_adjacent_descent_of_ne_one` (WF step: non-identity ⇒ adjacent descent);
- `eq_one_of_strictMono`, `strictMono_of_adjacent` (general `n`).

### Final assembly — the ONLY remaining step (all inputs proven)

In `JucysMurphy.lean` (imports `PermInversion` + `SytMathlibBridge`), after the
L1120–1144 reorg:

1. `permOf T := (tableauCellEquiv μ T).trans (Equiv.ofBijective (cellLabel T₀)
   (cellLabel_bijective T₀))` with `T₀ := rowSuperstandardBraidKnot μ`; then
   `permOf T₀ = 1` (tableauCellEquiv T₀ = (cellLabel T₀).symm).
2. `tableauCellEquiv_swapCells_*` (export the realization's internal cell
   identities: label `a` in `T'` at cell `q`, `b` at `p`, else fixed) ⇒
   `permOf (swapCellsSYT …) = permOf T * Equiv.swap a b`.
3. descent of `permOf T` ⇒ diff row & col (same-row/col ⇒ ascent via `T₀`
   `row_strict`/`col_strict`, using `entryLtRow`/`entryLtCol` on `T₀`) ⇒
   realization gives the admissible edge; `invCount_mul_swap_lt` ⇒ measure drops.
4. WF-recurse on `invCount (permOf T)` (`Nat.strong_induction_on`):
   `invCount = 0` ⇒ `permOf T = 1` ⇒ `T = T₀` (tableauCellEquiv injectivity) ⇒
   `refl`; else take the descent, step, recurse. Closes the L887 sorry with
   `T₀ = rowSuperstandardBraidKnot μ`.

## 2026-07-18 — #3799 σ₁ seminormal character capstone (sorry-free)

`SeminormalCharacterConnector.lean` (branch `askey-derivation-gap-canonical`):
`cellOf`/`generatorRho`, the full `StandardYoungTableau μᵀ` `transpose`
(`swap_bijOn_cells` + `transpose_cells_card` + `T.bijOn.comp`), the
self-conjugate involution on `SYT(μ)`, `card_rowClass_eq_colClass`
(`|R_row|=|R_col|`), and the **capstone** `sigmaOneCharacter_eq_card_mul`:
`χ_λ(σ₁) = |R_row|·h` for self-conjugate `μ` (`c_λ = |R_row| ∈ ℤ`), via
`SeminormalWeight.fullCharacter_two_mul` at `S_off = ∅`. All lean-direct exit 0.
Remaining toward `symbolic_character_table` (bean `qou-tqab`): the per-shape
`|R_row|` counts (`c_λ ∈ {1,3,8,10}`) and the general-`σ_i` off-diagonal case.

## 2026-07-18 — #3978 per-shape count closed: `c_λ = #SYT(μ)/2` (sorry-free)

`SeminormalCharacterConnector.lean` (branch `seminormal-clambda-syt-count`,
follow-on to merged #3799). Closes the `|R_row|` opaque count *in closed form*
with **no enumeration** of tableaux. For `σ₁` the pair `1,2` sits in the corner:
`cellOf_one` (`1` at `(0,0)`, via `entry_le` + `entry_zero_zero_eq_one`) and
`cellOf_two_coord_zero` (`2` at `(0,1)` or `(1,0)`) give the dichotomy
`sameRow12_or_sameCol12` + `not_sameRow12_and_sameCol12`, hence
`rowClass_union_colClass` (disjoint) ⇒ `|R_row| + |R_col| = #SYT(μ)`. With the
merged `card_rowClass_eq_colClass` (`|R_row| = |R_col|`):

- `two_mul_card_rowClass_eq_card`: `2·|R_row| = #SYT(μ)` (i.e. `c_λ = #SYT(μ)/2`);
- `two_mul_sigmaOneCharacter_eq_card`: `2·χ_λ(σ₁) = #SYT(μ)·h`.

11 new theorems, sorry-free, lean-direct exit 0. Remaining toward the *tabulated*
`c_λ ∈ {1,3,8,10}` (bean `qou-tqab`): a closed form / recursion for `#SYT(μ)` on
self-conjugate shapes (Mathlib has no HLF at the pinned toolchain), and the
general-`σ_i` off-diagonal case.

### #3978 (cont.) — general-`σ_i` full character `2·χ = (2|R_row^i|+|S_off^i|)·h`

The general single generator `σ_i` closed on the same PR (three commits):

1. **Diagonal count for every `σ_i`** — `sameRowGen`/`sameColGen`/`rowClassGen`/
   `colClassGen` + `card_rowClassGen_eq_colClassGen` (`|R_row^i| = |R_col^i|` via
   `selfTranspose`, which is already general in the entry `k`).
2. **Off-diagonal swap involution core** — `swapSucc` (value transposition
   `i↔i+1`) + `swapSuccSsyt`/`swapSuccSYT` (a valid `StandardYoungTableau` exactly
   when `i,i+1` are off-diagonal; the classical elementary-transposition fact,
   with the semistandard-preservation proof as the crux), `cellOf_swapSuccSYT_{i,i1}`
   (cell exchange), `generatorRho_swapSuccSYT` (`ρ` negation).
3. **Full character** — `offClassGen` (S_off^i), the total involution `tauGen`
   (swap on S_off, identity elsewhere) with maps-off / involution / ρ-negation, and
   `fullCharacterGen_two_mul`: `2·χ_λ(σ_i) = (2|R_row^i| + |S_off^i|)·h` — the
   complete abstract `symbolic_character_table` form for a single generator, over
   any `[Field R]`, `hnd` (`q^{2ρ}≠1`) passed through. All sorry-free, lean-direct
   exit 0. Remaining (bean `qou-tqab`): the per-shape `#SYT(μ)` / `|R_row^i|` counts
   (→ tabulated `c_λ ∈ {1,3,8,10}`), and multi-generator products.

## 2026-07-19 — tabulated `c_λ = {3,8,10}` closed (PR #4044)

`SytSmallShapeCountsLarger.lean` (new, sorry-free) pins the three remaining
self-conjugate shapes, completing the manuscript table `c_λ ∈ {1,3,8,10}`. The
enumeration count `numSYTenum_eq_numStandardYoungTableaux` (all `n`) is now on
main, so the **forward** route needs no explicit tableau construction:

- `#SYT(μ)` via `numSYTenum` (kernel `decide`) → `numStandardYoungTableaux`
  (`Nat.card` bridge) → `Fintype.card (StandardYoungTableau μ)`
  (`Nat.card_eq_fintype_card`) → `c_λ = |R_row| = #SYT/2`
  (`two_mul_card_rowClass_eq_card`, self-conjugacy).
- `[3,1,1]` #SYT=6 → `c=3` (`card_rowClass_mu311`); `[3,2,1]` #SYT=16 → `c=8`
  (`card_rowClass_mu321`); `[4,1,1,1]` #SYT=20 → `c=10` (`card_rowClass_mu4111`).
- Self-conjugacy `μᵀ=μ` via `YoungDiagram.ext` + `decide`; n=6/n=7 counts are
  axiom-free kernel `decide`.

Remaining on the χ_λ thread (bean `qou-tqab`): the **opaque `chiSigma`** in
`symbolic_character_table.lean:83` (unprovable as stated — a design decision to
restate that block, owner call), and **multi-generator products** `χ_λ(σ_iσ_j…)`.
Separately, the OV thread now bottoms out on the single `sorry`
`seminormalVector_base_exists` (`JucysMurphy.lean:850`, Vershik–Kerov base vector).

## 2026-07-19 — `symbolic_character_table` sorry discharged (PR #4044)

`symbolic_character_table.lean` **restated concretely and proved** (`sorry`
removed). The opaque `chiSigma` class field is gone; `chiSigma` is now a
`def` = `sigmaOneCharacter (shapeOf λ) q h` (the σ₁ seminormal character), and

  `symbolic_character_table (q h) (hq : q ≠ 0) (lam) : chiSigma q h lam = c_λ·h`

is proved via `sigmaOneCharacter_eq_card_mul` + `card_rowClass_shapeOf`
(`|R_row(shapeOf λ)| = c_λ ∈ {1,3,8,10}`). Theorem name preserved for the
`.ts` `lean.ref`; the `[3,1,1]` pair/triple polynomial identities retained.
Nothing imported the opaque class, so the restatement is non-breaking.

**χ_λ single-generator thread is now complete and sorry-free.** Remaining
open items on the wider program (not this thread):

- **OV base vector** — `seminormalVector_base_exists` / `seminormalVector_data_exists`
  (`JucysMurphy.lean`, beans `sp08` / `qou-kskn`): the famous Okounkov–Vershik /
  Gelfand–Zetlin eigenvector-existence theorem. **Now the ONLY live sorry in its
  cone** (Specht foundation — `Mtab`, `polytabloid`, `SpechtSubmodule`, standard
  basis, 2×2 seminormal block, subrepresentation, swap-transport, all-`T`
  connectivity — is all sorry-free; PR #4048). **Formalize-first check (2026-07-19,
  [audit](../audits/2026-07-19-ov-base-vector-column-superstandard-verification.md)):**
  the **column-superstandard** polytabloid `e_{T₀}` IS the base JM eigenvector
  (`X_s·e = content(cell_s)·e`, verified `[2,1]/[2,2]/[3,1]/[3,1,1]`); the
  **row-superstandard** one is NOT (would be proving a false statement — the repo's
  ready `rowSuperstandardStd` is the wrong target). Reduces `base_exists` to the
  single eigen-equation on the column-superstandard polytabloid.
- **Multi-generator characters** `χ_λ(σ_iσ_j…)` — natural extension of
  `fullCharacterGen_two_mul`; open.
- `QHeckeSeminormalCharacterClosure` — conditional class (`claim_paths_agree`
  assumed); discharge or leave conditional.
---

## 2026-08-15 — general-λ Hoefsmit: two of three Hecke relations proved globally (#5076)

**Scope map.**

| PR | branch | relationship |
|---|---|---|
| **#5076** (this) | `claude/seminormal-quadratic-2026-08-15` | general-λ seminormal rep on `SYT μ` — `SeminormalRep.lean` (new), `TableauCells.lean`, `SeminormalParam.lean`, `HoefsmitRep.lean` |
| #4954 | `claude/8vt2-generator-gap-and-identity-2026-08-10` | **overlap + downstream.** Adds `QOU/SchurWeyl/QJucysMurphy.lean`, which imports `HoefsmitRep.lean`; its `qJM_commute` sorry is explicitly blocked on the SW-4 seminormal residual = `qou-gjg6` = this work. [Intent posted](https://github.com/litlfred/qou/pull/4954#issuecomment-5300631637). |
| #5013 | `claude/wlambda-normalisation-census-2026-08-11` | **no overlap.** `w_λ` normalisation in `.md` prose + a Python census; touches no `QOU/SchurWeyl/**`. Not posted on. |

Every other open PR at the time of writing is in a different subtree
(q-NS, c₃/qbeta, precision drains, viewer, LP duals).

**State of `qou-gjg6`.** Route (c) — index the generator matrix by
`StandardYoungTableau μ` on *both* sides, so there is no per-orbit basis
correspondence to justify. Sorry-free and axiom-clean throughout:

- `genMat_quadratic` — `ρ(σ_k)² = (q − q⁻¹)ρ(σ_k) + 1`, arbitrary shape;
- `genMat_far_comm` — `ρ(σ_k)ρ(σ_l) = ρ(σ_l)ρ(σ_k)` for `|k − l| ≥ 2`, arbitrary
  shape, and **with no hypothesis on `q` at all**.

Both work because they are **column-local**: `genMat`'s column `T` has support in
`{T, s_k·T}`, so neither relation ever sees a third tableau. The braid is not
column-local — `σ_k` and `σ_{k+1}` have different supports — which is the precise
sense in which it is harder, and is exactly what `Orbit3Braid` / `Orbit6Braid`
encode.

**Braid: reduced to orbit algebra, not yet proved.** The parameter bookkeeping is
closed (only `p`, `r`, `p+r` and their negatives occur across an orbit —
`axialDist_succ_swapTableau`, `axialDist_swapTableau_word_left`/`_right`,
`axialDist_swapTableau`), the relation is available on `seminormalParam` directly
(`seminormalParam_rel`), the triple products expand onto named orbit tableaux
(`genMat_braid_lhs_expand` / `_rhs_expand`), and the diagonal row closes on that
relation with nothing left over (`braid_diag_identity`). What remains is the other
five rows plus the admissibility case tree for non-generic orbits.
`hoefsmit_seminormal_rep` keeps its `-- Ref:` sorry.

**Convention note for whoever wires `QJucysMurphy` to this.** The JM eigenvalue
`q^{2c}` is a per-cell **content**; `genMat`'s diagonal `seminormalParam q
(axialDist T k)` is a content **difference**. Not a convention clash — the axial
distance controls the *ratio* of consecutive JM eigenvalues, and that ratio is the
bridge. State it explicitly when the two meet.
