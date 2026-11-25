---
# qou-2k68
title: 'GAP: BraidBoostInertialEquivalence cannot be derived until inertial mass has an independent definition'
status: todo
type: task
created_at: 2026-11-25T00:38:04Z
updated_at: 2026-11-25T00:38:04Z
parent: qou-s028
---

Owner ask 2026-11-25: "derive BraidBoostInertialEquivalence" (QOU/Core/CategoricalHamiltonianLegendre.lean:501, from 1e8db432857). Related: qou-91w7 (E -> MeV map, owner call).

FINDING (measured from the Lean source; this is not a derivation):
1. The class takes `inertialMass` and `holonomyMass` as FREE functions `BraidClass -> R` and asserts that they are equal. The corpus nowhere defines inertial mass from dynamics, and no "boost of a braid" exists anywhere in folio/ or computations/. The only "boost" hits are the unrelated c3 meridian-boost audits of 2026-07-12 and 2026-07-25.
2. So the class is satisfiable for ANY holonomyMass by setting inertialMass := holonomyMass (`fun _ => rfl`), and braidRestEnergy_eq_holonomyMass_div_sq_of_boost_equiv then holds with no hypothesis left. The "conditional" theorem therefore amounts to the definition E := worldlineEnergy(m, v = 0), and prop:mass-energy stays a definition. That matches the 2026-11-15 owner ruling "energy is defined as m c_q^2".
3. The worldline Lagrangian -m c_q sqrt(c_q^2 - v^2) is postulated: it is not obtained from the categorical Lagrangian. That Lagrangian's traced Reeb-clock form is the polynomial a2 w^2 + a1 w + a0 (trace_scaled_reeb_eq_lagrangianClock), where w is a Reeb (time) rate and v is a horizontal velocity.

CANDIDATE ROUTE (untested): define inertial mass as the kinetic coefficient of the clock Lagrangian, 2 a2 = 2 hbar_q^2 tau(reeb >> reeb).
- Assume the Stokes hypothesis hStokes (reeb^2 is the mass endomorphism of the boundary word) and frobeniusForm = counit. Then reeb_holonomy_leftTrace_eq_functional_hol (CategoricalLagrangianTwoTermBridge.lean:193) gives tau(reeb^2) = the Frobenius functional of hol(w), i.e. the mass trace.
- That predicts m_in = 2 hbar_q^2 x (mass trace). This is not m(beta) of def:mass-identity unless the factor 2 hbar_q^2 and the framing factor are accounted for. It is a falsifiable test that has not been run.
- The route also needs a map from the clock rate w to the velocity v.

Status: OPEN. Needs an owner choice of definition for inertial mass (chat, 2026-11-25).
