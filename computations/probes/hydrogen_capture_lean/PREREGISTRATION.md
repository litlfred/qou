# Pre-registration: Lean for the hydrogen capture braid and the chirality × placement sign (2026-11-22)

Owner, 2026-11-22, card "What should I work on next for m_n?": *"Lepton-strand route for n-p"*.
Scope agreed with the m_n own-identity thread (draft PR #8804), which asked for item (b):
formalise the exact targets of `mn_hydrogen_capture_chirality_probe` (§43 there).
Written and committed before any number for this probe is computed.

## Objects (as in #8804 §43, unchanged)
- `(C²)^{⊗4}`, Jimbo `Ř`: `Ř e₀₀ = q e₀₀`, `Ř e₀₁ = e₁₀`, `Ř e₁₀ = e₀₁ + h e₁₀`, `Ř e₁₁ = q e₁₁`, `h = q − q⁻¹`.
- Capture, proton left: `W_L = (σ₀σ₁⁻¹)³ · (σ₂σ₁σ₀σ₀σ₁σ₂)⁻¹`, proton strands 0–2, electron strand 3.
- Capture, proton right: `W_R = (σ₁σ₂⁻¹)³ · (σ₀σ₁σ₂σ₂σ₁σ₀)⁻¹`, proton strands 1–3, electron strand 0.
- `T³ = (#0 − #1)/2`; `O₊` = proton strands carry 2 zeros, `O₋` = 1 zero; `F₁(O) = tr(T³ W Π_O)`,
  `S := F₁(O₊) + F₁(O₋)`. The photon is `1 + φ₀σ₀ + φ₁σ₁ + φ₀₁σ₀σ₁⁻¹` and `(σ₀σ₁⁻¹)³` is the
  γγ product of `borromeanV3A_eq_switched_photon_product`; no virtual photons enter.

## Predictions derived in advance (no compute)
- **D1 (weight reduction).** `Ř` preserves the number of zeros, so `W` is block diagonal over
  weights `z = 0..4`, and `T³ = z − 2`. On `O₊ ∪ O₋` only `z ∈ {1,2,3}` occur and `z = 2` has
  `T³ = 0`. Hence `S = Σ_{z=3, the 1 on a proton strand} W_ss − Σ_{z=1, the 0 on a proton strand} W_ss`.
  Only the two 4-dimensional weight spaces enter.
- **D2 (flip).** The spin flip `X` satisfies `X Ř X = Π Ř Π` (`Π` swaps the two tensor factors),
  so the `z = 3` block of a word equals, up to the basis relabelling `X`, the `z = 1` block of the
  same word with each `σ_i` replaced by `σ_i` acting with the reversed `Ř`.
- **D3 (conjecture, to be tested).** As for `n = 3` (`NucleonWeightSpaceTraces.trace_word_eq`),
  the two 4-dimensional weight spaces carry isomorphic braid actions, so every word has equal
  trace on them. If D3 holds, `S = W_{ee}|_{z=1} − W_{ēē}|_{z=3}`, where `e` (resp. `ē`) puts the
  minority spin on the electron strand: S is one matrix entry minus another.
- **D4 (reproduce #8804).** `S(W_L) = −h²[3]_q`, `S(W_R) = +h²[3]_q`, and the placement mirror
  `F₁(O₊; W_L) = −F₁(O₋; W_R)`.

What would refute: D3 fails if no invertible intertwiner exists (then the traces differ for some
word). D4 fails if the Lean-checked values differ from the #8804 sympy values.

## Method
Lean first (`QOU/BraidsAndKnots/HydrogenCaptureWeightSpace.lean`, generic `[Field R]`, sorry-free
target). A sympy check over ℚ(q) only to find the intertwiner for D3 and to cross-check; 60 dps
mpmath at q₀ for any reported value. No float64, no CODATA.

**Pre-registration completed: 2026-11-22 (UTC), before any computation for this probe.**
