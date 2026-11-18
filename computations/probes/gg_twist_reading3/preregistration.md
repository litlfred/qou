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

## Stage 5 — coarse-grained carbon ring (owner card 2026-11-16 "Both"; pre-registered, not yet run)

**Assumption, stated up front.** One carbon atom = one strand. QOU's carbon atom is not one strand
(it is a 3A-strand nucleus plus electrons), so this is a coarse-graining and any result is a
statement about the coarse-grained word only.

**Words (6 strands).** Bonds are Birman–Ko–Lee band generators a_{i,i+1}, i ∈ Z/6, with
a_{6,1} = ρ σ₅ ρ⁻¹, ρ = σ₁σ₂⋯σ₅, so the closing bond is a genuine crossing of strands 6 and 1 and
no bond is privileged by the strand order. Bond exponent e ∈ {±1, ±2}.
- Ring, symmetric: all six exponents equal.
- Ring, alternating (Kekulé): exponents (2,1,2,1,2,1) and its cyclic shift.
- Chain controls: the same with the closing bond removed (5 bonds).
- Sign controls: all exponents negated.

**Measured, reported, not selected on.** Reading 3 at levels 1..6 (convention D, proton pin,
mpmath 40 dps); components of the closure; writhe; χ₍₆₎ = q^{writhe}; the connected part φ(T) of
`log(δ·V)` on every 3-strand sublink of the ring vs the chain (exact, as in the Borromean probe).

**Questions, with no predicted answer.**
1. Does closing the chain into a ring change the reading-3 pass/fail of the same exponent pattern?
2. Does the symmetric ring differ from the alternating ring?
3. Is any three-party connected part nonzero on a ring whose pair parts are zero?

**What does not count.** Choosing e or the pattern because it passes. Any energy or CODATA/AME
comparison is out of scope for this stage.

## Stage 6 — n-strand chains, rings and Brunnian loops (owner card 2026-11-16, option 2; pre-registered before the probe was written)

**Assumption.** One strand per site, as in stage 5. Exact Jones polynomial via the Temperley–Lieb
bracket; `F(T) = log(δ·V_T) − |T| log δ`; connected part `φ(T)` by Möbius inversion over subsets.

**Words.**
- Chain on n strands: bonds σ_i^e, i = 0..n−2, e ∈ {+2, −2}.
- Ring on n strands: the chain plus the closing band ρ σ_{n−2}^e ρ⁻¹, ρ = σ₀⋯σ_{n−2}, in front.
- Brunnian loop on n strands: the iterated commutator c₂ = A₀₁, c_k = [c_{k−1}, A_{0,k−1}],
  A_{0,j} = σ_{j−1}⋯σ₁ σ₀² σ₁⁻¹⋯σ_{j−1}⁻¹. Deleting any one strand trivialises it by construction.
- n = 3..8 for chains and rings; n = 3..6 for Brunnian (word length grows as ~2^n).

**Reported, not selected on.** Exact `φ(full set)` for each word (zero or not, the ratio, its
leading order in log t); for chains, every connected part of size ≥ 3; for Brunnian words, that
every proper sublink is an unlink and so `φ(full) = F(full)`.

**Questions, no predicted answer for 2 and 3.**
1. Chains: is every connected part of size ≥ 3 exactly 0 for every n? (Lean
   `connected_eq_zero_of_bonds` says yes if F is bond-additive; the probe tests the hypothesis.)
2. Rings: is `φ(full)` nonzero for every n, and at what order in log t does it first appear?
3. Brunnian: is the closure a nontrivial link, i.e. `φ(full) ≠ 0`, for every n?

**What does not count.** Choosing n, e or a word because its φ is nonzero. No energy or
measurement comparison.

## Stage 1b — re-run with L₋ = σ₁σ₀ and the four-term photon (pre-registered 2026-11-17, also in bean qou-99qc)

Pre-registered before any computation. Re-run of gluon-thread stage 1 over the alphabet that prop:gamma-gamma-generates-particles gives (owner query 2026-11-17 06:27Z).
- Alphabet (a): {V, V⁻¹, L₊, L₋} with V = σ₀σ₁⁻¹, L₊ = σ₀σ₁, L₋ = σ₁σ₀ (NOT the inverse σ₀⁻¹σ₁⁻¹ used before). All words of length 1..6 on three strands.
- Alphabet (b): (a) plus e⁻ = σ₀σ₁σ₀, reachable from γγ once φ₀₁ ≠ 0. All words of length 1..5.
- Measured: reading 3 (Frobenius positivity, every level, convention D, proton pin, mpmath 40 dps), components, writhe; for each alphabet the pass count, whether pass ⟺ pure braid still holds, the writhe distribution of passers, the shortest passing word of each writhe.
- Old stage-1 table kept as the record for the inverse reading; this run is reported beside it, not in place of it.
- Questions, no predicted answer: 1. Does pass ⟺ pure survive? 2. Are passing writhes still symmetric, or one-signed (all letters except V⁻¹ are positive)? 3. Does adding e⁻ let any knot (1 component) pass?
- Not allowed: choosing a canonical word, letter or length from these results. This run measures admissibility only; selection is a separate, separately pre-registered step.

## Stage 7 — canonical-word reselection from γ(φ)γ(ψ)

Pre-registered in bean `qou-99qc` (entry *PRE-REGISTRATION 2026-11-18 04:30Z*) before `gg_photon_product_selection_probe.py` was written.

- **Letters.** The terms of the product of two four-term photons (`def:photon`), taken as braid words. No inverse letter occurs.
  - Rule A (primary): the bilinear pair terms. These are eight distinct braids, since σ₁σ₀σ₁ = σ₀σ₁σ₀.
  - Rule B (labelled comparison): Rule A plus the one-photon terms σ₀ and σ₁.
- **Selection.** FrobeniusSelected: reading 3 (χ ≥ 0 on every level), convention D, proton pin. Cost is the crossing count, up to 12. Every feasible word of minimal cost is reported.
- **Deviation from the pre-registration.** The pre-registration said near-zero values would be re-evaluated at 120 dps. The engine cannot do that, because q₀ enters as a stored string. Near-zero values are therefore decided exactly, with q symbolic (`exact_h3_level_chars.py`). This is a stronger test than the one pre-registered. The exact route agrees with the engine to max |diff| 5.7e-39, and the probe checks this.
