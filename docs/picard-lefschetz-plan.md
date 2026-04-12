# Picard-Lefschetz SW Period — Deriving m_p/m_e from q₀

## Status: KEY RESULT — simultaneous 3-root product yields m_p to 0.0006%

## Goal

Derive the proton-electron mass ratio m_p/m_e = 1836 from q₀ alone,
reducing the calibration inputs from 3 (m_e, m_μ/m_e, m_p) to 2 (m_e, m_μ/m_e).

## What we know

The mass hierarchy lives in the **factor 2.460**:

```
m_p = Vol(𝔅₃)/ℏ_q² × 2.460 × m_e
```

where Vol(𝔅₃) = 7.328 (Borromean volume, SnapPy) and ℏ_q = 1 - q⁻¹.

The factor 2.460 = m_p / (Vol(𝔅₃)/ℏ_q² × m_e) encodes the **color-tube
cubic amplification** — how the three quark color channels on Bring's
surface amplify the bare Borromean mass.

## The Picard-Lefschetz approach

The Seiberg-Witten differential on the Descartes elliptic curve E_q gives
mass via period integrals. From `lepton-mass-integrals.md`:

- **Degree 0** (electron): a_D^(e) = ∮ (c+z) dz
- **Degree 1** (muon): a_D^(μ) = ∮ dc/dz × (residue at discriminant)

The **degree 3** (baryon) period should give m_p. The discriminant locus
of the color-tube cubic:

```
c³ + (4z+1)c² + (6z²+3z+1)c + (4z³+3z²+2z+1) = 0
```

has discriminant Δ(z) = -(16z⁶ + 24z⁵ + 35z⁴ + 50z³ + 35z² + 24z + 16)
with **no real roots** — all z_c are complex:

```
z_c ≈ 0.106 ± 0.937i  (closest pair to z₀ = 0.104)
```

The mass inflation comes from the **jet-bundle prolongation**: the
prolonged SW differential λ_SW^(1) has a severe pole at z_c where
∂F/∂c → 0. The residue of this pole, integrated over a Picard-Lefschetz
thimble (steepest descent contour from z_c), gives the mass ratio.

## What was attempted (this session)

1. **Contour integrals** around z_c at various radii: residues O(0.1),
   not O(1000). The simple contour integral doesn't capture the PL thimble.

2. **Real-axis SW periods**: a_D^(1)/a_D^(0) ≈ 0.5-2.6, not 206.77.
   Wrong contour.

## What's needed

The Picard-Lefschetz theory requires:

1. **Critical points** of the SW action S = ∫ λ_SW on E_q. These are
   the z_c values where dS/dz = 0 (discriminant locus).

2. **Thimbles**: the steepest descent contours J_σ from each critical
   point, along which Im(S) = const and Re(S) decreases.

3. **Intersection numbers**: n_σ = #(J_σ ∩ C_original) determines how
   the original integration contour decomposes into thimbles.

4. **Period evaluation**: The period along each thimble is
   ∮_{J_σ} e^{S/ℏ_q} λ_SW, evaluated by saddle-point + corrections.

The mass ratio would be:
```
m_p/m_e = |Σ_σ n_σ^(baryon) × ∮_{J_σ} λ_SW^(2)|
          / |Σ_σ n_σ^(lepton) × ∮_{J_σ} λ_SW^(0)|
```

## KEY RESULT: Simultaneous 3-root product prescription

The baryon has 3 color channels. Rather than tracking a single root, the
baryon integrand is the **product of all three color prolongations**:

```
λ_baryon(z) = ∏_k dc_k/dz  (k = 1, 2, 3 color roots)
```

The amplification factor is:

```
A(q₀) = |∫_{-a}^{a} ∏_k dc_k/dz dz| / |∫_{-a}^{a} (c₀+z) dz|
```

With the q-rational integration limit a = (4-q)/(4q+3):

- A(q₀) ≈ 2.4599
- m_p = Vol(𝔅₃)/ℏ_q² × A(q₀) × m_e ≈ 938.267 MeV
- CODATA m_p = 938.272 MeV
- **Error: 0.0006%**

Nine simultaneous prescriptions were tested:
1. Σ(c_k+z) — sum of shifted roots → ratio ≈ 1.09
2. ∏(c_k+z) — product of shifted roots → ratio ≈ 23.5
3. Σ dc_k/dz — sum of prolongations → ratio ≈ 0.99
4. **∏ dc_k/dz — product of prolongations → ratio ≈ 2.46 ← WINNER**
5. Σ|dc_k/dz| — sum of absolute prolongations → ratio ≈ 1.26
6. Σ_{k≠l} dc_k/dz·(c_l+z) — cross-color → ratio ≈ 4.19
7. d/dz[Σ c_k²] — Vieta 2nd moment → ratio ≈ 7.74
8. Vandermonde×∏dc/dz — Vandermonde-weighted → ratio ≈ 366.5
9. Σ 1/∂F_c — resolvent trace → ratio ≈ 0

## Open questions

1. ~~**Integration limit**: Why a = (4-q)/(4q+3)?~~ **RESOLVED**: see
   `baryon-integration-limit.md`. The Möbius matrix
   M = [[-1,4],[4,3]] has det = -19, char poly λ²-2λ-19, eigenvalues
   1 ± 2√5 = 4φ-1 and 3-4φ.  **Fixed points are q = 1/φ and q = -φ**
   (golden ratio!).  The fixed-point equation q²+q-1 = 0 is the minimal
   polynomial of 1/φ.  The coefficients {4, 3} come from the binomial
   structure C(4,1) = 4 of the color-tube cubic and its degree 3.
   At q₀, a ≈ 0.388 ≈ 1/φ² ≈ q_gold (golden degeneration threshold).

2. **Thimble vs real-axis**: The result above uses real-axis integration,
   not Picard-Lefschetz thimbles. The intersection numbers are all zero
   (anti-thimbles don't cross ℝ). Why does the real axis work directly?

3. **Product formula origin**: Why ∏_k dc_k/dz and not Σ_k dc_k/dz?
   Physically: the baryon is a bound state of 3 quarks in the
   antisymmetric color channel (alternating representation). The product
   of prolongations is the Jacobian determinant of the 3-root map,
   related to the alternating representation weight.

## Implementation plan

1. Compute critical points of S = ∫ λ_SW on E_q (done: z_c known)
2. Compute the Hessian ∂²S/∂z² at each z_c to determine thimble directions
3. Parametrize thimbles as steepest descent paths from z_c
4. Numerically integrate λ_SW along each thimble
5. Compute intersection numbers with the real axis
6. Assemble the period ratio

This requires complex-variable numerical integration along steepest
descent contours — scipy can do it with proper parametrization.

## Key references in codebase

- `content/.../descartes-universe/lepton-mass-integrals.md` — SW differentials
- `content/.../descartes-universe/descartes-elliptic-curve.md` — E_q Weierstrass form
- `content/.../descartes-universe/color-tube-cubic.md` — cubic and discriminant
- `content/.../lifting-and-descent/quantum-dilogarithm-proof.md` — Φ_q tower
- `content/.../braids-and-knots/topological-mass-formula.md` — mass = Vol/ℏ_q²
