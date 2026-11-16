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

## Stage 4 — prior entangled γγ pair across proton and electron (owner card 2026-11-16 08:21Z)

Owner reading: no virtual photons. The bound electron's q^{±2} shift comes from one γγ pair, created
before binding, whose two photons land on the proton and electron strands. Backups kept on standby:
(i) put the shift on the bond letter, (ii) unseen emitters at the exceptional divisor (the
conjugation-invariant reading of stage 3).

**Atom (6 strands, order "pe").** Nucleon V^m on strands 0–2 (m ∈ {3, 6}), then the pair word P at
window b (sites b, b+1), then the free electron V³ on strands 3–5. No p–e single-crossing letter.
P ∈ {L₊V⁻¹, V⁻¹L₊, L₋V⁻¹, V⁻¹L₋}; b ∈ {1, 2} (the two windows that straddle the p|e boundary).
Order "ep" mirrors it: electron on 0–2, nucleon on 3–5, P at window b' ∈ {1, 2}.
Control: P empty (the free atom).

**Measured, reported, not selected on.**
1. Atom alone: reading 3 at levels 1..6, and χ₍₆₎(atom) (= q^{writhe P} = q^{±2} by construction).
2. H₂ (two atoms, both orders of atom 2), bonds none, V, V², V³ at s = 4, 5, reading 3 at levels
   1..12 — the stage-2 recipe.
3. Whether the passing set depends on the sign of P (L₊ vs L₋).

**Prediction.** None on the sign. Expect at least one P to give a passing atom; if no atom with a
pair passes, the entangled-pair reading fails as stated (scope a) and the backups come up.
