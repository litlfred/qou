# Pre-registration: deriving the lepton-strand normalisation (issue #8833, front 1)

Written and committed before the Lean file and probe are run. Owner 2026-11-21: *"1 and 3
simultaneously"*. Front 1 asks for the normalisation of the lepton strands to be **derived**,
not chosen to hit the #8868 window.

## Premises (stated, to be checked by the owner)

The ruled D1 nucleon rule ε_X = Tr(K^{⊗3} P_X ρ(X))/[2]³ is extended to a process word W on
n strands whose closure has c components by asking for three properties:

* **(N1) agreement:** on the bare nucleon word (n = 3, c = 3, sector observed) it is D1.
* **(N2) spectator invariance:** adding a split, idle unknot strand does not change the value.
* **(N3) closure invariance:** the value depends on the closed link, not the braid
  representative (Markov stabilisation does not change it; framing is corrected by q^{−2·writhe},
  which is 1 for every γγ word since their writhe is 0).

Only the nucleon sector is observed (proton weight q). Lepton strands are not observed, so
they are summed over all weight sectors.

## Lean first

`QOU/QBeta/LeptonStrandNormalisation.lean`:
* within normalisations [2]^{−(α n + β c)}, (N1) and (N3) force α = 0, β = 1, and then (N2)
  holds;
* a sector-restricted idle strand contributes q^{±1}/[2] ≠ 1 (q ≠ 0, q² ≠ −1 in a field), so
  restricting the lepton sector breaks (N2): the normalisation used in
  `qbeta_gg_process_word` (lepton sector restricted, divide by [2]⁹) is not spectator
  invariant.

## The probe

Exact sympy: the Jimbo partial quantum trace of R over the last strand is q²·1 (the Markov
property used by N3), checked. Then on the same 1560 words as `qbeta_gg_process_word`
(no change to the family):

  x̂(W) = q^{−2·wr(W)} · Tr(K^{⊗9} (P_p ⊗ 1) ρ(W)) / [2]^{c(W)},   c = 7.

Reported for every word: x̂ at q₀, whether it is in the #8868 window (0.33174, 0.40872),
e⁻ν̄ vs mirror; unlinked words factorise as ε_p · (normalised lepton invariant), checked.
Nothing is selected. If (N1)–(N3) are not the premises the owner wants, the result does not
stand.
