# Pre-registration: the linked n → p e⁻ ν̄ process word on 9 strands (issue #8833)

Written and committed before the probe in this directory is run.

## Rulings used (none chosen here)

* Photon vertex V_i = σ_i σ_{i+1}⁻¹ (owner 2026-11-20). Proton word β_Bor = V₀³ on strands 0–2.
* Electron σ₀σ₁σ₀, Hopf closure; antineutrino the unknot.
* The γγ lepton pair carries an extra closed loop: e⁻ + ν̄ + unknot on 6 strands, from a
  neutral start (owner card 2026-11-21, option 3; `docs/coordination/owner-rulings.md`).
* Q_β is not taken to be linear in the trace (owner, working conjecture); this probe computes
  x only and maps nothing to MeV.
* q₀: proton pin. Jimbo R on (C²)^{⊗9}, eigenvalues q, −1/q.

## The value computed

x(W) = Tr(K^{⊗9} P ρ(W)) / [2]⁹, P the projector onto nucleon strands 0–2 at weight q (one
down) and lepton strands 3–8 at weight q⁻² (four down). This is the nucleon rule of #8868
(K-weight × sector trace / [2]ⁿ) on the final-state sector fixed by K-conservation from
n (q⁻¹) ⊗ neutral 6-strand vacuum. For an unlinked word (X = 1) it factorises as
x = ε_p · f_L, f_L = q⁻²·tr_{d=4}(ρ(L))/[2]⁶; this is checked, not assumed.

x is a restricted-sector trace, not a link invariant: conjugating W can change it. Reported as
such.

## The closed family

W = X · β_Bor · L, where

* L: every γγ word on strands 3–8 (vertices V₃..V₆) of 1 to 5 vertices whose framing-corrected
  invariant equals that of Hopf ⊔ unknot ⊔ unknot or its mirror at q = 2 and q = 3 exactly
  (the 60 + 60 found in the 6-strand enumeration);
* X: every product of 0 to 6 junction vertices from {V₁, V₂} (the only vertices that cross
  between strand 2 and strand 3) whose strand permutation is the identity, so every closure
  keeps its seven components (three Borromean + four lepton). Length cut-off fixed here,
  because braid traces are not bounded in word length.

## Reported for every word

x at q₀; whether x lies in the #8868 window (0.33174, 0.40872); vertex counts; whether L is
e⁻ν̄ or the mirror. The window cannot separate e⁻ν̄ from e⁺ν (the closure invariant does not
see the ν/ν̄ label).

## What this does NOT do

No word is selected or scored. A word landing in the window is reported, not adopted: which
X is the physical junction is an owner call, and picking it by the window would be a fit.
