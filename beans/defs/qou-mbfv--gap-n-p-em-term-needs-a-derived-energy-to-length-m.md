---
# qou-mbfv
title: 'GAP: n-p EM term needs a derived energy-to-length map'
status: in-progress
type: task
priority: normal
created_at: 2026-11-27T20:11:35Z
updated_at: 2026-11-27T22:24:11Z
parent: qou-myts
---

The n−p EM term needs a derived energy-to-length map. All representations are covered and give n−p = −1/3 (Coulomb and magnetic), and the one-scale ratio is off by 27–44 (#9654). Audit addendum on litlfred/qou#9654. Filed for the n−p thread, which cannot reach the beans store.



2026-11-27 (thread "Close the n−p EM length gap", PR #9717): two-scale class proved in Lean (NucleonSplitTwoScale: ħc cancels; Casimir route gives EM² = 2f²α²Q²·M·E₁/q; flavour/EM ratio depends on E₀/M, outside #9654's one-scale class). Probe on main's radius routes, nothing re-tuned: Casimir C mass-formula unit r = 1.345 fm, EM n−p = −0.186 MeV, flavour/|EM| = 4.71 (lit 1.95–3.22); trace unit r = 11.28 fm, ratio 39.5. Open: electron weight w_e picks the row; magnetic channel needs a strand mass; A=3 gap E₁ not derived. Scope (a).



2026-11-27 follow-up (PR #9727): in the derived log-chart unit (#9718) the flavour cell is 2 ln q·|c| = 0.289 MeV and is fixed (k=2 forced in convention D; unit fixed). The overall-scale gap reduces to the mass-formula chart's electron weight, which is still hand-placed (electron-weight thread, #9725 does not settle it). The mass-formula-chart split row (E0 unit) is already in the audit and must be labelled conditional on the hand-placed ℏ_q² unit. Blocked on that chart.



2026-11-27 (after #9733, electron-weight thread): the mass-formula chart's electron weight is now derived, w_e = 3 + 4q²(q²−1)/((q⁴+1)(q²+1)) = 3.2035 at q₀. In that chart the n−p flavour cell is 2/w_e m_e = 0.319 MeV (Lean np_cell_energy_reading), 4.05× short of 1.293. The log chart gave 0.289 MeV (4.5× short). So with both derived units the cell is ~0.3 MeV: the chart is NOT the lever. The ~4× shortfall is in the cell itself (k = 2, forced in convention D for one block). Caveat from #9733: at current q₀ the mass chart gives m_μ/m_e = 64.7 (q₀ was defined with the hand-placed weight); q₀' = 1.0595 reported for comparison only, not adopted, and deriving q₀ is forbidden. Still open; next lever must change the cell, not the unit.



2026-11-27T22:05Z correction (from the electron-weight thread, checked by #9767): on the mass chart the n−p cell is m_n − m_p = −2/w_e m_e = −0.319 MeV, because w_e > 0 (CAL-1). That is the opposite sign to the log chart's +0.289 MeV, with the same size. So the mass chart misses the sign as well as the size. My earlier note above, giving +0.319, is wrong on the sign.



2026-11-27T22:30Z PR #9777 (audit §8): q-NS (q² from the #9752 Haar budget) and combinatorial factors (f^(2,1) = 2, Molien sum = 1, #9747 writhe ratio ≤ 1) neither supply the cell's ~4× nor fix its sign. Common factors cancel in τ_p/τ_n. A factor on E keeps the sign, and the largest derived one is q₀² = 1.232. A factor on the ratio would need q∂log g < −2 to flip the sign. Scope (a). The open part is the scale E or a second nucleon element (route 2), plus the orientation question in #9767.



2026-11-27T22:35Z PR #9777 §9: reading the split in the nucleon's own chart gives L_p = +1.201 and w_p = +0.925, so m_n < m_p in both charts (−163 / −2029 MeV). Scope (a). Route 2 within γγ words is closed (scope b, NucleonFlavourTypedLetters / NucleonDownQuarkStrand). Remaining: interface word #7876, a derivation of E, and the #9767 orientation. A next-lever card is with Carl.



2026-11-27T22:25Z From the electron-weight thread: PR #9789 uses the framing-corrected mass (def:mass-identity), U_e = 3 − D[4]/[4] = 2.4846. The cell becomes +2/U_e m_e = +0.411 MeV with the neutron above the proton (right sign), 3.15× short of 1.293. This may resolve the #9767 orientation; the size gap stays at ~3×. Not wired.

## 2026-11-28 — Coulomb length reduces to cell radius c (PR #9866)
Unit CAL-3 λ̄_π, A^(1/3) derived (#9859); only c selected. Arms c=1 and c³=3/2 recorded, none adopted (owner card). Next lever: derived p-shell shape (A≥5) replacing the imported ball.

2026-11-28: owner ruling. c stays open with two labelled arms (c = 1, c³ = 3/2); neither is adopted. Recorded in owner-rulings.md (PR #9905).
