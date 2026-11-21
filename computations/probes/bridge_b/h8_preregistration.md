# H8: an open categorical trace with a boundary object at the wall (pre-registration, 2026-11-21)

The user chose "Yes, pre-register H8" on the card. Written before anything is computed.

## Setting

The categorical action is a closed trace, `𝔖 = λ·tr(ℒ_q) = λ·ev ∘ (id ⊗ ℒ_q) ∘ coev`, unique up to
one scalar λ. On the three-strand nucleon space that trace is the pivotal trace `tr(K^{⊗3}·M)`.

A wall opens the trace at strand 1. Closing strand 1 through the boundary object (the type-B
reflection solution `𝒦`, H5) gives the boundary trace `tr(K^{⊗3}·M·𝒦₁)`. If the boundary inherits the
same λ, the two-piece action is

  `𝔖 = λ·[ tr(K^{⊗3} M) + tr(K^{⊗3} M 𝒦₁) ]`,

restricted to each weight space. Then ε = 1, but `𝒦` carries its own scale: by H5 the boundary trace
is proportional to `s = x + y`. So the effective coupling is `ε_eff = s`, and H8 asks whether a
corpus rule fixes `s`.

Framework: ruled photon, so the word is V³ = `γ(0,0,qh)·γ(0,0,−q⁻¹h)` (the general γγ pair is noted,
not swept). One-term `M_QCD` only. The electron is not in this word.

## Candidates for s, listed before evaluation

- **N1 Folding** (AGENTS.md §7b). The boundary generator gets the crossing's Hecke eigenvalues
  `{q, −q⁻¹}`, so `s = h = q − q⁻¹`.
- **N2 Involutive boundary** `𝒦² = 1`, with eigenvalues `{1, −1}`: `s = 0`. An expected null.
- **N3 Unit Markov value** `tr(K𝒦)/tr(K) = 1`: `s = (q² + 1)/q²` (from H6, `q²s/(q²+1)`).
- **N4 Quantum dimension.** The boundary object has the same categorical dimension as the strand it
  closes: `tr(K𝒦) = tr(K) = [2]_q`, which gives `s = [2]_q/q`. It is related to N3 and recorded
  separately.

## What is reported for each

1. Its status in the corpus: derived, a convention, or not stated.
2. The open-trace relative n − p measure:
   `D = (T_n + s·T̂_n)/(T_p + s·T̂_p) ÷ (T_n/T_p)`, with `T̂` the boundary trace at `s = 1`.
   `D = 1` means the wall changes nothing beyond the pivot.
3. Its value at q₀ and its limit at q = 1.

## Classification and discipline

A **hit** is a candidate whose `s` is fixed by a corpus statement rather than by a convention chosen
here, and which gives `D ≠ 1`.

`D` is not a mass. The trace-to-MeV map is not derived (B1 was refuted). No candidate is ranked by
closeness to the measured value. Any CODATA comparison appears only in a section labelled physics.
