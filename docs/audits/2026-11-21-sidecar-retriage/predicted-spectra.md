# Sidecar re-triage: predicted-spectra (2026-11-21)

Part of the stale-sidecar review (umbrella issue #8766). Criteria:
`proof-narrative-lean-equiv` (statement vs Lean) and `da-non-sequitur`
(proof vs statement). After this pass, every block in the chapter is fresh
on both criteria (37 statement blocks and 33 proof blocks).

## Re-stamps (28)

The diff was wording only, with no change to the mathematics or the Lean.
The earlier verdict is kept, and each entry cites the diff.

## Full reviews (6)

| block | criterion | verdict |
|---|---|---|
| torus-knot-shell-binding | stmt vs Lean | fail major: the Lean is rfl/decide over a hard-coded table; uses the withdrawn T(2,n_s) shell rule |
| torus-knot-shell-binding-proof | proof | fail major: the Hecke-gap step is built on the withdrawn T(2,n_s) rule |
| shell-structure-eigenvalues | stmt vs Lean | fail major: line 60 calls the trefoil "the electron" |
| knot-operator-selection-proof | proof | fail major: line 31 still says "T_{2,3} (trefoil, e⁻)" |
| gamma-gamma-generates-particles | stmt vs Lean | fail → warn major: now uses the ruled photon and has real `_NF` theorems; the ref still points at the def-based theorem; "span is all of H₃(q)" is not encoded |
| optimal-normal-form-valley | stmt vs Lean | fail major: the Lean is standard-basis combinatorics; the nucleus normal form and c_i = V̂_i are not encoded |

## Ruling check (docs/coordination/owner-rulings.md)

Each of these was recorded as a finding. No content was edited.

- **Electron = σ₀σ₁σ₀ ∈ B₃ with Hopf closure (the trefoil is the backup).** About 35 `.md` files in this chapter still mention the trefoil. Named conflicts: `knot-operator-selection-multichannel` ("trefoil (electron)"), `shell-structure-eigenvalues` line 60, and `knot-operator-selection-proof` line 31.
- **Nuclear Regime-I shell-size rule T(2,n_s) withdrawn (2026-11-21).** `torus-knot-shell-binding` and its proof rest on this rule, so they need an owner decision: retire the block or rescope it.
- **Photon form.** `gamma-gamma-generates-particles` is on the correct σ₀σ₁⁻¹ form.
