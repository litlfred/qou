# Picard-Lefschetz SW Period — Deriving m_p/m_e from q₀

## Status: OPEN PROBLEM for next session

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
