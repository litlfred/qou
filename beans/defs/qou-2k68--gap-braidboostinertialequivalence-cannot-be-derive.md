---
# qou-2k68
title: 'GAP: BraidBoostInertialEquivalence cannot be derived until inertial mass has an independent definition'
status: in-progress
type: task
priority: normal
created_at: 2026-11-25T00:38:04Z
updated_at: 2026-11-25T01:30:20Z
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


## 2026-11-25T01:13:10Z — owner chose options 1 + 2 ('try'); route 1 result
Probe computations/probes/braid_boost_inertial_clock/ (PR #9402, d32f457aaa5): exact computation in H2(q) and H3(q), 9 braids, pre-registered P1-P3, all hold. m_clock = 2 hbar_q^2 tr_reg is not the holonomy mass m. The ratio is braid-dependent (8 distinct rational functions), never identically 1, and changes sign; at proton q0 it runs -8.5e-4 .. 1.4e-2. m_clock(1) = 0 while m(1) = 2^c.
Scope (a) for this definition. Scope (b) for any hbar^2 x (finite trace) definition, invariant = order of vanishing at q = 1 (same obstruction as E0WeightAllWords).
STILL OPEN: option 2 (an explicit boost action on braids); a compensating 1/hbar^2 from the w -> v map. Next step: formalize-first scaffold for option 2.


## 2026-11-25T01:30:19Z — routes 2a + 2b (owner: '2a 2b'; 'light cone --> affine causality cone should be in corpus')
PR #9402, f32835580e3. All sorry-free, standard axioms.
- QOU/Core/AffineCausalityCone.lean, from def:contact-affine-chart (Z = u/w). The cone's null points +-c_q fix coneForm = c^2 w^2 - u^2 up to scale (quadratic_with_cone_roots). The boosts Z -> (Z+v)/(1+vZ/c^2) fix +-c (boost_fix_pos/neg), compose by velocity addition (boost_comp) and preserve |Z|<c (boost_preserves_cone).
- worldlineLagrangian = -m c_q sqrt(coneForm) (ReebHamiltonianChartBridgeReal), with einbein elimination (ReebWorldlineSignature.einbein_stationary_value). So the worldline form is DERIVED from the cone, not postulated.
- ReebWorldlineSignature: the trace route cannot supply the signature. tau((wX+uY)^2) >= 0 for symmetric X, Y and positive weights (convention-D y >= 0); only a skew Reeb contraction gives an indefinite form. The cone comes from projective geometry, not traces.
STILL OPEN (the conjecture proper): show a braid class's traced Lagrangian along a worldline is boost-covariant, with coefficient m = m(beta). Route 1 (m = 2 hbar^2 tr_reg) is excluded. The E_e / 70x split is unresolved.
