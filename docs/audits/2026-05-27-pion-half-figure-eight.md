# Audit: pion = half-figure-eight on V_(2,1)

**Date:** 2026-05-27
**Branch:** claude/meson-spectrum-vol-conj-2026-05-27

## Finding

The pion knot operator M_π and the half-4₁ braid σ₁σ₂⁻¹ have
**identical eigenvalue phases** on V_(2,1):

| Braid | Phase θ | |λ| |
|-------|---------|-----|
| M_π = (σ₁σ₂)²σ₂σ₁ | 2.1198 | 1.0 |
| σ₁σ₂⁻¹ (half-4₁) | 2.1198 | 1.0 |
| L₊ = σ₁σ₂ (Hopf) | 2.0944 = 2π/3 | 1.0 |
| (σ₁σ₂⁻¹)² = 4₁ | 2.0435 ≈ Vol(4₁) | 1.0 |

## Structural interpretation

1. The pion IS a half-Reeb-rotation on V_(2,1)
2. The figure-eight 4₁ = two pion rotations composed
3. Vol(4₁)/ℏ² (the lepton mass ratio) = two pion rotations / ℏ²
4. Pion decay = inverse half-Reeb-rotation (de-entanglement)

## What is derivable vs empirical

**Derivable (for paper):**
- M_π and σ₁σ₂⁻¹ have identical eigenvalue phases (algebraic identity)
- det(M_π) = det(σ₁σ₂⁻¹) = +1 → both unitary on V_(2,1)
- 4₁ = (σ₁σ₂⁻¹)² = two half-rotations composed

**Empirical (audit only):**
- θ(4₁) = 2.044 ≈ Vol(4₁) = 2.030 (0.67% match)
- θ(M_π) = 2.120 ≈ Vol(4₁) + correction (4.4% off Vol)
- The specific numerical match θ ≈ Vol is not derived

## How to use

- The algebraic identity (M_π phase = σ₁σ₂⁻¹ phase) can be
  stated as a proposition and proved in Lean
- The "pion = half-4₁" interpretation gives the categorical
  relationship between mesons and the lepton mass ratio
- The SDP on V_(2,1) can use this to constrain the meson
  normalization: m_π's normalization is the half-rotation energy
