---
# qou-k2xr
title: 'DECISIVE datum: resolve He-4 nu_SDP = 3 vs 2 — kills or saves the whole monotone {sc(n)=A-1} family'
status: todo
type: task
created_at: 2026-08-02T16:03:25Z
updated_at: 2026-08-02T16:03:25Z
---

See docs/audits/2026-08-02-ppq-attack-vectors-roast.md §Roast 2.
sc(3A)=A-1 for all A<=6 (verified); every monotone count predicts He-4 nu_SDP=3,
but the corpus assumes 2 (extrapolated, no census knot). Decisive:
- He-4=2  => sc(n)/A-1/distinct-odd-parts ALL refuted => nu_SDP is non-monotone/knot-intrinsic.
- He-4=3  => the monotone family survives; only the SDP-mult=sc(n) identity remains open.
Route: extend the joint-tower SDP knot solver to He-4 (needs the Frobenius re-pose,
bean qou-vd7j, to produce a real n=12 support), OR a knot-intrinsic argument for the
alpha-particle. Anti-fit: do NOT pick 2 to match the extrapolation.

## RESOLVED (2026-08-02): He-4 nu_SDP = 2, NOT 3 — monotone family REFUTED
Arbiter = binding data (probe he4_nu_sdp_binding_arbiter.py; audit
2026-08-02-he4-nu-sdp-decisive-2-not-3.md). Magic-A closure B=rho_F*m_e*A*8G with
rho_F=nu_SDP: rho_F=2 -> 29.96 MeV (+5.9%), rho_F=3 -> 44.93 MeV (+58.8%). Data-implied
rho_F=1.89 -> 2. Coulomb correction pushes strong-only rho_F to ~1.94 (closer to 2).
=> The sc(3A)=A-1 degeneracy (Roast 2) is a coincidence that BREAKS at the first
doubly-magic nucleus (A=4), not A=7. nu_SDP is NOT the bond count in disguise; it is
REGIME-DEPENDENT (A-1 for linear-chain census atoms, ~2 for the doubly-magic closed
shell). Sub-roast: rho_F=2 is corpus-rounded empirical (data says 1.89), not derived.
Orthogonal to sibling A=4 interface-magnitude work (that's the Delta_lambda MAGNITUDE
scalar m, not the nu_SDP multiplicity). Follow-on: bean qou-58r5 (regime-dependent
rho_F derivation) is now the sharpened open problem.
