/-!
# Ground Ring Annotations

Each Lean module in the QOU formalization works over a specific ring.
The **formal proof chain** (the results that constitute the paper's
theorems) uses only `ℤ[q, q⁻¹]`.  Modules over `ℝ` or `ℂ` provide
the **archimedean realisation** — they specialise the formal results
to numerical computations but are NOT part of the formal chain.

## Annotation Table

| Module | Ground ring | Formal chain? | Notes |
|--------|-------------|:---:|-------|
| **Descartes/** | `ℤ[q, q⁻¹]` | ✓ | Transfer matrices, β-decay, spectral decomposition |
| **GrobnerShirshov/** | `ℤ[q, q⁻¹]` | ✓ | Hecke algebra, admissible systems, PBW bases |
| **CategoricalFoundations** | generic `k` | ✓ | Categorical axioms (ring-independent) |
| **Structures** | generic `k` | ✓ | Involutive, Hodge, spin structures |
| **Instanton** | generic `k` | ✓ | q-deformed exterior derivative |
| **GaugeTheory** | generic `k` | ✓ | Categorical connection, action |
| **VolumeForm** | generic `k` | ✓ | Volume from rigidity |
| **PathIntegrals** | generic `k` | ✓ | Braid group, quantum SU(2) |
| **Torsion/** | generic `k` | ✓ | Jet prolongation, brane tower, descent |
| **KnotTheory** | `ℤ` | ✓ | Crossing sign, planar diagram |
| **KnotRegistry** | `ℤ` | ✓ | Knot data (integer invariants) |
| **BringsSurface** | `ℂ` | — | Archimedean realisation |
| **CRRealisation** | `ℂ` | — | ℂ quantum observable universe |
| **Calculations** | `ℝ` | — | Numerical substrate derivation |
| **MassDerivation** | `ℝ` | — | Topological mass (numerical) |
| **CODATAChain** | `ℝ` | — | End-to-end CODATA comparison |
| **ArchimedeanMassFormula** | `ℝ` | — | Volume → mass (numerical) |
| **HadronicMass** | `ℝ` | — | Terminal resolution (numerical) |
| **MathConstants** | `ℝ` | — | Derived physical constants |
| **Elaboration** | `ℝ` | — | d_q² computation (numerical) |
| **SubstrateParameter** | `ℝ` | — | q(p) field (numerical) |
| **FormalGroups** | generic `k` | ✓ | Skewed-Poisson, Witt vectors |
| **RepresentationTheory** | generic `k` | ✓ | Categorical hadrons |
| **PhotonThreading** | `ℤ[q, q⁻¹]` | ✓ | Hecke cost = mass |
| **MobiusEnergy** | `ℝ` | — | Energy functional (numerical) |
| **InformationTheory** | `ℝ` | — | Planck length, bandwidth |
| **GaugeFieldFluidDynamics** | `ℝ` | — | Brane fluid (numerical) |
| **PAdicQuantumGroups** | `ℚ_p`, `𝔽_p` | ✓ | p-adic realisation |

## The formal chain

The paper's formal results form a chain over `ℤ[q, q⁻¹]`:

```
ℤ[q, q⁻¹] (GroundRing)
  → Hecke algebra H_A(q) (GrobnerShirshov)
  → Torus knots τ(r,s) (TorusKnot)
  → Transfer matrices T(q) (TransferMatrix)
  → Skein polynomial P(q) (SkeinPolynomial)
  → β-decay operator T_{β-decay}(q) (BetaDecay)
  → Spectral decomposition Q_q (SpectralDecomp)
```

Results over `ℝ` (archimedean realisation) are obtained by
specialising `q ↦ q₀ ≈ 1.1098` and are confined to Chapter 7.

## Bridge: specialisation map

The specialisation `ι : ℤ[q, q⁻¹] → ℝ` sends `q ↦ q₀` where
`q₀ = 1 / (1 - √(Vol(4₁) / (m_μ/m_e)))`.  Every formal result
over `ℤ[q, q⁻¹]` descends to a numerical result via `ι`.

**Note to reader**: Lean proofs in the formal chain work exclusively
over `ℤ[q, q⁻¹]`.  Numerical evaluations (Chapter 7) use the
archimedean specialisation and are NOT part of the formal chain.
-/

-- This file is documentation only; no Lean definitions.
