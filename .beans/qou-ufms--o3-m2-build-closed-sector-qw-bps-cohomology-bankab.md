---
# qou-ufms
title: 'O3-M2: build closed-sector (Q,W) + BPS cohomology (bankable Route C math)'
status: completed
type: task
priority: high
created_at: 2026-08-14T22:05:39Z
updated_at: 2026-08-15T00:46:19Z
parent: qou-fiag
---

---
**2026-08-14 — O3-M2 landed.** Two corpus-map findings shaped it: (1) the explicit
closed-sector (Q,W) was never written (M1 content), so M2 also builds the reading;
(2) A_ω→S is two disconnected clusters (A_ω=3 DT count NOT wired downstream; the
S(muon)/S(proton) values come from S=c₃+Vol(4₁), a separate keystone).

M2 result on the certified eq-(98) datum (computations/probes/aomega_m2_bps_cohomology.py
EXIT 0; QOU/QBeta/AomegaM2BPSCohomology.lean lean-direct exit 0, route_c_m2 depends
only on [propext]): the closed-sector BPS spectrum is ABELIAN — every Borel ray
distinct ⇒ Davison-Meinhardt plethystic TRIVIAL ⇒ dim BPS = |Ω|, no superpotential
W, no motivic q-correction. Chirality {3,4}, bar (7,1), 4₁ dim s(1)=3, 5₂ extra
state s(1)+1 at a distinct ray. This is why A_ω and the tower 3,9,75,642,… are
integers, never Poincaré polynomials — reinforcing the O2 integrality obstruction.
Closed-sector category = this (Q,W) stays conjectural (M3, not claimed).


---
**2026-08-15 — framing corrected (owner challenge: "newly-categorified A_ω=3?").**
"Categorified" was an OVERCLAIM. M2 does NOT construct the (Q,W) (M1, unbuilt) or
compute a cohomology from a category, and does NOT derive A_ω (still imported,
conditional on conj:stokes-dt-bps-bridge). What M2 actually does: a CONDITIONAL
STRUCTURAL CHARACTERIZATION — taking the eq-(98) constants as DT invariants, the
Borel rays are distinct ⇒ Davison-Meinhardt plethystic trivial ⇒ the putative BPS
spectrum would be abelian (dim BPS=|Ω|, no motivic multiplicity). Corrected on main
via branch claude/aomega-m2-overclaim-fix-2026-08-15: the content block, the Lean
docstring title, the audit doc, and the coord doc all now say "characterized
(conditional)", not "categorified/computed".
