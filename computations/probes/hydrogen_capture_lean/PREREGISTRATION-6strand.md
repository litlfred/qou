# Pre-registration: Lean formalisation of the 6-strand bond-chirality table (#8804 §43)

Written 2026-11-22, before any Lean is generated or checked. Committed before the Lean work.

## Source

`computations/probes/mn_own_identity/LITERATURE-COMPARISON.md` §43 and
`mn_hydrogen_capture_chirality_probe.py` on `origin/claude/mn-own-identity-2026-11-21`.
Arm 1 of that probe: six strands, `(C²)^{⊗6}`, Jimbo Ř
(`Ř e00 = q e00`, `Ř e01 = e10`, `Ř e10 = e01 + h e10`, `Ř e11 = q e11`, `h = q − q⁻¹`,
`σ⁻¹ = σ − h`). Words, as lists applied right to left (matrix product in list order), with the
probe's 0-based generator indices:

| label | word | proton strands |
|---|---|---|
| G, proton left | `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂σ₃⁻¹)³` | 0,1,2 |
| G, proton right | `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂σ₃⁻¹)³` | 3,4,5 |
| G′, proton left | `(σ₀σ₁⁻¹)³ · σ₃σ₄σ₃ · (σ₂⁻¹σ₃)³` | 0,1,2 |
| G′, proton right | `σ₀σ₁σ₀ · (σ₃σ₄⁻¹)³ · (σ₂⁻¹σ₃)³` | 3,4,5 |

Functional B1: `F(O) = Σ_s T³(s)·W_ss` over basis states `s` whose three proton strands carry two
zeros (`O₊`) or one zero (`O₋`); `T³ = (#0 − #1)/2` over all six strands. `S = F(O₊) + F(O₋)`.

## Reproduction already done (before this file)

`sympy` over ℚ(q), the probe's own definitions, 64 basis states. All four `S` match §43 exactly:

| config | S | F(O₊) at q = 1 | F(O₋) at q = 1 |
|---|---|---|---|
| G left | `−4q·h⁴` | +6 | −6 |
| G right | `+(3q²+1)h⁴/q` | +6 | −6 |
| G′ left | `+(q²+1)(3q⁴−2q²+1)h⁴/q` | +6 | −6 |
| G′ right | `−(3q²+1)q³h⁴` | +6 | −6 |

So the "±6" of §43 belongs to all four 6-strand rows (`O₊ → +6`, `O₋ → −6`), and the "±3" belongs
to the two 4-strand capture rows (`O₊ → +3`, `O₋ → −3`, both placements), not to any 6-strand row.

## What will be proved (generic `{R} [Field R]`, hypothesis `q ≠ 0` only)

1. **Reduction (full space).** `T³ = #0 − 3`, `Ř` preserves `#0`, so only the weight spaces
   `#0 ∈ {1, 2, 4, 5}` (dimensions 6, 15, 15, 6) enter; `#0 = 3` has `T³ = 0`. For every word,
   `F(O₊) + F(O₋)` on the 64-dimensional space equals an explicit sum of 30 weight-space diagonal
   entries (per placement). Route: `gen64` via `Nat.testBit`, inclusion matrices `E`, a general
   lemma `M · E = E · M.submatrix idx idx` for any `M` that maps the weight space to itself, with
   closure and injectivity of `idx` checked by `decide`.
2. **Values.** The four `S` above, as equalities in `R`, from mulVec chains on the weight spaces.
3. **q = 1.** `F(O₊) = 6` and `F(O₋) = −6` at `q = 1` for all four configurations.

## Predictions

- P1: the Lean values equal the four §43 values exactly (they must, given the reproduction; a
  mismatch would mean a transcription error in the Lean, not new mathematics).
- P2: `F(O₊)(1) = 6`, `F(O₋)(1) = −6` in all four configurations.
- P3: the full-space reduction is provable with the closure route; if it is out of reach in this
  session, that is reported explicitly and only the weight-space values are claimed.

No numerical value enters; nothing is fitted. The words are §43's own (§43 itself records the bond
`(σ₂σ₃⁻¹)³` as a choice, not a corpus rule); formalising them does not adopt them.
