# Lepton pair on 5 strands (charged vacuum, option 1): linked words vs the window (2026-11-21)

Written and committed before the probe in this directory is run. Owner: "keep pushing on lepton",
then "Go" on computing option 1 of the 2026-11-21 lepton-pair card (charged 5-strand vacuum;
the owner chose option 3 for the ruling, and earlier asked to explore the options).

## Inputs (rulings, none chosen here)

* Photon vertex V_i = σ_i σ_{i+1}⁻¹; proton word β_Bor = V₀³ on strands 0–2.
* Electron σ₀σ₁σ₀ with Hopf closure, ν̄ the unknot: target Hopf ⊔ unknot on 5 strands, no extra
  loop. 5 + 3 is even, so γγ words can close to it (`gammaGamma_components_parity`).
* Lepton words: every 5-strand γγ word of ≤ 6 vertices that the #8836 enumeration matched to
  Hopf ⊔ unknot or its mirror (exact invariant at q = 2, 3): 43 e⁻ν̄ + 43 mirror, copied to
  `lepton_words_5strand.json`.
* Lepton normalisation forced by #8836: lepton strands summed over all sectors, factor
  [2]^(−components), framing q^(−2·writhe) (writhe is 0 for γγ words).

Consequence fixed before the run: under the forced normalisation the vacuum's charge does not
enter (no lepton sector is selected), so the 5-strand option differs from option 3 only through
linking. For unlinked words x̂ = ε_p·f_E exactly, the same as on 6 strands (Markov and idle-strand
invariance); this is checked, not assumed.

## The value computed

W = X · β_Bor · L on 8 strands (nucleon 0–2, lepton 3–7), X every product of 0 to 6 junction
vertices from {V₁, V₂} whose strand permutation is the identity (13 words).
x̂(W) = Tr(K⁸ (P_p ⊗ 1) ρ(W)) / [2]⁶, P_p the nucleon sector with one d (weight q).
Exact Laurent polynomials in q; Jimbo R, eigenvalues q, −1/q.

## Test

For every distinct x̂: e⁻ν̄ words tested for x̂ < ε_n, mirror words for x̂ > ε_p, on all of
q ∈ (1, 23/20], by exact real-root isolation (sympy `real_roots`) in t = q − 1. Report every word,
x̂(1), x̂(q₀), and any window entry with its boundary q. For unlinked words the mirror gives ε_p·f_M, f_M = q⁶f_E (#8836); checked the same way. Also the ≤ 5-vertex subset, for parity
with option 3. Nothing is selected or adopted; a word in the window is reported, not used.
