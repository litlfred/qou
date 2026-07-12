# RSK Brick Series — coordination ledger

**Goal.** Construct the Robinson–Schensted–Knuth correspondence bottom-up in
Lean, culminating in Identity-I `Σ_{λ⊢n} (f^λ)² = n!` (i.e. `RSKBurnsideHolds n`)
for **general `n`**, replacing the `RSK_substrate_axiom` that `RSKBridge` carries.

All work lives in new `content/quantum-observable-universe/lean/QOU/Mathlib/Schensted*`
files (namespace `QOU.Mathlib.Schensted`), disjoint from the `RSKBurnsideTarget` /
`RSKBridge` layer except for the `QOU.lean` import list.

## Brick status (2026-07-12)

| Brick | Content | PR | Status |
|-------|---------|-----|--------|
| 1–6b | `insertWord`/`insertWordRec`, row/col invariants, Q shape+standardness | — | merged (main) |
| 7 | `P(w)` as Mathlib `SemistandardYoungTableau` (`toSSYT`, `insertWordSSYT`) | #3623 | ✅ merged |
| 8 | `content (insertWordRec w).2 = range n` (Q timestamps `0..n-1`, `Nodup`) | #3647 | ✅ merged |
| 9a | `shiftT` (0→1 relabel) + shift-invariance + `recordingSSYT` | #3655 | ✅ merged |
| 9b | cells↔content bridge (`content_eq_cells_map`) + `insertWordSYT : StandardYoungTableau` | #3680 | ✅ merged |
| 10 | generic `listStandardYT` + `insertWordPSYT` (P(w) standard for permutation words) | #3688 | open |

## Convergence with #3243 (`rsk-substrate-instances`)

[#3243](https://github.com/litlfred/qou/pull/3243) discharges
`RSK_substrate_axiom : RSKBurnsideHolds n` for `n ≤ 12` by `decide` (live axiom
range now `n ≥ 13`), and builds `RSKBijection n` instances with `dim := dimSYT`.
The Brick series is the **constructive all-`n`** route to the same identity: once
`w ↦ (P(w), Q(w))` is packaged as `Sym n → Σ_λ SYT(λ)²` and shown bijective, it
discharges `RSKBurnsideHolds n` for all `n`, superseding both the `decide` range
and the axiom. No file conflict (Brick = `Schensted*`; #3243 = `RSK*`); shared
file is `QOU.lean` only. Intent posted on #3243 (2026-07-12).

## Next

1. Package `w ↦ (P(w), Q(w))` as a map into `Σ_λ (SYT(λ) × SYT(λ))` using the
   shape-equality `insertWordRec_shape_eq_P` (P and Q share a shape).
2. The RSK inverse (bumping-reversal) → bijection `Sym n ≃ Σ_λ SYT(λ)²`.
3. Cardinality: `n! = Σ_λ (f^λ)²` → `RSKBurnsideHolds n` for general `n`.
