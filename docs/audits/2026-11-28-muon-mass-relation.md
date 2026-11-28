# Derive the muon mass relation (2026-11-28)

Thread "Derive the muon mass relation". Owner ruling (2026-11-28 01:55Z): `q₀` goes back to the
proton pin unless CAL-2, `m_μ/m_e = Vol(4₁)/ℏ_q²`, is proved; the muon pin stays an open bean.
The proton-pin migration and the exposition cleanup are the tau thread's work. They are not done here.

## 1. The level-weight route gives an upper bound (Lean, sorry-free)

`QOU/MassTheory/MuonLevelRatio.lean`, in any ordered field, with no `ℝ` and no measured value:

* `m_μ/m_e = R(q) = (q⁸+q⁴−q²+1)/(q⁶(q⁴+1))` on the ring masses (N = 2 reading).
* `R(q) ≤ 1` for `q ≥ 1`, because `q⁶(q⁴+1) − (q⁸+q⁴−q²+1) = (q²−1)(q⁸+q⁴+1)`.
* `level_ratio_le`: the level-`n` Laplacian candidate `ρ = R/(ℏ_q[k]_u)^(2n)` satisfies
  `ℏ_q^(2n) ρ ≤ 1` for every `q > 1` and every mode `k ≥ 1`.
* `level_one_ne_cal2`: at level one, `ρ ≠ V/ℏ_q²` for any `V > 1`. Since `Vol(4₁) ≈ 2.03 > 1`, the
  level-one weight cannot produce CAL-2 at any `q`. That is consistent with the owner's ruling that
  CAL-2 is a calibration (#9952).
* `leading_coeff`: the pole coefficient at `q = 1` is `1/k^(2n)`, which is rational.

Unscored comparison (q₀ ≈ 1.10998, the same at either pin to 12 ppb): `ℏ_q⁻² ≈ 101.9`, so level
one gives at most ≈ 77.7 (k = 1). Level two gives a discrete set {7910, 606, 146, 56, 28, …}
(k = 1, …, 5) that does not contain 206.77. No `(n, k)` was selected, so nothing was fitted.

## 2. The words through the cat map (Lean, sorry-free)

`QOU/Observations/LeptonWordsCatMap.lean`: `L = σ₀σ₁⁻¹ ↦ [[2,1],[1,1]]` (Arnold's cat map), with
`4₁ = L²`, `μ = σ₀³L` and `τ = σ₀L²`. The images are e `[[0,1],[−1,0]]` (tr 0), μ `[[5,4],[1,1]]`
(tr 6), τ `[[8,5],[3,2]]` (tr 10) and 4₁ `[[5,3],[3,2]]` (tr 7). Also `img τ ≠ img μ · img 4₁`, in
either order, so braid multiplication by `4₁` is not the μ → τ step.

## 3. Complex volumes `Vol + i·CS` (SnapPy probe, comparison only, not in any proof)

Probe: `computations/probes/lepton_complex_volume/complex_volume_probe.py`. Closure ∪ axis is the
closure of `β · σ₃σ₂σ₁²σ₂σ₃` in B₄. This construction reproduces the earlier 5.33349 for σ₀²σ₁⁻¹.

| word | closure | closure ∪ axis | mirror flips CS? |
|---|---|---|---|
| e = Δ (Hopf) | not hyperbolic (Seifert) | not hyperbolic (Δ periodic) | — |
| μ = σ₀⁴σ₁⁻¹ (T(2,4)) | not hyperbolic (torus link) | 6.354587 + 2.997871 i | yes: −2.997871 |
| τ = σ₀²σ₁⁻¹σ₀σ₁⁻¹ (Whitehead) | 3.663862 + 2.467401 i (= π²/4) | 9.503404 + 4.081330 i | yes |
| 4₁ = L² | 2.029883 + 0 i | 8.119533 + 0 i (= 4·Vol(4₁) numerically) | CS = 0 |

Readings:
* On closures, e and μ both have no hyperbolic structure. The real part of the complex volume
  cannot separate them, so the e → μ step cannot come from closure volumes.
* The Whitehead closure's CS = π²/4 is its own negative modulo π²/2. It cannot carry the sign bit.
* On closure ∪ axis, μ and τ are chiral: the mirror flips CS, and CS is not a half-period. So the
  chirality bit (Bring orientation = Gm orientation, #9944) can be placed upstream as the
  orientation of the muon's braid ∪ axis complex volume. Amphichiral 4₁ has CS = 0, as expected.
* Ordering on closure ∪ axis: e 0 < μ 6.35 < τ 9.50. No mass rule has been fixed, so this is not
  scored (owner: "Derive the reading first").

## Open

* The muon pin (bean): derive `m_μ/m_e` from the axioms. Level one is excluded (§1).
* Which pre-trace (block-level) group action relates component masses. This is the owner's next
  direction (2026-11-28 02:09Z).
