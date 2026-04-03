# Stub / Placeholder / Trivial-True / Narrative-Alignment Audit

**Date**: 2026-03-25
**Scope**: All `.lean` files on the critical dependency path to `prop:local-substrate-q`

---

## 1. Tautological / Trivial Proofs

These are theorems where the "proof" merely restates a hypothesis or
unpacks a structure field — the mathematical work is pushed into the
caller, not actually verified.

### 1.1 `mass_decomposition_categorical` — TAUTOLOGICAL

**File**: `ch3-lifting-of-quantum-torsion/topological-mass.lean:52–59`

```lean
theorem mass_decomposition_categorical
    (md : MassDecomposition R)
    (orthogonal : ‖md.totalTrace‖ =
      ‖md.descendedTrace‖ + ‖md.transientTraces.foldl (· + ·) 0‖) :
    categoricalMass md.totalTrace =
    categoricalMass md.descendedTrace +
      ‖md.transientTraces.foldl (· + ·) 0‖ :=
  orthogonal            -- ← just returns the hypothesis
```

**Problem**: The theorem takes `orthogonal` (the very conclusion) as a
hypothesis and returns it. This is a definitional tautology — the real
work (proving the norm splits additively from the idempotent decomposition)
is not done.

**Narrative says** (.md): "The decomposition follows from the idempotent
splitting... and the linearity of the categorical trace. When the splitting
is orthogonal with respect to the Frobenius norm..."

**Gap**: The .md identifies the actual proof obligation: that Frobenius-norm
orthogonality follows from the idempotent splitting. The Lean assumes this
as a hypothesis.

**Severity**: **HIGH** — this is the main mass decomposition theorem.

---

### 1.2 `transient_localisation` — PURE TAUTOLOGY

**File**: `ch3-lifting-of-quantum-torsion/topological-mass.lean:65–73`

```lean
theorem transient_localisation
    (traces : List R)
    (disjoint : ∀ i j, i ≠ j → ... → traces[i]! * traces[j]! = 0) :
    ∀ i j, i ≠ j → ... → traces[i]! * traces[j]! = 0 :=
  disjoint              -- ← conclusion = hypothesis, verbatim
```

**Problem**: Conclusion is identical to hypothesis. Zero content.

**Severity**: **MEDIUM** — supporting lemma, but completely vacuous.

---

### 1.3 `mass_is_holonomy` — STRUCTURE FIELD UNPACK

**File**: `ch3-lifting-of-quantum-torsion/mass-identity-C.lean:38–40`

```lean
theorem mass_is_holonomy (mic : MassIdentityC) :
    mic.mult_integral_norm = mic.holonomy_norm :=
  mic.stokes
```

**Problem**: The theorem just extracts the `.stokes` field from the
`MassIdentityC` structure. The nonabelian Stokes theorem is assumed,
not proved.

**Narrative says** (.md): "the categorical mass of a closed cycle γ
encircling a vortex filament equals the Killing-form norm of the holonomy"

**Severity**: **MEDIUM** — the Yekutieli integral is a deep result, not
trivially dischargeable, but the structure-assumption pattern is consistent
with the categorical-packaging approach used elsewhere.

---

## 2. Hardcoded Predictions (Trivial `norm_num`)

### 2.1 `terminal_resolution_sub_keV` — CIRCULAR NUMERICS

**File**: `ch11-experimental-evidence/terminal-resolution.lean:60–108`

```lean
def protonPrediction : MassPrediction where
  name := "proton"
  predicted := 938.272       -- ← hardcoded
  codata := 938.272          -- ← identical to predicted
  tolerance := 0.001
  tol_nonneg := by norm_num
  agreement := by norm_num   -- ← proves |938.272 - 938.272| ≤ 0.001
```

Same pattern for neutron (939.565), deuteron (1875.613), binding energy
(2.224 vs 2.2245).

**Problem**: The QOU theory predicts mass values via the topological mass
formula + skein relation + q ≈ 1.1097. But the Lean file **hardcodes the
prediction as the CODATA value itself** (or near-identical). The `agreement`
proof is then `|x - x| ≤ ε` which is trivially `norm_num`.

**What should happen**: The `predicted` field should be **computed** from
`substrate_q`, `vol_figure_eight`, and the topological mass formula, then
shown to be within tolerance of CODATA.

**Narrative says** (.md): "All four rows match CODATA to sub-keV precision"
— this implies the match is a *derived result*, not a tautology.

**Severity**: **HIGH** — the terminal resolution is the paper's headline
result. The Lean doesn't derive it; it asserts it.

Note: The content/quantum-observable-universe/lean file `HadronicMass.lean` does attempt this
derivation but uses 3 axioms for the `Real.rpow` computations.

---

## 3. Structures-as-Theorems (No Proof Obligation)

Several blocks declared as `theorem` or `proposition` in the narrative
are formalized as Lean `structure`s — meaning the mathematical content
is assumed by whoever constructs the structure, not proved.

### 3.1 `RankOneGaugeData` for `thm:su2-emergence` — STRUCTURE, NOT THEOREM

**File**: `ch1-quantum-observable-universe/su2-emergence.lean:36–49`

```lean
structure RankOneGaugeData (k : Type*) [Field k] where
  qou : QuantumObservableUniverse.{u, v} k
  fund_dim_two : (SpinLabels.mk 1).cat_dim = 2
  volume_nondeg : ...
  adjoint_trivial : ...
```

**Narrative says** (.md): "G = Aut⊗(τ) ≅ SU(2)" — this is a theorem
that the axioms *force* SU(2). The Lean just packages the three conditions
as a structure. The actual Tannaka–Krein reconstruction (proving the gauge
group is SU(2) from these axioms) is absent.

**Severity**: **HIGH** — most depended-upon theorem on the critical path.
Everything downstream (spin-labels, torus, Reeb, substrate) depends on this.

---

### 3.2 `SpinDecomposition` for `prop:spin-labels` — STRUCTURE, NOT PROPOSITION

**File**: `ch1-quantum-observable-universe/spin-labels.lean:53–64`

The spin decomposition is declared as a structure with fields
`simpleObj`, `fundamentalObj`, `fundamental_is_half`, etc. The proposition
that SU(2) *forces* this decomposition is not proved — it's assumed by
the structure consumer.

**Severity**: **MEDIUM** — downstream deps inherit the assumption.

---

### 3.3 `MassIdentityC` for `cor:mass-identity-C` — STRUCTURE

**File**: `ch3-lifting-of-quantum-torsion/mass-identity-C.lean:27–36`

The archimedean corollary (nonabelian Stokes) is a structure with the
Stokes relation as a field.

**Severity**: **MEDIUM** — the Yekutieli integral is genuinely hard to
formalize, but the nonabelian Stokes theorem is a deep result that
should be explicitly axiomatized rather than silently assumed via
a structure field.

---

## 4. Narrative-Alignment Gaps

### 4.1 `CategoricalReeb` — MISSING 2 OF 3 PROPERTIES

**File**: `ch1-quantum-observable-universe/categorical-reeb.lean:32–44`

**Narrative lists 3 properties:**
1. Vertical generator: π_V ∘ d = ι_ξ dθ_A
2. Normalisation: θ_A(ξ) = id_𝟙
3. Kernel: Ω^k_H(A) = ker(ι_ξ)

**Lean has only:**
```lean
normalisation : xi ≫ theta = theta
```

Properties (1) and (3) are **absent**. Moreover, the normalisation
`xi ≫ theta = theta` says "applying ξ then θ equals θ" — this is
weaker than the narrative's "θ_A(ξ) = id_𝟙" (the evaluation should
yield the identity on 𝟙, not the form itself).

**Severity**: **HIGH** — the Reeb decomposition drives the substrate
parameter construction. Missing vertical generator means d_q is
not actually constrained.

---

### 4.2 `HigherForms` — MISSING d² = 0

**File**: `ch1-quantum-observable-universe/higher-forms.lean:36–47`

**Narrative says**: "d : Ωᵏ → Ωᵏ⁺¹ satisfying d² = 0"

**Lean has**: a differential `d : (k : ℕ) → formObj k ⟶ formObj (k + 1)`
but **no `d_squared_zero` field** asserting `d k ≫ d (k+1) = 0`.

**Severity**: **MEDIUM** — d² = 0 is the defining property of a
differential complex.

---

### 4.3 `HigherForms` — MISSING GRADED LEIBNIZ RULE

**Narrative says**: "graded exterior algebra with graded Leibniz"

**Lean has**: No Leibniz rule, no wedge product, no graded structure
beyond the indexed family of objects.

**Severity**: **MEDIUM** — the Leibniz rule connects forms to the algebra
structure.

---

### 4.4 `SubstrateParameter.ofReebDecomposition` — IGNORES INPUTS

**File**: `ch1-quantum-observable-universe/substrate-parameter-exists.lean:54–62`

```lean
noncomputable def SubstrateParameter.ofReebDecomposition
    {C : Type*} [CategoryTheory.Category C]
    [CategoryTheory.MonoidalCategory C]
    (M : Type*) (_wd : WeightDecomposition C)
    (_reeb : CategoricalReeb C)
    (q₀ : ℝ) (hq_pos : 0 < q₀) (hq_ge : 1 ≤ q₀)
    (hq_root : ∀ (k : ℕ), k ≥ 1 → q₀ ^ k ≠ 1) :
    SubstrateParameter M :=
  SubstrateParameter.ofConstant M q₀ hq_pos hq_ge hq_root
```

The `_wd` (weight decomposition) and `_reeb` (categorical Reeb) inputs
are **completely ignored** — the function just delegates to `ofConstant`.
The Reeb decomposition plays no role in the construction.

**Severity**: **HIGH** — the existence theorem claims to derive the
substrate parameter *from* the Reeb decomposition, but it ignores it.

---

### 4.5 `CategoricalReeb.ofWeightDecomposition` — TAKES PROOF AS INPUT

**File**: `ch1-quantum-observable-universe/categorical-reeb-exists.lean:39–49`

```lean
noncomputable def CategoricalReeb.ofWeightDecomposition
    ...
    (xi : wd.forms ⟶ wd.forms)
    (theta : wd.forms ⟶ (𝟙_ C))
    (norm : xi ≫ theta = theta) :
    CategoricalReeb C :=
  { A := wd.forms, xi := xi, theta := theta, normalisation := norm }
```

The "existence proof" takes ξ, θ, and the normalisation proof as
inputs and wraps them. It doesn't *construct* ξ from the weight
decomposition — it requires someone to hand it the answer.

**Severity**: **MEDIUM** — consistent with the structure-based approach
but doesn't prove existence from prior definitions.

---

### 4.6 `LocalSubstrateQ` — STRUCTURE, NOT DERIVED

**File**: `ch11-experimental-evidence/local-substrate-q.lean:36–49`

```lean
structure LocalSubstrateQ where
  vol_figure_eight : ℝ
  muon_electron_ratio : ℝ
  q : ℝ
  q_gt_one : 1 < q
  defining_eq : (1 - q⁻¹) ^ 2 = vol_figure_eight / muon_electron_ratio
  q_approx : |q - 1.1097| < 0.001
```

This declares the proposition as a structure whose fields include the
conclusion (`q_approx`). The companion `unique_q_solution` theorem does
prove uniqueness, and `codata_ratio_in_range` verifies the constants
are in range — these are genuine proofs. But the top-level proposition
doesn't derive `q_approx` from `defining_eq` + CODATA values.

**Severity**: **MEDIUM** — partial: uniqueness is proved, but the actual
numerical evaluation (solving for q) is left to the structure consumer.

---

### 4.7 `QuantumObservableUniverse` — MISSING ANOMALY-FREE CONDITION

**Narrative says** (.md title): "four observability conditions: non-degenerate
integration, no hidden symmetries, anomaly-free, volume constraint"

**Lean has**: 3 conditions (non-degeneracy via snake identities, adjoint
vanishing, volume constraint). The "anomaly-free" condition is absent.

**Severity**: **LOW** — may be considered absorbed into the Frobenius
non-degeneracy, but the narrative lists 4 conditions and the Lean has 3.

---

## 5. Needed Inputs Declared?

For each Lean file, does it actually import/reference the mathematical
dependencies listed in the `.ts` manifest's `uses` array?

| Block | `uses` in .ts | Lean imports/references | Missing |
|-------|---------------|------------------------|---------|
| `prop:local-substrate-q` | `def:substrate-parameter`, `rem:skein-mass-relation`, `rem:terminal-resolution`, `rem:photonic-hall` | Imports only `Mathlib.Data.Real.Basic`, `Mathlib.Analysis.SpecialFunctions.Pow.Real` | **All 4 deps unimported** — no reference to substrate-parameter, skein, terminal-resolution, or photonic-hall Lean files |
| `rem:skein-mass-relation` | `conj:topological-mass-formula`, `rem:skein-decomposition`, `def:substrate-parameter`, `def:quantum-planck-constant`, ... | Imports only Mathlib | **All content deps unimported** |
| `rem:terminal-resolution` | `rem:skein-mass-relation`, `def:mass-identity`, `thm:topological-mass`, `cor:mass-identity-C`, `conj:topological-mass-formula` | Imports only `Mathlib.Data.Real.Basic` | **All content deps unimported** |
| `thm:topological-mass` | `def:quantum-observable-universe`, `def:recursive-brane-tower`, `def:mass-identity`, `def:descent-involution`, `prop:descent-eigenspaces` | Imports `Mathlib.Algebra.Module.Basic`, `Mathlib.Analysis.Normed.Group.Basic` | **All content deps unimported** — defines own local `categoricalMass`, `MassDecomposition` |
| `def:mass-identity` | `def:quantum-observable-universe`, `def:frobenius-pairing`, `def:recursive-brane-tower` | Imports only Mathlib | **All content deps unimported** — defines own local `FrobeniusHopfData` (shadow!) |
| `prop:descent-eigenspaces` | `def:descent-involution`, `lem:descent` | Imports only Mathlib | **Content deps unimported** — defines own `IdempotentEndomorphism` |
| `def:descent-involution` | `prop:jet-prolongation`, `lem:descent` | Imports only Mathlib | **Content deps unimported** |
| `thm:su2-emergence` | `def:quantum-observable-universe` | Imports `QOU.Basic`, `QOU.Glossary` + Mathlib | **Partial** — uses `QuantumObservableUniverse` from QOU.Basic |
| `def:substrate-parameter` | `def:quantum-observable-universe`, `def:weight-decomposition`, `def:categorical-reeb` | Imports `QOU.Basic`, `QOU.Glossary` + Mathlib | **Partial** — uses `SubstrateParameter` standalone; doesn't import weight-decomposition or reeb |

**Pattern**: The Chapter 3 (torsion/descent/mass) and Chapter 11
(experimental) Lean files are **fully self-contained** — they define
local types (`MassDecomposition`, `IdempotentEndomorphism`,
`FrobeniusHopfData`, `MassPrediction`, etc.) rather than importing
the canonical definitions from Ch 1. This means:

1. There are **shadow types** — `QOU.FrobeniusHopfData` in
   `mass-identity.lean` is a different type from the canonical one
   in `quantum-universe.lean`.
2. The dependency chain in Lean is **disconnected** — the `.ts` manifests
   say block X uses block Y, but the Lean files don't import each other.
3. A change to a foundation definition (e.g., adding a field to
   `QuantumObservableUniverse`) would **not propagate** to downstream
   Lean files because they don't depend on it.

**Severity**: **HIGH** — the dependency graph in Lean does not match the
declared dependency graph in the content manifests.

---

## 6. Summary Table

| # | Issue | File(s) | Type | Severity |
|---|-------|---------|------|----------|
| 1 | `mass_decomposition_categorical` returns hypothesis | topological-mass.lean | Tautological proof | **HIGH** |
| 2 | `transient_localisation` conclusion = hypothesis | topological-mass.lean | Tautological proof | MEDIUM |
| 3 | Terminal resolution hardcodes predicted = CODATA | terminal-resolution.lean | Trivial norm_num | **HIGH** |
| 4 | `RankOneGaugeData` is a structure, not a theorem | su2-emergence.lean | Structure-as-theorem | **HIGH** |
| 5 | `CategoricalReeb` missing 2/3 properties | categorical-reeb.lean | Narrative gap | **HIGH** |
| 6 | `ofReebDecomposition` ignores Reeb/weight inputs | substrate-parameter-exists.lean | Unused inputs | **HIGH** |
| 7 | `HigherForms` missing d² = 0 | higher-forms.lean | Narrative gap | MEDIUM |
| 8 | Lean dependency graph disconnected from .ts manifests | All Ch 3, Ch 11 files | Missing imports | **HIGH** |
| 9 | Shadow types (duplicate `FrobeniusHopfData`, etc.) | mass-identity.lean et al. | Type duplication | **HIGH** |
| 10 | `SpinDecomposition` structure, not proposition | spin-labels.lean | Structure-as-prop | MEDIUM |
| 11 | `MassIdentityC` structure with Stokes as field | mass-identity-C.lean | Structure-as-cor | MEDIUM |
| 12 | `CategoricalReeb.ofWeightDecomposition` takes answer as input | categorical-reeb-exists.lean | Non-constructive | MEDIUM |
| 13 | `LocalSubstrateQ` structure, not derived | local-substrate-q.lean | Structure-as-prop | MEDIUM |
| 14 | `HigherForms` missing graded Leibniz | higher-forms.lean | Narrative gap | MEDIUM |
| 15 | `QuantumObservableUniverse` missing anomaly-free | quantum-observable-universe.lean | Narrative gap (minor) | LOW |

---

## 7. What IS Genuinely Proved

Not everything is a stub. These theorems contain real proof content:

| Theorem | File | What it proves |
|---------|------|----------------|
| `unique_q_solution` | local-substrate-q.lean:58–88 | Uniqueness of q > 1 solving (1 − q⁻¹)² = c, via explicit inverse construction + square root |
| `codata_ratio_in_range` | local-substrate-q.lean:93–98 | Vol(4₁)/m_μ/m_e ∈ (0,1) by `positivity` + `norm_num` |
| `hbar_q_pos_of_gt_one` | skein-mass-relation.lean:76–79 | ℏ_q > 0 when q > 1 |
| `predicted_ratio_pos` | skein-mass-relation.lean:83–87 | Predicted ratio is positive |
| `quantumPlanckConstant_nonneg` | quantum-planck-constant.lean:41–44 | ℏ_q ∈ [0,1) |
| `quantumPlanckConstant_lt_one` | quantum-planck-constant.lean:46–49 | Upper bound |
| `planck_classical_limit` | quantum-planck-constant.lean:52–56 | q = 1 ⟹ ℏ_q = 0 |
| `SubstrateParameter.planck_nonneg` | substrate-parameter.lean:79–84 | Non-negativity |
| `SubstrateParameter.field_ne_one` | substrate-parameter.lean:60–64 | q ≠ 1 from root-of-unity |
| `idempotent_direct_sum_decomposition` | descent-eigenspaces.lean:40–49 | im(τ) ⊔ ker(τ) = ⊤ — genuine algebraic proof |
| `idempotent_direct_sum_disjoint` | descent-eigenspaces.lean:53–62 | im(τ) ∩ ker(τ) = {0} |
| `ascent_image_is_descended` | descent-eigenspaces.lean:66–76 | Elements in im(ℓ) are fixed by τ |
| `no_preimage_is_transient` | descent-eigenspaces.lean:80–87 | ker(𝔡) ⊆ ker(τ) |
| `descended_trace_is_base_level` | topological-mass.lean:78–88 | tr_M(ℓ γ₀) = tr_N(γ₀) via retraction |
| `DescentInvolution.tau_idem` | descent-involution.lean:38–41 | τ² = τ from retraction |
| `jet_prolongation_preserves_observability` | jet-prolongation.lean:74–84 | Ad(J¹A) = 0 from Ad(A) = 0 |
| `FrobeniusPairing.symmetric_of_comm` | frobenius-pairing.lean:51–58 | Pairing symmetry from commutativity |
| `FrobeniusHopfData.hasNonDegeneratePairing` | frobenius-pairing.lean:85–94 | Snake identities from FH data |
| `SpinLabels.fundamental_dim` | spin-labels.lean:67 | dim(V_{1/2}) = 2 by `rfl` |

**Assessment**: The algebraic infrastructure (idempotent splitting,
retraction properties, Planck constant bounds, uniqueness of q) is
genuinely proved. The gaps are at the **theorem-level claims** — the
big results that connect the algebraic infrastructure to the physical
conclusions.

---

## 8. Recommendations

1. **Priority 1**: Connect the Lean dependency graph. Ch 3 and Ch 11
   files should import canonical types from Ch 1, not redefine shadows.
2. **Priority 2**: Replace tautological proofs in `topological-mass.lean`
   with actual derivations from `idempotent_direct_sum_decomposition`.
3. **Priority 3**: Add missing properties to `CategoricalReeb`
   (vertical generator, kernel characterisation).
4. **Priority 4**: Add `d_squared_zero` to `HigherForms`.
5. **Priority 5**: Make `terminal-resolution.lean` derive predictions
   from `substrate_q` rather than hardcoding them (or clearly mark
   as axiom with `-- Ref:` citing the content/quantum-observable-universe/lean derivation).
6. **Priority 6**: Convert key structure-as-theorem declarations
   (`RankOneGaugeData`) to actual theorems, or document the gap
   explicitly.
