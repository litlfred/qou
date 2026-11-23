# Axiom-field triage: the 80 most-consumed "uninhabited" carriers (2026-11-20)

**This is a reading-only triage. Every verdict is a judgement made by reading the
declaration and its docstring; nothing was compiled, and no trivial inhabitant below
has been typechecked.** Per-carrier data:
[`2026-11-20-axiom-field-triage-top80.json`](2026-11-20-axiom-field-triage-top80.json).

## Input

```sh
python3 computations/audits/lean_axiom_field_and_mathlib_gap_audit.py --json /tmp/af.json --top 0
```

The run reported 1040 carriers with `status != "inhabited"`. This triage covers the
first 80 by `consumers`, descending (range 354 to 6).

## Verdicts

| verdict | count | meaning |
|---|---:|---|
| `PARAM_BUNDLE` | 49 | parameters with satisfiable side conditions, or a definitional structure / Prop predicate. Not a gap. |
| `VACUOUS` | 21 | can be inhabited without proving the advertised claim |
| `HONEST_HYPOTHESIS` | 4 | a concrete literature theorem the corpus does not prove, honestly marked |
| `DUPLICATE` | 3 | restates another carrier |
| `UNCLEAR` | 3 | not decidable in a short read |

**Reading the headline.** "Uninhabited" in the scanner's sense mostly means "no
`instance` found". For 49 of these 80 that is expected: they are definitions,
parameter records or predicates, and nothing is assumed by leaving them without an
instance. Only 4 are honest open hypotheses. **21 are VACUOUS. They are where the
scanner's signal really matters**: each looks like a stated hypothesis or theorem,
but its fields can be met by chosen data.

### HONEST_HYPOTHESIS (4)

`QOU.QBeta.StateIntegral.Recursion` (Fantini–Wheeler eq. 14),
`QOU.Mass.GammaGammaH6Interface.InterfaceBranching` (Hoefsmit branching on
⟨σ₂,σ₃⟩), `QOU.MathlibExt.FrechetShohat.CarlemanDeterminacyStieltjes` (Carleman,
Mathlib gap), `QOU.Archimedean.FiveTwoOhtsukiBridge.OhtsukiAsymptotic` (Ohtsuki
Thm 1.1, d = 0).

### VACUOUS (21), with inhabitant sketches

| consumers | carrier | trivial inhabitant |
|---:|---|---|
| 26 | `QOU.AppendixSurreals.SurrealField` | ℝ* with the two-valued `flatBirthday`; **already built** as `surrealFieldHyperreal` |
| 15 | `QOU.AppendixSurreals.QCollatz` | Skein = ℤ, qgen = 1 (classical Collatz map), attractor = 1, `pos := fun _ => False` |
| 14 | `QOU.Torsion.ArchimedeanMassFormula` | q = 2, knotVolume = baselineHolonomy = 1, one blow-up contributing 3, totalMass = 4 |
| 13 | `QOU.Kashaev.VolumeConjecture` | `hypVolume = kashaevLimit := fun _ => 0` |
| 12 | `QOU.AlgebraicSubstrate.QouObstructionReductionContext` | `hhCohDim = hhHomDim := fun _ => 1`, χ = κ₀ = 0 |
| 10 | `QOU.UnitalGroebner.IsUnital` | both fields are `True`: `⟨fun _ _ => trivial, fun _ _ => trivial⟩` |
| 9 | `QOU.InstantonConnection` | curvature 0, Hodge star `id`, energy 0 |
| 8 | `QOU.CosimplicialCrossedGroupoid` | shift `.level` by ±1; **already built** by `cosimplicial_crossed_groupoid_exists` |
| 8 | `QOU.Torsion.VacuumState` | `state := dla.limitState`; **already built** by `vacuum_state_exists` |
| 7 | `QOU.BraidKnot.IsMarkovTrace` | `mT n w := z ^ w.length` (the docstring itself says no real trace satisfies it) |
| 7 | `QOU.FluidDynamics.DiscreteVortexSpectrumContext` | Prop field `:= True`, define λ/E_level/ΔE by the formulas, q = 2 |
| 7 | `QOU.LRFusion.DoubleMagicConjecture` | Z = N = 2, `Partition := fun _ => Unit`, `lr := fun _ _ _ => 1` |
| 7 | `QOU.MathlibExt.HyperbolicVolumeBridge` | `vol := 0`, `Realises T _ := T.volume = 0`, empty triangulation |
| 7 | `QOU.NonSelfIntersection` | `separation := fun _ _ => hbarQ cme.q` (barrier antecedent false) |
| 6 | `QOU.BraidKnot.HasFiniteLPDuality` | an `lp` record with `primal_obj = dual_obj = 0`, `tight := (· ∈ ∅)` |
| 6 | `QOU.BraidKnot.MassCoefficientShadowPrice` | all functions 0, `uStar := C * S` |
| 6 | `QOU.BraidsAndKnots.TypeBFoldingCpt` | `foldAct := id`, `stable := True`, `anti := False` |
| 6 | `QOU.Interactions.TrefoilCanonicalMassUnit.TrefoilElectronMassConj` | solve for the free `m_e_cat` (the docstring calls this a "cheat that remains available") |
| 6 | `QOU.QuantumObservableUniverse.ObservationEnergyContext` | S = 0, `E_classical x := (x-1)^2`, witnesses q_inc = 2, q_dec = 0 |
| 6 | `QOU.ShellNeutrality.SaturatedShellConjecture` | n = 2, `Endo := Unit` |
| 6 | `QOU.Torsion.TopologicalMassDecomposition` | zero blow-ups, totalMass = baseline = 0, τ = id |

Three patterns account for nearly all of them:

1. **The target object is a field.** The claim is stated about `vol`, `hypVolume`,
   `pos`, `lr`, `Endo` or `m_e_cat`, and the instance gets to choose that field
   (VolumeConjecture, HyperbolicVolumeBridge, QCollatz, DoubleMagic, SaturatedShell,
   TrefoilElectron).
2. **Hypothesis and conclusion relate free reals.** For example
   `baselineHolonomy = knotVolume`, or `uStar = C * S` with all of them free.
3. **An invariant is encoded as a degenerate equation.** Invariance is written as
   constancy, a cosimplicial identity is checked only on `.level`, or a field is just
   `True`.

### DUPLICATE (3)

`QOU.BraidKnot.OperatorSelectionLP` → `…ConfinementNFPartial.OperatorSelectionLP`;
`QOU.LiftingDescent.DirectLimitAlgebra` → `QOU.DirectLimitAlgebra`;
`QOU.LiftingDescent.CosimplicialCrossedGroupoid` → `QOU.CosimplicialCrossedGroupoid`.

### UNCLEAR (3)

- `QOU.Torsion.DirectLimitAlgebra` and `QOU.Torsion.CosimplicialCrossedGroupoid`.
  Their Prop fields are degenerate: state constancy, and Peiffer reduces to ∂ = 1
  over a commutative R. But an inhabitant also needs a `Torsion.RecursiveBraneTower`,
  and that was not checked.
- `QOU.BraidKnot.ConfinementNFPartial.HasFiniteLPDuality`. Its fields equate
  `opaque` constants that have no definition, so the class is neither provable nor
  about an actual LP.

## Scanner false positives (8)

These carriers are inhabited in the tree. The scanner matches `instance` and misses
`def`- and `Nonempty`-theorem witnesses:

- `QOU.QuantumSu2`: `braids-and-knots/q-casimir-exists.lean:40` (`QCasimir.qsZero`)
- `QOU.AppendixSurreals.SurrealField`: `lean/QOU/AppendixSurreals/HyperrealLimitTransfer.lean:260`
- `QOU.CategoricalQExtDeriv`: `quantum-observable-universes/categorical-q-ext-deriv-exists.lean:37`
- `QOU.Mathlib.PagedSpectralSequence.PagedSS`: `lean/QOU/Mathlib/ConcentratedColumnCollapse.lean:162`
- `QOU.QuantumUniverse`: `lean/QOU/QuantumObservableUniverse/TrivialWitness.lean:101`
- `QOU.CosimplicialCrossedGroupoid`: `lifting-and-descent/cosimplicial-crossed-groupoid.lean:153`
- `QOU.LiftingDescent.CosimplicialCrossedGroupoid`: `lean/QOU/LiftingDescent/CosimplicialCrossedGroupoid.lean:96`
- `QOU.Torsion.VacuumState`: `lean/QOU/Torsion/BraneTower.lean:72`

(Paths are relative to `folio/quantum-observable-universe/`.) One apparent hit is
not a false positive: `badLP : OperatorSelectionLP` sits inside a doc comment in
`LpDualityHypothesisClass.lean`. `UGB.GrobnerShirshov.JetConfig` has **no** Prop
field at all, so its `prop_fields = 1` looks like a scanner miscount.

## Recommended next fixes (ranked by consumers; owner's call)

These are recommendations, not actions taken. Each changes Lean content, so each needs
owner sign-off under §ASK THE OWNER.

1. **Scanner** (all 1040). Also treat `def … : C` and `Nonempty (C …)` theorems as
   witnesses. Add a "fields are free data" heuristic: the claim names a field of the
   same structure.
2. **`SurrealField` (26).** Pin `birthday` to Conway's recursion, or rename the class
   to say it is "ordered field with a birthday-like grading". The independence
   witness in the tree already demonstrates the gap.
3. **`QCollatz` (15) and `VolumeConjecture` (13).** Make `pos` and `hypVolume` /
   `kashaevLimit` definitions rather than fields. Without that, the open conjectures
   these classes advertise are not what they assert.
4. **`ArchimedeanMassFormula` / `TopologicalMassDecomposition` (14 / 6) and
   `QouObstructionReductionContext` (12).** Tie `knotVolume` and `hhCohDim` /
   `hhHomDim` to named objects, so that the "hypotheses" are about something.
5. **`IsUnital` (10).** Replace the two `True` fields with the leading-coefficient
   unit conditions that the TODO describes.
