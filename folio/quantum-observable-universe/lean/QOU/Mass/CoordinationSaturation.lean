import Mathlib.Tactic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Real.Archimedean

/-!
# QOU.Mass.CoordinationSaturation — nuclear saturation forces bounded coordination

Formalizes the *qualitative* saturation argument already stated in the corpus
(`folio/quantum-observable-universe/mass-theory/bk-coordination-multiplicity.md`,
§ "for `n_α ≥ 5` the complete graph over-counts … saturates to a geometric
close-packing count"; `q-clt-jsj-mass-scaling.md`, `B/𝔪` "plateaus under nuclear
saturation"). This file is the machine-checked structural half; it claims no new
physics beyond hardening that argument.

## Setup

Write the extensive binding as `B(A) = ε · M(A)`, with `M(A)` the total
nucleon–nucleon bond count and `ε > 0` a per-bond energy. The observed fact is
**saturation**: the binding per nucleon `B(A)/A` approaches a finite plateau
(~8 MeV/nucleon empirically), it does not grow with `A`.

## Result — the structural dichotomy

* **complete-graph coordination** `M = C(A,2)` (every nucleon bonded to all `A−1`
  others — the `z = A−1` law of `CoordinationBinding.lean`) gives
  `B(A)/A = ε·(A−1)/2`, **unbounded**: no plateau, the cluster over-binds without
  limit (`complete_graph_no_saturation`). Saturation therefore **refutes** the
  complete graph for heavy `A`.
* **bounded-degree coordination** (each nucleon bonded to a fixed `k` neighbours;
  handshake ⇒ `k·A/2` bonds) gives `B(A)/A = ε·k/2`, **constant** in `A`
  (`bounded_degree_saturates`): saturation.

## Conclusion and scope

Nuclear saturation *forces* a bounded coordination number (the close-packing /
fcc picture, arc item 3a) and *excludes* the complete-graph `z = A−1` (arc item
1, refuted at ⁴He). That is the structural content proved here.

The close-packing input is IMPORTED Euclidean geometry, now held and cited (bean
`qou-ywbd`); a citation makes it citable, not derived, and the four objections of
`docs/audits/2026-09-05-max-contact-sub-affine-negative.md` §5 stand:

-- Ref: [bezdek-reid2013] Thm 1(i) — touching pairs in any packing of n unit balls in
   E³ number < 6n − 0.926·n^{2/3}: bulk 12·n/2 from the kissing number k = 12, minus a
   sub-affine surface deficit. This is the bounded-degree `k` of `perNucleonBounded`.
-- Ref: [hales-etal2010] — the Kepler theorem statement (fcc density is maximal); the
   paper proves no kissing- or contact-number bound, so it does not source `k = 12`.

The REMAINING open input — that the binding multiplier is the **mutual**
(coordination) linking count while the mass multiplier is the **self**-linking
weight `lw` — is the linking-vs-self-energy amplitude assignment (bean
`qou-brng`); it is **not** proved here and must not be read as proved.

Ground ring `ℝ` (§7c: archimedean — the statement is unboundedness of `B/A`).
No fit: `ε`, `k` are free positive parameters, nothing is tuned to data.

## Convergent frontier (2026-08-29/30 sibling landings)

This lemma uses a **single uniform per-bond energy `ε`** — which is exactly the
**order-independent** regime `L_pp = L_pn = L_nn` that
`QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff` proves is the
*only* arrangement-invariant one (a nucleus has no arrangement, so bond-type-
dependent scalars are a non-physical DOF, scope-(b) excluded at `q ≠ 1`, bean
`qou-m07y`). So the saturation dichotomy here holds precisely in the physical case.

Together these exclude *both* simple coordination ansätze — the **complete graph**
(here, by saturation) and the **linear chain** (there, by arrangement-dependence) —
and sit alongside `QOU.MassTheory.BodyOrderRecurrenceDepth` (body-order depth ≥ 3
forced) and `QOU.MassTheory.MayerThreeBodySign` (the 3-body cumulant sign is
threshold-forced, wrong against AME). The extensive term's admissible structure is
being pruned from several directions at once; this file contributes the saturation
constraint.

LaTeX label: `prop:coordination-saturation` (interprets `bk-coordination-multiplicity`).
-/

namespace QOU.Mass.CoordinationSaturation

/-- Per-nucleon binding under **complete-graph** coordination: `B/A = ε·C(A,2)/A`. -/
noncomputable def perNucleonComplete (ε : ℝ) (A : ℕ) : ℝ := ε * (A.choose 2 : ℝ) / A

/-- Closed form: for `A ≥ 1`, `perNucleonComplete ε A = ε·(A−1)/2`
    (because `C(A,2) = A(A−1)/2`). -/
theorem perNucleonComplete_eq (ε : ℝ) {A : ℕ} (hA : 1 ≤ A) :
    perNucleonComplete ε A = ε * ((A : ℝ) - 1) / 2 := by
  unfold perNucleonComplete
  have hA0 : (A : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  rw [Nat.cast_choose_two]
  field_simp

/-- **Complete-graph coordination cannot saturate.** For `ε > 0` the per-nucleon
    binding exceeds every bound `B` at large enough `A` — no finite `B/A` plateau
    exists. This is the structural reason the complete-graph `z = A−1` (bond count
    `C(A,2)`) is refuted for heavy `A`: it predicts unbounded per-nucleon binding.
    (Qualitative source: `bk-coordination-multiplicity.md`.) -/
theorem complete_graph_no_saturation (ε : ℝ) (hε : 0 < ε) (B : ℝ) :
    ∃ A : ℕ, B < perNucleonComplete ε A := by
  obtain ⟨A, hA⟩ := exists_nat_gt (2 * |B| / ε + 1)
  have hnn : 0 ≤ 2 * |B| / ε := by positivity
  have h1lt : (1 : ℝ) < (A : ℝ) := lt_of_le_of_lt (by linarith) hA
  have hA1 : 1 ≤ A := by exact_mod_cast le_of_lt h1lt
  refine ⟨A, ?_⟩
  rw [perNucleonComplete_eq ε hA1]
  -- A > 2|B|/ε + 1  ⇒  A − 1 > 2|B|/ε  ⇒  ε(A−1)/2 > |B| ≥ B
  have hstep : 2 * |B| / ε < (A : ℝ) - 1 := by linarith
  have : |B| < ε * ((A : ℝ) - 1) / 2 := by
    rw [div_lt_iff₀ hε] at hstep
    nlinarith [le_abs_self B, hstep]
  linarith [le_abs_self B]

/-- Per-nucleon binding under **bounded-degree-`k`** coordination (each nucleon
    bonded to a fixed `k` neighbours; handshake ⇒ `k·A/2` bonds):
    `B/A = ε·(k·A)/2 / A`. -/
noncomputable def perNucleonBounded (ε : ℝ) (k A : ℕ) : ℝ :=
  ε * ((k * A : ℕ) : ℝ) / 2 / A

/-- The bounded-degree per-nucleon binding is `ε·k/2`, independent of `A`
    (for `A ≥ 1`). The `A` cancels — this is genuine saturation, not a
    definitional constant. -/
theorem perNucleonBounded_eq (ε : ℝ) (k : ℕ) {A : ℕ} (hA : 1 ≤ A) :
    perNucleonBounded ε k A = ε * (k : ℝ) / 2 := by
  unfold perNucleonBounded
  have hA0 : (A : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  push_cast
  field_simp

/-- **Bounded-degree coordination saturates:** the per-nucleon binding is the
    same at every `A ≥ 1` — a finite `B/A` plateau, the observed behaviour. -/
theorem bounded_degree_saturates (ε : ℝ) (k : ℕ) {A A' : ℕ}
    (hA : 1 ≤ A) (hA' : 1 ≤ A') :
    perNucleonBounded ε k A = perNucleonBounded ε k A' := by
  rw [perNucleonBounded_eq ε k hA, perNucleonBounded_eq ε k hA']

end QOU.Mass.CoordinationSaturation
