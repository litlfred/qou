import Mathlib.Tactic.Ring

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
| **KnotTheory** | `ℤ` | ✓ | Crossing sign, braid word |
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
| **ArchimedeanSubstrateField** | `ℝ` | — | q(p) field (numerical) |
| **FormalGroups** | generic `k` | ✓ | Skewed-Poisson, Witt vectors |
| **RepresentationTheory** | generic `k` | ✓ | Categorical hadrons |
| **PhotonThreading** | `ℤ[q, q⁻¹]` | ✓ | Hecke cost = mass |
| **MobiusEnergy** | `ℝ` | — | Energy functional (numerical) |
| **InformationTheory** | `ℝ` | — | Planck length, bandwidth |
| **GaugeFieldFluidDynamics** | generic `R` + `ℝ` shim | partial | q-arithmetic (`qInteger`, `qFactorial`, `qBinomial`, `qHookProduct`) generic over `[Field R]`; the ordering-dependent declarations (`pow_gt_inv_pow`, `qInteger_pos`, `qInteger_sq_pos`, `qInteger_ne_zero`, `markovParameter`, `markovParameter_pos`) stay at `ℝ` as the archimedean shim |
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

## Co-located stub annotations

Co-located `.lean` stubs live alongside `.ts`/`.md` content blocks in
chapter directories (NOT under `lean/QOU/`).  They are documentation
stubs — **not compiled by `lake build`** — that mirror the paper's
mathematical content in Lean syntax.

Each stub carries a ground-ring annotation in its module docstring.
Stubs in the formal chain use `R_q = ℤ[q, q⁻¹]`; stubs in the
archimedean realisation use `ℝ`.

### Formal chain stubs (R_q)

Stubs for definitions and theorems that belong to the formal proof
chain declare a local `R_q := LaurentPolynomial ℤ` and work over
the Laurent polynomial ring.  The parameter `q` is the canonical
indeterminate of `R_q`.  Ordering constraints (`q > 1`, `0 < q`)
are commented out — they are archimedean and not meaningful over `R_q`.

Directories: `quantum-observable-universes/`, `quantum-universes/`,
`models-of-qous/`, `lifting-and-descent/`, `braids-and-knots/`,
`archimedean-universe/` (algebraic stubs), `algebraic-substrate/`,
`information-theory/` (bounds).

### Archimedean stubs (ℝ)

Stubs that evaluate formal results at `q₀ ≈ 1.1098` for comparison
with experimental data.  These use `ℝ` and are NOT part of the
formal proof chain.

Directories: `observations/`, `glossary/`, `archimedean-universe/`
(mass predictions), some `information-theory/` files.

### Geometric/analytic stubs (ℝ)

Stubs using ℝ-specific analysis functions (trig, norms, real powers)
that cannot be expressed over `R_q`.

Includes: `exceptional-divisor`, `descartes-elliptic-curve`,
`mass-identity`, some `models-of-qous/` files.

### Co-located stub summary table

| Directory | Ground ring | Notes |
|-----------|------------|-------|
| `quantum-observable-universes/` | `R_q` | Categorical definitions (Ch 1–2) |
| `quantum-universes/` | `R_q` | Foundational structures (Ch 1) |
| `models-of-qous/` | `R_q` or `ℝ` | Categorical models (Ch 3) |
| `braids-and-knots/` | `R_q` or `ℝ` | Braid/knot algebra (Ch 4) |
| `archimedean-universe/` | `R_q` or `ℝ` | Particles (R_q), mass predictions (ℝ) |
| `lifting-and-descent/` | `R_q` or `ℝ` | Categorical lifting (Ch 6) |
| `algebraic-substrate/` | `R_q` or `ℝ` | q-analytic number theory |
| `observations/` | `ℝ` | Archimedean realisation (Ch 7) |
| `information-theory/` | `R_q` or `ℝ` | Info-theoretic bounds |
| `glossary/` | `ℝ` | Cross-references |
-/

-- This file is documentation only; no Lean definitions.
