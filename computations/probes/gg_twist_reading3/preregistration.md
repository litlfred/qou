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
