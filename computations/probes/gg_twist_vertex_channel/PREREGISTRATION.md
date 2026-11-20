# Pre-registration ε-L1V — does the photon's vertex channel V break u↔d?

Written 2026-11-20, before any computation in this directory. Bean `qou-99qc`.

## Why

ε-L1 (`computations/probes/gg_twist_channel_np_probe.py`, PR #8104) asked whether the
photon "twist channel" breaks the u↔d (n↔p) symmetry, using L₊ = σ₁σ₂ and
L₋ = σ₁⁻¹σ₂⁻¹ as that channel. It found ratio 1 on all six words.

Under the owner's photon ruling (2026-11-18, confirmed 2026-11-20;
`QOU/Photon.lean`), the photon is

    γ(φ) = 1 + φ₀σ₀ + φ₁σ₁ + φ₀₁·σ₀σ₁⁻¹,

so its own fourth-term (chiral) channel is the vertex **V = σ₀σ₁⁻¹**, not L±.
PR #8595 left "re-ask ε-L1 of V" open. This is that re-ask.

Strand labels: the probes write σ₀, σ₁ as `1`, `2` (letters `[1, -2]` = V).

## Setup (unchanged from ε-L1 / ε-TR1 / #8586)

- Space (C²)^{⊗3} with the level-2 Jimbo braiding Ř 'std'. Basis e₁ = u, e₂ = d,
  K = diag(q, q⁻¹). σ⁻¹ = σ − h, h = q − q⁻¹.
- **F1, the ε-L1 functional, reused verbatim.** `multiplicity_trace_epsilon_probe.Mmat`:
  the isospin-½ multiplicity trace with emission Ř₃₄. ε_tr(X) = Tr M(X·Δ_S)/Tr M(X), for
  n→p (n_A, n_B → p_A, p_B, s₊) and p→n (mirrored). u↔d asymmetry:
  ratio ε_pn/ε_np − 1.
- **F2, the convention-D trace on the nucleon weight spaces.** τ_zD = Tr(K^{⊗3}·)/[2]³
  (z_D = q³/(q²+1)), split over the T³ sectors W_p (two u) and W_n (one u), with the
  3×3 matrices of `NucleonWeightSpaceTraces.lean` as used in #8586. Reported:
  - the plain sector traces and their difference D(X) = tr_{W_n}(X) − tr_{W_p}(X)
    (this is the u↔d asymmetry of the channel);
  - the K-weighted split ε_flavour(X) = q⁻¹tr_{W_n}(X)/[2]³ − q·tr_{W_p}(X)/[2]³, which is
    the trace's own K-weighting and is reported only as context, not as a channel effect.

## Arms

1. **Arm V (the ruled twist channel).** X ∈ {V, V⁻¹, V·V³, V³·V, V·V⁻¹ (control = 1),
   V·σ₀ (the ε-L1 electron-type slot, L₊σ₀ → V·σ₀)}. These are the ε-L1 words with L₊ → V,
   L₋ → V⁻¹.
2. **Arm γ (the full four-term photon at corpus-derived weights).** The eigenvalue pair
   γ₊ = γ(0, 0, qh), γ₋ = γ(0, 0, −q⁻¹h) (derived in #8586/#8595; γ₊γ₋ = V³).
   X ∈ {γ₊, γ₋, γ₊γ₋, γ₋γ₊}.
3. **Arm φ (symbolic single-crossing weights).** X = γ(φ₀, φ₁, qh)·γ(ψ₀, ψ₁, −q⁻¹h) with
   φ₀, φ₁, ψ₀, ψ₁ symbolic. Report the first-order coefficients ∂/∂φ₀, ∂/∂φ₁, ∂/∂ψ₀, ∂/∂ψ₁ of
   the u↔d asymmetry at φ = ψ = 0 (F2: of D; F1: of t_pn − t_np for numerator and
   denominator traces separately, since ε is a ratio). Also a single symbolic photon
   γ(φ₀, φ₁, φ₀₁).

Exact over ℚ(q) (sympy). Values at the proton q₀ (`Q_50_DIGIT_STR`), mpmath 70 dps,
serialised with `_precision.fmt`. Bar parity (q ↦ q⁻¹) reported for each nonzero closed form.

## Predictions (written before computing)

- **Every arm is u↔d symmetric**: ratio 1 in F1, D = 0 in F2, all first-order
  coefficients 0. Reason expected: V, γ(φ) and every braid word are images of the Hecke
  algebra H₃(q), which commutes with U_q(sl₂). Concretely for F2, Δ = σ₀σ₁σ₀ conjugates
  σ₀ ↔ σ₁ (braid relation), W_n's matrices are W_p's with σ₀ ↔ σ₁ swapped, so every
  element's sector traces agree. For F1, ε-L1 already found every Ř word symmetric; F1
  is linear in X, so symmetry on a spanning set of H₃(q) gives it for every element.
- If symmetric, the claim is scope **(b)** only if the invariant is proved (the Δ
  conjugation; a basis check over H₃(q) for F1), else scope (a) on the listed elements.
- ε_flavour(V) nonzero and exactly bar-odd (it is the trace's K-weighting, as in #8586).

## Not done

Nothing is compared to a physical target (no CODATA, no AME). No element, weight or
word is chosen by any number reported here.
