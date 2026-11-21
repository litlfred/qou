---
# qou-kh7e
title: 'CIRCULAR: q*_S as a ''third determination of q0'' assumes (H1)'
status: completed
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-15T03:20:00Z
updated_at: 2026-11-21T12:40:00Z
parent: qou-q4oa
---

Found by the author, 2026-08-15, from one observation: **`c_3` is extracted from
experimental `Q_beta`.** Verified and quantified below.

## The claim, as published

`folio/quantum-observable-universe/mass-theory/rem-qstar-decay-sector-q0.md`
(a `remark` block in the paper), line 9:

> `q*` is a *third determination of `q_0`*, **independent of both mass-sector
> pins**.

and line 7 defines `q*` as

> the point where `c_3 = -Vol(4_1)` **exactly**

The same claim is restated in `ck-dk-canonical-registry.md` §3 ("a third,
decay-sector determination of q0 (mu-p-Q_beta three-way)") and — added
2026-08-15, in the same edit that corrected other errors — in **§9b**.

## Why it is circular

1. `c_3` is not a prediction. It is the **ladder inversion of the measured
   neutron Q-value**:

       c_3 = (Q_beta^exp / Q_N2(q) - 1) / u(q)^3

   (`qbeta_utils.c3_target_at`, whose docstring says so outright:
   *"`q_codata` (the experimental neutron beta-decay Q-value)"*).

2. `q*` is then **root-found** on `S(q) = c_3(q) + Vol(4_1)`
   (`qbeta_c3_qstar_k31_repin_probe.py:164`, `mp.findroot(S, (qp+qm)/2)`).

So `q*` is the modulus at which the ladder, fed experimental `Q_beta`, returns
exactly `-Vol(4_1)`. It is a determination of `q_0` **conditional on (H1)**
(`c_3^even = -Vol(4_1)`) — the very hypothesis under dispute. "Independent of
both mass-sector pins" is literally true (it uses neither `m_p` nor `m_mu`) and
is the wrong independence: it is not independent of the assumed offset.

## The quantitative kill: "80.3% muon-ward" IS Vol(4_1)'s window position

`sleak_offset_genericity_check.py` (already committed) shows the sign flip /
zero-between-anchors is produced by **every** constant in

    window = (-c_3(muon), -c_3(proton)) = (2.02020024, 2.06934258),  width 0.0491

7/7 unrelated constants tested (`2+1/36`, `63/31`, `e^0.708`, ...) reproduce it.
As `V` sweeps that window, `q*_V` sweeps the **entire** anchor interval. So the
paper's headline placement is just where `Vol(4_1)` sits in the window:

    (V - lo)/(hi - lo)  with V = Vol(4_1) = 2.029883213
      = 0.197039   from the muon end
      = 0.802961   from the proton end     <-- the paper's "~80.3% of the way
                                                from the proton anchor toward
                                                the muon anchor"

**80.2961 % computed vs "~80.3 %" published.** The figure is a reading of
`Vol(4_1)`'s position in the genericity window, i.e. a restatement of
`c_3(q_0) ~ -Vol(4_1)` to 0.48 %. It is not a decay-sector preference.

This also disarms the block's own argument that `q*` is "not the statistical
reconciliation of the mu-p tension" (precision-weighted mean sits 0.0007%
muon-ward, `q*` at 80.3%). True, and irrelevant: any in-window `V` gives some
other percentage, and none of them is a reconciliation either.

## What is NOT claimed here

Scope-(a). This does **not** show `Vol(4_1)` is absent from `c_3`, and does not
refute (H1) — see registry §9c, which already records (H1) as *motivated, not
derived*. What falls is the **use of `q*` as independent evidence**. The
underlying empirical fact survives and should be stated plainly instead:

    c_3 at the substrate anchor agrees with -Vol(4_1) to ~0.48%
    (0.07% at muon for the full keystone form -Vol(4_1) + u - (10/3)u^2,
     2.3% at proton -- and 2.3% is INSIDE the 2.4% genericity window)

Also untouched: the `1/u^3` smoothness result and `dq*/dQ_beta ~ -0.539` in the
same block (both correct, both about the extractor, neither depending on the
independence claim).

## Work

1. Re-scope the three assertion sites. The block is a **paper `remark`**, so
   this needs the content-block route (`.md` + `.ts` + `qa-sweep`), not just a
   registry edit:
   - `rem-qstar-decay-sector-q0.md` line 9 -- "third determination ...
     independent of both mass-sector pins" -> conditional on (H1), with the
     window figure.
   - `ck-dk-canonical-registry.md` §3 (the "mu-p-Q_beta three-way" phrase).
   - `ck-dk-canonical-registry.md` §9b (added 2026-08-15; my own).
2. Check whether anything downstream *consumes* `q*` as an independent q_0
   determination — that is the real blast radius. `BarOddLadderShape.lean`,
   `MassComputationChainRoadmap.lean` and `BraneTowerNStar.lean` mention the
   decay sector; `epistemic-status-of-calibrations.md` is the calibration
   authority and must not be inheriting a fourth pin from this.
3. Only then decide whether `q*` retains any standing. It may still be a useful
   *derived* quantity (it is exactly `-c_3^{-1}(Vol(4_1))`); what it cannot be
   is evidence for the offset that defines it.

## Discipline note

This is AGENTS.md §"Defined residual != derived decomposition" check 2 verbatim
— *"Is the offset forced, or merely in range? ... Compute that window and report
its width before claiming the feature is evidence for your particular C"* — and
that section already names this exact worked case. The window was computed, the
script is committed, and the conclusion still did not reach the block that
depends on it. Same shape as the 2026-08-09 correction not reaching the 1ppQ
ledger (`qou-tdp0`): a correction landing at one site and never propagating to
what restates it.

## Progress (PR #8452)
- Formalized in `folio/quantum-observable-universe/lean/QOU/Eightfold/PolarizationArgumentDiscardDecayWindowFractionSurprisalVolumeTermStepUnitDomainWallDilution.lean` (wired in `QOU.lean`).
- 80-dps numerical witness stamped in `computations/probes/qou_10v9_k6is_kh7e_lsvj_mumr_qjh8_probe.witness.json` (`Commit 1` = `ffa2d78ef5414a49bba12e0efccca6fbb72626d5`, `HEAD` = `078aa49b3db67c82ebbd4ebd6bd00b088ab2f9d9`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8452, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

## 2026-11-21 — paper-structure drain (https://claude.ai/code/session_01Qmmkt8R1YXFpKDbBiKB3hh)

Verified on main 2026-11-21: rem-qstar-decay-sector-q0.md:9 and epistemic-status-of-calibrations.md both now say q* is NOT an independent third determination and is conditional on c₃^even = −Vol(4₁). Closing.

Report: docs/audits/2026-11-21-paper-structure-bean-drain.md on branch claude/paper-structure-drain-2026-11-21.

Ruling check: the closed block quotes q*'s position in convention C and convention D side by side (rem-qstar l.16–24), so it does not rest on C alone. The circularity finding is about the extraction from measured Q_β; under the 2026-11-20 ruling Q_β is derived from γγ pair production, which removes the measured-Q_β input rather than reviving the third-determination claim. Closure stands.
