---
# qou-89w7
title: 'Cite [morita2012b] at QOU/MathlibExt/QBorelKernel.lean — Thm 1/Cor 1: first-kind q-Borel–Laplace of a bilateral series yields a q-elliptic theta-quotient connection coefficient (qou-wgnx route (a) precedent)'
status: completed
type: task
priority: normal
tags:
    - paper-relevance-triage
    - qdiff-stokes
    - reorg-2026-10-04
created_at: 2026-09-07T08:36:12Z
updated_at: 2026-11-21T12:54:01Z
parent: qou-1qhv
---

Source: library/arxiv-1205.1453v2/1205.1453v2.pdf -> [morita2012b] (Morita, asymptotic formula of the divergent bilateral 1ψ0). Relevance: **supporting** — agent assessment, not yet adjudicated. Raised by local/paper-relevance-triage 2026-09-07. One bean for the document's actions.

The divergent bilateral series 1ψ0(a;−;q,x) is the formal solution (eq. 20) of the degenerate first-order equation ((1/q − ax)σ_q + x)u = 0 (eq. 19). Thm 1 (§3.2): its first-kind q-Borel–Laplace resummation in direction λ is (q;q)_∞/(q/a;q)_∞ · θ(aqλ)/θ(qλ) · θ(ax/λ)/θ(x/λ) · 1/(1/ax;q)_∞ off the q-spiral [−λ;q]; Cor 1: the connection coefficient C(x;q) is q-elliptic (invariant under x → qx and x → e^{2πi}x); Thm 2 (§4): q → 1 recovers the bilateral 1H0.

Why the corpus wants it: bean qou-wgnx records that theta-normalisation of C1's ∞-side solutions moved the Stokes data into "the choice of theta", and its route (a) is to redo the ∞ side WITHOUT theta-normalisation — q-Borel–Laplace resum in two directions λ ≠ μ and form S_q = U_q(λ)U_q(μ)⁻¹. Morita's Thm 1 is the simplest worked instance of exactly that λ-dependence living in a theta quotient, one order down and bilateral; morita2014 (already registered, bean qou-hnuw todo) is the order-2 Ramanujan-equation instance. The two together are the precedents to cite at the level-1 kernel file.

What to do: add `-- Ref: [morita2012b] https://arxiv.org/abs/1205.1453 (Thm 1, Cor 1)` to QBorelKernel.lean beside the morita2014 citation that qou-hnuw will add; optionally note it in the qou-wgnx body under route (a).

Not a compute-check: the corpus has no bilateral 1ψ0 evaluation to compare against (the θ-kernel bilateral Laplace in computations/probes/qbeta_g3_5two_qborel_theta_laplace.py is a different object, the Masbaum bar-side series).

## 2026-11-21 — cite-intake drain (wave 1)

Verdict: **done** (commit `88c4ab972`, branch `claude/cite-intake-drain-2026-11-21`, PR #8818, issue #8814). Morita §3.2 theorem + q-elliptic C(x;q) verified in held copy.

Superseded-premise check: the edited text was read against `docs/coordination/owner-rulings.md` (photon 1+φ₀σ₀+φ₁σ₁+φ₀₁σ₀σ₁⁻¹; electron σ₀σ₁σ₀ with Hopf closure; up quark an unknot strand; two-term Lagrangian trace; T(2,n_s) withdrawn; no virtual photons). None of these forms is asserted or relied on in the cited sentences.

Status stays in-progress until PR #8818 merges.

## 2026-11-21 — PR #8818 merged

The cite-intake work above landed on main. Status set to completed.
