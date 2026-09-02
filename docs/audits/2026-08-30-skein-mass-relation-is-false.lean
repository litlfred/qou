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

  ## 2026-08-31 — the subject was removed, so this became a guard

  `SkeinMassRelationHolds` and its projection are **gone** from
  `QOU/HadronicMass.lean`: the class carried a proton/neutron/deuteron
  instantiation of the skein relation that the `.md` never states, and the
  measurement below is what showed it false.  The refutation itself survived
  the repair — it is now `QOU.HadronicMass.skein_pnd_identity_false`, proved
  in that file over the same constants.

  The theorem below no longer re-proves it.  It **restates** the surviving
  result and discharges it by that name, so this file compiles exactly when
  the replacement is present with the right statement.  A refutation whose
  target has been removed should leave behind a regression guard, not a file
  that no longer elaborates.

  The `rintro`/`nlinarith` proof this file used to carry moved verbatim into
  `skein_pnd_identity_false`; nothing was lost by deleting it here.
-/
import QOU.HadronicMass

open QOU.HadronicMass QOU.MassDerivation in
/-- **Guard: the refutation survived the class's removal.**

`SkeinMassRelationHolds` asserted `q·m_p − q⁻¹·m_n = (√q − 1/√q)·m_d`, which
is false at the file's own constants — LHS `194.5164`, RHS `195.3202`, `0.41 %`
apart, against a `1e-3 MeV` sibling tolerance.  The class is gone; the
inequality is proved in the library file, and this restatement fails to
elaborate if that ever stops being true. -/
theorem skein_pnd_identity_false_guard :
    substrate_q * proton_mass_MeV - substrate_q⁻¹ * neutron_mass_MeV ≠
      (substrate_q ^ (1/2 : ℝ) - substrate_q ^ (-(1/2 : ℝ))) * deuteron_mass_MeV :=
  skein_pnd_identity_false
