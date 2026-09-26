---
# qou-rav3
title: 'GUARD: inverting the plateau for a coordination number k is generic (73.7% of [2,12] reachable)'
status: completed
type: task
priority: normal
created_at: 2026-08-31T03:46:29Z
updated_at: 2026-09-05T07:29:46Z
---

## Measured, and closed as a guard (PR pending, branch `claude/brng-coordination-plausibility-2026-08-31`)

**The tempting move this forecloses.** `QOU.Mass.CoordinationSaturation.bounded_degree_saturates`
gives `B/A = ε·k/2`, and after #6338 the corpus has *derived* per-bond energies
`ε = E₀·log(1/f_bond)` trustworthy to 31 digits (ε_pp 2.0507, ε_pn 2.8332,
ε_nn 3.7978 MeV). Invert the observed plateau for `k` with ε_pn against the
Bethe–Weizsäcker volume coefficient and you get **11.118**, which is 7.3 % from
the fcc/hcp close-packing number **12**. Invert against the B/A peak instead and
you get **6.208**, 3.5 % from simple-cubic **6**. Either looks like the framework
predicting a lattice.

**It is not.** Inverting an empirical anchor for a parameter is a fit. The only
legitimate use is a plausibility check — is the implied `k` physically possible
at all? — and that check has teeth only if the plausible window is hard to hit.

**Measured (30 combinations: 6 reasonable ε choices × 5 empirical targets):**

    implied k, full range            4.62912 .. 15.4093
    inside the plausible window      27/30
    fraction of [2,12] reachable     73.7 %

So landing near **any** lattice coordination number — 12 fcc/hcp, 8 bcc, 6 simple
cubic — is a property of which ε and which target were chosen. The inversion does
not constrain `k`, and a "k ≈ 12, therefore close packing" reading is numerology.

The ε choices were not cherry-picked to inflate the range: the three pure bond
types, plus the bond-count-weighted means the complete graph and the chain
actually present at A=20 N=Z, plus the unweighted mean. The targets are the two
⁵⁶Fe/⁶²Ni peaks and a_V with its standard bracket.

**What this does NOT say.** `bounded_degree_saturates` is correct as stated and
nothing here argues against bounded coordination. Only the *inversion* is
uninformative.

**What would be informative:** a `k` derived from the substrate — from the braid
word's own geometry, or a packing argument inside the framework — and then
compared to the plateau. Derive-then-check. The above is check-then-derive, the
forbidden direction.

Probe: `computations/bounded_degree_coordination_genericity_probe.py`
(mpmath 50 dps, no float64, 50-digit proton pin, empirical values as exact
decimal strings). Shape follows `qbeta/sleak_offset_genericity_check.py`.


## 2026-09-05 (qou-kqdn) — this guard's METHOD applied to a k-independent quantity, and it bites there too. The surface-to-volume ratio a_S/a_V = c(k−k')/k from a boundary-deficit bond count has both ε and k cancel (QOU/Mass/CoordinationSurfaceDeficit.lean, surfaceToVolume_ratio), so this guard does not apply verbatim. Applying its methodology anyway: 3 fcc facets × 2 shell treatments reach 0.571..1.250 = 67.9 % of the plausible window [0.5,1.5], against this guard's 73.7 % for k. So the apparent fcc(100) match to the measured 0.961 is generic and was NOT claimed. The guard generalises beyond the inversion it was written for.
