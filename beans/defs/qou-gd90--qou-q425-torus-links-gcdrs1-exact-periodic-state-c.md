---
# qou-gd90
title: 'qou-q425 torus links gcd(r,s)>1: exact periodic-state correction to MiddleWeightTraces, then prove'
status: todo
type: task
priority: normal
created_at: 2026-10-12T18:13:10Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-59vq
---

Owner order: (1) gcd>1 torus links, (2) Schur–Weyl trace split under q not a root of unity, (3) W_{r,j}.


## 2026-10-12: torus links PROVED (branch claude/rosso-jones-torus-links-2026-10-12, PR #7737)
The torus-link formula holds for every gcd(r,s). Proof in QOU/Archimedean/RossoJonesTorusLink.lean, sorry-free; the only axioms are propext, Classical.choice and Quot.sound. Full details are in the 2026-10-12 append on qou-q425. Main declarations: T_gam_eq_sum, card_fixSet, T_gam_pow, rossoJones_torusLink, markov_rossoJones_torusLink. The probe computations/probes/rj_torus_link_periodic_probe.py runs 1350 exact checks and all pass.
Item (1) is done. Items (2), the Schur–Weyl trace split, and (3), the modules W_{r,j}, are still open.


## 2026-10-12 (later): items (2) and (3) PROVED, except the full-twist scalar (PR #7737, commit 4b3439b86d)
File: QOU/Archimedean/SchurWeylTrace.lean. Sorry-free; axioms are only propext, Classical.choice and Quot.sound. The hypothesis is QIntNonzero q r, i.e. [k]_q ≠ 0 for 1 ≤ k ≤ r. It covers q = 1 in characteristic 0.
- (2) trace_split: tr(X|V_m) = Σ_{j≤min(m,r−m)} tr(X|W_{r,j}), with W_{r,j} := ker E ∩ V_{r−j} (Wmod). It holds for every weight-preserving X with XE = EX.
  - Fm is the lowering operator. Em_Fm_comm and Dg_eq show [E,F] = diag([2·ones − r]).
  - qZ is the signed q-integer, with qZ_mul and sum_qZ.
  - Epow_inj: E^k is injective on V_m when 2m+k ≤ r.
  - Em_transpose: E^T(q) = cmp·E(q⁻¹)·cmp. With a rank argument this gives El_surj on the upper half.
  - trace_eq_trace_ker_add: trace across an intertwining surjection.
- (3) Proved: WP_gam and gam_comm_Em; gamW (γ^p on W_{r,j}); T_gam_pow_split; trace_W_gam_pow_split, which says tr(Wγ^p) = Σ_{2j≤r}(Σ_{m=j}^{r−j} q^{2m}) tr(γ^p|W_{r,j}).
- Probe computations/probes/rj_schur_weyl_trace_split_probe.py: 22504/22504 exact checks pass.
- STILL OPEN: the full twist γ^r acts on W_{r,j} by a scalar. The probe finds the scalar q^{r(r−1) − 2j(r−j+1)} for r ≤ 6. The proof needs the ribbon element (Δ² as a function of the quantum Casimir via Jucys–Murphy elements) or irreducibility of W_{r,j} under B_r. Neither is formalised.


## 2026-10-12 (later still): full-twist scalar PROVED (PR #7737, commit d4678e2306)
- SchurWeylTrace.lean §10–11, sorry-free; axioms are only propext, Classical.choice and Quot.sound. The hypothesis is QIntNonzero q r.
- gamW_fullTwist: γ^{rt} acts on W_{r,j} (for 2j ≤ r) as (twistScalar)^t, where twistScalar = q^{r(r−1)−2j(r−j+1)}.
  - Route: the telescoping γ^r = ρ^r + E K_r, with ρ^r the scalar s_j on V_j.
  - Then w = E^{r−2j} v, and γ^r w − s_j w = E^{r−2j+1} y. This vector is killed by E, so Epow_inj gives y = 0.
  - No ribbon element and no irreducibility were needed.
- finrank_Wmod (char 0): dim W_{r,j} = C(r,j) − C(r,j−1).
- trace_W_fullTwist and markov_fullTwist: per-module Rosso–Jones for the full twists.
- The probe's exact checks now also compare the scalar with the Lean twistScalar and the dims with the binomial formula: 22624/22624 pass.
- Not done: per-module Rosso–Jones for general s, not a multiple of r. That needs the action of γ (not only γ^r) on W_{r,j}, e.g. its eigenvalues. The torus-link formula itself is already proved in RossoJonesTorusLink.


## 2026-10-12: per-module trace of γ^p for EVERY p, PROVED (PR #7737, commit 61b4fc2a10)
SchurWeylTrace §12, sorry-free.
- trace_gamW (2j ≤ r): tr(γ^p|W_{r,0}) = q^{np}. For j ≥ 1, tr(γ^p|W_{r,j}) = rhoTr q n p j − rho'Tr q n p (j−1), where rhoTr and rho'Tr are the periodic-state closed forms. Proof: invert the triangular system T_gam_pow_split at m = j and m = j−1, then apply T_gam_succ.
- trace_W_gam_pow_explicit and markov_gam_pow_explicit: the per-module Rosso–Jones formula for every torus link T(r,p).
- Probe check (f) added: 22932/22932 exact checks pass.

## Parented 2026-11-15 (owner-approved bean triage)

Parent `qou-xhci` → `qou-59vq`. The old parent was missing or absent, so the bean had no epic; this attaches it to the subtree its subject belongs to. No other field changed.

## Claim reset 2026-11-15

Was in-progress with no bean update since October 2026. Reset to todo by the owner-approved bean triage (same rule as the 2026-10-04 reset). Nothing in the work was judged. Re-claim it if you pick it up.

- Round 74 (`lane-e667`): Formalized `qou-gd90`, `qou-gzsp`, `qou-h56b`, `qou-hah4`, `qou-luq7` in `QOU.Foundations.PeriodicStateTriangularInversionWeightSpaceEquivarianceBlockScalingWeightedDecomposition` with 80-dps `mpmath` 2-commit witness stamp (`90a852e5501c98f68c32c2d227ae5dc2719d5bb6` -> `ae44845094878bbd65a4bf4b8065339b39d10e57`, `scriptHash=0a79a20314ed167467fce31136d40aeaf330204cb85b728199138a30d69455e2`) in PR `litlfred/qou#8399` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8399, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-10-12: "qou-gd90/qou-q425: bean appends — full-twist scalar proved"). The work may be partly or fully done. Read the bean before you close it.
