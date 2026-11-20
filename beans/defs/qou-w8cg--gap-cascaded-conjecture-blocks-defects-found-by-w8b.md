---
# qou-w8cg
title: 'GAP: cascaded conjecture blocks (#8568) — defects found by W8b audit'
status: todo
type: task
priority: normal
created_at: 2026-11-20T18:30:00Z
updated_at: 2026-11-20T18:30:00Z
parent: qou-6qbv
---

Read-only audit (W8b, 2026-11-20) of the 9 blocks demoted by the #8568 cascade. Findings, none acted on except explicit-alpha-k-h3 (PR #8631):

- No §3b-cond conditional theorem is possible on the spectral chain yet: `SpectralSequenceH3Explicit` takes three arbitrary Props as parameters, so nothing derives from it. It needs content (an encoding of d1/d2/pages, owner deferred) first.
- Every edge in the 9 is citational except explicit-alpha-k-h3 (its sketch takes E∞ representatives from the spectral conj). The owner chose full cascade over dropping edges, so they stay.
- explicit-alpha-k-h3: values now derived as Markov traces (#8631). Open: σ1−σ2 is not central; 4 classes listed vs dim Z(H3) = 3.
- alpha-k-derivation-procedure: Lean proves generic unique solvability given invertibility; the invertibility of the generic-q character matrix is a hypothesis, needing a citation or proof. Its -proof.md pins q0 to the muon value (proton default).
- explicit-alpha-k-h4: hardcoded floats plus norm_num range checks on the same literals; the exact Q(q) table is not encoded (closable by a finite exact computation). Header still says convention C. Dangling lean.ref (library stub is empty).
- wedderburn-bratteli-recursion: BratteliEdge has no containment constraint and a free content field, so the predicate forces y ≡ 0; `axiom plancherel_completeness_axiom` has an unmeetable hypothesis (unused but undisclosed). Dangling lean.ref.
- joint-tower-sdp-confinement: `joint_tower_sdp_feasible` has its hypothesis equal to its conclusion; constraint predicates are placeholders. Dangling lean.ref.
- atom-knot-mass-derivation: near self-assuming projection; `MassIdentity` is "within 25 % of AME" (max miss 19.5 % at 40Ca) — a tolerance sized to its own miss.
- baryon-product-from-alt: the Lean proves a Vandermonde identity, not the .md's sign-isotype claim, which may be false (a plain product of three velocities is S3-symmetric). Lean over ℝ, .md says over R (§7c). Edge to atom-knot is citational.
- six-term / frobenius: stale `prop:`/`thm:` labels in docstrings; frobenius .lean links braids-and-knots/ but the block is in mass-theory/.
