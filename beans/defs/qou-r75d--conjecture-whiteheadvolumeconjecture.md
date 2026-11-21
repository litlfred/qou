---
# qou-r75d
title: 'Conjecture: WhiteheadVolumeConjecture'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-04T01:49:55Z
updated_at: 2026-11-21T12:10:00Z
parent: qou-n4nr
---

QOU/Knot/WhiteheadVolumeConjecture.lean: 1 sorry. Genuine volume conjecture — open.

## Round 79 Formalization Update (2026-11-17)

- **PR**: https://github.com/litlfred/qou/pull/8275 (`15c878c094e65c441587ef0bfb03d3ca8e8ed816`)
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/QuantumThreeStokesAndWhiteheadWindingBrick.lean` (wired into `folio/quantum-observable-universe/lean/QOU.lean`, verified with `lean -DautoImplicit=false -s 65536` exit 0, 0 `sorry`/`axiom`/`native_decide`, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/quantum_three_stokes_and_whitehead_winding_brick_probe.py` (`scriptCommitSha: b7b0957534826afd08d6dc085fb417146f29739e`) and `computations/probes/quantum-three-stokes-and-whitehead-winding-brick.witness.json` (`allPassed: true`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8275, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — premise check against docs/coordination/owner-rulings.md (main) + Stage 4 progress

Checked against today's owner-rulings ledger: **no superseded premise.** This bean and the
van der Veen Lemma 1 derivation (issue #7912) are pure U_q(sl₂) representation theory on
V_N⊗V_N; they use none of the photon form, virtual photons, γγ letters, T(2,n_s), Markov
convention C/D, the one- vs two-term Lagrangian trace, the electron word, c_2, χ₍₂,₁₎, or any
fitted/CODATA value. The quantum trace used is tr(Δ(K)·X), not the mass-sector Markov trace.

Stage 4 on branch claude/whitehead-jones-assembly-2026-11-21 (sorry-free, lean-direct exit 0):
- QuantumSl2ClaspDeltaF.lean: clasp commutes with Δ(F), scalar on each V_{2n+1}.
- QuantumSl2Decomposition.lean: F-strings are a basis (V⊗V = ⊕ V_{2n+1}); tr(Δ(K)X) = Σ c_j [2(m−j)+1].
- QuantumSl2TwistClaspTrace.lean: tr(Δ(K)·T^a X^c) = Σ_j [2n+1] t^{a n(n+1)} C(n)^c (b = d = 0).
Still open: belt on V⊗V (b ≥ 1 is needed for every Whitehead chain), mirror clasp, framing, 1/[N].
The volume conjecture itself stays OPEN; do not close this bean.

## 2026-11-21 — RT invariant: 1/[N] gap closed (draft #8943, stacked on #8941)

`QOU/Knot/WhiteheadBraidVolumeConjecture.lean` (sorry-free, lean-direct exit 0, standard axioms):
for every braid Markov-equivalent to σ₁⁻²σ₂σ₁⁻¹σ₂, [N]⁻¹·J_N(p)(σ) → whiteheadLinkKashaev N as
σ → e^{πi/(2N)} (punctured), and (2π/N) log‖·‖ of that limit → Vol(W). Remaining: Markov's
theorem (#8902), so the statement covers the Markov class, not yet every braid presentation of
the link. Polynomiality of the normalised invariant not proved (value at the root = the limit).
Bean stays open.
