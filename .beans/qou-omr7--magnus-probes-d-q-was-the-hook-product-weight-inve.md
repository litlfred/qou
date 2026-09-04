---
# qou-omr7
title: 'Magnus probes: d_q was the hook product, weight inverted (4 files)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T04:40:28Z
updated_at: 2026-09-03T14:56:20Z
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
