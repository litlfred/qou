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

## 4. Where `i` enters the pipeline (Lean, sorry-free)

`QOU/Observations/LeptonMassAtI.lean`, following the owner's 02:09Z direction ("group action before
the trace; track the imaginary part").

1. **Before the trace.** The standard 2-dimensional Hecke block, with `T₀ = [[q,1],[0,−q⁻¹]]` and
   `T₁ = [[−q⁻¹,0],[1,q]]` (quadratic and braid relations proved), becomes unipotent at `q = i`
   after the framing normalisation `q⁻¹`. Conjugation by `diag(1, i)` turns it, word by word, into
   the integer `B₃ → SL(2, ℤ)` image (`conj_word`). So the cat-map action *is* the pre-trace block
   at `q = i`. The two choices `±i` give the same integers (`conj_gen_neg`). The `√−1` choice lives
   only in the conjugator, which is the same one bit as the `G_m` orientation (#9944).
2. **The trace.** Every N = 2 ring mass has the factor `q² + 1 = q·[2]_q`, which vanishes at
   `q = i`, so all masses vanish there. For the reduced masses `J = m/(q²+1)` at `q = i`, Lean gives
   `J_e = −2`, `J_μ = 4` and `J_τ = −8`. These equal `∓(2 − tr img β)`, with traces 0, 6 and 10, and
   they are the link determinants (Hopf 2, T(2,4) 4, Whitehead 8, via the standard
   `V(−1) = ±det`, which is not formalised here).
3. **Ratios at `q = i`:** `J_μ/J_e = J_τ/J_μ = −2`, so the ladder doubles. This is the one point
   where the pre-trace group action fixes the mass ratios exactly. It is a value at `q = i`, not at
   `q₀`, and does not give 206.77.

## 5. One `G_m` per component: interactions across components (Lean, sorry-free)

`QOU/Observations/LeptonColouredBurau.lean`, following the owner's 02:14Z direction. Each lepton is a
2-component link, so `G_m × G_m` acts, with one colour `tᵢ` per component, through the coloured
Burau matrices before any trace. The `(0,0)` minor of `I − B` is `(1 − t₂)·Δ_L(t₁,t₂)` up to a unit:

| lepton | `Δ_L(t₁, t₂)` | lk | how the components interact |
|---|---|---|---|
| e (Hopf) | 1 | 1 | trivially |
| μ (T(2,4)) | 1 + t₁t₂ | 2 | only through the diagonal `G_m` (`mu_diagonal`): fully coupled |
| τ (Whitehead) | (t₁ − 1)(t₂ − 1) | 0 | factorises per component (`tau_split`): decoupled at this level |

The `torres` theorem proves `Δ(t,1)(t − 1) = t^lk − 1` per component, which is `U(1) = 3·lk` (#9805)
seen per component. On the diagonal at `t = −1` (`q = i`), `(t − 1)Δ` gives −2, 4 and −8, the same
determinants as §4. The log cross-derivative `∂₁∂₂ log Δ` at `t = 1` (sympy, not in Lean) is 0 for
e, 1/4 for μ and 0 for τ. Reading: the muon is the only lepton whose two components interact at
the Alexander level.

## 6. Two-colour ring trace: one irrep per component (unscored probe)

Probe `computations/probes/lepton_two_colour/two_colour_probe.py` (exact sympy, R-matrix of
`U_q(sl2)`). Each closure component gets its own irrep `V_a` (dimension `a+1`). Take the quantum
trace of the 3-braid word, correct the framing per component by the twist `θ_n = q^{n(n+2)/2}`,
and divide by the unlink value `[a+1][b+1]`. The result `C_L(a,b)` is the cross-component
interaction factor, and `C = 1` at `q = 1`. At `a = b = 1` the traces reproduce the N=2 ring
masses up to a monomial. The Hopf case matches `[(a+1)(b+1)]` exactly.

In `h = log q` (the `G_m` logarithm), with `C_a = a(a+2)` the Casimir:

    log C_L(a,b) = C_a C_b · ( κ₂ h² + κ₃ h³ ) + O(h⁴)

| lepton | κ₂ | κ₃ | `C(q₀)` at (1,1) / (1,2) / (2,2) |
|---|---|---|---|
| e (Hopf) | 1/6 = lk²/6 | 0 | 1.0163 / 1.0437 / 1.1187 |
| μ (T(2,4)) | 2/3 = lk²/6 | −2/3 | 1.0596 / 1.1618 / 1.4613 |
| τ (Whitehead) | 0 = lk²/6 | 4/3 | 1.0112 / 1.0305 / 1.0842 |

Checked at three colour pairs each, not proved for all colours. The `h⁴` term no longer
factorises as `C_a C_b`.

* **h² is pure linking.** The quadratic term is `lk²·C_a C_b/6`. So the muon's components couple
  four times as strongly as the electron's, and the tau's not at all at this order.
* **The odd part carries chirality.** `h ↦ −h` is `q ↦ q⁻¹`, the mirror. The electron has no odd
  terms. The tau's interaction starts at `h³`, so it is purely odd at leading order. Its sign is
  therefore the `G_m` orientation bit of §4 again. It moves the bit to the first odd jet order
  but does not fix it.
* No `C` value is near 206.77. This gives a coupling hierarchy, not a mass ratio.

## Open

* The muon pin (bean): derive `m_μ/m_e` from the axioms. Level one is excluded (§1).
* Which pre-trace (block-level) group action relates component masses. This is the owner's next
  direction (2026-11-28 02:09Z).
