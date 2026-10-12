---
# qou-507c
title: 'NS follow-up: re-derive or re-scope the NS singularity chain after item 3 retraction'
status: in-progress
type: task
priority: high
created_at: 2026-10-12T20:08:02Z
updated_at: 2026-10-12T20:08:02Z
parent: qou-vo9t
---

Owner-directed (2026-10-12): NS follow-up after thm:qu-to-qou item 3 (jet-tower perpetual obstruction) was retracted and replaced by Kummer persistence (commit bc60f24b9).

Blocks: fluid-dynamics/ns-obstruction-tower, ns-obstruction-computation, ns-singularity-descartes(-proof), ns-kummer-specialisation(-consequence), and their consumers.

Task: re-derive or honestly re-scope every step that relied on kappa_n != 0 for all n in the jet tower. Decide whether the NS-singularity conclusion survives through the Kummer form (Step 1 already argues in Kummer terms) or must be retracted. Follow the AGENTS.md (a)/(b) scope rule and the no-fitting rule.

## 2026-10-12 — verdicts (branch ns-followup; audit docs/audits/2026-10-12-ns-chain-after-item3-retraction.md)

**Overall: the NS-singular conclusion does not survive in any form the chain supports.** None of "NS-singular", $\mathrm{Obs}_\partial(A)=0$, or "$\kappa_n|_\Sigma\ne0$ for all $n$" is established. Two are false as literally written: scope (b), because a 1-dimensional Σ has $H^2(\Sigma,\cdot)=0$.

- **Survives (i):** $\kappa_0=e(\xi)=-6$; $e(\xi)|_\Sigma=0$; $H^2_{\{p\}}(\mathcal S,\mathbb Z)\cong\mathbb Z$.
- **Survives via Kummer (ii):** $\chi \bmod n\in H^2(\mathcal S,\mu_n)\cong\mathbb Z/n$ is non-zero iff $n\nmid6$. It is reached as the connecting map from $[\xi]\in H^1(\mathcal S,\mathbb G_m)$. The previously stated group $H^2(\mathcal S,\mathbb G_m)/n$ is ZERO on a closed surface, so `ns-kummer-specialisation` was corrected. The same placement in `substrate-gm-torsion` and `q-bsd-classical-limit` received scope notes. This class is GLOBAL: its restriction to Σ is 0, and it carries no NS content.
- **Cannot be supported (iii):**
  - complementary subgroups (retracted);
  - $\delta_n\ne0$ (scope b: $\delta_n\in\mathrm{im}\,H^2(\mathcal O)=0$);
  - $\mathrm{res}_\Sigma$ criterion (scope b, degenerate: it would call every QOU NS-regular);
  - $e(\xi)|_p=-6\deg_p$ (scope b, wrong formula: the local class is the index of a chosen section; Poincaré–Hopf sums to −6);
  - forced Reeb zero on Σ (scope b as a topological claim, open as a dynamical one);
  - descartes Steps 3–4 (scope a: their premise is unestablished).
- **Owner decisions** (framed in audit §5):
  - kind of `thm:ns-singularity-descartes`; recommendation (judgement): restate as the topological facts, with no NS verdict;
  - two interpretive remarks plus `observability-independent-motivation`;
  - the `motivic-perpetual-obstruction` sketch (same zero-group error).
- Bean stays in-progress: the open items are owner decisions plus the open dynamical question.
