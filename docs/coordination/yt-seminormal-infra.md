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
