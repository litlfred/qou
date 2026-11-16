# Pre-registration: reading 3 with the photon twist channel L± added to the γγ alphabet

Bean qou-a1hh (grammar), bean qou-99qc (asked by the weak-vertex thread). Committed before the probe is written or run.

## Question

The γγ rule (`QOU/Mass/GammaGammaWordSelection.lean`) uses the single vertex V = σ₀σ₁⁻¹ (writhe 0). The corpus photon blocks also carry a twist channel L₊ = σ₀σ₁, L₋ = σ₀⁻¹σ₁⁻¹ (writhe ±2). Does adding L± change which three-strand words pass reading 3, and does a chiral word appear among them? This probe does **not** add L± to the rule; that is an owner ruling.

## Stage 1 (this run): single particle on three strands

- Alphabet A = {V, V⁻¹, L₊, L₋} at site 0 of H₃(q).
- Every word over A of length 1..6 (4 + 16 + … + 4096 = 5460 words).
- Named controls: L₊σ₀ (trefoil closure, cited by the weak-vertex thread), V³, V⁶.
- Readout per word: the reading-3 level characters at levels 1..3 (two-row μ, convention D, proton pin, 40 dps, same functions as `h2_gg_atom`), pass = all > 0; writhe; permutation; whether the closure is a knot (1 component).
- Report: the passing set, grouped by writhe, with every passing word of nonzero writhe listed (those are the chiral candidates), and the minimum length at which one appears.

## Stage 2 (pre-registered now, run only if stage 1 has passing nonzero-writhe words)

H₂ with nucleon V³ and V⁶ and each passing nonzero-writhe electron of minimal length, as in `h2_gg_electron` (bonds none, V, V², V³ at s = 4, 5; levels 1..12).

## What counts as a result

Either outcome is reported: "no word of writhe ≠ 0 passes up to length 6" (scope (a)), or the list of passing chiral words. Nothing is selected or compared with measurement.

## Stage 3 — full photon (owner 2026-11-16: "L is part of photon so it is supposed to be included … use it")

Basis: `gamma-gamma-generates-particles` (γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁; two-photon products span H₃(q), incl. L±
and e⁻ = σ₀σ₁σ₀; `gamma_gamma_chirality_surjective`, `gamma_gamma_reaches_Lminus`). With γ and γ̄ the letters
σ₀^±1, σ₁^±1 are all photon terms, so the full-photon γγ word set on 3 strands is the whole braid group B₃ and the
selection is reading 3 alone. Test: every freely reduced word over {σ₀^±1, σ₁^±1} of length 1..7 at site 0; record
pass/fail (reading 3, every level 1..3, convention D, proton pin, mpmath 40 dps), writhe, components.
Prediction recorded before running: pass ⟺ pure (3 components) on this set, as in stage 1. Nothing fitted.
