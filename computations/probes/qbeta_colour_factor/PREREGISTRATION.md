# Pre-registration: a colour factor on the ruled Q_β cell (issue #8833, front 3)

Written and committed before any number in this directory is computed.

## The cell this acts on (ruled, not chosen here)

D1 quantum trace, convention D, proton q₀ pin (`q_parameter.Q_50_DIGIT_STR`):
ε_p(X) = q·tr_{W_p}(X)/[2]³, ε_n(X) = q⁻¹·tr_{W_n}(X)/[2]³, X = β_Bor = V³, V = σ₀σ₁⁻¹
(owner rulings 2026-11-20; `QOU/QBeta/FlavourWeightSplit.lean`). Here W_p, W_n are the
one-down and two-down weight spaces of (C²)^{⊗3}, i.e. the strands carry **isospin only**.
The scored value misses by F_required ≈ 2.404 (0.78233341 / 0.325433929).

## The mechanism (one, derivation-based)

Give each quark strand colour as well as isospin: the strand object is V ⊠ C³, a
fundamental of U_q(sl₂) ⊠ U_q(sl₃) (Deligne product of the two ribbon categories). In a
Deligne product the braiding of (V⊠W) with itself is c_{V,V} ⊠ c_{W,W}, so the braid acts by
ρ(X) = ρ₂(X) ⊗ ρ₃(X), with ρ₂, ρ₃ the Jimbo R-matrix actions on (C²)^{⊗3} and (C³)^{⊗3}.
The quantum trace uses K = K₂ ⊗ K₃, K₂ = diag(q, q⁻¹), K₃ = diag(q², 1, q⁻²). The flavour
projections act on the isospin factor only (they are the ruled T³ sectors). So

  ε_p^col(X) = Tr((K^{⊗3})(P_{W_p} ⊗ P_c) ρ(X)) / N_norm

and, because the trace of a Kronecker product is the product of traces, this is
**ε_p(X) · F_c(X)** with the same F_c(X) for the neutron: the colour factor is flavour-blind
and multiplies ε_flavour = ε_n − ε_p by F_c(X).

## The closed family (every member reported)

Colour sector and normalisation (three members, fixed now):
* **C1** full colour trace, normalised by the colour quantum dimension [3]³:
  F = Tr(K₃^{⊗3} ρ₃(X))/[3]³ (the Markov trace at level 3, z₃ = q⁵/(q⁴+q²+1)).
* **C2** colour-singlet projection (the q-antisymmetric line Λ³_q C³, the baryon colour
  state), normalised by [3]³: F = Tr(K₃^{⊗3} P_{Λ³} ρ₃(X))/[3]³.
* **C3** colour-singlet projection normalised by the singlet's own quantum dimension (1):
  F = Tr(K₃^{⊗3} P_{Λ³} ρ₃(X)).

Framing (two members): gl₃ (Jimbo R as is) and sl₃ (R scaled by c = q^{-1/3}, forced by the
singlet, `QOU.Braiding.SlNFramingColourFactor`).

Words: X = V³ is the ruled element and the one the verdict is about. V⁶ and V⁹ (the reported
survivors of the flavour-split audit) are reported alongside, not used.

## Predictions (stated before computing)

* **P1 (structural).** V has exponent sum 0, so the sl₃ framing factor c^{e(X)} is 1: gl₃ and
  sl₃ give identical F on every V^k.
* **P2 (structural, exact).** For any rank N, with a = q^N and h = q − q⁻¹:
  C1 on V³ = 1 − h⁴·[N−1][N+1]/[N]² = 1 − h⁴ + h⁴/[N]². This uses χ_(3)(V³) = χ_(1³)(V³) = 1,
  χ_(2,1)(V³) = 2 − h⁴[3], and Σ_λ f_λ dim_q S_λ(C^N) = [N]³. For real q > 1 and N ≥ 2 this
  lies strictly in (1 − h⁴, 1). To be proved in Lean (`QOU/QBeta/ColourFactorDeligne.lean`).
* **P3.** C2 = 1/[3]³ on every V^k; C3 = 1 on every V^k (V acts on Λ³_q by
  (−q⁻¹)(−q) = 1, and the singlet has K-weight 1).
* **P4 (consequence).** Every member gives F ≤ 1. The family cannot supply F ≈ 2.404; under
  any member the scored cell gets smaller or stays the same.

## Reported, for every member

F at q₀ (60 dps), F·ε_p, F·ε_n, F·ε_flavour, and the ratio F / F_required. A brute-force check
on the 216-dim space (C² ⊗ C³)^{⊗3} that the product trace equals ε·F (factorisation is
checked, not assumed). Exact checks at rational q = 2, 3 for P2 and P3.

## What this does NOT do

Nothing is selected by closeness to F_required, no member is promoted, nothing is mapped to MeV
(Q_β is not assumed linear in ε: owner working conjecture 2026-11-21). The γγ / reading-3
selection of the word is not redone; the lepton-strand normalisation (front 1) is not touched.
`bring_color_weighted` is a p–n *interface* factor between nucleons and has no slot inside a
single nucleon's word; it is not part of this family.

## Prior colour work this does not repeat

* `QuantumTraceFamilyCoth.lean` / `qbeta-epsilon-is-ruled-not-derived` §13: replacing the
  strand rep SU_q(2) by SU_q(N) (a rank *swap*, on Δ_S, before the flavour split). Here
  isospin stays SU_q(2) and colour is an additional tensor factor.
* `sl_n_framing_colour_factor_probe`, `level_three_colour_channel_probe`: colour exchange
  ratios and the forced q^{-1/N} framing; used here as the sl₃ framing member.
* `gg_gluon_segment`: gluon segments V^k on three strands (isospin only).
* `nucleon_photon_colour_weights`: photon colour weights φ; a different meaning of "colour".
