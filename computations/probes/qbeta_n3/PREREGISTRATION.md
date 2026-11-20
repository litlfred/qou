# N3 pre-registration: Q_β / 𝔇_n as a T⁺ matrix element (2026-11-20)

Bean `qou-99qc`. Written BEFORE any number at q₀ is computed. Re-aimed 19:33 by the
owner: the primary output is the matrix element M(q) and the rate 𝔇_n(q) ∝ |M(q)|² ×
phase space, as exact functions of q.

## Construction (all pieces from the corpus)

- Hadron side: `V^{⊗3}`, `T⁺ = Δ²(E) : W₋ → W₊` and `T⁻ = Δ²(F)` exactly as in
  `IsospinRaisingRoundTrip.lean` (#8632). Pairing: the standard form on the weight basis,
  under which `σ₁, σ₂` are symmetric and `T⁻ = (T⁺)ᵀ` (to be PROVED, not assumed).
- Lepton side: one quark strand crosses one lepton strand (lepton doublet `ν = u`-label,
  `e = d`-label). The weak insertion on that crossing is `W − σ = −h·P_L`
  (`weakVertex_sub_letter`), `P_L = P₊ = (σ + q⁻¹)/[2]` at `q > 1`.
- Charge exchange = the amplitude, in the strand-following frame, that the quark strand
  leaves with the other label (`d → u`) and the lepton strand with `ν → e`.

## Pre-registered readings (each reported whatever its value)

| id | quantity | prediction before computing |
|---|---|---|
| A | Hecke-energy difference across `T⁺` | **0 identically** (`T⁺` intertwines `σ₁, σ₂`) |
| B | normalised `|⟨p|T⁺|n⟩|²`, isospin ½ / 3/2 | `1` / `[2]²` |
| C | lepton exchange amplitude of `−h P_L`, quark left / right | `−hq/[2]` / `−hq⁻¹/[2]` |
| D | `|M|² = B × C²` for the four (isospin, placement) cells | products of the above |
| E | `Q_β` from the construction | expected NOT derivable (A = 0); reported as such |

No reading is selected by accuracy. CODATA `Q_β`, `τ_n` appear only in a comparison
column. Choices that remain (placement, isospin, frame, factorisation) are enumerated,
not resolved.
