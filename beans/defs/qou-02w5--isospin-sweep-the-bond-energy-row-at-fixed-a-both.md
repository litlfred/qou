---
# qou-02w5
title: 'Isospin sweep: the bond-energy row at fixed A, both colour arms, and two routes to the mirror splitting differing 11x'
status: completed
type: task
priority: normal
created_at: 2026-08-31T05:28:16Z
updated_at: 2026-08-31T05:29:17Z
---

## Measured 2026-08-31 — `computations/probes/isospin_sweep_bond_energy_probe.py` (8/8)

Closes the scope caveat #6336 and #6365 both carried: *"whether the pp bond
inside a MIXED nucleus behaves this way is not tested here."*

### The rows (blind arm = canonical)

    A=2   Z=2  2.128360946   Z=1  2.330026199   Z=0  2.435584784
    A=3   Z=3  3.932685215   Z=2  3.737937771   Z=1  3.719531467   Z=0  3.376754267
    A=4   Z=4  5.554756841   Z=3  5.032709171   Z=2  4.687594960
          Z=1  4.239298070   Z=0  3.722495004

Both pure endpoints reproduce the merged B_pp (#6336) and B_nn (#6365) totals.

**The monotone DIRECTION flips between A=2 and A=3.** At A=2 the energy rises as
Z falls (argmax Z=0); at A=3 and A=4 it falls (argmax Z=A). That is #6365's
nn/pp crossover, now resolved across the whole row rather than only at its ends.
No interior extremum on any row.

### The colour arm acts ONLY in the interior — structural, and it matters

Crossing census: **pure compositions carry ZERO `averaged_weighted` crossings;
every mixed composition carries exactly ONE.** So the blind and colour-weighted
arms are identical at both endpoints *by construction* — verified numerically
rather than short-circuited.

Consequence: reproducing the merged endpoint totals validates the machinery and
says **nothing** about whether the arm choice is right at the interior points,
which are the points the probe exists to measure. Both arms are therefore
reported. The gap is small — 1.4e-4 to 3.4e-4 MeV, ~1e-4 relative — so the arm
choice does not explain any of the row structure.

Canonical arm is BLIND, per `colour_weighting_across_mixed_nuclei_probe`
cross-checking it against the canonical Rust value (#6309 for D; T/3He/4He
there). Not re-established here. NOTE: a different knob from the
`bring_color_weighted` p/n convention of owner ruling R3, which governs
`closed_form_tau_M`. Same adjective, different object.

### Two routes to "the model's mirror splitting" differ 11x

    D_kappa(3) = (A-1)/2 * tanh(ln q0) * B_pp(3) = 0.204428272713 MeV   (#6336)
    D_chain(3) = B(3, Z=2) - B(3, Z=1)           = 0.018406303196 MeV   (here)
    ratio 11.106

NOT the same object and not required to agree — D_kappa isolates an EM-linking
FRACTION of the pp bond; D_chain is the full composition difference. Recorded
for SIZE, not as an inconsistency finding. The comparison appears nowhere in the
corpus.

Context: bean `adhb` records a THIRD route via the brane tower giving
`T - 3He ~ -737 MeV` against CODATA `+0.019`, already documented as pathological
(the archimedean Phi_q specialisation is not Markov-invariant). So this is a
known-hard quantity and an 11x gap is modest beside the documented failure.

### Scope (a)

Chains, not nuclei — no spatial arrangement, and
`QOU.MassTheory.ChainBondOrderDependence.orderIndependent_iff` already says a
chain bond sum is arrangement-invariant only when L_pp = L_pn = L_nn. No AME
comparison, no fit, nothing wired. Interior compositions have no committed twin
and are validated only through their own row's endpoints. A pn bond is NOT
isolated: `include_inter` toggles all A-1 bonds together.
