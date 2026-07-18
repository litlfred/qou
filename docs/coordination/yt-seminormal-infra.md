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

## Open / next (bean `qou-9vvr`, `qou-tqab`)

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
