/-
  Bean `qou-z9ws` — `SkeinMassRelationHolds` is FALSE, not merely uninhabited.

  THE FINDING

  Hand-adjudicating the context classes behind the 90 self-assuming projections
  turned up one that is not in the same category as the rest.  Every other
  class measured so far is *vacuous* — inhabited by `Unit` and zero, so a `[C]`
  binder assumes nothing.  This one is **refutable**, and the refutation is
  below.

  `QOU.HadronicMass.SkeinMassRelationHolds` asserts, at the substrate `q` and
  the CODATA masses the same file defines:

      q · m_p − q⁻¹ · m_n = (√q − 1/√q) · m_d

  With `q = 1.1097`, `m_p = 938.27208943`, `m_n = 939.56542194`,
  `m_d = 1875.612945` (all `def`s in that file, all literals):

      LHS = 194.5164        RHS = 195.3202        0.41 % apart

  WHY REFUTABLE IS WORSE THAN VACUOUS, NOT BETTER

  A vacuous class makes its downstream `[C]`-conditional theorem *unconditional
  but empty*.  A FALSE class makes it **vacuously true**: `False → P` holds for
  every `P`, so the conditional proves nothing and would equally "prove" the
  negation.  Two declarations sit downstream of this one in the same file:

    - `skein_mass_relation_holds [hi : SkeinMassRelationHolds]` — the
      self-assuming projection that put the class in the ledger;
    - `skein_mass_relation_proton_neutron [SkeinMassRelationHolds] :
      SkeinMassRelation` — a `def` that CONSTRUCTS the Skein-mass-relation
      structure for the physical proton / neutron / deuteron out of the false
      hypothesis.

  The second is the one that matters.  The corpus carries a construction of the
  p/n/d Skein mass relation whose instance argument can never be supplied, so
  the object it builds is unreachable and anything reasoning from it is
  vacuous.  That is a different repair from the vacuous cases: it is not "the
  class asserts nothing", it is "the class asserts something the corpus's own
  constants contradict".

  WHAT THIS DOES NOT SAY.  It does not say the Skein mass relation is wrong as
  mathematics, nor that some nearby relation fails.  It says the equality as
  written, at the constants this file supplies, is false by 0.41 % — which is
  far outside anything the surrounding file treats as agreement (its own
  `row1_proton_matches_CODATA` uses a 1e-3 MeV tolerance).  Whether the right
  repair is an approximate form with a stated tolerance, different constants, or
  a corrected relation is an authorial question, not one this file answers.

  ON THE PROOF.  `norm_num` alone cannot close it: it normalises the decimal
  literals to rationals but leaves the two `rpow` terms `q ^ (1/2)` and
  `q ^ (-(1/2))` untouched, and the goal comes back with them intact.  The
  proof sets `s = q ^ (1/2)`, supplies `s * s = q` and `s > 0`, rewrites the
  negative exponent as `s⁻¹` via `Real.rpow_neg`, clears the inverse, and hands
  `nlinarith` a polynomial system.  Note the `norm_num at h` before the rewrite
  is load-bearing: without it the base is the *decimal* literal `1.1097` while
  the lemma is stated for `11097/10000`, and the rewrite finds no occurrence.

  VERIFY (lean-direct, Mathlib oleans restored, no `lake build` — a build
  against a restored cache with `traces=0` evicts it).  This one is slow, ~17
  minutes: `QOU.HadronicMass` has a large import cone, which is why it is in
  its own file rather than alongside the fast witnesses in
  [`2026-08-30-context-classes-hand-adjudicated.lean`](2026-08-30-context-classes-hand-adjudicated.lean).

      LEAN_PATH=<mathlib libs>:<QOU build lib> \
        lean docs/audits/2026-08-30-skein-mass-relation-is-false.lean

  Measured 2026-08-30: exit 0, 0 errors.
-/
import QOU.HadronicMass

open QOU.HadronicMass in
/-- **`SkeinMassRelationHolds` is false at the constants its own file defines.**
LHS 194.5164, RHS 195.3202 — 0.41 % apart. -/
theorem skeinMassRelationHolds_false : ¬ SkeinMassRelationHolds := by
  rintro ⟨h⟩
  rw [QOU.MassDerivation.substrate_q, proton_mass_MeV, neutron_mass_MeV,
      deuteron_mass_MeV] at h
  -- Normalise the decimal literals to rationals FIRST: the rewrite below is
  -- stated for `11097/10000` and will not match the literal `1.1097`.
  norm_num at h
  have hx : (0:ℝ) ≤ 11097/10000 := by norm_num
  have hxp : (0:ℝ) < 11097/10000 := by norm_num
  set s : ℝ := (11097/10000 : ℝ) ^ (1/2 : ℝ) with hsdef
  have hs0 : 0 < s := Real.rpow_pos_of_pos hxp _
  have hs2 : s * s = 11097/10000 := by
    rw [hsdef, ← Real.rpow_add hxp]; norm_num
  have hneg : (11097/10000 : ℝ) ^ (-(1/2) : ℝ) = s⁻¹ := by
    rw [hsdef, ← Real.rpow_neg hx]
  rw [hneg] at h
  have hsne : s ≠ 0 := ne_of_gt hs0
  field_simp at h
  nlinarith [hs2, hs0, h, sq_nonneg s, sq_nonneg (s - 1)]
