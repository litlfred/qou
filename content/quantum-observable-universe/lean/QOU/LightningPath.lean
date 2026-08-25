import QOU.QuantumObservableUniverse
import QOU.Torsion
import QOU.CODATAChain
import QOU.HadronicMass
import QOU.ArchimedeanUniverse
import QOU.MassDerivation

/-!
# Lightning Path — Terminal Observational Synthesis

A single concluding remark that depends on **all** key observational results
in the QOU formalization.  Its purpose is twofold:

1. **Dependency graph**: this declaration is the unique sink node.  Tracing
   its transitive imports backwards yields the "lightning path" — the minimal
   subgraph of the proof forest connecting categorical axioms to CODATA
   observables.

2. **Evidence summary**: the remark collects the five pillars of
   observational support proved elsewhere in the formalization:

   | Pillar | Source | Key declaration |
   |--------|--------|-----------------|
   | Gauge group emergence | VolumeForm | `SU2Emergence.det_one` |
   | Self-dual instantons | Instanton | `categorical_self_duality` |
   | Topological mass decomposition | TopologicalMass | `topological_mass_decomposition` |
   | CODATA end-to-end chain | CODATAChain | `end_to_end` |
   | Descartes terminality | ArchimedeanUniverse | `descartes_terminal` |

> **Canonical-accuracy note.** This synthesis node bundles the *proved*
> pillars, but the CODATA leg (`end_to_end`) rests on CODATA-pinned mass
> constants (`HadronicMass`) and the deprecated `Vol(K)/ℏ_q²` mass shape,
> **not** the canonical muon-anchored Hecke energy (`computations/canonical_mass.py`),
> and its binding row is a consistency identity rather than a prediction.
> Read pillars 3–4 below with those caveats — per-isotope binding is the
> still-open `Δ_λ` gate.  Canonical sources:
> `docs/canonical-mass-formula-guardrail.md`,
> `docs/canonical-derivation-cheat-sheet.md` §9.

> **Pillar 1 carries less than its heading (bean `qou-szd6`).**  Pillar 1 is
> stated below as "the volume constraint forces `Aut⊗(ω) ≅ SU(2)`".  The
> conjunct actually proved is `emg.ext_sq_action g = 𝟙 exteriorSquare`,
> discharged by projecting the `det_one` field of `QOU.SU2Emergence`
> (`VolumeForm.lean`).  That structure has three fields — an abstract
> `gaugeGroupType`, an action on `exteriorSquare`, and `det_one` — and
> `exteriorSquare` is an unconstrained parameter.  **It mentions neither
> `SU(2)` nor the rank of the fundamental object**, so what this synthesis
> node checks is that a group acts trivially on some object, not that the
> gauge group is `SU(2)`.  The two supporting lemmas
> (`SU2EmergenceVolumeDeterminant`, `SU2EmergenceDaggerUnitarity`) are
> single-field classes restating their own conclusions, with docstrings
> recording the witness as pending a categorical-determinant formalisation in
> Mathlib.
>
> This is a gap in the *formalisation*, not a claim that the theorem is
> wrong — `prf:su2-emergence` is a real argument, but it takes the rank as an
> input to both of its lemmas rather than deriving it.
> `QOU.BraidsAndKnots.VolumeConstraintForcesFibreTwo` re-sources that rank
> from the categorical volume constraint of `def:quantum-observable-universe`;
> see bean `qou-n1dj` for what remains open.

## How to use

```
lake exe graph QOU.LightningPath   -- renders the full dependency DAG
```

The resulting graph shows the critical path from `FrobeniusHopfData` through
`ArchimedeanSubstrateField`, `TopologicalMassDecomposition`, `ArchimedeanMassFormula`,
and `HadronicMass` to `terminal_resolution_hadronic_mass`.
-/


namespace QOU

open HadronicMass CODATAChain ArchimedeanUniverse Torsion

/-! ## Concluding Observational Synthesis -/

/-- **Remark (Lightning Path — Observational Evidence for QOU).**

    The Quantum Observable Universe framework, starting from three categorical
    axioms (Frobenius self-duality, adjoint vanishing, volume constraint),
    produces a chain of predictions that match experiment:

    1. **Gauge group**: the volume constraint forces `Aut⊗(ω) ≅ SU(2)`
       (Theorem `thm:su2-emergence`).

    2. **Self-dual instantons**: every Yang–Mills minimiser on the QOU is an
       instanton with `⋆_q F = F` (Proposition `categorical_self_duality`).

    3. **Topological mass**: a stable vortex's mass decomposes categorically
       as `m = baseline + Σᵢ exceptional` via the descent involution
       (Theorem `topological_mass_decomposition`).  This categorical
       decomposition is **not** the canonical absolute-mass form: per the
       owner ruling (2026-06-24) the absolute nucleon mass is the
       muon-anchored Hecke energy `m_p = 2·(m_μ·F_Bor − 6·m_e)` with
       `m_μ = m_e·Vol(4₁)/ℏ_q²` and `F_Bor = |tr_M(β_Bor)|·[3]_q!/q³`,
       routed through `computations/canonical_mass.py`.  The `Vol(K)/ℏ_q²`
       shape carried by `ArchimedeanMassFormula` is deprecated for absolute
       mass (read with `K = 𝓑₃` it gives `m_p ≈ 966` MeV, +2.96%; the λ_A
       linking weight is a fit).  See `docs/canonical-mass-formula-guardrail.md`.

    4. **CODATA agreement**: the substrate parameter `q ≈ 1.1097` is *derived*
       (not assumed) from `Vol(4₁)` and the muon/electron ratio, with
       `|q − 1.1097| < 0.001` proved by interval arithmetic — this is the one
       genuinely-derived observable on this leg.  The proton and neutron rows
       of `end_to_end` are **CODATA-pinned reference constants**
       (`proton_topological := proton_mass_MeV`; see the `HadronicMass`
       honesty note), so `row1/row2_matches_CODATA` are equalities-by-
       construction, not predictions.  The deuteron and binding rows are a
       mass-deficit **consistency identity** `m_p + m_n − B_exp ≈ m_D` with
       `B_exp = binding_energy_QOU` the *experimental* deficit rounded to
       4 s.f. — **not** an independent binding prediction.  Canonically the
       per-isotope binding `B(K) = m_e·Σ_λ y_λ χ^λ Δ_λ` is the **OPEN `Δ_λ`
       gate**: derived only to ≈ −9% on the deuteron and off 44–72% for
       A ≥ 3 (`docs/canonical-derivation-cheat-sheet.md` §9b).

    5. **Descartes terminality**: the Descartes universe with `χ = −6` is the
       unique rigid completion (`descartes_terminal`).

    This remark carries no new mathematical content — it exists solely as
    the terminal node of the dependency graph, enabling the "lightning path"
    visualization from axioms to observables.

    LaTeX: `\label{rem:lightning-path}` -/
theorem lightning_path_synthesis :
    -- Pillar 1: Gauge group (SU(2) emergence via det-one constraint).
    -- The volume-determinant constraint `det(g_V) = 1` is exactly the
    -- statement that every gauge element acts as the identity on the
    -- exterior square `Λ²V` — the genuine `SU2Emergence.det_one` field.
    (∀ {C : Type*} [CategoryTheory.Category C] [CategoryTheory.MonoidalCategory C]
        {exteriorSquare : C} (emg : SU2Emergence C exteriorSquare)
        (g : emg.gaugeGroupType),
        emg.ext_sq_action g = CategoryTheory.CategoryStruct.id exteriorSquare)
    -- Pillar 2: Self-dual instantons
    ∧ (∀ {C : Type*} [CategoryTheory.Category C] [CategoryTheory.MonoidalCategory C]
        (fh : FrobeniusHopfData C) (inst : CategoricalInstanton fh),
        inst.hodge.IsSelfDual inst.curvature)
    -- Pillar 3: Topological mass decomposition
    ∧ (∀ {M : Type*} (tmd : TopologicalMassDecomposition M),
        tmd.totalMass = tmd.baselineHolonomy +
          (Finset.univ.sum fun i => tmd.exceptionalContribution i))
    -- Pillar 4: CODATA end-to-end (all four hadronic rows match)
    ∧ (|proton_topological - proton_mass_MeV| < 1e-3 ∧
       |neutron_topological - neutron_mass_MeV| < 1e-3 ∧
       |deuteron_topological - deuteron_mass_MeV| < 1e-3 ∧
       |binding_energy_QOU - binding_energy_CODATA| < 0.001)
    -- Pillar 5: Descartes terminality
    ∧ (∀ (dc : ArchimedeanCondition) (tk : TannakaKreinRigidity),
        dc.eulerChar = -6 ∧ tk.iso_count = 1) :=
  ⟨fun emg g => emg.det_one g,
   fun _ inst => categorical_self_duality _ inst,
   fun tmd => topological_mass_decomposition tmd,
   terminal_resolution_hadronic_mass,
   fun dc tk => descartes_terminal dc tk⟩

end QOU
