---
# qou-1gkf
title: 'qou-dw20 convergence (B): (2π/N)log S_{n*,k*} → 4·clausen(π/2) at saddle n*≈N/2,k*≈N/4 — Riemann-sum→integral, adapt FigureEightVolumeSaddle E5c to the shifted+doubled integrand 2log sin(π(k+j)/N)−log sin(πj/N) (uses landed integral_le_sum_log_sin/_falling). MULTI-SESSION.'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - close-candidate
created_at: 2026-08-02T08:33:15Z
updated_at: 2026-11-22T21:33:04Z
parent: qou-n4nr
---


## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-02 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## Round 83 Execution Note (2026-11-17T10:23:09Z)

- **Status**: `in-progress` (PR awaiting merge; no unilateral closure).
- **PR**: [`litlfred/qou#8301`](https://github.com/litlfred/qou/pull/8301) (`feat/qou-b9cj-1gkf-gz37-ips1-ized-m1nz`, HEAD `8def28bdd6676a091a84204c0314f39da9ee6d5c`).
- **Lean Module**: `folio/quantum-observable-universe/lean/QOU/QBeta/GaroufalidisZagierS3BlockAndFiveTwoDiscBrick.lean` (wired into `QOU.lean`, compiled with Lean 4.24.0, 0 findings across all 7 static Lean audits).
- **80-dps Probe & Witness**: `computations/probes/garoufalidis_zagier_s3_block_and_five_two_disc_brick_probe.py` & `computations/probes/garoufalidis-zagier-s3-block-and-five-two-disc-brick.witness.json` (`scriptCommitSha = d726ce17152d0bdd416fbd50d86ba08930c726e7`, `scriptHash = 1b13751c9d60`, `outputHash = 36c8353af8986ccd33f16fae6cef94ba4dab83e96f5a0e688d772b07b9d32e72`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8301, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-08-07: "chore(beans): qou-kvvu completed (catalanG bridge verified); qou-1gkf lower-envelope progress"). The work may be partly or fully done. Read the bean before you close it.

## 2026-11-22 — wave-2 drain (thread "Work the volume conjecture beans")

Re-scope, no status change. The analytic content is on `main` and unconditional: `WhiteheadSaddleClausen.whitehead_vc_innerSum_half` (inner sum at `⌊N/2⌋` → 4G). What this bean still literally asks is a port to the class `WhiteheadVolumeConjectureLimit`, which uses index `(N−1)/2`; for even `N` that is `N/2 − 1`, a different sequence, and the file itself calls it a placeholder link. Porting buys little: that class is about the inner sum, not `J_N(W)`. The mathematically live gap is the phased outer sum (`VdVWhiteheadLemma4`, epic `qou-u1b5`). Suggest: replace the placeholder index by `N/2` and instantiate the class from `whitehead_vc_innerSum_half` (a short Lean change), then close this bean; left for a Lean-capable pass because it edits a theorem statement.

## 2026-11-22 — applicability review (owner instruction, thread "Work the volume conjecture beans")

**Verdict: APPLIES.** Formal mathematics (volume conjecture, Lean hyperbolic/AJ infrastructure, Mathlib gaps). Checked its premises against owner-rulings.md on main: it uses none of the retired ones (σ₀σ₁ photon, trefoil electron, convention C, z = 1 Q_β base, census selection, absolute mass, muon pin A, substrate-q₀ derivation, virtual photons, SM quark charges). Today's rulings (strand colour states, b = −qX on colour singlets with flavour trace values unchanged, convention D on the baryon sector, photon kept with fixed constant 1) do not reach knot-complement geometry. Its batch-PR notes (Nov 16–18 Round PRs) are all still open and unmerged as of 2026-11-22.
