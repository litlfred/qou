import Mathlib.Data.Real.Basic

/-!
# QOU.HadronicMass.nucleon_borromean_topology

Canonical Lean for content block
[`lem:nucleon-borromean-topology`](../../../quantum-observable-universe/observations/nucleon-borromean-topology.md):
*Nucleon Borromean topology and Hopf-link binding*.

The `lean.ref` URI `qou:QOU.HadronicMass.nucleon_borromean_topology`
resolves to `nucleon_borromean_topology` below.

The lemma's content is that the Hopf link, being a torus link, has
hyperbolic volume `Vol(L_Hopf) = 0`, so the nucleon mass contribution
arises entirely from the Skein functional, not the volume term.  The
genuine geometric inputs are:

* `h_vol_hopf : Vol_Hopf = 0` — the Hopf link is a torus link (open
  manuscript fact for this abstract carrier);
* `h_mass_volume : mass_volume = Vol_Hopf * c` — the volume mass term
  is the volume scaled by the (Skein) coefficient `c`;
* `h_mass_total : mass_total = mass_volume + mass_skein` — the total
  mass is the sum of the two contributions.

From these the conclusion is **derived**: the volume mass vanishes
(`mass_volume = 0`) and the total reduces to the Skein mass
(`mass_total = mass_skein`).  The empirical inputs are isolated as
hypotheses (pattern A of the vacuity-fix playbook); the previous
encoding projected the whole conjunction from a self-asserting class
field — a vacuous self-assuming projection — and is removed.
-/

namespace QOU.HadronicMass

/-- **Nucleon Borromean topology / Hopf-link binding**
([`lem:nucleon-borromean-topology`]).

The proton and neutron are each a Borromean configuration (`6₂³`) of
three quark vortices, bound by Hopf links `L_Hopf` (color exchange).
The Hopf link is a torus link, so `Vol(L_Hopf) = 0` (`h_vol_hopf`); its
volume mass term `mass_volume = Vol_Hopf · c` then vanishes, and the
total mass `mass_total = mass_volume + mass_skein` collapses to the
Skein mass.  Both numerical clauses are *derived* from the geometric
hypotheses, not projected. -/
-- Ref: [leitner2026] quantum-observable-universe/observations/nucleon-borromean-topology.ts
theorem nucleon_borromean_topology
    {Vol_Hopf c mass_volume mass_skein mass_total : ℝ}
    (h_vol_hopf : Vol_Hopf = 0)
    (h_mass_volume : mass_volume = Vol_Hopf * c)
    (h_mass_total : mass_total = mass_volume + mass_skein) :
    Vol_Hopf = 0 ∧ mass_volume = 0 ∧ mass_total = mass_skein := by
  refine ⟨h_vol_hopf, ?_, ?_⟩
  · rw [h_mass_volume, h_vol_hopf, zero_mul]
  · rw [h_mass_total, h_mass_volume, h_vol_hopf, zero_mul, zero_add]

end QOU.HadronicMass
