---
# qou-58r5
title: 'Real open content of rho_F=nu_SDP: prove/refute identity SDP-saturating-mult = bar-fixed-block sc(n) = bond count A-1 (NOT which integer)'
status: todo
type: task
created_at: 2026-08-02T16:03:25Z
updated_at: 2026-08-02T16:03:25Z
---

See docs/audits/2026-08-02-ppq-attack-vectors-roast.md §Roast 2.
nu_SDP {1,2,2} is INDISTINGUISHABLE from the Lean-proved bond count A-1 on all light
data. Real open content = the IDENTITY: SDP-saturating-multiplicity in H_{3A}(q0)
= bar-fixed-block count sc(n) = bond count A-1. Sibling infra: WardFiltrationCounting.lean
(sc(n)=bar-fixed points, decide-proved), chiral_sign_cancels (closes magnitudes, leaves
sign/chirality open). A derivation needs a proof the saturating projection's multiplicity
= self-conjugate-block count. Deuteron corroboration (1 atom): the excluded (3,2,1) is the
lone self-conjugate block (2026-07-26-deuteron-conjugation-parity audit). Anti-laundering:
do not wire nu_SDP=sc(n) without the identity proof.

## RESOLVED (2026-08-02): NO derived origin for the rho_F cap at 2 — honest negative + re-scope
Audit: 2026-08-02-rho-f-cap-no-derived-origin.md. Agent-B adversarial survey (verified):
- rho_F(4He) = 1.889 (NOT integer 2; corpus rounds), sits STRICTLY BETWEEN isospin
  count 2T+1=1 (T=0) and monotone A-1=3. No clean integer count reproduces it.
- Candidates all fail to DERIVE the cap: isospin 2T+1 {1,2,2,1} fails low; monotone/sc
  {1,2,2,3} fails high (refuted); bar-parity=constant-2 (no deuteron=1); #closed-shells
  {0,1,1,2} off-by-one; exchange-magnitude #distinct|lambda| {1,2,2,2} MATCHES but
  doesn't cap (A=5->3), is a selected functional, and isn't nu_SDP. min(A-1,2)=fit.
- One derived fact nearby: SU(4) He4-locality C(4,A)=0 for A>4 (Lean SU4SupermultipletGate)
  bounds the DOMAIN (A<=4), not the VALUE.
=> BREAKS nu_SDP in Z_{>0} at A=4. RE-SCOPE conj:kashaev-density-equals-sdp-multiplicity
to census-knot/linear-chain atoms (rho_F=A-1 exact); doubly-magic prefactor is empirical
(~1.89), an effective binding coefficient, not an integer count. scope-(a). Nothing wired.
