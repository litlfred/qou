---
# qou-li9a
title: chi_at_q0_via_matrix_m_mpfr prints n_match/n_total and exits 0 regardless — the qou-7bv5 silence, unfixed
status: in-progress
type: bug
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-08T05:02:18Z
updated_at: 2026-11-16T20:10:00Z
parent: qou-trd0
---

Split out of `qou-7bv5` on 2026-09-08. That bean's *artifact* defect is fixed
and it is being closed; **this is the part it called the important one and it is
still live on `main`**:

> *"The severity is the silence. The producer prints 0/11 and exits 0, so the
> harness records ok. Two independent detectors — this cross-check and
> `qou-9d6h`'s probe — both reported real defects into a channel nothing reads.
> That is the pattern worth fixing generally, not the deuteron number."*

## The live code

`computations/chi_at_q0_via_matrix_m_mpfr.py`, lines 503-523. `n_match` is
computed correctly against a 1e-(dps-5) tolerance and then **only printed**:

```python
        n_match = 0
        …
            if abs(chi_mpf - chi_rust) < tol:
                n_match += 1
        …
        print(f"  {'':>10}     cross-check vs chi_q_via_gp at q_0: "
              f"{n_match}/{n_total} match (tol 1e-{args.dps-5}), "
              f"{n_skipped} skipped ({cap_note})")

    return 0 if last_record is not None else 1
```

The return value depends on whether a record was *produced*, never on whether it
was *right*. `0/11 match` and `11/11 match` both exit 0. That is what let the
stale deuteron cache sit unnoticed while the producer's own detector was
printing the defect on every run.

## There is a precedent fix in the corpus — follow it, do not invent one

**`qou-9d6h` is `completed`** and is the same defect one producer over:
*"D3: `deuteron_tower_fusion_frame_probe` exits 0 while `allPassed` is False."*
Read what it did before writing anything here; the two should end up behaving
the same way, exactly as the `qou-7bv5` resume guard was *ported* from
`chi_at_q0_via_hoefsmit_mpfr` rather than reinvented.

## Why this was NOT fixed inline while it was found

Changing the exit code is a **contract change on every caller**, not a local
repair: any sweep or harness that runs this producer would begin failing on a
mismatch it currently tolerates, and how many such callers exist is unmeasured.
AGENTS.md's ask-first override (2026-09-07) does not exempt it — it neither
increases precision nor is fixed by a corpus artifact — and the taxonomy
records a near-miss of exactly this shape, a contract change that *"would have
turned 29 correct records into violations."*

## Next honest step

1. Read `qou-9d6h`'s fix and mirror its shape.
2. **Measure the caller set first** — grep for invocations of this producer in
   sweeps, `q0_repin_sweep.py`, and the witness-pipeline paths, and say how many
   would newly fail. That number is what makes this decidable.
3. Then put it to the owner with that number, or apply it if the caller set
   turns out to be empty.

Do **not** make the exit code conditional on a *widened* tolerance to keep
current callers green — that is the baseline-widening move the precision
discipline forbids, one layer up.


## Round 48 Execution Update (2026-11-16, PR #8161)

- **PR:** https://github.com/litlfred/qou/pull/8161 (`38bc15fe7214bb6951d6acb18fa8c8d7d32d5225`)
- **Action taken:**
  - Gated the exit code of `computations/chi_at_q0_via_matrix_m_mpfr.py` on `n_match == n_total` across all cross-checked atoms (and on atom build errors) via `any_mismatch`, so a cross-check mismatch against `chi_rust_at_q_mpf` exits `1` instead of `0`.
  - Updated `computations/audits/silent_self_check_audit.py` `REPAIRED` table and verified `silent_self_check_audit.py` reports `chi_at_q0_via_matrix_m_mpfr.py` as fixed.
- **Status:** Kept `in-progress` pending PR #8161 merge and owner review.
