# Pre-registration: the H₂ bond with the ruled electron σ₀σ₁σ₀ and the ruled photon

Written 2026-11-21, before any number in this directory was computed. Issue #8821.

## Why

`prop:ilp-covalent-bond` selects the H₂ bond word with a γγ-power electron `V^k` (k ∈ {0, 3, 6}).
Three owner rulings since then change its inputs (`docs/coordination/owner-rulings.md`):

- **Electron (2026-11-21).** The electron is `E = σ₀σ₁σ₀ ∈ B₃`, whose closure is the Hopf link.
  The trefoil `σ₀³ ∈ B₂` is a backup only, and it is not run here.
- **Photon (2026-11-18, reaffirmed 2026-11-20).** `γ = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹`.
  There are no virtual photons. Exchange is modelled as prior entangled photons or unseen
  intermediary emitters.
- **Two-term Lagrangian trace (2026-11-21).**

## What is fixed (taken from the corpus, not chosen)

- **Nucleon.** `V^m` on its own three strands, with `m ∈ {3, 6}`. These are the two powers that
  pass reading 3 alone (`h2_gg_atom/results.md`).
- **Electron.** `E = σ₀σ₁σ₀` on its own three strands. It is the existing corpus word
  `knot_convoluted_tensor_h2_probe.ELECTRONS["Tw0_s0s1s0"]`.
- **Atom.** Six strands, with no p–e letter and no junction letter (the owner-option-1 cell).
  Atom 1 has order `pe`. Atom 2 has order `pe` or `ep`, and both are run. The H₂ word has 12
  strands, and the junction cut lies between strands 5 and 6.
- **Selector.** Reading 3 under convention D at the proton pin `q₀`, at every level 1…12. The code
  of `h2_one_rule` and `h2_gg_atom` is reused unchanged: mpmath at 40 dps, `TOL = 1e-25`, no float.
- **Selection rule (owner 2026-11-15).**
  - Each constituent passes reading 3 on its own strands.
  - The bare H₂ word passes.
  - The bonded word passes at every level.

## The bond alphabet, from the ruled photon

A photon absorbed at window `s` contributes one term of `γ_s`. The non-identity terms are `σ_s`,
`σ_{s+1}` and `V_s = σ_sσ_{s+1}⁻¹`. The identity term means the photon is not absorbed there.

- The junction windows are `s ∈ {4, 5}`, the two windows that straddle the 5|6 cut.
- The letter set is `A = {σ₄, σ₅, σ₆, V₄, V₅}`. `σ₅` is a term of both windows and is counted once.
- A bond `K` is a product of `j` letters from `A`, for `j = 1, 2, 3`. That gives
  5 + 25 + 125 = 155 words.
- `j` is the number of photons absorbed at the junction.
- The coefficients `φ` are **not** used. Each monomial of the expansion of a product of photons is
  tested on its own, so no value of `φ` is chosen.

**Exchange model.** No virtual photon is used. The `j` absorbed photons existed before binding.
Either they are members of entangled pairs, or they come from an unseen intermediary emitter. The
braid word records only the absorbed terms. Where an unabsorbed partner photon goes is not in the
word. So this probe cannot tell the two models apart. Stage 4 of `gg_twist_reading3` measured the
same limit: the pass/fail of reading 3 did not separate a prior pair from a self-twist. The parity
of `j` is reported (even `j` is compatible with complete pairs absorbed at the junction). It is not
used to select.

**The old family is a subfamily.** `V_s^k` (k = 1, 2, 3) is the γγ-power family of the current
proposition. It is the calibration (E0 below).

## The two-term trace

**Primary insertion: the derived lepton insertion of PR #8743.** It is all pairs plus
`(2/3)·Σ_ℓ Q_ℓ²`, with `Q = T³ + 1/6` on a quark strand and `Q = T³ − 1/2` on a lepton strand. All
three strands of each nucleon are quark strands and all strands of each electron are lepton strands.
This assignment is the corpus "C-lep" convention, and it is an assumption, not a derivation.

- **Prediction (structural, 99 %).** The `T³`-linear terms cancel, so the insertion depends only on
  `T³_tot` and the species counts. It is therefore a scalar on every weight space `W_m` of
  `V^{⊗12}`, whatever the colouring of the positions. So its connected part is 0, and the two-term
  trace equals the one-term trace on every word.
- **Check E2.** The insertion is evaluated exactly (`Fraction`) on all 4096 basis states for both
  layouts, and it must be constant on each `W_m`.
- **Lean.** A generic-field lemma for this cancellation, with `#print axioms`.

**Not run: the H_N-projected pairs-only insertion of #8707.** #8743 shows it is not carried at a
quark–lepton crossing. It is recorded as a comparison that this probe does not compute.

## Calibration checks

- **E0.** The rows `K = V_s^k` (k = 1, 2, 3) with nucleon `V³` reproduce the committed
  `h2-gg-atom.witness.json` Tw0 rows (all level characters) to 1e-18.
- **E1.** `χ_(3)(E) = q³`, the trivial block (`σ ↦ q`).
- **E2.** As stated above.

## Quantities reported for each (m, order of atom 2, K)

- Reading 3 at every level, the failing levels, and the negative characters.
- The one-term trace ratio `tr(xK)/tr(x)`. It is reported and never used to select (ruling B).
- `j`, the parity of `j`, and the crossing count (`σ` counts 1, `V` counts 2).
- The permutation of `K` on strands 4…7. This shows whether `K` is a pure braid on the junction.

Also reported: reading 3 for `E` alone at levels 1…3, with its characters.

## Outcomes, fixed before computing

- **(i) V³ stays unique.** Among the 155 words, exactly `V_4³` and `V_5³` pass whenever the
  constituents and the bare word pass.
- **(ii) V³ is not unique.** Other photon-term words also pass. The passing set is reported in
  full, with its least `j` and its least crossing count. The rule does not then pick one word, and
  that gap is reported as a gap. It is not filled by the trace, by `j`, or by a choice.
- **(iii) Blocked.** The electron fails alone, or the bare word fails.

## Priors (stated before computing)

- **P1 (95 %).** `E` passes reading 3 alone, and the bare word passes. `h2_gg_atom` already saw the
  bare Tw0 words pass with nucleon `V³`.
- **P2 (95 %).** Within the `V_s^k` subfamily only `V³` passes, as in `h2_gg_atom`.
- **P3 (70 %).** Outcome (ii). Some non-V words pass, most likely pure junction twists such as
  `σ₅²`. Stage 1 of `gg_twist_reading3` found "pass if and only if pure".
- **P4 (99 %).** The connected two-term term is 0 on every row.

## Not done here

- The trefoil backup electron.
- The pairs-only H_N comparison of #8707.
- Values of `q` other than `q₀`.
- Bond words with more than three photons.

Nothing is wired into the content block. Any change to `prop:ilp-covalent-bond` waits for the owner.
