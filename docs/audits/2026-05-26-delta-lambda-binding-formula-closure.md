# Δ_λ binding formula closure — top-down from the categorical action

## Status: CLOSED for deuteron (2026-05-26)

The per-isotope binding-energy formula is derived top-down through
the Cat → Alg → Geom → Arch pipeline with **zero free parameters**:

    B(K) = m_e × |Σ_λ y_λ · χ^λ(β_K) · sgn(w_0^{S_{λ'}}) · f^λ|

Each factor comes from a specific pipeline layer:

| Factor | Pipeline layer | Source | Status |
|--------|---------------|--------|--------|
| sgn(w_0^{S_{λ'}}) | **Categorical** | Macdonald I.1.5 | PROVED (PR #1305) |
| f^λ = dim(V_λ) | **Categorical** | Regular-rep / Burnside | PROVED (PR #1305) |
| y_λ | **Algebraic** | Wenzl Markov weights | Computed (on disk) |
| χ^λ(β_K) | **Geometric** | Hoefsmit + interface operator | Computed (branching witness) |
| m_e, q₀ | **Archimedean** | CAL-1, CAL-2 evaluation | Input |

The "geometric layer" is not a separate multiplicative constant —
it is encoded in χ^λ(β_K) via the interface operator between
nucleon H_3 subspaces within H_{3A}. The interface flips the sign
of dominant partitions and sets the binding magnitude.

## How the six prior ansätze failed (and why this one works)

The prior Δ_λ attempts (Frobenius co-Casimir, Demazure, LP-Plancherel,
LP-Frobenius, crystal, augmented Markov) failed because they tried to:
1. Derive Δ_λ from **single-nucleon** data (missing the interface)
2. Use **q-dependent** algebraic expressions (mixing Cat and Alg layers)
3. Treat the geometric correction as a **separate constant** to be fitted

The correct approach: Δ_λ lives at the **categorical** level (sign × dim,
q-independent), and the geometric correction lives inside χ^λ(β_K) via
the interface operator — already computed, not a separate parameter.

## Remaining: T, ³He, ⁴He

| Atom | H_n | χ^λ (chi-cache) | Interface branching | Status |
|------|-----|-----------------|---------------------|--------|
| D | H_6 | on disk | on disk (deuteron branching) | **CLOSED** |
| T | H_9 | on disk | on disk (H_9 tritium branching) | ready to wire |
| ³He | H_9 | on disk | on disk (H_9 branching) | ready to wire |
| ⁴He | H_12 | on disk | needs H_12 branching (~30 min) | feasible |

## References

- PR #1305 (merged): sign rule + dim weight proofs
- PR #1296 (merged): 4-atom cross-validation, Wenzl y_λ for H_9/H_12
- PR #1292 (merged): CAL-3 = m_π, meson/lepton dictionary
- `sublemma-2-1-deuteron-branching.witness.json`: interface ratios
- `deuteron-binding-interface-closure.witness.json`: zero-parameter result
