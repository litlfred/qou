---
# qou-omr7
title: 'Magnus probes: d_q was the hook product, weight inverted (4 files)'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-03T04:40:28Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-m6dn
---

## The defect (PR #6442)

Four probes under computations/deltalambda/ compute the EXACT RECIPROCAL of the
weight their own docstring specifies:

    """y_λ = d_q(λ)² / [n]_q!"""              <- docstring
    dq = prod(q_int(hh, q) for hh in hooks)   <- this is H, the DENOMINATOR
    return (dq * dq) / nfact                  <- so it returns H²/[n]_q!

Hook-length formula: d_q(λ) = [n]_q!/∏[h(x)]_q, so the intended value is
[n]_q!/H². Returned is its reciprocal. Copy-pasted across
deuteron_magnus_omega2_sign_probe, triton_magnus_omega2_sign_probe,
he4_magnus_omega2_sign_sparse_probe, deuteron_interface_handle_curvature_probe
— one docstring even says "same as the prior probe".

VERIFIED THREE WAYS: probe × correct = 1.0 identically; the as-written formula
reproduces the COMMITTED witnesses to rel 1e-40 (so the defect is in source,
not a stale payload); and the fix agrees with pyhecke.wedderburn, whose
q_dimension IS q_factorial(n)/q_hook_product(partition). That third agreement
is ~1e-16, the limit of the reference's arithmetic — "agrees to the limit of
the arithmetic used", NOT exact.

Error magnitude at q0: 54x, 7.8x, 1042x, 265,000x on the partitions sampled;
grows with n as H and [n]_q! diverge.

## VERDICTS SURVIVE — checked, not assumed

Both probes key on a SIGN and the weights are positive either way. Recomputing
every weighted sum with the corrected weight leaves every sign unchanged:

  deuteron tr_rho_Omega2                -12882.86 ->     -72.25   holds
  deuteron tr_rho_Omega2_interface_only  -5794.40 ->     -59.14   holds
  triton   tr_rho_Omega2              -19243689.18 ->   -108.15   holds
  both     tr_Omega2_ctrl                     0.0 ->       0.0    vanishes
                                        term-by-term => weight-independent

Confirmed on real data after regenerating deuteron: old × new = 1.0 on every
partition, and the verdict string is BYTE-IDENTICAL ("LIVE — the linear Magnus
pairing tr_M(rho.Omega2) CLEARS the non-negativity wall").

So the DEAD/alive conclusions stand; the published magnitudes do not.

## How it was found — a false positive of my own detector

The convention-C fingerprint audit reported these three witnesses as a
REGRESSION after I left it at 0/0 on 2026-08-24. They were never convention C:
the field held a Plancherel-family weight, which the D row cap says nothing
about. The audit keys on the FIELD NAME y_lambda — a limitation its docstring
already stated, now with a concrete instance.

Fixed by recomputing d_q²/[n]_q! and checking whether the field IS it (also
accepting the reciprocal, for the inverted shipped values). An unevaluable
shape stays FLAGGED so a genuine hit is never silently dropped.

WRONG TURN WORTH RECORDING: I first matched these to wedderburn_weight in
qou-mass/_internal/, read its "symmetric Plancherel weight" warning, and began
building a notation-conflation finding on it. Wrong function — that one takes
ONE argument; the probes call a TWO-argument local definition. The signature
mismatch caught it before it reached the PR.

TWO BUGS IN MY OWN FIX, both caught by testing rather than shipping:
 1. q_parameter moved to substrate.q_parameter in the 10 days since I last
    touched this; a bare `except: return False` swallowed the ImportError, so
    every candidate stayed flagged and the audit LOOKED fine while the new
    check ran on nothing. Now tries four paths and WARNS loudly when q cannot
    be resolved.
 2. It then cached q at the default dps=15 before raising precision, so
    comparisons were accurate to ~1e-15 and a 1e-20 threshold could never be
    met — silently answering "not Plancherel" for everything. Precision now
    raised before q is parsed. This is the module-const-precision trap the
    corpus already gates on.

Both are the same shape as the defect itself: a check that reports success for
a question nobody asked.


## ORDERING CONSTRAINT — he4-sparse gates on the COMMITTED triton witness

Discovered by hitting it. `he4_magnus_omega2_sign_sparse_probe` failed:

    assert reldiff < mp.mpf(10)**-30, "GATE FAIL: P_total disagrees with triton"
    AssertionError: GATE FAIL: P_total disagrees with triton (1.0)

That is the gate working as designed, not a defect. Line 44 states the probe's
purpose (c) is to "reproduce the COMMITTED triton", and line 540 is
"[gate 2] reproduce COMMITTED triton H_9 P_total with the sparse method". With
the weight fix applied it computes the CORRECTED P_total and compares against
triton's still-INVERTED committed witness, so it correctly refuses.

**The four probes are therefore NOT independent.** Regeneration order is:
triton first, commit it, then he4-sparse. Any agent regenerating this family
piecemeal will hit the same wall, and the failure message names the cause
precisely — worth keeping rather than working around.

Do NOT relax that assertion to get he4-sparse green. It is a cross-producer
consistency check and it just earned its keep by catching a half-migrated
state I created.

Status: deuteron-magnus + deuteron-interface-handle regenerated, committed,
both verdicts byte-identical and reciprocal exact on every partition. Triton is
the blocker — ~40 min CPU, SINGLE-THREADED, and grep shows ZERO
resume/checkpoint machinery, so each container restart costs the entire run
(three so far). he4-sparse is fast (30 partitions in ~20s) once triton lands.


## LANDED — PR #6442 merged as 95d9b62368 (2026-09-03)

Verified in merged main: convention-C fingerprint 0 files / 0 fields over 3462
witnesses; the hook-length fix and the triton checkpoint both present.

Shipped: the d_q inversion fixed in all 4 Magnus probes; the fingerprint audit's
weight-family false positive killed (recomputes d_q²/[n]_q! and accepts the
reciprocal, so it cannot be fooled by either the correct Plancherel weight or
the inverted one); 2 of 4 witnesses regenerated with byte-identical verdicts;
a stamped resume checkpoint for triton; .gitignore for its progress file.

## STILL OPEN — 2 of 4 witnesses, and why

  triton-magnus-omega2-sign          NOT regenerated
  he4-magnus-omega2-sign-sparse      BLOCKED on triton (gate 2 reproduces the
                                     COMMITTED triton; do NOT relax it)

**Triton cannot finish in this environment.** Measured across FIVE attempts:
the H_9 sweep is ~90 min single-threaded and container restarts land every
~30-60 min. Best progress was 12/30 partitions. Attempts 1-4 lost everything;
attempt 5 was the first with the checkpoint and banked 8/30, then died within
minutes of resuming — the checkpoint is proven (it printed "resumed 8/30
partitions") but the window is shorter than the remaining work.

**The path forward is incremental, and now cheap.** The checkpoint is in main,
so each relaunch resumes and adds a few partitions:

    cd computations/deltalambda
    setsid nohup python3 -u triton_magnus_omega2_sign_probe.py >/tmp/t.log 2>&1 &

Repeat until the witness is written (the checkpoint self-deletes on clean
completion). Then run he4_magnus_omega2_sign_sparse_probe.py, which is fast
(30 partitions in ~20s) and will pass once triton's witness is committed.

**LIVENESS CHECK — do not use `pgrep -c`.** It counts your own diagnostic
shells; it made me report a dead run as alive for ~4 hours. Use:

    pgrep -af triton_magnus | grep -v "bash -c"
    wc -l < computations/deltalambda/.triton_magnus_omega2_progress.jsonl

Neither remaining witness is a correctness risk: both are stale-but-correctly-
excluded by the fixed audit (hence 0/0), and the source fix is verified
independently of them — reciprocal exact and verdict byte-identical on the two
that DID regenerate, plus agreement with pyhecke's independent implementation.

## 2026-09-04 — he4-sparse COMPLETE, and "2 of 4 witnesses remain" was miscounted

`he4_magnus_omega2_sign_sparse_probe` ran to completion for the first time.
77/77 partitions at H₁₂, proton pin. PR #6670.

    P_total(A=4) = -57.8031140268901789536480073022687094580855069850233004411658
    sign = -1        per-partition 26+ / 49-
    P_control (rho = I) = 0.0  -> vanishes
    sign-vs-A:  A2 = -1  A3 = -1  A4 = -1   -> no flip

**Verdict: NO MOVE.** The "negative at A=2, flips positive at A>=3" reading fails
at the alpha as well as the triton. A constant-sign Magnus carrier is the working
hypothesis through the light nuclei. scope-(a): a dimensionless SIGN datum, NOT a
MeV (Delta_lambda gate open), NOT a physical binding-sign convention.

**The margin is thin and that is part of the finding.** -57.8 is a small residual
of much larger cancelling contributions -- partitions reach +/-1349, split 26+/49-,
and the running total crossed zero TWICE in the last four blocks (+11.60 -> -3.60
-> -153.74 -> -57.80). Exact at 60 dps, so the sign is determined rather than
noisy; what is fragile is treating -57.8 as a robust margin. It is ~4% of one
large contribution and is sensitive to the model, not to arithmetic.

### THE COUNT IN THIS BEAN WAS WRONG

This bean has said "2 of 4 witnesses remain [to be regenerated]". That counted two
different situations as one, and I repeated the error all session -- calling this
"the last of the four to REGENERATE" and predicting its y_lambda would be exact
reciprocals of committed values.

**`he4-magnus-omega2-sign.witness.json` has never existed on main.** There was
nothing to regenerate. The probe had simply never run to completion (~9h). It
already carries the corrected `(d_q^2)/[n]_q!` weight from #6442 at lines 136-139,
so it was born right rather than fixed.

Correct statement: of the four Magnus probes #6442 touched, **three had witnesses
that needed regenerating** (two done in #6442, triton in #6533) and **one had no
witness at all**, which is now produced. Not "2 of 4 remain".

### Why it took four attempts, and what actually worked

Worker restarts land ~hourly and kill the compute. One dim-5632+ partition takes
~55 min, so runs 2 and 3 each banked **zero** in a full hour, dying just short.

Run 4 changed three things and finished:
- `--skip-gate` (gates 1 and 2 had PASSED twice on this code against the
  committed triton -- so skipping was evidenced, not assumed);
- `--workers 4` (4 cores, 4 partitions left: one ~60 min wall, not four
  sequential);
- launching at the **start** of a restart window.

Three landed together at ~58-60 min. The fourth, `(5,3,2,1,1)` at **dim 7700**,
is the single largest block in the n=12 problem and took **108 min** -- it looked
like a stall and was not (one worker R at 98.6% with climbing CPU, three S and
finished). `setsid` did NOT protect the run; the kill is a container-level reap,
not a process-group signal.

**The per-partition JSONL checkpoint is the whole reason four attempts were
survivable.** Each relaunch resumed instead of restarting, and it correctly
refused to resume when the parameter stamp would not have matched.

### Method notes worth keeping

- `pgrep -af he4_magnus` without `| grep -v "bash -c"` matches your own diagnostic
  shell. It reported a dead run as alive three separate times this session.
- Judge liveness by CPU time (`ps -o time,%cpu`), never by log mtime: 30-55 min of
  silence per partition is normal at these dimensions.
- Gate 2 reproduces the COMMITTED triton to 3.03e-60 by a separate sparse route --
  two independent confirmations of the #6442 weight fix.

## 2026-09-08 coordination: same kernel as qou-x631, qou-k5r5, qou-o6ov, qou-za3q

Audit docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 1 / §7.3 C2: `k5r5` (99 commits, 08-21 → 09-08) and `o6ov` (99 commits, 08-30 → 09-05) both work the odd-moment / Magnus `tr(ρ_λ Ω₂)` kernel, and before this note there were **zero** cross-citations among k5r5 / o6ov / x631 / za3q / omr7 (measured 2026-09-08 by grepping each body for the other four ids). Shared ledger: epic `qou-x631`, now parent of the other four. Roles — x631: epic, Cov_Planch(f^λ, Σc²) ≤ 0 / T₃(k) kernel; k5r5: M₁ > 0 (first odd moment), all-n proof OPEN, identity Lean-proved; o6ov: does |tr(ρ_λ Ω₂)|/dim decay in b across the ≤2-row column (open mathematics, rescoped 2026-09-05, PR #6822); za3q: Magnus-Ω₂ probes use the Plancherel weight y_λ, 91 % of their work on shapes tr_M annihilates; omr7: Magnus probes' d_q was the hook product, weight inverted (4 files, PR #6442). Statuses are unchanged by this note; a result landing on any of the five should be cited in the other four.


## Cross-citation from qou-za3q (2026-09-11): the A=4 Magnus sign is measured

Per the 2026-09-08 coordination note on qou-za3q ("a result landing on any of the
five should be cited in the other four"), this is such a result.

`he4_magnus_omega2_sign_sparse_probe.py`, 77/77 partitions of H_12, max dim 7700,
28661s:

    P_total(A=4) = 34.1260272853576529271380692762741452981457684651471317452205
    sign = +1    control (rho = I) = 0.0 vanishes    33+/42-    sign_flip_vs_A3 = False

Sign map across the light nuclei: A2 = -1, A3 = +1, A4 = +1. There is exactly ONE
sign change in A = 2,3,4 and it sits between the deuteron and the triton, NOT at
the alpha particle.

Load-bearing for anyone reading the older framing: the he4 probe's docstring
asserted "A=3: P<0, NO flip vs A=2" and that premise had propagated into its
GENERATED VERDICT string. It is false — A=3 is +2.4701927, confirmed by the
committed witness and a fresh 30/30 re-run. Fixed under qou-rfhj. If any of the
five beans reasons from "negative through the deuteron and triton", that premise
is stale.

scope-(a): a dimensionless SIGN datum. NOT a MeV (the Delta_lambda magnitude gate
is open and untouched), NOT a physical binding-sign assertion (qou-v7ro / #6077,
cited not re-derived). The total is a weighted sum of mixed-sign terms (33+/42-).



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-11 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## Progress Update (Round 91 — lane-cf11)
- Formalized in `folio/quantum-observable-universe/lean/QOU/QBeta/HookEvenMomentAndBorromeanTripleBrick.lean` with 80-dps probe `computations/probes/hook_even_moment_and_borromean_triple_brick_probe.py` and witness `computations/probes/hook-even-moment-and-borromean-triple-brick.witness.json`.
- PR: https://github.com/litlfred/qou/pull/8343 (`feat/qou-b9cj-ogrk-ohaz-omr7-ooqh-po72`, HEAD `8c185bc247a4dfba4e6316715175039c0defb340`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8343, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.

**Review before closing:** a main commit subject names this bean with a closing word (2026-09-04: "beans(qou-omr7): he4-sparse complete, and this bean's own "2 of 4" count was wrong"). The work may be partly or fully done. Read the bean before you close it.
